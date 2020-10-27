import datetime
import sys
import time
import scrollphathd as sphd


sphd.set_brightness(0.5)
sphd.rotate(degrees=180)

def get_delta():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:&S"))
    halloween = datetime.datetime(2020,10,31,0,0)
    print(halloween.strftime("%Y-%m-%d %H:%M:&S"))
    delta = halloween - now 
    print(delta.days)
    return delta.days

def set_message(days):
    if days + 1 < 1:
        message = "Happy Halloween!!!   "
    else:
        message = str(days + 1)
    return message   

def pumpkins():
    bri = 0.5
    pic1 = [(0,4,bri),(0,12,bri),(1,2,bri),(1,3,bri),(1,4,bri),(1,5,bri),
    (1,6,bri),(1,10,bri),(1,11,bri),(1,12,bri),(1,13,bri),(1,14,bri),
    (2,1,bri),(2,2,bri),(2,4,bri),(2,6,bri),(2,7,bri),(2,9,bri),(2,10,bri),
    (2,12,bri),(2,14,bri),(2,15,bri),(3,1,bri),(3,2,bri),(3,3,bri),(3,4,bri),
    (3,5,bri),(3,6,bri),(3,7,bri),(3,9,bri),(3,10,bri),(3,11,bri),(3,12,bri),
    (3,13,bri),(3,14,bri),(3,15,bri),(4,1,bri),(4,2,bri),(4,3,bri),(4,4,bri),
    (4,5,bri),(4,6,bri),(4,7,bri),(4,9,bri),(4,10,bri),(4,11,bri),(4,12,bri),
    (4,13,bri),(4,14,bri),(4,15,bri),(5,1,bri),(5,2,bri),(5,6,bri),(5,7,bri),
    (5,9,bri),(5,10,bri),(5,14,bri),(5,15,bri),(6,2,bri),(6,3,bri),(6,4,bri),
    (6,5,bri),(6,6,bri),(6,10,bri),(6,11,bri),(6,12,bri),(6,13,bri),
    (6,14,bri)]

    pic2 = [(0,4,bri),(0,12,bri),(1,2,bri),(1,3,bri),(1,4,bri),(1,5,bri),
    (1,6,bri),(1,10,bri),(1,11,bri),(1,12,bri),(1,13,bri),(1,14,bri),
    (2,1,bri),(2,2,bri),(2,4,bri),(2,6,bri),(2,7,bri),(2,9,bri),(2,10,bri),
    (2,12,bri),(2,14,bri),(2,15,bri),(3,1,bri),(3,2,bri),(3,3,bri),(3,4,bri),
    (3,5,bri),(3,6,bri),(3,7,bri),(3,9,bri),(3,10,bri),(3,11,bri),(3,12,bri),
    (3,13,bri),(3,14,bri),(3,15,bri),(4,1,bri),(4,2,bri),(4,3,bri),(4,4,bri),
    (4,5,bri),(4,6,bri),(4,7,bri),(4,9,bri),(4,10,bri),(4,11,bri),(4,12,bri),
    (4,13,bri),(4,14,bri),(4,15,bri),(5,1,bri),(5,2,bri),(5,6,bri),(5,7,bri),
    (5,9,bri),(5,10,bri),(5,14,bri),(5,15,bri),(6,2,bri),(6,3,bri),(6,4,bri),
    (6,5,bri),(6,6,bri),(6,10,bri),(6,11,bri),(6,12,bri),(6,13,bri),
    (6,14,bri),(2,3,bri),(2,5,bri),(2,11,bri),(2,13,bri)]

    x = 0
    while x < 5:
        sphd.clear()
        for pixel in pic1:
            print(pixel)
            sphd.set_pixel(pixel[1],pixel[0],pixel[2])
        sphd.show()
        time.sleep(0.1)
        sphd.clear()
        for pixel in pic2:
            sphd.set_pixel(pixel[1],pixel[0],pixel[2])
        sphd.show()
        x += 1

