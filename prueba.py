import mss
import mss.tools
from window import quicktime_values

with mss.mss() as sct:

    #1334x750

    #left=x, top=y de inicio de la imagen, cuadrante 4 en plano
    monitor = {"top": 400, "left": 800, "width": 375, "height": 200}
    import time

import cv2
import mss
import numpy


with mss.mss() as sct:
    # Part of the screen to capture

    #quicktime_values = [xSize, ySize, xPos, yPos]
    quicktime_values = quicktime_values().rstrip().split(', ')
    quicktime_values = list(map(int, quicktime_values))


    monitor = {"top": quicktime_values[3],
        "left": quicktime_values[2],
        "width": quicktime_values[0],
        "height": quicktime_values[1]}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", cv2.resize(img, (quicktime_values[0]//2, quicktime_values[1]//2)) )

        #if img[10, 20]
        print(quicktime_values)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
