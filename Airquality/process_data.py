value_list = []
def prognosis(value):
    list_length = 5
    prognosis_length = 30

    def update_value_list(value):
        if len(value_list) < list_length:
            value_list.append(value)

        else:
            value_list.pop(0)
            value_list.append(value)

    def gradient(value_list):
        x_0, x_1 = 0, len(value_list)
        y_0, y_1 = value_list[0], value_list[-1]
        return (y_1-y_0) / (x_1-x_0)

    update_value_list(value)

    if len(value_list) == list_length:
        t = (1000-value)/gradient(value_list)
        print(t)

        prognosis = value + gradient(value_list)*prognosis_length
        if prognosis < 0:
            return 0
        else:
            return prognosis
    else:
        return 0

