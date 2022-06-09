from select import select
from unittest import TestCase, result


class TestRestAdapter(TestCase):
    def setUp(self):
        self.rest_adapter = RestAdapter
        self.response = requests.Response()

    def test__do_good_request_returns_result(self):
        # Arrange
        self.response.status_code = 200
        self.response._content = "{}".encode()
        with mock.patch("request.request", return_value=self.response):
            result = self.rest_adapter._de("GET", "")
            self.assertIsInstance(result, Result)

    def test__do(self):
        self.fail()

    def test_get(self):
        self.fail()

    def test_post(self):
        self.fail()

    def test_delete(self):
        self.fail()

    def test_fetch_data(self):
        self.fail()
