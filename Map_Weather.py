"""weather.txt
2001,30
2001,40
2002,50
2002,30
2003,20
2003,25
"""

# Mapper Program

import sys

for line in sys.stdin:
    
    # Remove extra spaces/newline
    line = line.strip()

    # Split year and temperature
    year, temp = line.split(",")

    # Send output to reducer
    print(year + "\t" + temp)
    
    
    
#-------

# Reducer Program

import sys

current_year = None
temp_list = []

hottest_year = ""
coolest_year = ""

highest_avg = -9999
lowest_avg = 9999

for line in sys.stdin:

    # Remove spaces/newline
    line = line.strip()

    # Split mapper output
    year, temp = line.split("\t")

    temp = int(temp)

    # First year case
    if current_year == None:
        current_year = year

    # Same year
    if year == current_year:
        temp_list.append(temp)

    # New year comes
    else:

        # Calculate average
        avg = sum(temp_list) / len(temp_list)

        print(current_year, "Average Temperature =", avg)

        # Check hottest
        if avg > highest_avg:
            highest_avg = avg
            hottest_year = current_year

        # Check coolest
        if avg < lowest_avg:
            lowest_avg = avg
            coolest_year = current_year

        # Reset for new year
        current_year = year
        temp_list = [temp]

# Last year processing
if current_year != None:

    avg = sum(temp_list) / len(temp_list)

    print(current_year, "Average Temperature =", avg)

    if avg > highest_avg:
        highest_avg = avg
        hottest_year = current_year

    if avg < lowest_avg:
        lowest_avg = avg
        coolest_year = current_year

# Final Result
print("\nHottest Year =", hottest_year)
print("Coolest Year =", coolest_year)
