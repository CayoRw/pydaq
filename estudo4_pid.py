import serial
print(serial.__version__)  # Verifique a versão instalada
ser = serial.Serial('COM3', 9600, timeout=2)
print("Serial inicializado com sucesso!")
ser.close()
