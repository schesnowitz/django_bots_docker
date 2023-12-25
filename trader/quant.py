
# region imports
from AlgorithmImports import *
# endregion

class BuyAndHold(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 1, 1)
        self.SetEndDate(2020, 1, 1)

        self.SetCash(10000)

        self.AddEquity("AAPL", Resolution.Daily)
        self.AddEquity("MSFT", Resolution.Daily)
        # self.AddEquity("BND", Resolution.Minute)
        # self.AddEquity("AAPL", Resolution.Minute)

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested:
            self.SetHoldings("AAPL", 0.5)
            self.SetHoldings("MSFT", 0.5)
            # self.SetHoldings("BND", 0.33)
            # self.SetHoldings("AAPL", 0.33)














# sell at fixed price
# region imports
from AlgorithmImports import *
# endregion

class SellAtPrice(QCAlgorithm):

    def Initialize(self):

        self.SetCash(10000)

        self.SetStartDate(2010, 1, 1)
        self.SetEndDate(2020, 1, 1)

        self.apple = self.AddEquity("AAPL", Resolution.Daily)

        self.limit_price = 50
        self.invest = True


    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("AAPL", 1)

        closing_price = self.Portfolio["AAPL"].Price

        if closing_price > self.limit_price and self.Portfolio.Invested: 
            self.Liquidate("AAPL")
            self.invest = False



# sell after time
            
# region imports
from AlgorithmImports import *
# endregion

class SellAfterTime(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 1, 1)
        self.SetEndDate(2021, 1, 1)

        self.SetCash(10000)

        self.AddEquity("SPY", Resolution.Daily)
        self.invest = True

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("SPY", 1)
            self.invested_time = self.Time
        self.Log(self.Time - self.invested_time)
        time_diff = (self.Time - self.invested_time).days

        if time_diff > 1000:
            self.Liquidate('SPY')
            self.invest = False            



# sell based on profit 
# region imports
from AlgorithmImports import *
# endregion

class SellOnProfit(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2010, 1, 1)
        self.SetEndDate(2015, 1, 1)

        self.SetCash(10000)

        self.AddEquity("AAPL", Resolution.Daily)
        self.invest = True

        self.limit_profit_percent = 1

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("AAPL", 1)
                        
        profit_percent = self.Portfolio["AAPL"].UnrealizedProfitPercent 
        # self.Log(profit_percent)
        if profit_percent >= 1:
            self.Liquidate("AAPL")
            self.invest = False




# trigger limit based on a percentage
        if self.sell_ticket == None:
            self.sell_ticket = self.StopMarketOrder(self.ba.Symbol, -10, self.Securities["BA"].Open*0.60)            





# region imports
from AlgorithmImports import *
# endregion

class SellOnProfit(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2019, 1, 1)
        # self.SetEndDate(2015, 1, 1)

        self.SetCash(100000)

        self.spy =  self.AddEquity("SPY", Resolution.Daily)
        self.invest = True

        self.sell_ticket = None

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.invest:
            close = self.Securities["SPY"].Close
            # 1 % drop stop triggered
            stop_price = close * 0.99
            # limit is 1 % above close
            limit_price = close * 1.01

            self.StopMarketOrder(self.spy.Symbol, 100, stop_price, limit_price)









      Alert(Digits)
      double signal_price = 1.08000;
      int take_profit_pips = 40;
      int stop_loss_pip = 20;
      
      //if(Bid > signal_price)
      //   {
      //      Alert("Price is bidding above at" + Bid);
      //      stop_out = Bid - stop_loss_pip
      //   }
      //else if(Bid < signal_price)
      //   {
      //      Alert("Price is below at" + Ask);
      //   }
      
  }
//+------------------------------------------------------------------+


//double GetPipValue()
//{
//   if(_Digits >= 4)
//   {
//      return 0.0001;
//   }
//      if(_Digits == 3)
//   {
//      return 0.01;
//   }
//}















     double calculate_take_profit(bool is_long, double entry_price, int pips)
      {  
         double take_profit_amount;
         
         if (is_long)
         {
            take_profit_amount = entry_price + pips * GetPipValue();
         }
         else
         {
            take_profit_amount = entry_price - pips * GetPipValue();
         }
         return take_profit_amount;
      }   


      double calculate_stop_loss(bool is_long, double entry_price, int pips)
      {  
         double stop_loss_amount;
         
         if (is_long)
         {
            stop_loss_amount = entry_price - pips * GetPipValue();
         }
         else
         {
            stop_loss_amount = entry_price + pips * GetPipValue();
         }
         return stop_loss_amount;
      }   
      







      
      //Long Position
      if(Ask < signal_price)
     {
         
         double stop_loss = calculate_stop_loss(true, Ask, stop_loss_pips);
         double take_profit = calculate_take_profit(true, Ask ,profit_pips);
         Alert("Entry Price at: " + Ask);
         Alert("Stop at: " + stop_loss);
         Alert("TP: " + take_profit); 
         Alert("Buy triggered");
     }   
     //Short Position
      else if(Ask > signal_price)
     {
     
         double stop_loss = calculate_stop_loss(false, Bid, stop_loss_pips);
         double take_profit = calculate_take_profit(false, Bid ,profit_pips);
         Alert("Entry Price at: " + Bid);
         Alert("Stop at: " + stop_loss);
         Alert("TP: " + take_profit); 
         Alert("Sell triggered");
     }   
  }
  
  
      for(int i=0; i < 6; i++)
      {
        //---
        //---
        //---Alert(Time[]Open[i]High[i]Low[i]Close[i]Volume[i]);
        Alert("Time: " + Time[i] + " Open: " + Open[i]+ " High: " + High[i]+ " Low: " + Low[i]+ " Close: " + Close[i] );
        
         
         
      }
      
      for(int i=0; i < Bars; i++)
      {
        //---
        //---
        //---Alert(Time[]Open[i]High[i]Low[i]Close[i]Volume[i]);
        Alert("Time: " + Time[i] + " Open: " + Open[i]+ " High: " + High[i]+ " Low: " + Low[i]+ " Close: " + Close[i] );
        
         
         
      }
      