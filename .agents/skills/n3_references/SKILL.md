---
name: n3_references
description: Use when writing or answering about N3/Turtle/RDF/Notation3/Triples in Comindware Platform
---

Use this skill when answering questions about:
- N3 triples (триплеты) — structure, examples, business use cases
- Running/starting processes via API
- Web API methods
- API call configuration

## Key Files to Reference

When writing content about Notation3/N3/Turtle/RDF/Triples use the following sources to extract content and code samples:

### N3 Basics & Triples
- `docs/ru/developer_guide/n3/.references/n3_lecture_transcript_2025.08.21.md` — N3 tutorial with triple explanation (lines 28-90)
- `docs/ru/developer_guide/n3/.references/n3_guide_summary.md` — N3 guide summary (triplet = subject-predicate-object)
- `docs/ru/business_apps/expressions/expression_intro.md` — N3 introduction (lines 35-45)

### N3 Examples (business-oriented)
- `docs/ru/examples/n3_calculate_active_task_accounts.md` — Active tasks & accounts (business: who has open tasks)
- `docs/ru/examples/n3_calculate_active_task_assignee.md` — Task assignee calculation
- `docs/ru/examples/4932-example_n3_account_attributes_compare.md` — Comparing two attributes
- `docs/ru/examples/n3_filter_active_tasks.md` — Filtering active tasks

### Process API & API Calls
- `docs/ru/examples/4927-api_call_config.md` — **Main reference for running process via API**
- `docs/ru/examples/4928-call_platform_api.md` — Calling API with Postman
- `docs/ru/developer_guide/api/api_web.md` — Web API methods (outline, use line numbers)
- `docs/ru/developer_guide/api/api_system_core.md` — System Core API (OntologyService AddStatement/RemoveStatement)

### Process Scenarios
- `docs/ru/business_apps/scenarios/scenario_elements.md` — Scenario actions including "Запустить процесс" (lines 141-145, 393-394)
- `docs/ru/examples/4904-business_approval_process.md` — Full business process example

### Auxiliary reference Files

#### N3 Snippets (attributes)
- `docs/ru/.snippets/attribute_enum_filter_value_n3.md`
- `docs/ru/.snippets/attribute_enum_get_data_localized_n3.md`
- `docs/ru/.snippets/attribute_enum_get_data_n3.md`
- `docs/ru/.snippets/attribute_enum_set_value_n3.md`
- `docs/ru/.snippets/attribute_document_add_file_n3.md`
- `docs/ru/.snippets/attribute_document_get_file_n3.md`
- `docs/ru/.snippets/attribute_enum_compare_value_n3.md`

#### N3 Examples
- `docs/ru/examples/3_attribute_get_value_by_system_name.md`
- `docs/ru/examples/attribute_date_time_value_format.md`
- `docs/ru/examples/attribute_enum_value_calculation.md`
- `docs/ru/examples/attribute_enum_value_filter.md`
- `docs/ru/examples/attribute_text_substring_search.md`
- `docs/ru/examples/autonumerating_records.md`
- `docs/ru/examples/autonumerating_related_records.md`
- `docs/ru/examples/document_clone_scenario_n3.md`
- `docs/ru/examples/n3_collection_get_selected_ids.md`
- `docs/ru/examples/n3_collection_join_filter.md`
- `docs/ru/examples/n3_collection_join_filter_hierarchy.md`
- `docs/ru/examples/n3_collection_join_string.md`
- `docs/ru/examples/n3_collection_select_conditional.md`
- `docs/ru/examples/n3_periodic_task_notifications.md`
- `docs/ru/examples/scenario_verify_data.md`

#### N3 Guide & References
- `docs/ru/developer_guide/n3/n3_guide.md`
- `docs/ru/developer_guide/n3/n3_tutorial.md`
- `docs/ru/developer_guide/n3/n3_examples.md`
- `docs/ru/developer_guide/n3/.references/**`
- `docs/ru/developer_guide/n3/.references/n3_example_collection_last_item.md`
- `docs/ru/developer_guide/n3/.references/n3_presentation_summary_notebook_lm.md`
- `docs/ru/developer_guide/n3/.references/n3_tutorial_plan_angelina_t.md`
- `docs/ru/developer_guide/n3/.references/n3_video_transcript_complete_notebook_lm.md`
- `docs/ru/developer_guide/n3/.references/presentation_converted_from_pdf.md`
- `docs/ru/developer_guide/n3/.references/n3_examples_collection.n3`

