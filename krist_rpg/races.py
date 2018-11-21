class Race():
    def __init__(self,name,language,unlocked):
        self.name=name
        self.language=language
        self.unlocked=unlocked
    def __str__(self):
        return"""
{0}
{1}
{2}
        """.format(self.name,self.language,self.unlocked)
class Hybrid(Race):
    def __init__(self,race,race2,language,language2,name,unlocked):
        self.race=race
        self.race2=race2
        self.name=name
        self.language=language
        self.language2=language2
        self.unlocked=unlocked
    def __str__(self):
        return"""
{0}
{1}
{2}
{3}
{4}
{5}
        """.format(self.race,self.race2,self.language,self.language2,self.name,self.unlocked)
Races={"human":Race("human","english",False),
"elf":Race("elf","elvish",False),
"dwarf":Race("dwarf","dwarvish",False),
"orc":Race("orc","orcish",False),
"fairy":Race("fairy","pixyan",False),
"giant":Race("giant","english",False),
"enden":Race("enden","enden",False),
"aron":Race("aron","aroni",False),
"merloc":Race("merloc","english",False),
"drake":Race("drake","english",False),
"kurkur":Race("kurkur","japanese",False),
"hollow":Race("hollow","english",False),
"spirit":Race("spirit","elvish",False),
"demon":Race("demon","english",False),
"robot":Race("robot","english",False),
"vampire":Race("vampire","english",False),
"werewolf":Race("werewolf","english",False),
"ghost":Race("ghost","english",False),
"wraith":Race("wraith","english",False),
"litch":Race("litch","english",False),
"reaper":Race("reaper","english",False),
"ent":Race("ent","pixyan",False),
"haltija":Race("haltija","elvish",False),
"centaur":Race("centaur","english",False),
"ma'netsewel":Race("ma'netsewel","english",False),
"moleman":Race("moleman","dwarvish",False),
"be'ar":Race("be'ar","orcish",False),
"goldhorn":Race("goldhorn","english",False),
"naga":Race("naga","english",False),
"monster":Race("monster","greek",False),
"satyr":Race("satyr","english",False),
"yaren":Race("yaren","orcish",False),
"kappa":Race("kappa","japanese",False),
"aracne":Race("aracne","english",False),
"angel":Race("angel","latin",False),
"god":Race("god","latin",False),
}

Hybrid_Races={
"Half Elf":Hybrid("human","elf","english","elvish","Half Elf",False)
}
