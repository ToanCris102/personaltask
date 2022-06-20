from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkspaceListCreateView.as_view(), name='create_list_workspace'),
    path('<int:workspace_id>/', views.WorkspaceDetailView.as_view(), name='detail_workspace'),
]