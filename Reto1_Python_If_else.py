import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n>= 1 and n<=100:
        x=n%2
        if x!=0 or (n>=6 and n<=20):
            print("Weird")
        else:
            print ("Not Weird")
