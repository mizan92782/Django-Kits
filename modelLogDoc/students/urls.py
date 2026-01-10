from rest_framework.routers import DefaultRouter

from students.views import StudentView


router =DefaultRouter()
router.register(r'students/',StudentView,basename='student')
urlpatterns = router.urls