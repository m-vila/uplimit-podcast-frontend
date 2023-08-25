# AI Podcast Summarizer 🎙️

This project utilizes Large Language Models (LLMs) from OpenAI to summarize AI podcast episodes, identify key topics and highlights, and generate a personalized newsletter for the user. Try it out [here!](https://skainet-podcast.streamlit.app/)

## **The Problem** 😩

With the rising popularity of AI podcasts, it can be overwhelming to keep up with all the latest episodes and identify the most relevant ones to listen to. Manually going through show notes is time-consuming and ineffective.

## **The Solution** 💡

This project automates the process of discovering relevant AI podcast episodes by:

- Allowing users to provide a list of podcast RSS feeds they follow
- Periodically checking for new episodes from these feeds
- Using an LLM to summarize each new episode by extracting key information like guests, topics, and highlights

## **Features** ✨

**Podcast feed integration:** Users can provide a list of RSS feeds to track episodes from. New episodes are automatically detected.

**AI-powered summarization:** An LLM reads the podcast transcript and identifies important topics, guests, and highlights.

**Web interface:** Users can manage feeds and access generated summaries through a web dashboard.

## **Implementation** 🛠️

The project is broken down into three parts:

1. AI Models
- OpenAI's API is used to access LLMs for summarization and information extraction.
- A speech-to-text model generates transcripts from the podcast audio.

2. Backend
- The summarization workflow is containerized using Modal to run on demand upon new episodes.
- APIs expose functionality to the frontend.

3. Frontend
- A Streamlit web dashboard allows users to manage feeds and access summaries.
- The frontend calls backend APIs to generate and retrieve summaries.
