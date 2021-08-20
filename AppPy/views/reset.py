def update_Reset(ui, state):
    state.a = 0
    state.data = {}
    state.time = []

    ui.Plotter.clear()
    ui.Monitor.clear()