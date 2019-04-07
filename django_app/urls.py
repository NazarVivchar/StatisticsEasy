from django.urls import include, path
from rest_framework import routers
from .views import main_page, info_demo_regression, regression_info, dnn_demo_info, dnn_info, polynomial_reg

urlpatterns = [
    path('', main_page.as_view(), name='main_page'),
    path('regression_demo_info/',info_demo_regression.as_view(), name='info_demo_regression'),
    path('regression_info/', regression_info.as_view(), name='regression_info'),
    path('dnn_demo_info/', dnn_demo_info.as_view(), name='dnn_demo_info'),
    path('dnn_info/', dnn_info.as_view(), name='dnn_info'),
    path('polynomial_regression', polynomial_reg.as_view(), name='poly_reg')
]