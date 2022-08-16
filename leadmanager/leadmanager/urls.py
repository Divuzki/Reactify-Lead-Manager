from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ad/', admin.site.urls, name="admin"),
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
    path('', include('accounts.urls'))
]
