import datetime
import pygame.mixer
import time
import threading
import RPi.GPIO as GPIO

#time_now
def alarm():
    set_timer=0
    
    while True:
        button = GPIO.input(27)
        time_now = datetime.time.hour #現在の時刻を取得
        print("今の時間:")
        print(time_now)
        print("セットタイマー")

        if time_now == set_timer:
            sound()#再生

#pause method
#loop until pushed button
# 60*5sec pause after 60sec sound
def time_pause(pause_time):
    while True:
        if (datetime.time.minute - pause_time) % 5 == 0:
            pygame.mixer.unpause()
        if button == HIGH:
            finish_program()
        pygame.mixer.pause()
        time.sleep(60*5) #300sec pause


#sound method
def sound():
    button = GPIO.input(27)
    pygame.mixer.init()
    pygame.mixer.music.load('Cat.mp3')
    pygame.mixer.music.play()

    if datetime.time.minute == 1:#初回
        pygame.mixer.pause()
        pause_time = datetime.time.minute
        time_pause(pause_time)

        
def finding_out():
    while True:
        rmotion = GPIO.input(25)
        lmotion = GPIO.input(26)

        #in room
        #rmotion = 0, lmotion = 0

        #when someone coming, program finish 
        if (rmotion == 0 and lmotion == 1) or (rmotion == 1 and lmotion == 1):
            finish_program()

#finish the program
def finish_program():
    while True:
        if GPIO.input(28) == 1:
            GPIO.cleanup()
            break

if __name__ == "__main__":
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25,GPIO.IN) #rsensor
    GPIO.setup(26,GPIO.IN) #lsensor
    GPIO.setup(27,GPIO.IN) #button
    GPIO.setup(28,GPIO.IN) #finish

    thread_1 = threading.Thread(target = alarm)
    thread_2 = threading.Thread(target = finding_out)
    thread_3 = threading.Thread(target = finish_program)
    thread_1.start()
    thread_2.start()
    thread_3.start()



