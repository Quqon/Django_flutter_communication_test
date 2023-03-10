from django.urls import path,inclue     # include를 사용해 routing을 한다.
from . import views
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=False)
router.register('plan', views.TodoView)

urlpatterns = [
    path('', include(router.urls))       # 홈페이지에 접속하면 바로 앱 url로 가게 라우팅
]
