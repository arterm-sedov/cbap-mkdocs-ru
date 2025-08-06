---
title: Table stopped working (error «Object reference not set to an instance of an object»)
kbId: 2016
---


# Table stopped working (error «Object reference not set to an instance of an object»)

If a table that used to work stopped working for a user or several users: the table does not open and the error message «Object reference not set to an instance of an object» is displayed, then most likely there is a conflict between the personal configuration of the table and the system configuration of the table. Perhaps some changes were made to the system settings of the table, for example, an attribute was removed that was filtered in the personal configuration of the table.

**Solution**

This problem can only be fixed by deleting the personal configuration of the table where the error occurred. The appearance of the table for the end user will thus be returned to the default settings.

1. Go to the API area by typing «***/docs***» after the domain name of the site.
2. Select «***System Core Api***» from the list.
3. Select «***Ontology***» and then «***GetReferences***». Enter the table ID in the query field and click «***Try it out!***». Thus, you’ll get a list of all personal configurations of the specified table.
4. Then you need to find the personal configuration of the table created by the user who encountered the error. Select «***Ontology***» and then «***GetAxioms***». In the query field, enter the table's personal configuration ID and click «***Try it out!***». Thus, you’ll get information on the specified personal configuration of the table.
5. Once you have determined the personal configuration of the table you want to remove, select «***Ontology***» and then «***Remove***». In the query field, enter the table's personal configuration ID and click «***Try it out!***».

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
