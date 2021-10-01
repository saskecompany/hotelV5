from django.urls.conf import path
from stay.views import longstay

app_name = "stay"

urlpatterns = [
    path("<int:id>/",longstay, name='stay')
]
