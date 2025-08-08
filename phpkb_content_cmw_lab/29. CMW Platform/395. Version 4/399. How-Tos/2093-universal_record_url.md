---
title: Universal URL to open any record in the system
kbId: 2093
---


# Universal URL to open any record in the system

When setting up solutions, it may be necessary to calculate a direct URL link to objects with a dynamically affixed object ID, whose belonging to a particular template is not known in advance. Such a problem can arise, for example, when generating notification templates that require one reference to objects from potentially different templates, or when conditionally calculating links in calculated fields.

Standard direct links to records and tasks always contain an indication of the template (and sometimes also the template form) in which the object is stored and putting down the object ID from another template will open a form that does not correspond to this object.

To avoid this, the link must be in the following format:

```
https://<product instance URL>/#Resolver/<ID>
```

where the product instance URL should be replaced with the address of the product instance, and <ID> with the contextual ID of the object you are looking for, for example, using the ***FORMAT*** function.

See also: [Computing a hyperlink to a process instance](https://kb.comindware.ru/article.php?id=1891).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
