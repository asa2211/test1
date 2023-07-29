from django.urls import path

from .views import detail, results, votes

urlpatterns = [
    path("<int:question_id>/", detail),

    path("<int:question_id>/results/", results),

    path("<int:question_id>/vote/", votes),
]