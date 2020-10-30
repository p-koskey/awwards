from django.test import TestCase
from .models import Profile,Rate, Post


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='kayce', password='45rfvb')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='kayce')
        self.post = Post.objects.create( projectname='project', link='www.santorini.com', projectinfo='loremipsum',
                                        languages='ruby',posted='2020/12/2', picture='photo.jpg',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_post('project')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_post'project')
        self.assertTrue(len(post) < 1)


class RateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='kayce')
        self.post = Post.objects.create(projectname='project', link='www.santorini.com', projectinfo='loremipsum',
                                        languages='ruby',posted='2020/12/2', picture='photo.jpg',user=self.user)
        self.rate = Rate.objects.create(design=2, usability=5, content=5, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Rate))

    def test_save_rate(self):
        self.rate.save_rate()
        rate = Rate.objects.all()
        self.assertTrue(len(rate) > 0)

    def test_get_post_rates(self, id):
        self.rate.save()
        rate = Rate.get_ratings(post_id=id)
        self.assertTrue(len(rate) == 1)