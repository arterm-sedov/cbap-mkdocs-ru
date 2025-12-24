---
title: Calculating substitution parameters
kbId: 2126
---


# Calculating substitution parameters

**CMW Platform** has a system substitution functionality available by default to system administrators. This functionality allows you to appoint deputies for the period of absence of a certain employee, indicating the delegated roles. Deputies can complete tasks for an absent employee during the replacement period and perform other actions based on the delegated roles. Since the Substitution section is part of the system administration, information about the availability of current substitutions or information about the deputies of a particular employee is not available to end users by default. If you need to show any information about employee substitutions or set up any calculations that take into account substitutions, this article is for you.

In order to be able to connect to the substitution parameters library in the N3 expression, the following prefix must be used:

@prefix substitution: <<http://comindware.com/ontology/substitution>#>.

This prefix stores the following substitution parameters:

- name — substitution’s short description;
- deputies — one or several employees who will be replacing the absentee in the system;
- absentee — a person who needs to be substituted during the substitution period;
- roles — delegated roles;
- startDate — start of the substitution period;
- endDate — end of the substitution period.

In order to get the value of a particular parameter, you need to use the following predicate construction: *substitution:parameter*.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
