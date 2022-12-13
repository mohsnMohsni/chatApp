# Standard imports
import os

# Core imports.
from django.core.asgi import get_asgi_application

# Third-party imports.
from channels.routing import URLRouter, ProtocolTypeRouter

# Local imports.
from apps.chat.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django_asgi_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': django_asgi_application,
        'websocket': URLRouter(websocket_urlpatterns),
    }
)
