# 🏀 NBA_Analysis_TrackB
 
> Analyzing the relationship between shooting efficiency and team success across player positions in the NBA (2020–2025).
 
---
 
## Overview
 
This project investigates whether shooting efficiency (measured by eFG%) has a statistically significant impact on team win percentage, and whether that relationship varies by player position (PG, SG, SF, PF, C).
 
Data is sourced from the [Sumitro Datta NBA Stats Dataset](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats) on Kaggle, covering the 2020–2025 NBA regular seasons.
 
---
 
## Repository Structure
 
```
NBA_Analysis_TrackB/
│
├── NBA_Dataset/
│   ├── Advanced.csv
│   ├── All-Star Selections.csv
│   ├── Draft Pick History.csv
│   ├── End of Season Teams (Voting).csv
│   ├── End of Season Teams.csv
│   ├── Opponent Stats Per 100 Poss.csv
│   ├── Opponent Stats Per Game.csv
│   ├── Opponent Totals.csv
│   ├── Per 36 Minutes.csv
│   ├── Per 100 Poss.csv
│   ├── Player Award Shares.csv
│   ├── Player Career Info.csv
│   ├── Player Per Game.csv
│   ├── Player Play By Play.csv
│   ├── Player Season Info.csv
│   ├── Player Shooting.csv
│   ├── Player Totals.csv
│   ├── Team Abbrev.csv
│   ├── Team Stats Per 100 Poss.csv
│   ├── Team Stats Per Game.csv
│   ├── Team Summaries.csv
│   └── Team Totals.csv
│
├── nba_clean.py              # Data cleaning and merging script
├── NBA_Analysis.ipynb        # Exploratory data analysis and visualizations
├── NBA_Analysis.html         # Exported notebook as HTML
├── nba_analysis_data.csv     # Cleaned and merged output dataset
└── NBA_Viz.twb               # Tableau workbook for visualizations
```

---
 
---
 
## Dependencies
 
```
pandas
numpy
matplotlib
pathlib
```
 
---
 
## Contributors
 
| Contributor | Roles |
|-------------|-------|
| [Brandon Cartagena] | Data Curation, Supervision, Software, Resource, Writing - Review & Editing |
| [Shiv Patel] | Visualization, Formal Analysis, Writing - Review & Editing |
---
 
## 📄 License
 
This project is for academic purposes only. Data glossary from [Basketball Reference](https://www.basketball-reference.com/) and [NBA Dataset](https://www.kaggle.com/datasets/sumitrodatta/nba-aba-baa-stats/data) via Kaggle.
