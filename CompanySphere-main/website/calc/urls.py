'''from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index.html',views.index,name='index'),
]'''
# urls.py

'''from django.urls import path
from .views import your_view
from .views import your_view1
from .views import your_view2
from .views import your_view3
from .views import your_view4
from .views import your_view5
#from .views import data
#from .views import pie_chart_view
#from . import views
#from .views import line_chart, line_chart_json



urlpatterns = [
            path('index.html',views.index,name='index'),

        path('google.html', your_view, name='your-view'),
        path('microsoft.html', your_view1, name='your-view1'),
        #path('microsoft.html', line_chart, name='line_chart'),
        #path('chartJSON', line_chart_json, name='line_chart_json'),


        path('ibm.html', your_view2, name='your-view2'),
        path('tcs.html', your_view3, name='your-view3'),
        path('walmart.html', your_view4, name='your-view4'),
        path('wipro.html', your_view5, name='your-view5'),
        #path('login/', views.login, name='login'),
        

]'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Mapping the root URL to your index view
    path('index.html', views.index, name='index'),  # Explicitly mapping index.html to your index view

    # Add other URL patterns for your views
    path('google.html', views.your_view, name='your-view'),
    path('microsoft.html', views.your_view1, name='your-view1'),
    path('ibm.html', views.your_view2, name='your-view2'),
    path('tcs.html', views.your_view3, name='your-view3'),
    path('walmart.html', views.your_view4, name='your-view4'),
    path('wipro.html', views.your_view5, name='your-view5'),
]

