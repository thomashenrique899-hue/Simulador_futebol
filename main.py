from random import randint

teams = {
    "Cruzeiro": {
        "attack": 75,
        "midfield": 79,
        "defense": 76,
        "points": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "played": 0
    },
    "Flamengo": {
        "attack": 79,
        "midfield": 78,
        "defense": 77,
        "points": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "played": 0
    },
    "Palmeiras": {
        "attack": 78,
        "midfield": 78,
        "defense": 77,
        "points": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "played": 0
    },
    "Santos": {
        "attack": 74,
        "midfield": 73,
        "defense": 72,
        "points": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "played": 0
    },
    "Juventude": {
        "attack": 70,
        "midfield": 70,
        "defense": 69,
        "points": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "played": 0
    },
    "Ponte Preta": {
        "attack": 67,
        "midfield": 66,
        "defense": 65,
        "points": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "played": 0
    }
}

#Calcula a força do time de acordo com os overs de defesa, meio e ataque
def calculate_strength(team1, team2):
    team_overall = (team1["attack"] + team1["midfield"] + team1["defense"]) / 3
    attack_difference = team1["attack"] - team2["defense"]
    
    return team_overall + attack_difference

#Calcula os gols de acordo com a força dos times
def calculate_goals(strength):
    if strength <= 70:
        return randint(0,2)
    elif 71 <= strength <= 80:
        return randint(0,3)
    elif strength > 80:
        return randint(0,4)

def simulate_match(home_team, away_team):
    if home_team in teams and away_team in teams:

        home_team_strength = calculate_strength(teams[home_team], teams[away_team])
        away_team_strength = calculate_strength(teams[away_team], teams[home_team])

        home_team_goals = calculate_goals(home_team_strength)
        away_team_goals = calculate_goals(away_team_strength)

        #Calcula e insere no dicionário jogos, gols sofridos e feitos
        teams[home_team]["played"] += 1
        teams[away_team]["played"] += 1
        teams[home_team]["goals_for"] += home_team_goals
        teams[away_team]["goals_for"] += away_team_goals
        teams[home_team]["goals_against"] += away_team_goals
        teams[away_team]["goals_against"] += home_team_goals

        #Printa o resultado e o vencedor e insere as derrotas, vitórias, empates e pontos no dicionário
        print(f"{home_team} {home_team_goals} x {away_team_goals} {away_team}")

        if home_team_goals > away_team_goals:
            teams[home_team]["wins"] += 1
            teams[away_team]["losses"] += 1
            teams[home_team]["points"] += 3
            print(f"Winner: {home_team}")

        elif away_team_goals > home_team_goals:
            teams[home_team]["losses"] += 1
            teams[away_team]["wins"] += 1
            teams[away_team]["points"] += 3
            print(f"Winner: {away_team}")

        else:
            teams[home_team]["draws"] += 1
            teams[away_team]["draws"] += 1
            teams[home_team]["points"] += 1
            teams[away_team]["points"] += 1
            print("Draw")

    else:
        print("Select one of these teams: ")
        for key in teams.keys():
            print(key)

def show_table():

    print(f"{'TEAM':<15}{'PTS':>4}{'P':>4}{'W':>4}{'D':>4}{'L':>4}{'GF':>5}{'GA':>5}{'GD':>5}")

    organized = sorted(
        teams.items(),
        key=lambda item: (
            item[1]["points"],
            item[1]["wins"],
            item[1]["goals_for"] - item[1]["goals_against"],
            item[1]["goals_for"]
        ),
        reverse=True
    )

    for team, stats in organized:

        goal_difference = stats["goals_for"] - stats["goals_against"]

        print(
            f"{team:<15}"
            f"{stats['points']:>4}"
            f"{stats['played']:>4}"
            f"{stats['wins']:>4}"
            f"{stats['draws']:>4}"
            f"{stats['losses']:>4}"
            f"{stats['goals_for']:>5}"
            f"{stats['goals_against']:>5}"
            f"{goal_difference:>5}"
        )

simulate_match("Cruzeiro", "Palmeiras")
simulate_match("Santos", "Juventude")
simulate_match("Flamengo", "Ponte Preta")

show_table()
