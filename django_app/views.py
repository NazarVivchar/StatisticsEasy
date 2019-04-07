from rest_framework import permissions
import os

import numpy as np
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView, Response

from .models import DataFile, ImageFile
from .serializers import FileSerializer, ImageSerializer
from .statistic_algorithms import simple_linear_regretion, neural_network_prediction, polynomial_regression, \
    logistic_regression


class regression_info(APIView):
    permission_classes = [permissions.AllowAny, ]
    def post(self,request):
        file_serializer = FileSerializer(data=request.data)
        
        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)
    def get(self,request):
        file = DataFile.objects.all()
        print(file)
        print(file[0].get_file_name())

        x = []
        y = []
        with open(file[0].get_file_name()) as f:
            for line in f:
                tmp = line.split(',')
                x.append(float(tmp[0]))
                y.append(float(tmp[1]))

        alpha,beta = simple_linear_regretion.least_squers_fit(x,y)
        chart_reg_y = [beta*point + alpha for point in x]
        chart_reg_x = [point for point in x]
        os.remove(file[0].get_file_name())
        file[0].delete()

        return Response([{'chart_reg_x':chart_reg_x},{'chart_reg_y':chart_reg_y},{'chart_x':x},{'chart_y':y}])



        
    


class main_page(APIView):

    def get(self,request):

        return render(request, '../templates/Index.html')


class info_demo_regression(APIView):
    permission_classes = [permissions.AllowAny, ]
    def post(self,request):
        print(request.data)
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
        return Response(status=200)

    def get(self,request):
        x = []
        y = []
        with open('media/dataset1.csv') as file:
            for line in file:
                tmp = line.split(',')
                x.append(float(tmp[0]))
                y.append(float(tmp[1]))

        alpha,beta = simple_linear_regretion.least_squers_fit(x,y)
        chart_reg_y = [beta*point + alpha for point in x]
        chart_reg_x = [point for point in x]
        
        return Response([{'chart_reg_x':chart_reg_x},{'chart_reg_y':chart_reg_y},{'chart_x':x},{'chart_y':y}])


class dnn_demo_info(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        print(request.data)
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
        return Response(status=200)

    def get(self, request):
        x = []
        y = []
        with open('media/dataset1.csv') as file:
            for line in file:
                tmp = line.split(',')
                x.append(float(tmp[0]))
                y.append(float(tmp[1]))

        np_y = np.array([[*y]])
        np_x = x
        chart_dnn_x, chart_dnn_y = neural_network_prediction.dnn_prediction(np_x,np_y)

        return Response([{'chart_dnn_x': chart_dnn_x}, {'chart_dnn_y': chart_dnn_y}, {'chart_x': x}, {'chart_y': y}])


class dnn_info(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()
        print(file)
        print(file[0].get_file_name())

        x = []
        y = []
        with open(file[0].get_file_name()) as f:
            for line in f:
                tmp = line.split(',')
                x.append(float(tmp[0]))
                y.append(float(tmp[1]))

        np_y = np.array([[*y]])
        np_x = x
        chart_dnn_x, chart_dnn_y = neural_network_prediction.dnn_prediction(np_x, np_y)
        os.remove(file[0].get_file_name())
        file[0].delete()
        return Response([{'chart_dnn_x': chart_dnn_x}, {'chart_dnn_y': chart_dnn_y}, {'chart_x': x}, {'chart_y': y}])




class polynomial_reg(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()


        x = []
        y = []
        with open('media/dataset1.csv') as f:
            for line in f:
                tmp = line.split(',')
                x.append(float(tmp[0]))
                y.append(float(tmp[1]))

        chart_reg_y = polynomial_regression.func('media/dataset1.csv',3)
        chart_reg_x = x
        # os.remove(file[0].get_file_name())
        # file[0].delete()
        return Response([{'chart_reg_x': chart_reg_x}, {'chart_reg_y': chart_reg_y}, {'chart_x': x}, {'chart_y': y}])


class logistic_reg(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()


        chart_reg = logistic_regression.func('media/example.csv','Survived')[2]
        reg_image = ImageSerializer(ImageFile.objects.all()[0])
        print(reg_image.data)

        # os.remove(file[0].get_file_name())
        # file[0].delete()
        return Response([{'chart_reg': chart_reg}, {'reg_image': reg_image.data}])
