import pydantic

# None is meaningful value, use this magic keyword as default value
default_none = "::None"


def to_camel(arg: str) -> str:
    return "".join(x.capitalize() or " " for x in arg.split("_"))


class CamelModel(pydantic.BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class ForeignKeyType(CamelModel):
    ref_table: str
    ref_column: str = None


class ColumnType(CamelModel):
    name: str
    type: str
    type_arg1: str = None
    type_arg2: str = None
    nullable: bool = False
    primary_key: bool = False
    foreign_key: ForeignKeyType = None
    unique: bool = False
    default: str = default_none
    comment: str = None


class TableType(CamelModel):
    name: str
    columns: list[ColumnType]


class ErdType(CamelModel):
    version: float
    tables: list[TableType]
    title: str = None
