from pydantic import BaseModel


class Base(BaseModel):
    def __repr__(self) -> str:
        attrs = []
        for k, v in self.__class__.schema().items():
            attrs.append(f"{k}={v}")
        return f"{self.__class__.__name__}({attrs})"

    class Config:
        orm_mode = True
