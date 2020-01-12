TRADE = "TRADE"
OFFTR = "OFFTR"
UNKNOWN = "UNKNOWN"
tradeRequiredTagFields = ['legTradeIds', 'receivedTime', 'selectTime']
offtrRequiredTagFields = ['receivedTime', 'selectTime']


def get_line_type(line_str):
    """
    Get whether or not the line is for a TRADE or OFFTR
    :param line_str:
    :return: string
    """
    if TRADE in line_str:
        return TRADE

    if OFFTR in line_str:
        return OFFTR

    return UNKNOWN


with open('trades.txt', 'r') as tradesFile:
    for line in tradesFile:
        line_type = get_line_type(line)
        if line_type == TRADE:
            if not all(ele in line for ele in tradeRequiredTagFields):
                print(f'NOT all trade required tagfields found in {line}')
        if line_type == OFFTR:
            if not all(ele in line for ele in offtrRequiredTagFields):
                print(f'NOT all offtr required tagfields found in {line}')
