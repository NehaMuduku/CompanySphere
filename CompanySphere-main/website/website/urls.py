'''
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from calc.views import index
from calc.views import your_view1
#from calc.views import data
#from calc.views import pie_chart_view

urlpatterns = [
    path('',include('calc.urls')),
    path('admin/', admin.site.urls),
    path('index.html',views.index,name='index'),

      path('', your_view1, name='your-view1'),
            #path('microsoft.html', pie_chart_view, name='pie_chart_view'),



]
urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)'''
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from calc.views import index  # Import your index view

urlpatterns = [
    path('', include('calc.urls')),  # Include the URLs from the 'calc' app
    path('admin/', admin.site.urls),
]

# Serve static and media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
