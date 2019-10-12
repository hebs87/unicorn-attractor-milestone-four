from django.conf.urls import url
from dashboard.views import dashboard_stats

urlpatterns = [
    url(r"^$", dashboard_stats, name="dashboard_stats")
]
