import unittest
from unittest import mock
from unittest.mock import MagicMock, patch

# from app import app
# from app.models import Project
# from app.projects import get_projects
from app import models, projects, app


class ProjectsTestCase(unittest.TestCase):
    mock_data_good = {"name": "testproj"}
    mock_data_bad = []

    def test_get_projects_response(self):
        tester = app.test_client(self)
        response = tester.get('/api/projects')
        self.assertEqual(response.status_code, 200)

    def test_add_noname_project_response(self):
        tester = app.test_client(self)
        response = tester.post('/api/projects')
        self.assertEqual(response.status_code, 400)

    @mock.patch('app.models.Project')
    @mock.patch('app.models.db')
    # @mock.patch('app.projects.get_projects')
    def test_get_projects(self, mock_1, mock_2):
        test = models.Project()
        test.name = 'name'
        print(test.validate_name())

    # def test_number(self):
    #
    #     self.assertEqual(response.status_code, 200)

    def test_mock_get_projects(self):
        with patch.object(projects, "get_projects", return_value=ProjectsTestCase.mock_data_good):
            result = projects.get_projects()
            self.assertTrue(result)
    #
    # @mock.patch('app.db', autospec=True)
    # def test_save(self, mock_dblib):
    #     writer = DBWriter()
    #     writer.save("Hello World")
    #     mock_dblib.return_value.commit.assert_called_with(writer,
    #                                                       "INSERT INTO mytable SET mystring = 'Hello World'")




if __name__ == '__main__':
    unittest.main()
