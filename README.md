# NSEazy
NSEazy Is A Python Library To Get Publicly Available Data NSE India and NIFTY Indices

##  Installation
```bash
pip install --upgrade nseazy
```
- NSEazy requires [pandas](https://pypi.org/project/pandas/)

---

## <a name="announcements"></a>**&roarr; [Latest Release Information](https://github.com/DrChandrakant/NSEazy/releases) &loarr;**
#### <a name="announcements"></a> &roarr; **[Older Release Information](https://github.com/DrChandrakant/NSEazy/blob/main/README.md)**


---
## <a name="Unoffical NSE India Api"></a> Unoffical NSE (National Stock Exchange) of India API

This repository, `DrChandrakant/NSEazy`, contains a new **NSE (National Stock Exchange)** API that makes fetching financial nse listed companies easier.  It interfaces nicely with **Pandas** DataFrames.  

*More importantly, **the NSEazy API automatically does the extra work that the user previously had to do "manually" with the other API.*** .

The conventional way to import the new API is as follows:

```python
    import nseazy as nse
```

The most common usage is then to call

```python
    nse.help('show_data')
```
where the `help` method and `show_data` function for which the user seeks help.

```python
    data_required = {'Info' : True } # LTP : True By Default
```

```python
    nse.show_data('L&T',data_required)
```
```python
    data_required = {
        'OHLCV' : True,
        'Start' : '10-6-2023', # Error month or date 06 or 6 will be corrected automatically
        'End'   : '19-06-2023' 
    } # OHLCV : False By Default
```

```python
    nse.show_data('TCS',data_required)
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-11-01</th>
      <td>3050.72</td>
      <td>3066.95</td>
      <td>3050.72</td>
      <td>3066.91</td>
      <td>510301237</td>
    </tr>
    <tr>
      <th>2019-11-04</th>
      <td>3078.96</td>
      <td>3085.20</td>
      <td>3074.87</td>
      <td>3078.27</td>
      <td>524848878</td>
    </tr>
    <tr>
      <th>2019-11-05</th>
      <td>3080.80</td>
      <td>3083.95</td>
      <td>3072.15</td>
      <td>3074.62</td>
      <td>585634570</td>
    </tr>
  </tbody>
</table>


Details on how to call the new API can be found below under **[Basic Usage]()**, as well as in the jupyter notebooks in the **[examples]()** folder.

I am very interested to hear from you regarding what you think of the new NSE API `nseazy`, plus any suggestions you may have for improvement.  You can reach me at **DrChandrakant.github@gmail.com**  or, if you prefer, provide feedback or a ask question on our **[issues page.](https://github.com/DrChandrakant/NSEazy/issues/new/choose)**

---
Main Features:
=============

* Getting live quotes for stocks using stock codes.
* Return data in both json and python dict and list formats.
* Getting quotes for all the indices traded in NSE, e.g CNX NIFTY, BANKNIFTY etc.
* Getting list of top losers.
* Getting list of top gainers.
* Helper APIs to check whether a given stock code or index code is correct.
* Getting list of all indices and stocks.
* Cent percent unittest coverage.
