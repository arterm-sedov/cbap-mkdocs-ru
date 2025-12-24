---
title: Configuring Context-Dependent Filter for Record Attribute
kbId: 2022
---


# Configuring Context-Dependent Filter for Record Attribute

## Use Case

In the **CMW Platform**, a **Record** attribute is used to select values from another record template.

By default, a **Record** field lists all records linked to the attribute. But in some scenarios, you might want to show only certain records.

To limit the record set displayed in the **Record** field, use the **Filter** field in the **Field properties** pane of the form designer.

In this article, we will configure a city selector dropdown to display the cities from the country where an employee plans to travel.

## Prerequisites

In our example, we have a database of countries, cities, and travel requests. When creating a travel request, an employee selects a destination city. Instead of displaying all the cities from all the countries, we will filter the cities list by the selected country of the business trip.

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template display name (system name)** | **Attribute display name (system name)** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Countries (countries)* | *Title (title)* | **Text** | Stores the country name. |
| *Cities of the country (cities\_of\_the\_country)* | **Record** | The  *cities\_of\_the\_country*attribute is linked to the *Cities* template.  The  **Store multiple values** box is checked. |
| *Cities (cities)* | *Title (title)* | **Text** | Stores the city name. |
| *Country (country)* | **Record** | The *country* attribute is linked to the *Countries* template. |
| *Travel requests (travel\_requests)* | *Title (title)* | **Text** | Stores the request name. |
| *Country (request\_country)* | **Record** | The *request\_country* attribute is linked to the *Countries* template. |
| *City (request\_city)* | **Record** | The *request\_citiy*attribute is linked to the *Cities* template. |

## Instructions

1. Open the default form for the *Travel requests* template for editing.
2. Place the following attributes on the form: *Title, Country*, and *City*from the *Travel requests* template.
3. Select the *Cities* field on the form to display its **Field properties** pane.
4. In the **Appearance** property, select **Dropdown**.
5. In the **Filter** property, define the filter using one of the following options:
   - **Attribute** — select the *Countries → Cities of the country*attribute from the dropdown***.***
   - **Formula** — write the following expression in CMW formula language:
     ```

     from a in db->cities where a-> country == $request_country select a->id

     ```
   - **N3** — write the following expression in N3 language:
     ```

     @prefix container: <http://comindware.com/ontology/container#>.
     @prefix object: <http://comindware.com/ontology/object#>.
     @prefix math: <http://www.w3.org/2000/10/swap/math#>.
      
     {
         ("cities" "country") object:findProperty ?citiescountryProp.
         ("travel_requests" "request_country") object:findProperty ?tr_countryProp.
      
         ?item ?tr_countryProp ?tr_country.
         ?value a [object:alias "cities"].
         ?value ?citiescountryProp ?tr_country.
     }

     ```
   - **DMN** — select the *Cities* template as the **Data source** and configure the DMN table as shown below:

     ![DMN filter example](https://kb.cmwlab.com/assets/img_64358119dbc92.png)

     *DMN filter example*
6. Save the form.
7. Create or open a *Travel requests* record.
8. Test the filter:
   - Select the *Country*.
   - Select the *City*.
   - The *City* dropdown should list the cities of the selected country.

**Note:**The user needs sufficient access rights to view the country and city records. If a dropdown does not show any entries, check the access rights in the user's role.

**Tip:**Use the form rules to configure a dynamic field behavior for more convenient data entry. See [Configuring Form Rule Using Formula](https://kb.comindware.ru/article.php?id=1987).

## See Also

[Configuring Filters for Record Attributes](https://kb.comindware.ru/article.php?id=2020)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
