# Crime Type Prediction

A machine learning classification project that predicts crime type based on evidence type, location, and case details.

## Dataset
- Synthetic dataset with realistic patterns (1000 samples)
- 5 crime types: Theft, Fraud, Assault, Robbery, Cyber Crime
- Features: Location, Evidence Type, Case Status, Month, Weekday

## Models & Results

| Model | Accuracy | CV Mean (5-fold) |
|---|---|---|
| Random Forest | 0.580 | 0.569 |
| Logistic Regression | 0.650 | 0.662 |

Logistic Regression outperformed Random Forest due to clear 
linear patterns in the data.

## Key Insights
- Evidence type is a strong predictor — Logs correlate with 
  Cyber Crime, Documents with Fraud
- Cross validation confirmed results are consistent, not a fluke
- Original model had 100% accuracy on just 30 rows — 
  this version uses 1000 samples for reliable evaluation
- Synthetic data showed spurious correlations in time features

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib

## Author
Rahat Khan
LinkedIn: www.linkedin.com/in/rahatkhan1305