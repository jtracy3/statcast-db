import datetime as dt
import pandas as pd
from pybaseball import (
    statcast,
    cache,
    playerid_reverse_lookup
)


GAME_TYPE = {
    "E": "Exhibition",
    "R": "Regular Season",
    "S": "Spring Training",
    "F": "Wild Card Series",
    "D": "Divisional Series",
    "L": "League Championship Series",
    "W": "World Series"
}

COL_LIST = [
    "game_pk",
    "game_type",
    "game_date",
    "home_team",
    "away_team",
    "pitch_type",
    "pitch_name",
    "pitcher_id",
    "pitcher_name",
    "pitcher_handedness",
    "batter_id",
    "batter_name",
    "batter_handedness",
    "inning",
    "inning_topbot",
    "outs_when_up",
    "at_bat_number",
    # "pitch_number",
    # "release_speed",
    # "release_pos_x",
    # "release_pos_z",
    # "spin_axis",
    # "events",
    # "description",
    # "zone",
    # "des",
    # "type",
    # "hit_location",
    # "bb_type",
    # "balls",
    # "strikes",
    # "pfx_x",
    # "pfx_z",
    # "plate_x",
    # "plate_z",
    # "hc_x",
    # "hc_y",
    # "vx0",
    # "vy0",
    # "vz0",
    # "ax",
    # "ay",
    # "az",
    # "sz_top",
    # "sz_bot",
    # "hit_distance_sc",
    # "launch_speed",
    # "launch_angle",
    # "effective_speed",
    # "release_spin_rate",
    # "release_extension",
    # "release_pos_y",
    # "estimated_ba_using_speedangle",
    # "estimated_woba_using_speedangle",
    # "launch_speed_angle",
    # "home_score",
    # "post_home_score",
    # "away_score",
    # "post_away_score"
]


def batter_lookup(batter_id):
    player_table = playerid_reverse_lookup(batter_id)[["key_mlbam", "name_last", "name_first"]]
    player_table["batter_name"] = (
        player_table[["name_last", "name_first"]]
        .apply(lambda x: f"{x[0].title()}, {x[0].title()}", raw=True, axis=1)
    )
    player_table = player_table[["key_mlbam", "batter_name"]].set_index("key_mlbam")
    return player_table


def clean_dates(x):
    if isinstance(x, str):
        x = x[:9]
    elif isinstance(x, (dt.date, dt.datetime)):
        x = x.strftime("%Y-%m-%d")
    return x


def clean(data):
    data_c = data.copy()
    data_c["game_type"] = data_c.game_type.map(GAME_TYPE)
    data_c = data_c[~data_c.game_type.isin(["Exhibition", "Spring Training"])]
    data_c.rename(columns={
        "pitcher": "pitcher_id",
        "batter": "batter_id",
        "player_name": "pitcher_name",
        "p_throws": "pitcher_handedness",
        "stand": "batter_handedness"
    }, inplace=True)
    batter_table = batter_lookup(data_c.batter_id)
    data_c = data_c.merge(batter_table, left_on="batter_id", right_on=batter_table.index)
    return data_c[COL_LIST]


def statcast_data(start_dt, end_dt):
    df = statcast(start_dt, end_dt)
    return clean(df)


def statcast_data_test(start_dt, end_dt):
    df = pd.read_csv("savant_data.csv")
    return clean(df)


def insert():
    pass

