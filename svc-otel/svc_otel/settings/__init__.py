"""
Django settings for svc_otel project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import logging

import pymysql
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from .default import *  # isort:skip

pymysql.install_as_MySQLdb()
# Patch version info to forcely pass Django client check
setattr(pymysql, "version_info", (1, 4, 2, "final", 0))


# 接入 sentry
# All of this is already happening by default!
sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR,  # Capture info and above as breadcrumbs  # Send errors as events
)

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration(), sentry_logging],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )

STATIC_ROOT = "staticfiles"

LOGGING = get_logging_config(LOGGING_LEVEL)

ALLOWED_HOSTS = ["*"]