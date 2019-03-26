import unittest
from unittest import mock
from unittest.mock import MagicMock


from app import app
# from app.models import Project
from app.projects import get_projects


class ProjectsTestCase(unittest.TestCase):
    def test_get_projects_response(self):
        tester = app.test_client(self)
        response = tester.get('/api/projects')
        self.assertEqual(response.status_code, 200)

    @mock.patch('app.models.Project')
    @mock.patch('app.projects.get_projects')
    def test_get_projects(self, mock_1, mock_2):
        mock_1.return_value = MagicMock(status_code=500)
        mock_2.return_value = MagicMock(status_code=500)


    # def test_number(self):
    #
    #     self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
