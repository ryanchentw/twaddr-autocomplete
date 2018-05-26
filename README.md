# 台灣地址工具
[![Build Status](https://travis-ci.org/ryanchentw/twaddr-autocomplete.svg?branch=master)](https://travis-ci.org/ryanchentw/twaddr-autocomplete)

```Python
>>> from twaddr.autocomplete import get_autocomplete_handler
>>> ac = get_autocomplete_handler()
>>> ac.query(u'市政北')
[u'市政北一路', u'市政北二路', u'市政北三路', u'市政北五路', u'市政北六路', u'市政北七路']
```

## Strong influence from
- [ronnywang/taiwan-address-lookup](https://github.com/ronnywang/taiwan-address-lookup)
- [https://github.com/moskytw/zipcodetw](https://github.com/moskytw/zipcodetw)


## Data source
- data/roads.txt (6.6 »路街中英對照文字檔 107/02(漢語拼音,zip檔
