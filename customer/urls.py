

from django.urls import path

from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

app_name = 'customer'
urlpatterns = [
    path('', views.Customer.as_view(),name='customer'),
    path('verification/', views.Verification.as_view(),name='verification'),
    path('profile/', views.Profile.as_view(),name='profile'),
    path('customer/', views.Dashboard.as_view(),name='Dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()