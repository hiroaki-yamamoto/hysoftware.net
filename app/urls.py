"""
Hysoft URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

"""

from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin

from django_otp.admin import OTPAdmin, AdminSite

OTPAdmin.enable()
admin.site = AdminSite()

urlpatterns = [
    url(r'^c/', include('app.common')),
    url(r'^l/', include('app.legal')),
    url(r'^s/', admin.site.urls),
    url(r"^qr/", include("django_otp.urls")),
    url(r"^u/", include('app.user')),
    url(r'^', include('app.home'))
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
