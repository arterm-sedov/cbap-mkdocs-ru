---
title: Transferring business solutions
kbId: 1971
---


# Transferring business solutions

When building a business solution, it is a good practice to create several instances for different purposes: development instance, test instance, production instance; and then transferring solution settings between instances. Business solution settings can be transferred in 4 ways:

**1.** Transferring a database.

In this case, all the settings of the instance, as well as all the data, will be transferred.

**2.** Pulling business application configuration from Git.

**3.** Transferring all the settings manually.

Manual transfer implies a step-by-step transfer of data and settings between instances manually, that is, a new business application is configured from scratch. It is recommended to use this method with a small amount of data.

**4.** Export / import of a business application configuration (see the article [Exporting and Importing Applications](https://kb.comindware.ru/article.php?id=1973)).

This method is limited to transferring records in business application templates, all the settings and data will be transferred, with the exception of template records. This method is characterized by a fast speed of data transfer.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
