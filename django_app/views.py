import os
import base64
import numpy as np
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView, Response
from rest_framework.parsers import JSONParser
from .models import DataFile, ImageFile,Distribution
from .serializers import FileSerializer, DistributionSerializer
from .statistic_algorithms import neural_network_prediction
from django_app.statistic_algorithms.Regressions import logistic_regression, polynomial_regression, \
    simple_linear_regretion

from django_app.statistic_algorithms.MovingAverages import simple_ma,weighted,runing_mean,exponential
from django_app.statistic_algorithms.Clasterization import k_means, hierarcial_clasterization,t_sne
from django_app.statistic_algorithms.Distributions import anglit,arcsine,bernoulli,dweibull,expon,normal,triang,\
    uniform, wald
from django_app.statistic_algorithms.Filters import kalman

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
                print(line)
                tmp = line.split(',')
                print(tmp)
                x.append(int(tmp[0]))
                y.append(int(tmp[1]))

        alpha,beta = simple_linear_regretion.least_squers_fit(x, y)
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

        alpha,beta = simple_linear_regretion.least_squers_fit(x, y)
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
                x.append(int(tmp[0]))
                y.append(int(tmp[1]))

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
        with open(file[0].get_file_name()) as f:
            for line in f:
                tmp = line.split(',')
                x.append(float(tmp[0]))
                y.append(float(tmp[1]))

        chart_reg_y = polynomial_regression.func(file[0].get_file_name(), 3)
        chart_reg_x = x
        os.remove(file[0].get_file_name())
        file[0].delete()
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
        print(file)

        chart_reg = logistic_regression.func(file[0].get_file_name())[2]
        print(ImageFile.objects.all()[0].image)



        with open(ImageFile.objects.all()[0].get_file_name(), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        print(encoded_string)


        os.remove(file[0].get_file_name())
        file[0].delete()
        image = ImageFile.objects.all()
        os.remove(image[0].get_file_name())
        image[0].delete()
        return Response([{'chart_reg': chart_reg},{'reg_image': encoded_string}])


class h_claster(APIView):
    permission_classes = [permissions.AllowAny, ]
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()

        print(file[0].get_file_name())

        hierarcial_clasterization.main(filename=file[0].get_file_name())
        images = ImageFile.objects.all()

        with open(images[0].get_file_name(), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())



        with open(images[1].get_file_name(), "rb") as image_file:
            encoded_string1 = base64.b64encode(image_file.read())



        with open(images[2].get_file_name(), "rb") as image_file:
            encoded_string2 = base64.b64encode(image_file.read())



        os.remove(file[0].get_file_name())
        file[0].delete()

        os.remove(images[0].get_file_name())
        images[0].delete()
        os.remove(images[0].get_file_name())
        images[0].delete()
        os.remove(images[0].get_file_name())
        images[0].delete()
        return Response([{'hierarcial_preview': encoded_string}, {'hierarcial_dendrogram': encoded_string1},
                         {'hierarcial_result': encoded_string2}])

class k_mean(APIView):
    permission_classes = [permissions.AllowAny, ]
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()
        print(file)
        k_means.main(filename=file[0].get_file_name())
        with open(ImageFile.objects.all()[0].get_file_name(), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())



        with open(ImageFile.objects.all()[1].get_file_name(), "rb") as image_file:
            encoded_string1 = base64.b64encode(image_file.read())




        os.remove(file[0].get_file_name())
        file[0].delete()
        image = ImageFile.objects.all()
        os.remove(image[0].get_file_name())
        image[0].delete()
        os.remove(image[0].get_file_name())
        image[0].delete()
        return Response([{'result_image': encoded_string1},{'preview_image': encoded_string}])


class t_Sne(APIView):
    permission_classes = [permissions.AllowAny, ]
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()
        print(file)

        t_sne.main()
        print(ImageFile.objects.all()[0].image)



        with open(ImageFile.objects.all()[0].get_file_name(), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        with open(ImageFile.objects.all()[1].get_file_name(), "rb") as image_file:
            encoded_string1 = base64.b64encode(image_file.read())




        os.remove(file[0].get_file_name())
        file[0].delete()
        image = ImageFile.objects.all()
        os.remove(image[0].get_file_name())
        image[0].delete()
        os.remove(image[0].get_file_name())
        image[0].delete()
        return Response([{'result_image': encoded_string1},{'preview_image': encoded_string}])

class simple_ma_info(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        print(request)
        file = DataFile.objects.all()

        x,chart_reg_y,y = simple_ma.main(file[0].get_file_name())
        chart_reg_y = chart_reg_y[4:-2]
        x = x[4:-2]
        y = y[4:-2]
        print(chart_reg_y)
        print(y)

        os.remove(file[0].get_file_name())
        file[0].delete()
        return Response([{'chart_reg_x': x}, {'chart_reg_y': chart_reg_y}, {'chart_x': x}, {'chart_y': y}])

class distribution_info(APIView):
    permission_classes = [permissions.AllowAny, ]
    parser_classes = (JSONParser,)
    def post(self, request):

        distr_serializer = DistributionSerializer(data=request.data)
        if distr_serializer.is_valid():
            distr_serializer.save()

        tp = request.data.get('distribution_type')

        response = []
        if tp in 'anglit' or tp in 'arcsine' or tp in 'dweibull' or tp in 'norm' or tp in 'triang' or tp in 'wald':
            response.append('location')
            response.append('scale')
        if tp in 'bernoulli':
            response.append('probability')
        if tp in 'dweilbull' or tp in 'triang':
            response.append('c')
        if tp in 'uniform':
            response.append('high')
            response.append('low')
        return Response([{'features': response}])


    def get(self, request):
        distribution = Distribution.objects.all()[0]

        if distribution.distribution_type in 'Anglit':
            result = anglit.anglit(distribution.n, int(request.GET.get('location')),int(request.GET.get('scale')))
        elif distribution.distribution_type in 'Arcsine':
            result = arcsine.arcsine(distribution.n, float(request.GET.get('location')), float(request.GET.get('scale')))
        elif distribution.distribution_type in 'Bernoulli':
            result = bernoulli.test(distribution.n, float(request.GET.get('probability')))
        elif distribution.distribution_type in 'Double Weibull':
            result = dweibull.dweibull(distribution.n, float(request.GET.get('c')),int(request.GET.get('location')),
                                    float(request.GET.get('scale')))
        elif distribution.distribution_type in 'Exponential':
            result = expon.expon(distribution.n)
        elif distribution.distribution_type in 'Normal':
            print('##########################################')
            result = normal.normal(distribution.n, float(request.GET.get('location')), float(request.GET.get('scale')))
            print('##########################################')
        elif distribution.distribution_type in 'Triangular':
            result = triang.triang(distribution.n,  loc = int(request.GET.get('location')),
                                    scale = int(request.GET.get('scale')))
        elif distribution.distribution_type in 'Uniform':
            result = uniform.uniform(distribution.n)
        else:
            result = wald.wald(distribution.n, int(request.GET.get('location')), int(request.GET.get('scale')))
        distribution.delete()

        return Response([{'result': result}])



class weighted_ma_info(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()


        x,chart_reg_y,y = weighted.main(file[0].get_file_name())
        chart_reg_y = chart_reg_y[6:-2]
        x = x[6:-2]
        y = y[6:-2]
        print(chart_reg_y)
        print(y)

        os.remove(file[0].get_file_name())
        file[0].delete()
        return Response([{'chart_reg_x': x}, {'chart_reg_y': chart_reg_y}, {'chart_x': x}, {'chart_y': y}])
class running_ma_info(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()


        x,chart_reg_y,y = runing_mean.main(file[0].get_file_name())
        chart_reg_y = chart_reg_y[4:-2]
        x = x[4:-2]
        y = y[4:-2]
        print(chart_reg_y)
        print(y)

        os.remove(file[0].get_file_name())
        file[0].delete()
        return Response([{'chart_reg_x': x}, {'chart_reg_y': chart_reg_y}, {'chart_x': x}, {'chart_y': y}])

class exp_ma_info(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()




        x,chart_reg_y,y = exponential.main(file[0].get_file_name())
        chart_reg_y = chart_reg_y[4:-2]
        x = x[4:-2]
        y = y[4:-2]
        print(chart_reg_y)
        print(y)

        os.remove(file[0].get_file_name())
        file[0].delete()
        return Response([{'chart_reg_x': x}, {'chart_reg_y': chart_reg_y}, {'chart_x': x}, {'chart_y': y}])




class kalman_info(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(status=200)

    def get(self, request):
        file = DataFile.objects.all()

        kalman.main()
        print(ImageFile.objects.all()[0].image)



        with open(ImageFile.objects.all()[0].get_file_name(), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        print(encoded_string)




        image = ImageFile.objects.all()
        os.remove(image[0].get_file_name())
        image[0].delete()
        os.remove(file[0].get_file_name())
        file[0].delete()
        return Response([{'reg_image': encoded_string}])
