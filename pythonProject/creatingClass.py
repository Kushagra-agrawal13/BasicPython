# MarshallMathers = class
# eminem, slim_shady = object
# songs, grammy = attributes


class MarshallMathers:
    def __init__(self, songs_released, grammys):            # "pass" means if there is nothing inside a class or function , we write "pass"
        self.songs = songs_released
        self.grammy = grammys

eminem = MarshallMathers("stan", 15)

print(eminem.grammy)

slim_shady = MarshallMathers("Kim", 20)

print(slim_shady.songs)
