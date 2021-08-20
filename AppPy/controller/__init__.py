from controller.maxmin import update_Max, update_Min

class Controllers(object):
    def __init__(self, view, app):
        self.app = app
        self.view = view
        Strdata = self.readData()
        # print(Strdata)
        data, pen = self.dataProcessor(Strdata)
        if data!= False:
            self.Monitor(Strdata)
            update_Max(view.ui, app.state)
            update_Min(view.ui, app.state)
            self.Drawer(data, pen)
        else :
            pass
    def readData(self):
        self.app.state.bytetoread = self.app.state.serialConn.inWaiting()
        
        try:
            if (self.app.state.bytetoread > 0):
                self.app.state.receive_data = self.app.state.serialConn.readline()
                Strdata = str(self.app.state.receive_data, "utf-8")
                if Strdata:
                    final = Strdata.replace("\r\n", "")
                    return final

        except:
            pass

    def dataProcessor(self, Strdata):
        data = {}
        package = []
        name = []
        value = []
        try:
            ob = Strdata.split(",")
            for i in ob:
                temp = i.split(":")
                package.append(temp)
            for i,q in enumerate(package):
                name.append(q[0])
                value.append(q[1])
            data = dict({name[i]:[] for i in range(len(name))})
            for i in name:
                for j in range(len(name)):
                    if name[j] == i:
                        data[i].append(float(value[j]))

            pen = dict({name[i]:self.app.state.color[i] for i in range(len(name))})
            return data, pen
        except (KeyError , AttributeError , ValueError) as e:
            return False , e

    def Monitor(self, Strdata):
        self.view.ui.Monitor.append(Strdata)

            
    def Drawer(self, data, pen):
        self.app.state.a += 1
        self.app.state.time.append(self.app.state.a*100)

        try:
            if self.app.state.a == 1:
                self.app.state.data = data
            else:
                for i in data:
                    self.app.state.data[i] = self.app.state.data[i] + data[i]
            
            for i in self.app.state.data:
                if self.app.state.a == 1:
                    self.view.ui.Plotter.plot(self.app.state.time, self.app.state.data[i], name=i, pen=pen[i])
                else:
                    self.view.ui.Plotter.plot(self.app.state.time, self.app.state.data[i], pen=pen[i])
        except KeyError:
            pass