from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from first import views

urlpatterns = [
    path('list/', views.UserViewSet.users_list),
    path('detail/<int:pk>/', views.UserViewSet.users_detail),
    path('web/list/', views.WebPageViewSet.as_view()),
    path('web/list/<int:pk>/', views.WebPageDetailViewSet.as_view()),
    path('topic/list/', views.TopicViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
