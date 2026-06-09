---
title: 'Импорт данных из локального CSV-файла'
tags:
    - C#
    - CSV
    - импорт данных
    - интеграция
    - сетевая папка
    - синхронизация данных
    - скрипт
hide: tags
---

# Импорт данных из локального CSV-файла с помощью C#-скрипта {: #import_local_csv_csharp }

## Введение {: #import_local_csv_csharp_intro }

Здесь представлен способ программного импорта данных из CSV-файла, расположенного в локальной или сетевой папке на сервере **{{ productName }}**. C#-скрипт выполняется в задаче технического процесса, читает CSV-файл с диска сервера, разбирает его и создаёт или обновляет записи в шаблонах через API.

Этот метод применяется, когда недоступна интеграция через OData или REST API, но есть возможность разместить CSV-файл в общей сетевой папке, доступной серверу **{{ productName }}**. Например:

- смежная система регулярно выгружает данные в общую папку в виде CSV;
- требуется периодическая синхронизация справочников из внешнего источника;
- файл формируется вручную и сохраняется в сетевую папку для последующего импорта.

!!! tip "Альтернативные способы импорта"

    - Встроенный [импорт данных из файлов XLSX и CSV][import_data] через интерфейс шаблона — для разовых загрузок через веб-интерфейс.
    - [Адаптер импорта данных][adapter_data_import] через очереди сообщений — для автоматического приёма XML/JSON из внешних систем.

## Прикладная задача {: #import_local_csv_csharp_use_case }

Имеется CSV-файл с данными клиентов и их договоров, который регулярно выгружается в сетевую папку `\\server\shared\import\clients_contracts.csv`. Требуется автоматически импортировать эти данные в шаблоны записей **{{ productName }}**: создавать новые записи клиентов и договоров, связывать их между собой и назначать статусы договоров.

## Подготовка шаблонов записей {: #import_local_csv_csharp_templates }

1. Создайте шаблон записи _«Статусы договора»_ со следующими атрибутами:

    | Название              | Тип        | Свойства                                                  |
    | --------------------- | ---------- | --------------------------------------------------------- |
    | _Название_            | **Текст**  | **Использовать как заголовок записей:** флажок установлен |

2. Создайте три записи в шаблоне _«Статусы договора»_: _В обработке_, _В работе_, _Завершён_.

3. Создайте шаблон записи _«Договоры»_ со следующими атрибутами:

    | Название          | Тип               | Свойства |
    | ----------------- | ----------------- | -------- |
    | _Название_        | **Текст**         | **Использовать как заголовок записей:** флажок установлен |
    | _Сумма_           | **Число**         | **Количество знаков после запятой: 2** |
    | _Дата_            | **Дата и время**  | |
    | _Статус_          | **Запись**        | **Связанный шаблон:** _Статусы договора_ |

4. Создайте шаблон записи _«Клиенты»_ со следующими атрибутами:

    | Название              | Тип        | Свойства |
    | --------------------- | ---------- | -------- |
    | _Наименование_        | **Текст**  | **Использовать как заголовок записей:** флажок установлен |
    | _Контактное лицо_     | **Текст**  | |
    | _Телефон_             | **Текст**  | |
    | _Email_               | **Текст**  | |
    | _Договор_             | **Запись** | **Связанный шаблон:** _Договоры_ |

## Подготовка CSV-файла {: #import_local_csv_csharp_csv_prep }

1. Сформируйте CSV-файл со следующими столбцами (в качестве разделителя используется точка с запятой):

    ```
    Наименование клиента;Контактное лицо;Телефон;Email;Наименование договора;Статус;Дата;Сумма договора
    ```

2. Сохраните файл в кодировке **UTF-8** — это исключит проблемы с отображением кириллических символов.

