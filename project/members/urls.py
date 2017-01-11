from django.conf.urls import url, include
from members import views

urlpatterns = [
    url(r'^members/$', views.MemberListView.as_view(), name='member_list'),

]