---
tags:
  - выражения
  - n3
  - тройки
  - переменные
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Ввод имени переменной

1. Введите фигурные скобки `{  }` в пустое выражение (после [префиксов](prefix_autocomplete.md)).
2. Внутри фигурных скобок введите символ `?`. Этот список также можно вызвать, нажав клавиши ++ctrl+space++ в позиции после символа `?`.
3. Отобразится список доступных переменных.
*![Список доступных переменных](n3_editor_variable_autocomplete.png)*
4. Дважды нажмите имя переменной, например `value`, чтобы вставить его в выражение.
  
```turtle title="Пример: выражение, возвращающее список всех записей из шаблона аккаунта"
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

[Ввод предиката](predicate_autocomplete.md)

[Ввод префикса](predicate_autocomplete.md)

**[Редактор выражений][expression_editor]**

**[Примеры использования языка N3. База знаний Comindware]({{ kbCategoryURLPrefix }}408){:target="_blank"}**
