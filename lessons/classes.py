from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo',300000,8,'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')


# class Planet:

#   shape = 'round'

#   def __init__(self, name, radius, gravity, system):
#     self.name = name
#     self.radius = radius
#     self.gravity = gravity
#     self.system = system
  
#   def orbit(self):
#     return f'{self.name} is orbiting in the {self.system}'

#   @classmethod
#   def commons(cls):
#     return f'All planets are {cls.shape} because of gravity'
  
#   @staticmethod
#   def spin(speed = '2000mph'):
#     return f'The planet spins and spins at {speed}'

# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'Gravity is: {hoth.gravity}')
# print(hoth.orbit())

# naboo = Planet('Naboo',300000,8,'Naboo System')
# print(f'Name:{naboo.name}')
# print(f'Name:{naboo.radius}')
# print(f'Name:{naboo.gravity}')
# print(naboo.orbit())
# print(naboo.shape)
# print(naboo.commons())
# print(Planet.spin('a very high speed'))