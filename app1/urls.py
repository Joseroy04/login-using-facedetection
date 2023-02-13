# urls.py
from django.urls import path
from .views import signup, login_face_recog, home,login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/',login , name='login'),
    path('login_face_recog/', login_face_recog, name='login_face_recog'),
    path('home/', home, name='home'),
    path('', home),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        