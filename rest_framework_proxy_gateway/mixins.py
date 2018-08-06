"""
Mixins to modify the ProxyView from the rest_framework_proxy package.
The mixin classes need to be listed before the ProxyView class, like this:
from rest_framework_proxy_gateway.mixins import (
    BlockDelete,
    BlockOptions,
    BlockPatch,
    BlockPost,
    BlockPut,
)

class AllowGetOnly(
    BlockDelete,
    BlockOptions,
    BlockPatch,
    BlockPost,
    BlockPut,
    ProxyView):
    
"""

from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.response import Response


class BlockDelete():
    """Block the HTTP DELETE method. Return HTTP 405."""
    def delete(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


class BlockGet():
    """Block the HTTP GET method. Return HTTP 405."""
    def get(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


class BlockOptions():
    """Block the HTTP OPTIONS method. Return HTTP 405."""
    def options(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


class BlockPatch():
    """Block the HTTP PATCH method. Return HTTP 405."""
    def patch(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


class BlockPost():
    """Block the HTTP POST method. Return HTTP 405."""
    def post(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


class BlockPut():
    """Block the HTTP PUT method. Return HTTP 405."""
    def put(self, request, *args, **kwargs):
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)

