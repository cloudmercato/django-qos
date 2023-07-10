from django.urls import path
from django.contrib import admin
from django_qos.db import views as db_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-result/', db_views.TestResultListView.as_view(), name="testresult-list"),
]
