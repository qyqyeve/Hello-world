cars = 100 # 车有100辆
space_in_a_car = 4.0 # 车内空间允许4人乘坐
drivers = 30 #司机有30
passengers = 90 #乘客有90
cars_not_driven = cars - drivers #空闲的车= 车辆 - 司机数量
cars_driven = drivers # 被使用的车 = 司机数量
carpool_capacity = cars_driven * space_in_a_car  #拼车容量 = 被使用的车 * 车内空间
average_passengers_per_car =passengers / cars_driven #每辆车的平均乘客数量 = 乘客数量 / 被使用的车数量


print("There are ", cars, "cars available")
print("There are only ", drivers , "drivers avaliable.")
print("There will be ", cars_not_driven , "empty cars today.")
print("We can transport",carpool_capacity , "people today.")
print("We have ", passengers ,"to carpool today.")
print("We need to put about ", average_passengers_per_car, "in each car")


