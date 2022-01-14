from django.urls import path
from . import views

urlpatterns = [
	path("main", views.main),
	path("techcrunch", views.techcrunch),
	path("mashable", views.mashable),
	path("theverge", views.theverge)
]