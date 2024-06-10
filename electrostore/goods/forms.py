from django import forms

from main.models import Review


class ReviewForm(forms):
    body = forms.CharField()

    class Meta:
        model = Review()
        fields = ["body"]
