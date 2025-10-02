from django.urls import path,include
from .import views


#urlpatterns
urlpatterns=[
    path("",views.stuapi,name="stuapi"),
    path("/student/<int:pk>/",views.student_detail,name='primary view'),
]