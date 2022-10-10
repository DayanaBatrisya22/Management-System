"""Department URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Department import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('systemanalyst/', views.SystemAnalyst_list),
    path('systemanalyst/<int:id>/',views.SystemAnalyst_detail),

    path('softwaretester/', views.SoftwareTester_list),
    path('softwaretester/<int:id>/',views.SoftwareTester_detail),

    path('datascientist/', views.DataScientist_list),
    path('datascientist/<int:id>/',views.DataScientist_detail),

    path('backend/', views.BackEnd_list),
    path('backend/<int:id>/',views.BackEnd_detail),

    path('frontend/', views.FrontEnd_list),
    path('frontend/<int:id>/',views.FrontEnd_detail),

    path('uiux/', views.UiUx_list),
    path('uiux/<int:id>/',views.UiUx_detail),

    path('salesmarketing/', views.SalesMarketing_list),
    path('salesmarketing/<int:id>/',views.SalesMarketing_detail),

    path('',views.HomePage ),
    path('SA/',views.SA_html ),
    path('ST/', views.ST_html),
    path('DS/', views.DS_html),
    path('BE/', views.BE_html),
    path('FE/', views.FE_html),
    path('SM/', views.SM_html),
    path('UIUX/', views.UIUX_html),
]

urlpatterns = format_suffix_patterns(urlpatterns)