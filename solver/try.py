import pandas as pd
import pyfpgrowth

patterns = pyfpgrowth.find_frequent_patterns(transactions, 2)
patterns