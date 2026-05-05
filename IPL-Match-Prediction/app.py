import gradio as gr
import joblib
import pandas as pd

# Load saved files
model = joblib.load('ipl_model.pkl')
model_columns = joblib.load('model_columns.pkl')
venues = joblib.load('venues.pkl')

# Current IPL teams
current_teams = [
    'Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans',
    'Kolkata Knight Riders', 'Lucknow Super Giants', 'Mumbai Indians', 
    'Punjab Kings', 'Rajasthan Royals', 'Royal Challengers Bengaluru', 
    'Sunrisers Hyderabad'
]

def predict_winner(team1, team2, venue, toss_winner, toss_decision, season):
    if team1 == team2:
        return "⚠️ Team 1 and Team 2 cannot be the same!"
    
    input_data = pd.DataFrame({
        'season': [int(season)],
        'match_type': ['League'],
        'venue': [venue],
        'team1': [team1],
        'team2': [team2],
        'toss_winner': [toss_winner],
        'toss_decision': [toss_decision]
    })
    
    # Encode
    input_encoded = pd.get_dummies(input_data,
                                   columns=['match_type', 'venue', 'team1',
                                            'team2', 'toss_decision', 'toss_winner'])
    
    # Add missing columns with 0
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    
    # Keep only model columns in correct order
    input_encoded = input_encoded[model_columns]
    
    prediction = model.predict(input_encoded)[0]
    return f"🏆 Predicted Winner: {prediction}"

# Gradio Interface
interface = gr.Interface(
    fn=predict_winner,
    inputs=[
        gr.Dropdown(current_teams, label="🏏 Team 1"),
        gr.Dropdown(current_teams, label="🏏 Team 2"),
        gr.Dropdown(sorted(venues), label="🏟️ Venue"),
        gr.Dropdown(current_teams, label="🪙 Toss Winner"),
        gr.Dropdown(['bat', 'field'], label="⚡ Toss Decision"),
        gr.Slider(2008, 2030, step=1, value=2024, label="📅 Season")
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="🏏 IPL Match Winner Prediction",
    description="Predict the winner of an IPL match based on teams, venue, toss and season.",
    examples=[
        ["Mumbai Indians", "Chennai Super Kings", "Wankhede Stadium", "Mumbai Indians", "field", 2024],
        ["Kolkata Knight Riders", "Royal Challengers Bengaluru", "Eden Gardens", "Kolkata Knight Riders", "field", 2024],
    ]
)

interface.launch()