from backend.recommender import recommend_songs_by_emotion

songs = recommend_songs_by_emotion("sad")

for song in songs:
    print(song)