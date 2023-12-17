## Search Symbol

```bash
$ fyersh search -h
usage: fyersh search [-h] [search_query]

positional arguments:
  search_query  Maximum number of matches (default=10)

options:
  -h, --help    show this help message and exit

```

Search Symbol is a feature provided by Fyers API Helper which is used to get the exact symbol name for Fyers API based on the search query provided to it.

To use search feature open terminal and use this command

```bash
$ fyersh search
```

Six different options will be presented:

- NSE Currency
- NSE Equity Derivatives
- NSE Capital Market
- BSE Capital Market
- BSE Equity Derivatives
- MCX Commodity

Choose your database code accordingly and enter the search string. The result will have top ten search queries.

Example Usage:
```bash
$ fyersh search

Enter the database code

1: NSE Currency
2: NSE Equity Derivatives
3: NSE Capital Market
4: BSE Capital Market
5: BSE Equity Derivatives
6: MCX Commodity

Enter your choice: 3
Enter your search: nifty

Search Results for: 'nifty'

             String              Symbol
0   KOTAK NIFTY ETF   NSE:KOTAKNIFTY-EQ
1     NIFTY50-INDEX   NSE:NIFTY50-INDEX
2     NIFTYIT-INDEX   NSE:NIFTYIT-INDEX
3  SBI-ETF NIFTY 50    NSE:SETFNIF50-EQ
4    NIFTYPSE-INDEX  NSE:NIFTYPSE-INDEX
5    FINNIFTY-INDEX  NSE:FINNIFTY-INDEX
6    NIFTY100-INDEX  NSE:NIFTY100-INDEX
7    NIFTY200-INDEX  NSE:NIFTY200-INDEX
8    NIFTY500-INDEX  NSE:NIFTY500-INDEX
9    NIFTYMNC-INDEX  NSE:NIFTYMNC-INDEX
```

For specifc amount of search results, enter the number of search results you want as key arguments. Default is 10 search results.

Example:

```bash
$ fyersh search 15

Enter the database code

1: NSE Currency
2: NSE Equity Derivatives
3: NSE Capital Market
4: BSE Capital Market
5: BSE Equity Derivatives
6: MCX Commodity

Enter your choice: 3
Enter your search: nifty

Search Results for: 'nifty'

              String                Symbol
0    KOTAK NIFTY ETF     NSE:KOTAKNIFTY-EQ
1      NIFTY50-INDEX     NSE:NIFTY50-INDEX
2      NIFTYIT-INDEX     NSE:NIFTYIT-INDEX
3   SBI-ETF NIFTY 50      NSE:SETFNIF50-EQ
4     NIFTYPSE-INDEX    NSE:NIFTYPSE-INDEX
5     FINNIFTY-INDEX    NSE:FINNIFTY-INDEX
6     NIFTY100-INDEX    NSE:NIFTY100-INDEX
7     NIFTY200-INDEX    NSE:NIFTY200-INDEX
8     NIFTY500-INDEX    NSE:NIFTY500-INDEX
9     NIFTYMNC-INDEX    NSE:NIFTYMNC-INDEX
10   NIFTYBANK-INDEX   NSE:NIFTYBANK-INDEX
11   NIFTYCPSE-INDEX   NSE:NIFTYCPSE-INDEX
12   NIFTYAUTO-INDEX   NSE:NIFTYAUTO-INDEX
13   NIFTYFMCG-INDEX   NSE:NIFTYFMCG-INDEX
14  NIFTYINFRA-INDEX  NSE:NIFTYINFRA-INDEX
```
