# Project Zeng.
Project Zeng is a school project for the second year Q1 of the Software Engineering/Security Engineering course of the Hanze University of Applied Sciences.

The goal of this project is to design an solar screen control unit for a fictional company Zeng 😎.

The project consist of two parts, an dashboard written in Python 3.5x used to control and modify the control units running on Arduino Uno's written in C.

## C
The latest build can be found under *C > build* and can be flashed to an Arduino Uno using avrdude.

To build the program you can use the avr-gcc toolchain.
An example (linux) build process would be.

    # Cd to src/
    # Compile using gcc
    avr-gcc -Os -mmcu=atmega328p main.c -o ../build/build.o
    # Convert to hex
    avr-objcopy -O ihex ../build/build.o ../build/build.hex
    # Flash to Arduino using avrdude
    avrdude -c arduino -P /dev/ttyACM0 -p m328p -U flash:w:../build/build.hex
