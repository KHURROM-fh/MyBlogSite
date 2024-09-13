from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns = [
    # path('add/', views.add_post, name='add_post'),
    path('add/', views.AddPostCreateView.as_view(), name='add_post'),
    # path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('edit/<int:id>/', views.EditPostView.as_view(), name='edit_post'),
    # path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='delete_post'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='details_post'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  