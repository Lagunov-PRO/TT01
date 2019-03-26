import unittest
from app import app


class ProjectsTestCase(unittest.TestCase):
    def test_get_posts(self):
        tester = app.test_client(self)
        response = tester.get('/api/projects', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
