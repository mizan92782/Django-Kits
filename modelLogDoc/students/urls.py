from rest_framework.routers import DefaultRouter

from students.views import FahterView, MotherView


router =DefaultRouter()
router.register(r'father',FahterView,basename='father')
router.register(r'mother',MotherView,basename='mother')
urlpatterns = router.urls