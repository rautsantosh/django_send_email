from send_mails import views
from django.urls import path

urlpatterns = [
    path('send_mail/', views.smtp_send_mail, name='send_mail'),
]