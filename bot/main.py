from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection

if __name__ == '__main__':
    api = OandaApi()

    instruments = api.get_account_instruments()
  # [print(x['name']) for x in instruments] 

    summary = api.get_account_summary()
  # print(summary) 


# instrumentCollection.CreateFile(api.get_account_instruments(), "./bot/data")
instrumentCollection.LoadInstruments("./bot/data")
run_collection(instrumentCollection, api) 

# run_ma_sim()
# instrumentCollection.PrintInstruments()

# run_ma_sim(curr_list=["EUR", "USD", "GBP", "JPY", "AUD", "CAD"])

    # print(api.fetch_candles("EUR_USD", granularity="D", price="MB"))
