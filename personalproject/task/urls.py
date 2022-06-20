from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.TaskListCreateView.as_view(), name="task_list_create"),
    path('<int:task_id>/', views.TaskDetailView.as_view(), name="task_detail"),
]