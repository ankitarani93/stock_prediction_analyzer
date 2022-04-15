from flask import Flask , request, render_template
from stock_functions import print_database, findstockname, get_stock_symbols, find_stock_price
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

stock_symbol='TCS.NS'
data = find_stock_price(stock_symbol)
df = pd.DataFrame(data, columns=['Date_time', 'Symbol', 'Price', 'Volume'])
df.to_parquet('df.parquet', compression='None')

# Testing "partition by" concept Optimized way to save and read data
table = pa.Table.from_pandas(df)
pq.write_to_dataset(
                table,
                root_path='output.parquet',
                partition_cols=['Symbol','Price'],
            )
