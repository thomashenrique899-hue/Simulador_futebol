from random import randint

teams = {
    "Cruzeiro": {
        "attack": 75,
        "midfield": 79,
        "defense": 76
    },
    "Flamengo": {
        "attack": 79,
        "midfield": 78,
        "defense": 77
    },
    "Palmeiras": {
        "attack": 78,
        "midfield": 78,
        "defense": 77
    },
    "Corinthians": {
        "attack": 78,
        "midfield": 73,
        "defense": 73
    },
    "Santos": {
        "attack": 74,
        "midfield": 73,
        "defense": 72
    },
    "Juventude": {
        "attack": 70,
        "midfield": 70,
        "defense": 69
    },
    "Ponte Preta": {
        "attack": 67,
        "midfield": 66,
        "defense": 65
    }
}
       
def calculate_strength(team):
    return sum(team.values()) / len(team)

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

        print(f"{home_team} {home_team_goals} x {away_team_goals} {away_team}")
        if home_team_goals > away_team_goals:
            print(f"Winner: {home_team}")
        elif away_team_goals > home_team_goals:
            print(f"Winner: {away_team}")
        else:
            print("Draw")

    else:
        print("Select one of these teams: ")
        for key in teams.keys():
            print(key)

simulate_match("Palmeiras", "Cruzeiro")
simulate_match("Juventude", "Flamengo")
simulate_match("Ponte Preta", "Juventude")
