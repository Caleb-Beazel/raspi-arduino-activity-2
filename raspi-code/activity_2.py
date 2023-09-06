#read serial
#receive number --> if number < 15 --> power on LED
import serial
import time
connect_count = 0

while connect_count < 5:
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1.0)
        print("Connected to Arduino.")
        break
    except serial.SerialException:
            print("Attempt " + str(connect_count + 1) + "Failed to connect.")
            connect_count += 1
            time.sleep(2)
            
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK")

light_status = 'off'

try:
    while True:
        time.sleep(1)
        while ser.in_waiting <= 0:
            
            time.sleep(0.01)
        temp = int(ser.readline().decode('utf-8').rstrip())
        
        if temp < 15 and light_status == 'off':
            ser.write("on\n".encode('utf-8'))
            light_status = 'on'
            print(f"Light was turned on. Temp = {temp}")
        elif temp < 15 and light_status == 'on':
            print(f"Temp = {temp}")
            continue
        elif temp >= 15 and light_status == 'on':
            ser.write("off\n".encode('utf-8'))
            light_status = 'off'
            print(f"Light was turned off. Temp = {temp}")
        elif temp >= 15 and light_status == 'off':
            print(f"Temp = {temp}")
            continue
        else:
            print("Error")
            break
except KeyboardInterrupt:
        print("Connection broken.")
        ser.write("off\n".encode('utf-8'))
        ser.close()