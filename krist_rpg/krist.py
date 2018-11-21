#imports
import races
import visual

#introduce to krist 
def Introduction():
    pass



#lists

Files_Loaded=[]

#vars

#Health,Wisdom,Speed,Detection,Power,Leader,Charge,Magic,Fourtune

hp,wp,sp,dp,pp,lp,cp,mp,fp=0,0,0,0,0,0,0,0,0

#use all 90 points on stats
def formatted():
    print("""
    Health:    {0}
    Wisdom:    {1}
    Speed:     {2}
    Detection: {3}
    Power:     {4}
    Leader:    {5}
    Charge:    {6}
    Magic:     {7}
    Fourtune:  {8}
    """.format(hp,wp,sp,dp,pp,lp,cp,mp,fp))
    #char sheet stuff
def Stats_Sheet():
    global hp,wp,sp,dp,pp,lp,cp,mp,fp
    hp,wp,sp,dp,pp,lp,cp,mp,fp=0,0,0,0,0,0,0,0,0
    Points_Left=90
    operation=""
    pts=0
    while Points_Left > 0:
        stat_up=input("enter one of the nine stats to modify: Health,Wisdom,Speed,Detection,Power,Leader,Charge,Magic,or Fourtune. or view points by typing view   ").lower()
        if stat_up != "view":
            while operation == "":
                operation=input("would you like to ADD or SUBtract points?").lower()
                if operation != "add" and operation != "sub":
                    operation=""
        if stat_up=="health":
            try:
                pts=int(input("enter the amount of health points (hp) you would like to {0}".format(operation)))
                if operation == "sub":
                    hp-=pts
                    Points_Left+=pts
                else:
                    hp+=pts
                    Points_Left-=pts
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up=="wisdom":
            try:
                pts=int(input("enter the amount of wisdom points (wp) you would like to {0}".format(operation)))
                if operation == "sub":
                    wp-=pts
                    Points_Left+=pts
                else:
                    wp+=pts
                    Points_Left-=pts
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up=="speed":
            try:
                pts=int(input("enter the amount of speed points (sp) you would like to {0}".format(operation)))
                if operation == "sub":
                    sp-=pts
                    Points_Left+=pts
                else:
                    sp+=pts
                    Points_Left-=pts
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up=="detection":
            try:
                pts=int(input("enter the amount of detection points (dp) you would like to {0}".format(operation)))
                if operation == "sub":
                    dp-=pts
                    Points_Left+=pts
                else:
                    dp+=pts
                    Points_Left-=pts
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up=="power":
            try:
                pts=int(input("enter the amount of power points  you would like to {0}".format(operation)))
                if operation == "sub":
                    pp-=pts
                    Points_Left+=pts
                else:
                    pp+=pts
                    Points_Left-=pts
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up== "leader":
            try:
                pts=int(input("enter the amount of leader points (lp) you would like to {0}".format(operation)))
                if operation == "sub":
                    lp-=pts
                    Points_Left+=pts
                else:
                    lp+=pts
                    Points_Left-=pts
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up=="charge":
            try:
                pts=int(input("enter the amount of charge points (cp) you would like to {0}".format(operation)))
                if operation == "sub":
                    cp-=pts
                    Points_Left+=pts
                else:
                    cp+=pts
                    Points_Left-=pts
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up=="magic":
            try:
                pts=int(input("enter the amount of magic points (mp) you would like to {0}".format(operation)))
                if operation == "sub":
                    mp-=pts
                    Points_Left+=pts
                else:
                    mp+=pts
                    Points_Left-=pts
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up=="fourtune":
            try:
                pts=int(input("enter the amount of fourtune points (fp) you would like to {0}".format(operation)))
                if operation == "sub":
                    fp-=pts
                    Points_Left+=pts
                else:
                    fp+=pts
                    Points_Left-=pts            
            except ValueError:
                "You didn't enter numbers only."
        elif stat_up=="view":
            
            formatted()
        else:
            print("that isnt a stat.")
def Race_Sheet():
    global races
    input("you can either have a purebred or a hybrid race. purebreds have less abilities but are usually stronger in their own abilities.")
    input("the list of races is:")
input("Human")
input("Elf")
input("Dwarf")
input("Orc")
input("Fairy")
input("Giant")
input("Enden")
input("Aron")
input("Murloc")
input("Drake")
input("Kurkur")
input("Hollow")
input("Spirit")
input("Demon")
input("Robot")
input("Werewolf")
input("Vampire")
input("Ghost")
input("Wraith")
input("Construct")
input("Litch")
input("Reaper")

#game start stuff
string=""
File=open("saved_file_names","r")
if len(File)==0:
    File.close()
    awnser=input("you dont have any files saved. would you like to make one? Y or N").lower()
    if awnser=="y":
        input("now you need to set your stats (enter to continue)")
        input("the first stat is health. Health points are The amount of hits you can take. Good for knights.")
        input("the second is wisdom. Wisdom points are how smart you are. Good for Mages.")
        input("the third is speed. Speed points are how fast you are. Good for Rogues.")
        input("the fourth is detection. Detection points are how well you can locate stuff. Good for Rangers.")
        input("the fifth is power. Power points are how hard you can hit. Good for Berserkers.")
        input("the sixth is leader. Leader points are how well you can communicate with people. Good for Bards.")
        input("the seventh is charge. Charge points are how long you can do stuff for.")
        input("the eighth is magic. Magic points are your natural magic skills.")
        input("the ninth is fourtune. Fortune points are how often odds lie in your favor.")
        input("you can subtract and add points by typing add and sub.")
        input("you cannot have any stat as zero. any stat below 10 will negatively affect a task that requires that stat to be checked.")
        while hp==0 or cp==0 :
            Stats_Sheet()
            if hp==0:
                print("you cannot have 0 health")
            if wp==0:
                print("you cannot have 0 charge")
            if sp==0:
                print("you cannot have 0 speed")
            if dp==0:
                print("you cannot have 0 dexterity")
            if pp==0:
                print("you cannot have 0 power")
            if lp==0:
                print("you cannot have 0 leader")
            if cp==0:
                print("you cannot have 0 charge")
            if mp==0:
                print("you cannot have 0 magic")
            if fp==0:
                print("you cannot have 0 fourtune")
        print("your stats")
        formatted()
        print("now you need you set your race. an example would be human. however there are more than just humans in this game. there are others like dwarvs and elvs. these all speak diferent languages. to understand multiple languages you need to do certain things.")
        Race_Sheet()

        intro=input("would you like the introduction to krist?(vital for beginners) Y or N").lower
        if intro=="y":
            Introduction()
    else:
        File=open("saved_file_names","r")
        i=input()
        for e in range(1,i):
            Files_Loaded.append(input())
        print("saved files are:")
        for string in Files_Loaded:
            input(string)
            completed=False
            completed2=0
        while completed==False:
            file_inputted=input("what would you like to open? type the file name you would like to select.")
            for string in Files_Loaded:
                if string==file_inputted:
                    completed=True
                    selected_file=string
                    string=input("are you sure you want to use this file? Y or N")
                    if string=="Y":
                        completed=False
                else:
                    completed2+=1
            if completed2==len(Files_Loaded):
                print("you didnt select a valid file")
        
        
        
