# Heart Stroke Prediction

This project aims to predict the risk of heart stroke using machine learning algorithms based on various health-related parameters.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Heart stroke is a critical health issue, and early prediction can potentially save lives. This project employs machine learning techniques to predict the probability of a heart stroke based on factors such as age, gender, BMI, smoking habits, etc.

## Project Overview

The project includes:
- Exploratory Data Analysis (EDA)
- Data Preprocessing: Handling missing values, encoding categorical variables
- Model Training: Decision Tree, Logistic Regression, K-Nearest Neighbors (KNN), Random Forest, Support Vector Machine (SVM)
- Evaluation: Model accuracy assessment
- Streamlit Web App: A user-friendly interface to predict heart stroke risk based on user input

## Project Structure

The project structure is organized as follows:
- `dataset/`: Contains the Heart Stroke Data CSV file.
- `models/`: Stores trained machine learning models and the scaler object.
- `src/`: Contains the Python source code.
  - `data_preprocessing.py`: Code for data cleaning and preprocessing.
  - `model_training.py`: Code for training various machine learning models.
  - `app.py`: Streamlit web application for heart stroke prediction.
- `README.md`: Documentation providing an overview of the project (you are here).

## Installation

To run the project locally, follow these steps:
1. Clone this repository.
2. Install necessary Python dependencies: `pip install -r requirements.txt`.
3. Execute the Python scripts in the `src/` directory for data preprocessing, model training, and app deployment.

## Usage

- **Data Preprocessing**: Execute `data_preprocessing.py`.
- **Model Training**: Run `model_training.py` to train and save the models.
- **Web App Deployment**: Execute `streamlit run app.py` to deploy the Streamlit app locally.

## Technologies Used

- Python
- Pandas, NumPy for data manipulation
- Scikit-learn for machine learning models
- Matplotlib, Seaborn for data visualization
- Streamlit for web app deployment

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or find any issues, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
