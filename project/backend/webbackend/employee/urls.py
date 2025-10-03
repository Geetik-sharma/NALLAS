from django.urls import path,include
from .import views


#urlpatterns
urlpatterns=[
    path("/api/v2/employee",include("api.urls")),
]