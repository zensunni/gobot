# Gobot

Gobot is a project for a cellular network controlled robot buggy that can navigate pedestrian pathways, interact with people, and go anywhere there is a cell phone reception.

While building a robot that can be operated from your home might seem like the epitome of lazyness, a device like this has a wide variety of applications, especially for people with disabilities.

## Iterations:

* POC: RC car controlled via cell network
* Alpha: Buy an item from a store
* Beta: Sidewalk navigation AI

## Requirements:

POC

* RC car wheel chassis (radio controlled parts not needed)
* Phone case to snap in phone
* Phone (utilizing camera)
* PC game controller
* [IOIO (Android breakout board)](sparkfun.com/products/13613)

Alpha

* Self opening/closing holding tank
* Self opening/closing cash box
* video camera (phone or GoPro)
* Text display (phone, possibly)

Possible Software

* pypi.python.org/pypi/inputs
* libsdl.org/languages.php
* github.com/jkuhlmann/gainput

## Gamepad input:

* Language: python
* Library: PyGame_SDL2, or maybe just straight-up pygame

Notes:

* It looks like everyone is using pygame's .joystick and/or .key api
* PyGame_SDL2 is a reimplementation of the Pygame API using SDL2 and related libraries.

Helpful sources:

* PyGame_SDL2: https://github.com/renpy/pygame_sdl2
* Pygame docs: http://www.pygame.org/docs
* https://www.reddit.com/r/pygame/comments/1zgixs/xbox_360_controller_with_pygame/
* https://yameb.blogspot.ca/2013/01/gamepad-input-in-python.html
* http://robots.dacloughb.com/project-1/logitech-game-pad/