3. Разместите файл в сетевой папке, доступной серверу **{{ productName }}**, например `\\server\shared\import\contracts.csv`.

    !!! warning "Путь к файлу"

        C#-скрипт выполняется на стороне сервера. Указывайте путь, доступный серверу, а не клиентскому компьютеру. Поддерживаются как локальные пути (`C:\import\file.csv`), так и сетевые (UNC) пути (`\\server\share\file.csv`).

4. Убедитесь, что учётная запись, под которой работает сервер приложений **{{ productName }}**, имеет права на чтение файлов в указанной папке.

## Создание процесса импорта {: #import_local_csv_csharp_process }

1. Создайте новый процесс: на странице «**Процессы**» нажмите кнопку «**Создать**».

2. Назовите процесс, например _«Импорт данных из CSV»_.

3. Добавьте элемент «**Задача-скрипт**» на схему процесса и соедините его со стартовым и конечным событиями.

4. Нажмите на задачу-скрипт и в открывшейся панели свойств выберите вкладку «**Скрипт**».

5. Вставьте приведённый ниже C#-скрипт.

6. Опубликуйте процесс.

## C#-скрипт {: #import_local_csv_csharp_script }

``` cs title="Скрипт импорта данных из локального CSV-файла — объявление класса модели и чтение файла"
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using Comindware.Data.Entity;

class Script
{
    // Data model matching the CSV file columns
    public class CsvRow
    {
        public string ClientName   { get; set; }
        public string Contact      { get; set; }
        public string Phone        { get; set; }
        public string Email        { get; set; }
        public string ContractName { get; set; }
        public string StatusName   { get; set; }
        public DateTime Date       { get; set; }
        public decimal Total       { get; set; }
    }

    // Maps a human-readable status name to the record ID in the "Статусы договора" template
    private static string GetStatusId(string statusName)
    {
        // Replace with actual record IDs from your "Статусы договора" template
        switch (statusName.Trim())
        {
            case "В обработке": return "oa.1";
            case "В работе":    return "oa.2";
            case "Завершён":    return "oa.3";
            default:            return "";
        }
    }

    // Parses a single CSV line into a CsvRow object
    private static CsvRow ParseLine(string line, char delimiter)
    {
        var columns = line.Split(delimiter);

        DateTime date;
        DateTime.TryParse(columns[6].Trim(), CultureInfo.InvariantCulture, DateTimeStyles.None, out date);
        date = TimeZoneInfo.ConvertTime(date, TimeZoneInfo.Utc, TimeZoneInfo.Local);

        decimal total = 0;
        Decimal.TryParse(columns[7].Trim(), NumberStyles.Any, CultureInfo.InvariantCulture, out total);

        return new CsvRow
        {
            ClientName   = columns[0].Trim(),
            Contact      = columns[1].Trim(),
            Phone        = columns[2].Trim(),
            Email        = columns[3].Trim(),
            ContractName = columns[4].Trim(),
            StatusName   = columns[5].Trim(),
            Date         = date,
            Total        = total
        };
    }

{% if pdfOutput %}
```

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

``` cs title="Скрипт импорта данных из локального CSV-файла — основная логика импорта"
{% endif %}
    public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
    {
        // Path to the CSV file on the server.
        // Use a UNC path for a shared network folder, e.g.:
        //   @"\\server\shared\import\contracts.csv"
        // Or a local server path:
        //   @"C:\import\contracts.csv"
        string filePath = @"\\server\shared\import\contracts.csv";

        // CSV delimiter (configure according to your file)
        char delimiter = ';';

        // Encoding of the CSV file — UTF-8 is recommended for Cyrillic text
        Encoding fileEncoding = Encoding.UTF8;

        // Read the entire file and parse each non-empty line
        string fileContent;
        using (var reader = new StreamReader(filePath, fileEncoding))
        {
            fileContent = reader.ReadToEnd();
        }

        var rows = new List<CsvRow>();
        foreach (var line in fileContent.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries))
        {
            // Skip the header line by detecting a non-numeric value in the last column
            decimal testTotal;
            var firstColumn = line.Split(delimiter)[7].Trim();
            if (!Decimal.TryParse(firstColumn, NumberStyles.Any, CultureInfo.InvariantCulture, out testTotal))
            {
                continue; // This is the header or a non-data line
            }

            rows.Add(ParseLine(line, delimiter));
        }

{% if pdfOutput %}
```

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

