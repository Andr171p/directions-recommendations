from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.services.sql_database.crud import BaseCRUD

from abc import ABC, abstractmethod
from pydantic import BaseModel


class SQLDatabaseRepository(ABC):
    _crud: "BaseCRUD"
    
    @abstractmethod
    async def get_all(self) -> BaseModel | None:
        raise NotImplemented
    
    @abstractmethod
    async def add(self, item: BaseModel) -> int | None:
        raise NotImplemented
    