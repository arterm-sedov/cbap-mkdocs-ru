---
title: Уведомления о задачах. Изменение стандартного текста
kbId: 4683
---

# Уведомления о задачах. Изменение стандартного текста

В **{{ productName }}** есть системный функционал отправки уведомлений пользователям о назначенных задачах. Данный функционал включается после настройки подключения для отправки эл. почты и включения флага «Включить внешние уведомления» в разделе «Глобальная конфигурация». Системное уведомление о назначении задачи выглядит следующим образом:

_![Пример системного уведомления о новой задаче](https://kb.comindware.ru/assets/2021-12-16_13h12_51.png)_

Формат системного уведомления стандартный и содержит название объекта, название задачи, ссылку на задачу, а также название процесса, в рамках которого создалась данная задача. Тема письма также стандартизирована и содержит название задачи. По нажатию на название задачи или кнопку «Перейти к задаче» пользователь перенаправляется в систему на форму назначенной задачи.

Разберём, откуда берутся составные части системного уведомления о задаче.

- Название объекта — значение в отображаемом атрибуте записи, по которой запущен процесс («Телефония - топология», в нашем примере);
- Название задачи — задаётся в настройках задачи во вкладке «Дополнительные свойства», поле «Заголовок задачи» («Проверить контент по заявке...», в нашем примере);
- Ссылка на задачу — формируется автоматически;
- Крайний срок — задаётся в настройках задачи во вкладке «Дополнительные свойства», поле «Продолжительность выполнения» (в нашем примере отсутствует);
- Название процесса — задаётся в свойствах шаблона процесса.

Если стандартный формат системного уведомления о задаче вас не устраивает, в **{{ productName }}** есть возможность настроить свой формат системного уведомления для отправки дополнительной информации пользователю для каждой задачи.

**Примечание :** для изменения доступны только тема и тело уведомления.

**1.** Создайте новый путь передачи данных для уведомления о задачах.

**2.** Перейдите в настройки задачи. Во вкладке «Данные в сообщении» укажите созданный в п.1 путь передачи данных и настройте передачу данных.

**3.** Опубликуйте диаграмму процесса.

**4.** Протестируйте.

См. также: [Гиперссылка на задачу. Вычисление с помощью N3 и формулы](https://kb.comindware.ru/article.php?id=4879).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
