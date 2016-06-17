from django.test import TestCase, Client, override_settings

@override_settings(ROOT_URLCONF='webhook.urls')
class WebhookTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_webhook_response(self):
        """Webhook returns correct response"""
        response = self.client.post('/',
                {'foo': 'bar'},
                HTTP_X_GITHUB_EVENT='some event',
                )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['event'], 'some event')
