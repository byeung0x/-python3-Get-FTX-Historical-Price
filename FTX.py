
import requests
import pandas as pd
import time as time
import time

def get_price(market_name,resolution,start_time='',end_time=''):
    if end_time != '':
        url = 'https://ftx.com/api' + f"/markets/{market_name}/candles?resolution={resolution}&end_time={end_time}"
    else:
        url = 'https://ftx.com/api' + f"/markets/{market_name}/candles?resolution={resolution}"

    try:
        r = requests.get(url).json()
        r1 = r['result']
    except:
        print(r)
        raise Exception
    df1 = pd.DataFrame(r1)

    return [df1['time'].min(),df1]



def get_FTX_historical_price(market_name,resolution): #market_name please follow name on FTX website #resolution is in second(s)
    start_time = ''
    end_time = ''

    df_m1 = pd.DataFrame()
    while True:
        try:
            if df_m1.empty == False:
                end_time = return1[0]/1000
            return1 = get_price(market_name,resolution,start_time,end_time)
            if len(return1[1])>1:
                df_m1 = pd.concat([df_m1,return1[1]],ignore_index=True)
            else:
                break


        except Exception as e:
            print("Error",e)
            break

    df_m1.drop_duplicates(subset=['time'],inplace=True)
    df_m1.set_index('time',inplace=True)
    df_m1.sort_index(inplace=True)

    return df_m1

#fixed parameter
market_name = 'CRV/USD'
resolution = 60*60
#variable parameter

print(get_FTX_historical_price(market_name,resolution))