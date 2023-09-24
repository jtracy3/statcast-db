from .base import Session, Base
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    Date,
)
from sqlalchemy.orm import relationship


class Statcast(Base):

    __tablename__ = "statcast"

    id = Column(Integer, primary_key=True, unique=True)
    game_pk = Column(Integer, nullable=False)
    game_type = Column(String, nullable=False)
    game_date = Column(Date, nullable=False)
    home_team = Column(String, nullable=False)
    away_team = Column(String, nullable=False)
    pitch_type = Column(String, nullable=True)
    pitch_name = Column(String, nullable=True)
    pitcher_id = Column(Integer, nullable=False)
    pitcher_name = Column(String, nullable=False)
    pitcher_handedness = Column(String, nullable=False)
    batter_id = Column(Integer, nullable=False)
    batter_name = Column(String, nullable=False)
    batter_handedness = Column(String, nullable=False)
    inning = Column(Integer, nullable=False)
    inning_topbot = Column(String, nullable=False)
    outs_when_up = Column(Integer, nullable=False)
    at_bat_number = Column(Integer, nullable=False)
    pitch_number = Column(Integer, nullable=False)
    release_speed = Column(Float, nullable=True)
    release_pos_x = Column(Float, nullable=True)
    release_pos_z = Column(Float, nullable=True)
    spin_axis = Column(Integer, nullable=True)
    events = Column(String, nullable=True)
    description = Column(String, nullable=False)
    zone = Column(Integer, nullable=True)
    des = Column(String, nullable=True)
    type = Column(String, nullable=False)
    hit_location = Column(Integer, nullable=True)
    bb_type = Column(String, nullable=True)
    balls = Column(Integer, nullable=False)
    strikes = Column(Integer, nullable=False)
    pfx_x = Column(Float, nullable=True)
    pfx_z = Column(Float, nullable=True)
    plate_x = Column(Float, nullable=True)
    plate_z = Column(Float, nullable=True)
    hc_x = Column(Float, nullable=True)
    hc_y = Column(String, nullable=True)
    vx0 = Column(Float, nullable=True)
    vy0 = Column(Float, nullable=True)
    vz0 = Column(Float, nullable=True)
    ax = Column(Float, nullable=True)
    ay = Column(Float, nullable=True)
    az = Column(Float, nullable=True)
    sz_top = Column(Float, nullable=True)
    sz_bot = Column(Float, nullable=True)
    hit_distance_sc = Column(Integer, nullable=True)
    launch_speed = Column(Float, nullable=True)
    launch_angle = Column(Float, nullable=True)
    effective_speed = Column(Float, nullable=True)
    release_spin_rate = Column(Integer, nullable=True)
    release_extension = Column(Float, nullable=True)
    release_pos_y = Column(Float, nullable=True)
    estimated_ba_using_speedangle = Column(Float, nullable=True)
    estimated_woba_using_speedangle = Column(Float, nullable=True)
    launch_speed_angle = Column(Integer, nullable=True)
    home_score = Column(Integer, nullable=False)
    post_home_score = Column(Integer, nullable=False)
    away_score = Column(Integer, nullable=False)
    post_away_score = Column(Integer, nullable=False)