from django.contrib import admin
from django.urls import path, include

import accountapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
]
