# Name: Connor Warner
# Class: CIS 218
# Date: 1/24/24


from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomepageTest(SimpleTestCase):
    """Test home/resume page"""

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""

        responce = self.client.get("/")
        self.assertEqual(responce.status_code, 200)

    def test_url_available_by_name(self):
        """Test url available by name"""
        responce = self.client.get(reverse("home"))
        self.assertEqual(responce.status_code, 200)

    def test_template_name_correct(self):
        "Test template name correct"
        responce = self.client.get(reverse("home"))
        self.assertTemplateUsed(responce, "home.html")

    def test_template_content(self):
        """Test template content"""
        # responce = self.client.get(reverse("home"))
        # self.assertContains(responce, "TODO: Add content")
        pass


class ProjectspageTest(SimpleTestCase):
    """Test projects page"""

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""

        responce = self.client.get("/projects/")
        self.assertEqual(responce.status_code, 200)

    def test_url_available_by_name(self):
        """Test url available by name"""
        responce = self.client.get(reverse("projects"))
        self.assertEqual(responce.status_code, 200)

    def test_template_name_correct(self):
        "Test template name correct"
        responce = self.client.get(reverse("projects"))
        self.assertTemplateUsed(responce, "projects.html")

    def test_template_content(self):
        """Test template content"""
        # responce = self.client.get(reverse("projects"))
        # self.assertContains(responce, "TODO: Add content")
        pass


class ContactpageTest(SimpleTestCase):
    """Test projects page"""

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""

        responce = self.client.get("/contact/")
        self.assertEqual(responce.status_code, 200)

    def test_url_available_by_name(self):
        """Test url available by name"""
        responce = self.client.get(reverse("contact"))
        self.assertEqual(responce.status_code, 200)

    def test_template_name_correct(self):
        "Test template name correct"
        responce = self.client.get(reverse("contact"))
        self.assertTemplateUsed(responce, "contact.html")

    def test_template_content(self):
        """Test template content"""
        # responce = self.client.get(reverse("projects"))
        # self.assertContains(responce, "TODO: Add content")
        pass