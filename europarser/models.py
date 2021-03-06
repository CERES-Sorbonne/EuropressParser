from typing import Literal

from pydantic import BaseModel


class FileToTransform(BaseModel):
    name: str
    file: str


class Error(BaseModel):
    message: str
    article: str
    transformer: str


class Pivot(BaseModel):
    journal: str
    date: str
    titre: str
    texte: str


OutputType = Literal["csv", "json", "txt", "xml"]
Output = Literal["pivot", "txm", "iramuteq", "gephi", "cluster_tool"]

