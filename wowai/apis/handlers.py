# quickstart/handlers.py
from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

from apis.services import AuthenService, CustomUserService, ActionService


# TODO @thanhlv add more for all services
def grpc_handlers(server):
    app_registry = AppHandlerRegistry("apis", server)
    app_registry.register(AuthenService)
    app_registry.register(CustomUserService)
    app_registry.register(ActionService)

