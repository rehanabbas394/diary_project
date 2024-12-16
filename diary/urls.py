from django.urls import path
from . import views

urlpatterns = [
    # Api urls
    path('entries/', views.diary_list, name='diary-list'),
    path('entries/<int:pk>/', views.diary_detail, name='diary-detail'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('add/', views.add_entry_view, name='add_entry'),  
    path('edit/<int:id>/', views.edit_entry_view, name='edit_entry'),  
    path('delete/<int:id>/', views.delete_entry_view, name='delete_entry'),
]







