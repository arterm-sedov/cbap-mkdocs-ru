---
title: 'QR-код. Формирование с помощью C#-скрипта по нажатию кнопки'
kbId: 5340
url: 'https://kb.comindware.ru/article.php?id=5340'
updated: '2026-06-16 19:15:37'
---

# QR-код. Формирование с помощью C#-скрипта по нажатию кнопки

Здесь приведён пример настройки кнопки, которая формирует QR-код для текущей записи с помощью C#-скрипта.

Такую кнопку можно использовать, например, чтобы создать внутренний код сотрудника, пропуск, ссылку на карточку записи или другой QR-код, который должен генерироваться по запросу пользователя.

## Логика решения

Для отображения QR-кода используются два текстовых атрибута:

- `QRinbase` — хранит QR-код в формате Base64;
- `QRcode` — отображает QR-код как изображение на форме.

Кнопка вызывает C#-скрипт, который:

1. Формирует ссылку на текущую запись.
2. Передаёт ссылку во внешний сервис генерации QR-кодов.
3. Получает изображение QR-кода.
4. Преобразует изображение в строку Base64.
5. Записывает строку Base64 в атрибут `QRinbase`.

Атрибут `QRcode` по формуле преобразует строку Base64 в HTML-изображение.

## Настройка атрибутов

1. В шаблоне записи, где требуется формировать QR-код, создайте атрибут типа «**Текст**» с системным именем `QRinbase`.
2. Создайте ещё один атрибут типа «**Текст**» с системным именем `QRcode`.
3. Для атрибута `QRcode` задайте формат отображения «**HTML-текст**».
4. Установите для атрибута `QRcode` флажок «**Вычислять автоматически**».
5. Введите для атрибута `QRcode` следующую формулу:

```
FORMAT(
    "<img align='center' src='data:image/png;base64,{0}' width='60' height='60' />",
    LIST($QRinbase)
)
```cs
**Здесь**

| Значение | Описание |
| -------- | -------- |
| `width='60'` | Ширина QR-кода на форме. |
| `height='60'` | Высота QR-кода на форме. |
| `QRinbase` | Системное имя атрибута, который хранит QR-код в формате Base64. |

## Настройка кнопки {: #qr-code-csharp-button_button }

1. В том же шаблоне записи создайте кнопку _«Сформировать QR-код»_.
2. Настройте кнопку:

    | Свойство | Значение |
    | -------- | -------- |
    | Тип кнопки | **C#-скрипт** |
    | Контекст кнопки | **Запись** |
    | Результат выполнения | **Обновить данные** |

3. На вкладке «**Скрипт**» введите следующий C#-скрипт:

``` csharp
using System;
using System.Collections.Generic;
using System.Net;
using Comindware.TeamNetwork.Api.Data;
using Comindware.TeamNetwork.Api.Data.UserCommands;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext)
    {
        ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;

        var objectId = userCommandContext.ObjectIds[0];
        var recordUrl = "https://yourinstance.comindware.net/#form/oa.1/form.2/" + objectId;
        var encodedUrl = Uri.EscapeDataString(recordUrl);
        var qrCodeBytes = new WebClient().DownloadData(
            "https://qrcode.tec-it.com/API/QRCode?size=small&data=" + encodedUrl);
        var qrCodeBase64 = Convert.ToBase64String(qrCodeBytes);

        var data = new Dictionary<string, object>
        {
            { "QRinbase", qrCodeBase64 }
        };

        Api.TeamNetwork.ObjectService.EditWithAlias("RecordTemplate", objectId, data);

        return new UserCommandResult
        {
            Success = true,
            Commited = true,
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "QR-код сформирован"
                }
            }
        };
    }
}
```

**Здесь:**

| Значение | Описание |
| --- | --- |
| `https://yourinstance.comindware.net/#form/oa.1/form.2/` | Ссылка на форму записи, которая должна открываться после сканирования QR-кода. |
| `QRinbase` | Системное имя атрибута, в который записывается QR-код в формате Base64. |
| `RecordTemplate` | Системное имя текущего шаблона записи. |
| `QR-код сформирован` | Текст сообщения, которое отобразится пользователю после успешного выполнения кнопки. |

## Проверка результата

1. Вынесите атрибут `QRcode` на форму записи.
2. Вынесите кнопку *«Сформировать QR-код»* на форму или в область кнопок.
3. Откройте запись.
4. Нажмите кнопку *«Сформировать QR-код»*.
5. Убедитесь, что на форме отобразился QR-код.
6. Отсканируйте QR-код и проверьте, что он открывает нужную форму записи.

Внимание!

В примере используется внешний сервис генерации QR-кодов. Перед применением решения в промышленной среде убедитесь, что использование внешнего сервиса соответствует требованиям безопасности вашей организации.

--8<-- "related_topics_heading.md"

- [C#-скрипты. Руководство по разработке][csharp_guide]
- [Кнопки. Определения, настройка, удаление][buttons]
- [Атрибут типа «Текст»][attribute_text]
- [Язык формул](https://kb.comindware.ru/category.php?id=901)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
