---
title: 'Выгрузка выбранных записей и столбцов из таблицы с помощью C#'
kbId: 5008
tags: 
    - скрипт
    - C#
    - кнопка
    - экспорт таблицы
    - сишарп
hide: tags
---

# Выгрузка выбранных записей и столбцов из таблицы с помощью C\# {: #example_csharp_table_download_selection }

## Введение {: #example_csharp_table_download_selection_intro }

Здесь представлен пример скрипта для скачивания выбранных столбцов и строк из таблицы в виде файла Excel.

Скрипт запускается по нажатию кнопки.

Приведённый пример скрипта поддерживает экспорт столбцов следующих типов:

- **Логический**
- **Число**
- **Длительность**
- **Текст**
- **Запись**
- **Дата и время**
- **Аккаунт**

## Прикладная задача {: #example_csharp_table_download_selection_use_case }

Имеется шаблон _«Заявки»_.

Требуется экспортировать из таблицы в шаблоне _«Заявки»_ строки и столбцы, выбранные пользователем.

Данные должны выгружаться в файл формата `.XLSX` по нажатию кнопки.

Пользователь выбирает столбцы и строки для экспорта следующим образом:

- устанавливает флажки выбора в требуемых строках;
- скрывает ненужные столбцы с помощью меню «**Мои настройки**» <i class="fa-light fa-edit"></i> — «**Настроить внешний вид**» <i class="fa-light fa-table"></i>.

## Настройка скрипта {: #example_csharp_table_download_selection_script_configure .pageBreakBefore }

!!! warning "Логика работы скрипта"

    Представленный здесь скрипт работает следующим образом:

    1. Получает список видимых и выбранных пользователем строк (записей) в таблице.
    2. Получает список видимых столбцов на основе настроенного пользователем представления таблицы.
    3. Создаёт пустой файл Excel с помощью библиотеки `Aspose.Cells`.
    4. Заполняет файл данными из выбранных строк и столбцов.
    5. Форматирует ячейки в Excel в соответствии с типом экспортируемых данных (текст, числа, даты и т.&nbsp;д.)
    6. Формирует таблицу на листе для более наглядного отображения и фильтрации данных.
    7. Возвращает сформированный файл пользователю для скачивания.
    8. Обрабатывает возможные ошибки (отсутствие выбранных записей, сбои при экспорте).

1. В шаблоне _«Заявки»_ создайте кнопку со следующими свойствами:

    - **Отображаемое название:** _Экспортировать в Excel_
    - **Контекст операции: запись**
    - **Операция: C#-скрипт**
    - **Результат выполнения: скачать документ**

