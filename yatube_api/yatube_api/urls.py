from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

"""
Я все urls перенесла в прилжение, тут никаких проблем, но возник вопрос.
Пришлось или в главном urls.py проекта писать path('', include('api.urls')),
или убирать из префиксов ссылок в самом api/urls.py префикс 'api/'.
Я по тексту пожелания сделала вывод, что лучше в основном файле писать
path('api/', include('api.urls')), верно? =)
"""


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
