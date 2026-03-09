class Car:
    wheelers = 4
    engine = 'Petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4

    def __init__(self, air_bags, security, base_budget):
        self.air_bags=air_bags
        self.security=security
        self.base_budget=base_budget

    def display_properties(self):
        print({
            'wheelers': self.wheelers,
            'engine': self.engine,
            'base_speed':self.base_speed,
            'max_speed':self.max_speed,
            'air bags':self.air_bags,
            'security':self.security
        })

    @classmethod
    def update_gears(cls, new_gears):
        cls.gears = new_gears
        print(f'No of gears: {cls.gears}')


tata = Car(True, 'Level 5', '2L')
tata.display_properties()
tata.update_gears(5)

# mahindra = Car(True, 'Level 4','5L')
# print(tata.air_bags)