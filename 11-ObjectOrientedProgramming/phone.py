import random

class Phone():
    def __init__(self, battery_capacity, camera_quality,pin):
        self.battery_capacity = battery_capacity
        self.current_charge = battery_capacity
        self.camera_quality = camera_quality
        self.pin = pin
        self.is_on = False
        self.is_shut = False
        self.photos = []
        self.curent_photo = 0

        actions_dict = {
            "set new pin": self.set_new_PIN,
            "unblock": self.unblock,
            "block": self.block,
            "charge up": self.charge_up,
            "take a photo": self.take_a_photo,
            "show photo": self.show_photo,
            "next photo": self.next_photo,
            "previous photo": self.prev_photo,
            "perform a complicated task": self.perform_a_complicated_task
        }


    def start_operating(self):
        going = True

        while(going):
            action = input("What to do: ").lower()

            if not self.actions_dict[action] == None:
                self.actions_dict[action]()
            elif action == "":
                going = False
            elif action == "help":
                print(self.actions_dict)
            # if action == "set new pin":
            #     self.set_new_PIN()
            # elif action == "unblock":
            #     self.unblock()
            # elif action == "block":
            #     self.block()
            # elif action == "charge up":
            #     self.charge_up()
            # elif action == "take a photo":
            #     self.take_a_photo()
            # elif action == "show photo":
            #     self.show_photo()
            # elif action == "previous photo":
            #     self.prev_photo()
            # elif action == "next photo":
            #     self.next_photo()
            # elif action == "perform a complicated task":
            #     self.perform_a_complicated_task()
            # elif action == "":
            #     going = False
            # else:
            #     print("This command doesn't exist")


    def check_status(self):
        result = False
        if self.is_shut:
            print("Your phone is turned off")
            result = True
        elif not self.is_on:
            print("Unblock your phone first")
            result = True
        
        return result


    def set_new_PIN(self):
        if self.check_status():
            return
        new_pin = input("Enter new PIN: ")
        attempt = input("Enter your PIN: ")
        if self.pin == attempt:
            self.pin = new_pin
            print("Changed PIN")


    def unblock(self):
        if self.is_shut:
            print("Your phone is powered off")
            return
        elif(self.is_on):
            print("Your phone is already unblocked")
            return
        attempt = input("Enter your PIN: ")
        if self.pin == attempt:
            self.is_on = True
            print("Unblocked")


    def block(self):
        self.is_on = False


    def reduce_energy(self, multiplier=1):
        self.current_charge -= 100*multiplier
        if self.current_charge <=0:
            self.is_shut = True
            self.is_on = False
            self.current_charge = 0
            print("Phone has shut down")
        elif self.current_charge/self.battery_capacity*100 <= 15:
            print("Low battery!")


    def perform_a_complicated_task(self):
        if self.check_status():
            return
        self.reduce_energy(100)


    def charge_up(self):

        time = int(input("For how long:"))
        unit = input("What unit of measurement: ")
        if unit == "hours":
            self.current_charge += 100*60*time
        elif unit == "seconds":
            self.current_charge += 100/60*time
        else:
            self.current_charge += 100*time
            print("unit understood as: \"minutes\"")
        
        if self.current_charge > self.battery_capacity:
            self.current_charge = self.battery_capacity
        
        print(f"Phone at {self.current_charge/self.battery_capacity*100}%")
        

    def take_a_photo(self):
        if(self.check_status()):
            return
        elif self.camera_quality == "good":
            new_photo = random_photo()
            self.photos.append(new_photo)
            print("Took a photo")
        elif self.camera_quality == "OK":
            if self.current_charge/self.battery_capacity*100 >= 50:
                new_photo = random_photo()
                self.photos.append(new_photo)
                print("Took a photo") 
            else:
                self.photos.append("[BLANK PHOTO]")
                print("Battery too low")
        else:
            if self.current_charge/self.battery_capacity*100 >= 75:
                new_photo = random_photo()
                self.photos.append(new_photo)
                print("Took a photo")
            else:
                self.photos.append("[BLANK PHOTO]")
                print("Battery too low")

        
        self.reduce_energy(2)


    def show_photo(self):
        if self.check_status() or self.curent_photo>= len(self.photos) or self.curent_photo < 0:
            print("This photo doesn't exist")
            return
        else:
            print(self.photos[self.curent_photo])
        self.reduce_energy()
        
    
    def next_photo(self):
        if self.check_status():
            return
        self.curent_photo += 1
        print("Moved to the next photo")
        self.reduce_energy()


    def prev_photo(self):
        if self.check_status():
            return
        print("Moved to the previous photo")
        self.curent_photo -= 1
        self.reduce_energy()
    

def random_photo():
    result = ""

    for i in range(250):
        rand = random.randrange(1, 5)
        if rand == 1:
            result += " "
        elif rand == 2:
            result += "."
        elif rand == 3:
            result += "*"
        elif rand == 4:
            result += "/"
        else:
            result += "\\"
        if (i+1)%25 == 0:
            result+= "\n"

    return result 