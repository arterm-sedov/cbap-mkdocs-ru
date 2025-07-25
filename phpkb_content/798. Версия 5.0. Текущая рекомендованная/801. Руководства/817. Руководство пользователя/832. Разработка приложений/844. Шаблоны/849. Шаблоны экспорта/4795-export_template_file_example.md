---
title: Пример настройки и использования шаблона экспорта авансового отчёта
kbId: 4795
---

# Пример настройки и использования шаблона экспорта авансового отчёта

## Порядок настройки

1. Создайте три **[шаблона записи][record_templates]**:

   - *Заявки*
   - *Затраты*
   - *Тип затрат*
2. В шаблоне *«Заявки»* создайте атрибуты:

   - *Номер заявки*
     - **Системное имя**: `Nomerzayavki`
     - **Тип данных**: **текст**
   - *Время подачи*
     - **Системное имя**: `Datapodachi`
     - **Тип данных**: **дата и время**
   - *Затраты*
     - **Системное имя**: `Zatraty`
     - **Тип данных**: **запись**
     - **Связанный шаблон**: *Затраты*
     - **Хранить несколько значений**: флажок установлен
   - *Итоговая сумма затрат*
     - **Системное имя**: `Itogovayasummazatrat`
     - **Тип данных**: **число**
3. В шаблоне *«Затраты»* создайте атрибуты:

   - *Тип затрат*
     - **Системное имя**: `Tipzatrat`
     - **Тип данных**: **запись**
     - **Связанный шаблон**: *Тип затрат*
   - *Сумма*
     - **Системное имя**: `Summa`
     - **Тип данных**: **число**
4. В шаблоне *«Тип затрат»* создайте атрибуты:

   - *Название*
     - **Системное имя**: `Nazvanie`
     - **Тип данных**: **текст**
5. Вынесите созданные атрибуты на формы в шаблонах.
6. Создайте несколько наглядных записей:

   - справочник типов затрат;
   - затраты с указанием их типа;
   - заявки с указанием затрат.
7. Создайте файл шаблона экспорта `advance_report.xlsx`, показанный на иллюстрации:

   ![Файл шаблона экспорта «Авансовый отчёт»](https://kb.comindware.ru/assets/export_template_file_example_advance_report.png)

   Файл шаблона экспорта «Авансовый отчёт»
8. Создайте в шаблоне записи «*Заявки*» [шаблон экспорта][export_templates] «*Авансовый отчёт*» с файлом `advance_report.xslx`.
9. Вместе с шаблоном экспорта будет автоматически создана [кнопка экспорта записи][export_template_button_configure] «*Авансовый отчёт*».
10. Вынесите кнопку «*Авансовый отчёт*» на форму шаблона записи «*Заявки*».
11. Откройте любую запись шаблона «*Заявки*».
12. Нажмите кнопку «*Авансовый отчёт*».
13. Браузер скачает файл следующего вида (с именем, заданным в [свойствах шаблона экспорта][export_templates]):

    ![Файл, сформированный по шаблону экспорта](https://kb.comindware.ru/assets/export_template_file_result.png)

    Файл, сформированный по шаблону экспорта

--8<-- "related_topics_heading.md"

**[Настройка шаблона экспорта с использованием C#][export_template_csharp_configure]**

**[Настройка выгрузки нескольких коллекций и изображений][export_template_csharp_collection_download]**

**[Настройка шаблона экспорта][export_templates]**

**[Подготовка файла шаблона экспорта][export_template_file_configure]**

**[Настройка кнопки экспорта][export_template_button_configure]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
