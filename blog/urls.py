from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<int:topic_id>/', views.topics, name='topic'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
]
