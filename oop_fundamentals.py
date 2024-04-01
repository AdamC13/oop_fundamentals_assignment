#1
class Vehicle:
    def __init__(self, reg_num, v_type, owner):
        self.registration_number = reg_num
        self.v_type = v_type
        self.owner = owner
    
    def update_owner(self, owner):
        self.owner = owner


Acura = Vehicle(10053, "TL", "Adam")
Alpha_Romeo = Vehicle(100452, "Guilia", "Haya")
Ford = Vehicle(1256156, "F-150", "Kevin")

print(Alpha_Romeo.owner)
Alpha_Romeo.update_owner("Junkyard")
print(Alpha_Romeo.owner)


#2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0

    def add_participant(self, new_participants = 1):
        self.participants += new_participants
    
    def get_participant_count(self):
        return self.participants

Valorant = Event("VCT", "Always")
Valorant.add_participant()
print(Valorant.get_participant_count())
Valorant.add_participant(6)
print(Valorant.get_participant_count())

