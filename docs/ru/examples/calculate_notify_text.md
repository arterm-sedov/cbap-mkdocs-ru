---
title: Вычисление текста сообщения в стиле системного уведомления о задаче
kbId: 4971
tags:
    - FORMAT
    - HTML
    - LIST
    - системные уведомления
    - уведомления
    - формулы
hide: tags
---

# Вычисление текста сообщения в стиле системного уведомления о задаче {: #calculate_notify_text }

Здесь приведён пример формулы, которая формирует HTML-текст сообщения в стиле системного уведомления о задаче.

Такой текст можно использовать, например, чтобы отправить пользователю уведомление с кратким описанием заявки и ссылкой для перехода к записи.

## Синтаксис формулы {: #calculate_notify_text_formula }

Чтобы сформировать текст сообщения, используйте следующую формулу:

``` cs
FORMAT(
    CONCAT(LIST(
        '<p>&nbsp;</p>',
        '<table border="0" width="100%" cellspacing="0" cellpadding="40" align="center" bgcolor="#eeeeee">',
            '<tbody>',
                '<tr>',
                    '<td align="center" valign="top">',
                        '<table border="0" width="600" cellspacing="0" cellpadding="40">',
                            '<tbody>',
                                '<tr>',
                                    '<td valign="top" bgcolor="#ffffff">',
                                        '<table border="0" cellspacing="0" cellpadding="6">',
                                            '<tbody>',
                                                '<tr>',
                                                    '<td valign="top" bgcolor="#ffffff">',
                                                        '<span style="font-size: 11pt; color: #000000; font-family: sans-serif;">',
                                                            '<strong>Ваша заявка на перевод организации {0} принята в работу</strong>',
                                                        '</span>',
                                                        '<br />',
                                                        '<span style="font-size: 9pt; color: #666f76; font-family: sans-serif;">',
                                                            '<strong>Процесс: </strong>',
                                                        '</span>',
                                                        'Согласование заявки на перевод организации',
                                                    '</td>',
                                                '</tr>',
                                            '</tbody>',
                                        '</table>',
                                        '<br /><br />',
                                        '<table style="line-height: 14pt; margin-top: 0pt;" border="0" cellspacing="0" cellpadding="6">',
                                            '<tbody>',
                                                '<tr>',
                                                    '<td align="center" bgcolor="#2590d4">&nbsp;</td>',
                                                    '<td align="center" bgcolor="#2590d4">',
                                                        '<a style="text-decoration: none;" href="{1}">',
                                                            '<span style="color: #ffffff; font-family: sans-serif; font-size: 11pt;">',
                                                                '<strong>Перейти к заявке</strong>',
                                                            '</span>',
                                                        '</a>',
                                                    '</td>',
                                                    '<td align="center" bgcolor="#2590d4">&nbsp;</td>',
                                                '</tr>',
                                            '</tbody>',
                                        '</table>',
                                    '</td>',
                                '</tr>',
                            '</tbody>',
                        '</table>',
                        '<table style="border-collapse: collapse; line-height: 13px;" border="0" width="620" cellspacing="0" cellpadding="10">',
                            '<tbody>',
                                '<tr></tr>',
                            '</tbody>',
                        '</table>',
                    '</td>',
                '</tr>',
            '</tbody>',
        '</table>'
    )),
    LIST($id, $link))
```

**Здесь**

| Значение | Описание |
| -------- | -------- |
| `Ваша заявка на перевод организации {0} принята в работу` | Текст заголовка уведомления. Замените его своим текстом. |
| `Согласование заявки на перевод организации` | Название процесса или другой поясняющий текст в теле уведомления. |
| `Перейти к заявке` | Текст кнопки-ссылки. |
| `{0}` | Заполнитель, в который будет подставлено первое значение из `LIST()`. В данном примере это ID заявки. |
| `{1}` | Заполнитель, в который будет подставлено второе значение из `LIST()`. В данном примере это ссылка на заявку. |
| `$id` | Атрибут или системная переменная с ID заявки. |
| `$link` | Атрибут или системная переменная со ссылкой на заявку. |

## Как работает формула {: #calculate_notify_text_formula_logic }

- `FORMAT()` подставляет значения из `LIST()` в заполнители `{0}` и `{1}` внутри HTML-текста.
- `CONCAT()` объединяет фрагменты HTML-разметки в одну строку, чтобы формулу было удобнее читать и редактировать.
- `LIST($id, $link)` передаёт в формулу значения, которые должны быть подставлены в сообщение.
- HTML-разметка задаёт внешний вид уведомления: заголовок, описание процесса и кнопку-ссылку.

!!! tip "Совет"

    Перед использованием формулы проверьте, что значение `$link` содержит корректную ссылку на запись или задачу. Иначе кнопка в уведомлении будет отображаться, но переход по ней не сработает.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Уведомления о задачах. Настройка текста и отправки эл.&nbsp;почтой][task_notifications]
- [Язык формул][formula_guide]
- [Список функций языка формул **{{ productName }}**][formula_function_list]
- [Атрибут типа «Текст»][attribute_text]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
