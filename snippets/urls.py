from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetsViewSet.snippet_list),
    path('snippets/<int:pk>/', views.SnippetsViewSet.snippet_detail),
]