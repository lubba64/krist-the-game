race_suffixes=["_d1","_d2","_l1","_l2","_r1","_r2","_u1","_u2","_dr1","_dr2","_lr1","_lr2","_rr1","_rr2","_ur1","_ur2","_i1","_i2","_i3","_i4"]
notcrash=True
addedraces=[]
racename=input("what is the race name?")
compiledracelist=[]
for i in range(0,len(race_suffixes)):
    compiledracelist.append(racename+race_suffixes[i]+",")
print(compiledracelist)