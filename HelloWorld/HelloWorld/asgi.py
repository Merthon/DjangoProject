"""
ASGI config for HelloWorld project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
# 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目。
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HelloWorld.settings')

application = get_asgi_application()
