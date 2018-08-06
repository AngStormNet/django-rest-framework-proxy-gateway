from rest_framework.status import HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.test import APITestCase
from rest_framework_proxy_gateway.views import (
    ProxyViewDeleteOnly,
    ProxyViewGetOnly,
    ProxyViewGetPost,
    ProxyViewOptionsOnly,
    ProxyViewPatchOnly,
    ProxyViewPutOnly,
    ProxyViewPostOnly,
)


class ProxyViewDeleteOnlyTest(APITestCase):
    """Test the HTTP methods of the ProxyViewDeleteOnly view."""

    class TestView(ProxyViewDeleteOnly):
        source = 'api/test'

    def setUp(self):
        self.view = self.TestView()

    def test_blocked_methods(self):
        """Verify the blocked methods are not allowed to be executed."""

        response = self.view.get(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.options(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.patch(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.post(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.put(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_allowed_method(self):
        """Verify the DELETE method is allowed to be executed, but throws an error."""
        with self.assertRaises(AttributeError):
            self.view.delete(request=None)


class ProxyViewGetOnlyTest(APITestCase):
    """Test the HTTP methods of the ProxyViewGetOnly view."""

    class TestView(ProxyViewGetOnly):
        source = 'api/test'

    def setUp(self):
        self.view = self.TestView()

    def test_blocked_methods(self):
        """Verify the blocked methods are not allowed to be executed."""

        response = self.view.delete(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.options(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.patch(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.post(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.put(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_allowed_method(self):
        """Verify the GET method is allowed to be executed, but throws an error."""
        with self.assertRaises(AttributeError):
            self.view.get(request=None)


class ProxyViewGetPostTest(APITestCase):
    """Test the HTTP methods of the ProxyViewGetPost view."""

    class TestView(ProxyViewGetPost):
        source = 'api/test'

    def setUp(self):
        self.view = self.TestView()

    def test_blocked_methods(self):
        """Verify the blocked methods are not allowed to be executed."""

        response = self.view.delete(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.options(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.patch(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.put(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_allowed_methods(self):
        """Verify the GET and POST methods are allowed to be executed,
        but throws an error.
        """
        with self.assertRaises(AttributeError):
            self.view.get(request=None)

        with self.assertRaises(AttributeError):
            self.view.post(request=None)


class ProxyViewOptionsOnlyTest(APITestCase):
    """Test the HTTP methods of the ProxyViewOptionsOnly view."""

    class TestView(ProxyViewOptionsOnly):
        source = 'api/test'

    def setUp(self):
        self.view = self.TestView()

    def test_blocked_methods(self):
        """Verify the blocked methods are not allowed to be executed."""

        response = self.view.delete(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.get(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.patch(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.post(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.put(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_allowed_method(self):
        """Verify the OPTIONS method is allowed to be executed, but throws an error."""
        response = self.view.options(request=None)
        self.assertEqual(response.status_code, HTTP_200_OK)


class ProxyViewPatchOnlyTest(APITestCase):
    """Test the HTTP methods of the ProxyViewPatchOnly view."""

    class TestView(ProxyViewPatchOnly):
        source = 'api/test'

    def setUp(self):
        self.view = self.TestView()

    def test_blocked_methods(self):
        """Verify the blocked methods are not allowed to be executed."""

        response = self.view.delete(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.get(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.options(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.post(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.put(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_allowed_method(self):
        """Verify the PATCH method is allowed to be executed, but throws an error."""
        with self.assertRaises(AttributeError):
            self.view.patch(request=None)


class ProxyViewPostOnlyTest(APITestCase):
    """Test the HTTP methods of the ProxyViewPostOnly view."""

    class TestView(ProxyViewPostOnly):
        source = 'api/test'

    def setUp(self):
        self.view = self.TestView()

    def test_blocked_methods(self):
        """Verify the blocked methods are not allowed to be executed."""

        response = self.view.delete(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.get(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.options(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.patch(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.put(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_allowed_method(self):
        """Verify the POST method is allowed to be executed, but throws an error."""
        with self.assertRaises(AttributeError):
            self.view.post(request=None)


class ProxyViewPutOnlyTest(APITestCase):
    """Test the HTTP methods of the ProxyViewPutOnly view."""

    class TestView(ProxyViewPutOnly):
        source = 'api/test'

    def setUp(self):
        self.view = self.TestView()

    def test_blocked_methods(self):
        """Verify the blocked methods are not allowed to be executed."""

        response = self.view.delete(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.get(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.options(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.patch(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        response = self.view.post(request=None)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_allowed_method(self):
        """Verify the PUT method is allowed to be executed, but throws an error."""
        with self.assertRaises(AttributeError):
            self.view.put(request=None)


