def enders(num_list):
    '''
    list -> list

    Given a list of nubers returns a list containing just the first and last item of the list

    >>>enders([3, 56, 56, 2, 89])
    [3, 89]
    >>>enders(["skip", "daily", 4, 67, 4.5, "alky"])
    ["skip", "alky"]
    >>>enders([56, "else", 44, "reader"])
    [56, "reader"]

    '''

    ends = [num_list[0], num_list[-1]]

    print(ends)
    
