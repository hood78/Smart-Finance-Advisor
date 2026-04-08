def recommend(risk):
    if risk == "Low":
        return ["Fixed Deposit", "PPF", "Savings Account"]
    elif risk == "Medium":
        return ["Mutual Funds", "SIP", "Index Funds"]
    else:
        return ["Stocks", "Crypto", "ETF"]