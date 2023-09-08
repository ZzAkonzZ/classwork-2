from django.urls import path
from users.views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('auth/', auth_view, name="auth"),
    path('logout/', logout_view, name="logout"),
]
