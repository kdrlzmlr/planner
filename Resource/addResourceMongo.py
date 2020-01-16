import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

myDb = myclient.get_database("planner")

print(myclient.list_database_names())
print(myDb.list_collection_names())
