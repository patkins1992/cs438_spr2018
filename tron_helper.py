# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:19:19 2018

@author: diane
"""

import numpy as np

class bad_data(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))

def append_data(filename, x, y):
    """This function is called to add player data to the training file for Tron.
    It will be used in 
    Args:   filename: the name the training data will be stored in.
            x: a list of lists. Each list contains a board state from the point
                of view of the player making the move. Should be 1 x 400.
            y: a list of lists. Each list contains the "correct" move based on
                the strategy employed by the player in the Tron game. Should be
                1 x 4.
    Returns: True if data was successfully added to training data, False
                otherwise.
    Raises: bad_data: if the length of the list containing the board states is
                not equal to the length of the list containing the correct
                moves, this error is raised and no data is added to the data
                file.
    """
    #test that the length of x == the length of y. If not - do not process data.
    try:
        if len(x) != len(y):
            raise(bad_data)
    except bad_data as error:
        return False
    #open the specified filename to append the test data to
    training_data = open(filename, 'a+', 1)
    #for each line in x,y
    for i in range(len(x)):
        #create a string that contains one list from x, a ":", then one list
        #from y
        add_data = x[i] + ":" + y[i] + "\n"
        #append that string to the file
        training_data.write(add_data)
    #close the file
    training_data.close()
    return True

def format_input_data(filename):
    """This function will generate the training or testing data for the neural
    net. The input data file will contain 1 record per line in the format:
    board_state:correct_move
    The board states will be stored in x (which will contain a list of lists).
    The correct states will be stored in y (which will also contain a list of
    lists.) These lists will be returned when the function is called.
    Args: filename: the name of the file where the data is.
    Returns: (x, y) where x is a list of board states, and y is a list of
             correct answers for the board states (correlated by index).
             If there is a problem with the data file, ([0],[0]) is returned.
    Raises: OSError or IOError if there is a problem with the data file
    """
    x = []
    y = []
    #open the file containing the training data
    try:
        training_data = open(filename, 'r', 1)
        #for each line in the file, split the line on the ':' character, putting
        #the first part of the line into x, and the second part of the line into
        #y.
        for line in training_data:
            line = str.replace(line, '[', '')
            line = str.replace(line, ']', '')
            line = str.replace(line, '\'', '')
            line = str.replace(line, '\n', '')
            line_list = line.split(':')
            #x_list = str.replace(line_list[0], "'", "")
            single_x_record = []
            x_line_list = line_list[0].split(', ')
            for i in x_line_list:
                i = float(i)
                single_x_record.append(i)
            x_record = np.array(single_x_record)
            x.append(x_record)
            #x.append(np.array(line_list[0]))
            #y.append(np.array(line_list[1]))
            single_y_record = []
            y_line_list = line_list[1].split(', ')
            for j in y_line_list:
                j = float(j)
                single_y_record.append(j)
            y_record = np.array(single_y_record)
            y.append(y_record)
        #close the file
        training_data.close()
        x = np.array(x)
        y = np.array(y)
        return(x, y)
    except(OSError, IOError):
        x.append(0)
        y.append(0)
        x = np.array(x)
        y = np.array(y)
        return(x, y)

