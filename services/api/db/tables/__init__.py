import importlib
import pkgutil

from .bases import Base, BaseThrough
from .transactions import Transaction
from .users import User

__all__ = (
    "Base",
    "BaseThrough",
    "User",
    "Transaction",
)


def discover_model_classes():
    for _, name, _ in pkgutil.walk_packages(__path__):
        importlib.import_module(f"db.tables.{name}")
