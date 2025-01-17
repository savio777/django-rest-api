from django.urls import path

from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/list/", views.BlogPostList.as_view(), name="blogpost-view-list"),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name="blogpost-view-update",
    ),
]
