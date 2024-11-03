from django import forms

class UploadFileForm(forms.Form):
    followers_file = forms.FileField(label='Unggah followers_1.json')
    following_file = forms.FileField(label='Unggah following.json')
