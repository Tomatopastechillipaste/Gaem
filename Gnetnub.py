import random

# คลาสผู้เล่น
class SingMeSheWit:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

    def IsAlive(self):
        if self.hp <= 0:
            return False
        else:
            return True



# ฟังก์ชันใช้สกิล


# เทิร์นของผู้เล่น



# เริ่มเกม
SMSI = SingMeSheWit("Nam", 100, 100)
SMSII = SingMeSheWit("MeNam", 100, 100)

# ลูปรอบเกม


# แสดงผลลัพธ์เมื่อเกมจบ
print(SMSI.IsAlive())