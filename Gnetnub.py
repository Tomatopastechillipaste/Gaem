import random

# คลาสผู้เล่น
class SingMeSheWit:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.anti = False
        self.status = ""
        self.useanti = 0

    def IsAlive(self):
        if self.hp <= 0:
            return False
        else:
            return True
        
    def DisplayVisables(self, roundNum):

        print(f"[Round: {roundNum} 》》Turn: {self.name}]")
        print(f"________________________________________________________________________________")
        print(f"    P1 => HP: {SMSI.hp}                                          P2 => HP: {SMSII.hp}")
        print(f"          MN: {SMSI.mana}                                                 MN: {SMSII.mana}")
        print(f"                 {SMSI.status}                                           {SMSII.status}") 

        if SMSI.anti == True and SMSII.anti == False:
            print("                        _____")
            print("           /\__/\      /     \                                   ( )__( )")
            print("          ( ● ^ ●)     \     /                                   (● ^ ● )")
            print("         /(______)\/    \   /                                  \/(______)\\")
            print("           |    |        \_/                                      |    |")
        elif SMSI.anti == False and SMSII.anti == True:
            print("                                                      _____")
            print("           /\__/\                                    /     \     ( )__( )")
            print("          ( ● ^ ●)                                   \     /     (● ^ ● )")
            print("         /(______)\/                                  \   /    \/(______)\\")
            print("           |    |                                      \_/        |    |")
        elif SMSI.anti == True and SMSII.anti == True:
            print("                        _____                        _____")
            print("           /\__/\      /     \                      /     \     ( )__( )")
            print("          ( ● ^ ●)     \     /                      \     /     (● ^ ● )")
            print("         /(______)\/    \   /                        \   /    \/(______)\\")
            print("           |    |        \_/                          \_/        |    |")
        else:
            print("           /\__/\                                                ( )__( )")
            print("          ( ● ^ ●)                                               (● ^ ● )")
            print("         /(______)\/                                           \/(______)\\")
            print("           |    |                                                 |    |")

        print("          P1: Meme                                                P2: Nunu")        
        print("________________________________________________________________________________")
        print(f"{self.name} 》》CHOOSE")
        print("S = Small attack " \
        "| M = Medium attack " \
        "| L = Large attack " \
        "| XL = Xtra Large attack " \
        "| R = Random attack " \
        "| P = Purloin (Stealing HP or MN) " \
        "\nAM = Anit Minimise (Protect HP) " \
        "| PM = Purchase Mana (-5 HP : +1 MN) " \
        "| ATP = Add To health Points (+250 HP) ")
    # def DisplayCharacter(self):

# ฟังก์ชันใช้สกิล
def Smallattack(player, opponent):
    player.mana -= 25
    damage = random.randint(10, 50)    
    if opponent.anti == True:
        damage = 0
        opponent.anti = False
    opponent.hp -= damage
    opponent.status = f"-{damage}"
    player.status = ""

def Mediumattack(player, opponent):
    player.mana -= 50
    if random.randint(1, 100) < 75:
        damage = random.randint(50, 75)
        if opponent.anti == True:
            damage = 0
            opponent.anti = False
        opponent.hp -= damage
        opponent.status = f"-{damage}"
        player.status = ""
    else:
        player.status = "Missed"
        opponent.status = ""
    
def Largeattack(player, opponent):
    player.mana -= 75
    if random.randint(1, 100) < 50:
        damage = random.randint(150, 175)
        if opponent.anti == True:
            damage = 0
            opponent.anti = False
        opponent.hp -= damage
        opponent.status = f"-{damage}"

        player.status = ""
    else:
        player.status = "Missed"
        opponent.status = ""
    
def XtraLargeattack(player, opponent):
    player.mana -= 100
    if random.randint(1, 100) < 25:
        damage = random.randint(350, 500)
        if opponent.anti == True:
            damage = 0
            opponent.anti = False
        opponent.hp -= damage
        opponent.status = f"-{damage}"
        player.status = ""
    else:
        player.status = "Missed"
        opponent.status = ""
    
def Randomattack(player, opponent):
    player.mana -= 25
    damage = random.randint(0, 500)
    if opponent.anti == True:
            damage = 0
            opponent.anti = False
    opponent.hp -= damage
    opponent.status = f"-{damage}"
    player.status = ""

def Purloin(player, opponent, hm):
    if random.randint(1, 100):
        print(hm)
        if hm.lower() == "hp":
            damage = random.randint(0, 100)
            if player.hp + damage >= 1000:
                damage = 1000 - player.hp
            player.hp += damage
            player.status = f"+{damage}"
            opponent.hp -= damage
            opponent.status = f"-{damage}"               
        elif hm.lower() == "mn":
            damage = random.randint(0, 10)
            if player.mana + damage >= 100:
                damage = 100 - player.mana
            # print(damage)
            player.mana += damage
            player.status = f"+{damage}"            
            opponent.mana -= damage
            opponent.status = f"-{damage}"

    else:
        player.status = "Missed"
        opponent.status = ""

def AnitMinimise(player, opponent, Round):
    player.mana -= 25
    if random.randint(1, 100) < 50:
        player.anti = True
        player.useanti = Round
        opponent.status = "" 
        player.status = ""     
    else:
        player.status = "Missed"
        opponent.status = ""

