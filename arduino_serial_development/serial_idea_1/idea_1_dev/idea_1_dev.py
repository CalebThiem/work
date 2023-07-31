import serial
import time

def send_to_arduino(data, port='/dev/ttyACM0', baud_rate=115200):
    ser = serial.Serial(port, baud_rate)  # replace '/dev/ttyACM0' with your serial port

    # Wait for the Arduino to reset
    time.sleep(2)

    # Send the data
    ser.write(b'a')
    for char in data:
        ser.write(char.encode())
        time.sleep(0.00001)  # Delay to prevent Arduino's serial buffer from overflowing
    ser.write(b'z')

    # Print out the sent data
    print('Sent data:    ', data)

    # Wait for Arduino to start transmission (human intuition that fixed the program!)
    time.sleep(0.05)

    # Wait for the Arduino to send back the data
    received_data = ser.readline().decode().strip()

    # Verify the data
    if received_data == data:
        print('Data verification successful')
        ser.write(b'Proceed')
    else:
        print('Error: Data verification failed. Resending data...')
        send_to_arduino(data, port, baud_rate)

    ser.close()