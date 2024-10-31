from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from models.base import Base
# from models.union import tour_union_table

class Tour(Base):
    __tablename__ = "tours"
    
    id: Mapped[int] = mapped_column("id", primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column()
    # travels: Mapped[List[Travel]] = relationship(secondary=tour_union_table)