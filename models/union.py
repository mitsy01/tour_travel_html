from sqlalchemy import Column, String, ForeignKey, Table

from models.base import Base


tour_union_table = Table(
    "tour_union_table",
    Base.metadata,
    Column("tour_id", ForeignKey("tours.id"), primary_key=True),
    Column("travel_id", ForeignKey("travel.id"), primary_key=True)
)