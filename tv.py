class TV:
    def __init__(self, brand, price, inches, status="Off"):
        self.brand = brand
        self.channel = 1  # Default channel is 1
        self.price = price
        self.inches = inches
        self.status = status
        self.volume = 50  # Default volume is 50
        self.max_channels = 50  # channel limit is 50

    def turn_on(self):
        if self.status == "Off":
            self.status = "On"
            print(f"{self.brand} TV is now On.")
        else:
            print(f"{self.brand} TV is already On.")

    def turn_off(self):
        if self.status == "On":
            self.status = "Off"
            print(f"{self.brand} TV is now Off.")
        else:
            print(f"{self.brand} TV is already Off.")

    def set_channel(self, channel):
        if self.status == "On":
            if 1 <= channel <= self.max_channels:
                self.channel = channel
                print(f"Changed channel to {channel} on {self.brand} TV.")
            else:
                print(f"Invalid channel number. {self.brand} TV stays at channel {self.channel}.")
        else:
            print(f"You can't change the channel because {self.brand} TV is Off.")

    def adjust_volume(self, volume):
        if self.status == "On":
            if 0 <= volume <= 100:
                self.volume = volume
                print(f"Adjusted volume to {volume} on {self.brand} TV.")
            else:
                print("Volume should be between 0 and 100.")
        else:
            print(f"You can't adjust the volume because {self.brand} TV is Off.")

    def show_status(self):
        print(f"Brand: {self.brand}")
        print(f"Channel: {self.channel}")
        print(f"Price: ${self.price}")
        print(f"Inches: {self.inches}")
        print(f"Status: {self.status}")
        print(f"Volume: {self.volume}")
        print(f"{self.brand} at channel {self.channel} volume {self.volume}")


my_tv = TV(brand="Sony", price=799.99, inches=55)
my_tv.show_status()
my_tv.turn_on()
# my_tv.set_channel(60)
# my_tv.show_status()
# my_tv.turn_off()
