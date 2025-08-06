---
title: Can&#039;t start a process based on several records
kbId: 1962
---


# Can&#039;t start a process based on several records

In **CMW Platform** you can configure a button to start a process by a record. However, the possibility to select multiple records on the list can be somewhat confusing. It is impossible to start a process based on several records, since conflicts in attributes, actions, rules, etc. will arise.

Thus, one process = one record.

**Solution:**

If you still want to provide users with the ability to select several records to start the process, then you will need to create a button with the script operation that will start a process for each record, or start a related process using several records.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
