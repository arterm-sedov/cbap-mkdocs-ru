---
title: 'Ввод имени переменной'
kbId: 2484
url: 'https://kb.comindware.ru/article.php?id=2484'
updated: '2023-08-23 11:38:01'
---

# Ввод имени переменной

## Инструкции

1. Введите фигурные скобки `{ }` в пустое выражение (после [префиксов](https://kb.comindware.ru/article.php?id=2477)).
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

## Связанные статьи

**[Ввод предиката](https://kb.comindware.ru/article.php?id=2479)**

**[Ввод префикса](https://kb.comindware.ru/article.php?id=2477)**

**[Редактор выражений](https://kb.comindware.ru/article.php?id=2463)**

**[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=408)**