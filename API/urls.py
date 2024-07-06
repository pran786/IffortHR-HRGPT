from django.urls import path
from API import views


urlpatterns = [
    path('', views.index, name = 'index'),
    # path('upload_data', views.UploadData, name = 'upload_data'),
    # path('extract-text/', views.extract_text_from_website, name='extract_text'),
    path('ask/', views.HRAssistantView.as_view(), name='hr_assistant'),
]


    