def update_serialConnected(ui):
    ui.Com.setEnabled(False)
    ui.Com.setEnabled(False)
    ui.Baudrates.setEnabled(False)
    ui.DataSize.setEnabled(False)
    ui.Parity.setEnabled(False)

    ui.Start.setEnabled(True)
    ui.Reset.setEnabled(True)
    ui.Record.setEnabled(False)
    ui.Send_2.setEnabled(True)
    ui.AutoScroll.setEnabled(False)
    ui.Hex.setEnabled(True)

    ui.Connect.setText("Disconnect")
    ui.Connect.setStyleSheet('QPushButton {color: red;}')


def update_serialDisconnected(ui):
    ui.Com.setEnabled(True)
    ui.Com.setEnabled(True)
    ui.Baudrates.setEnabled(True)
    ui.DataSize.setEnabled(True)
    ui.Parity.setEnabled(True)

    ui.Start.setEnabled(False)
    ui.Reset.setEnabled(False)
    ui.Record.setEnabled(False)
    ui.Send_2.setEnabled(True)
    ui.AutoScroll.setEnabled(False)
    ui.Hex.setEnabled(False)
    ui.timer_getdata.stop()

    ui.Connect.setText("Connect")
    ui.Connect.setStyleSheet('QPushButton {color: black;}')