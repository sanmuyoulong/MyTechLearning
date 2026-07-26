# Instructions
# Imagine you have a dataset with information about your favorite sports team. 🏀🎾⚽ The goal is to use Python's data structures to organize and analyze this data.

# If you can't think of any, feel free to use the Super Bowl 2024 champions, the Kansas City Chiefs. 🏈

# As a data analyst for the Kansas City Chiefs you have been given a dataset containing information about the players, their positions, and some game statistics.

# Let's start analyzing!

# Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name,' 'position,' and 'jersey number.'
# Print out a list of all player positions in the dataset.
# Choose a player and update their game statistics in the dataset.
# Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.

player1 = {
    "name": "Patrick Mahomes",
    "position": "Quarterback",
    "jersey_number": 15,
    "yards_gained": 4500,
    "touchdowns": 38
}

player2 = {
    "name": "Travis Kelce",
    "position": "Tight End",
    "jersey_number": 87,
    "yards_gained": 1200,
    "touchdowns": 10
}

player3 = {
    "name": "Chris Jones",
    "position": "Defensive Tackle",
    "jersey_number": 95,
    "yards_gained": 0,
    "touchdowns": 0
}

players = [player1, player2, player3]
print("Player Positions:", [player["position"] for player in players])
player1["yards_gained"] += 300
player1["touchdowns"] += 3

# Calculate average statistics
total_yards = sum(player["yards_gained"] for player in players)
total_touchdowns = sum(player["touchdowns"] for player in players)
num_players = len(players)

avg_yards = total_yards / num_players if num_players > 0 else 0
avg_touchdowns = total_touchdowns / num_players if num_players > 0 else 0

print("Average Yards Gained:", avg_yards)
print("Average Touchdowns:", avg_touchdowns)