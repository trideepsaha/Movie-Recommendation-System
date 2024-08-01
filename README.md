# Movie Recommendation System

Welcome to the Movie Recommendation System! This project leverages machine learning techniques to recommend movies based on user input. The system uses a content-based filtering approach to suggest movies similar to the one provided by the user.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Running the App](#running-the-app)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Movie Recommendation System uses a content-based approach to recommend movies. The system processes movie metadata, including genres, keywords, and overviews, to build a model that calculates similarities between movies. The recommendations are generated based on cosine similarity of the movie features.

## Running the App

You can also access a live version of the Streamlit app hosted online:

- [Movie Recommendation System](https://movie-recommendation-system-gyrr6wqk4baqcmbmfuhbsp.streamlit.app/)

## Dataset

The dataset used for this project is the TMDb Movie Metadata dataset. You can download it from the following link:

- [TMDb Movie Metadata Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Model

The model uses the following approach:

1. **Data Preprocessing**: The dataset is cleaned and processed to extract relevant features such as genres, keywords, and overviews.
2. **Feature Extraction**: Textual data is converted into numerical vectors using Bag of Words representation.
3. **Similarity Calculation**: Cosine similarity is used to measure the similarity between movies.
4. **Recommendation**: Based on the similarity scores, the system recommends movies similar to the input movie.

You can interact with the model via a Streamlit web application.

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/Movie-Recommendation-System.git
    cd Movie-Recommendation-System
    ```

2. **Install Required Packages**:

    It is recommended to use a virtual environment. Install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure you have the following dependencies in `requirements.txt`:

    ```
    pandas
    numpy
    scikit-learn
    nltk
    streamlit
    ```

3. **Download the Dataset**:

    Download the dataset from [TMDb Movie Metadata Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and place it in the project directory.

## Usage

1. **Preprocess the Data**:

    Run the preprocessing script to prepare the data and generate the similarity matrix:

    ```bash
    python preprocess_movies.py
    ```

    This script will create `movies.pkl` and `similarity.pkl` files containing the preprocessed data and similarity matrix, respectively.

2. **Run the Streamlit App**:

    Start the Streamlit application with the following command:

    ```bash
    streamlit run app.py
    ```

    Open your browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## Contributing

Contributions to the project are welcome! Please fork the repository, make your changes, and submit a pull request. For any issues or suggestions, feel free to open an issue in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to replace placeholders like `yourusername` with your actual GitHub username and adjust any links or details as needed.
