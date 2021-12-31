from db import mongobase


def get_connection(host_name_uri,port_no,db_name):
    mongo = mongobase.MongoConnector(host_name_uri,port_no)
    mongo.set_db(db_name)
    return mongo
