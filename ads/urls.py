from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('all_ads/', AdsList.as_view(), name='ads_list'),
    path('rubrics/', rubric_list, name='rubric_list'),
    path('rubrics/<int:id>/', theme_of_rubric, name='theme_list'),
    path('rubrics/<int:rubric>/<int:theme>/', ads_of_themes, name='ads_of_theme'),
    path('rubrics/<int:rubric>/<int:theme>/<int:id>', detail_of_theme, name='detail_ads'),
    path('rubrics/create/', ads_create, name='create_ads'),

]