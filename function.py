from datetime import timedelta, datetime


def rocket_parts():
    print("payload", "propellant", "structure")


rocket_parts()
#----------------------------------------------------------#


def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"


distance_from_earth("Moon")
# output '238,855'

distance_from_earth("Saturn")
# output 'Unable to compute to that destination'

# distance_from_earth()
# output TypeError
#----------------------------------------------------------#


def generate_report(main_tank, Exteral_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main_tank:{main_tank}
    Exteral_tank:{Exteral_tank}
    Hydrogen_tank:{hydrogen_tank}"""
    print(output)


generate_report(50, 50, 50)
#----------------------------------------------------------#


def arrival_time(distination, hours=51):  # 抵達時間需要51hrs
    now = datetime.now()  # 獲取現在時間
    arrival = now + timedelta(hours=hours)  # 計算抵達時間
    # 回傳格式化為字串的抵達時間
    return arrival.strftime(f"{distination} Arrival: %A %H:%M")


print(arrival_time("moon"))

#----------------------------------------------------------#
# 可變參數 語法:參數前加上*


def variable_length(*args):
    print(args)


variable_length('one', 'two')
variable_length(None)


def sequence_time(*args):
    total_minutes = sum(args)  # 所有步驟的所需時間
    if total_minutes < 60:  # 如果總時間小於60mins
        return f"Total time to launch is {total_minutes} minutes"  # 列印此行
    else:  # 如果總時間大於1hrs
        return f"Total time to launch is {total_minutes/60} hours"  # 列印此行


print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))

#----------------------------------------------------------#
# 可變關鍵字參數


def variable_length2(**kwargs):
    print(kwargs)


variable_length2(tanks=1, day="Wednesday", pilots=3)  # 輸出以dic形式分配

# EX1


def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin",
             command_pilot="Michael Collins")

# EX2


def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')


fuel_report(main=50, external=100, emergency=60)
