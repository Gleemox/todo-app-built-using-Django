from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup),
    path('loginn/', views.loginn),
    path('todopage', views.todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>', views.delete_todo), # pass serial number as integer in url to know which item to delete 

]
