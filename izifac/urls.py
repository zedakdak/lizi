from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from iziapp import views

admin.autodiscover()

# Router de l'application : contient les routes du service web
router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'invoicesitems', views.InvoiceItemViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^$', 'api_root'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)