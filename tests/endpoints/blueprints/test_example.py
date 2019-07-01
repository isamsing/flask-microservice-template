import json
import unittest

from app import init


class ExampleEndpointTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.uri = "/example/"
        cls.app = init("testing").test_client()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get(self):
        response = self.app.get(self.uri, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {"arg": "test"}
        response = self.app.post(self.uri,
                                 data=json.dumps(data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.app.delete(self.uri, follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
