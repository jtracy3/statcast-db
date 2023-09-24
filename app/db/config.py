import os


CONFIG = dict()
for key in os.environ.keys():
    CONFIG[key] = os.environ[key]