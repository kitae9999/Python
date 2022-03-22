class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp,self.damage))


marine1=Unit("마린",40,5)
marine2=Unit("마린",40,5)
tank=Unit("탱크",150,35)