def bat():
    bri = 0.5
    pic1 = [(1,1,bri),(1,2,bri),(1,3,bri),(1,6,bri),
    (1,9,bri),(1,12,bri),(1,13,bri),(2,1,bri),(2,2,bri),(2,3,bri),
    (2,4,bri),(2,6,bri),(2,7,bri),(2,8,bri),(2,9,bri),(2,11,bri),(2,12,bri),
    (2,13,bri),(2,14,bri),(3,2,bri),(3,3,bri),(3,4,bri),(3,5,bri),(3,7,bri),
    (3,8,bri),(3,10,bri),(3,11,bri),(3,12,bri),(3,13,bri),(4,4,bri),(4,5,bri),
    (4,6,bri),(4,7,bri),(4,8,bri),(4,9,bri),(4,10,bri),(4,11,bri),(5,7,bri),
    (5,8,bri)]

    pic2 = [(1,6,bri),(1,9,bri),(2,6,bri),(2,7,bri),(2,8,bri),(2,9,bri),
    (3,4,bri),(3,5,bri),(3,7,bri),(3,8,bri),(3,10,bri),(3,11,bri),
    (4,2,bri),(4,3,bri),(4,4,bri),(4,5,bri),(4,6,bri),(4,7,bri),(4,8,bri),
    (4,9,bri),(4,10,bri),(4,11,bri),(4,12,bri),(4,13,bri),(5,1,bri),(5,2,bri),
    (5,3,bri),(5,4,bri),(5,7,bri),(5,8,bri),(5,11,bri),(5,12,bri),(5,13,bri),
    (5,14,bri),(6,1,bri),(6,2,bri),(6,3,bri),(6,12,bri),(6,13,bri),(6,14,bri)]

    x = 0
    while x < 5:
        sphd.clear()
        for pixel in pic1:
            print(pixel)
            sphd.set_pixel(pixel[1],pixel[0],pixel[2])
        sphd.show()
        time.sleep(0.1)
        sphd.clear()
        for pixel in pic2:
            sphd.set_pixel(pixel[1],pixel[0],pixel[2])
        sphd.show()
        x += 1


def ghost():
    bri = 0.5
    x = 0
    

    while x < 17:
        sphd.clear()
        pic1 = [(0,x+1,bri),(0,x+2,bri),(0,x+3,bri),(0,x+4,bri),(0,x+5,bri),
        (1,x+0,bri),(1,x+1,bri),(1,x+2,bri),(1,x+3,bri),(1,x+4,bri),(1,x+5,bri),
        (1,x+6,bri),(2,x+0,bri),(2,x+3,bri),(2,x+6,bri),(3,x+0,bri),(3,x+3,bri),
        (3,x+6,bri),(4,x+0,bri),(4,x+1,bri),(4,x+2,bri),(4,x+3,bri),(4,x+4,bri),
        (4,x+5,bri),(4,x+6,bri),(5,x+0,bri),(5,x+1,bri),(5,x+2,bri),(5,x+3,bri),
        (5,x+4,bri),(5,x+5,bri),(5,x+6,bri),(6,x+0,bri),(6,x+2,bri),(6,x+4,bri),
        (6,x+6,bri)]

        pic2 = [(0,x+1,bri),(0,x+2,bri),(0,x+3,bri),(0,x+4,bri),(0,x+5,bri),
        (1,x+0,bri),(1,x+1,bri),(1,x+2,bri),(1,x+3,bri),(1,x+4,bri),(1,x+5,bri),
        (1,x+6,bri),(2,x+0,bri),(2,x+3,bri),(2,x+6,bri),(3,x+0,bri),(3,x+3,bri),
        (3,x+6,bri),(4,x+0,bri),(4,x+1,bri),(4,x+2,bri),(4,x+3,bri),(4,x+4,bri),
        (4,x+5,bri),(4,x+6,bri),(5,x+0,bri),(5,x+1,bri),(5,x+2,bri),(5,x+3,bri),
        (5,x+4,bri),(5,x+5,bri),(5,x+6,bri),(6,x+1,bri),(6,x+3,bri),(6,x+5,bri)]
        for pixel in pic1:
            print(pixel)
            sphd.set_pixel(pixel[1],pixel[0],pixel[2])
        sphd.show()
        time.sleep(0.1)
        sphd.clear()
        x += 1
        for pixel in pic2:
            sphd.set_pixel(pixel[1],pixel[0],pixel[2])
        sphd.show()
        x += 1

def boo():
    x = 0
    while x < 5:
        sphd.clear()
        sphd.write_string('BOO')
        sphd.show()
        time.sleep(0.1)
        sphd.clear()
        sphd.show()
        time.sleep(0.1)
        x += 1

while True:
    sphd.clear()
    days = get_delta()
    message = set_message(days)
    sphd.write_string(message)
    sphd.show()
    time.sleep(5)
    sphd.clear()
    pumpkins()
    sphd.clear()
    sphd.write_string(message)
    sphd.show()
    time.sleep(5)
    sphd.clear()
    ghost()
    sphd.clear()
    sphd.write_string(message)
    sphd.show()
    time.sleep(5)
    sphd.clear()
    bat()
    sphd.clear()
    sphd.write_string(message)
    sphd.show()
    time.sleep(5)
    sphd.clear()
    boo()
