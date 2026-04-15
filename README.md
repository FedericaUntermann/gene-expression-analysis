# 🧬 Gene Expression Analysis & Tumor Prediction API

This project implements a complete Data Science pipeline applied to gene expression data, from exploratory analysis to deploying a machine learning model as an API.

---

## 📌 Objective

To develop a model capable of predicting tumor presence based on gene expression levels and expose it through an accessible API.

---

## 🧪 Dataset

The dataset consists of gene expression data with a limited number of samples.

⚠️ Due to the small dataset size, results should be interpreted with caution.

---

## ⚙️ Project Pipeline

1. Exploratory Data Analysis (EDA)  
2. Data preprocessing  
3. Feature (gene) selection  
4. Model training  
5. Deployment as an API using FastAPI  

---

## 🤖 Model

A simple model (**Logistic Regression**) was used to reduce the risk of overfitting given the small dataset size.

---

## 🚀 API

You can test the API here:

https://gene-expression-api.onrender.com/docs

---

## 📥 Example Usage

Endpoint:
POST /predict

Example input:

```json
{
  "TOMM20": 6.2,
  "SPRED3": 2.8,
  "MITF": 2.0
}
```
Response:

```json
{
  "prediction": "tumor",
  "confidence": 0.60
}
```
---

## ⚠️ Limitations
-Very small dataset

-Potential overfitting

-Not validated on external data

---

## 📈 Future Improvements
-Use larger datasets

-Apply cross-validation

-Improve feature engineering

-Add an interactive interface (e.g., Streamlit)

---

## 🛠️ Technologies Used
-Python

-Pandas / NumPy

-Scikit-learn

-FastAPI

-Uvicorn

-Render


## 👩‍🔬 Author

Developed by Federica Untermann.
