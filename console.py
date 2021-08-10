import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist = Artist("Michael Jackson")
artist1 = Artist("Jack White")

album = Album("Bad", "Pop", artist)
album2 = Album("Blunderbuss", "Rock", artist1)


album_repository.save(album)
artist_repository.save(artist)

for album in album_repository.select_all():
    print(album.__dict__)



pdb.set_trace()
