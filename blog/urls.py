from django.urls import path

from . import views


from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('topic/<int:pk>/', views.topics, name='topic'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
]
