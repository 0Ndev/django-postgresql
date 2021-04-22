from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView
from basic_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cheatsheets/', include('basic_app.urls')),
    # path('cheatsheet/', TemplateView.as_view(template_name="cheatsheet_view.html"),
    #      name='cheatsheet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
