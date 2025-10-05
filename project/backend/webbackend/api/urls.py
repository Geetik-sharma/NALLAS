from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('owned',views.OwnedViewset,basename='owned') #register the viewset class in views.py



#urlpatterns
urlpatterns=[
    path("/student",views.stuapi,name="stuapi"),
    path("/student/<int:pk>/",views.student_detail,name='primary view'),

    path("/employees/",views.Employees.as_view()),
    path("/employees/<int:pk>",views.emp.as_view()),
     path("/product",views.prods.as_view()),
     path("/update/<int:pk>",views.Update_Prod.as_view()),
    #  path("/owned",views.owned.as_view()),
    #  path("/owned/<int:pk>",views.update_owned.as_view()),
    path("",include(router.urls)),
]