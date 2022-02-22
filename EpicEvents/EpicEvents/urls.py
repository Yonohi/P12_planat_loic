"""EpicEvents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from CRMapp import views as CRM_views
from authentication import views as auth_views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
#from django.contrib.auth.views import LoginView, LogoutView

router = routers.DefaultRouter()
router.register(r'client', CRM_views.ClientViewSet, basename='client')
router.register(r'my_clients', CRM_views.MyClientsViewSet, basename='my_clients')
router.register(r'contract', CRM_views.ContractViewSet)
router.register(r'my_contracts', CRM_views.MyContractsViewSet, basename='my_contracts')
router.register(r'event', CRM_views.EventViewSet, basename='event')
router.register(r'my_events', CRM_views.MyEventsViewSet, basename='my_events')
router.register(r'user', auth_views.UserTeamViewSet)
router.register(r'user_sale', auth_views.UserTeamSaleViewSet)
router.register(r'user_support', auth_views.UserTeamSupportViewSet)
router.register(r'user_management', auth_views.UserTeamManagementViewSet)
router.register(r'events_without_support', CRM_views.EventsWithoutSupportViewSet, basename='events_without_support')


# Ajouter les event sans support pour les management

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # Nous donne le loginview et logoutview
    path('', include('rest_framework.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
    