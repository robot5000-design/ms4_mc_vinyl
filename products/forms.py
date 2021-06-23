from django import forms
from django.forms import Textarea
from crispy_forms.bootstrap import InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from .widgets import CustomClearableFileInput
from .models import Product, Genre, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'artist',
            'title',
            'release_date',
            'sku',
            'price',
            'genre',
            'description',
            'album_format',
            'color',
            'image',
            'track_list',
            )

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        genres = Genre.objects.all()
        genres_friendly_names = [(genre.id, genre.get_friendly_name()) for genre in genres]
        self.fields['genre'].choices = genres_friendly_names
        for field_name, field in self.fields.items():
            if field_name == 'track_list':
                field.widget.attrs['class'] = 'my-2 mr-2 border-black rounded-0'
            else:
                field.widget.attrs['class'] = 'border-black rounded-0'


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = (
            'body',
            'review_rating',
        )
        widgets = {
            'body': Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'body',
            InlineRadios('review_rating')
        )
        self.fields['review_rating'].widget.attrs['required'] = True
        for field in self.fields:
            if field == 'body':
                self.fields[field].label = False
                self.fields[field].widget.attrs[
                    'placeholder'] = 'Write your review here...'
            elif field == 'review_rating':
                self.fields[field].label = "What's your rating?"
            self.fields[field].widget.attrs[
                'class'] = 'border-black rounded-0 profile-form-input'
