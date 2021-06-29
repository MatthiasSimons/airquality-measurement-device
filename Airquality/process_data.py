value_list = []
def prognosis(value):
    # function for calculating a prognosed ppm value
    list_length = 5 # length of rolling window
    prognosis_length = 30 # prognosis duration in minutes

    def update_value_list(value):
        # create a rolling list
        if len(value_list) < list_length:
            value_list.append(value)
        else:
            value_list.pop(0)
            value_list.append(value)

    def gradient(value_list):
        # calculate gradient
        x_0, x_1 = 0, len(value_list)
        y_0, y_1 = value_list[0], value_list[-1]
        return (y_1-y_0) / (x_1-x_0)

    update_value_list(value)
    # check if value_list has enough values
    if len(value_list) == list_length:
        # calculate time in minutes until ppm value is over 1000 ppm 
        t = (1000-value)/gradient(value_list)
        print("in ", t, " minutes 1000 ppm will be reached")
        
        # calculate prognosed ppm value
        prognosis = value + gradient(value_list)*prognosis_length
        if prognosis < 0:
            return 0
        else:
            return prognosis
    else:
        return 0

