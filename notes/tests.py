from django.test import TestCase
from django.shortcuts import reverse

class NotesListViews(TestCase):
    def test_note_list_views_in_browser(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    def test_name_urls_patterns(self):
        response = self.client.get(reverse('list views'))
        self.assertEqual(response.status_code, 200)
