#! /usr/bin/env python3


FNAME = "./key_leak.log"

import pandas as pd
import numpy as np

def main():
    with open(FNAME, "r") as fd:
        n_one = 0
        n_zero = 0
        c = 0
        for line in fd:
            idx, realbit, one, zero = line.split(",")
            if int(idx) == 1:
                n_one += int(one)
                n_zero += int(zero)
                c += 1
        print("none", n_one / c)
        print("nzero", n_zero / c)





if __name__ == "__main__":
    main()
