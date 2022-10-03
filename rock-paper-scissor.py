class Participant: #建立類別(參與者)
    def __init__(self, name):
        self.name = name
        self.points = 0 
        self.choice = ""
    def choose(self): #定義Method(五選一)
        self.choice = input("{name}, select rock, paper, scissor, lizard or Spock: ".format(name= self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))
    def toNumericalChoice(self):
        switcher = {
             "rock": 0,
             "paper": 1,
             "scissor": 2,
             "lizard": 3,
             "spock": 4
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:#建立類別(遊戲回合)
    def __init__(self, p1, p2):
        self.rules = [
            #比較方式(橫向(p1)對於直向(p2)判斷win or lose)
           # 0   1  2  3   4
            [0, -1, 1, 1, -1], #0
            [1, 0, -1, -1, 1], #1
            [-1, 1, 0, 1, -1], #2
            [-1, 1, -1, 0, 1], #3
            [1, -1, 1, -1, 0]  #4
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        print("Round resulted in a {result}".format(result = self.getResultAsString(result) ))
        #result:橫向(p1)相對直向(p2)對比後的結果(0:draw 1:win -1:loss)
        if result > 0:
           p1.incrementPoint()
        elif result < 0:
           p2.incrementPoint()
    def compareChoices(self, p1, p2):#定義Method(比較選擇)
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def awardPoints(self):#定義Method(獎勵積分)
        print("implement")
    def getResultAsString(self, result):#定義Method(公布該回合勝負-p1比p2)
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }       
        return res[result]

class Game:#建立類別(遊戲)
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
    def checkEndCondition(self):#定義Method(檢查結束條件-是否結束)
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):#定義Method(遊戲結束-宣布獲勝者)
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()