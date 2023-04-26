from django.urls import path
from .views import HomePageView,PostDetail,AddPostView,ContactUsView,AboutView,ComingSoonView

# important urls for navigating through the site
app_name = "feed"

urlpatterns = [
    path('',HomePageView.as_view(),name = "index"),
    path('detail/<int:pk>/',PostDetail.as_view(),name="detail"),
    path('post/',AddPostView.as_view(),name = "post"),
    path('contact/',ContactUsView.as_view(),name = "contact"),
    path('about/',AboutView.as_view(),name = "about"),
    path('coming/',ComingSoonView.as_view(),name = "coming")
        
]