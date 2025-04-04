---
title: Ввод имени переменной
kbId: 2484
---

# Ввод имени переменной

## Инструкции

1. Введите фигурные скобки `{ }` в пустое выражение (после [префиксов][n3_editor_prefix_autocomplete]).
2. Внутри фигурных скобок введите символ `?`. Этот список также можно вызвать, нажав клавиши `Ctrl` `Пробел` в позиции после символа `?`.
3. Отобразится список доступных переменных.

_![Список доступных переменных](https://kb.comindware.ru/assets/n3_editor_variable_autocomplete.png)_

4. Дважды нажмите имя переменной, например `value`, чтобы вставить его в выражение.

Пример: выражение, возвращающее список всех записей из шаблона аккаунта

```
@prefix account: <http://comindware.com/ontology/account#>.
@prefix container: <http://comindware.com/ontology/container#>.
{
  # Получаем ID шаблона аккаунта Zakazchiki
  ?user container:alias "Zakazchiki".
  # Получаем список аккаунтов из шаблона Zakazchiki
  ?value account:extendedBy ?user.
}
```

--8<-- "related_topics_heading.md"

**[Ввод предиката][n3_editor_predicate_autocomplete]**

**[Ввод префикса][n3_editor_prefix_autocomplete]**

**[Редактор выражений][expression_editor]**

**[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=408)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
