---
title: 'Импорт данных из CSV-файла на сервере'
kbId: 5745
url: 'https://kb.comindware.ru/article.php?id=5745'
updated: '2026-06-16 19:18:36'
---

# Импорт данных из CSV-файла на сервере

## Введение

Здесь представлен способ программного импорта данных из CSV-файла, расположенного в папке на сервере **Comindware Platform**. C#-скрипт выполняется в задаче технического процесса, читает CSV-файл с диска сервера, разбирает его и создаёт или обновляет записи в шаблонах через API.

Этот метод применяется, когда недоступна интеграция через OData или REST API, но есть возможность разместить CSV-файл в общей сетевой папке, доступной серверу **Comindware Platform**. Например:

- смежная система регулярно выгружает данные в общую папку в виде CSV;
- требуется периодическая синхронизация справочников из внешнего источника;
- файл формируется вручную и сохраняется в сетевую папку для последующего импорта.

Альтернативные способы импорта

- Встроенный [импорт данных из файлов XLSX и CSV](https://kb.comindware.ru/article.php?id=5737) через интерфейс шаблона — для разовых загрузок через веб-интерфейс.
- [Адаптер импорта данных](https://kb.comindware.ru/article.php?id=5743) через очереди сообщений — для автоматического приёма XML/JSON из внешних систем.

## Прикладная задача

Имеется CSV-файл с данными клиентов и их договоров, который регулярно выгружается в сетевую папку `\\\\server\\shared\\import\\clients_contracts.csv`. Требуется автоматически импортировать эти данные в шаблоны записей **Comindware Platform**: создавать новые записи клиентов и договоров, связывать их между собой и назначать статусы договоров.

## Подготовка шаблонов записей

1. Создайте шаблон записи *«Статусы договора»* со следующими атрибутами:

   | Название | Тип | Свойства |
   | --- | --- | --- |
   | *Название* | **Текст** | **Использовать как заголовок записей:** флажок установлен |
2. Создайте три записи в шаблоне *«Статусы договора»*: *В обработке*, *В работе*, *Завершён*.
3. Создайте шаблон записи *«Договоры»* со следующими атрибутами:

   | Название | Тип | Свойства |
   | --- | --- | --- |
   | *Название* | **Текст** | **Использовать как заголовок записей:** флажок установлен |
   | *Сумма* | **Число** | **Количество знаков после запятой: 2** |
   | *Дата* | **Дата и время** |  |
   | *Статус* | **Запись** | **Связанный шаблон:** *Статусы договора* |
4. Создайте шаблон записи *«Клиенты»* со следующими атрибутами:

   | Название | Тип | Свойства |
   | --- | --- | --- |
   | *Наименование* | **Текст** | **Использовать как заголовок записей:** флажок установлен |
   | *Контактное лицо* | **Текст** |  |
   | *Телефон* | **Текст** |  |
   | *Email* | **Текст** |  |
   | *Договор* | **Запись** | **Связанный шаблон:** *Договоры* |

## Подготовка CSV-файла

1. Сформируйте CSV-файл со следующими столбцами (в качестве разделителя используется точка с запятой):

   ```
   Наименование клиента;Контактное лицо;Телефон;Email;Наименование договора;Статус;Дата;Сумма договора
   ```
2. Сохраните файл в кодировке **UTF-8** — это исключит проблемы с отображением кириллических символов.
3. Разместите файл в сетевой папке, доступной серверу **Comindware Platform**, например `\\\\server\\shared\\import\\contracts.csv`.

   Путь к файлу

   C#-скрипт выполняется на стороне сервера. Указывайте путь, доступный серверу, а не клиентскому компьютеру. Поддерживаются как локальные пути (`C:\\import\\file.csv`), так и сетевые (UNC) пути (`\\\\server\\share\\file.csv`).
4. Убедитесь, что учётная запись, под которой работает сервер приложений **Comindware Platform**, имеет права на чтение файлов в указанной папке.

## Создание процесса импорта

1. Создайте новый процесс: на странице «**Процессы**» нажмите кнопку «**Создать**».
2. Назовите процесс, например *«Импорт данных из CSV»*.
3. Добавьте элемент «**Задача-скрипт**» на схему процесса и соедините его со стартовым и конечным событиями.
4. Нажмите на задачу-скрипт и в открывшейся панели свойств выберите вкладку «**Скрипт**».
5. Вставьте приведённый ниже C#-скрипт.
6. Опубликуйте процесс.

## C#-скрипт

Скрипт импорта данных из локального CSV-файла — объявление класса модели и чтение файла```
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

    public static void Main(Comindware.Process.Api.Data.ScriptContext context)
    {
        // Path to the CSV file on the server.
        // Use a UNC path for a shared network folder, e.g.:
        //   @"\\\\server\\shared\\import\\contracts.csv"
        // Or a local server path:
        //   @"C:\\import\\contracts.csv"
        string filePath = @"\\\\server\\shared\\import\\contracts.csv";

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
        foreach (var line in fileContent.Split(new[] { '\\r', '\\n' }, StringSplitOptions.RemoveEmptyEntries))
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
- **Метод `GetStatusId` (строки 26–34)** — сопоставляет человекочитаемое название статуса из CSV с идентификатором записи в шаблоне *«Статусы договора»*. Замените `"oa.1"`, `"oa.2"`, `"oa.3"` на фактические идентификаторы записей из вашего шаблона.
- **Метод `ParseLine` (строки 37–58)** — разбирает строку CSV на объект `CsvRow`: разделяет по указанному разделителю, преобразует дату с учётом часового пояса, преобразует сумму в число.
- **Метод `Main`** — точка входа, вызывается при выполнении задачи-скрипта в процессе.

  - **Переменная `filePath`** — путь к CSV-файлу. Для сетевой папки укажите UNC-путь (например, `\\\\server\\share\\file.csv`). Для локальной папки сервера — локальный путь (`C:\\import\\file.csv`).
  - **Переменная `delimiter`** — символ-разделитель столбцов. По умолчанию `;`.
  - **Переменная `fileEncoding`** — кодировка файла. Рекомендуется `Encoding.UTF8`. При использовании других кодировок (например, `Encoding.GetEncoding("windows-1251")`) замените значение.
  - **Чтение файла (строки 76–80)** — файл читается целиком через `StreamReader` с указанием кодировки.
  - **Разбор строк (строки 82–93)** — содержимое файла разбивается на строки. Строка-заголовок пропускается по условию: последний столбец заголовка не является числом.
  - **Цикл по строкам CSV (строки 100–127)** — для каждой строки данных:

    1. Определяется идентификатор статуса через `GetStatusId`.
    2. Создаётся запись договора через `CreateWithAlias` — в словарь передаются системные имена атрибутов и их значения.
    3. Создаётся запись клиента через `CreateWithAlias` — в атрибут `Dogovor` передаётся идентификатор созданного договора, устанавливая связь между записями.

**Системные имена, которые необходимо заменить на ваши:**

| В скрипте | Описание |
| --- | --- |
| `Contracts` | Системное имя шаблона записи *«Договоры»* |
| `Clients` | Системное имя шаблона записи *«Клиенты»* |
| `Nazvanie` | Системное имя атрибута *«Название»* в шаблоне *«Договоры»* |
| `Summa` | Системное имя атрибута *«Сумма»* в шаблоне *«Договоры»* |
| `Data` | Системное имя атрибута *«Дата»* в шаблоне *«Договоры»* |
| `Status` | Системное имя атрибута *«Статус»* в шаблоне *«Договоры»* |
| `Naimenovanie` | Системное имя атрибута *«Наименование»* в шаблоне *«Клиенты»* |
| `KontaktnoeLitso` | Системное имя атрибута *«Контактное лицо»* в шаблоне *«Клиенты»* |
| `Telefon` | Системное имя атрибута *«Телефон»* в шаблоне *«Клиенты»* |
| `Email` | Системное имя атрибута *«Email»* в шаблоне *«Клиенты»* |
| `Dogovor` | Системное имя атрибута *«Договор»* в шаблоне *«Клиенты»* |

Системные имена шаблонов и атрибутов указаны на вкладке «**Свойства**» соответствующего шаблона или атрибута.

Обновление существующих записей

В приведённом примере для каждой строки CSV создаются новые записи. Если требуется обновлять существующие записи при повторном импорте, необходимо добавить логику поиска записи по ключевому полю (например, по названию договора) и вызывать `Api.TeamNetwork.ObjectService.EditWithAlias(recordId, data)`, если запись найдена, либо `CreateWithAlias`, если запись отсутствует.

## Тестирование

1. Убедитесь, что CSV-файл размещён в указанной сетевой папке и доступен для чтения с сервера.
2. Запустите созданный процесс вручную со страницы «**Процессы**»: выберите процесс и нажмите кнопку «**Запустить**».
3. Дождитесь завершения процесса.
4. Перейдите в шаблон *«Клиенты»*, на вкладку «**Свойства**» и нажмите кнопку «**Перейти к экземплярам**» — в списке должны отобразиться записи клиентов с привязанными договорами.
5. Перейдите в шаблон *«Договоры»* — в списке должны отобразиться записи договоров с указанными статусами.
6. Если импорт не выполнился, проверьте:

   - доступность сетевой папки с сервера **Comindware Platform**;
   - права учётной записи сервера приложений на чтение файла;
   - соответствие системных имён шаблонов и атрибутов в скрипте;
   - кодировку CSV-файла (должна быть UTF-8);
   - корректность идентификаторов статусов в методе `GetStatusId`.

## Автоматизация запуска

Для регулярной синхронизации данных процесс импорта можно запускать автоматически:

- **По расписанию** — настройте [подключение для приёма сообщений](https://kb.comindware.ru/article.php?id=5628), которое будет запускать процесс по расписанию.
- **По событию** — настройте сценарий, отслеживающий изменения в сетевой папке, и запускающий процесс импорта при появлении нового файла.
- **По HTTP-запросу** — настройте [подключение для приёма HTTP-запросов](https://kb.comindware.ru/article.php?id=5311), которое будет запускать процесс импорта по внешнему сигналу (например, после завершения выгрузки данных смежной системой).

## Связанные статьи

- *[Импорт данных в шаблон](https://kb.comindware.ru/article.php?id=5737)*
- *[Адаптер импорта данных](https://kb.comindware.ru/article.php?id=5743)*
- *[Написание скриптов на языке C#](https://kb.comindware.ru/article.php?id=5211)*
- *[HTTP-запросы POST. Отправка JSON/XML из сценария с помощью C#](https://kb.comindware.ru/article.php?id=5324)*
- *[Подключения для приёма сообщений](https://kb.comindware.ru/article.php?id=5628)*
- *[Задача-скрипт](https://kb.comindware.ru/article.php?id=5668)*