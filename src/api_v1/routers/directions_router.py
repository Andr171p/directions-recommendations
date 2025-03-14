from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.core.entities import Direction, PointsHistory
from src.core.use_cases import DirectionUseCase, PointsUseCase
from src.api_v1.dependencies import (
    get_direction_use_case,
    get_points_use_case
)


directions_router = APIRouter(
    prefix='/ap1/v1/directions',
    tags=['Directions'],
)


@directions_router.get(path="/{direction_id}/", response_model=Direction)
async def get_by_direction_id(
        direction_id: int,
        direction_use_case: Annotated[
            DirectionUseCase,
            Depends(get_direction_use_case)
        ]
) -> JSONResponse:
    direction = await direction_use_case.get_by_direction_id(direction_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=direction.model_dump()
    )
