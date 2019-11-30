from django.contrib import admin
from django.urls import path,include
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 시작 페이지
    path('', accounts.views.login, name='login'),
    # accounts app url
    path('accounts/', include('allauth.urls')),

    path('game/', include('game.urls')),
]
