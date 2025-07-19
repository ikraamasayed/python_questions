# *         *
#  *       *
#   *     *
#    *   *
#     * *
#      *




# ['*', ' ', ' ', ' ', ' ', '*'], 
#   ['*', ' ', ' ', ' ', '*'], 
#     ['*', ' ', ' ', '*'], 
#         ['*', ' ', '*'], 
#         ['*', '*'],  
#             ['*'],
n=6
for i in range(n):
    lst_len = n-i # decreasing iter
    start_space_len = n-lst_len
    # list len decreasing in each iter
    lst = [' ' for el in range(lst_len)] # lsit of space
    lst[0] = '*' # first element *
    lst[-1] = '*' # last element *
    # since start space handeled before, we are applying this below
    print(' '*start_space_len +  ' '.join(lst))


