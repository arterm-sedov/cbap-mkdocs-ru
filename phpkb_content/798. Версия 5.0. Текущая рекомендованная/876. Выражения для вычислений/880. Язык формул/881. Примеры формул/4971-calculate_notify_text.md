---
title: Вычисление текста сообщения в стиле системного уведомления о задаче
kbId: 4971
---

# Вычисление текста сообщения в стиле системного уведомления о задаче

Для того, чтобы передать в тело сообщения текст в формате системного уведомления о задаче, введите следующее выражение:

```
FORMAT(
    '<p>&nbsp;</p><table border="0" width="100%" cellspacing="0" cellpadding="40" align="center" bgcolor="#eeeeee"><tbody><tr><td align="center" valign="top"><table border="0" width="600" cellspacing="0" cellpadding="40"><tbody><tr><td valign="top" bgcolor="#ffffff"><table border="0" cellspacing="0" cellpadding="6"><tbody><tr><td valign="top" bgcolor="#ffffff"><span style="font-size: 11pt; color: #000000; font-family: sans-serif;"><strong>Ваша заявка на перевод организации {0} принята в работу</strong></span><br /><span style="font-size: 9pt; color: #666f76; font-family: sans-serif;"><strong>Процесс: </strong></span>Согласование заявки на перевод организации</td></tr></tbody></table><br /><br /><table style="line-height: 14pt; margin-top: 0pt;" border="0" cellspacing="0" cellpadding="6"><tbody><tr><td align="center" bgcolor="#2590d4">&nbsp;</td><td align="center" bgcolor="#2590d4"><a style="text-decoration: none;" href="{1}"><span style="color: #ffffff; font-family: sans-serif; font-size: 11pt;"><strong>Перейти к заявке</strong></span></a></td><td align="center" bgcolor="#2590d4">&nbsp;</td></tr></tbody></table></td></tr></tbody></table><table style="border-collapse: collapse; line-height: 13px;" border="0" width="620" cellspacing="0" cellpadding="10"><tbody><tr></tr></tbody></table></td></tr></tbody></table>',
    LIST($id,$link))
```

**где:**

Текст и переменные (*Ваша заявка на перевод организации {0} принята в работу...*) замените своими данными;

***LIST*** — перечислите атрибуты для передачи данных в переменные, указанные в тексте (в данном примере это ИД заявки и ссылка на неё).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
