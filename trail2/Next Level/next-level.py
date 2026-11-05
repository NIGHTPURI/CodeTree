user2_id, user2_level = input().split()
user2_level = int(user2_level)
class game :
    def __init__(self, id, lev) :
        self.id = id
        self.lev = lev

game1 = game('codetree',10)
game2 = game(user2_id,user2_level)

print(f"user {game1.id} lv {game1.lev}")
print(f"user {game2.id} lv {game2.lev}")

