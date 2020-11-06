from .views import PictureWorkArtUploadView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('work-art', PictureWorkArtUploadView)

urlpatterns = router.urls
