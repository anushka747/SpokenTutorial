from . import models
from django.forms import ModelForm

class UploadTranscriptForm(ModelForm):
    class Meta:
        model = models.TranscriptsModel
        fields = ('transcript', 'gender')

class UploadVideosForm(ModelForm):
    class Meta:
        model = models.MergeVideosModel
        fields = ('video', 'audio')