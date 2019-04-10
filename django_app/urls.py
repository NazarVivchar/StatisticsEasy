from django.urls import path

from .views import main_page, info_demo_regression, regression_info, dnn_demo_info, dnn_info, polynomial_reg, \
    logistic_reg, t_Sna,k_mean, h_claster, simple_ma_info,distribution_info

urlpatterns = [
    path('', main_page.as_view(), name='main_page'),
    path('regression_demo_info/',info_demo_regression.as_view(), name='info_demo_regression'),
    path('regression_info/', regression_info.as_view(), name='regression_info'),
    path('dnn_demo_info/', dnn_demo_info.as_view(), name='dnn_demo_info'),
    path('dnn_info/', dnn_info.as_view(), name='dnn_info'),
    path('poly_info/', polynomial_reg.as_view(), name='poly_reg'),
    path('log_info/', logistic_reg.as_view(), name='log_reg'),
    path('t_sna_info/', t_Sna.as_view(),name='t_sna'),
    path('h_claster_info/', h_claster.as_view(),name='h_claster'),
    path('k_means_info/', k_mean.as_view(),name='k_means'),
    path('simple_ma_info/', simple_ma_info.as_view(), name='simple_ma_info'),
    path('distribution_info/', distribution_info.as_view(), name='distribution_info'),


]