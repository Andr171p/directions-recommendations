from sqlalchemy.orm import Mapped, mapped_column

from src.services.database.models.base_model import BaseModel
from src.services.database.models.direction_relation_mixin import DirectionRelationMixin


class PointsModel(DirectionRelationMixin, BaseModel):
    __tablename__ = "points"

    _direction_back_populates = "points"

    year: Mapped[int] = mapped_column(nullable=False)
    points: Mapped[int] = mapped_column(nullable=False)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(year={self.year}, points={self.points})"

    def __repr__(self) -> str:
        return str(self)
