from django.test import TestCase
from django.contrib.auth.models import User

from polling.models import Post  # add this import at the top

class PostTestCase(TestCase):
    # def setUp(self):
    #     self.user = User.objects.get(pk=1)

    # add this test method to the PostTestCase
    def test_string_representation(self):
        # Given: a title
        expected = "This is a title"

        # When: the post is created
        p1 = Post(title=expected)
        actual = str(p1)

        # Then: The class __str__ should be the title
        self.assertEqual(expected, actual)

