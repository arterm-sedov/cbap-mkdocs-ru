---
title: 'Периодические напоминания об открытых задачах. Настройка процессов, сценария и HTML-текста письма'
kbId: 2318
url: 'https://kb.comindware.ru/article.php?id=2318'
updated: '2024-08-01 18:02:51'
---

# Периодические напоминания об открытых задачах. Настройка процессов, сценария и HTML-текста письма

**{{ productName }}** поддерживает в базовой конфигурации отправку системных уведомлений пользователю по поставленной задаче или процессного уведомления с информацией из бизнес-процесса.

Иногда возникает необходимость настроить напоминания сотруднику об его открытых задачах, например, ежедневно в определенное время.

Для данной настройки создайте 2 бизнес-процесса:

- Поиск сотрудников для отправки напоминания;
- Отправка ежедневного напоминания.

Первый процесс будет запускаться по таймеру ежедневно, например, в 7:00 и искать сотрудников, у которых есть открытые задачи в этот момент времени, и по каждому запускать параллельно в цикле подпроцесс «*Отправка ежедневного напоминания*», который в свою очередь будет формировать и отправлять перечень открытых задач сотрудника на эл. почту в виде таблицы.

**Настройка процесса «Отправка ежедневного напоминания»**

**1.** Создайте новый шаблон процесса «Отправка ежедневного напоминания».

