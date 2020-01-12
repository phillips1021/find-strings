TRADE = "TRADE"
OFFTR = "OFFTR"
UNKNOWN = "UNKNOWN"
trade_required_tagfields = ['legTradeIds', 'receivedTime', 'selectTime']
offtr_required_tagfields = ['receivedTime', 'selectTime']

# --------------Functions------------------------------------


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


def get_trade_files():
    """
    Get list of trade file names
    :return: list of trade file names
    """
    return ['trades.txt', 'trades2.txt']


def validate_line(required_tagfields, trade_line, trade_file_name):
    """
    Check if required_tagfields are all present in the trade_line
    and if all required tagfields are not present write to the log
    :param required_tagfields: list of tagfields that must be present in trade_line
    :param trade_line: line from trade file
    :param trade_file_name: name of file
    :return:
    """
    if not all(ele in trade_line for ele in required_tagfields):
        print(f'NOT all required tagfields found in {line} from {trade_file_name}')


# ----------------------Main Code--------------------------------

trade_file_names = get_trade_files()

for trade_file in trade_file_names:

    with open(trade_file, 'r') as tradesFile:
        for line in tradesFile:
            line_type = get_line_type(line)
            if line_type == TRADE:
                validate_line(trade_required_tagfields, line, trade_file)
                continue
            if line_type == OFFTR:
                validate_line(offtr_required_tagfields, line, trade_file)
                continue
