import pymongo
import datetime
#pretty print, used in example, puts object Id last
import pprint

from pymongo import MongoClient
client = MongoClient()

db = client['DKFinal']
collection = db['pistats']

#what the collection will be named once we insert a document
posts = db.pistats
shadow = db.shadow

#inserting what we want.alpha
#post = {'_id' : '1' ,'Temperature' : '55F'}
#postd = {'_id' : '2' ,'Pressure' : '34psi'}
#post_id = posts.insert_one(post).inserted_id
#post_id = posts.insert_one(postd).inserted_id

#updates a document in the collection or inserts one if its not there
#we use this operation for every data field we want
UM = posts.update_one({'_id' : '1'}, {'$set' : {'Temperature' : '54F'}}, upsert=True)
UM = posts.update_one({'_id' : '2'}, {'$set' : {'Pressure' : '15psi'}}, upsert=True)
UM = posts.update_one({'_id' : '3'}, {'$set' : {'Humidity' : '25%'}}, upsert=True)

#a little extra effort, creating a logged shadow with a TTL to avoid database overvolume
#UH = shadow.insert_one({'Temperature' : '77'})
#UH = shadow.create_index([('Temperature', pymongo.ASCENDING)], expireAfterSeconds = 60)


#checks to see if the posts collection has been created on the server
print(db.collection_names(include_system_collections=False))

#prints the first document within the collection.....which is within the database
pprint.pprint(posts.find_one())

#prints number of documents in collection
print(posts.count())
