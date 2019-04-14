# This script uses lists to display the list content in tabular format
# All the credit goes to Bhusp (Bhushan Pathak) for this script
# Give credits while using it...

import sys

# Definig lists which will store the data...
# Header_list will store the header content, data will store the rows and max_col_width contains maximum width of columns

header_list = list()
data = list()
max_col_width = list()

# This method just copies the header content into header_list to use it later

def add_header(head_list):
    global header_list
    header_list = head_list

# This method checks whether columns of header and data are same or not and then copies the row into data list

def insert_row(row_list):
    global data
    if len(header_list) == len(row_list):
        data.extend(row_list)
    else:
        print('header_list column number does not match with given list columns...don\'t you want to print your data?\n')
        sys.exit(0)

# This method prints the '-' to make display tabular

def repeated_print():
    for i in range(0, len(header_list), 1):
        if not max_col_width:
            sys.stdout.write(' ' + '-' * (len(header_list[i]) + 2))
        else:
            if max_col_width[i] <= len(header_list[i]):
                sys.stdout.write(' ' + '-' * (len(header_list[i]) + 2))
            elif max_col_width[i] > len(header_list[i]):
                sys.stdout.write(' ' + '-' * (max_col_width[i] + 2))

# This function retuens item length which is max in that list

def get_max_width(item_list):
    width = 0
    for item in item_list:
        if len(item) > width:
            width = len(item)
    return width

# Main function where displaying happens

def tabular_print():
    global max_col_width
    for x in range(0, len(header_list), 1):
        max_col_width.append(get_max_width([data[i] for i in range(x, len(data), len(header_list))]))
        #max_col_width.append(len(max([data[i] for i in range(x, len(data), len(header_list))])))
   
    repeated_print()

    print()

    for i in range(0, len(header_list), 1):
        if i == len(header_list) - 1:
            if not max_col_width:
                sys.stdout.write(sys.stdout.write('| ' + header_list[i] + ' ' * (len(header_list[i]) + 1)) + '|')
            else:
                if max_col_width[i] <= len(header_list[i]):
                    sys.stdout.write('| ' + header_list[i] + '|')
                elif max_col_width[i] > len(header_list[i]):
                    sys.stdout.write('| ' + header_list[i] + ' ' * (max_col_width[i] - len(header_list[i]) + 1) + '|')
        else:
            if not max_col_width:
                sys.stdout.write(sys.stdout.write('| ' + header_list[i] + ' ' * (len(header_list[i]) + 1)))
            else:
                if max_col_width[i] <= len(header_list[i]):
                    sys.stdout.write('| ' + header_list[i] + ' ')
                elif max_col_width[i] > len(header_list[i]):
                    sys.stdout.write('| ' + header_list[i] + ' ' * (max_col_width[i] - len(header_list[i]) + 1))
    print()
    
    repeated_print()

    print()
    
    temp = 0
    z = 0
    run_while = len(data)/len(header_list)
    while(z < run_while):
        for i in range(temp, len(header_list) + temp, 1):
            if i == len(header_list) + temp - 1:
                if not max_col_width:
                    sys.stdout.write('| ' + data[i] + ' ' * (len(header_list[i - temp]) - len(data[i]) + 1) + '|')
                else: 
                    if max_col_width[i - temp] <= len(header_list[i - temp]):
                        sys.stdout.write('| ' + data[i] + ' ' * (len(header_list[i - temp]) - len(data[i]) + 1) + '|')
                    elif max_col_width[i - temp] > len(header_list[i - temp]):
                        sys.stdout.write('| ' + data[i] + ' ' * (max_col_width[i - temp] - len(data[i]) + 1) + '|')
            else:
                if not max_col_width:
                    sys.stdout.write('| ' + data[i] + ' ' * (len(header_list[i - temp]) - len(data[i]) + 1))
                else: 
                    if max_col_width[i - temp] <= len(header_list[i - temp]):
                        sys.stdout.write('| ' + data[i] + ' ' * (len(header_list[i - temp]) - len(data[i]) + 1))
                    elif max_col_width[i - temp] > len(header_list[i - temp]):
                        sys.stdout.write('| ' + data[i] + ' ' * (max_col_width[i - temp] - len(data[i]) + 1))
        print()
        
        repeated_print()
        
        print()
        temp = temp + len(header_list)
        z = z + 1
        if z >= run_while:
            header_list.clear()
            data.clear()
            max_col_width.clear()
