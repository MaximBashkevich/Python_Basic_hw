players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_player_dict = {j_name: j_score for i_name, i_score in
                   players.items() for j_name, j_score in players.items()}
print(new_player_dict)
