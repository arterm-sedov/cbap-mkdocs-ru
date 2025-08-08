---
title: Calculating child records of all levels of the tree structure
kbId: 2104
---


# Calculating child records of all levels of the tree structure

In **CMW Platform** it is possible to create mutual links both between record templates and within a single record template, for example, to build a tree structure (works, departments, etc.). This article is applicable in the case of implementing a tree structure of relationships and provides an example of an expression for obtaining all child records of a record, taking into account all levels the tree structure.

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
    ("Projectworks" "Childrenworks") object:findProperty ?CWprop.
    ("Projectworks " "Allchildrenworks") object:findProperty ?ACWprop.
   
    (
               {?item ?CWprop ?value.}
        {
            ?item ?CWprop ?CW.
            ?CW ?ACWprop ?value.
        }
    )assert:union true
}

```

**where****:**

***Projectworks*** — the system name of the record template, where the tree structure of the relationships is implemented (in this example, it is “Project Works”);

***Childrenworks*** — the system name of an attribute with the "Record" data type, which is located in the specified record template, refers to it, and which stores the relationship for child records;

***Allchildrenworks*** — the system name of an attribute with the "Record" data type, which is located in the specified record template, and in which this calculation occurs (i.e., we reuse the calculated attribute in which this calculation occurs).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
