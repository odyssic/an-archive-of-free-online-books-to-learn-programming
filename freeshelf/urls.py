from django.contrib import admin
from django.urls import path
from core import views
from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', views.homepage, name='homepage'),
    path('books/<int:pk>', views.book_detail, name='book-detail'),
    path('author/<int:pk>', views.author, name='author'),
    path('subject/<int:pk>', views.subject, name='subject'),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
