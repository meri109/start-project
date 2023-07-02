from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('blog/', views.blog, name='article_blog'),
    path('blog/<int:id>/', views.blog_detail, name='blog-detail'),
    path('example/', views.example),

]