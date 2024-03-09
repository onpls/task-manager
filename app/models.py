from aiopg import Cursor
from pydantic import BaseModel


class BaseDataModel(BaseModel):

    @classmethod
    async def from_cursor(cls, cursor: Cursor) -> list:
        rows = await cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        dict_results = [dict(zip(columns, row)) for row in rows]
        model_objects = [cls(**item) for item in dict_results]
        return model_objects

    async def save(self, cursor: Cursor, table: str, pk: str):
        dict_data = self.model_dump(exclude=[pk])
        columns = ", ".join(dict_data.keys())
        template = ", ".join(["%s"] * len(dict_data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({template})"
        await cursor.execute(query, list(dict_data.values()))
