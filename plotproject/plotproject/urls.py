from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("plotapp.urls")),
    path('', include("plotappauth.urls")),
    path('', include("plotcategories.urls")),

]
