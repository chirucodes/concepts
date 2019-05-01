# Place any standard lib imports below
from collections import defaultdict

# All exchanges open at 09:30:00 and close at 16:30:00 everyday
ex_open_time = "09:30:00"
ex_close_time = "16:30:00"

def GetMaxPrice(date_data, symbol, exchange_id):
    """
    To get the max price details
    :param date_data: each day's data
    :param symbol: each symbol
    :param exchange_id: exchange id
    :return: max_price for a given symbol and exchange_id
    """
    if len(date_data) > 0:
        max_price = "0"
        for each_rec in date_data:
            if isNowInTimePeriod(nowTime=each_rec['time']):
                if each_rec['symbol'] == symbol and each_rec['exchangeid'] == exchange_id and max_price < each_rec['price']:
                    max_price = each_rec['price']
        return max_price

    else:
        return None

def GetLowPrice(date_data, symbol, exchange_id, maxprice):
    """
    To get the lowest price per day for a given sumbol and exchange price
    :param date_data: each day's data
    :param symbol: each symbol
    :param exchange_id: exchange id
    :param maxprice: max price of the day
    :return: low price
    """
    if len(date_data) > 0:
        low_price = maxprice
        for each_rec in date_data:
            if isNowInTimePeriod(nowTime=each_rec['time']):
                if each_rec['symbol'] == symbol and each_rec['exchangeid'] == exchange_id and low_price > each_rec['price']:
                    low_price = each_rec['price']
        return low_price

    else:
        return None

def GetQuoteWithSmallestExchangeId(input_dict={}):
    """
    To get the quote details which has smallest exchange id
    :param input_dict: given data
    :return: symbol and exchange ids dict
    """
    symbol_exchange_id = defaultdict(dict)
    for each_rec in input_dict:
        if isNowInTimePeriod(nowTime=each_rec['time']):
            if each_rec['symbol'] in symbol_exchange_id.keys():
                if each_rec['exchangeid'] < symbol_exchange_id[each_rec['symbol']]['exchangeid']:
                    symbol_exchange_id[each_rec['symbol']]['exchangeid'] = each_rec['exchangeid']
                    symbol_exchange_id[each_rec['symbol']]['time'] = each_rec['time']
                    # each_rec['exchangeid'] = symbol_exchange_id['symbol']
                else:
                    pass
            else:
                symbol_exchange_id[each_rec['symbol']]['exchangeid'] = each_rec['exchangeid']
                symbol_exchange_id[each_rec['symbol']]['time'] = each_rec['time']
    return symbol_exchange_id

def GetQuotePriceOrder(input_dict={}, each_symbol="", child={}):
    """
    To prepare the Guotes in price order for a given symbol and exchange id
    :param input_dict: records of a day
    :param each_symbol: symbol
    :param child: each symbol's exchange id and time
    :return: prices
    """
    initial_time = ex_close_time
    prices = defaultdict(dict)
    flag = 0

    for each_rec in input_dict:
        if each_symbol == each_rec['symbol'] and child['exchangeid'] == each_rec['exchangeid']:
            # po[each_rec['symbol']]['open'] = each_rec['price']
            if flag == 0:
                initial_time = each_rec['time']
                prices[each_rec['symbol']]['open'] = each_rec['price']
                flag = 1
            if each_rec['time'] < initial_time:
                initial_time = each_rec['time']
                prices[each_rec['symbol']]['open'] = each_rec['price']
    return prices

def GetQuoteLastPriceBeforeExchangeClose(input_dict={}, each_symbol="", child={}):
    """
    To get the last price befor the exchange closes
    :param input_dict:
    :param each_symbol:
    :param child:
    :return:
    """
    initial_time = ex_open_time
    prices = defaultdict(dict)
    for each_rec in input_dict:
        if each_symbol == each_rec['symbol'] and child['exchangeid'] == each_rec['exchangeid']:
            if isNowInTimePeriod(nowTime=each_rec['time']):
                if each_rec['time'] > initial_time:
                    initial_time = each_rec['time']
                    prices[each_rec['symbol']]['last'] = each_rec['price']
    return prices

def isNowInTimePeriod(nowTime, startTime=ex_open_time, endTime=ex_close_time):
    """
    To validate if the given date is a valid date
    :param nowTime: time given
    :param startTime: exchange open date
    :param endTime: exchange close date
    :return: Nothing
    """
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime

def GetMaxTime(times=[]):
    """
    To return the max time.
    :param times: times given for a day
    :return: Nothing
    """
    if len(times) > 0:
        max_time = ex_open_time
        for each_time in times:
            if isNowInTimePeriod(nowTime=each_time['time']):
                if each_time['time'] > max_time:
                    max_time = each_time['time']
        return max_time
    else:
        return None

def PrintLastQuoteTime(input_dict = {}):
    """
    To print the first line as Last Quote Time = and the below lines.
    :param input_dict:Given input in dict format
    :return: nothing
    """
    for each_day in sorted(input_dict.keys()):
        max_time_found = GetMaxTime(input_dict[each_day])
        if max_time_found is not None:
            print "Last Quote Time = %s %s"%(each_day, max_time_found)
            symbol_with_least_exchange_id = GetQuoteWithSmallestExchangeId(input_dict=input_dict[each_day])
            for each_symbol, child in sorted(symbol_with_least_exchange_id.items()):
                prices = GetQuotePriceOrder(input_dict=input_dict[each_day], each_symbol=each_symbol, child=child)
                max_price = GetMaxPrice(date_data=input_dict[each_day], symbol=each_symbol, exchange_id=child['exchangeid'])
                low_price = GetLowPrice(date_data=input_dict[each_day], symbol=each_symbol, exchange_id=child['exchangeid'],maxprice=max_price)

                last_price = GetQuoteLastPriceBeforeExchangeClose(input_dict=input_dict[each_day], each_symbol=each_symbol, child=child)

                print "%s %s,%s,%s,%s,%s,%s,%s"%(each_day, child['time'], each_symbol, child['exchangeid'], prices[each_symbol]['open'], max_price, low_price, last_price[each_symbol]['last'])

def PrepareDict(data):
    """
    #Converting Comma (,) separeated values into a dict type to handle the input data easily.
    :param data: Given input
    :return: Converted dict
    """
    input_dict = defaultdict(dict)
    for each_row in data.split('\n'):
        if each_row != "":
            splitted = each_row.split(',')
            if splitted[0].split(' ')[0] not in input_dict.keys():
                input_dict[splitted[0].split(' ')[0]] = []
            input_dict[splitted[0].split(' ')[0]].append({'time':splitted[0].split(' ')[1], 'symbol':splitted[1], 'exchangeid': splitted[2], 'price': splitted[3]})
    return input_dict

# Fill out the function definition below
def process_feed():
    n = int(input())  # Get number of rows
    row = ""
    for i in range(n):
        row += "\n"
        row += raw_input()  # Get row

    dict_data = PrepareDict(data=row)
    print "_____________OUTPUT_____________"
    PrintLastQuoteTime(input_dict=dict_data)
    return

if __name__ == '__main__':
    process_feed()

