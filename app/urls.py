from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from app.controllers.auth_controller import RegisterController, LoginController
from app.controllers.document_controller import DocumentListCreateController, DocumentDetailController
from app.controllers.query_controller import QueryController, QueryHistoryController

urlpatterns = [
    # OpenAPI Schema, Swagger & ReDoc Documentation
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Auth endpoints
    path('auth/register/', RegisterController.as_view(), name='auth-register'),
    path('auth/login/', LoginController.as_view(), name='auth-login'),

    # Document endpoints
    path('documents/', DocumentListCreateController.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentDetailController.as_view(), name='document-detail'),

    # Query endpoints
    path('query/', QueryController.as_view(), name='query-create'),
    path('queries/', QueryHistoryController.as_view(), name='query-history'),
]
