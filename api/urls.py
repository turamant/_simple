from django.urls import path

from api.views import PostAPIView

urlpatterns =[
    path('', PostAPIView.as_view()),


]