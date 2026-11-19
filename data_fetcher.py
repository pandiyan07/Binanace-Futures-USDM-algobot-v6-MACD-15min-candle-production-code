from binance.um_futures import UMFutures
import pandas as pd

def REST_API_DATFET():
    # Initialize the Binance USD-M Futures client
    umfut_rest_api_client = UMFutures()

    # Download the last 40 one-minute candles for BTCUSDT
    candles = umfut_rest_api_client.klines("BTCUSDT", "15m", limit=89)

    # Convert the candle data to a DataFrame
    columns = [
        "timestamp", "open", "high", "low", "close", "volume", 
        "close_time", "quote_asset_volume", "number_of_trades", 
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", 
        "ignore"
    ]
    df = pd.DataFrame(candles, columns=columns)
    df = df[[ "open", "high", "low", "close","close_time"]]

    # Convert timestamp columns to a readable datetime format
    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms').dt.strftime('%H:%M:%S')

    return df