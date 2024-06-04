# compilador.py
#from pydaq.pid_control import *
#app = start_application()


from pydaq.step_response import Step_response
s = Step_response()
#s.step_response_arduino_gui()

s.step_response_arduino_pyside()