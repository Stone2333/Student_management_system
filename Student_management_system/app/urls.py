from django.conf.urls import url
from app import views

urlpatterns = [
    url('^login$', views.login),
    url('^login_check$', views.login_check),
    url('index$', views.index),
    url('student_all$', views.student_all),
    url('student_id$', views.student_info_student_id),
    url('student_name$', views.student_info_student_name),
    url('student_address$', views.student_info_student_address),
    url('student_departments$', views.student_info_student_departments),
    url('student_gender$', views.student_info_student_gender),
    url('student_birth$', views.student_info_student_birth),
    url('^add$', views.add),
    # url('delete$', views.delete),
    url('student_add$', views.student_add),
    url('student_delete$', views.student_delete),
    # url('student_info_name$', views.student_info_name),
    # url('student_info_address$', views.student_info_address),

]