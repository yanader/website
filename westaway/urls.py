from django.urls import path

from westaway import views

app_name = 'westaway'

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("entry/<int:id>", views.entry, name="entry"),
    path("mostvisited/", views.mostvisited, name="mostvisited"),
    path("mostvisited/ajax/", views.mostvisited_ajax, name="mostvisited_ajax"),
    path("randomentry", views.randomentry, name="randomentry"),
    path("error", views.error, name="error")
]