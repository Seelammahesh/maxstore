"""maxstore URL Configuration

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
from inventry.views import add_product,get_products,get_product_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',add_product,name="add"),
    path('get/',get_products,name="get_products"),
    path('get/<int:id>/',get_product_by_id,name="get_product_by_id"),
]
