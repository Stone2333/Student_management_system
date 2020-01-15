from django.conf.urls import url
from app import views

urlpatterns = [
    url('^login$', views.login),
    url('^login_check$', views.login_check),
    url('index$', views.index),
    url('student_all$', views.student_all),
    url('student_info$', views.student_info),
    # url('student_info_name$', views.student_info_name),
    # url('student_info_address$', views.student_info_address),

]