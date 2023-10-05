
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, admin_views, judge_views, police_views, general_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base')





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
