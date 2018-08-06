# django-rest-framework-proxy-gateway
Extends django-rest-framework-proxy, which entends django-rest-framework.

This package extends the ProxyView class to create views that have limited access to the HTTP verbs DELETE, GET, OPTIONS, PATCH, POST, and PUT.

* $ pip install django-rest-framework-proxy-gateway


# Views
Extend these gateway views to create your application views.
* ProxyViewDeleteOnly
* ProxyViewGetOnly
* ProxyViewGetPost
* ProxyViewOptionsOnly
* ProxyViewPatchOnly
* ProxyViewPostOnly
* ProxyViewPutOnly

```from rest_framework_proxy_gateway.views import ProxyViewPostOnly

class MyPostOnlyView(ProxyViewPostOnly):
    source = 'api/objects'
```

# Mixins
Use these gateway mixins to create your custom application views, if the provided views are not sufficient.
* BlockDelete
* BlockGet
* BlockOptions
* BlockPatch
* BlockPost
* BlockPut

```from rest_framework_proxy.views import ProxyView
from rest_framework_proxy_gateway.mixins import BlockDelete, BlockOptions

class MyView(BlockDelete, BlockOptions, ProxyView):
```

### The ProxyView class must be last in the class list.
