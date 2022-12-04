import pandas as pd 
import pymongo 
import json 
from dataclasses import dataclass 
import os 

@dataclass
class EnvironmentVariable:
    mongo_db_url:str=os.getenv("MONGODB_URL")


env_var=EnvironmentVariable() 
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)

