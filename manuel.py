import cv2
import serial
import time
import pygame
import os
pygame.init()
screen = pygame.display.set_mode((600,600))
cap = cv2.VideoCapture(0)
my_font = pygame.font.SysFont('Comic Sans MS', 30)
if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
    ser.reset_input_buffer()
while (True):    
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, [600,600], interpolation= cv2.INTER_LINEAR)
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    text_surface = my_font.render(cpu_temp, False, (0, 0, 0))

    cv2.imwrite("test.jpg",resized_frame)
    Image = pygame.image.load("test.jpg").convert()
    screen.blit(Image, ( 0,0))
    screen.blit(text_surface, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_w:
                ser.write(b"15")
                print("1800")
            if event.key == pygame.K_s:
                ser.write(b"14")
                print("1450")
    if cv2.waitKey(20) == ord("q"):
        break
    pygame.display.flip()
exit()
