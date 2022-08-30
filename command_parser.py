'''
DESCRIPTION:
Module for parsing commands for CDP 2.0

NOTES:
CommandParser inherets from argparse.ArgumentParser

All command line arguments are optional, the default arguments are defined
at the top of this file. The input commands are assumed
to be separated by a newline character (one command per line). The output is
(command), (response)
..., ...

This file should read a csv file to get a list of serial commands, store those
in the approriate data structure, write the commands in an arbitrary order to
a specifiable COM port (default /dev/ttyUSB0), record the response in a separate
csv file, preferably also with the command that produced the response

AUTHOR:
D.B and G.LC

AFFILIATION:
Bio-Rad, CDG, Advanced-Tech Team

CREATED ON:
8/30/2022
'''

import argparse

# Argument Parser
class CommandParser(argparse.ArgumentParser):

    # Public variables
    COM = 'COM8' #'/dev/ttyUSB0'
    command_fpath = 'commands.csv'
    response_fpath = 'responses.csv'
    baud_rate = 115200

    # Private variables
    __description = "Specify COM port, commands file (in), response file (out),and baud rate"
    __args = None
    __COM_port = None
    __input_fpath = None
    __output_fpath = None
    __baud_rate = None

    def __init__(self):
        super().__init__(self, description=self.__description)
        self.add_argument('-COM', default=self.COM, required=False)
        self.add_argument('-i', default=self.command_fpath, required=False)
        self.add_argument('-o', default=self.response_fpath, required=False)
        self.add_argument('-b', default=self.baud_rate, required=False)
        self.__args = self.parse_args()
        self.__COM_port = self.__args.COM
        self.__input_fpath = self.__args.i
        self.__output_fpath = self.__args.o
        self.__baud_rate = self.__args.b

    def getArgs(self):
        return self._args

    def getCOMPort(self):
        return self.__COM_port

    def getInputFPath(self):
        return self.__input_fpath

    def getOutputFPath(self):
        return self.__output_fpath

    def getBaudRate(self):
        return self.__baud_rate

    def setOutputFPath(self, output_fath):
        self.__output_fpath = output_fath
        self.__args.o = output_fath


