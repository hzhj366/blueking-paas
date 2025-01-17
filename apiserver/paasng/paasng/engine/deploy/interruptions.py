from bkpaas_auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _

from paasng.engine.constants import JobStatus
from paasng.engine.deploy.bg_build.bg_build import interrupt_build_proc
from paasng.engine.exceptions import DeployInterruptionFailed
from paasng.engine.models.deployment import Deployment


def interrupt_deployment(deployment: Deployment, user: User):
    """Interrupt a deployment, this method does not guarantee that the deployment will be interrupted
    immediately(or in a few seconds). It will try to do following things:

    - When in "build" phase: this method will try to stop the build process by calling engine service
    - When in "release" phase: this method will set a flag value and abort the polling process of
      current release

    After finished doing above things, the deployment process MIGHT be stopped if anything goes OK, while
    the interruption may have no effects at all if the deployment was not in the right status.

    :param deployment: Deployment object to interrupt
    :param user: User who invoked interruption
    :raises: DeployInterruptionFailed
    """
    if deployment.operator != user.pk:
        raise DeployInterruptionFailed(_('无法中断由他人发起的部署'))
    if deployment.status in JobStatus.get_finished_states():
        raise DeployInterruptionFailed(_('无法中断，部署已处于结束状态'))

    now = timezone.now()
    deployment.build_int_requested_at = now
    deployment.release_int_requested_at = now
    deployment.save(update_fields=['build_int_requested_at', 'release_int_requested_at', 'updated'])

    if deployment.build_process_id:
        try:
            interrupt_build_proc(deployment.build_process_id)
        except DeployInterruptionFailed:
            # This exception means that build has not been started yet, transform
            # the error message.
            raise DeployInterruptionFailed('任务正处于预备执行状态，无法中断，请稍候重试')
