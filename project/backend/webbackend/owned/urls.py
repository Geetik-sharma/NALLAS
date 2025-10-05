from django.urls import path,include

urlpatterns=[
    path("/api/v2/owned",include("api.urls")),
]