#### Connections & Integrations
- `docs/ru/administration/connections_communication_routes/custom_connections/esphere_receive_configure.md`
- `docs/ru/administration/connections_communication_routes/email_connections/scenario_receive_email.md`
- `docs/ru/administration/connections_communication_routes/email_connections/scenario_send_email.md`
- `docs/ru/administration/connections_communication_routes/rest_odata_connections/http_receive_file.md`
- `docs/ru/administration/connections_communication_routes/rest_odata_connections/http_send_file.md`
- `docs/ru/administration/connections_communication_routes/rest_odata_connections/receive_http_example.md`
- `docs/ru/administration/connections_communication_routes/sql_connections/sql_receive_connection.md`
- `docs/ru/administration/connections_communication_routes/sql_connections/sql_send_connection.md`

#### Other References
- `docs/ru/architect/architect_example.md`
- `docs/ru/business_apps/diagrams/process_diagram/process_error_monitor.md`
- `docs/ru/business_apps/expressions/expression_editor/n3_editor/index.md`
- `docs/ru/business_apps/scenarios/scenario_variables.md`
- `docs/ru/business_apps/templates/attributes/attribute_document.md`
- `docs/ru/business_apps/templates/attributes/attribute_enum.md`
- `docs/ru/business_apps/variables.md`
- `docs/ru/tutorials/tutorial_architect/lesson_2.md`
- `docs/ru/tutorials/tutorial_hr/lesson_8.md`

## Core Knowledge

### N3 Triple Structure
```
subject predicate object.
```
- **Subject** — usually `?item` (current record/instance) or a variable
- **Predicate** — property/attribute (`<Status>`, `<Responsible>`)
- **Object** — value or variable

### Example Business Triples
```n3
# Filter by status
?item <Status> "В работе".

# Compare two attributes
?item <Ответственный> ?responsible.
?item <Согласующий> ?responsible.

# Get all groups
?group rdf:type account:Group.
```

## Quick Answers Template

**5 Business Triple Examples:**
1. Filter by status: `?item <Status> "В работе".`
2. Get active tasks: `?tasks a cmw:UserTask. ?tasks cmw:taskStatus taskStatus:inProgress.`
3. Check attribute value: `?item <СвойствоСтатус> "Завершено".`
4. Compare attributes: `?item <Ответственный> ?responsible. ?item <Согласующий> ?responsible.`
5. Find all groups: `?group rdf:type account:Group.`

## Notes
- Triplet uniqueness error: `"Транзакция нарушает уникальность триплета: cmw.account.mbox - email@<hostname>"` (see `log_files_event_examples.md`)
- For detailed Web API methods, read `api_web.md` section by section (file is large, use line numbers)
- N3 queries execute sequentially top-to-bottom per triplet
- Use `?item` as input parameter, `?value` as output parameter
```

**4. Get accounts with active tasks**
```n3
?task a cmw:UserTask.
?task cmw:taskStatus taskStatus:inProgress.
?task cmw:taskAssignee ?account.
```

**5. Get value by system name stored in another template**
```n3
?item <СистемноеИмяАтрибута> ?systemName.
?target <СистемноеИмя> ?systemName.
?target <Значение> ?result.
```

### Full N3 Example: Active Tasks Accounts
```n3
# Input: ?item (current record with Account attribute)
# Output: ?result (count of accounts with active tasks)

?item <Account> ?account.
{
  ?tasks a cmw:UserTask.
  ?tasks cmw:taskAssignee ?account.
  ?tasks cmw:taskStatus taskStatus:inProgress.
}
=> {
  ?item <Result> ?result.
}.
```

## Notes
- Triplet uniqueness error: `"Транзакция нарушает уникальность триплета: cmw.account.mbox - email@<hostname>"` (see `log_files_event_examples.md`)
- N3 queries execute sequentially top-to-bottom per triplet
- Use `?item` as input parameter, `?result` as output parameter
- Use `{} => {}` pattern for conditional rules
- Use `<AttributeSystemName>` for direct attribute access
