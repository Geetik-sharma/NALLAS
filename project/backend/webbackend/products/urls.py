from django.urls import path,include

urlpatterns=[
    path("/api/v2/product",include("api.urls"))
]