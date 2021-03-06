# coding: utf-8

from django.db import models
from django.utils.translation import ugettext as _

from colorfield.fields import ColorField


class IssueStatus(models.Model):
    COLOR_DEFAULT = '#818A91'

    STATUS_NEW = 'new'
    STATUS_AUTO_VERIFICATION = 'auto_verification'
    STATUS_NEED_INFO = 'need_info'
    HIDDEN_STATUSES = {STATUS_NEW: 1,
                       STATUS_AUTO_VERIFICATION: 2,
                       STATUS_NEED_INFO: 6}

    STATUS_REWORK = 'rework'
    STATUS_VERIFICATION = 'verification'
    STATUS_ACCEPTED = 'accepted'
    STATUS_SEMINAR = 'seminar'

    ISSUE_STATUSES = (
        (STATUS_REWORK, _(STATUS_REWORK)),
        (STATUS_VERIFICATION, _(STATUS_VERIFICATION)),
        (STATUS_ACCEPTED, _(STATUS_ACCEPTED)),
        (STATUS_SEMINAR, _(STATUS_SEMINAR))
    )

    name = models.CharField(max_length=191, db_index=True, null=False, blank=False)
    tag = models.CharField(max_length=191, db_index=False, null=True, blank=True, choices=ISSUE_STATUSES)
    color = ColorField(default=COLOR_DEFAULT)

    hidden = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{0}'.format(self.name)


class IssueStatusSystem(models.Model):
    name = models.CharField(max_length=191, db_index=False, null=False, blank=False)
    statuses = models.ManyToManyField(IssueStatus, null=True, blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)
