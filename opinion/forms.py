from django.forms import ModelForm

from captcha.fields import CaptchaField

from .models import OpinionBox, AnswerBox


class OpinionForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = OpinionBox
        fields = ['opinion_text', 'opinion_photo']


class AnswerForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = AnswerBox
        fields = ['answer_text', 'answer_photo']
