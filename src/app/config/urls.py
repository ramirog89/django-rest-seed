# django url handler
from django.urls import include, path, re_path

# swagger views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# rest api features
from rest_framework import routers, permissions

# rest jwt token handlers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView 

# application views
from src.app import controllers

# schema for swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Rest API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   url="http://localhost:7000/api/",
   urlconf="src.app.config.urls"
)

# Register routers
router = routers.DefaultRouter()

# Url patterns registered in the application
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/auth/login', controllers.AuthenticationController.as_view({'post' : 'login'}), name='auth_login'),
    path('api/auth/logout', controllers.AuthenticationController.as_view({'post': 'logout'}), name='auth_logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/account/', controllers.AccountController.list, name='account_list'),
    path('api/account/create', controllers.AccountController.create, name='account_create'),
    path('api/account/update', controllers.AccountController.update, name='account_update'),
    path('api/account/delete', controllers.AccountController.delete, name='account_delete'),
    path('api/account/special-endpoint', controllers.AccountController.someBusinessLogicEndpoint, name='account_special_endpoint'),
]