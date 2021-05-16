from tinydb import TinyDB

db = TinyDB('database.json')


def create_event(event):
    return db.insert({'name': event})


def get_all_events():
    return db.all()


def remove_event_by_id(id):
    db.remove(doc_id=id)
