"""This Program impliments the basic form of popular dice game 'Yatzy'.
In this ,program starts with asking number of players .then the users
will get a change to enter their names.The user will be given 3 Choises
the user has to input choice in the form of '1','2','3'.
'Start' will initiate the game .In 'Edit' the player can re-enter number
of players and names .'Exit' will terminate the code.Every input has to
be concluded with an enter """
from random import randint
from collections import namedtuple
from collections import Counter
from collections import OrderedDict

NAME_LIST = []
CATEGORY = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
            "Pairs", "Two Pairs", "Three of a Kind",
            "Four of a Kind", "Small Stright", "Large Stright",
            "Full House", "Chance", "Yatzy"]
PLAYERS = {}
TOTAL = {}

def insert_player():
    """Input Number of Players and names"""
    p_no = int(input("Enter Number of PLAYERS : "))
    NAME_LIST.clear()
    for i in range(p_no):
        NAME_LIST.append(input("Enter Name of the Player {} : ".format(i+1)))
    NAME_LIST.sort()

def intilise():
    """Initilises all variable depending on Number of players"""
    scoreing_pad = {}
    five_dice = {}
    for i in CATEGORY:
        scoreing_pad[i] = 0
        five_dice[i] = [0, 0, 0, 0, 0]

    NT_player = namedtuple("player", ["Name", "ScoringPad", "Dice"])
    PLAYERS.clear()
    for i in NAME_LIST:
        PLAYERS[i] = NT_player(i, scoreing_pad.copy(), five_dice.copy())
        TOTAL[i] = 0

def dice_generator(num):
    """Yields random integers from 1-6 depecting a Dice"""
    i = 0
    while i < num:
        temp = randint(1, 6)
        i += 1
        try:
            yield temp
        except GeneratorExit:
            return

def keep():
    """Returns list of Dice that are to be rolled again"""
    flag = True
    keep_list = []
    roll_list = []
    while flag:
        n_dice = int(input("Enter Number of Dice you want keep : "))
        if 0 < n_dice <= 5:
            for i in range(n_dice):
                temp = int(input("Enter Dice Number to keep: "))
                if 0 < temp <= 5:
                    keep_list.append(temp-1)
                else:
                    print("Invalid Input : ")
                    keep_list.clear()
                    break
            flag = False
        else:
            print("Invalid Input ")

    for i in range(5):
        if i not in keep_list:
            roll_list.append(i)
    return roll_list

def dice_roll():
    """Returns list five Dices values after finalizing"""
    no_dice = 5
    dice_list = [0, 1, 2, 3, 4]
    rolled_list = [0, 0, 0, 0, 0]

    for i in range(3):
        print("\n\tDice:1\tDice:2\tDice:3\tDice:4\tDice:5")
        roll = dice_generator(no_dice)
        for j in dice_list:
            rolled_list[j] = next(roll)
            #close(Roll)
        print("\t", rolled_list[0], "\t", rolled_list[1], "\t", rolled_list[2],
              "\t", rolled_list[3], "\t", rolled_list[4],)
        flag = True
        ch_2 = ''
        while flag and i < 2:
            ch_2 = input("Do You want to keep or Finilize (Y/N/F) : ")
            if ch_2 in ('y', 'Y'):
                dice_list = keep()
                no_dice = len(dice_list)
                flag = False
            elif ch_2 in ('n', 'N'):
                flag = False
            elif ch_2 in ('f', 'F'):
                return rolled_list
            else:
                print("Invalid Choise ")
    return rolled_list

def game_start():
    """Saves five dice for each and every player and category"""
    k = 0
    for i in CATEGORY:
        k += 1
        for j in NAME_LIST:
            print("*************************************************")
            print("\nRound ", k, " : ", i, " -> ", j)
            PLAYERS[j].Dice[i] = dice_roll()

def ones(p_name):
    """Counting and storing score for Ones category """
    temp_l = PLAYERS[p_name].Dice["Ones"]
    count = temp_l.count(1)
    PLAYERS[p_name].ScoringPad["Ones"] = count

def twos(p_name):
    """Counting and storing score for Twos category """
    temp_l = PLAYERS[p_name].Dice["Twos"]
    count = temp_l.count(2)
    PLAYERS[p_name].ScoringPad["Twos"] = count*2

def threes(p_name):
    """Counting and storing score for Threes category """
    temp_l = PLAYERS[p_name].Dice["Threes"]
    count = temp_l.count(3)
    PLAYERS[p_name].ScoringPad["Threes"] = count*3

def fours(p_name):
    """Counting and storing score for Fours category """
    temp_l = PLAYERS[p_name].Dice["Fours"]
    count = temp_l.count(4)
    PLAYERS[p_name].ScoringPad["Fours"] = count*4

def fives(p_name):
    """Counting and storing score for Fives category """
    temp_l = PLAYERS[p_name].Dice["Fives"]
    count = temp_l.count(5)
    PLAYERS[p_name].ScoringPad["Fives"] = count*5

