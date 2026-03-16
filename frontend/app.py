import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="AI MoodMate", page_icon="🎵")
st.title("🎵 AI MoodMate")

input_method = st.radio(
    "Choose input method",
    ["Upload Image", "Use Webcam"]
)

image = None

# OPTION 1 — IMAGE UPLOAD
if input_method == "Upload Image":

    uploaded_file = st.file_uploader(
        "Upload your face image",
        type=["jpg","png","jpeg"]
    )

    if uploaded_file:
        image = uploaded_file.getvalue()
        st.image(uploaded_file)

# OPTION 2 — WEBCAM
if input_method == "Use Webcam":

    captured_image = st.camera_input("Take a photo")

    if captured_image:
        image = captured_image.getvalue()

# DETECT EMOTION BUTTON
if image and st.button("Detect Emotion & Recommend Music"):

    files = {"image": image}

    response = requests.post(
        "http://127.0.0.1:5000/recommend",
        files=files
    )

    data = response.json()

    st.success(f"Detected Emotion: {data['emotion']}")

    st.markdown("### 🎧 Recommended Songs")

    for song in data["songs"]:

            st.subheader(f"{song['name']} — {song['artist']}")

            embed_url = f"https://open.spotify.com/embed/track/{song['spotify_id']}?utm_source=generator&theme=0"
            components.iframe(embed_url, height=80)