_![Создание шаблона процесса](https://kb.comindware.ru/assets/timenotif6.jpg)_

**2.** В связанном с процессом шаблоне записи создайте атрибуты:

- ***Сотрудник*** (Sotrudnik) — атрибут с типом данных «Аккаунт», кому будет отправляться напоминание;
- ***Тело письма*** (body) — атрибут с типом данных «Текст» и форматом отображения «HTML-текст» с таблицей задач. Проставьте галочку «Вычислять по выражению». В поле «Вычисляемое выражение» укажите N3 и вставьте следующее:

```
 

@prefix cmw: <http://comindware.com/logics#>.

@prefix string: <http://www.w3.org/2000/10/swap/string#>.

@prefix cmwstring: <http://comindware.com/logics/string#>.

@prefix object: <http://comindware.com/ontology/object#>.

@prefix configuration: <http://comindware.com/ontology/configuration#>.

@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.

 

{

           ?confid a configuration:Configuration.

           ?confid configuration:baseUri ?baseUri.

           ("Poiskisotrudnikovdlyaotpravkinapominaniya" "Sotrudnik") object:findProperty ?Sotrudnik.

 

           ?item ?Sotrudnik ?SotrudnikVal.

                      

    #First table

    ("<p style='font-size: 100%' >Перечень задач на исполнение</p>" "<table border='1' style='width: 60%; border-collapse: collapse; border: 1px solid black' ><tbody> <tr><td style='padding: 2px; width: 200px; border: 1px solid black'>Задача</td> <td style='width: 200px; padding: 2px; border: 1px solid black'>Срок</td></tr>") string:concatenation ?firstHeaderRow.

 

    from {

                       ?tasks a cmw:UserTask.

                       or {?tasks cmw:assignee ?SotrudnikVal.}

                       or {?tasks cmw:possibleAssignee ?SotrudnikVal.}.

                       ?tasks cmw:taskStatus taskStatus:inProgress.

                       ?tasks cmw:title ?title.

                       ?tasks cmw:id ?id.

        ("{0}" ?title) string:format ?titleVal.

        ("{0}" ?id) string:format ?idVal.

                      

                       or {?tasks cmw:dueDate ?dueDate.}

                       or {"" -> ?dueDate.}.

                      

        ("{0}" ?dueDate) string:format ?dueDateVal.

                      

        ("<tr><td class='A' style='padding: 2px; border: 1px solid black; '><a href='" ?baseUri "#task/" ?idVal "'>" ?titleVal "</a></td><td align='right' style='padding: 2px; border: 1px solid black; text-align: right'>" ?dueDateVal "</td></tr>") string:concatenation ?firstRow.

    } select ?firstRow -> ?firstFactrow.

    (" " ?firstFactrow) cmwstring:join ?firstFact.

    (?firstHeaderRow ?firstFact "</tbody></table> <br/>") string:concatenation ?first.

    ?first  -> ?value.

}
```

- ***Кому*** (to) — атрибут с типом данных «Текст» с адресом эл. почты сотрудника. Проставьте галочку «Вычислять по выражению». В поле «Вычисляемое выражение» укажите «Формула» и вставьте следующее:

```
$Sotrudnik->cmw.account.mbox
```

**3.** Нарисуйте схему процесса по типу:

_![Типовая схема процесса](https://kb.comindware.ru/assets/timenotif7.jpg)_

**4.** Настройте событие-отправку сообщения.

**5.** Опубликуйте процесс.

**Настройка процесса «Поиск сотрудников для отправки напоминания»**

**1.**  Создайте новый шаблон процесса «Поиск сотрудников для отправки напоминания».

_![Создание шаблона процесса](https://kb.comindware.ru/assets/timenotif1.jpg)_

**2.**  В связанном с процессом «Поиск сотрудников для отправки напоминания» шаблоне записи создайте атрибуты:

- ***Сотрудники***  (Sotrudniki) — вычисляемый атрибут с типом данных «Аккаунт». Проставьте галочки «Хранить несколько значений» и «Вычислять по выражению». В поле «Вычисляемое выражение» укажите N3 и вставьте следующее:

```
 

@prefix cmw: <http://comindware.com/logics#>.

@prefix container: <http://comindware.com/ontology/container#>.

@prefix account: <http://comindware.com/ontology/account#>.

@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.

 

{

           ?class cmw:className "Account".

           ?value a ?class.

           ?value account:active true.

           not {?value cmw:isDisabled true.}.

           or {?tasks cmw:assignee ?value.}

           or {?tasks cmw:possibleAssignee ?value.}.

           ?tasks cmw:taskStatus taskStatus:inProgress.

}
```

- ***Отправки напоминания*** (Otpravkinapominaniya) — атрибут с типом данных «Запись», связанный шаблон — «Отправки ежедневного напоминания». Установите взаимную связь с новым атрибутом — Поиск (Poisk). Проставьте галочкe «Хранить несколько значений».

**3.** Нарисуйте схему процесса по типу:

_![Типовая схема процесса](https://kb.comindware.ru/assets/timenotif2.jpg)_

**4.** Настройте стартовое событие-таймер.

_![Настройка таймера](https://kb.comindware.ru/assets/timenotif3.jpg)_

**Примечание :** если нужно, предусмотрите также простое стартовое событие для запуска процесса вручную без необходимости ожидания нового рабочего дня.

**5.** Настройте сценарий на входе в повторно используемый подпроцесс для создания записей, по которым затем будет запущен подпроцесс.

_![Действия сценария на входе](https://kb.comindware.ru/assets/trigger1.jpg)_

**5.1.** Первые два блока являются системными, поэтому начните с добавления действия «Цикл по объектам» и его настройки.

_![Добавление действия «Цикл по объектам»](https://kb.comindware.ru/assets/trigger2.jpg)_

Переменная «*local*» хранит в себе поочередно по одному экземпляру из указанной выборки. Внизу укажите атрибут «Сотрудники», в котором вычисляются сотрудники с активными задачами.

**5.2.**Добавьте действие «Создать запись» и настройте его.

_![Добавление действия «Создать запись»](https://kb.comindware.ru/assets/trigger3.jpg)_

- Целевой шаблон записи — укажите шаблон записи «Отправка ежедневного напоминания»
- Ссылка на новую запись — укажите атрибут «Отправки напоминания», созданный в п.3.
- Операция со значениями — укажите «Добавить».

**5.3.**Добавьте действие «Изменить значения атрибутов» и настройте его.

_![Добавление действия «Изменить значения атрибутов»](https://kb.comindware.ru/assets/trigger4.jpg)_

Нажмите «Создать», выберите атрибут «Сотрудник», укажите «Заменить» в «Операция со значениями» и вставьте формулу $$local в последнем столбце.

**6.** Настройте запуск повторно-используемого подпроцесса.

_![Настройка подпроцесса](https://kb.comindware.ru/assets/trigger5.jpg)_

В «Записи для запуска процесса» укажите атрибут «Отправки напоминания», а в «Шаблоне вызываемого процесса» — «Отправка ежедневного напоминания».

**7.**Опубликуйте процесс и протестируйте.

Перед началом тестирования проверьте работоспособность подключения для отправки почты и правильность настройки исходящего пути передачи данных.

**Примечание :** для корректной работы вычисляемых полей и формулы запуска подпроцесса проверьте точное соответствие системного имени каждого шаблона записи и атрибутов, а также шаблонов процессов.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
