from django.conf.urls import url
from .views import view_all_tickets, new_bug_ticket, new_feature_ticket, view_single_ticket, delete_ticket, edit_ticket, upvote


urlpatterns = [
    url(r'^$', view_all_tickets, name="view_all_tickets"),
    url(r"^new/bug$", new_bug_ticket, name="new_bug_ticket"),
    url(r"^new/feature$", new_feature_ticket, name="new_feature_ticket"),
    url(r"^(?P<pk>\d+)$", view_single_ticket, name="view_single_ticket"),
    url(r"^edit/(?P<pk>\d+)$", edit_ticket, name="edit_ticket"),
    url(r"^delete/(?P<pk>\d+)$", delete_ticket, name="delete_ticket"),
    url(r"^upvote/(?P<pk>\d+)$", upvote, name="upvote"),
]
