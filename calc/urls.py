from django.urls import path
from .views import survey_view, success_view
from . import views
# from .views import question_view,success_view
# from django.shortcuts import render

urlpatterns=[
 path('', views.home, name='home'),
#  path('r1', views.r1, name='r1'),
 path('add',views.add, name='add'),
 path('dashboard',views.dashboard, name='dashboard'),

#   path('test1', lambda request: render(request, 'test1.html'), name='test1'),
#   path('r1', question_view, name='r1'),
#   path('test1', success_view, name='test1'),

  path('r1', views.survey_view, name='r1'),
  path('test1/<str:q1>/<str:q2>/', views.success_view, name='test1'),
]
