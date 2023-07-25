# crime_statistics_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from crime_stats.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crime-stats/', include('crime_stats.urls')),
    # Add a default URL pattern for the root path
    # For example, you can include a view function here or redirect to a specific URL
    # Replace 'your_default_view' with the view function that should handle the root path.
    # Alternatively, you can use Django's redirect function to redirect to a specific URL.
    path('', home),
]

# Add the following line to serve static files during development
from django.conf import settings
from django.conf.urls.static import static

# Add this line to serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
