
from django.contrib import admin
from django.urls import path
from register import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage, name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('upload_post/', views.upload_post, name='upload_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/', views.post_list, name='post_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


