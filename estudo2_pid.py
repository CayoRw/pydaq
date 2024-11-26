import serial  # Importa o módulo serial

try:
    ser = serial.Serial('COM3', 9600, timeout=2)  # Ajuste para a sua porta
    print("Conexão bem-sucedida.")
    ser.write("Teste de comunicação\n".encode('utf-8'))  # Codificando com UTF-8
    data = ser.readline()
    print(f"Dados recebidos: {data.decode('utf-8')}")
    ser.close()
except Exception as e:
    print(f"Erro de conexão: {e}")
