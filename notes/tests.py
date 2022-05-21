from django.test import TestCase

class NotesListViews(TestCase):
    def test_note_list_views_in_browser(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
