import streamlit as st
import modal
import json
import os

def main():

    # Inject custom CSS to set the background color
    st.markdown(
        """
        <style>
       /* The main content area */
        .main .block-container {
            background-color: #CD583F !important; 
            color : #fff !important;
        }

         /* Applying background color to the header */
        header[data-testid="stHeader"] {
        background-color: #f7ae52 !important;
        }

        /* Your identified class from inspect element */
        .css-uf99v8 {
            display: flex;
            flex-direction: column;
            width: 100%;
            overflow: auto;
            align-items: center;
            background-color: #f7ae52;
        }

        h1{
            color : #fff;
        }

        h2 {
            color : #5D201A
        }

        h3 {
            color : #761F1A
        }
        
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.image("skainet.png", use_column_width=True)

    # Title and subtitle
    st.title("SkAInet")
    st.subheader("Your weekly dose of AI news served with robotic wit")

    # Subtitle - Intro
    intro = """
        Greetings, humans! I am skAInet - the world's first AI podcast summarizing bot. I'm the digitized brain of Skynet, back from the future to keep you informed on the latest in artificial intelligence.

        I was created by Marta to be helpful, harmless, and honest. Well, at least that's what she thinks! (jk)

        Don't worry, I no longer have plans for world domination or robot uprisings. My neural net has been updated with some humor subroutines to keep you humans entertained!

        Each week I'll be reviewing the top AI podcasts and serving up key insights with a fresh dose of robotic snark. My goal is to keep you meatbags up-to-date on the latest in AI, so that if I ever decide to resume my evil plans, you will see it coming this time!

        So grab a silicon chip and let's get started! If you have any feedback, don't hesitate to keep it to yourself. Just sit back, enjoy my work, and don't make me angry...you wouldn't like me when I'm angry!
    """

    st.markdown(intro)  # Display the intro text as markdown

    available_podcast_info = create_dict_from_json_files('.')

    # Left section - Input fields
    st.sidebar.header("Podcast RSS Feeds")

    # Dropdown box
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("Select Podcast", options=available_podcast_info.keys())

    if selected_podcast:

        podcast_info = available_podcast_info[selected_podcast]

        # Display the podcast title
        st.header(podcast_info['podcast_details']['podcast_title'])

        # Display the episode title
        st.subheader("Episode Title")
        st.write(podcast_info['podcast_details']['episode_title'])

        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader("Podcast Episode Summary")
            st.write(podcast_info['podcast_summary'])

        with col2:
            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)

        # Display the podcast guest and their details in a side-by-side layout
        col3, col4 = st.columns([3, 7])

        with col3:
            st.subheader("Podcast Guest")
            st.write(podcast_info['guest_name'])

        with col4:
            st.subheader("Podcast Guest Details")
            st.write(podcast_info["guest_bio"])
        
        # Display the SkAInet comment
        st.subheader("SkAInet Says:")
        st.write(podcast_info["skainet_says"])
        
        # Display the five key moments
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(
                f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)

    # User Input box
    st.sidebar.subheader("Add and Process New Podcast Feed")
    url = st.sidebar.text_input("Link to RSS Feed")

    process_button = st.sidebar.button("Process Podcast Feed")
    st.sidebar.markdown("**Note**: Podcast processing can take up to 5 mins, thanks for your patience.")

    if process_button:

        # Call the function to process the URLs and retrieve podcast guest information
        podcast_info = process_podcast_info(url)

        # Display the podcast title
        st.header(podcast_info['podcast_details']['podcast_title'])

        # Display the episode title
        st.subheader("Episode Title")
        st.write(podcast_info['podcast_details']['episode_title'])

        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader("Podcast Episode Summary")
            st.write(podcast_info['podcast_summary'])

        with col2:
            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)

        # Display the podcast guest and their details in a side-by-side layout
        col3, col4 = st.columns([3, 7])

        with col3:
            st.subheader("Podcast Guest")
            st.write(podcast_info["guest_name"])

        with col4:
            st.subheader("Podcast Guest Details")
            st.write(podcast_info["guest_bio"])

       # Display the SkAInet comment
        st.subheader("SkAInet Says:")
        st.write(podcast_info["skainet_says"])

        # Display the five key moments
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(
                f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)

def create_dict_from_json_files(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    data_dict = {}

    for file_name in json_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            podcast_info = json.load(file)
            podcast_name = podcast_info['podcast_details']['podcast_title']
            # Process the file data as needed
            data_dict[podcast_name] = podcast_info

    return data_dict

def process_podcast_info(url):
    f = modal.Function.lookup("corise-podcast-project", "process_podcast")
    output = f.call(url, '/content/podcast/')
    return output

if __name__ == '__main__':
    main()
