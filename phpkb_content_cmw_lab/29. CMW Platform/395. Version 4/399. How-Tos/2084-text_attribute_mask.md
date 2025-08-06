---
title: Configuring Custom Mask
kbId: 2084
---


# Configuring Custom Mask

## Use Case

In the **CMW Platform**, you can define a regular expression mask for the **Text** attribute display format. When the user enters the attribute value, the mask restricts it to the specified format. You can use the preconfigured **E-mail address** mask or specify a **Custom mask**.

In this article, we will create the *Name* attribute that can consist maximum of 10 Latin letters and the *Phone* attribute restricted to the US phone numbers in international format: *+1 (XXX) XXX-XXXX*.

## Instructions

1. Create the *Name* attribute:
   - **Data type** — **Text**
   - **Display format** — **Custom mask**
   - **Mask regular expression:**`[A-Za-z]{10}`
2. Create the *Phone* attribute:
   - **Data type** — **Text**
   - **Display format** — **Custom mask**
   - **Mask regular expression:** `\+1 \([0-9]{3}\) \([0-9]{3}\)-\([0-9]{4}\)`
     **Tip:** To validate the attribute value (e.g., to make sure the user does not omit phone number digits), configure the validation expression and message on the **Value validation** tab.
3. Place the *Name* and *Phone* attributes on a form.
4. The *Name* field will allow entering up to 10 upper and lower case Latin letters.
5. The *Phone*field will allow entering up to 10 digits. Other phone number elements will be fixed.

_![Name and Phone fields with custom masks](https://kb.cmwlab.com/assets/img_643ec6f918a6d.png)_

## Mask Regular Expression Syntax

| Element | Description |
| --- | --- |
| `[A-Za-z]{10}` | - The `[ ]` square brackets define a character range. - The number in the `{ }` curly brackets defines the preceding token repetition number. - The `[A-Za-z]{10}` token defines a string 10 Latin upper and lower case letters. |
| `\+1` | - The `\` backslash escapes the reserved `+` character. Otherwise, it is interpreted as a regex token. - The `+``1` are fixed characters. They are automatically entered in the field. |
| `\([0-9]{3}\) \([0-9]{3}\)-\([0-9]{4}\)` | - The \ backslash escapes the reserved ( and ) characters. Otherwise, they are interpreted as a regex group token. - The  `[0-9]{3}` token defines a string of 3 Arabic numbers. - The parentheses, hyphen, and space are fixed characters. They are automatically entered in the field. |

**Tip:** You can learn more and experiment with regular expressions at <https://regex101.com/>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
