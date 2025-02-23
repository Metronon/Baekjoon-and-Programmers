kda = list(map(int, input().split("/")))
score = kda[0] + kda[2]
death = kda[1]
if ((score < death) or (death == 0)):
    print("hasu")
else:
    print("gosu")