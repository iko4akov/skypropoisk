from .auth import api as auth_ns
from .user import api as user_ns
from .product import api as product_ns

__all__ = [
    'auth_ns',
    'user_ns',
    'product_ns'
]
