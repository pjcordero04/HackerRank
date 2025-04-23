def Solution(matches):
    answers = [[],[]]
    players = set()
    for a,b in matches:
        players.add(a)
        players.add(b)
    losers = [x[1] for x in matches]
    print(players)
    count = 0
    for p in players:
        for l in losers:
            if(p==l):
                count+=1
        if(count==0):
            answers[0].append(p)
        if(count==1):
            answers[1].append(p)
        count = 0
 
    answers[0].sort()
    answers[1].sort()

    return answers

matches=[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(Solution(matches))


#chat GPT faster solution

from collections import defaultdict

def lose_counter(matches):
    loss_count = defaultdict(int)
    all_players = set()

    # Count losses and track all players
    for winner, loser in matches:
        all_players.add(winner)
        all_players.add(loser)
        loss_count[loser] += 1

    # Classify players based on loss count
    zero_losses = []
    one_loss = []

    for player in all_players:
        if loss_count[player] == 0:
            zero_losses.append(player)
        elif loss_count[player] == 1:
            one_loss.append(player)

    return [sorted(zero_losses), sorted(one_loss)]