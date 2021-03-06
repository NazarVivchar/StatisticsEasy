from django.urls import path

from .views import main_page, info_demo_regression, regression_info, dnn_demo_info, dnn_info, polynomial_reg, \
    logistic_reg, t_Sne,k_mean, h_claster, simple_ma_info,distribution_info,exp_ma_info,weighted_ma_info, \
    running_ma_info,kalman_info, sgd_info, svm_info, general_info, tree_info


urlpatterns = [
    path('', main_page.as_view(), name='main_page'),
    path('regression_demo_info/',info_demo_regression.as_view(), name='info_demo_regression'),
    path('regression_info/', regression_info.as_view(), name='regression_info'),
    path('dnn_demo_info/', dnn_demo_info.as_view(), name='dnn_demo_info'),
    path('dnn_info/', dnn_info.as_view(), name='dnn_info'),
    path('poly_info/', polynomial_reg.as_view(), name='poly_reg'),
    path('log_info/', logistic_reg.as_view(), name='log_reg'),
    path('t_sne_info/', t_Sne.as_view(),name='t_sna'),
    path('h_claster_info/', h_claster.as_view(),name='h_claster'),
    path('k_means_info/', k_mean.as_view(),name='k_means'),

    path('simple_ma_info/', simple_ma_info.as_view(), name='simple_ma_info'),
    path('distribution_info/', distribution_info.as_view(), name='distribution_info'),

    path('exp_ma_info/', exp_ma_info.as_view(), name='exponential_ma'),
    path('running_ma_info/', running_ma_info.as_view(), name='running_ma'),
    path('weighted_ma_info/', weighted_ma_info.as_view(), name='weighted_ma'),
    path('kalman_info/',kalman_info.as_view(),name='kanman_info'),
    path('sgd_info/', sgd_info.as_view(), name='sgd_info'),
    path('svm_info/', svm_info.as_view(), name='svm_info'),

    path('general_info/', general_info.as_view(), name='general_info'),
    path('tree_info/', tree_info.as_view(), name='tree_info'),


]