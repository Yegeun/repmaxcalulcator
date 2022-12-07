# This is a sample Python script.
# The idea of this project is to make a rep max calculator and caculate the the rep max percentages for programming
# This is the for example if you 90%(90kg) and 80% of this is 72kg then therefore you should be able to do this for 8reps
import pandas


# The way to look at the table is down

# TODO The top rows needed to get edited to show the true percentage of the working weigh relative to the weighting weight
# max the next thing to do is we need to edit the table so it only shows the useful bit sof oinformation not any duplicated information


def rpmindex(repm):
    if repm == 1:
        return 100
    elif repm == 2:
        return 95
    elif repm == 3:
        return 93
    elif repm == 4:
        return 90
    elif repm == 5:
        return 87
    elif repm == 6:
        return 85
    elif repm == 7:
        return 83
    elif repm == 8:
        return 80
    elif repm == 9:
        return 77
    elif repm == 10:
        return 75
    elif repm == 11:
        return 70
    elif repm == 12:
        return 67
    elif repm == 15:
        return 65
    else:
        return 60


def data_log(weight, reps):
    sub_data = []
    counter = 0
    while counter < reps:
        row_data = []
        temp_weight = (weight * rpmindex(counter + 1) / 100)
        for j in range(1, reps + 1):
            if counter < j - 1:
                row_data.append(" ")
            else:
                row_data.append((temp_weight * rpmindex(j) / 100))
        counter += 1
        sub_data.append(row_data)

    row_header = []
    for i in range(1, reps + 1):
        row_header.append(str(i) + " " + str(rpmindex(i)) + "%")
    columns_header = []
    for i in range(1, reps + 1):
        columns_header.append("RI" + str(rpmindex(i)))  # RI stands Relative Intensity

    return sub_data, row_header, columns_header


while True:
    max_weight = input("Please enter a number ")
    try:
        val = int(max_weight)
        print("Your Max Weight is", val)
        break
    except ValueError:
        try:
            float(max_weight)
            print("Input is an float number.")
            break
        except ValueError:
            print("This is not a number. Please enter a valid number")

print("The weight table is generated", max_weight)

ex_data, r_header, c_data = data_log(int(max_weight), 5)

print(pandas.DataFrame(ex_data, r_header, c_data))
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     exdata = data_log(100)
#     print(exdata[0],
#           exdata[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
