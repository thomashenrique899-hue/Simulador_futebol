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
        "goals_against": 0
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
        "goals_against": 0
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
        "goals_against": 0
    },
    "Corinthians": {
        "attack": 78,
        "midfield": 73,
        "defense": 73,
        "points": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0
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
        "goals_against": 0
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
        "goals_against": 0
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
        "goals_against": 0
    }
}

#Calcula a força do time de acordo com os overs de defesa, meio e ataque
def calculate_strength(team):
    return team["attack"] + team["midfield"] + team["defense"] / 3

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

        home_team_strength = calculate_strength(teams[home_team])
        away_team_strength = calculate_strength(teams[away_team])

        home_team_goals = calculate_goals(home_team_strength)
        away_team_goals = calculate_goals(away_team_strength)

        #Calcula e insere no dicionário gols sofridos e feitos
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

simulate_match("Palmeiras", "Cruzeiro")
simulate_match("Juventude", "Flamengo")
simulate_match("Ponte Preta", "Juventude")
