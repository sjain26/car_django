from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path("", views.CreateUserView.as_view(), name='signup'),
    path("", views.sign_up_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('sold/', views.sold_car, name='mail'),
    # path('home/', views.CarListView.as_view(), name='home'),
    path('consumer/<int:id>', views.buy_car, name='consumer'),
    path('myadmin/<int:id>', views.MyAdmin.get, name='myadmin'),
    path('home/', views.home_page, name='home'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)