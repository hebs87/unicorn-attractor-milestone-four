from django.conf.urls import url
from .views import view_all_tickets


urlpatterns = [
    url(r'^$', view_all_tickets, name="view_all_tickets"),
]
