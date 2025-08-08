---
title: Setting up advanced object search by parameters
kbId: 2076
---


# Setting up advanced object search by parameters

Usually, users select the necessary value from the drop-down attribute with the “Record” data type that shows either the display attribute or the object ID of the specified record template. In some cases, this information is not enough, and then the values ​​of several attributes can be joined to form a complex displayed attribute (see article [Combine Several Values Into a Record Title](https://kb.comindware.ru/article.php?id=2003)).

Besides, you can configure an advanced search for an object by certain parameters. To do that:

**1.** Create a technical record template “*Advanced object search*”.

**2.** Create attributes by which you plan to search for the objects, for example, “*Date from*” and “*Date to*”.

**3.** Create an attribute with the “Record” data type and select the record template from which you plan to initiate the advanced search.

**4.** In the «*Advanced object search*» record template, create a «*Search*» form and bring out the attributes created in step 2.

**5.** In the record template from which you plan to initiate the advanced search, create an “*Advanced search*” button with the “*Create linked record*” operation and select the “*Advanced object search*” record template by the attribute created in step 3.

**6.** On the “*Search*” form, open the attribute created in step 2 and drag out the required attribute that you want to search for and write a “*Filter*” for it. Filter example: *from a in db->Projects where AND(GREATER(a->DueDate,$DateFrom),LESS(a->DueDate,$DateTo))*

**7.** In the initial record template, got to the form and place the “Advanced search” button next to the attribute that you want to search for by the advanced parameters.

**8.** When clicking on the button, a window with the “*Search*” form should pop up, with the attributes for the advanced search and the attribute that you are looking for, with filtered values. Select a required value in it and when you save it, this value will be also saved in the main record.

**Note :** you can use this record template to find objects from different record templates. To do this, you need to create the required number of forms, attributes for the search and create different buttons to select the required search forms.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
