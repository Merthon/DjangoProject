from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 所有 API 路由以 /api/ 开头
    path('api/', include('analysis.urls')),
]
