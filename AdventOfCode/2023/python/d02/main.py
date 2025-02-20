class d02:
    def __init__(self, filename):
        self.games = {int(game.split(":")[0].split(" ", 1)[-1]): [{color.strip().split(' ')[-1]: int(color.strip().split(' ')[0]) for color in subset.strip().split(',')} for subset in game.split(":")[-1].split(";")] for game in open(filename) if game.strip() != ""}
        self.p1_check = {'red': 12, 'green': 13, 'blue': 14}
    def p1(self):
        p1_answer = 0
        for game in self.games:
            good = True
            #print('\n', game)
            for subset in self.games[game]:
                for key in subset:
                    if self.p1_check[key] < subset[key]:
                        #print(key, subset[key])
                        good = False
                        break
                if not good:
                    break
            if good:
                #print(p1_answer, '+', game)
                #input(self.games[game])
                p1_answer += game
        print("part 1 output:", p1_answer)
    def p2(self):
        power_sum = 0
        for game_id in self.games:
            base = {"red": 0, "green": 0, "blue": 0}
            power = 1
            for subset in self.games[game_id]:
                for color in subset:
                    if subset[color] > base[color]:
                        base[color] = subset[color]        
            for key in base:
                power = power * base[key]
            power_sum += power
        print("part 2 output:", power_sum)
                
        

def main():
    ex1 = d02('example')
    ex1.p1()
    
    p1 = d02('input')
    p1.p1()

    ex2 = d02('example')
    ex2.p2()

    p2 = d02('input')
    p2.p2()
main()
