from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views, urls

router = routers.DefaultRouter()
router.register('paradigm', views.ParadigmView)
router.register('language', views.LanguageView)
router.register('programmer', views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view())
]
