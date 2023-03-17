from django.urls import path
from . import views


urlpatterns = [

    path('', views.user_list, name='user_list'),
    path('trans', views.translation_list, name='translation_list'),
    path("<int:id>", views.user_detail, name='user_detail'),
    path("trans/<int:id>", views.user_update, name='user_update'),

]
