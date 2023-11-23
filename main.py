from signal import signal, SIGTERM, SIGHUP, pause
import time
import RPi.GPIO as GPIO
from rpi_lcd import LCD

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)


def end_game(score):
    lcd.clear()
    score = str(score)
    lcd.text("Thank you",1)
    lcd.text("for playing!",2)
    time.sleep(3)
    lcd.clear()
    lcd.text("Final score: ",1)
    lcd.text(score,2)
    time.sleep(5)
    lcd.clear()

def quiz():
    score = 0

    lcd.clear()
    lcd.text("Q1: Bytes in a",1) # First line
    lcd.text("    kilobyte?",2) # Second line
    ans = input("Ans: ") # Get user input
    if ans == "1024": # If correct answer: trigger green LED and increment score, else trigger red LED
        score+=1
        triggerLight(26)
    else:
        triggerLight(19)
    

    lcd.clear()
    lcd.text("Q2: # of bits to",1)
    lcd.text("store a number?",2)
    ans = input("Ans: ")
    if ans == "32":
        score+=1
        triggerLight(26)
    else:
        triggerLight(19)

    lcd.clear()
    lcd.text("Q3: # of bits to",1)
    lcd.text("rep. 32?",2)
    ans = input("Ans: ")
    if ans == "6":
        score+=1
        triggerLight(26)
    else:
        triggerLight(19)

    
    lcd.clear()
    lcd.text("Q4: How many bits",1)
    lcd.text("is 1111?",2)
    ans = input("Ans: ")
    if ans == "4":
        score+=1
        triggerLight(26)
    else:
        triggerLight(19)

    lcd.clear()
    lcd.text("Q5: How many",1)
    lcd.text("nums is 12 bits?",2)
    ans = input("Ans: ")
    if ans == "4096": 
        score+=1
        triggerLight(26)
    else:
        triggerLight(19)

    end_game(score)

def triggerLight(gpio):

    GPIO.output(gpio,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(gpio,GPIO.LOW)

def main():
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)
    lcd.text("Welcome!",1)
    lcd.text("Start Quiz?",2)
    prompt = input("Y/N: ")
    GPIO.output(26,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    if (prompt == "Y" or prompt == "y"):
        lcd.clear()
        lcd.text("Let's begin!",1)
        time.sleep(1)
        quiz()
    elif (prompt == "N" or prompt == "n"):
        lcd.clear()
        lcd.text("Goodbye!",1)
        time.sleep(1)
        lcd.clear()
    else: 
        lcd.clear()
        lcd.text("Invalid Input.",1)
        time.sleep(1)
        lcd.clear()

main()