``` cs title="Скрипт импорта данных из локального CSV-файла — создание записей"
{% endif %}
        foreach (var row in rows)
        {
            // Resolve the status ID from the status name in the CSV
            string statusId = GetStatusId(row.StatusName);

            // Create a "Договор" record
            var contractData = new Dictionary<string, object>
            {
                // Use system names of the attributes in the "Договоры" template
                { "Nazvanie", row.ContractName },
                { "Summa",    row.Total.ToString(CultureInfo.InvariantCulture) },
                { "Data",     row.Date },
                { "Status",   statusId }
            };

            // "Contracts" — system name of the "Договоры" template
            string contractId = Api.TeamNetwork.ObjectService.CreateWithAlias("Contracts", contractData);

            // Create a "Клиент" record linked to the newly created "Договор"
            var clientData = new Dictionary<string, object>
            {
                // Use system names of the attributes in the "Клиенты" template
                { "Naimenovanie",    row.ClientName },
                { "KontaktnoeLitso", row.Contact },
                { "Telefon",         row.Phone },
                { "Email",           row.Email },
                { "Dogovor",         contractId }
            };

            // "Clients" — system name of the "Клиенты" template
            Api.TeamNetwork.ObjectService.CreateWithAlias("Clients", clientData);
        }
    }
}
```

**Пояснения к скрипту:**

- **Строки 1–8** — импортируются необходимые пространства имён. `System.IO` требуется для работы с файловой системой, `System.Globalization` — для корректного разбора чисел и дат, `System.Text` — для указания кодировки файла, `Comindware.Data.Entity` — для доступа к API платформы.

- **Класс `CsvRow` (строки 12–23)** — модель данных, описывающая структуру одной строки CSV-файла. Свойства класса соответствуют столбцам файла.

- **Метод `GetStatusId` (строки 26–34)** — сопоставляет человекочитаемое название статуса из CSV с идентификатором записи в шаблоне _«Статусы договора»_. Замените `"oa.1"`, `"oa.2"`, `"oa.3"` на фактические идентификаторы записей из вашего шаблона.

- **Метод `ParseLine` (строки 37–58)** — разбирает строку CSV на объект `CsvRow`: разделяет по указанному разделителю, преобразует дату с учётом часового пояса, преобразует сумму в число.

- **Метод `Main`** — точка входа, вызывается при выполнении задачи-скрипта в процессе.

    - **Переменная `filePath`** — путь к CSV-файлу. Для сетевой папки укажите UNC-путь (например, `\\server\share\file.csv`). Для локальной папки сервера — локальный путь (`C:\import\file.csv`).

    - **Переменная `delimiter`** — символ-разделитель столбцов. По умолчанию `;`.

    - **Переменная `fileEncoding`** — кодировка файла. Рекомендуется `Encoding.UTF8`. При использовании других кодировок (например, `Encoding.GetEncoding("windows-1251")`) замените значение.

    - **Чтение файла (строки 76–80)** — файл читается целиком через `StreamReader` с указанием кодировки.

    - **Разбор строк (строки 82–93)** — содержимое файла разбивается на строки. Строка-заголовок пропускается по условию: последний столбец заголовка не является числом.

    - **Цикл по строкам CSV (строки 100–127)** — для каждой строки данных:
        1. Определяется идентификатор статуса через `GetStatusId`.
        2. Создаётся запись договора через `CreateWithAlias` — в словарь передаются системные имена атрибутов и их значения.
        3. Создаётся запись клиента через `CreateWithAlias` — в атрибут `Dogovor` передаётся идентификатор созданного договора, устанавливая связь между записями.

