from turtle import update
from unicodedata import name


planet = {
    'name': 'Jupiter',  # 行星名稱
    'moons': 79  # 衛星數目
}

# 讀取字典值
print(planet.get('name'))
# or
print(planet['name'])
# get和[]的行為與擷取專案相同，但有一個主要差異。
# 如果索引鍵無法使用，get會傳回None，而[]會引發KeyError。
# wibble = planet.get('wibble')  # Returns None
# wibble = planet['wibble']  # Throws KeyError


# 修改字典值
planet.update({'name': 'Makemake'})
# or
planet['name'] = 'Makemake'
print(planet['name'])

# update 的主要優點是能夠在一個作業中修改多個值。

# 新增索引
planet['orbital period'] = 4333
# 移除索引
planet.pop('orbital period')


# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)
# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

# Output: Jupiter polar diameter: 133709


planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
total_planets = len(planet_moons.keys())

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet as an average of {average} moons')
