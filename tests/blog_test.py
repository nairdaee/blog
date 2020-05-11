import unittest
from app import db
from app.models import User

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.user = User(username='nairdaee', password='mutemuas2001',
                         email='etadriano2@gmail.com.com')
        self.new_comment = Comment(
            comment='comment', blog_id=1, user_id=self.user)
        self.new_blog = Blog(id=1, title="Blog", body='blog',
                               category='Interview', writer=self.user, comment=self.new_comment)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_variables(self):
        self.assertEquals(self.new_blog.id, 1)
        self.assertEquals(self.new_blog.title, 'Blog')
        self.assertEquals(self.new_blog.body, 'blogs')
        self.assertEquals(self.new_blog.category, "Anything")
        self.assertEquals(self.new_blog.writer, self.user)
        self.assertEquals(self.new_blog.comment, self.new_comment)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):

        self.new_pitch.save_blog()
        get_blogs = Blog.get_blogs(1)
        self.assertTrue(len(get_blogs) == 1)
