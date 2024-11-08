from django import forms
from reviews.models import Review

class ReviewForm(forms.ModelForm):

    # name = forms.CharField(max_length=25)
    # email = forms.EmailField()
    # review=forms.CharField(widget=forms.Textarea)
    # rating = forms.IntegerField(min_value=1,max_value=10)

    class Meta:
        model=Review
        fields=['name','email','rating','review']
        widgets = {
            'ratings':forms.NumberInput(attrs={'min':1,'max':10})
        }