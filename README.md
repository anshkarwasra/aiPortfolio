# Palcidux Project Documentation

## Project Overview

Palcidux offers three major AI-driven services:
1. **Image-Based Question Answering (Prompt-Based Image Summarization)**: Users input an image along with a related query, and the system provides an answer based on the content of the image.
2. **Prompt-Based Text Generation**: Users input a text prompt, and the system generates coherent and contextually relevant text.
3. **Car Price Prediction**: Users input the car's brand and model name, and the system predicts the car's price by retrieving other features from the backend database.

Additionally, Palcidux provides **AI-related blogs** for users to explore through designated endpoints.

The frontend is built using **TailwindCSS**, providing a modern and responsive UI, while the backend is powered by **Flask**, which handles all API requests and business logic. The car price prediction is driven by a **Decision Tree Regressor** model.

## Features

### 1. Image-Based Question Answering (Prompt-Based Image Summarization)
- **Functionality**: Users upload an image and ask a query related to that image. The system processes the image and responds with an answer based on the content.
- **Technology**: Flask manages the input and passes the image and query to an AI model capable of image summarization and answering questions based on image content.
- **API Endpoint**: `/image`
- **User Input**: Image (file) and query (text)
- **User Output**: Answer related to the image.

### 2. Prompt-Based Text Generation
- **Functionality**: Users can generate text by providing a prompt. This service is useful for content creation, storytelling, and writing assistance.
- **Technology**: Flask connects user input with a language model that generates text based on the prompt.
- **API Endpoint**: `/text-gen`
- **User Input**: Prompt (text)
- **User Output**: Generated text.

### 3. Car Price Prediction
- **Functionality**: Users input only the car's **brand** and **model**. The system predicts the car’s price by retrieving other features (such as year and mileage) from the backend.
- **Machine Learning Model**: A **Decision Tree Regressor** is used for predicting car prices. This model has been trained on car features and historical price data.
- **API Endpoint**: `/carprice`
- **User Input**: Car brand and model (text)
- **User Output**: Predicted price of the car.

### 4. AI Blogs
- **Functionality**: Palcidux also offers AI-related blogs, allowing users to read up on topics related to artificial intelligence.
- **API Endpoint**: `/blog-{blogname}`
- **User Input**: Blog name in the URL.
- **User Output**: Blog content.

## Technology Stack

### Frontend
- **TailwindCSS**: TailwindCSS is used to design a responsive and modern user interface. It enables the rapid styling of the application's components.

### Backend
- **Flask**: Flask is used for managing API requests, routing, and integration with machine learning models. It serves the core functionality for the image, text, and car price prediction services.

### Machine Learning Model
- **Decision Tree Regressor**: This model powers the car price prediction service. It is trained using a dataset of car prices and their associated features.

## How the System Works

1. **User Interface**: Users interact with Palcidux through a web-based interface built with TailwindCSS.
2. **Backend Services**: Flask handles all the backend logic, managing API requests for image-based question answering, text generation, and car price prediction, as well as serving blog content.
3. **Machine Learning**: For car price prediction, the Decision Tree Regressor model retrieves the necessary data and predicts prices based on user inputs and backend information.

## API Endpoints

### 1. Image-Based Question Answering
- **URL**: `/image`
- **Method**: POST
- **Input**: Form data with image file and query (text)
- **Output**: Answer related to the image content.

### 2. Text Generation
- **URL**: `/text-gen`
- **Method**: POST
- **Input**: JSON `{ "prompt": "text prompt" }`
- **Output**: Generated text.

### 3. Car Price Prediction
- **URL**: `/carprice`
- **Method**: POST
- **Input**: JSON `{ "brand": "car brand", "model": "car model" }`
- **Output**: Predicted price of the car.

### 4. AI Blogs
- **URL**: `/blog-{blogname}`
- **Method**: GET
- **Input**: URL parameter (blog name).
- **Output**: Blog content related to artificial intelligence.

## Installation and Setup

### Prerequisites
- Python 3.x
- Flask
- scikit-learn
- TailwindCSS

### Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   ```

2. **Install Backend Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Backend**
   ```bash
   python app.py
   ```

4. **Frontend Setup**
   Install and configure **TailwindCSS** as per the official documentation [TailwindCSS Installation Guide](https://tailwindcss.com/docs/installation).

5. **Train the Car Price Prediction Model (if needed)**
   If retraining the model is required:
   ```python
   from sklearn.tree import DecisionTreeRegressor
   # Load your dataset
   # Split data and train the model
   model = DecisionTreeRegressor()
   model.fit(X_train, y_train)
   ```

