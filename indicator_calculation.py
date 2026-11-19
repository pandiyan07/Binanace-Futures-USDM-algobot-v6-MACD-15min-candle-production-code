import pandas_ta as ta

def ATR_CALCULATOR(df,length):
    return ta.atr(df['high'].astype(float), df['low'].astype(float), df['close'].astype(float), length=length)            

def CALCULATE_MACD(df, fa, sl, sig):
    macd_df = ta.macd(df['oc2'], fast=fa, slow=sl, signal=sig)
    macd_df.rename(columns={
        f'MACD_5_34_9': 'macd_line',
        f'MACDs_5_34_9': 'signal_line',
        f'MACDh_5_34_9': 'histogram'
    }, inplace=True)
    df = df.join(macd_df)
    return df

def EMA_CALCULATOR(oc2_df, length):
    return ta.ema(oc2_df, length=length)

def SMA_CALCULATOR(oc2_df, length):
    return ta.sma(oc2_df, length=length)

def INDICATOR_CALCULATOR( df, atr_len, small_ema_len, large_ema_len):
    df['oc2'] = (df['open'].astype(float) + df['close'].astype(float)) / 2
    df['ema_5'] = EMA_CALCULATOR(df['oc2'], small_ema_len)
    df['sma_34'] = SMA_CALCULATOR(df['oc2'], large_ema_len)
    df['atr'] = ATR_CALCULATOR(df, atr_len)
    df = CALCULATE_MACD(df,5,34,9)
    return df