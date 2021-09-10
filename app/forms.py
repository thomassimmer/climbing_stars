from django import forms

from .models import Path, Comment, Image


class PathForm(forms.ModelForm):

    class Meta:
        model = Path
        fields = [
            'name',
            'description'
        ]

    name = forms.CharField(
        label='Nom de la voie *:',
        widget=forms.TextInput(
            attrs={"placeholder": "", "class": "form-control", "id": "pathName"}),
        error_messages={
            "required": "Le nom de la voie est requis.",
            "max_length": "Le nom de la voie doit être compris entre 1 et 200 caractères.",
            "min_length": "Le nom de la voie doit être compris entre 1 et 200 caractères."
    })

    description = forms.CharField(label='Description *:', widget=forms.Textarea(
        attrs={"class": "form-control", "id": "description", "rows": 3}),
        error_messages={
            "required": "Une description est requise.",
            "max_length": "La taille de la description doit être comprise entre 1 et 2000 caractères.",
            "min_length": "La taille de la description doit être comprise entre 1 et 2000 caractères."
    })


# This form includes images, to check them all together during the creation of a new path.
# This is needed because a path may have any number of images. Thus, images must have their own model.
class PathFormWithImages(PathForm):
    
    class Meta(PathForm.Meta):
        fields = PathForm.Meta.fields + ['images',]
    
    images = forms.FileField(label='SELECTIONNER UNE / DES PHOTOS *:', widget=forms.ClearableFileInput(
        attrs={"class": "hide-input-file", "id": "imageUploader", "rows": 3, "multiple": True}),
        error_messages={
            "required": "Une image est requise.",
            "invalid": "L'image est invalide.",
            "missing": "Une image est requise.",
            "empty": "Une image est requise.",
            "invalid_image" : "L'image est invalide."
    })


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'author',
            'note',
            'path',
            'comment'
        ]

    author = forms.CharField(
        label='Auteur *:',
        widget=forms.TextInput(
            attrs={"placeholder": "", "class": "form-control", "id": "author"}),
        error_messages={
            "required": "Le nom de l'auteur est requis.",
            "max_length": "Le nom de l'auteur doit être compris entre 1 et 200 caractères.",
            "min_length": "Le nom de l'auteur doit être compris entre 1 et 200 caractères."
        })

    note = forms.IntegerField(max_value=10,
                              min_value=0,
                              label='Note *:',
                              widget=forms.TextInput(
                                  attrs={"placeholder": "/10",  "class": "form-control", "id": "noteInput"}),
                              error_messages={
                                  "required": "Une note sur 10 est requise.",
                                  "invalid": "La note est invalide.",
                                  "max_value": "La note doit être comprise entre 0 et 10.",
                                  "min_value": "La note doit être comprise entre 0 et 10."
                              })

    comment = forms.CharField(label='Commentaire *:', widget=forms.Textarea(
        attrs={"class": "form-control", "id": "comment", "rows": 3}),
        error_messages={
            "required": "Un commentaire est requis.",
            "max_length": "Le commentaire doit être compris entre 1 et 2000 caractères.",
            "min_length": "Le commentaire doit être compris entre 1 et 2000 caractères."
    })

    path = forms.ModelChoiceField(
        queryset=Path.objects.all(), widget=forms.HiddenInput())

