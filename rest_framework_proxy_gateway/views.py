"""
Extend the django-rest-framework-proxy ProxyView class
to create views that are limited in their use of http verbs.

Create your ProxyView views like this:
from rest_framework_proxy_gateway.views import ProxyViewPostOnly
class EventCreateView(ProxyViewPostOnly):
    source = 'api/events'

"""

from rest_framework_proxy.views import ProxyView
from .mixins import (
    BlockDelete,
    BlockGet,
    BlockOptions,
    BlockPatch,
    BlockPost,
    BlockPut,
)


class ProxyViewDeleteOnly(
    BlockGet,
    BlockOptions,
    BlockPatch,
    BlockPost,
    BlockPut,
    ProxyView):
    """Only allow the DELETE method."""
    pass


class ProxyViewGetOnly(
    BlockDelete,
    BlockOptions,
    BlockPatch,
    BlockPost,
    BlockPut, 
    ProxyView):
    """Only allow the GET method."""
    pass


class ProxyViewGetPost(
    BlockDelete,
    BlockOptions,
    BlockPatch,
    BlockPut,
    ProxyView):
    """Only allow the GET and POST methods."""
    pass


class ProxyViewOptionsOnly(
    BlockDelete,
    BlockGet,
    BlockPatch,
    BlockPost,
    BlockPut,
    ProxyView):
    """Only allow the OPTIONS method."""
    pass


class ProxyViewPatchOnly(
    BlockDelete,
    BlockGet,
    BlockOptions,
    BlockPost,
    BlockPut,
    ProxyView):
    """Only allow the PATCH method."""
    pass


class ProxyViewPostOnly(
    BlockDelete,
    BlockGet,
    BlockOptions,
    BlockPatch,
    BlockPut,
    ProxyView):
    """Only allow the POST method."""
    pass


class ProxyViewPutOnly(
    BlockDelete,
    BlockGet,
    BlockOptions,
    BlockPatch,
    BlockPost,
    ProxyView):
    """Only allow the PUT method."""
    pass
