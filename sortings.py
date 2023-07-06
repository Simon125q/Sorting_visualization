import visual_table as vt

def bubble_sort(table):
    for iteration in range(table.length-1):
        for index in range(table.length-1-iteration):
            if table.compare(index, index+1):
                table.swap(index, index+1)
    return table

def insertion_sort(table):
    for index in range (1, table.length):
        com_index = index
        while(com_index > 0 and table.compare(com_index-1, com_index)):
            table.swap(com_index-1, com_index)
            com_index -=1
    return table


if __name__ == "__main__":
    array = [12, 43, 1, 0, 67, 89, 17, 21, 13]
    vTable = vt.VisualTable(array)
    #new_array = bubble_sort(vTable)
    new_array = insertion_sort(vTable)