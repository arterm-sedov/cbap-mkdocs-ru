---
title: Calculation of objects that meet the condition
kbId: 2024
---


# Calculation of objects that meet the condition

Task example: in the table on the project form, it is necessary to display only those employees who have the skills necessary for the project. An employee is displayed only if all the requested skills are present.

The project "Space tourism", the necessary skills to work in the project: Astronomy, Foreign languages, Logistics.

Employee #1 has the following skills: Astronomy, Logistics, Programming, Network technologies.

Employee #2 has the following skills: Web design, Astronomy, Foreign languages, Logistics.

Employee #1 does not have all the required skills to participate in the project and does not need to be displayed in the table. And employee #2 has all the necessary skills, so he needs to be displayed.

Data model:

- Record template "Projects" (projects):
  - Attribute "Required skills" (required\_skills), referring to the record template "Skills" (multiple values);
  - Attribute "Employees fit for the project", referring to the record template "Employees" (multiple values).
- Record template "Employees" (employees):
  - Attribute "Employee skills" (available\_skills), referring to the record template "Skills" (multiple values).
- Record template "Skills".

In order to calculate objects that meet the condition specified in the main object (in this case, employees with the necessary skills), enter the following expression:

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix cmw: <http://comindware.com/logics#>.
{
    ("projects" "required_skills") object:findProperty ?PropertyLittle. 
    ("employees" "available_skills") object:findProperty ?PropertyBig.

    ?container object:alias "employees". 
    ?allObjs cmw:container ?container.

    {
        ?item ?PropertyLittle ?resultL.
        ?allObjs ?PropertyBig ?resultL.
    } assert:count ?c.

    {
        ?item ?PropertyLittle ?resultA.
    } assert:count ?d.
    
    if {?c == ?d}
    then {?allObjs -> ?value.}
}

```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
