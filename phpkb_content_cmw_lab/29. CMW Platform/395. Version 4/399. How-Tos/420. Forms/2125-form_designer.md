---
title: Form Designer
kbId: 2125
---


# Form Designer

## Opening the Form Designer

Use the form designer to configure the form layout, properties, and [elements](#form-elements).

1. Open the template [form list](https://kb.cmwlab.com/article.php?id=2120).
2. Double-click a form row.
3. The form designer will be displayed.
4. [Configure the form](#mcetoc_1gk35dl3l5).

   ![Form Designer](https://kb.cmwlab.com/assets/form_designer.png)

   Form Designer

## Form Designer Elements

1. Element panel — a palette of [elements](#mcetoc_1gk35dl3l4) to drag onto the form: attributes and visual elements. See [Element Panel Operations](#mcetoc_1gk35dl3l7). Use this panel to:
   - Drag and drop elements on the form layout.
   - Search for elements.
   - Filter element list by element type.
   - Create and edit attributes, buttons, and forms.
2. Form layout sets the form's visual appearance.
3. Properties panel — view and configure the properties of the selected element.
4. Buttons:
   - **Save** — save the form.
   - **Clear** — remove all elements from the form layout.
   - **Clone** — [create a form duplicate](#mcetoc_1gk35dl3lb).
   - **Configure template** — go to the template **Properties** page.
   - **Relations** — view a list of application objects that use the form.

## Form Properties

1. **Display name** — the form name that will be displayed in its header when viewing template records.
2. **System name** — a unique form name, for use scripts, expressions, and scenarios.
3. **Is default** — check this box to display this form by default when viewing template records.
4. **Type**:
   - **Public** — select this type for the form to be viewed using the form selection dropdown next to the form title.
   - **Internal** — select this type for the form to be displayed only if it is embedded in another form or is set as a record form (eg. for process start, record creation, dialogues).

## Form Elements

You can place the following elements on the form.

- **Region** — contains all other form elements. You can drag other elements only onto the area. The form must have at least one region. There can be several areas on a form.
- **Tabs** — arrange form elements on several tabs.
- **Columns** — arrange elements in several columns.
- **Static text** — arbitrary text with HTML formatting.
- **Attribute field** — when you drag an attribute to the form layout, a field associated with the attribute is created. Field properties correspond to the associated attribute type.
- **Embedded form** — you can drag another form onto the form layout to embed it into the current form.
- **Button area** — provided for each form and each area. Buttons can be placed only in the button areas.
- **Button group** — combines buttons into a dropdown.
- **Button Separator** — visually separates buttons within button areas.

## Configuring the Form

1. Drag the required [elements](#mcetoc_1gk35dl3l4) from the elements panel to the form layout.
2. To set the [form properties](#mcetoc_1gk35dl3l3), click an empty layout area and configure the properties using the properties panel.
3. To set the properties of a form element, select it in the layout and configure the properties in the properties panel.
4. Click **Save**.

## Editing the Form Rules

1. Click the selector button next to the form title in the designer.
2. Select **Form Rules** from the dropdown.
3. The rule builder for the form is displayed.
4. Edit the form rules.
5. Click **Save**.

   ![Jump menu to form rules designer](https://kb.cmwlab.com/assets/form_designer_goto_form_rules.png)

   Jump menu to form rules designer

## Element Panel Operations

### Creating an Attribute

1. In the element panel:
   - Hover over the **Attributes** heading to create an attribute in the current template, or…
   - Hover over the template name in the element list to create an attribute in the corresponding template.
2. Click the **Add Attribute** button that appears.
3. The attribute creation window will be displayed.

   ![Creating an attribute using the form designer](https://kb.cmwlab.com/assets/form_designer_create_attribute.png)

   Creating an attribute using the form designer

### Editing an Attribute, Button, or Form

1. Hover the mouse pointer over an attribute, button, or form name in the elements panel.
2. Click **Edit Attribute**, **Edit Button**, or **Edit Form** button that appears.
3. The attribute properties window, the [button designer](https://kb.cmwlab.com/article.php?id=2117), or the [form designer](#mcetoc_1gk35dl3l2) will be displayed.

   ![Editing a form using the form designer](https://kb.cmwlab.com/assets/form_designer_edit_form.png)

   Editing a form using the form designer

### Creating a Button

1. In the element pane, hover over the **Buttons** heading.
2. Click the **Add button** button that appears.
3. The button creation page will be displayed.

   ![Creating a button in the form designer](https://kb.cmwlab.com/assets/form_designer_create_button.png)

   Creating a button in the form designer

## Cloning a Form

1. Click **Clone**.
2. In the form cloning window, enter the form **name** and **system name**.
3. Click **Save**.
4. The new form will be opened in the form designer.

   ![Form cloning](https://kb.cmwlab.com/assets/form_designer_clone_form.png)

   Form cloning

## Related Articles

**[Viewing the Template Form List](https://kb.comindware.ru/article.php?id=2120)**

**`![](https://kb.cmwlab.com/images/marker.png)Creating a Form {Article-ID:2121}`**

 [Back to top](#)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
