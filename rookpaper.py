import random
import streamlit as st

# Possible choices
CHOICES = ["Rock", "Paper", "Seizure"]

def ai_choice():
    """AI selects a move using randomness."""
    return random.choice(CHOICES)

def determine_winner(player, ai):
    """Determines the winner of the game."""
    if player == ai:
        return "It's a tie!"
    elif (player == "Rock" and ai == "Seizure") or \
         (player == "Paper" and ai == "Rock") or \
         (player == "Seizure" and ai == "Paper"):
        return "You win!"
    else:
        return "AI wins!"

# Streamlit UI
st.title("Rock-Paper-Seizure Game")
st.write("Play against an AI that makes a random move!")

# User selection
player_choice = st.radio("Choose your move:", CHOICES)

if st.button("Play"):
    ai_move = ai_choice()
    result = determine_winner(player_choice, ai_move)
    
    # Display result
    st.write(f"AI chose: **{ai_move}**")
    st.success(result)
