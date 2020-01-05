from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class PostTest(TestCase):
    
    @classmethod
    def setUpTestData(self):
        # create user
        user = User.objects.create_user(username='tester', password='1234')
        user.save()

        # create post
        post = Post.objects.create(title='Test Post', body='test post', author=user)
        post.save()
    
    def test_post_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEquals(author, 'tester')
        self.assertEquals(title, 'Test Post')
        self.assertEquals(body, 'test post')
