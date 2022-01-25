import numpy as np
import pandas as pd
from lib import gsheets

def web_amazon(sheet):
    links = gsheets.read_sheet(sheet, 'celular')
    return links

def web_americanas(sheet):
    links = gsheets.read_sheet(sheet, 'celular')
    return links


