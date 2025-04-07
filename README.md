# **Crop Yield Prediction with Weather and Soil Conditions**

## **Overview**

This project aims to predict crop yield based on weather and soil conditions using machine learning techniques. It is divided into three phases:

1. **Dataset Generation** – Creating a synthetic dataset with various weather and soil conditions.  
2. **Model Training** – Training machine learning models (Random Forest, Gradient Boosting, XGBoost) to predict crop yield.  
3. **User Interface** – Building a Streamlit web app where users can input environmental factors and receive real-time crop yield predictions.

---

## **Phase 1: Dataset Generation**

A synthetic dataset is created with 100 features representing various weather and soil conditions. These features are used to predict the target variable: **crop yield**.

### **Features**

- Weather factors: temperature, rainfall, humidity, wind speed  
- Soil-related factors: moisture content, pH level, nutrient levels

### **Target Variable**

- **Crop Yield** – A continuous variable representing the predicted yield of the crop.

---

## **Phase 2: Model Training**

Multiple machine learning models are trained to predict crop yield based on the dataset generated in Phase 1. The models include:

- Random Forest  
- Gradient Boosting  
- XGBoost  

The best-performing model is selected based on metrics like R² score and RMSE, and is saved for future predictions.

---

## **Phase 3: User Interface**

A **Streamlit web application** is developed to allow users to input weather and soil conditions and receive crop yield predictions in real time using the trained model.

### **User Inputs**

- Temperature (°C)  
- Rainfall (mm)  
- Humidity (%)  
- Soil pH  
- Soil Moisture (%)  
- Other environmental factors

### **Output**

- **Predicted Crop Yield** based on the input conditions.

---

## **Requirements**

To run the project locally, ensure you have the following:

- Python 3.x  
- [Streamlit](https://streamlit.io/)  
- [XGBoost](https://xgboost.readthedocs.io/)  
- [scikit-learn](https://scikit-learn.org/)  
- `pandas`, `numpy`, `matplotlib`

---

## **Steps to Run the App Locally**

1. Clone the repository:

```bash
git clone https://github.com/mac-cloud/crop-yield-prediction.git
```

2. Navigate to the project directory:

```bash
cd crop-yield-prediction
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv prediction
```

4. Activate the virtual environment:  
   - On **Windows**:

     ```bash
     prediction\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source prediction/bin/activate
     ```

5. Install required packages:

```bash
pip install -r requirements.txt
```

6. Run the Streamlit app:

```bash
streamlit run app.py
```

---

![Project Output](output.jpeg)

---
