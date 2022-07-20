from django.contrib import admin
from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('', views.render_post, name='posts'),
    path('<int:post_id>', views.detail_post, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

