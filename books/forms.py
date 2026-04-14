from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "reviews", "rating"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Book title"}),
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "Author name"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Book description"}),
            "reviews": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Reader reviews (optional)"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 5, "step": 0.1}),
        }


class QuestionForm(forms.Form):
    query = forms.CharField(
        label="Your Question",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Ask anything about books, e.g. 'Recommend a mystery novel set in India'",
        }),
    )
