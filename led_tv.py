from tv import TV


class LedTv(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate,
                 viewing_angle, backlight, status="Off"):
        super().__init__(brand, price, inches, status)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        self.show_status()
        print(f"Screen Thickness: {self.screen_thickness} inches")
        print(f"Energy Usage: {self.energy_usage} watts")
        print(f"Lifespan: {self.lifespan} years")
        print(f"Refresh Rate: {self.refresh_rate} Hz")
        print(f"Viewing Angle: {self.viewing_angle} degrees")
        print(f"Backlight: {self.backlight}")


# Example usage:
my_smart_tv = LedTv(brand="Samsung", price=999.99, inches=65, screen_thickness="0.5", energy_usage=120,
                    lifespan=10, refresh_rate=120, viewing_angle=178, backlight="LED")
my_smart_tv.display_details()
my_smart_tv.turn_on()
my_smart_tv.set_channel(8)
my_smart_tv.adjust_volume(60)
my_smart_tv.display_details()
my_smart_tv.turn_off()
