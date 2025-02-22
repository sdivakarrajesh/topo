from rest_framework.test import APITestCase
from django.urls import reverse

class AllDataAPITest(APITestCase):

    def test_get_memberships(self):
        url = reverse('all_data')  # Update with your actual API name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("activity_sessions", response.data)
        self.assertIn("quarterly_reports", response.data)
        self.assertIn("annual_summaries", response.data)
        self.assertIn("revenue_breakdowns", response.data)
        self.assertIn("companies", response.data)

    def test_data_by_type_view(self):
        file_types = ['csv', 'json', 'pptx', 'pdf']
        expected_keys = {
            'csv': ['activity_sessions'],
            'json': ['companies'],
            'pptx': ['annual_summaries', 'quarterly_reports'],
            'pdf': ['quarterly_reports']
        }
        for file_type in file_types:
            url = reverse('data_by_type', kwargs={'file_type': file_type})  # Update with your actual API name
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            data = response.data
            for key in expected_keys[file_type]:
                self.assertIn(key, data)