# 🏏 IPL Match Winner Prediction

A machine learning project that predicts IPL match winners based on 
teams, venue, toss decision, and historical performance features.

## 🚀 Live Demo
👉 [Try the app here](https://huggingface.co/spaces/Rahat1311/ipl-match-predictor)

## Dataset
- IPL Matches dataset 2008-2024 (1044 matches after cleaning)
- Source: Kaggle — IPL Complete Dataset
- Features: Teams, Venue, Toss Decision, Season

## Models & Results

| Model | CV Accuracy |
|---|---|
| Logistic Regression | 51.9% |
| Random Forest | 49.8% |
| KNN | 44.2% |

Best Model: Logistic Regression (most consistent across folds)

## Feature Engineering
6 custom features engineered using expanding window approach
to prevent data leakage:
- Team historical win rate
- Head to head win rate
- Venue win rate per team
- Team recent form (last 5 matches)

## Key Insights
- Season year was the strongest predictor — team strengths 
  shift significantly across IPL eras
- Fielding first gives 53.9% win rate vs 45.4% for batting first
- Despite feature engineering, accuracy remained ~52% — confirming 
  that IPL outcomes depend heavily on factors not captured in 
  pre-match data (player form, pitch, weather)
- Cross validation revealed Random Forest was overfitting on 
  single splits — LR was most reliable

## Data Cleaning
- Fixed team name inconsistencies (Delhi Daredevils → Delhi Capitals etc.)
- Merged duplicate venue names (58 → 39 unique venues)
- Removed defunct franchises (Kochi Tuskers, Pune Warriors etc.)
- Fixed data leakage from defunct team encoded columns

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Gradio
- Joblib
- Hugging Face Spaces

## Author
Rahat Khan
LinkedIn: www.linkedin.com/in/rahatkhan1305