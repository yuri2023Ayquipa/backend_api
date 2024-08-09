from django.urls import path


from .views import MenuViews, MenuDetail_views


urlpatterns = [
    path('', MenuViews.as_view()),
    path('<str:pk>', MenuDetail_views.as_view())
]

