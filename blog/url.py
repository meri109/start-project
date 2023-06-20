from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.blog),
    path('blog-detail/', views.blog_detail),
]