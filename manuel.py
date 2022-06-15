import cv2
import serial
import time
import pygame
import os
line = ""
a = 0
pygame.init()
screen = pygame.display.set_mode((500,1000))
cap = cv2.VideoCapture(0)
my_font = pygame.font.SysFont('Comic Sans MS', 30)
if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
    ser.reset_input_buffer()
while (True):    
    ret, frame = cap.read()
    frame1 = cv2.pyrDown(frame)
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    text1 = my_font.render(cpu_temp, False, (255, 255, 255))
    text1_ = my_font.render(cpu_temp, False, (0, 0, 0))
    cv2.imshow("kamera1",frame)
    #cv2.imwrite("test.jpg",frame1) #Image = pygame.image.load("test.jpg").convert() #screen.blit(Image, ( 0,0))
    screen.blit(text1, (0,0))
    text2_ = my_font.render(line, False, (0, 0, 0))
    print(ser.in_waiting )
    if ser.in_waiting > 37:
        if a > 0:
            line = ""
            screen.blit(text2_, (0,30))
        line = ser.readline().decode('utf-8').rstrip()
        text2 = my_font.render(line, False, (255, 255, 255))
        text2_ = my_font.render(line, False, (0, 0, 0))
        screen.blit(text2, (0,30))
        a += 1
    elif ser.in_waiting > 10:
        ser.readline().decode('utf-8').rstrip()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            ser.write(b"15")
            print("1800")
        elif keys[pygame.K_s]:
            ser.write(b"18")
            print("1200")
        elif keys[pygame.K_1]:
            ser.write(b"16")
            print("motor1 1900")
        elif keys[pygame.K_2]:
            ser.write(b"17")
            print("motor2 1900")
        if event.type == pygame.KEYUP:
            ser.write(b"14")
            print("1450")
    if cv2.waitKey(20) == ord("q"):
        exit()
    pygame.display.flip()
    screen.blit(text1_, (0,0))
    #print(len(line))

