from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists(name) VALUES(%s) RETURNING *"
    values = (artist.name)
    result = run_sql(sql, values)
    id = result[0]['id']
    return artist

def delete_all():
    pass

def select(id):
    pass

def albums(artist):
    pass


def select_all():
    pass

def delete(id):
    pass

def update(artist):
    pass
