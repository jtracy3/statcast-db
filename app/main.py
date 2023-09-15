import argparse
import os

import pandas as pd
from lib import statcast_data_test
from db.base import Base, Session, engine
from db.models import Statcast

Base.metadata.create_all(bind=engine)

db = Session()


if __name__ == "__main__":
    # get arguments for the date to pull
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", type=str)
    parser.add_argument("--end-date", type=str, default=None)
    args = parser.parse_args()

    # if os.getenv("WORKING_ENV") == "prd":
    #     stats = statcast_data(args.start_date, args.end_date)
    # elif os.getenv("WORKING_ENV") == "dev":
    #     stats = pd.read_csv("savant_data.csv")
    # else:
    #     raise Exception("Need to set variable WORKING_ENV")

    # i = 0
    stats = statcast_data_test(args.start_date, args.end_date)
    for row in stats.to_dict(orient="records"):
        # row.update({"id": i})
        statcast = Statcast(**row)
        db.add(statcast)
        db.commit()
        db.refresh(statcast)
        # i += 1

    db.close()
    print("here")