"""
nba_clean.py
------------
This script is responsible for cleaning the NBA dataset that contains player statistics.
The statistics spans from 1979 to now, and includes various metrics such as points per game, rebounds, assists, etc.
The dataset comes from a website called Kaggle, and is from the user Sumitro Datta.

Disclaimer: Due to the amount of data and the complexity of the dataset, our analysis will be focused on the most recent 5 seasons (2020-2025) 
to ensure that we are analyzing the most relevant and up-to-date information about NBA players. We will not be focusing on older seasons and players, 
as the game has evolved significantly over the years, and the statistics from older seasons may not be as relevant to our analysis of current player performance.

For the purpose of our analysis, we will be focusing on the following columns:
- 'Player': The name of the player and its career information.
- 'Pos': The position of the player (e.g., Guard, Forward, Center).
- 'Team': The team the player was on during the season.
- 'Shooting Efficiency': A metric that combines various shooting statistics to give an overall efficiency rating.
- 'Points Per Game': The average number of points the player scored per game during the season.
- 'Rebounds Per Game': The average number of rebounds the player grabbed per game during the season.
- 'Assists Per Game': The average number of assists the player made per game during the season.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Load the necessary datasets
player_path = Path("NBA_Dataset") / "Player Totals.csv"
team_path = Path("NBA_Dataset") / "Team Totals.csv"


nba_player = pd.read_csv(player_path)
nba_team_df = pd.read_csv(team_path)

# Exploring the datasets types and unique values. 
# Uncomment the following lines to check the data types and unique values.
print(nba_player['season'].unique()[:10])   # check int vs string format

# Filtering players from the most recent 5 seasons (2020-2025)
recent_seasons = [2020, 2021, 2022, 2023, 2024, 2025]
nba_player = nba_player[nba_player['season'].isin(recent_seasons)]
nba_team_df = nba_team_df[nba_team_df['season'].isin(recent_seasons)]



# HANDLE TOT ROWS (traded players) 
# Keep only the TOT row for players who appeared on multiple teams.
# For players on one team, keep their single row.
nba_player = nba_player.sort_values('team').drop_duplicates(
    subset=['player', 'season'], keep='first'
)
# Note: sorting puts 'TOT' last alphabetically — use this instead:
nba_player = (nba_player.sort_values('team', key=lambda x: x == 'TOT', ascending=False)
    .drop_duplicates(subset=['player', 'season'], keep='first')
)

# SELECT RELEVANT COLUMNS 
# Use shooting stats directly from Player Totals
player_cols = ['season', 'player', 'pos', 'team', 'g', 'mp', 'fg_percent', 
               'x3p_percent', 'x2p_percent', 'e_fg_percent', 'ft_percent']
player_df   = nba_player[player_cols]

team_cols = ['season', 'abbreviation']
team_cols = [c for c in team_cols if c in nba_team_df.columns] # Check if columns exist in team dataframe
nba_team_df = nba_team_df[team_cols]

# Rename abbreviation to team for merging
nba_team_df = nba_team_df.rename(columns={'abbreviation': 'team'})

# FILTER LOW SAMPLE SIZE PLAYERS 
# Drop players with very few minutes to avoid noise skewing team averages
player_df = player_df[player_df['mp'] >= 100]

# STANDARDIZE POSITION
# Some players are listed as "PF-C" or "SG-SF" — take the primary position
player_df['pos'] = player_df['pos'].str.split('-').str[0]

# Keep only the 5 standard positions
valid_positions = ['PG', 'SG', 'SF', 'PF', 'C']
player_df = player_df[player_df['pos'].isin(valid_positions)]

# SELECT FINAL COLUMNS WITH PLAYER NAMES 
final_df = player_df[['season', 'player', 'team', 'pos', 'g', 'mp', 
                       'fg_percent', 'x3p_percent', 'x2p_percent', 
                       'e_fg_percent', 'ft_percent']]

# MERGE WITH TEAM INFO
# Merge on season + team (abbreviation) just to eliminate multi-team players
final_df = final_df.merge(nba_team_df[['season', 'team']], 
                           on=['season', 'team'], how='inner')

# DROP NULLS IN KEY COLUMNS 
final_df = final_df.dropna(subset=['e_fg_percent'])

# INSPECT RESULT 
print(final_df.shape)
print(final_df.head(10))
print(final_df.isnull().sum())

# WRITE TO CSV 
output_path = Path("nba_analysis_data.csv")
final_df.to_csv(output_path, index=False)
print(f"\nData written to {output_path}")