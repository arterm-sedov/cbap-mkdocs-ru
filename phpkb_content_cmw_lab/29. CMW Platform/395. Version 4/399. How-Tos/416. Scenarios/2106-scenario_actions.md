---
title: Scenario Actions
kbId: 2106
---


# Scenario Actions

 **{{ productName }}**scenarios may consist of the following actions. For specific action properties description, see the [Scenario Action Types](#mcetoc_1gj42f3a31).

For information on configuring scenario actions, see [Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109).

## Common Action Properties

All actions have the ***Description*** field on the ***General***tab — an optional comment about the action purpose.

All actions have the following properties on the ***Additional*** tab:

- ***Type** —* the action type.
- ***Context template*** — the action will be executed for this template.
- ***Ignore all errors** —* if this box is checked, the scenario action will continue to run despite any errors: exceptions, invalid data, etc.
- ***Execute Separately from the scenario** —* if this box is checked, the action and all its child actions will be executed asynchronously with the remaining scenario actions.
- ***Clear cache** —* if this box is checked, the data is refreshed before executing the action to avoid using obsolete cached values.

![Common actions properties on the Additional tab](https://kb.cmwlab.com/assets/img_6388a68d3d365.png)

*Common actions properties on the Additional tab*

## Scenario Action Types

### Validate the Expression Result

This action validates a condition in the context template (specified on the ***Additional*** tab). If the condition is not met, an error message is displayed with the specified text.

The ***General*** tab provides the following properties:

- ***Failure message** —*the text that will be displayed to the user if the expression returns `false`.
- ***Expression** —* the condition to validate. The action will be triggered if the expression (***formula***, ***N3**,* or ***DMN***) returns `false`.

_![Validate the Expression Result action general properties](https://kb.cmwlab.com/assets/img_6388a63c2b977.png)_

### Create a Record

This action creates a record in the specified template.

_![Create a Record action general properties](https://kb.cmwlab.com/assets/img_6388a49fbe381.png)_

The **General** tab provides the following properties:

- ***Target record template*** — the record will be created in this template.
- ***New record reference***— a ***Record***attribute of the***context template*** (specified on the ***Additional*** tab) that will contain a link to the created record. You can set this field if the context template is linked with the target template.
- ***Value operation*** ​— available if a new record reference is selected:
  - ***Add** —*adds a created record link to the specified attribute (if the attribute’s ***Store multiple values*** check box is checked).
  - ***Replace***— replaces the existing links in the specified attribute with a created record link.

### Clone a Record

This action duplicates the specified records. The target template must match the context template (specified on the ***Additional*** tab).

_![Clone a Record action properties](https://kb.cmwlab.com/assets/img_6388b07ccf52c.png)_

The **General** tab provides the following properties:

- ***Target record template*** — the duplicate record will be created in this template.
- ***New record reference***— a ***Record***attribute of the***context template*** (specified on the ***Additional*** tab) that will contain a link to the created record. You can set this field if the context template is linked with the target template.
- ***An attribute or expression to find the objects***— a ***Record*** attribute linked to the records being cloned, or an expression (***formula***, ***N3***, or ***DMN***) that returns the ID of the records to clone.
- ***Value operation*** ​— available if a new record reference is selected:
  - ***Add**—*adds a created record link to the specified attribute (if the attribute’s ***Store multiple values*** check box is checked).
  - ***Replace***— replaces the existing links in the specified attribute with a created record link.
- ***Clone with child records*** — check this box to clone the record and the records it references. In this case, the action will only clone the child records referenced by the attributes with the checked ***Delete related records*** checkbox.
  - ***Cloning depth***— the number of child record levels to clone.

### Change the Context

This action changes the scenario execution context to the specified records in the target template. The subsequent actions in the scenario will be executed for these records.

_![Change the Context action properties](https://kb.cmwlab.com/assets/img_6388b6b8c4f8a.png)_

The **General** tab provides the following properties:

- ***Target record******template*** — the scenario execution context will be changed to this template.
- ***An attribute or expression to find the objects***— a ***Record*** attribute or an expression (***formula***, ***N3***, or ***DMN***) that returns the IDs of one or more records to which the context will be changed. If an attribute or expression refers to multiple records, a loop for each of the referred records will be run with the actions nested within the ***Change the context*** action.

### Change Attribute Values

This action changes the specified attribute values in the context template record (listed on the ***Additional*** tab).

_![Change Attribute Values ​​action properties](https://kb.cmwlab.com/assets/img_6388bc8e23d2e.png)_

The **General** tab provides the following properties and buttons.

- ***Attribute***— the context template attribute to be modified (the context template is specified on the ***Additional*** tab).
- ***Value operation***
  - ***Replace***— sets the attribute value specified in the ***Value*** column.
  - ***Delete***— removes all attribute values.
  - ***Add*** dd the value specified in the **Value** column to the attribute (this item is displayed for ***Record**,* ***Account***, ***Role***, ***Organizational unit***, ***Document***, and ***Image*** attributes with the checked ***Store multiple values***​ checkbox).
  - ***Exclude***— removes object references specified in the **Value** column from the attribute (this item is displayed for ***Record**,* ***Account***, ***Role***, ***Organizational unit***, ***Document***, and ***Image*** attributes with the checked ***Store multiple values***​ checkbox). The associated objects themselves will not be deleted.
  - ***Create***— click this button to add an attribute.
  - ***Delete***  — check the boxes for the attributes to be deleted and click this button to delete them.
- ***Value***— specify one or more attribute values ​​using an ***attribute***, ***formula**,* ***N3*** expression, or ***DMN*** table.

### Change Variable Values

This action changes the values in a structured variable set.

_![Change Variable Values ​​action properties](https://kb.cmwlab.com/assets/img_6388c34dbddf4.png)_

The **General** tab provides the following properties:

- ***Variable set*** — the name of the variable set to change. This variable set is a key-value dictionary.
- ***Value operation***
  - ***Add** —*adds the variables and values specified in the variable table to the variable set.
  - ***Replace***— sets the variables and values specified in the variable table to the variable set.
  - ***Exclude***— removes all variables and values ​​from the variable set.
- Variable table
  - ***Variable name*** — a variable to change.
  - ***Value***  — an attribute or expression (***formula***, ***N3***, or ***DMN***) that specifies one or more variable values.
  - ***Create***— click this button to add a variable.
  - ***Delete***  — check the boxes for the variables to be deleted and click this button to delete them.

### Start a Process

This action creates an instance of the specified process template.

_![Start a Process action properties](https://kb.cmwlab.com/assets/img_6389c1276d862.png)_

The **General** tab provides the following properties:

- ***Process template*** — a process template in which a new instance will be created based on the current record of the context template (specified on the ***Additional*** tab). To start the process with a new record, execute the ***Create a record*** action before this action.

### Send a Message

This action sends a message through the specified connection and communication route.

_![Send a Message action properties](https://kb.cmwlab.com/assets/img_6389c316db2fa.png)_

The **General** tab provides the following properties:

- ***Connection** —* the connection used to send the message.
- ***Communication route****—*the communication route used to generate the message.
- ***Message variable name***— a variable that stores message content. This variable must be set using the preceding ***Change variable values*** action. This variable is a key-value dictionary. The specified data path translates the message variable into a message. The resulting message will be sent over the specified connection.
- ***Successful response variable name*** — a variable to store the server response if message sending succeeds.
- ***Error response****variable** **name***— a variable to store the server response if message sending fails.

### Import Data from a File

This action imports the data from the file into the context template (specified on the ***Additional*** tab). Each line of data from the file is imported as a separate entry in the context template.

![Import Data From a File action properties](https://kb.cmwlab.com/assets/img_6389c64d38c26.png)

Import Data from a File action properties

The **General** tab provides the following properties:

- ***Data fil****e*** — load a data file (by selecting the ***Value*** item), specify *an****attribute**,* ***formula**,* ***N3***expression, or ***DMN*** table that returns a document link.
- ***Encoding***— imported file data encoding.
- ***Time zone***— the time zone in which the date and time values are stored in the imported file.
- ***Column****separator*** — imported file data column separator (used for CSV file import): comma, semicolon, period, tab, space.
- ***Ignore parsing errors***— if this box is checked, the data will be imported even if errors occur during data processing.
- ***Update existing records with data from the file*** — check this box to update existing records in the context template with the data from the corresponding rows of the imported file and create the missing records. If this check box is not checked, a new record will be created for each row of the imported file. When this box is checked, the ***Key attribute*** table is displayed.
- ***Key attribute***— this table maps the context template key attribute to the imported file key column:
  - ***Attribute***  — an attribute containing *unique values* ​​by which rows in the imported file will be mapped to the database records.
  - ***Format***  — key column value format.
  - ***Column***— the column number in the imported file corresponding to the key attribute.
- ***Data mapping***— this table maps the context template attributes to the imported file columns:
  - ***Attribute***  — the attribute to import the values from the corresponding column.
  - ***Format***  — imported column value format.
  - ***Column***— imported column number corresponding to the specified attribute.

### Create a Document Using a Template

This action generates a file using an export template and stores the generated file link in a variable.

_![Create a Document Using a Template action properties](https://kb.cmwlab.com/assets/img_638ef501bb9af.png)_

The **General** tab provides the following properties:

- ***Place the document in a variable***
  - ***Variable*** — a variable to store the generated file link.
  - ***Variable value operation***
    - ***Add** —*adds the generated file link to the variable.
    - ***Replace***  — replaces all file links stored in the variable with the generated file link (does not replace the files).
    - ***Remove*** *—* removes all file links from the variable (does not delete the files).
- ***Export template***
  - ***Create****—* create an export template to generate a file.
    - ***Name*** *—*a descriptive export template name.
    - ***System name***— a unique export template name, auto-transliterated from the template name.
    - ***Template file***— load an export template file (by selecting the ***Value*** item), specify a ***Document*** **attribute** that contains an export template file, or enter a ***formula***, ***N3*** expression, or ***DMN***table that returns such an attribute.
    - ***Output file name***— specify an ***attribute***,  ***formula**,* ***N3***  expression, or ***DMN*** table that returns the name for the generated file.
    - ***Export as PDF*** — check this box to generate a PDF file.

![Creating a new export template for the Create a Document Using a Template action](https://kb.cmwlab.com/assets/img_6389db296395a.png)

*Creating a new export template for the Create a Document Using a Template action*

- - ***Select existing****:*
    - ***Select an export template***— specify an export template that will be used to generate a new file.

_![Selecting an existing export template for the Create a Document Using a Template action](https://kb.cmwlab.com/assets/img_6389db63e2cf2.png)_

### Store a Document in a Variable

This action stores file links from the specified attributes or variables in a variable set.

_![Store a Document in a Variable action properties](https://kb.cmwlab.com/assets/img_6389e955bc155.png)_

The **General** tab provides the following properties:

- ***Variable set** —* the variable set name to store the file links. This variable set is a key-value dictionary.
- ***Value operation***
  - ***Add*** — adds the file links specified in the ***Value*** column to the variable set.
  - ***Replace***  — replaces all file links in the variable set with the file links specified in the ***Value*** column (does not replace the files).
  - ***Remove***— removes all variables and file links from the variable set (does not delete the files).
- *Variable table*
  - ***Variable name*** — a variable to store the file links specified in the ***Value*** column.
  - ***Value***  — specify the variable value (a file link) using an ***attribute***,  ***formula****,* ***N3***  expression, *or* ***DMN*** table.
  - ***Create***— click this button to add a variable.
  - ***Delete***  — check the boxes for the variables to be deleted and click this button to delete them.

### Attach a Document to an Attribute

This action stores file links from the specified attributes or variables in the attributes.

_![Attach a Document to an Attribute action properties](https://kb.cmwlab.com/assets/img_6389ebf0925c6.png)_

The **General** tab provides the following properties:

- ***Attribute** —* an attribute to store file links specified in the ***Value*** column.
- ***Value operation***
  - ***Adds***— adds file link to the attribute.
  - ***Replace***  — replaces all file links in the attribute with the file links specified in the ***Value*** column (does not replace the files).
  - ***Create*** — creates new file links in the attribute.
- ***Value** —*  set attribute value (a file link) using an **attribute**,  ***formula****,* ***N3***  expression, *or* ***DMN*** table.
- ***Create***— click this button to add an attribute.
- ***Delete***  — check the boxes for the attributes to be deleted and click this button to delete them.

### Execute on Conditions

This action executes the nested actions on the specified conditions. You can set several conditions. The nested action is executed if the conditional expression returns `true`. If none of the conditions returns `true`, the ***Execute on Conditions*** action and its nested actions are skipped.

_![Execute on Conditions action properties](https://kb.cmwlab.com/assets/img_6389f8c30c118.png)_

The **General** tab provides the following properties and buttons.

- ***Condition name***  — a brief condition description.
- ***Expression***  — a tribute, ***formula****,* ***N3***  exp ion, *or* ***DMN*** table that specifies the nested action execution condition. For each condition, a track is created inside the ***Execute on Conditions*** action for nested actions that are executed if the expression returns `true`.
- ***Create***— click this button to add a condition.
- ***Delete***  — check the boxes for the conditions to be deleted and click this button to delete them.

### Iterate by Numeric Counter

This action executes the nested actions a specified number of times.

_![Iterate by Numeric Counter action properties](https://kb.cmwlab.com/assets/img_63eb66f010005.png)_

The **General** tab provides the following properties:

- ***Variable**—*a counter variable to iterate the loop, similar to the `for` loop counter. The variable value increments from 0 to the value set in the ***Number of Iterations*** field, minus 1.
- ***Number of iterations** —* specify the loop iteration number using a numeric ***value***, ***attribute***, ***formula***, ***N3*** expression*,* *or* ***DMN*** table.

### Iterate by Object Counter

This action executes the nested actions with the objects returned by the specified ***attribute***, ***formula***, ***N3*** expression, or ***DMN*** table. The number of iterations equals the number of returned objects.

_![Iterate by Object Counter action properties](https://kb.cmwlab.com/assets/img_63eb666142ecd.png)_

The **General** tab provides the following properties:

- ***Variable**—*an iterator variable to execute the loop, similar to the `for each` loop iterator. This variable will be assigned the value of the given attribute or expression in the same way.
- ***An attribute or expression to find the objects**—* specify a value an ***attribute***,  ***formula****,* ***N3***  expression, or ***DMN*** table that returns the object references to iterate the loop through*.*

## Related Articles

**[Creating a Scenario](https://kb.comindware.ru/article.php?id=2108)**

**[Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109)**

**[Scenario Definition and List](https://kb.comindware.ru/article.php?id=2110)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
