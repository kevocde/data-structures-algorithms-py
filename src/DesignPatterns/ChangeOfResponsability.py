"""
El patrón de diseño Cámbio de Reespnsabilidad, permite añadir dinámicamente diferentes comportamientos previos a un
proceso en concreto. Imagina que tienes un api rest, la cuál permite consultar los datos de determinados usuarios,
para hacer eso primero se debe chequear que el cliente esté autenticado, segundo que el cliente tenga los permisos apro-
piados y así tercero y cuarto puntos.
"""
from __future__ import annotations
from typing import Any, Optional
from abc import ABC, abstractmethod

USERNAME = 'kevocde'
PASSWORD = 'fuckingindexers.1'


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        return self._next_handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class AuthenticationHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        auth_string = f'usu:{USERNAME},pass:{PASSWORD}'

        if auth_string in request:
            print('Successful authentication')

            return super().handle(request.replace(auth_string, ''))
        else:
            print('Invalid authentication parameters, please, try again changing its')

            return None


class PermissionsHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        permissions_string = f'permissions:r,e'

        if permissions_string in request:
            print('Permissions successful validated')

            return super().handle(request.replace(permissions_string, ''))
        else:
            print('Invalid permissions')

            return None


def client_code(handler: Handler) -> None:
    request1 = 'I need access'
    handler.handle(request1)

    request2 = 'usu:kevocde,pass:fuckingindexers.1permissions:r,e|Good Message'
    handler.handle(request2)


if __name__ == '__main__':
    auth = AuthenticationHandler()
    permissions = PermissionsHandler()
    auth.set_next(permissions)
    client_code(auth)
