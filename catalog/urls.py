from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import hello
from catalog.views import contacty
from django.conf import settings
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [
        path('', hello),
        path('contacts/', contacty),
        ]