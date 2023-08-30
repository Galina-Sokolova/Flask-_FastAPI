from pydantic import BaseModel, Field
from Flask_project.HW_6.settings import settings


class ProductIn(BaseModel):
    title: str = Field(..., max_length=settings.STRING_MAX_LENGTH)
    description: str = Field(..., max_length=settings.STRING_MAX_LENGTH)
    price: float = Field(..., )


class Product(ProductIn):
    id: int
