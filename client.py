import socket
import pygame

# ====== Port connection setup
#UDP_IP = "127.0.0.1"
#UDP_PORT = 5005
#MESSAGE = "Start your engines!"
#print "UDP target IP:", UDP_IP
#print "UDP target port:", UDP_PORT
#print "message:", MESSAGE

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# =======

pygame.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

clock = pygame.time.Clock()

# [NCURSES INPUT] do not wait for input when calling getch
#stdscr.nodelay(1)

while True:
    pygame.event.pump()
    #for event in pygame.event.get():
    print joystick.get_axis(0),  joystick.get_axis(1)


    # [NCURSES INPUT] get keyboard input, returns -1 if none available
    #c = stdscr.getch()

    #if c == 27:
        #break;
    # pygame.key.get_press()

#        stdscr.addstr(str(int(axis)))
#        stdscr.refresh()
    # return curser to start position
#        stdscr.move(0, 0)

    clock.tick(40)


pygame.quit()

# ====== Port connection actions
#        if c != -1:
#            if c == 27:
#                break;
#            # print numeric value
#
#            sock.sendto(str(c), (UDP_IP, UDP_PORT))
#            stdscr.addstr(str(c) + ' ')
#            stdscr.refresh()
#            # return curser to start position
#            stdscr.move(0, 0)
# =======

#if __name__ == '__main__':
#    curses.wrapper(main)

# Sources:
  # https://stackoverflow.com/questions/39817549/pygame-joystick-get-axis-always-returns-zero
