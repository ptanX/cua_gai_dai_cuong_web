import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds151004.mlab.com:51004/binhnt5_c4e
host = "ds151004.mlab.com"
port = 51004
db_name = "binhnt5_c4e"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
