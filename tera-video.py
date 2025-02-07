import streamlit as st

"""Extracts the video ID and returns the embeddable video URL."""
def get_embedded_url(shared_url):
    video_id = shared_url.split("/")[-1]  # Extract ID from URL
    # Remove the first 1 character from the video ID
    video_id = video_id[1:]
    return f"https://www.1024terabox.com/sharing/embed?surl={video_id}&autoplay=true&mute=false"

st.title("TeraBox Video Player")

# Use a session state key so that we can clear it programmatically
shared_url = st.text_input("Paste the TeraBox URL:", key="url_input")

if st.button("Play Video"):
    if st.session_state.url_input.strip() == "":
        st.error("Please enter a valid URL before playing the video.")
    else:
        with st.spinner("Loading video..."):
            embed_url = get_embedded_url(st.session_state.url_input)
            print(embed_url)
            st.markdown(
                f"""
                <div style="overflow: auto; max-height: 500px;">
                    <iframe src="{embed_url}" width="700" height="400" frameborder="0" allowfullscreen></iframe>
                </div>
                """,
                unsafe_allow_html=True,
            )
