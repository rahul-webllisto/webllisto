from django.urls import path
from . views import *

urlpatterns = [
	path('contactus/', ContactusAPIView.as_view(), name="contact_us"),
	path('blog-list/', BlogListAPIView.as_view(), name="blog_list"),
]
    
