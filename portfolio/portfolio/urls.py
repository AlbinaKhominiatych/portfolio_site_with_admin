from django.contrib import admin
from django.urls import path
from portfolio_app.views import ProjectListView, IndexView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
