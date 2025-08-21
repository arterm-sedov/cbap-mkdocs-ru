---
title: QR-код. Формирование с помощью C#-скрипта по нажатию кнопки
kbId: 4882
---

# QR-код. Формирование с помощью C#-скрипта по нажатию кнопки

В процессе настройки решения может понадобиться генерация QR-кода по нажатию кнопки (например, для формирования внутреннего кода для сотрудников). В данной статье мы рассмотрим пошаговую настройку генерации QR-кода по кнопке на форме.

**1.** В шаблоне записи, где вы планируете генерировать QR-код, создайте новый атрибут с типом данных «Текст» (***QRinbase***). Формат отображения не важен.

**2.** В том же шаблоне записи создайте ещё один атрибут с типом данных «Текст» (***QRcode***) и форматом отображения «HTML-текст». Установите флаг «Вычисляемый» и в поле «Вычисляемое выражение» вставьте следующую строку:

```

FORMAT("<img align='center'src='data:image/png;base64,{0}'width='60' height='60' frameborder='0'</img>",LIST($QRinbase))

```

**где:**

***width='60' / height='60'*** — значения ширины и высоты QR-кода на форме;

***QRinbase*** — системное имя атрибута, созданного в п.1.

Нам необходимо именно два атрибута, так как в первом будет храниться созданный QR-код в формате base64, а во втором — он же, но в формате изображения.

**3.** В том же шаблоне записи создайте новую кнопку (***Сформировать QR-код***) со следующими параметрами:

- Операция — C# скрипт;
- Контекст операции — Запись;
- Результат выполнения — Обновить данные.

Во вкладке «Скрипт» вставьте следующее:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
using RestSharp;
 
class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
        ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
        var link = Uri.EscapeDataString("https://yourinstance.comindware.net/#form/oa.1/form.2/" + userCommandContext.ObjectIds[0]);
        byte[] AsBytes = new System.Net.WebClient().DownloadData
            ("https://qrcode.tec-it.com/API/QRCode?size=small&data="+link);
      string AsBase64String = Convert.ToBase64String(AsBytes);
       
        var data = new Dictionary<string, object>
        {
            { "QRinbase", AsBase64String }
        };
        Api.TeamNetwork.ObjectService.EditWithAlias("RecordTemplate", userCommandContext.ObjectIds[0], data);
       
    var result = new UserCommandResult
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
    return result;
    }
}

```

**где:**

***https://yourinstance.comindware.net/#form/oa.1/form.2/*** — ссылка на форму в шаблоне записи, на которую пользователь должен попадать после сканирования QR-кода;

***QRinbase*** — системное имя атрибута в текущем шаблоне записи, созданного в п.1, куда записывается QR-код в формате base64;

***RecordTemplate*** — системное имя текущего шаблона записи;

***QR-код сформирован*** — текст сообщения для пользователя при успешном выполнении операции.

**4.** В том же шаблоне записи вынесите атрибут, созданный в п.2, на нужную форму(ы).

**5.** Вынесите кнопку, созданную в п.3, в нужное место: на форму(ы) или на область кнопок для форм.

**6.** Протестируйте.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
