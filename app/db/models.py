from .base import Session, Base
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    BigInteger,
    DateTime,
)
from sqlalchemy.orm import relationship


class Statcast(Base):

    __tablename__ = "statcast"

    id = Column(BigInteger, primary_key=True, unique=True)
    game_pk = Column(BigInteger, nullable=False)
    game_type = Column(String, nullable=False)
    game_date = Column(String, nullable=False)
    home_team = Column(String, nullable=False)
    away_team = Column(String, nullable=False)
    pitch_type = Column(String, nullable=False)
    pitch_name = Column(String, nullable=False)
    pitcher_id = Column(BigInteger, nullable=False)
    pitcher_name = Column(BigInteger, nullable=False)
    pitcher_handedness = Column(String, nullable=False)
    batter_id = Column(BigInteger, nullable=False)
    batter_name = Column(String, nullable=False)
    batter_handedness = Column(String, nullable=False)
    inning = Column(BigInteger, nullable=False)
    inning_topbot = Column(String, nullable=False)
    outs_when_up = Column(BigInteger, nullable=False)
    at_bat_number = Column(BigInteger, nullable=False)
    pitch_number = Column(BigInteger, nullable=False)

    def __init__(self):
        pass
