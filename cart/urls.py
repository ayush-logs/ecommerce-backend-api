from rest_framework.routers import SimpleRouter
from .views import CartViewSet, CartItemViewSet

router = SimpleRouter()
router.register(r"carts", CartViewSet)
router.register(r"cartitems", CartItemViewSet)

urlpatterns = router.urls
