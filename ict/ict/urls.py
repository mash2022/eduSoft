"""ict URL Configuration

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
from django.urls import include, path
from django.conf import settings 
from django.conf.urls.static import static
from courses import views as courses_view
from django.contrib.auth import views as auth


urlpatterns = [
    path('', include('courses.urls')),
    path('admin/', admin.site.urls),
    path('login/', courses_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('signup/', courses_view.signup, name ='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


