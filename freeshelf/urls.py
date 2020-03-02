from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('books/<int:pk>', views.book_detail, name='book-detail'),
    path('author/<int:pk>', views.author, name='author'),
    path('subject/<int:pk>', views.subject, name='subject'),
    # path('image/<int:pk>', views.image, name='image'),
    path('accounts/', include('registration.backends.default.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
