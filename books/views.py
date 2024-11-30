from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from books.models import Books, Departments
from books.api.serializers import BookSerializer, DepartmentSerializer


@csrf_exempt
def bookApi(request, id=0):
    if request.method=='GET':
        books = Books.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    
    elif request.method=='POST':
        books_data = JSONParser().parse(request)
        books_serializer = BookSerializer(data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Process realized with success!", safe=False)
        return JsonResponse("Process not realized!", safe=False)
    
    elif request.method=='PUT':
        books_data = JSONParser().parse(request)
        books = Books.objects.get(books_id = books_data['book_id'])
        books_serializer = BookSerializer(books, data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Process actualized with success!", safe=False)
        return JsonResponse("Process not actualized!", safe=False)
    
    elif request.method=='DELETE':
        book = Books.objects.get(book_id=id)
        book.delete()
        return JsonResponse("Process deleted with success!", safe=False)
    return JsonResponse("Process not deleted!", safe=False)


@csrf_exempt
def departmentApi(request, id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    
    elif request.method=='POST':
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Process realized with success!", safe=False)
        return JsonResponse("Process not realized!", safe=False)
    
    elif request.method=='PUT':
        departments_data = JSONParser().parse(request)
        departments = Departments.objects.get(departments_id = departments_data['department_id'])
        departments_serializer = DepartmentSerializer(departments, data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Process actualized with success!", safe=False)
        return JsonResponse("Process not actualized!", safe=False)
    
    elif request.method=='DELETE':
        department = Departments.objects.get(department_id=id)
        department.delete()
        return JsonResponse("Process deleted with success!", safe=False)
    return JsonResponse("Process not deleted!", safe=False)
