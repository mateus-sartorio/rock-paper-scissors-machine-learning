# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

moves_sequences_map = {}
N = 5

def player(prev_play, opponent_history=[]):
    global moves_sequences_map
    global N

    if prev_play == "":
        moves_sequences_map = {}
        opponent_history.clear()

    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < N:
        return "R"
    
    last_pattern = "".join(opponent_history[-N:])

    if last_pattern in moves_sequences_map:
        moves_sequences_map[last_pattern] += 1
    else:
        moves_sequences_map[last_pattern] = 1
    
    current_pattern = "".join(opponent_history[-(N-1):])

    potential_plays = [
        current_pattern + "R",
        current_pattern + "P",
        current_pattern + "S"
    ]

    predicted_enemy_next_play = max(potential_plays, key=lambda k: moves_sequences_map.get(k, 0))[-1]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    prediction = ideal_response[predicted_enemy_next_play]

    return prediction