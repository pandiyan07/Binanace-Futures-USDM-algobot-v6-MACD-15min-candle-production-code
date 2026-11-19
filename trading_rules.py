def CONDITION_VERIFIER(df):
    long_HISTOGRAM = 300
    short_HISTOGRAM = 300
    ATR_value = 252
    
    last_atr_value = float(df['atr'].iloc[-1])
    
    last_macd_line_value = float(df['macd_line'].iloc[-1])
    last_signal_line_value = float(df['signal_line'].iloc[-1])
    last_histogram_value = float(df['histogram'].iloc[-1])
    
    atr_rule = last_atr_value > ATR_value
    
    l1 = last_macd_line_value > last_signal_line_value
    l2 = last_histogram_value > long_HISTOGRAM
    #l3 = last_macd_line_value > 0
    
    s1 = last_macd_line_value < last_signal_line_value
    s2 = last_histogram_value < short_HISTOGRAM
    #s3 = last_macd_line_value < 0
    
    long_entry_condition = l1 and l2 and atr_rule
    short_entry_condition = s1 and s2 and atr_rule
    
    return long_entry_condition, short_entry_condition