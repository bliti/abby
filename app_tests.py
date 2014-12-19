import app
import unittest


class AppTestCase(unittest.TestCase):


    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
    

    def test_index_page(self):
        r = self.app.get('/')
        self.assertEquals('200 OK', r.status)
        self.assertTrue('Abby' in r.data)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()