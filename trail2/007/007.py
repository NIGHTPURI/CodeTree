secret_code, meeting_point, time = input().split()
time = int(time)

class secret :
    def __init__(self,sc,mp,t) :
        self.sc = sc
        self.mp = mp
        self.t = t

secret = secret(secret_code, meeting_point, time)

print('secret code :',secret.sc)
print('meeting point :',secret.mp)
print('time :',secret.t)

# Please write your code here.