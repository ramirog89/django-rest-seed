# django url handler
from django.urls import include, path

# swagger views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# rest api features
from rest_framework import routers, permissions

# rest jwt token handlers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 

# application views
from src.app import views

# schema for swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Rest API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Register routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Url patterns registered in the application
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('posts', views.PostView.as_view({'get': 'list'}), name='posts_list'),
    path('posts/create', views.PostView.as_view({'create': 'create'}), name='posts_create'),
    path('posts/update', views.PostView.as_view({'update': 'update'}), name='posts_update'),
    path('posts/delete', views.PostView.as_view({'delete': 'delete'}), name='posts_delete'),
]