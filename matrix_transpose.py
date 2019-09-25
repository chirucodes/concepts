#Python code to do transpose of a given matrix

def display_matrix(matrix):
    """
    To display a given matrix.
    :param matrix: Multi dimensional matrix
    :return: Nothing
    """
    print("__________________")
    for each_row in matrix:
        print(each_row)
    print("__________________")

input_matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

#####################################################################
#Logic using 'for' loops
transposed_matrix = []
for each_row_index in range(len(input_matrix[0])):
    temp_lst = []
    for each_row in input_matrix:
        temp_lst.append(each_row[each_row_index])
    print(temp_lst)
    transposed_matrix.append(temp_lst)
print("~~~~~~INPUT~~~~~~~~~~")
display_matrix(input_matrix)
print("~~~~~~OUTPUT~~~~~~~~~~")
display_matrix(transposed_matrix)

#####################################################################
#Logic using List Comprehension
transposed_matrix2 = [[each_row[each_row_index] for each_row in input_matrix] for each_row_index in range(len(input_matrix[0]))]
print("~~~~~~INPUT~~~~~~~~~~")
display_matrix(input_matrix)
print("~~~~~~OUTPUT~~~~~~~~~~")
display_matrix(transposed_matrix2)
