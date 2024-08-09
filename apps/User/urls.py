from django.urls import path


from .views import UserView, UserDetailView


urlpatterns = [
    path('', UserView.as_view()),
    path('<str:pk>', UserDetailView.as_view())
]

