---
title: Working with Date &amp; time attribute
kbId: 2005
---


# Working with Date &amp; time attribute

The attribute with the «Date & time» data type is used in **CMW Platform** to record and display data in date and time format.

The attribute with the «Date & time» data type is stored in the database in the «UTC 0» time zone:

```
"op.117": "2020-12-10T07:45:00Z"
```

On the form or on the table, it is displayed in the server time zone, which is specified in the global configuration:

_![Defining the time zone](https://kb.cmwlab.com/assets/2022-02-10_14h05_00.png)_

When **importing** an attribute of the «Date & time» data type, it is loaded into the database in «UTC 0» time zone, but displayed in the time zone specified in the global configuration.

For example, the server time zone is UTC+3, so if you upload from a file to the system with the following date and time: *03.12.2020 17:00*, in the system in the attribute of the «Date & time» data type you will see the same time, but in the database it will be stored as follows: *03.12.2020 14:00*.

When **exporting** an attribute of the «Date & time» data type, it is unloaded in the server time zone specified in the global configuration.

For example, if you export the attribute of the «Date & time» data type with the value «*12/03/2020 17:00*» to Excel, then this field will store exactly the same time as in the system.

When **changing the display format** of the attribute of the «Date & time» data type from «*dd.MM.YYYY hh: mm*» to the display format «*dd.MM.YYYY*», hours and minutes are reset to the zero time zone to avoid incorrect time display and display errors when importing and exporting.

**Note :** the IANA library is used to determine the time zones in which to store information in the database.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
