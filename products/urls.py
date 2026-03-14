from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, CategoryViewSet

router = SimpleRouter()
router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = router.urls
