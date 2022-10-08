# # Python-
# # >>> open("/path/to/mars.jpg")

# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>     报告该文件为stdin(交互式终端中的输入)
# # FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'
# # 错误为FileNotFoundError（异常名称）异常，这意味着该文件不存在，或者可能不存在该文件的目录。


# Python-

# >>> try:
# ...     open('config.txt')
# ... except FileNotFoundError:
# ...     print("Couldn't find the config.txt file!")
# ...
# Couldn't find the config.txt file!
# loaded_config = """# Rocket Ship Configuration File!
# fuel_tanks=4
# oxygen_tanks=3
# initial_propulsion_level=84
# $ End of file"""
# parsed_config = {}
# for line in loaded_config.split('\n'):
#     try:
#         key, value = line.split('=')
#         parsed_config[key] = value
#     except ValueError:
#         print(f'Unable to parse {line}')
# print(parsed_config)


# # EX
def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type
            # Raise the same exception but with a better error message
            raise TypeError(
                f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(
            f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"


print(water_left(5, 100, 2))

# EX2

true_values = ['yes', 'y']
false_values = ['no', 'n']


def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid entry')


print(str_to_bool('y'))
print(str_to_bool('n'))
print(str_to_bool('abc'))
