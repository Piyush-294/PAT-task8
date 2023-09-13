class Circle:
    # Private class variable
    __pi = 3.141

    def __init__(self, radii):
        self.radii = radii

    def area(self):
        # Calculate the area of each circle and store in a list
        areas = [Circle.__pi * r * r for r in self.radii]
        return areas

    def perimeter(self):
        # Calculate the perimeter (circumference) of each circle and store in a list
        perimeters = [2 * Circle.__pi * r for r in self.radii]
        return perimeters

    def display_info(self):
        # Display information about each circle
        for i, r in enumerate(self.radii):
            area = self.area()[i]
            perimeter = self.perimeter()[i]
            print(f"Circle {i+1} - Radius: {r}, Area: {area}, Perimeter: {perimeter}")


# List of radii
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create a Circle object with the list of radii
circle = Circle(radii_list)

# Display information about the circles
circle.display_info()
