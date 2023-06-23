from django.urls import path
from.import views
urlpatterns = [ path('', views.test_app, name='test_app_home'),
                path('answer/', views.test_app2, name='test_app_answer'),
]