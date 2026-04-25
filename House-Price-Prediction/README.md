<<<<<<< HEAD
# House Price Prediction

A machine learning project that predicts California house prices 
using the California Housing dataset from sklearn.

## Overview
Compared two models — Linear Regression and Random Forest — to predict
house prices based on neighbourhood features like income, location, 
occupancy and house age.

## Dataset
- California Housing Dataset (sklearn built-in)
- 20,640 samples, 8 features
- Target variable: Median house price (in hundreds of thousands)

## Models & Results

| Model | MAE | MSE | R2 Score |
|---|---|---|---|
| Linear Regression | 0.533 | 0.556 | 0.576 |
| Random Forest | 0.328 | 0.255 | 0.805 |

Random Forest outperformed Linear Regression by 0.229 in R2 Score.

## Key Insights
- **MedInc (Median Income)** was the most important feature by far —
  neighbourhood income is the strongest predictor of house price
- **Location (Latitude/Longitude)** matters significantly — 
  coastal California areas are considerably more expensive
- **AveOccup** negatively impacts price — overcrowded houses 
  signal lower income neighbourhoods
- Dataset has a price cap at 5.0 ($500,000) which affects 
  model performance on high value houses

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib

## Author
Rahat Khan
LinkedIn: www.linkedin.com/in/rahatkhan1305
=======
# Crime Type Prediction using Machine Learning

## Overview
This project uses Machine Learning to predict the type of crime based on
location, evidence type, case status, and date-based features.

The goal is to demonstrate an end-to-end Data Science workflow:
- Data cleaning
- Feature engineering
- Encoding categorical variables
- Model training and evaluation
- Feature importance analysis

## Dataset
The dataset contains fictional crime case records with the following fields:
- Case ID
- Crime Type (target variable)
- Location
- Date
- Evidence Type
- Case Status

## Machine Learning Model
- Algorithm: Random Forest Classifier
- Features:
  - Location (encoded)
  - Evidence Type (encoded)
  - Case Status (encoded)
  - Day, Month, Weekday (from date)

## Results
- Accuracy achieved on test set (small dataset)
- Feature importance visualization used to interpret the model

> Note: This dataset is small and used for learning purposes. High accuracy
does not indicate a production-ready model.

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib

## Author
Rahat Khan
>>>>>>> d02714f (Initial commit: Crime type prediction using Random forest)
>>>>>>> 3f0eb29041f6872c20c9753526b2627542818a5c
