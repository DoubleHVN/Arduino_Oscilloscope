def update_Max(ui, state):
    max_value = []
    display = ""
    keys = list(state.data.keys())
    for i in state.data:
        max_value.append(max(state.data[i]))
    for i in range(len(keys)):
        display = display + str(keys[i]) + ":" + str(max_value[i]) + ";"
    ui.Max.clear()
    ui.Max.append(display)


def update_Min(ui, state):
    min_value = []
    display = ""
    keys = list(state.data.keys())
    for i in state.data:
        min_value.append(min(state.data[i]))
    for i in range(len(keys)):
        display = display + str(keys[i]) + ":" + str(min_value[i]) + ";"
    ui.Min.clear()
    ui.Min.append(display)