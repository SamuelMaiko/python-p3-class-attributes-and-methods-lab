class Song:
    count=0
    genres=list()
    genre_count=dict()
    artist_count=dict()
    artists=list()
    def __init__(self,name, artist, genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls,increment=1):
        cls.count+=increment

    @classmethod
    def add_to_genres(cls,new_genre):
        # if not(new_genre in cls.genres):
        cls.genres.append(new_genre)
        new_tuple=tuple(cls.genres)
        cls.genres=list(new_tuple)

    @classmethod
    def add_to_artists(cls, new_artist):
        cls.artists.append(new_artist)
        new_tuple=tuple(cls.artists)
        cls.artists=list(new_tuple)
        
    @classmethod
    def add_to_genre_count(cls,genre):
        # if not cls.genre_count:
        available_genre_keys=[key for key, value in cls.genre_count.items()]
        if genre not in available_genre_keys:
            cls.genre_count[genre]=1
        else:
            cls.genre_count[genre]+=1
    @classmethod
    def add_to_artist_count(cls,artist):
        available_artists=[key for key,value in cls.artist_count.items()]
        if artist not in available_artists:
            cls.artist_count[artist]=1
        else:
            cls.artist_count[artist]+=1
        # cls.genre_count=dict()
# song1=Song("Top scorer","Wakadinali","Drill")
# song2=Song("Rex","BBoyz","Drill")
# song3=Song("Let me down slowly","Benjamin","RnB")
# song4=Song("Tripple XL","Wakadinali","Drill")
# print(Song.artist_count)
# print(Song.genre_count)
