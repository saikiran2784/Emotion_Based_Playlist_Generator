# Emotion-Based Playlist Generator

An interactive application that analyzes your mood from text input and generates a Spotify playlist based on the detected emotion. It leverages Hugging Face's Transformers for emotion analysis, Streamlit for a user-friendly web interface, and FastAPI to provide an API endpoint for external integrations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [License](#license)
- [Contact](#contact)

## Overview

The Emotion-Based Playlist Generator is designed to enhance your music listening experience by aligning playlists with your current mood. Simply input your thoughts or feelings, and the application uses a pre-trained emotion analysis model to determine the underlying emotion. Based on this, it crafts a Spotify search URL to help you quickly find a playlist that matches your mood.

## Features

- **Emotion Detection:** Uses the `j-hartmann/emotion-english-distilroberta-base` model from Hugging Face to analyze text and determine emotions such as joy, sadness, anger, anxiety, and more.
- **Mood Mapping:** Maps detected emotions to specific mood categories (e.g., "anger", "happy", "sadness", "love") to refine the playlist search.
- **Spotify Integration:** Generates a Spotify search URL based on the mapped emotion, allowing you to quickly access a playlist that suits your mood.
- **Interactive UI:** Built with Streamlit for a straightforward and interactive web experience.
- **API Access:** Provides a FastAPI endpoint (`/get_playlist`) that can be used to integrate the functionality into other applications or services.

## Technologies Used

- **Python** – Core programming language.
- **Streamlit** – For building the interactive web interface.
- **FastAPI** – To create a RESTful API endpoint.
- **Transformers (Hugging Face)** – For emotion analysis using a pre-trained model.
- **Spotify** – Utilizes Spotify's search functionality to retrieve mood-based playlists.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/emotion-based-playlist-generator.git
   cd emotion-based-playlist-generator
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

   *Make sure your `requirements.txt` includes dependencies such as `streamlit`, `fastapi`, `uvicorn`, `transformers`, and any others you are using.*

## Usage

### Running the Streamlit App

To launch the interactive web interface:

```bash
streamlit run model.py
```

Once the app is running, enter your mood or thoughts into the text area and click **Generate Playlist** to see the detected emotion and open a corresponding Spotify playlist.

### Running the FastAPI Server

To run the FastAPI API server:

```bash
uvicorn model:app --reload
```
Access the API at `http://127.0.0.1:8000/get_playlist?text=your+input`.

## Project Structure

A typical structure for the repository might look like this:

```
emotion-based-playlist-generator/
├── README.md
├── requirements.txt
├── model.py         # Contains both Streamlit and FastAPI code
```

## API Endpoints

- **GET /get_playlist**  
  - **Description:** Analyzes the provided text to detect the emotion and returns a JSON response with the detected emotion and the corresponding Spotify URL.
  - **Query Parameter:** `text` – The mood or thought input.
  - **Response Example:**

    ```json
    {
      "text" : "I just got a promotion at work and I'm feeling on top of the world!"
      "Generated emotion": "happy",
      "spotify_url": "https://open.spotify.com/search/happy"
    }
    ```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or further information, please contact [saikiran2784@gmail.com](mailto:saikiran2784@gmail.com).

---

*Happy coding and enjoy your personalized music experience!*
