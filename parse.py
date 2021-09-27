# Author:       Josh Mandzak
# File:         parse.py
# Description:  This program reads in a single text file and creates
#               a Jgraph readable output file from it

import sys

colors = [
    (1, 0, 0),      # red
    (1, 1, 0),      # yellow
    (0.5, 0, 1),    # purple
    (0, 1, 1),      # turquoise
    (0.5, 0.5, 0.5),# gray
    (0, .5, 1),     # light blue
    (1, 0, 0.5),    # magenta
    (0, 0, 1),      # blue
    (1, 0, 1),      # pink
    (1, 0.5, 0),    # orange
    (1, 1, 1),      # white
    (0, 0, 0),      # black
    (1, 0.4, 0.4),  # faded red
    (1, 0.8, 1),    # faded pink
    (1, 1, 0.8),    # tan
]

# this is the function that actually builds jgraph
def build_graph(teams, over_200):
    # this first part is just building the football field
    # this is mostly verbatim from Dr. Plank's lecture notes
    print('newgraph')

    # set the title
    team_names = list(teams)
    print(f'title font Times-Bold fontsize 24 y 11 : {team_names[0]} vs {team_names[1]}')

    # create the x axis
    print('xaxis')
    print('  min .2 max 2.8 size 5')
    print('  no_auto_hash_labels mhash 0 hash 1.8 shash 0.6')

    # create the y axis
    print('yaxis')
    print('  min 0 max 10 size 6')
    print('  nodraw')

    print('newcurve marktype box marksize 2.6 10 cfill 0 .5 0 pts 1.5 5')

    # 10 yard lines
    for i in range(9):
        print(f'newline gray 1 pts 0.2 {i+1} 1.4 {i+1}')
        print(f'newline gray 1 pts 1.6 {i+1} 2.8 {i+1}')

    print('newstring hjc vjc font Times-Italic lgray 1 fontsize 14 x 1.5')

    # this part is slightly different since we're modifying the field
    # to show fantasy points rather than yardlines
    for i in range(9):
        if over_200:
            print(f'copystring y {i+1} : {(i+1)*30}')
        else:
            print(f'copystring y {i+1} : {(i+1)*20}')

    # hash marks for each yard
    for i in range(99):
        if (i+1) % 5 == 0 and (i+1) % 10 != 0:
            print(f'newline gray 1 pts 0.2 {float((i+1)/10)} 2.8 {float((i+1)/10)}')
        else:
            print(f'newline gray 1 pts 0.97 {float((i+1)/10)} 1.03 {float((i+1)/10)}')
            print(f'newline gray 1 pts 1.97 {float((i+1)/10)} 2.03 {float((i+1)/10)}')

    print('xaxis')
    print('hash_labels fontsize 20')

    # go ahead and set some constants
    positions = list(teams[team_names[0]])
    total_scores = []
    total_scores.append(sum(list(teams[team_names[0]].values())))
    total_scores.append(sum(list(teams[team_names[1]].values())))

    factor = 0
    if over_200:
        factor = 30
    else:
        factor = 20

    # show team names and win/loss at bottom
    if total_scores[0] > total_scores[1]:
        print(f'hash_label at 0.6 : {team_names[0]}\\')
        print('WINNER')
        print(f'hash_label at 2.4 : {team_names[1]}\\')
        print('LOSER')
    else:
        print(f'hash_label at 0.6 : {team_names[0]}\\')
        print('LOSER')
        print(f'hash_label at 2.4 : {team_names[1]}\\')
        print('WINNER')

    # create the actual bars for each position
    i = 0
    for team, vals in teams.items():
        color = 0
        current_score = 0
        for key, val in vals.items():
            print('newcurve')
            print(f'  marktype box cfill {colors[color][0]} {colors[color][1]} {colors[color][2]} marksize 0.2 {val / factor}')
            if i == 0:
                print(f'  pts 0.6 {current_score + (val / (factor * 2))}')
            else:
                print(f'  pts 2.4 {current_score + (val / (factor * 2))}')

            current_score += (val / factor)
            color += 1
            
        i += 1
            
    # time to create the legend now
    num_positions = len(teams[team_names[0]])
    print('newstring fontsize 18 hjl vjc font Times-Bold x 2.9 y 9.5 : Position Colors')
    for i in range(num_positions):
        print(f'newcurve marktype box marksize 0.2 0.5 cfill {colors[num_positions-i-1][0]} {colors[num_positions-i-1][1]} {colors[num_positions-i-1][2]}')
        print(f'pts 3 {9.5 - i - 1}')
        print(f'newstring fontsize 14 hjl vjc x 3.2 y {9.5 - i - 1} : {positions[num_positions-i-1]}')


def main():
    if len(sys.argv) < 2:
        print('Usage: python parse.py [filename]')
        return
    
    fin = open(sys.argv[1], 'r')
    lines = fin.readlines()
    fin.close()

    teams_final_scores = {}
    teams = {}
    # example of what this dict might look like at the end:
    # teams = {
    #   'JOSH': {
    #            'QB': 15,
    #            'RB1': 14,
    #            ...
    #            }
    #   'JAKE': {
    #            'QB': 12,
    #            'RB1': 17,
    #            ...
    #           }
    #         }

    current_team = ''
    current_score = 0
    
    for line in lines:
        line = line.replace('\n', '')
        line = line.split(' ')

        # check and see if we have a new team
        if 'TEAM' in line:
            if current_score != 0:
                teams_final_scores[current_team] = round(current_score, 2)
                current_score = 0
            current_team = line[1]
            teams[current_team] = {}
        else:
            current_score += float(line[1])
            teams[current_team][line[0]] = float(line[1])

    teams_final_scores[current_team] = round(current_score, 2)

    # go through dict to make sure each team has the same
    # number of positions, if not, throw an error
    num_positions = 0
    for val in teams.values():
        if num_positions == 0:
            num_positions = len(val)
        else:
            if num_positions != len(val):
                print('Error: Teams have different number of players')
                return

    over_200 = False
    for val in teams_final_scores.values():
        if val > 200:
            over_200 = True

    build_graph(teams, over_200)


if __name__ == '__main__':
    main()