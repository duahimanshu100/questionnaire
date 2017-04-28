from django.conf.urls import url
from app.api import PredictionApi
urlpatterns = [
    # url(r'^(?i)api/(?P<profile_id>.+)/Posts$', PostListApi.as_view()),
    url(r'^(?i)api/PredictionApi$', PredictionApi.as_view()),

]
