from django import forms

# Create your models here.


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    resource = forms.FileField()


#eof
