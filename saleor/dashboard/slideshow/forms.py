from django import forms

from ...slideshow.models import Slideshow

class SlideshowForm(forms.ModelForm):
    class Meta:
        model = Slideshow
        fields = ('content', 'image', )