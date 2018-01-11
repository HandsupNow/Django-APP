from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel


class OpinionBox(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'用户')
    opinion_text = models.TextField(max_length=500, verbose_name=u'意见')
    opinion_photo = models.ImageField(upload_to='opinion/', null=True, blank=True, verbose_name=u'截图')


class AnswerBox(TimeStampedModel):
    opinion_box = models.ForeignKey(OpinionBox)
    answer_text = models.TextField(max_length=500, verbose_name=u'回复')
    answer_photo = models.ImageField(upload_to='opinion/', null=True, blank=True, verbose_name=u'截图')
