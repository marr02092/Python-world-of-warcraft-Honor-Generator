# Python-world-of-warcraft-Honor-Generator
This is a little program I wrote in python using the PYAUTOGUI library to generate honor for my world of warcraft character 
(Don't do this type of things on blizzard's servers or u will get banned)

'this could be done without the program but it would be slow, boring, and tyring, so i coded and it will repeat the procedures for the whole day if i want"

This is what my little program does.
It will create two characters in two different wow windows, one will receive the honor(honor generator) and the other will be 
killed to provide honor to the other character(enemy). the names are randomly generated until it finds one that's available,
after that it will teleport the enemy infront of the honor generator, switch windows and get the enemy killed, then it will 
delete the enemy character, create a new one and repeat the same thing again and again. Through the process it will be constantly 
checking that everything is going as planned and if something goes wrong, for example, "the game crashes", it will reopen the game
and continue like nothing happened.

In order to move around the graphical interface of the game I used
PYAUTOGUI which is very useful to automate robotic boring tasks :D.
