# -python3-Get-FTX-Historical-Price
Directly get FTX's historical price if you use this endpoint directly. FTX imposes no rate limit or authentication requirement on market data so you could use this easily without register any account.

FTX API Documentation
https://docs.ftx.com/#get-historical-prices

FTX Website
https://ftx.com/trade/BTC-PERP

FTX derivatives premium data(developed by third party)
https://ftxpremiums.com/

Sample output for CRV/USD:
                              startTime      open      high       low     close        volume
time                                                                                         
1.610086e+12  2021-01-08T06:00:00+00:00  0.694475  0.694475  0.694475  0.694475       0.00000
1.610089e+12  2021-01-08T07:00:00+00:00  0.675150  0.703250  0.674375  0.701950       1.40510
1.610093e+12  2021-01-08T08:00:00+00:00  0.701950  0.703900  0.686550  0.693750      45.61700
1.610096e+12  2021-01-08T09:00:00+00:00  0.693750  0.711850  0.677200  0.711850     369.83600
1.610100e+12  2021-01-08T10:00:00+00:00  0.711850  0.727000  0.711650  0.719050    2094.33355
...                                 ...       ...       ...       ...       ...           ...
1.657066e+12  2022-07-06T00:00:00+00:00  0.954700  0.967850  0.933900  0.950300  265992.20520
1.657069e+12  2022-07-06T01:00:00+00:00  0.950300  0.958850  0.927100  0.932650  201268.64765
1.657073e+12  2022-07-06T02:00:00+00:00  0.932650  0.933850  0.915550  0.921400  189375.05680
1.657076e+12  2022-07-06T03:00:00+00:00  0.921400  0.937950  0.918050  0.935450  208473.58430
1.657080e+12  2022-07-06T04:00:00+00:00  0.935450  0.938900  0.931350  0.935200   13893.92745

[13055 rows x 6 columns]
