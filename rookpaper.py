import random
import gradio as gr

# Possible choices
CHOICES = ["Rock", "Paper", "Seizure"]

def ai_choice():
    """AI selects a move using randomness (can be replaced with Hugging Face model)."""
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

def play_game(player_choice):
    """Handles game logic when a player makes a choice."""
    ai_move = ai_choice()
    result = determine_winner(player_choice, ai_move)
    return f"AI chose: {ai_move}\n{result}"

# Gradio UI
demo = gr.Interface(
    fn=play_game,
    inputs=gr.Radio(CHOICES, label="Choose your move"),
    outputs=gr.Textbox(label="Result"),
    title="Rock-Paper-Seizure Game",
    description="Play against an AI that makes a random move! (Future versions will use a Hugging Face model.)"
)

demo.launch()
