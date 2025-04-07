# Crop Yield Prediction with Weather and Soil Conditions

## Overview
This project aims to predict crop yield based on weather and soil conditions using machine learning techniques. The project is divided into three phases:
1. **Dataset Generation**: Creating a synthetic dataset with various weather and soil conditions.
2. **Model Training**: Training machine learning models (Random Forest, Gradient Boosting, XGBoost) to predict crop yield.
3. **User Interface**: Building a Streamlit web app where users can input environmental factors and get real-time crop yield predictions.

## Phase 1 - Dataset Generation
A synthetic dataset is created with 100 features representing various weather conditions (temperature, rainfall, humidity, etc.) and soil-related factors. These features are used to predict the target variable: **crop yield**.

### Features:
- Weather factors like temperature, rainfall, humidity, and wind speed.
- Soil-related factors such as moisture content, pH level, and nutrient levels.

### Target Variable:
- **Crop yield**: A continuous variable representing the predicted crop yield.

## Phase 2 - Model Training
We train several machine learning models to predict crop yield based on the dataset generated in Phase 1. The models evaluated include:
- Random Forest
- Gradient Boosting
- XGBoost

The best-performing model is selected based on metrics like R² score and RMSE. The selected model is then saved for future predictions.

## Phase 3 - User Interface
A **Streamlit web app** is developed to allow users to input weather and soil conditions, and receive real-time crop yield predictions based on the trained model.

### User Input:
- Temperature (°C)
- Rainfall (mm)
- Humidity (%)
- Soil pH
- Soil Moisture (%)
- Other environmental factors

### Output:
- Predicted crop yield based on the input conditions.

## Requirements
To run the project locally, you'll need the following libraries and tools:
- Python 3.x
- [Streamlit](https://streamlit.io/)
- [XGBoost](https://xgboost.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/)
- pandas
- numpy
- matplotlib

### Install Required Packages:

pip install -r requirements.txt

git clone https://github.com/mac-cloud/crop-yield-prediction.git

cd crop-yield-prediction
# Run
streamlit run app.py


![Project Output](output.jpeg)
