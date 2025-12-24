---
title: Calculating a hyperlink to a record
kbId: 2094
---


# Calculating a hyperlink to a record

In order to calculate a link to a specific record in the system, for example, to be sent in a notification, enter the following expression:

```
FORMAT("<a href=https://cmw.com/#form/oa.2/form.3/{0}>Request</a>",LIST($id))
```

**where:**

***https://cwm.com/#form/oa.1/form.1*** — link to the entry form;

***Request***— the displayed text;

***$id*** — record ID.

The calculated attribute must be in the HTML display format to display the link correctly.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
