from django import forms

class Myform(forms.Form):
    # text = forms.CharField(label='Text', max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    # textarea = forms.CharField(label='Entered texts', max_length=30,widget=forms.Textarea(attrs={'class':'form-control'}))
    title = forms.CharField(label='Title',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject Description', max_length=200,widget=forms.Textarea(attrs={'class':'form-control'}))