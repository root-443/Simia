import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")



print(client.list_database_names())

class CodyDB :
    global db;
    global col;
    
    db = client["Produits"]
    col = db["info"]
    def __init__(self) :
        print("CodyDB launched successfuly")
    
    def CreateCollection(self,name) :
        col = db(name)
        if col in mydb.list_collection_names() :
            print("Databse exists !")
            exit()

    def Insert(self,name,price,kwrd,site):
        file = {"Name":name,"Price" : price,"Kwrd":kwrd,"Site":site}
        col.insert_one(file)
        print(col.find())





