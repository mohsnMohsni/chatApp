# Standard imports
import os

# Core imports.
from django.core.asgi import get_asgi_application

# Third-party imports.
from channels.routing import ProtocolTypeRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
    }
)
