from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path, include

from dowr.views import *

app_name = "dowr"
urlpatterns = [
    # general

    path('', homepage, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('signup/', signup, name='signup'),
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),
    path('game/', game, name='game')



]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
