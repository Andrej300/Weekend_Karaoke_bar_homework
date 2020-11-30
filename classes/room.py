

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        # self.fee = fee
        self.guests = []
        self.songs = []


    def count_guests(self):
        return len(self.guests)
        

    def check_in_guests(self, guest):
        self.guests.append(guest)

    def check_out_guests(self, guest):
        for person in self.guests:
            if person == guest:
                self.guests.remove(guest)
       




