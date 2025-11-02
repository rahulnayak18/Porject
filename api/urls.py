from django.urls import path
from . import views

urlpatterns = [
    path("blogposte/",views.BlogPostListCreate.as_view(),name="blogpost-view-create"),
        path("blogposts/<int:pk>/",views.BlogPostRetrieveUpdateDestory.as_view(),name="update", ),
]
