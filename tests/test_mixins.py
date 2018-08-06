from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework_proxy.views import ProxyView
from rest_framework_proxy_gateway.mixins import (
    BlockDelete,
    BlockGet,
    BlockOptions,
    BlockPatch,
    BlockPost,
    BlockPut,
)


class MixinTests(APITestCase):
    """Test the Block* mixin classes."""

    def test_block_delete(self):
        """Verify the BlockDelete mixin does block the DELETE method."""
        class TestProxyView(BlockDelete, ProxyView):
            source = 'api/test'

        response = TestProxyView().delete(request=None)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_block_get(self):
        """Verify the BlockGet mixin does block the GET method."""
        class TestProxyView(BlockGet, ProxyView):
            source = 'api/test'

        response = TestProxyView().get(request=None)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_block_options(self):
        """Verify the BlockOptions mixin does block the OPTIONS method."""
        class TestProxyView(BlockOptions, ProxyView):
            source = 'api/test'

        response = TestProxyView().options(request=None)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_block_patch(self):
        """Verify the BlockPatch mixin does block the PATCH method."""
        class TestProxyView(BlockPatch, ProxyView):
            source = 'api/test'

        response = TestProxyView().patch(request=None)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_block_post(self):
        """Verify the BlockPost mixin does block the POST method."""
        class TestProxyView(BlockPost, ProxyView):
            source = 'api/test'

        response = TestProxyView().post(request=None)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_block_put(self):
        """Verify the BlockPut mixin does block the PUT method."""
        class TestProxyView(BlockPut, ProxyView):
            source = 'api/test'

        response = TestProxyView().put(request=None)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_block_delete_patch_put(self):
        """Verify that combined mixins block the methods."""
        class TestProxyView(BlockDelete, BlockPatch, BlockPut, ProxyView):
            source = 'api/test'
        
        view = TestProxyView()

        response = view.delete(request=None)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
        response = view.patch(request=None)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
        response = view.put(request=None)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
