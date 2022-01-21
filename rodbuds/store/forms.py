from django import forms

from .models import Product, Variation, ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
    # product = forms.ForeignKey(Product, on_delete=models.CASCADE)
    # user = forms.ForeignKey(Account, on_delete=models.CASCADE)
    # subject = forms.CharField(max_length=100, blank=True)
    # review = forms.TextField(max_length=500, blank=True)
    # rating = forms.FloatField()
    # ip = forms.CharField(max_length=20, blank=True)
    # status = forms.BooleanField(default=True)
    # created_at = forms.DateTimeField(auto_now_add=True)
    # updated_at = forms.DateTimeField(auto_now=True)