**Системные имена, которые необходимо заменить на ваши:**

| В скрипте             | Описание                                      |
| --------------------- | --------------------------------------------- |
| `Contracts`           | Системное имя шаблона записи _«Договоры»_     |
| `Clients`             | Системное имя шаблона записи _«Клиенты»_      |
| `Nazvanie`            | Системное имя атрибута _«Название»_ в шаблоне _«Договоры»_ |
| `Summa`               | Системное имя атрибута _«Сумма»_ в шаблоне _«Договоры»_ |
| `Data`                | Системное имя атрибута _«Дата»_ в шаблоне _«Договоры»_ |
| `Status`              | Системное имя атрибута _«Статус»_ в шаблоне _«Договоры»_ |
| `Naimenovanie`        | Системное имя атрибута _«Наименование»_ в шаблоне _«Клиенты»_ |
| `KontaktnoeLitso`     | Системное имя атрибута _«Контактное лицо»_ в шаблоне _«Клиенты»_ |
| `Telefon`             | Системное имя атрибута _«Телефон»_ в шаблоне _«Клиенты»_ |
| `Email`               | Системное имя атрибута _«Email»_ в шаблоне _«Клиенты»_ |
| `Dogovor`             | Системное имя атрибута _«Договор»_ в шаблоне _«Клиенты»_ |

Системные имена шаблонов и атрибутов указаны на вкладке «**Свойства**» соответствующего шаблона или атрибута.

!!! note "Обновление существующих записей"

    В приведённом примере для каждой строки CSV создаются новые записи. Если требуется обновлять существующие записи при повторном импорте, необходимо добавить логику поиска записи по ключевому полю (например, по названию договора) и вызывать `Api.TeamNetwork.ObjectService.EditWithAlias(recordId, data)`, если запись найдена, либо `CreateWithAlias`, если запись отсутствует.

## Тестирование {: #import_local_csv_csharp_test .pageBreakBefore }

1. Убедитесь, что CSV-файл размещён в указанной сетевой папке и доступен для чтения с сервера.

2. Запустите созданный процесс вручную со страницы «**Процессы**»: выберите процесс и нажмите кнопку «**Запустить**».

3. Дождитесь завершения процесса.

4. Перейдите в шаблон _«Клиенты»_, на вкладку «**Свойства**» и нажмите кнопку «**Перейти к экземплярам**» — в списке должны отобразиться записи клиентов с привязанными договорами.

5. Перейдите в шаблон _«Договоры»_ — в списке должны отобразиться записи договоров с указанными статусами.

6. Если импорт не выполнился, проверьте:
    - доступность сетевой папки с сервера **{{ productName }}**;
    - права учётной записи сервера приложений на чтение файла;
    - соответствие системных имён шаблонов и атрибутов в скрипте;
    - кодировку CSV-файла (должна быть UTF-8);
    - корректность идентификаторов статусов в методе `GetStatusId`.

## Автоматизация запуска {: #import_local_csv_csharp_automation }

Для регулярной синхронизации данных процесс импорта можно запускать автоматически:

- **По расписанию** — настройте [подключение для приёма сообщений][process_receiving_connection], которое будет запускать процесс по расписанию.
- **По событию** — настройте сценарий, отслеживающий изменения в сетевой папке, и запускающий процесс импорта при появлении нового файла.
- **По HTTP-запросу** — настройте [подключение для приёма HTTP-запросов][http_receive_example], которое будет запускать процесс импорта по внешнему сигналу (например, после завершения выгрузки данных смежной системой).

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Импорт данных в шаблон][import_data]_
- _[Адаптер импорта данных][adapter_data_import]_
- _[Написание скриптов на языке C#][csharp_guide]_
- _[HTTP-запросы POST. Отправка JSON/XML из сценария с помощью C#][http_send_example_csharp]_
- _[Подключения для приёма сообщений][process_receiving_connection]_
- _[Задача-скрипт][process_diagram_elements_script_task]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
