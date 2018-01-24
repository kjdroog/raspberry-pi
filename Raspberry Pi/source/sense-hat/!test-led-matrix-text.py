import sys
from sense_hat import SenseHat 

input_string = sys.argv[1]

sense = SenseHat()
sense.show_message(input_string)
