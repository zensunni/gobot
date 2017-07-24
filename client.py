import socket
import curses

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Start your engines!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


def main(stdscr):

    # do not wait for input when calling getch
    stdscr.nodelay(1)


    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value

            sock.sendto(str(c), (UDP_IP, UDP_PORT))
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)

if __name__ == '__main__':
    curses.wrapper(main)

