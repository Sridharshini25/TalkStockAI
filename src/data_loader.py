import polars as pl


def load_data():
    return pl.read_csv("data/supply_chain_data.csv")