def sixes(p_name):
    """Counting and storing score for Sixes category """
    temp_l = PLAYERS[p_name].Dice["Sixes"]
    count = temp_l.count(6)
    PLAYERS[p_name].ScoringPad["Sixes"] = count*6

def pairs(p_name):
    """Counting and storing score for Pairs category """
    temp_l = PLAYERS[p_name].Dice["Pairs"]
    count_list = Counter(temp_l)
    temp_1 = 0
    for key, values in count_list.items():
        if values >= 2:
            temp_2 = key*2
            if temp_1 < temp_2:
                temp_1 = temp_2
    PLAYERS[p_name].ScoringPad["Pairs"] = temp_1

def two_pairs(p_name):
    """Counting and storing score for Two Pairs category """
    temp_l = PLAYERS[p_name].Dice["Two Pairs"]
    count_list = Counter(temp_l)
    temp = 0
    cn_pair = 0
    for key, values in count_list.items():
        if values >= 2:
            temp = temp + key*2
            cn_pair = cn_pair + 1
    if cn_pair < 2:
        temp = 0
    PLAYERS[p_name].ScoringPad["Two Pairs"] = temp

def three_kind(p_name):
    """Counting and storing score for Three of Kind category """
    temp_l = PLAYERS[p_name].Dice["Three of a Kind"]
    count_list = Counter(temp_l)
    temp = 0
    for key, values in count_list.items():
        if values >= 3:
            temp = temp + key*3
    PLAYERS[p_name].ScoringPad["Three of a Kind"] = temp

def four_kind(p_name):
    """Counting and storing score for Four of a kind category """
    temp_l = PLAYERS[p_name].Dice["Four of a Kind"]
    count_list = Counter(temp_l)
    temp = 0
    for key, values in count_list.items():
        if values >= 4:
            temp = temp + key*4
    PLAYERS[p_name].ScoringPad["Four of a Kind"] = temp

def small_stright(p_name):
    """Counting and storing score for Small Stright category """
    temp_l = PLAYERS[p_name].Dice["Small Stright"]
    small_list = [1, 2, 3, 4, 5]
    temp_l.sort()
    if temp_l == small_list:
        temp = 15
    else:
        temp = 0
    PLAYERS[p_name].ScoringPad["Small Stright"] = temp

def large_stright(p_name):
    """Counting and storing score for Large Stright category """
    temp_l = PLAYERS[p_name].Dice["Large Stright"]
    large_list = [2, 3, 4, 5, 6]
    temp_l.sort()
    if temp_l == large_list:
        temp = 20
    else:
        temp = 0
    PLAYERS[p_name].ScoringPad["Large Stright"] = temp

def full_house(p_name):
    """Counting and storing score for Full House category """
    temp_l = PLAYERS[p_name].Dice["Full House"]
    count_list = Counter(temp_l)
    temp = 0
    if 3 in count_list.values() and 2 in count_list.values():
        temp = sum(temp_l)
    PLAYERS[p_name].ScoringPad["Full House"] = temp

def chance(p_name):
    """Counting and storing score for Chance category """
    temp_l = PLAYERS[p_name].Dice["Chance"]
    temp = sum(temp_l)
    PLAYERS[p_name].ScoringPad["Chance"] = temp

def yatzy(p_name):
    """Counting and storing score for Yatzy category """
    temp_l = PLAYERS[p_name].Dice["Yatzy"]
    count_list = Counter(temp_l)
    temp = 0
    if 5 in count_list.values():
        temp = 50
    PLAYERS[p_name].ScoringPad["Yatzy"] = temp

def total_score(p_name):
    """Adds scores from all Categories and stores total """
    temp = 0
    for i in CATEGORY:
        temp = temp+PLAYERS[p_name].ScoringPad[i]
    TOTAL[p_name] = temp

def get_result():
    """Calls all the function for each players """
    for i in NAME_LIST:
        ones(i)
        twos(i)
        threes(i)
        fours(i)
        fives(i)
        sixes(i)
        pairs(i)
        two_pairs(i)
        three_kind(i)
        four_kind(i)
        small_stright(i)
        large_stright(i)
        full_house(i)
        chance(i)
        yatzy(i)
        total_score(i)

def print_result():
    """Prints the final result """
    sort = OrderedDict(sorted(TOTAL.items(), key=lambda kv: kv[1],
                              reverse=True))
    print("-------- Scores --------")
    for name, score in sort.items():
        print(name, " = ", score)

def start():
    """Calls all primary Functions """
    intilise()
    game_start()
    get_result()
    print_result()

print("***** YATZY *****")
insert_player()
while True:
    print("\n~~~~~~ YATZY ~~~~~~~ ")
    print("1.Start \n2.Edit PLAYERS \n3.Exit ")
    CHOICE = input("Enter your Choice : ")
    if CHOICE == '1':
        start()
    elif CHOICE == '2':
        insert_player()
    elif CHOICE == '3':
        exit(0)
    else:
        print("Invalid Choice")
