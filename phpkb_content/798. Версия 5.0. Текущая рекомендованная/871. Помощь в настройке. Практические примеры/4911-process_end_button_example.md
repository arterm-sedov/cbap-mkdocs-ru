---
title: Отмена процесса по кнопке. Настройка шаблонов, процессов и кнопки
kbId: 4911
---

# Отмена процесса по кнопке. Настройка шаблонов, процессов и кнопки

Процессы зачастую имеют несколько вариантов завершения. Например, заявка может быть согласована и не согласована. Бывают также случаи, когда нужно отменить процесс извне, например, если инициатор хочет отозвать договор, который уже был отправлен на согласование. В данном случае будет удобно создать отдельную кнопку, по которой процесс может быть отменен, вне зависимости от того, на каком шаге он находится.

**Сценарий:**Процесс «*Согласование договора*». Инициатор решает, что договор больше неактуален и хочет отменить согласование. 

**Описание:**Реализовывать данную настройку мы будем, основываясь на межпроцессном взаимодействии.

 

**Настройка:**

**1.** В шаблоне записи, связанном с основным процессом «*Согласование договора*», создайте атрибут ***$processid***.

**2.** Перейдите в сценарий на выходе из стартового события на диаграмме процесса «*Согласование договора*» и добавьте действие «Изменить значения атрибутов», где заполните атрибут, созданный в п.1, следующим выражением: ***FORMAT("{0}", LIST($$ProcessObject))***.

**3.** На этой же диаграмме процесса сразу после стартового события поставьте развилку «и». Один поток пойдёт по вашему настроенному процессу, а другой — в промежуточное событие–получение сообщения. В настройках события укажите имя сообщения (должно быть уникальным между отправляющим и получающим событиями), и настройте соответствие атрибутов, если нужно.

_![Настройка основного процесса](https://kb.comindware.ru/assets/cancel101.png)_

**Примечание :** важно, чтобы все выходы из процесса в данном случае были терминаторами, чтобы останавливался весь процесс, а не одна его ветка.
Таким образом, при запуске процесса будут активны оба потока и процесс завершится либо по настроенной логике (например, договор не согласован), либо если в событие–получение сообщения придет сообщение об отмене.

**4.** Создайте технический процесс «*Отмена договора*» с новым шаблоном записи (например, «*Отмены договоров*»). В новом шаблоне создайте необходимые атрибуты: ссылка на шаблон записи, связанный с основным процессом (с обратной связью) и, например, комментарий, который будет заполняться на стартовой форме.

_![Настройка технического процесса](https://kb.comindware.ru/assets/cancel2.png)_

В настройках события–отправки сообщения укажите имя сообщения (как в п.3) и экземпляр процесса по типу: ***$Dogovor-> processid***, где ***$Dogovor*** — ссылка на шаблон записи, связанный с основным процессом, ***processid*** — атрибут, созданный в п.1, хранящий информацию об экземпляре запущенного процесса. Если необходимо, настройте соответствие атрибутов и стартовую форму.

**5.** В шаблоне записи, связанном с основным процессом, создайте новую кнопку «*Отменить договор*»:

- Контекст операции — Запись;
- Операция — Запустить процесс по связанному шаблону;
- Результат выполнения — Обновить данные;
- Шаблон — Отмена договора (атрибут: ссылка на основной шаблон записи).

Если нужно, настройте условие отображения кнопки.

**6.** Вынесите кнопку на область кнопок для таблиц, формы, или на саму форму.

**7.** Протестируйте.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
