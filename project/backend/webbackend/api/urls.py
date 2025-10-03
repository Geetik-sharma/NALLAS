from django.urls import path,include
from .import views


#urlpatterns
urlpatterns=[
    path("/student",views.stuapi,name="stuapi"),
    path("/student/<int:pk>/",views.student_detail,name='primary view'),

    path("/employees/",views.Employees.as_view()),
     path("/employees/<int:pk>",views.emp.as_view()),
     path("/product",views.prods.as_view()),
     path("/update/<int:pk>",views.Update_Prod.as_view()),
]