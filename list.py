# create list
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

# 修改列表值
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])
# Output
# Mars is also known as Red Planet

# 確認列表長度
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
# Output:
# There are 8 planets in the solar system

# 添加值
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
# Output:
# There are actually 9 planets in the solar system.

# 刪除值
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets,
      "planets in the solar system.")

# 查找值
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
# Output
# Jupiter is the 5 planet from the sun


# practice
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650  # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs",
      bus_weight * gravity_on_planets[0], "kg")
print("The lightest a bus would be in the solar system is",
      bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is",
      bus_weight * max(gravity_on_planets), "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg


# 切片列表
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)
# Output: ['Mercury', 'Venus']

planets_after_earth = planets[3:8]
print(planets_after_earth)
# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets_after_earth = planets[3:]
print(planets_after_earth)
# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# 連接列表
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']

# 列表排序
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output
# The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']

# 顛倒排序
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output
# The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']
