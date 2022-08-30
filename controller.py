'''
DESCRIPTION:
This module contains the Controller which deals with read/writing to the COM port and executing commands. 

USAGE:
python controller.py -COM COM_port -i input_filename -o output_filename

NOTES:
Controller is inherets from serial.Serial

All command line arguments are optional, the default arguments are defined
at the top of this file. The input commands are assumed
to be separated by a newline character (one command per line). The output is
(command), (response)
..., ...

This file should read a csv file to get a list of serial commands, store those
in the approriate data structure, write the commands in an arbitrary order to
a specifiable COM port (default /dev/ttyUSB0), record the response in a separate
csv file, preferably also with the command that produced the response
'''

import sys
import time
import serial
import numpy as np

sys.path.insert(0, './sample_prep_operations')
sys.path.insert(0, './reader_operations')

from command_parser import CommandParser
from coordinate import Coordinate

from home_pipettor import HomePipettor
from tip_pickup import TipPickup

class Controller(serial.Serial):
    # Public variables.

    # Private variables.
    __COM_port = None
    __baud_rate = None
    __command_parser = CommandParser()
    __command_list = None

    def __init__(self):
        # Get the COM port and baud rate.
        self.__COM_port = self.__command_parser.getCOMPort()
        self.__baud_rate = self.__command_parser.getBaudRate()

        # Setup the serial connection to the COM port.
        try:
            super().__init__(self.__COM_port, self.__baud_rate, timeout=2)
        except Exception as e:
            print(e)
            print("Connection timeout on COM port {0}".format(self.__COM_port))

    def run_from_script(self):
        print("Need 'english' commands for scripts for extraction etc.")

    def run_from_csv(self):
        # Process the commands file to get an nparray of the commands.
        self.__command_list = np.loadtxt(fname=self.__command_parser.getInputFPath(), dtype=str, delimiter='\n')

        # Write and Read to the COM port.
        with open(self.__command_parser.getOutputFPath(), 'w') as wf:
            for command in self.__command_list:
                # Check that the command is a byte string.
                try:
                    command = command.encode('utf -8')
                except AttributeError:
                    # String is already a byte string.
                    pass

                # Write to the COM port.
                self.write(command)

                # Read a byte.
                response = self.read()

                # Build log output.
                log = ','.join((command.decode(), response.decode(), '\n'))
                wf.write(log)

if __name__ == '__main__':
    controller = Controller()

    # Test Homing.
    print("Test:")
    print("\tFunction Name: HomePipettor()")
    HomePipettor(controller)
    print("\tCompleted: Yes")

    # Test Pickup Tips 
    tip_trays = [i for i in range(4)]
    tip_rows = [i for i in range(12)]
    for tip_tray in tip_trays:
        for tip_row in tip_rows:
            print("Test:")
            print("\tFunction Name: TipPickup(tip_tray={0}, tip_row={1})".format(tip_tray, tip_row))
            #TipPickup(controller, tip_tray, tip_row)
            print("\tCompleted: Yes")
            print("\n\tWait 5 seconds...\n")
            #time.sleep(5)