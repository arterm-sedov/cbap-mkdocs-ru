---
title: Setting up and using the holiday calendar
kbId: 2103
---


# Setting up and using the holiday calendar

To control the due dates of the tasks assigned to users, **CMW Platform** has a built-in functionality in the task settings that allows you to specify the amount of time, up to seconds, within which the user must complete the task. But there are cases when the due dates must be set taking into account working days and hours.

For this purpose there are ***WORKDAYS()*** and ***WORKHOURS()*** functions, which return a date based on the number of working days or hours since a particular date. However, these functions have a limitation: they only take into account weekends and do not consider national or other holidays. Therefore, in these functions it is possible to additionally specify a list of dates that are non-working. In order not to register all holidays inside the function, we recommend creating a separate reference record template with a calendar of holidays, and refer to it when writing an expression with ***WORKDAYS()*** and ***WORKHOURS()*** functions.

**1.** Create a "*Holiday Calendar*" record template.

**2.** Create an attribute with the "Date and time" data type and name it "*Date*".

**3.** Customize the form and table by placing the newly created attribute.

**4.** Create records. Go to the table, click the "***Create***" button and in the "*Date*" field, select one of the holidays, for example, January 1 of the current year.

**5.** Next, in the same way, create records for all the holidays that are in the current year (for the subsequent years, you will also need to create separate records in this record template).

**6.** Go to the task settings where you want to set the due date with taking into account working days. Click the "***Advanced***" tab, then select the "*Formula*" option in the "***Execution time***" field, then insert the following:

```
WORKHOURS(NOW(),18,DURATION("PT9H"),DURATION("PT9H"),LIST((from a in db->holliday_calendar select a->Date)))
```

**where:**

***holiday\_calendar*** — system name of the record template created in step 1;

***Date***— the system name of the attribute created in step 2.

This formula is deciphered as follows: starting from the current moment (when the process created the task), count 18 working hours (the duration of the task), considering that the working day starts at 9 am and lasts 9 hours, and taking into account all the exceptions indicated in the holiday calendar.

**Note:** if you add a weekend (Saturday or Sunday) to the holiday calendar, then when calculating the expression, it will be considered as a working day.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
