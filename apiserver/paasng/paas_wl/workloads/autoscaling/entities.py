# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except
in compliance with the License. You may obtain a copy of the License at

    http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific language governing permissions and
limitations under the License.

We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""
from dataclasses import dataclass

from paas_wl.resources.base import crd
from paas_wl.resources.kube_res.base import AppEntity
from paas_wl.workloads.autoscaling.models import AutoscalingConfig, ScalingObjectRef
from paas_wl.workloads.autoscaling.serializers import ProcAutoscalingDeserializer, ProcAutoscalingSerializer


@dataclass
class ProcAutoscaling(AppEntity):
    """自动伸缩实例定义"""

    spec: AutoscalingConfig
    target_ref: ScalingObjectRef

    class Meta:
        kres_class = crd.GPA
        deserializer = ProcAutoscalingDeserializer
        serializer = ProcAutoscalingSerializer
