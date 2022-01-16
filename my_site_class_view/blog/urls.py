from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostView.as_view(), name="post-page"),
    path("posts/<slug:slug>", views.SignlePostView.as_view(), name="post-detail-page"),
]
