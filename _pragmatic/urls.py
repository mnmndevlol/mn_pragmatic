from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    # path('', RedirectView.as_view(url='/accounts/hello_world/', permanent=True)),
]
