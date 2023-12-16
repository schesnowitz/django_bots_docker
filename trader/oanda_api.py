import pandas as pd
import tpqoa

api = tpqoa.tpqoa("./trader/oanda.cfg")

print(api.get_account_summary())
