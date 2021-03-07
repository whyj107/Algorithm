# Ranking NBA teams
# https://www.codewars.com/kata/5a420163b6cfd7cde5000077/train/python

# 나의 풀이
def nba_cup(result_sheet, to_find):
    if to_find == "": return to_find
    dic = {"W": 0, "D": 0, "L": 0, "S": 0, "C": 0}
    for i in result_sheet.split(','):
        if to_find + ' ' in i:
            tmp = [int(j) for j in i.split(' ') if j.isdecimal()]
            if len(tmp) < 2: return f'Error(float number):{i}'

            t1, t2 = tmp[0], tmp[1]

            if i.find(to_find) != 0: t2, t1 = tmp[0], tmp[1]

            if t1-t2 > 0: dic["W"] += 1
            elif t1-t2 < 0: dic["L"] += 1
            else: dic["D"] += 1

            dic["S"] += t1
            dic["C"] += t2
    if dic["S"] == dic["C"] == 0:
        return f"{to_find}:This team didn't play!"
    else:
        return f'{to_find}:W={dic["W"]};D={dic["D"]};L={dic["L"]};Scored={dic["S"]};Conceded={dic["C"]};Points={dic["W"]*3+dic["D"]}'

# 다른 사람의 풀이
import re
def nba_cup1(result_sheet, team):
    if not team: return ""
    wins, draws, losses, points, conced = 0, 0, 0, 0, 0
    for t1, p1, t2, p2 in re.findall(r'(.+?) (\b[\d.]+\b) (.+?) (\b[\d.]+\b)(?:,|$)', result_sheet):

        if '.' in p1 or '.' in p2: return "Error(float number):{} {} {} {}".format(t1, p1, t2, p2)

        if team == t1 or team == t2:
            ptsTeam, ptsOther = map(int, (p1, p2) if t1 == team else (p2, p1))
            points += ptsTeam
            conced += ptsOther
            if ptsTeam == ptsOther:
                draws += 1
            elif ptsTeam < ptsOther:
                losses += 1
            else:
                wins += 1

    overAllScore = 3 * wins + draws
    return ("{}:This team didn't play!" if not points and not losses else
            "{}:W={};D={};L={};Scored={};Conceded={};Points={}").format(team, wins, draws, losses, points, conced,
                                                                        overAllScore)

r = (
    "Los Angeles Clippers 104 Dallas Mavericks 88,New York Knicks 101 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112,"
    "Los Angeles Lakers 111 Minnesota Timberwolves 112,Phoenix Suns 95 Dallas Mavericks 111,Portland Trail Blazers 112 New Orleans Pelicans 94,"
    "Sacramento Kings 104 Los Angeles Clippers 111,Houston Rockets 85 Denver Nuggets 105,Memphis Grizzlies 76 Cleveland Cavaliers 106,"
    "Milwaukee Bucks 97 New York Knicks 122,Oklahoma City Thunder 112 San Antonio Spurs 106,Boston Celtics 112 Philadelphia 76ers 95,"
    "Brooklyn Nets 100 Chicago Bulls 115,Detroit Pistons 92 Utah Jazz 87,Miami Heat 104 Charlotte Hornets 94,"
    "Toronto Raptors 106 Indiana Pacers 99,Orlando Magic 87 Washington Wizards 88,Golden State Warriors 111 New Orleans Pelicans 95,"
    "Atlanta Hawks 94 Detroit Pistons 106,Chicago Bulls 97 Cleveland Cavaliers 95,"
    "San Antonio Spurs 111 Houston Rockets 86,Chicago Bulls 103 Dallas Mavericks 102,Minnesota Timberwolves 112 Milwaukee Bucks 108,"
    "New Orleans Pelicans 93 Miami Heat 90,Boston Celtics 81 Philadelphia 76ers 65,Detroit Pistons 115 Atlanta Hawks 87,"
    "Toronto Raptors 92 Washington Wizards 82,Orlando Magic 86 Memphis Grizzlies 76,Los Angeles Clippers 115 Portland Trail Blazers 109,"
    "Los Angeles Lakers 97 Golden State Warriors 136,Utah Jazz 98 Denver Nuggets 78,Boston Celtics 99 New York Knicks 85,"
    "Indiana Pacers 98 Charlotte Hornets 86,Dallas Mavericks 87 Phoenix Suns 99,Atlanta Hawks 81 Memphis Grizzlies 82,"
    "Miami Heat 110 Washington Wizards 105,Detroit Pistons 94 Charlotte Hornets 99,Orlando Magic 110 New Orleans Pelicans 107,"
    "Los Angeles Clippers 130 Golden State Warriors 95,Utah Jazz 102 Oklahoma City Thunder 113,San Antonio Spurs 84 Phoenix Suns 104,"
    "Chicago Bulls 103 Indiana Pacers 94,Milwaukee Bucks 106 Minnesota Timberwolves 88,Los Angeles Lakers 104 Portland Trail Blazers 102,"
    "Houston Rockets 120 New Orleans Pelicans 100,Boston Celtics 111 Brooklyn Nets 105,Charlotte Hornets 94 Chicago Bulls 86,"
    "Cleveland Cavaliers 103 Dallas Mavericks 97")

teams = ("Los Angeles Clippers,Dallas Mavericks,New York Knicks,NYK,Atlanta Hawks,Indiana Pacers,Memphis Grizzlies,"
         "Los Angeles Lakers,Minnesota Timberwolves,Phoenix Suns,Portland Trail Blazers,New Orleans Pelicans,"
         "Sacramento Kings,Los Angeles Clippers,Houston Rockets,Denver Nuggets,Cleveland Cavaliers,Milwaukee Bucks,"
         "Oklahoma City Thunder, San Antonio Spurs,Boston Celtics,Philadelphia 76ers,Brooklyn Nets,Chicago Bulls,"
         "Detroit Pistons,Utah Jazz,Miami Heat,Charlotte Hornets,Toronto Raptors,Orlando Magic,Washington Wizards,"
         "Golden State Warriors,Dallas Maver")

print(nba_cup(r, "Boston Celtics"), "Boston Celtics:W=4;D=0;L=0;Scored=403;Conceded=350;Points=12")
print(nba_cup(r, "Boston Celt"), "Boston Celt:This team didn't play!")
