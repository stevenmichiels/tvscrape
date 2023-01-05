# **TvDatafeed**

A simple TradingView historical Data Downloader. Tvdatafeed allows downloading upto 5000 bars on any of the supported timeframe.



## Installation

This module is installed from github repo

```sh
pip install --upgrade --no-cache-dir git+https://github.com/stevenmichiels/tvscrape.git
```



## Usage

Import the packages and initialize with your tradingview username and password.

```python
from tvScrape import TvScrape, Interval

username = 'YourTradingViewUsername'
password = 'YourTradingViewPassword'

tv = TvScrape(username, password)
```

You may use without logging in, but in some cases tradingview may limit the symbols and some symbols might not be available.

To use it without logging in

```python
tv = TvScrape()
```

when using without login, following warning will be shown `you are using nologin method, data you access may be limited`

---

## Getting Data

To download the data use `tv.get_hist` method.

It accepts following arguments and returns pandas dataframe

```python
(symbol: str, exchange: str = 'NSE', interval: Interval = Interval.in_daily, n_bars: int = 10, fut_contract: int | None = None, extended_session: bool = False) -> DataFrame)
```

for example-

```python
# index
nifty_index_data = tv.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.in_1_hour,n_bars=1000)

# futures continuous contract
nifty_futures_data = tv.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.in_1_hour,n_bars=1000,fut_contract=1)

# crudeoil
crudeoil_data = tv.get_hist(symbol='CRUDEOIL',exchange='MCX',interval=Interval.in_1_hour,n_bars=5000,fut_contract=1)

# downloading data for extended market hours
extended_price_data = tv.get_hist(symbol="EICHERMOT",exchange="NSE",interval=Interval.in_1_hour,n_bars=500, extended_session=False)
```

---

## Search Symbol

To find the exact symbols for an instrument you can use `tv.search_symbol` method.

You need to provide search text and optional exchange. This will return a list of macthing instruments and their symbol.

```python
tv.search_symbol('CRUDE','MCX')
```

---



## Supported Time Intervals

Following timeframes intervals are supported-

`Interval.in_1_minute`

`Interval.in_3_minute`

`Interval.in_5_minute`

`Interval.in_15_minute`

`Interval.in_30_minute`

`Interval.in_45_minute`

`Interval.in_1_hour`

`Interval.in_2_hour`

`Interval.in_3_hour`

`Interval.in_4_hour`

`Interval.in_daily`

`Interval.in_weekly`

`Interval.in_monthly`

---

## Read this before creating an issue

Before creating an issue in this library, please follow the following steps.

1. Search the problem you are facing is already asked by someone else. There might be some issues already there, either solved/unsolved related to your problem. Go to [issues](https://github.com/StreamAlpha/tvdatafeed/issues) page, use `is:issue` as filter and search your problem. ![image](https://user-images.githubusercontent.com/59556194/128167319-2654cfa1-f718-4a52-82f8-b0c0d26bf4ef.png)
2. If you feel your problem is not asked by anyone or no issues are related to your problem, then create a new issue.
3. Describe your problem in detail while creating the issue. If you don't have time to detail/describe the problem you are facing, assume that I also won't be having time to respond to your problem.
4. Post a sample code of the problem you are facing. If I copy paste the code directly from issue, I should be able to reproduce the problem you are facing.
5. Before posting the sample code, test your sample code yourself once. Only sample code should be tested, no other addition should be there while you are testing.
6. Have some print() function calls to display the values of some variables related to your problem.
7. Post the results of print() functions also in the issue.
8. Use the insert code feature of github to inset code and print outputs, so that the code is displyed neat. !
9. If you have multiple lines of code, use tripple grave accent ( ``` ) to insert multiple lines of code.

   [Example:](https://docs.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks)

   ![1659809630082](image/README/1659809630082.png)
