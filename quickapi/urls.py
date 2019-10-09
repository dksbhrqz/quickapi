from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'bills', views.BillViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'bills_products', views.BillProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]