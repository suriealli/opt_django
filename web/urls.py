"""web URL Configuration

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
from django.conf.urls import url, include
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


def handler400(request):
    from django.http import HttpResponse
    return HttpResponse("400")

def handler500(request):
    from django.http import HttpResponse
    return HttpResponse("500")


lis = [
    url(r'^auth/', include('web_auth.urls')),
]

urlpatterns = lis

# urlpatterns = [
#     url(r'^auth/', include('web_auth.urls')),
#     url(r'^admin/', admin.site.urls),
# ]


