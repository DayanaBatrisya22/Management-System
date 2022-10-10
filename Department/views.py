from os import system
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

from .models import SystemAnalyst
from .serializers import SystemAnalystSerializer
from .models import SoftwareTester
from .serializers import SoftwareTesterSerializer
from .models import DataScientist
from .serializers import DataScientistSerializer
from .models import BackEnd
from .serializers import BackEndSerializer
from .models import FrontEnd
from .serializers import FrontEndSerializer
from .models import UiUx
from .serializers import UiUxSerializer
from .models import SalesMarketing
from .serializers import SalesMarketingSerializer

#HOME PAGE


def HomePage(request):
    return render(request, 'dept/HomePage.html')

def SA_html(request):
    data = SystemAnalyst.objects.all()
    return render(request, 'dept/List.html', {'DATA':data})

def ST_html(request):
    data = SoftwareTester.objects.all()
    return render(request, 'dept/List.html', {'DATA':data})
    
def DS_html(request):
    data = DataScientist.objects.all()
    return render(request, 'dept/List.html', {'DATA':data})

def BE_html(request):
    data = BackEnd.objects.all()
    return render(request, 'dept/List.html', {'DATA':data})
    
def FE_html(request):
    data = FrontEnd.objects.all()
    return render(request, 'dept/List.html', {'DATA':data})

def SM_html(request):
    data = SalesMarketing.objects.all()
    return render(request, 'dept/List.html', {'DATA':data})
    
def UIUX_html(request):
    data = UiUx.objects.all()
    return render(request, 'dept/List.html', {'DATA':data})
    

###########################################

#LIST FOR SYSTEM ANALYST
@api_view(['GET', 'POST'])
def SystemAnalyst_list(request, format=None):

    if request.method == 'GET':
        systemAnalyst = SystemAnalyst.objects.all()
        serializer = SystemAnalystSerializer(systemAnalyst, many =True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SystemAnalystSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def SystemAnalyst_detail(request, id, format=None):

    try:
        systemAnalyst = SystemAnalyst.objects.get(pk=id)
    except SystemAnalyst.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = SystemAnalystSerializer(systemAnalyst)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = SystemAnalystSerializer(systemAnalyst, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        systemAnalyst.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#LIST OF SOFTWARE TESTER
@api_view(['GET', 'POST'])
def SoftwareTester_list(request, format=None):

    if request.method == 'GET':
        softwareTester = SoftwareTester.objects.all()
        serializer = SoftwareTesterSerializer(softwareTester, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SoftwareTesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def SoftwareTester_detail(request, id, format=None):

    try:
        softwareTester = SoftwareTester.objects.get(pk=id)
    except SoftwareTester.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SoftwareTesterSerializer(softwareTester)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = SoftwareTesterSerializer(softwareTester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        softwareTester.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#LIST FOR DATA SCIENTIST
@api_view(['GET', 'POST'])
def DataScientist_list(request, format=None):

    if request.method == 'GET':
        dataScientist = DataScientist.objects.all()
        serializer = DataScientistSerializer(dataScientist, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DataScientistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def DataScientist_detail(request, id, format=None):

    try:
        dataScientist = DataScientist.objects.get(pk=id)
    except DataScientist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DataScientistSerializer(dataScientist)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = DataScientistSerializer(dataScientist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        DataScientist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#LIST FOR BACK END
@api_view(['GET', 'POST'])
def BackEnd_list(request, format=None):

    if request.method == 'GET':
        backEnd = BackEnd.objects.all()
        serializer = BackEndSerializer(backEnd, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BackEndSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def BackEnd_detail(request, id, format=None):

    try:
        backEnd = BackEnd.objects.get(pk=id)
    except BackEnd.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BackEndSerializer(backEnd)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = BackEndSerializer(backEnd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        BackEnd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#LIST FOR FRONT END
@api_view(['GET', 'POST'])
def FrontEnd_list(request, format=None):

    if request.method == 'GET':
        frontEnd = FrontEnd.objects.all()
        serializer = FrontEndSerializer(frontEnd, many =True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = FrontEndSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def FrontEnd_detail(request, id, format=None):

    try:
        frontEnd = FrontEnd.objects.get(pk=id)
    except FrontEnd.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FrontEndSerializer(frontEnd)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = FrontEndSerializer(frontEnd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        FrontEnd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#LIST FOR UIUX
@api_view(['GET', 'POST'])
def UiUx_list(request, format=None):

    if request.method == 'GET':
        uiUx = UiUx.objects.all()
        serializer = UiUxSerializer(uiUx, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UiUxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def UiUx_detail(request, id, format=None):

    try:
        uiUx = UiUx.objects.get(pk=id)
    except UiUx.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UiUxSerializer(uiUx)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = UiUxSerializer(uiUx, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        UiUx.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#LIST FOR SALES AND MARKETING
@api_view(['GET', 'POST'])
def SalesMarketing_list(request, format=None):

    if request.method == 'GET':
        salesMarketing = SalesMarketing.objects.all()
        serializer = SalesMarketingSerializer(salesMarketing, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SalesMarketingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def SalesMarketing_detail(request, id, format=None):

    try:
        salesMarketing = SalesMarketing.objects.get(pk=id)
    except SalesMarketing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SalesMarketingSerializer(salesMarketing)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = SalesMarketingSerializer(salesMarketing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        SalesMarketing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)