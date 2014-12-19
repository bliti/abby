import app
import unittest


class AppTestCase(unittest.TestCase):


    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
    

    def test_index_page(self):
        r = self.app.get('/')
        self.assertEquals('200 OK', r.status)
        self.assertTrue('WutBot' in r.data)


    def test_blog_redirect(self):
        r = self.app.get('/blog')
        self.assertEquals('302 FOUND', r.status)


    def test_twitter_redirect(self):
        r = self.app.get('/twitter')
        self.assertEquals('302 FOUND', r.status)

    
    def test_youtube_redirect(self):
        r = self.app.get('/youtube')
        self.assertEquals('302 FOUND', r.status)

    
    def test_store_redirect(self):
        r = self.app.get('/store')
        self.assertEquals('302 FOUND', r.status)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()