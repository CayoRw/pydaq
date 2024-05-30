from pydaq.pid_control import MyGUI, create_application

app = create_application()
gui = MyGUI(app)
gui.show()
app.exec_()
