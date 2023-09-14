import os
# from dotenv import load_dotenv

# load_dotenv(".env")

CONFIG = dict()
for key in os.environ.keys():
    CONFIG[key] = os.environ[key]