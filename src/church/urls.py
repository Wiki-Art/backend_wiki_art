from .views import PictureChurchUploadView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('church', PictureChurchUploadView)


urlpatterns = router.urls
