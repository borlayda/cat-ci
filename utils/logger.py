"""
 Logger module
 -------------

 It creates the logger object to create log files.
"""
import logging
import sys


def getLogger(name):
    """
    Getting a logger object, to create logging.
    @param name : Name of the logger object
    @type name : str
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    SH = logging.StreamHandler(sys.stdout)
    SH.setLevel(logging.INFO)
    FORMATTER = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    SH.setFormatter(FORMATTER)
    logger.addHandler(SH)
    return logger
