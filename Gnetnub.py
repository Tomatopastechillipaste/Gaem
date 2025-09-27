import random

# คลาสผู้เล่น
class SingMeSheWit:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.anti = False

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
        print()
        print("          /\__/\                                                 ( )__( )") 
        print(f"         ( ● ^ ●)                                                (● ^ ● )")
        print("        /(______)\/                                            \/(______)\\")
        print("          |    |                                                  |    |")
        print("         P1: Meme                                                P2: Nunu")
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
    opponent.hp -= damage
    return f"{damage}"
def Mediumattack(player, opponent):
    player.mana -= 50
    if random.randint(1, 100) < 75:
        damage = random.randint(50, 75)
        opponent.hp -= damage
        return f"{damage}"
    else:

        return "Missed"
def Largeattack(player, opponent):
    player.mana -= 75
    if random.randint(1, 100) < 50:
        damage = random.randint(150, 175)
        opponent.hp -= damage
        return f"{damage}"
    else:
        return "Missed"
    
def XtraLargeattack(player, opponent):
    player.mana -= 100
    if random.randint(1, 100) < 25:
        damage = random.randint(350, 500)
        opponent.hp -= damage
        return f"{damage}"
    else:
        return "Missed"
    
def Randomattack(player, opponent):
    player.mana -= 25
    damage = random.randint(0, 500)
    opponent.hp -= damage
    return f"{damage}"

def Purloin(player, opponent, hm): # steal
    if random.randint(1, 100) < 50:
        if hm == "HP":
            damage = random.randint(0, 100)
            opponent.hp -= damage
            player.hp += damage
            return f"{damage}"
        elif hm == "MN":
            damage = random.randint(0, 10)
            opponent.mana -= damage
            player.mana += damage
            return f"{damage}"
    else:
        return "Missed"

def AnitMinimise(player):
    player.mana -= 25
    if random.randint(1, 100) < 50:
        player.anti = True
def PurchaseMana(player, mp):
    player.hp -= mp*5
    player.mana += mp
    return f"+{mp}"
def AddTohealthPoints(player):
    player.mana -= 100
    player.hp += 250
    return "+250"

def Chosen(code, player, opponent):
    code=code.lower()
    if code == "s" and player.mana >= 25:
        return Smallattack(player, opponent)
    elif code == "m" and player.mana >= 50:
        return Mediumattack(player, opponent)
    elif code == "l" and player.mana >= 75:
        return Largeattack(player, opponent)
    elif code == "xl" and player.mana >= 100:
        return XtraLargeattack(player, opponent)
    elif code == "r" and player.mana >= 25:
        return Randomattack(player, opponent)
    elif code == "p" and player.mana >= 0:
        hm = input("Purloin HP or MN: ").lower        
        return Purloin(player, opponent, hm)
    elif code == "am" and player.mana >= 25:
        return AnitMinimise(player, opponent)
    elif code == "pm":
        mp = input("Purchase Mana: ")
        if player.hp >= mp*5:
            return PurchaseMana(player, opponent, mp)
    elif code == "atp" and player.mana >= 100:
        return AddTohealthPoints(player, opponent)
    else:
        print("Choose again: ")

# เทิร์นของผู้เล่น



# เริ่มเกม
SMSI = SingMeSheWit("Meme", 1000, 100)
SMSII = SingMeSheWit("Nunu", 1000, 100)

# ลูปรอบเกม


# แสดงผลลัพธ์เมื่อเกมจบ
print(SMSI.IsAlive())
SMSI.DisplayVisables(1)


code = input("CHOOSE: ")
Chosen(code, SMSI, SMSII)

# [Round: 1 》》Turn: Meme]
# ________________________________________________________________________________
#     P1 => HP: 1000                                           P2 => HP: 1000
#           MN: 100                                                  MN: 100
#          /\__/\                                                 ( )__( )
#         ( ● ^ ●)  ♤♡◇♧ ~♡                              ○¤@๑   (● ^ ● )
#        /(______)\/                                            \/(______)\
#          |    |                                                  |    |
#        P1: Meme                                                P2: Nunu
# ________________________________________________________________________________







