from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="RZA"

urlpatterns = [
    path('', views.home, name="home"),
    path('information/', views.information, name="information"),
    path('tickets/',views.tickets,name="tickets"),
    path('cancel-booking/<int:booking_id>/',views.cancel_booking, name='cancel_booking'),
    path('hotel/',views.hotel, name="hotel"),
    path('cancel-hotel/<int:hotel_id>/',views.cancel_hotel, name='cancel_hotel'),
    path('profile/',views.profile, name="profile"),
    path('terms&conditions',views.terms, name="terms"),
    path('privacyPolicy',views.policy, name="policy"),
    path('schoolTrip', views.schoolTrip, name="schoolTrip"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)