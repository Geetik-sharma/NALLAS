
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerialzers,EmpSerializer,ProdSerializer,OwnedSerializer
from rest_framework.decorators import api_view
from insurance import models
from employee.models import employee
from rest_framework.views import APIView
from django.http import Http404
from products.models import products
from rest_framework import mixins,generics,viewsets
from owned.models import owned_products
# Create your views here.


#function based views

@api_view(['GET','POST'])
def stuapi(request):
    '''
    # stuinfo=models.student.objects.all()
    # print(stuinfo)
    # # json response assume we are passing dict. but now it is query set
    # # return JsonResponse( stuinfo , safe=False)
    # 
    # #now we can searialize data manually by iterating thourgh query set and making a list 
    # 
    # stuinfo_list=list(stuinfo.values())
    # 
    # # OR we can use rest's serializers(conersion of query set to josn formate or any formate we require) here we will use model serializer
    # return JsonResponse( stuinfo_list , safe=False)

    # # OR we can use rest's serializers(conersion of query set to josn formate or any formate we require) here we will use model serializer
    '''
    if request.method == "GET":
        #get all data from student 
        student=models.student.objects.all()
        serializer=StudentSerialzers(student, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif (request.method == "POST"):
        serializer=StudentSerialzers(data=request.data)
        if(serializer.is_valid)():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT',"DELETE"])
def student_detail(request, pk):
    try:
        student=models.student.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        serializer=StudentSerialzers(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif(request.method=="PUT"):
        serializer=StudentSerialzers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif(request.method=='DELETE'):
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
#class based views

class Employees(APIView):
    def get(self,request):
        employees=employee.objects.all()
        serializer=EmpSerializer(employees, many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    def post(self,request):
        serializer=EmpSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class emp(APIView):
    def get_object(self,pk):
        try:
            return employee.objects.get(pk=pk)
        except employee.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        emp=self.get_object(pk)
        serializer=EmpSerializer(emp)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    def put(self,request,pk):
        serializer=EmpSerializer(self.get_object(pk),data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

'''    
Mixins(reusable code classes in oop)
django provide 5 built in mixins
1. ListModelmixin list()
2.createmodelmixin create()
3.retrivemodel mixin retrive()
4. update model mixin update()
5.delete  model mxin delete()

#generic act as baseclass for building api views

# generic.GenericAPI_views provide essential functionalities such as get posst put delete

'''

"""MIXINS"""
'''
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin ,generics.GenericAPIView):
    queryset=employee.objects.all()
    serializer_class=EmpSerializer
    
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class emp(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
     queryset=employee.objects.all()
     serializer_class=EmpSerializer
     def get(self,request,pk):
        return self.retrieve(request,pk)
     def put(self, request, pk):
         return self.update(request,pk)
     def delete(self, request,pk):
         return self.destroy(request, pk)
'''

'''
@generic 
list api view -> listing object
create api view -> creating object
retrive api view -> retriving a single object using primary key
update api view -> updateing single object using pk
destroy api view -> for deletion of object using pk
listcreate api view -> listing and creating an objects
retriveupdate api view -> retriving and updating object using primary key
retriveupdatedestroy api view -> retriving and updating and deleting object using primary key
'''

#generics
class Employees(generics.ListAPIView, generics.CreateAPIView):#we can also use listcreateAPIView
    queryset=employee.objects.all()
    serializer_class=EmpSerializer


class emp( generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset=employee.objects.all()
    serializer_class=EmpSerializer
    lookup_field='pk'





#main Project
'''
class prods(APIView):
    def get(self,request):
        prod=products.objects.all()
        serializer=ProdSerializer(prod, many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    def post(self,request):
        serializer=ProdSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class Update_Prod(APIView):
    def update_prod(self,pk):
        try:
            return products.objects.get(pk=pk)
        except products.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        serializer=ProdSerializer(self.update_prod(pk))
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    def put(self,request,pk):
        serializer=ProdSerializer(self.update_prod(pk),data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        self.update_prod(pk).delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
'''
#by mixins
class prods(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=products.objects.all()
    serializer_class=ProdSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class Update_Prod(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=products.objects.all()
    serializer_class=ProdSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def post(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
    

'''
#owned products
class owned(APIView):
    def get(self,request):
        own=owned_products.objects.all()
        serializer=OwnedSerializer(own,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=OwnedSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class update_owned(APIView):
    def check(self,pk):
        try:
            return owned_products.objects.get(pk=pk)
        except owned_products.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        serializer=OwnedSerializer(self.check(pk))
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    def put(self,request,pk):
        serializer=OwnedSerializer(self.check(pk),data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            raise Http404
    def delete(self,request,pk):
        self.check(pk).delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
'''

"""by using viewset and router 
we use viewset to perform all get post put retrive delete and update task under one function
and use router to automatically handel the urls for simillar class
"""

class OwnedViewset(viewsets.ViewSet):
    def list(self,request):
        own=owned_products.objects.all()
        serializer=OwnedSerializer(own,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def create(self,request):
        serializer=OwnedSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    def retrieve(self,request,pk=None):
        own=get_object_or_404(owned_products,pk=pk)
        serializer=OwnedSerializer(own)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    def update(self,request,pk=None):
        serializer=OwnedSerializer(owned_products.objects.get(pk=pk),data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        owned_products.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_404_NOT_FOUND)