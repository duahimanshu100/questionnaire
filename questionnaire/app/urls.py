from django.conf.urls import url
from app.api import PredictionApi
from app.views import IndexView
urlpatterns = [
    # url(r'^(?i)api/(?P<profile_id>.+)/Posts$', PostListApi.as_view()),
    url(r'^(?i)api/PredictionApi', PredictionApi.as_view()),
    url(r'^', IndexView.as_view()),

]
