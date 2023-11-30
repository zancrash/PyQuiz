
# PyQuiz

PyQuiz is built using a Raspberry Pi in conjunction with a 1602 LCD screen. For this build, I used the LCD screen as well as two LED lights. I wrote a Python script that will display quiz questions on the LCD screen, and the user must enter the answers through the command line to progress. If the answer is correct, the user’s score is incremented and the green LED is triggered, if the answer is incorrect, the red LED is triggered.

### Demo:

https://github.com/zancrash/PiQuiz/assets/17016252/104c2c15-1ef8-4e26-9fde-e9d1085a329a



To write the program, I had to use the rpi_lcd python library which creates an LCD class and allows text to be sent to the display. 

Displaying text on the screen:
```
from rpi_lcd import LCD
from time import sleep

lcd = LCD()

lcd.text("This text will appear on the top half of the screen", 1)
lcd.text("This text will appear on the bottom half of the screen!", 2)

```

Clear text on screen:
```
lcd.clear()
```



One of the challenges I ran into was finding a suitable and easy-to-use library, the second was installing the library onto my pi as it isn’t connected to the internet, I had to do some research on installing a library from source.

https://github.com/bogdal/rpi-lcd

This is the link to the open-source library that I used, I found this useful because it allowed me to look at the library’s source code to get an understanding of its structure, and the readme gives a demonstration of how it works.

https://packaging.python.org/en/latest/tutorials/installing-packages/ 

This page goes over several methods of installing Python packages. It was helpful to me as it helped me in manually installing the rpi_lcd library.

https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi

This is a guide on setting up and interfacing the 1602 LCD screen with the Raspberry Pi, it helped to setup the LCD screen with the cobbler and pi.
