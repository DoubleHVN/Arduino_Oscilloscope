def update_startStreaming(ui):
    ui.Record.setEnabled(True)
    ui.Send_2.setEnabled(True)
    ui.AutoScroll.setEnabled(True)
    ui.Hex.setEnabled(True)
    ui.timer_getdata.start()

    ui.Plotter.setBackground("w")
    ui.Plotter.showGrid(x=True, y=True)
    ui.Plotter.setMouseEnabled(x=False, y=False)
    ui.Plotter.addLegend()

    ui.Start.setText("Stop")
    ui.Start.setStyleSheet("QPushButton {color: red}")

def update_stopStreaming(ui):
    ui.Record.setEnabled(False)
    ui.Send_2.setEnabled(False)
    ui.AutoScroll.setEnabled(False)
    ui.Hex.setEnabled(False)
    ui.timer_getdata.stop()
    
    ui.Start.setText("Start")
    ui.Start.setStyleSheet('QPushButton {color: black;}')