def PurchaseMana(player, opponent, mp):
    player.hp -= mp*5
    player.mana += mp
    player.status = f"+{mp}"
    opponent.status = ""

def AddTohealthPoints(player, opponent):
    player.mana -= 100
    player.hp += 250
    player.status = "+250"
    opponent.status = ""

def Chosen(code, player, opponent, Round):
    code=code.lower()
    if code == "s" and player.mana >= 25:
        Smallattack(player, opponent)
    elif code == "m" and player.mana >= 50:
        Mediumattack(player, opponent)
    elif code == "l" and player.mana >= 75:
        Largeattack(player, opponent)
    elif code == "xl" and player.mana >= 100:
        XtraLargeattack(player, opponent)
    elif code == "r" and player.mana >= 25:
        Randomattack(player, opponent)
    elif code == "p" and player.mana >= 0:
        hm = input("Purloin HP or MN: ")      
        Purloin(player, opponent, hm)
    elif code == "am" and player.mana >= 25:
        AnitMinimise(player, opponent, Round)
    elif code == "pm":
        mp = input("Purchase Mana: ")
        if player.hp >= mp*5:
            PurchaseMana(player, opponent, mp)
    elif code == "atp" and player.mana >= 100:
        AddTohealthPoints(player, opponent)
    else:
        print("Choose again: ")



# เริ่มเกม
SMSI = SingMeSheWit("Meme", 1000, 100)
SMSII = SingMeSheWit("Nunu", 1000, 100)


# แสดงผลลัพธ์เมื่อเกมจบ
Round = 1
SMSI.DisplayVisables(Round)
while SMSI.IsAlive() and SMSII.IsAlive():

    code = input("CHOOSE: ")
    Chosen(code, SMSI, SMSII, Round)
    SMSII.DisplayVisables(Round)
    code = input("CHOOSE: ")
    Chosen(code, SMSII, SMSI, Round)
    Round += 1
    SMSI.DisplayVisables(Round)


    if Round - SMSI.useanti >= 2:
        SMSI.anti = False
    if Round - SMSII.useanti >= 2:
        SMSII.anti = False


    if  SMSI.mana >= 80:
        SMSI.mana = 100
    else:
        SMSI.mana += 20
    if  SMSII.mana >= 80:
        SMSII.mana = 100
    else:
        SMSII.mana += 20
if SMSII.IsAlive() == False:
    print("          /\__/\                                                 ( )__( )")
    print("         ( ● ^ ●)                  | MEME |                      (X ^ X )")
    print("        /(______)\/                | WON! |                    \/(______)\\")
    print("          |    |                                                  |    |")
if SMSI.IsAlive() == False:
    print("          /\__/\                                                 ( )__( )")
    print("         ( X ^ X)                  | NUNU |                      (● ^ ● )")
    print("        /(______)\/                | WON! |                    \/(______)\\")
    print("          |    |                                                  |    |")

# ♧ = 10-50 damage
# ◇ = 50-75 damage
# ♡ = 150-175 damgage
# ♤ = 350-500 damage
# [Round: 1 》》Turn: Meme]
# ________________________________________________________________________________
#     P1 => HP: 1000                                          P2 => HP: 1000
#           MN: 100                                                 MN: 100

#           /\__/\                                                 ( )__( )
#          ( ● ^ ●)                                                (● ^ ● )
#         /(______)\/          ~♧                                \/(______)\
#           |    |                                                  |    |
#          P1: Meme                                                P2: Nunu
# ________________________________________________________________________________


# [Round: 1 》》Turn: Meme]
# ________________________________________________________________________________
#     P1 => HP: 1000                                          P2 => HP: 1000
#           MN: 100                                                 MN: 100
#                        _____
#           /\__/\      /     \                                    ( )__( )
#          ( ● ^ ●)     \     /                                    (● ^ ● )
#         /(______)\/    \   /                                   \/(______)\
#           |    |        \_/                                       |    |
#          P1: Meme                                                P2: Nunu
# ________________________________________________________________________________


# [Round: 1 》》Turn: Meme]
# ________________________________________________________________________________
#     P1 => HP: 1000                                          P2 => HP: 1000
#           MN: 100                                                 MN: 100
#                                                       _____
#           /\__/\                                     /     \     ( )__( )
#          ( ● ^ ●)                                    \     /     (● ^ ● )
#         /(______)\/                                   \   /    \/(______)\
#           |    |                                       \_/        |    |
#          P1: Meme                                                P2: Nunu
# ________________________________________________________________________________


# [Round: 1 》》Turn: Meme]
# ________________________________________________________________________________
#     P1 => HP: 1000                                          P2 => HP: 1000
#           MN: 100                                                 MN: 100
#                        _____                          _____
#           /\__/\      /     \                        /     \     ( )__( )
#          ( ● ^ ●)     \     /                        \     /     (● ^ ● )
#         /(______)\/    \   /                          \   /    \/(______)\
#           |    |        \_/                            \_/        |    |
#          P1: Meme                                                P2: Nunu
# ________________________________________________________________________________
