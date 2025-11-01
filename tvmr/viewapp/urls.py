from tempt.urls import urlpatterns,path
from . import views

urlpatterns=[
  path('json/', views.json_data_view,name='json'),
  path('post/', views.post_data,name='post'),
  path('baseView/', views.base_view.as_view(),name='baseview')
]