from django.test import TestCase, Client

class Test_Cases(TestCase):
    def test_xml_url(self):
        self.client = Client()
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json_url(self):
        self.client = Client()
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def test_html_url(self):
        self.client = Client()
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)