unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class bomb :
    def __init__(self,uc,wc,s) :
        self.uc = uc
        self.wc = wc
        self.s = s

bomb1 = bomb(unlock_code,wire_color,seconds)

print(f"code : {bomb1.uc}")
print(f"color : {bomb1.wc}")
print(f"second : {bomb1.s}")

# Please write your code here.