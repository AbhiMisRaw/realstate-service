from .user_routes import router as user_routes
from .property_routes import router as property_routes

__all__ = [
    "user_routes",
    "property_routes",
]