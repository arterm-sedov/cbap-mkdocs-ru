---
title: Отображение кнопки при отсутствии запущенных процессов по записи
kbId: 5272
tags:
    - N3
    - выражение на N3
    - кнопки
    - пример
    - процессы
hide: tags
---

# Отображение кнопки при отсутствии запущенных процессов по записи {: #show_button_no_process }

Для того чтобы отобразить кнопку при условии, что по текущей записи не запущен ни один процесс, введите следующее выражение:

```turtle
@prefix task: <http://comindware.com/ontology/task#>.
@prefix process: <http://comindware.com/ontology/process#>.
{
if { ?processObject process:businessObject ?item.}
then {false -> ?value.}
else {true -> ?value.}.
}
```

!!! note "Примечание"

    Данное условие не применимо только к процессам, запущенным по текущей записи (процессам, связанным с текущим шаблоном записи).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
