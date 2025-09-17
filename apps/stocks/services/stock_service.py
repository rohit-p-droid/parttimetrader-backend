import yfinance as yf
from nsetools import Nse
from utils.number_formater import format_number
from utils.third_party_apis import twelvedata_api

class StockService:
    @staticmethod
    def get_top_4_indices():
        indices = []
        tickers = {
            "NIFTY 50": "^NSEI",
            "SENSEX": "^BSESN",
            "BANK NIFTY": "^NSEBANK",
            "NASDAQ": "^IXIC"
        }

        for name, symbol in tickers.items():
            ticker = yf.Ticker(symbol)
            data = ticker.history(period="2d")

            if len(data) >= 2:
                current_price = float(data["Close"].iloc[-1])
                previous_price = float(data["Close"].iloc[-2])
                change = current_price - previous_price
                change_pct = (change / previous_price) * 100

                indices.append({
                    "name": name,
                    "price": f"{current_price:,.2f}",        
                    "changed_price": change,     
                    "change_pct": change_pct  
                })

        return indices

    @staticmethod
    def top_gainers_losers():
        nse = Nse()
        result = {"gainers": [], "losers": []}
        gainers = nse.get_top_gainers()
        top_gainers = []
        for g in gainers[:5]:
            ticker = yf.Ticker(f"{g['symbol']}.NS")
            hist = ticker.history(period="2d")
            
            if len(hist) >= 2:
                curr_price = float(hist["Close"].iloc[-1])
                prev_price = float(hist["Close"].iloc[-2])
                top_gainers.append({
                    "symbol": g["symbol"],
                    "ltp": round(curr_price, 2),  # Last traded price
                    "change": round(curr_price - prev_price, 2),
                    "net_price": round(((curr_price - prev_price) / prev_price) * 100, 2)
                })
        result["gainers"] = top_gainers
        
        losers = nse.get_top_losers()
        top_losers = []
        for l in losers[:5]:
            ticker = yf.Ticker(f"{l['symbol']}.NS")
            hist = ticker.history(period="2d")
            
            if len(hist) >= 2:
                curr_price = float(hist["Close"].iloc[-1])
                prev_price = float(hist["Close"].iloc[-2])
                top_losers.append({
                    "symbol": l["symbol"],
                    "ltp": round(curr_price, 2),
                    "change": round(curr_price - prev_price, 2),
                    "net_price": round(((curr_price - prev_price) / prev_price) * 100, 2)
                })
        result["losers"] = top_losers
        return result
    
    @staticmethod
    def get_popular_stocks():
        nse = Nse()
        gainers = nse.get_top_gainers()[:5]

        popular = []
        for g in gainers:
            symbol = g["symbol"]
            name = symbol
            try:
                ticker = yf.Ticker(f"{symbol}.NS")
                info = ticker.info
                if info and isinstance(info, dict):
                    name = info.get("longName") or info.get("shortName") or symbol
                
            except Exception as e:
                print(f"Error fetching info for {symbol}: {e}")
            popular.append({
                "symbol": symbol,
                "name": name
            })

        return popular
    
    @staticmethod
    def search_stocks(request):
        q = request.GET.get("q", "").strip()
        url = "/symbol_search?symbol="+q
        data = twelvedata_api(url)
        return data
    
    @staticmethod
    def get_stock_by_symbol(symbol):
        try:
            ticker = yf.Ticker(f"{symbol}.NS")
            hist = ticker.history(period="2d")
            
            if hist.empty or len(hist) < 2:
                return None

            curr_price = float(hist["Close"].iloc[-1])
            prev_price = float(hist["Close"].iloc[-2])
            change = curr_price - prev_price
            change_percent = (change / prev_price) * 100 if prev_price else 0

            info = ticker.info

            data = {
                "symbol": symbol.upper(),
                "name": info.get("longName", symbol),
                "price": f"{curr_price:,.2f}",
                "change": f"{'+' if change >= 0 else ''}{change:,.2f}",
                "changePercent": f"{'+' if change >= 0 else ''}{change_percent:.2f}%",
                "isPositive": change >= 0,
                "marketCap": format_number(info.get("marketCap")),
                "volume": f"{round(info.get('volume', 0) / 1_000_000, 1)}M" if info.get("volume") else None,
                "sector": info.get("sector", "N/A"),
            }

            return data

        except Exception as e:
            print(e)
            return None

    
        

   














