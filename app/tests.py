from django.urls.conf import path
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Path, Image, Comment
from .forms import PathForm, PathFormWithImages, CommentForm


# Just some quick important tests. TODO : Add more

def create_path(name, description):
    return Path.objects.create(name=name, description=description)
    
def create_image(path, image):
    return Image.objects.create(path=path, image=image)
    
def create_comment(author, note, comment, path):
    return Comment.objects.create(author=author, note=note, comment=comment, path=path)

class PathCreationTests(TestCase):
    def test_path_creation(self):
        """
        Test if the user can create a path and if he is redirected without problem to the detail page of that path.
        """
        
        # With a name and a description
        path_correct = create_path(name='Path 1', description="Description of the path")
        url = reverse('app:detail', args=(path_correct.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class FormTests(TestCase):
    def test_path_forms_without_image(self):
        """
        Test if user can create path without pictures
        """
        post_dict = {'name': 'Test name', 'description': 'Test Description'}
        file_dict = {'images': None}
        form = PathFormWithImages(post_dict, file_dict)
        self.assertFalse(form.is_valid())



    def test_path_forms_with_images(self):
        """
        Test if user can create path with pictures
        """
        upload_file = open('app/static/app/test_image.png', 'rb')
        post_dict = {'name': 'Test name', 'description': 'Test Description'}
        file_dict = {'images': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = PathFormWithImages(post_dict, file_dict)
        self.assertTrue(form.is_valid())


        

