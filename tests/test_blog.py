import unittest
from app.models import Blog, User
from app import db
class BlogModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the blog class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Joe = User(username='Joe',password='joej', email='test@mail.com')
        self.new_blog = Blog(title='Test', blog='Test if blog data is working!', user=self.user_Joe)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.blog, 'Test if blog data is working!')
        self.assertEquals(self.new_blog.user, self.user_Joe)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)