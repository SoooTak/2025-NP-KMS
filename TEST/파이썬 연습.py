import random
class Player:
    def __init__(self, name = None) :
        self.name = name
        self.numbers = random.sample(range(10), 3)
        
    def check_strike(self, guessed_nums):
        strike_count = ball_count = 0
        for i in range(3) :
            if guessed_nums[i] == self.numbers[i] :
                strike_count += 1
            elif guessed_nums[i] in self.numbers :
                ball_count += 1
        print(f"{strike_count} strike, {ball_count} ball")
        return strike_count == 3
    
class Game:
    def __init__(self, players):
        self.players = players
    
    def play(self) :
        game_result = [False] * len(self.players)
        round_no = 1
        while(True) :
            print(f"**** round {round_no} ****")
            for i in range(len(self.players)) :
                a, b, c = map(int, (input(f"{self.players[i].name} 's turn : ").split()))
                guess = [a, b, c]
                game_result[i] = self.players[i].check_strike(guess)
            if self.check_gameover(game_result) :
                break
            round_no += 1
            
    
    def check_gameover(self, game_result) :
        if sum(game_result) :
            print(f"\n\n{'<GAME OVER>':^40}"); print('=' * 40)
            for i in range(len(game_result)) :
                if game_result[i] :
                    print(f"{self.players[i].name} win!")
            print('=' * 40)
            return True
        
if __name__ == '__main__' :
    print(f"{'<숫자야구>':^40}")
    n = int(input("게임 창가자 수 :"))
    players = [Player(input(f"{i+1}번째 참가자 : ")) for i in range(n)]
    game = Game(players)
    game.play()