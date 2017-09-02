#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Project: Project Diferential Geometry
# Description of the program: Artificial Intelligence
# Author: Alejandro Sánchez Yalí - Juan David Arias


# Native Libraries of Python
import numpy as np
import sympy as np
import matplotlib.pyplot as plt
import tkinter


class messages(object):
    """
    This class is for the messages of the aplication.
    """
    title = 'Regular'



class regularCurves(object):
    """
    This class is for the study of curves theory.
    """


    def __init__(self):
        """
        This function is for instances the characterict basics of the class.
        """
        # Graphic environment
        main_window = tkinter.Tk()
        main_window.title(messages.title)
        main_window.resizable(width=False, height=False)
        main_window.mainloop()

if __name__ == '__main__':
    regularCurves()