2. Сохраните кнопку.
3. На вкладке «**Скрипт**» введите следующий код:
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

    ``` cs title="Скрипт для выгрузки выбранных ячеек из таблицы"
    // Импорт базовых типов и функций .NET Framework для работы с основными типами данных.
    using System;
    // Импорт расширений LINQ для работы с коллекциями и выполнения запросов.
    using System.Linq;
    // Импорт классов для обработки нажатий кнопок и возврата результатов выполнения скрипта.
    using Comindware.TeamNetwork.Api.Data.UserCommands;
    // Импорт основных классов для работы с данными в {{ pdroductName }}.
    using Comindware.TeamNetwork.Api.Data;
    // Импорт классов для работы с формами.
    using Comindware.TeamNetwork.Api.Data.Forms;
    // Импорт классов для работы с потоками данных, файлами и операциями ввода-вывода.
    using System.IO;
    // Импорт библиотеки Aspose.Cells для создания и форматирования документов Excel.
    using Aspose.Cells;
    // Импорт дополнительных классов Aspose.Cells для работы с таблицами и их стилями в Excel.
    using Aspose.Cells.Tables;
    using System.Collections.Generic;

    class Script
    {
        // userCommandContext содержит данные контекста при нажатии кнопки.
        public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
        {
            // Получаем ID выбранных записей (строк) в таблице при нажатии кнопки.
            var selectedTableRows = userCommandContext.ObjectIds as string[];
            if(selectedTableRows.Count() > 0)
            {
                try
                {
                    // Получаем ID экспортируемой таблицы.
                    var tableToExportId = userCommandContext.Query.DatasetId;
                    // Получаем параметры разбиения таблицы на страницы.
                    var paging = userCommandContext.Query.Paging;
                    // Получаем параметры сортировки данных в таблице.
                    var sorting = userCommandContext.Query.Sorting;
                    // Получаем параметры фильтрации данных в таблице.
                    var filter = userCommandContext.Query.Filter;
                    // Получаем ID шаблона, к которому относится таблица, по ID первой из записей.
                    var templateId = Api.Base.OntologyService.GetAxioms(selectedTableRows.First())["cmw.container"].First().ToString();
                    // Получаем все таблицы шаблона для дальнейшей обработки.
                    var templateTables = Api.TeamNetwork.DatasetService.GetQueries(templateId);

                    // Создаём пустой набор экспортируемых данных.
                    Dataset datasetToExport;
                    // Создаём пустой файл Excel для экспорта данных.
                    Workbook excelWorkbook = new Workbook();
                    // Получаем первый лист книги Excel для заполнения данными.
                    Worksheet excelSheet = excelWorkbook.Worksheets[0];

                    // Создаём стили для форматирования ячеек Excel.
                    var style = excelWorkbook.CreateStyle();
                    // Разрешаем числовые типы для форматирования ячеек.
                    var flag = new StyleFlag();
                    flag.NumberFormat = true;
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для выгрузки выбранных ячеек из таблицы — продолжение"
    {% else %}

    {% endif %}
                    // Перебираем все таблицы шаблона для поиска экспортируемой таблицы по её ID.
                    foreach(var table in templateTables)
                    {
                        // Применяем  к таблице параметры разбиения на страницы, сортировки и фильтрации.
                        table.Paging = paging;
                        table.Sorting = sorting;
                        table.Filter = filter;
                        // Проверяем, требуется ли экспортировать таблицу.
                        if(table.DatasetId == tableToExportId)
                        {
                            // Получаем настроенную пользователем конфигурацию таблицы.
                            var personalTable = Api.TeamNetwork.DatasetConfigurationService.GetPersonalDataset(table.DatasetId);
                            // Получаем данные строки и столбцы таблицы, без учёта выбора пользователя.
                            datasetToExport = Api.TeamNetwork.DatasetService.QueryData(table);
                            // Создаем массив контейнеров для хранения выбранных пользователем столбцов таблицы.
                            var selectedTableColumns = new columnContainer[personalTable.Columns.Count()];
                            // Инициализируем счётчик столбцов.
                            var i=0;
                            // Перебираем все столбцы настроенной пользователем таблицы.
                            foreach(var coll in personalTable.Columns)
                            {
                                // Проверяем, что столбец не скрыт пользователем.
                                if(!coll.IsHidden)
                                {
                                    // Создаём контейнер с данными столбца.
                                    selectedTableColumns[i] = new columnContainer(coll.DataSourceInfo.Id, i);
                                    // Записываем название столбца в заголовок Excel.
                                    excelSheet.Cells[0,i].PutValue(coll.Name);
                                    // Получаем путь к свойству столбца для определения его типа.
                                    var attribute = coll.DataSourceInfo.PropertyPath.Last().ToString();

                                    // Проверяем, что атрибут в столбце не является системным.
                                    if(attribute != "id" && attribute != "lastWriteDate" && attribute != "creationDate" && attribute != "В архиве" && attribute != "creator" && attribute != "processes" && attribute != "isDisabled")
                                    {
                                        // Получаем свойства атрибута для определения его типа.
                                        var attributeProperties = Api.Base.OntologyService.GetAxioms(attribute);
                                        // Получаем тип атрибута.
                                        attribute = attributeProperties["cmw.propertyType"].Last().ToString();
                                    }
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для выгрузки выбранных ячеек из таблицы — продолжение"
    {% else %}

    {% endif %}
                                    // Форматируем ячейки в соответствии с типом данных.
                                    switch(attribute)
                                    {
                                        case "xsd.decimal":
                                        {
                                            // Устанавливаем числовой формат (код 1) для десятичных чисел.
                                            style.Number = 1;
                                            // Применяем формат к столбцу
                                            excelSheet.Cells.Columns[i].ApplyStyle(style, flag);
                                        }
                                        break;
                                        case "lastWriteDate":
                                            {
                                                // Устанавливаем формат даты (код 22) для столбца даты.
                                                style.Number = 22;
                                                // Применяем формат к столбцу.
                                                excelSheet.Cells.Columns[i].ApplyStyle(style, flag);
                                                // Устанавливаем ширину столбца для отображения даты  и времени.
                                                excelSheet.Cells.Columns[i].Width = 15;
                                            }
                                        break;
                                        case "creationDate":
                                            {
                                                // Устанавливаем формат даты (код 22) для столбца даты создания.
                                                style.Number = 22;
                                                // Применяем формат к столбцу.
                                                excelSheet.Cells.Columns[i].ApplyStyle(style, flag);
                                                // Устанавливаем ширину столбца для отображения даты и времени.
                                                excelSheet.Cells.Columns[i].Width = 15;
                                            }
                                        break;
                                        case "xsd.dateTime":
                                            {
                                                // Устанавливаем формат даты (код 22) для столбца даты и времени.
                                                style.Number = 22;
                                                // Применяем формат к столбцу.
                                                excelSheet.Cells.Columns[i].ApplyStyle(style, flag);
                                                // Устанавливаем ширину столбца для отображения даты и времени.
                                                excelSheet.Cells.Columns[i].Width = 15;
                                            }
                                        break;
                                    }
                                    // Увеличиваем счётчик столбцов.
                                    i++;
                                }
                            }
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для выгрузки выбранных ячеек из таблицы — продолжение"
    {% endif %}
                            // Инициализируем счётчик строк, начиная с 1 (0 — заголовки).
                            var j=1;
                            // Инициализируем счётчик столбцов.
                            var y = 0;
                            // Перебираем все столбцы из набора данных для экспорта.
                            foreach(var datasetColumn in datasetToExport.Columns)
                            {
                                try
                                {
                                    // Получаем идентификатор столбца в данных для экспорта.
                                    var columnId = datasetColumn.DataSourceInfo.Id;
                                    // Находим индекс столбца в массиве выбранных пользователем столбцов.
                                    var selectedColumnIndex = Array.Find(selectedTableColumns, x=> x.dataSourceId == columnId).columnIndex;
                                    // Сохраняем позицию столбца в массиве выбранных пользователем столбцов.
                                    selectedTableColumns[selectedColumnIndex].Position = y;
                                }catch{}
                                // Увеличиваем счётчик позиции.
                                y++;
                            }

                            // Перебираем все строки из набора данных.
                            foreach(var row in datasetToExport.Rows)
                            {
                                // Проверяем, что строка выбрана пользователем для экспорта.
                                if(Array.Find(selectedTableRows, v => v == row.Id) != null)
                                {
                                    // Получаем данные строки.
                                    var rowData = row.Data;
                                    // Перебираем все видимые столбцы.
                                    for(var jj = 0; jj < i; jj++)
                                    {
                                        // Получаем позицию столбца в исходных данных.
                                        var ii = selectedTableColumns[jj].Position;
                                        // Проверяем, что данные в ячейке не пустые.
                                        if(rowData[ii] != null)
                                        {
                                            // Определяем типы данных, для которых требуется преобразование.
                                            if(
                                                // Не ссылка на аккаунт.
                                                rowData[ii].GetType() != typeof(Comindware.TeamNetwork.Api.Data.Forms.AccountReference)
                                                // Не булево значение.
                                                && rowData[ii].GetType() != typeof(System.Boolean)
                                                // Не ссылка на запись.
                                                && rowData[ii].GetType() != typeof(Comindware.TeamNetwork.Api.Data.Forms.InstanceReference)
                                                // Не значение из списка.
                                                && rowData[ii].GetType() != typeof(Comindware.TeamNetwork.Api.Data.Forms.EnumReference)
                                                // Не коллекция ссылок на записи.
                                                && !(rowData[ii] is System.Collections.IList)
                                            )
                                            {
                                            // Для остальных типов данных просто записываем значение в ячейку.
                                                excelSheet.Cells[j,jj].PutValue(rowData[ii]);
                                            }
                                            else if (rowData[ii].GetType() == typeof(Comindware.TeamNetwork.Api.Data.Forms.AccountReference))
                                            {
                                                // Для ссылок на аккаунты записываем в ячейку Ф. И. О аккаунта.
                                                excelSheet.Cells[j,jj].PutValue(((AccountReference)rowData[ii]).Name);
                                            }
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для выгрузки выбранных ячеек из таблицы — продолжение"
    {% endif %}
                                            else if(rowData[ii].GetType() == typeof(System.Boolean))
                                            {
                                                // Логические значения преобразуем в строку.
                                                if((bool)rowData[ii])
                                                {
                                                    excelSheet.Cells[j,jj].PutValue("Истина");
                                                }
                                                else
                                                {
                                                    excelSheet.Cells[j,jj].PutValue("Ложь");
                                                }
                                            }
                                            // Для ссылок на записи записываем имя записи.
                                            else if(rowData[ii].GetType() == typeof(Comindware.TeamNetwork.Api.Data.Forms.InstanceReference))
                                            {
                                                excelSheet.Cells[j,jj].PutValue(((Comindware.TeamNetwork.Api.Data.Forms.InstanceReference)rowData[ii]).Name);
                                            }
                                            // Для значения из списка записываем в ячейку название значения на языке текущего пользователя.
                                            else if(rowData[ii].GetType() == typeof(Comindware.TeamNetwork.Api.Data.Forms.EnumReference))
                                            {
                                                excelSheet.Cells[j,jj].PutValue(((Comindware.TeamNetwork.Api.Data.Forms.EnumReference)rowData[ii]).Name);
                                            }
                                            // Обрабатываем атрибуты с несколькими значениями.
                                            else if (rowData[ii] is System.Collections.IList list)
                                            {
                                                var names = new List<string>();
                                                foreach (var item in list)
                                                {
                                                    if (item is Comindware.TeamNetwork.Api.Data.Forms.InstanceReference instanceRef)
                                                    {
                                                        names.Add(instanceRef.Name);
                                                    }
                                                    else if (item is Comindware.TeamNetwork.Api.Data.Forms.AccountReference accountRef)
                                                    {
                                                        names.Add(accountRef.Name);
                                                    }
                                                    else if (item is Comindware.TeamNetwork.Api.Data.Forms.EnumReference enumRef)
                                                    {
                                                        names.Add(enumRef.Name);
                                                    }
                                                }
                                                excelSheet.Cells[j,jj].PutValue(string.Join(", ", names));
                                            }
                                        }
                                    }
                                    // Увеличиваем счётчик строк после обработки текущей строки.
                                    j++;
                                }
                            }
                            // Формируем таблицу на листе Excel:
                            // - Применяем фильтры к заголовкам столбцов для сортировки и фильтрации данных.
                            // - Применяем чередующуюся заливку строк для наглядности.
                            // - Применяем автоматическое форматирование заголовков.
                            // - Параметры таблицы:
                            //   - начальные строка и столбец (0,0)
                            //   - конечные строка и столбец (j-1,i-1)
                            //   - включить заголовки (true)
                            ListObject listObject = excelSheet.ListObjects[excelSheet.ListObjects.Add(0,0, j-1,i-1, true)];
                        }
                    }

                    // Создаем поток в памяти для сохранения файла Excel.
                    MemoryStream stream = new MemoryStream();
                    // Сохраняем рабочую книгу в поток в формате XLSX.
                    excelWorkbook.Save(stream, SaveFormat.Xlsx);

                    // Формируем результат нажатия кнопки с успешным статусом.
                    var result = new UserCommandResult
                    {
                        Success = true,
                        Commited = true,

                        File=new UserCommandFileResult(){
                            Content = stream.ToArray(),
                            // Задаём имя файла для экспорта.
                            Name = "ExportedTable.xlsx"
                            },
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для выгрузки выбранных ячеек из таблицы — продолжение"
    {% else %}

    {% endif %}
                        Messages = new[]
                        {
                            new UserCommandMessage
                            {
                                Severity = SeverityLevel.Normal,
                                Text = "Экспорт выполнен"
                                }
                        }
                    };
                    return result;

                }
                catch
                {
                    // Формируем результат нажатия кнопки с ошибкой.
                    var result1 = new UserCommandResult
                    {
                        Success = false,
                        Commited = true,
                        Messages = new[]
                        {
                            new UserCommandMessage
                            {
                                Severity = SeverityLevel.Normal,
                                Text = "Не удалось выполнить экспорт"
                                }
                        }
                    };
                    return result1;
                }
            }
            else
            {
                // Формируем результат нажатия кнопки с ошибкой, если не выбрано ни одной записи.
                var result1 = new UserCommandResult
                {
                    Success = false,
                    Commited = true,
                    Messages = new[]
                    {
                        new UserCommandMessage
                        {
                            Severity = SeverityLevel.Normal,
                            Text = "Выберите хотя бы одну строку таблицы для экспорта"
                            }
                    }
                };
                return result1;
            }
        }
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для выгрузки выбранных ячеек из таблицы — продолжение"
    {% else %}

    {% endif %}
        // Вспомогательный класс для хранения информации о столбцах таблицы.
        public class columnContainer
        {
            // Индекс выбранного пользователем столбца.
            public int columnIndex {get;set;}
            // Позиция столбца в исходных данных.
            public int Position {get;set;}
            // Идентификатор источника данных столбца.
            public string dataSourceId {get;set;}

            // Конструктор класса.
            public columnContainer(string id , int index )
            {
                dataSourceId = id; columnIndex = index;
            }
        }
    }
    ```

4. Сохраните кнопку.
5. Поместите кнопку _«Экспортировать в Excel»_ на **область кнопок** таблицы «**Все записи**» шаблона _«Заявки»_.

## Тестирование скрипта {: #example_csharp_table_download_selection_test }

1. Откройте таблицу «**Все записи**» шаблона _«Заявки»_.
2. Откройте меню «**Мои настройки**» <i class="fa-light fa-edit"></i> — «**Настроить внешний вид**» <i class="fa-light fa-table"></i>.
3. Скройте любой из столбцов таблицы и сохраните настройки внешнего вида.
4. Выберите требуемые строки в таблице с помощью флажков в левом столбце.
5. Нажмите кнопку _«Экспортировать в Excel»_.
6. Браузер должен скачать файл формата `.XLSX` с выбранными данными.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
