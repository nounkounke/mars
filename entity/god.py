from pydantic import BaseModel


class God(BaseModel):
    name: str
    powers: str
    description: str
