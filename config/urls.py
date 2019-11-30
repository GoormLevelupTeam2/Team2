from django.contrib import admin
from django.urls import path,include
import accounts.views

urlpatterns = [
    path('', accounts.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
]
