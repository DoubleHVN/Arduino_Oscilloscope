import pandas as pd


csv = pd.DataFrame()

def Record(ui, state):
    if (ui.Type.currentText() == "xlsx"):
        relative_path = state.StoragePath + "\\" + str(ui.Name.toPlainText()) + ".xlsx"
        xlsx = pd.DataFrame(data=state.data)
        xlsx.to_excel(relative_path, index=False)
    if (ui.Type.currentText() == "csv"):
        relative_path = state.StoragePath + "\\" + str(ui.Name.toPlainText()) + ".csv"
        csv = pd.DataFrame(data=state.data)
        csv.to_csv(relative_path, index=False)