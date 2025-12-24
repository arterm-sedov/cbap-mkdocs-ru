---
title: Combine Several Values Into a Record Title
kbId: 2003
---


# Combine Several Values Into a Record Title

## Use Case

You can calculate an attribute value ​​from several values and use it as the record title. This can be useful for more convenient searching, composing user-friendly titles for records, tasks and reference fields, and other purposes.

In this article, we will create the *Case name* attribute to combine three other attribute values and use it as a title for the records and record links.

## Instructions

1. Create a **Text** attribute *Case name*.
2. Check ***Use as record title*** and ***Calculate using an expression*****.**
3. In the ***Calculated value***, enter the [**formula**](#mcetoc_1gtntho192):
   ```
   FORMAT("{0} / {1} / {2}",LIST($CityRef->Name,$Applicant,$StatusRef->Name))
   ```
4. Save the attribute.
5. Create or open a record and fill in the fields for the attributes passed to the `LIST()` function in Step 3.
6. The calculated composite value of the *Case name* attribute should appear in the form header.

_![A form heading showing the calculated attribute value](https://kb.cmwlab.com/assets/img_64341fdbbdd83.png)_

### Formula Syntax

| Element | Description |
| --- | --- |
| `FORMAT(originalString, placeholderArray)` | This function takes a string and array as arguments, replaces the placeholders in the string with the array values, and returns the resulting string. |
| `LIST(argument1, argument2, ... argumentN)` | This function takes several values (e.g., *City name, Applicant's name*, and *Case status*) and returns them as an array. |
| `"{0} / {1} / {2}"` | The string to parse. In addition to placeholders, it may contain arbitrary text, numbers, symbols, etc. |
| `{0}, {1}, ... {N}` | These placeholders are replaced with the array values returned by the `LIST()` function. The placeholders are numbered from 0. |

Note

- When you pass a Date & time or Duration attribute value to the `FORMAT()` function, it ignores the configured attribute display format. For example, any Date & time attribute value is output as *MM/DD/YY HH:MM:SS*.
- You can pass any values to the `LIST()` function, not necessarily attribute references. For example, you could pass the current user's full name as a second argument:
  `LIST($CityName,USER()->fullName,$StatusName)`.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
