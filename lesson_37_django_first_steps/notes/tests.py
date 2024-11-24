from datetime import datetime, timezone
from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from notes.models import Category, Note


class TestViews(TestCase):
    def test_note_create_with_correct_data_302(self):
        # Arrange
        note_create_url = reverse('notes:note_create')
        category1 = Category.objects.create(title='Category 1')
        data = {
            "title": "title",
            "text": "text",
            "author": "author",
            "category": category1.id,
            "reminder": "2024-10-26 17:10:25"
        }

        # Act
        response = self.client.post(note_create_url, data)

        # Assert
        note_list_url = reverse('notes:note_list')
        self.assertRedirects(response, note_list_url, status_code=HTTPStatus.FOUND,
                             target_status_code=HTTPStatus.OK, fetch_redirect_response=True)
        note = Note.objects.filter(title=data["title"])
        self.assertEqual(note.count(), 1)
        self.assertEqual(note[0].title, "title")
        self.assertEqual(note[0].text, "text")
        self.assertEqual(note[0].author, "author")
        self.assertEqual(note[0].reminder, datetime(2024, 10, 26, 17, 10, 25, tzinfo=timezone.utc))
        self.assertEqual(note[0].category, category1)

    def test_note_create_with_incorrect_data_400(self):
        # Arrange
        note_create_url = reverse('notes:note_create')
        data = {
            "title": "title",
            "text": "text",
            "author": "author",
            "category": "incorrect_category",
            "reminder": "2024-10-26 17:10:25"
        }

        # Act
        response = self.client.post(note_create_url, data)

        # Assert
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_note_edit_with_not_existing_note_404(self):
        # Arrange
        invalid_note_id = 999
        note_edit_url = reverse('notes:note_edit', kwargs={'pk': invalid_note_id})
        data = {
            "title": "title",
            "text": "text",
            "author": "author",
            "category": "category",
            "reminder": "2024-10-26 17:10:25"
        }

        # Act
        response = self.client.post(note_edit_url, data)

        # Assert
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_note_edit_with_correct_data_302(self):
        # Arrange
        category1 = Category.objects.create(title='Category 1')
        note = Note.objects.create(title="title", text="text", author="author", category=category1, )
        note_edit_url = reverse('notes:note_edit', kwargs={'pk': note.id})
        data = {
            "title": "new_title",
            "text": "new_text",
            "author": "new_author",
            "category": category1.id,
            "reminder": "2021-10-26 17:10:25"
        }

        # Act
        response = self.client.post(note_edit_url, data)

        # Assert
        note_list_url = reverse('notes:note_list')
        self.assertRedirects(response, note_list_url, status_code=HTTPStatus.FOUND,
                             target_status_code=HTTPStatus.OK, fetch_redirect_response=True)
        note = Note.objects.filter(title=data["title"])
        self.assertEqual(note.count(), 1)
        self.assertEqual(note[0].title, "new_title")
        self.assertEqual(note[0].text, "new_text")
        self.assertEqual(note[0].author, "new_author")
        self.assertEqual(note[0].reminder, datetime(2021, 10, 26, 17, 10, 25, tzinfo=timezone.utc))
        self.assertEqual(note[0].category, category1)
