# division round down Ex:
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)
# Output: 17

# find minute and second
seconds = 1042
display_minutes = 1042 // 60  # 取整數
display_seconds = 1042 % 60  # 取餘數

print(display_minutes)
print(display_seconds)
# Output:
# 17
# 22

first_planet = 149597870
second_planet = 778547200
distance_km = second_planet - first_planet
print(distance_km)
distance_mi = distance_km / 1.609344
print(distance_mi)


# string to int or float
demo_int = int('215')
print(demo_int)
demo_float = float('215.3')
print(demo_float)
# Output:
# 215
# 215.3

# absolute
print(abs(39 - 16))
print(abs(16 - 39))
# Output
# 23
# 23

# round off
print(round(14.5))
# Output: 15


# practice 2
first_planet_input = input(
    'Enter the distance from the sun for the first planet in KM: ')
second_planet_input = input(
    'Enter the distance from the sun for the second planet in KM: ')

first__planet = int(first_planet_input)
second__planet = int(second_planet_input)

distance__km = abs(second__planet-first__planet)
print(distance__km)
