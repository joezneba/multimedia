
from django.contrib import admin
from django.urls import path, include
from apps.video import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('apps.video.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
