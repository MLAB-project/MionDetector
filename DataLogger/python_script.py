import serial
import time
import pygame

pygame.mixer.init()

pipani = 'C:\\Users\\pc\\Downloads\\uiiiiiiii.mp3'

ser = serial.Serial('COM4', 9600, timeout=1)

file_path = 'G:\\Můj disk\\prespavacka_v_reaktoru\\data_experiment\\hustej_vyzkumnik_pod_posteli.txt'

def read_serial(duration):
    start_time = time.time()
    with open(file_path, 'a') as log_file:
        while True:
            if ser.in_waiting > 0:
                pygame.mixer.music.load(pipani)
                pygame.mixer.music.play()
            
                line = ser.readline().decode('utf-8').rstrip()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                log_line = f"{timestamp}|{line}"
                print(log_line)
                log_file.write(log_line + '\n')
            
            if time.time() - start_time > duration:
                break

with open(file_path, 'a') as log_file:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    cas_zacatku = f"{timestamp}|Miony te zacali mijet|0"
    log_file.write(cas_zacatku + '\n')

duration = 100000

try:
    read_serial(duration)
except Exception as e:
    print("Miony te neminou")
finally:
    with open(file_path, 'a') as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cas_konce = f"{timestamp}|Miony te prestali mijet|0"
        log_file.write(cas_konce + '\n')
    ser.close()
    
