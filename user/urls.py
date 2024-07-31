from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import IndexView, UserProfileDetailView

app_name = "user"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile/', IndexView.as_view(), name='profile'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='user_profile_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)