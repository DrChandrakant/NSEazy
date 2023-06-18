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

Details on how to call the new API can be found below under **[Basic Usage]()**, as well as in the jupyter notebooks in the **[examples]()** folder.

I am very interested to hear from you regarding what you think of the new NSE API `nseazy`, plus any suggestions you may have for improvement.  You can reach me at **DrChandrakant.github@gmail.com**  or, if you prefer, provide feedback or a ask question on our **[issues page.](https://github.com/DrChandrakant/NSEazy/issues/new/choose)**

---
