import pandas as pd
import random

music_df = pd.read_csv("Music Dataset/Music Info.csv")


def recommend_songs_by_emotion(emotion: str, n: int = 7, uplift: bool = False):

    emotion = emotion.lower().strip()

    if not uplift:

        if emotion == "sad":
            recs = music_df[(music_df["valence"] < 0.4) & (music_df["energy"] < 0.5)]

        elif emotion == "happy":
            recs = music_df[(music_df["valence"] > 0.6) & (music_df["energy"] > 0.5)]

        elif emotion == "angry":
            recs = music_df[(music_df["valence"] < 0.4) & (music_df["energy"] > 0.7)]

        elif emotion == "surprise":
            recs = music_df[(music_df["valence"].between(0.4,0.7)) & (music_df["energy"] > 0.6)]

        elif emotion == "fear":
            recs = music_df[(music_df["valence"] < 0.4) & (music_df["energy"].between(0.6,1.0))]

        else:  # neutral
            recs = music_df[(music_df["valence"].between(0.4,0.6)) & (music_df["energy"].between(0.4,0.6))]

    else:

        if emotion == "sad":
            recs = music_df[(music_df["valence"] > 0.6) & (music_df["energy"].between(0.4,0.7))]

        elif emotion == "angry":
            recs = music_df[(music_df["valence"] > 0.5) & (music_df["energy"] < 0.5)]

        elif emotion == "fear":
            recs = music_df[(music_df["valence"] > 0.6) & (music_df["energy"].between(0.3,0.6))]

        elif emotion == "happy":
            recs = music_df[(music_df["valence"] > 0.6) & (music_df["energy"] > 0.5)]

        elif emotion == "surprise":
            recs = music_df[(music_df["valence"].between(0.5,0.8)) & (music_df["energy"] > 0.6)]

        else:
            recs = music_df[(music_df["valence"].between(0.4,0.6)) & (music_df["energy"].between(0.4,0.6))]

    recs = recs.sample(n=min(n, len(recs)))

    return recs[["name","artist","track_id", "spotify_id"]].to_dict(orient="records")