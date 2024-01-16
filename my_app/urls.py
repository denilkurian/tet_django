from django.urls import path
from .views import listall,delete_candidate,delete_each_candidate,add_new_candidate,trash,restore_trash,clear_trash,clear_single_trash,add_update_candidate



urlpatterns = [
   path('all/',listall,name='all'),
   path('delete/',delete_candidate,name='delete'),
    path('delete_each/<int:pk>/',delete_each_candidate,name='delete_each'),
     path('add/',add_new_candidate,name='add'),
      path('trash/',trash,name='trash'),
      path('restore_trash/<int:pk>/',restore_trash,name='restore_trash'),
      path('clear_trash/',clear_trash,name='clear_trash'),
      path('clear_single_trash/<int:pk>/',clear_single_trash,name='clear_single_trash'),
      path('add_update_candidate/<int:pk>/',add_update_candidate,name='add_update_candidate'),
]



