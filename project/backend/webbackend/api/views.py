
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerialzers,EmpSerializer,ProdSerializer
from rest_framework.decorators import api_view
from insurance import models
from employee.models import employee
from rest_framework.views import APIView
from django.http import Http404
from products.models import products
# Create your views here.


#function based views

@api_view(['GET','POST'])
def stuapi(request):

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
    
