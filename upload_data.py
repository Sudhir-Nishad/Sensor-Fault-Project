from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://Sudhir-Nishad:OTAqbDiq1a3JvAWg@cluster0.ybyy5vm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="Sensor_Project"
COLLECTION_NAME='data_list'

df=pd.read_csv("C:\Users\sudhi\Desktop\sensorproject01-main\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)