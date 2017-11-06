#!/usr/bin/python3.6
#Task is to return the value of left battery capacity
# parsed from given string (let's assume it is some shell command's result).
#Current level should be calculated as CurrentCapacity / MaxCapacity
# in percents. The resulting value should be like the following example:
#61.41%
import re

data = '''
           "MaxCapacity" = 4540
           "CurrentCapacity" = 2897
           "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,
           "Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
           "DesignCapacity" = 6700
'''
def get_battery_level(data): 
       max_capacity = int(re.search('"MaxCapacity" = (\d+)', data).group(1))
       cur_capacity = int(re.search('"CurrentCapacity" = (\d+)', data).group(1))
       result = float(float(cur_capacity) * 100 / float(max_capacity))
       return "{:.2f}%".format(result)

print(get_battery_level(data))

