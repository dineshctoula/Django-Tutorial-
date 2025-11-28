from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # All blog URLs start with /blog/
    path('shop/', include('shop.urls')),  # All shop URLs start with /shop/
]