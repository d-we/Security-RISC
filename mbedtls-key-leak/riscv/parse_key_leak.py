#! /usr/bin/env python3

import sys

#FNAME = f"./measurement_results/log_decrypt{sys.argv[1]}.csv"
#FNAME = "./clean_key_leak_complete.log"
FNAME = "./key_leak.log"

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv(FNAME, names=["idx", "realbit", "one", "zero"])
    df_aggr = pd.DataFrame()
    print("ONE: ", df.groupby("realbit")["one"].median())
    print("ZERO: ", df.groupby("realbit")["zero"].median())

    df_aggr['one-min'] = df.groupby("idx")["one"].min()
    df_aggr['prediction'] = np.where(df_aggr["one-min"] < 80, 1, 0)
    #df_aggr['zero-min'] = df.groupby("idx")["zero"].mean()
    df_aggr['realbit'] = df.groupby("idx")["realbit"].min()
    precision = np.where(df_aggr['realbit'] == df_aggr['prediction'], 1, 0).sum()

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df_aggr)
    print("precision: ", precision)


    fig = go.Figure()
    fig.add_trace(go.Bar(y=df_aggr["realbit"]*1000+5000, name="realbit"))
    fig.add_trace(go.Scatter(y=df_aggr["one-min"],name="pmc",line=dict(color='firebrick', width=4)))
    fig.show()

    # df = pd.read_csv("key_leak.log",names=["idx","realbit","one","zero"])
    # df_aggr = pd.DataFrame()

    # thresh_zero = int(df.groupby("realbit")["zero"].mean().apply(int))
    # thresh_one = int(df.groupby("realbit")["one"].mean().apply(int))

    # print("tz", thresh_zero)
    # print("to", thresh_one)

    # df_aggr["realbit"] = df.groupby("idx")["realbit"].min()
    # df_aggr["one_avg"] = df.groupby("idx")["one"].mean().apply(int)
    # df_aggr["zero_avg"] = df.groupby("idx")["zero"].mean().apply(int)
    # df_aggr["one_min"] = df.groupby("idx")["one"].min()
    # df_aggr["zero_min"] = df.groupby("idx")["zero"].min()

    # df_aggr["avg_key_predict"] = np.where(df_aggr["one_avg"] < thresh_one,1,0)
    # df_aggr["min_key_predict"] = np.where(df_aggr["one_min"] < thresh_zero,1,0)


    # print(df_aggr)




if __name__ == "__main__":
    main()
