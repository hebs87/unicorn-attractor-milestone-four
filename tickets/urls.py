from django.conf.urls import url
from .views import view_all_tickets, new_bug_ticket, new_feature_ticket


urlpatterns = [
    url(r'^$', view_all_tickets, name="view_all_tickets"),
    url(r"^new/bug$", new_bug_ticket, name="new_bug_ticket"),
    url(r"^new/feature$", new_feature_ticket, name="new_feature_ticket"),
]
