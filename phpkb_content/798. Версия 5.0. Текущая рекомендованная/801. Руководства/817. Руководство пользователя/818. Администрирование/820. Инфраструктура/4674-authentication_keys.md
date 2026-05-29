---
title: 'Ключи аутентификации API. Определения, настройка, удаление'
kbId: 4674
url: 'https://kb.comindware.ru/article.php?id=4674'
updated: '2025-10-21 15:18:36'
---

# Ключи аутентификации API. Определения, настройка, удаление

## Определения

- **Ключи аутентификации** используются для доступа к API **{{ productName }}** из внешних систем с использованием HMAC-аутентификации.
- Ключ аутентификации следует назначать аккаунту, у которого есть разрешение «**Вызовы API**» в [системной роли][system_roles], либо пользователю входящему в системную роль «**Системные администраторы**». Только такие аккаунты могут использовать API **{{ productName }}**.
- При HMAC-аутентификации внешняя система должна передать токен и секретный ключ.

## Просмотр списка и настройка ключа аутентификации

1. На странице «[**Администрирование**][administration]» в разделе «**Инфраструктура**» выберите пункт «**Ключи аутентификации**» *‌*.
2. Отобразится список ключей.

   ![Список ключей аутентификации](/platform/v5.0/administration/infrastructure/img/authentication_key_list.png)

   Список ключей аутентификации
3. Нажмите кнопку «**Создать**» или дважды нажмите строку имеющегося ключа.
4. При создании ключа выберите аккаунт **пользователя** и **срок действия ключа**. При настройке имеющегося ключа можно только изменить его **срок действия**.

   ![Настройка нового ключа аутентификации](/platform/v5.0/administration/infrastructure/img/authentication_key_settings.png)

   Настройка нового ключа аутентификации
5. Нажмите кнопку «**Сохранить**».
6. Отобразятся свойства сформированного ключа.
7. Используйте сформированные **секретный ключ** и **токен для аутентификации** внешних систем при доступе к API **{{ productName }}**.

   ![Свойства сформированного ключа аутентификации](/platform/v5.0/administration/infrastructure/img/authentication_key_properties.png)

   Свойства сформированного ключа аутентификации

## Примеры отправки запросов с HMAC-аутентификацией

### Скрипт для Postman

Для отправки запросов с HMAC-аутентификацией в Postman:

1. Создайте новый запрос и укажите метод и URL.
2. Перейдите на вкладку **Scripts** — **Pre-request**.
3. Вставьте следующий скрипт:

   ```
   // Укажите свой токен аутентификации
   const credential = '*******';
   // Укажите свой секретный ключ
   const secret = '******************************';

   // Функция подписания запроса
   const signRequest = (host,
       method,      // HTTP-метод (GET, PUT, POST, DELETE)
       url,         // Путь и параметры запроса
       body,        // Тело запроса (undefined если отсутствует)
       credential,  // Токен аутентификации
       secretKey    // Секретный ключ (base64)
   ) => {
       var verb = method.toUpperCase();
       var utcNow = new Date().toUTCString();
       // Вычисляем SHA256-хеш тела запроса
       var contentHash = CryptoJS.SHA256(body).toString(CryptoJS.enc.Base64);
       // Имена заголовков через точку с запятой
       var signedHeaders = "x-ms-date;host;x-ms-content-sha256";
       // Формируем строку для подписи
       var stringToSign =
           verb + '\\n' +                              // HTTP-метод
           url + '\\n' +                               // Путь и параметры
           utcNow + ';' + host + ';' + contentHash;   // Значения подписанных заголовков
       console.log('string to sign', stringToSign);
       // Вычисляем подпись в формате MAC-SHA256
       var secret = CryptoJS.enc.Base64.parse(secretKey);
       var signature = CryptoJS.HmacSHA256(stringToSign, secret).toString(CryptoJS.enc.Base64);
       // Возвращаем заголовки для аутентификации
       return [
           { key: "x-ms-date", value: utcNow },
           { key: "x-ms-content-sha256", value: contentHash },
           { key: "Authorization", value: "HMAC-SHA256 Credential=" + credential + "&SignedHeaders=" + signedHeaders + "&Signature=" + signature },
           { key: 'Content-Type', value: 'application/json' }
       ];
   }

   // Функция интерполяции переменных Postman
   const interpolate = (value) => {
       const { Property } = require('postman-collection');
       return Property.replaceSubstitutions(value, pm.variables.toObject());
   }

   // Получаем параметры запроса из Postman
   const host = pm.request.url.getHost() + (pm.request.url.port ? ':' + pm.request.url.port : '');
   const method = pm.request.method;
   const url = pm.request.url.getPath();
   const bodyStr = interpolate(pm.request.body.toString());
   // Получаем подписанные заголовки
   const headers = signRequest(host, method, url, bodyStr ?? '', credential, secret)

   // Добавляем заголовки к запросу
   headers.forEach((header) => pm.request.addHeader(
       {
           key: header.key,
           value: header.value,
       }
   ));
   ```
4. Протестируйте работу запроса.

### Скрипт для PowerShell

Для отправки запросов с HMAC-аутентификацией в PowerShell используйте следующий скрипт.

```
# Укажите свой ттокен аутентификации
$Credential = "********"
# Укажите свой секретный ключ
$Secret = "**********************"

# Укажите URL сервера {{ productName }}
$hostUrl = "http://localhost:80"
# Укажите метод запроса (`GET`, `POST`, `PUT`, `DELETE`)
$method = "POST"
# Укажите путь к эндпоинту API {{ productName }}
$apiUrl = "/api/public/system/Base/OntologyService/GetAxioms"
# Составьте тело запроса (если необходимо)
$bodyStr = "1234"

# Функция вычисления SHA256-хеша
function Compute-Sha256 {
    param (
        [string]$inputString
    )

    $bytes = [System.Text.Encoding]::UTF8.GetBytes($inputString)
    $hashBytes = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)
    return [Convert]::ToBase64String($hashBytes)
}

# Функция подписания запроса
function Sign-Request {
    param (
        [string]$hostParam,
        [string]$methodParam,
        [string]$urlParam,
        [string]$bodyParam
    )

    $verb = $methodParam.ToUpper()
    $utcNow = [System.DateTime]::UtcNow.ToString("R") # RFC1123 формат
    $contentHash = Compute-Sha256 $bodyParam
    $signedHeaders = "x-ms-date;host;x-ms-content-sha256"
    $hostOnly = $hostParam.Replace('http://','').Replace('https://','')
    $stringToSign = "${verb}`n${urlParam}`n${utcNow};${hostOnly};${contentHash}"

    Write-Host "String to sign: $stringToSign"

    $secretBytes = [Convert]::FromBase64String($Secret)
    $hmac = [System.Security.Cryptography.HMACSHA256]::new($secretBytes)
    $signatureBytes = $hmac.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($stringToSign))
    $signature = [Convert]::ToBase64String($signatureBytes)

    # Возвращаем хеш-таблицу вместо массива объектов
    return @{
        "x-ms-date" = $utcNow
        "x-ms-content-sha256" = $contentHash
        "Authorization" = "HMAC-SHA256 Credential=${Credential}&SignedHeaders=${signedHeaders}&Signature=${signature}"
        "Content-Type" = "application/json"
    }
}

# Получаем подписанные заголовки
$headers = Sign-Request -hostParam $hostUrl -methodParam $method -urlParam $apiUrl -bodyParam $bodyStr

# Формируем параметры запроса
$params = @{
    Uri = "$hostUrl$apiUrl"
    Method = $method
    # Используем готовую хеш-таблицу заголовков
    Headers = $headers
    ContentType = "application/json"
}

# Добавляем тело запроса (если есть)
if (-not [string]::IsNullOrEmpty($bodyStr)) {
    $params.Body = $bodyStr
}

# Отправляем запрос
try {
    $response = Invoke-RestMethod @params
    Write-Host "Успешный ответ:`n$($response | ConvertTo-Json -Depth 10)"
} catch {
    Write-Host "Ошибка: $($_.Exception.Message)"
    if ($_.Exception.Response) {
        $reader = [System.IO.StreamReader]::new($_.Exception.Response.GetResponseStream())
        $reader.BaseStream.Position = 0
        $errorResponse = $reader.ReadToEnd()
        Write-Host "Детали ошибки: $errorResponse"
    }
}
```

## Удаление ключей аутентификации

Внимание!

После удаления ключей аутентификации аккаунты, которым они назначены, потеряют возможность использовать API **{{ productName }}** с HMAC-аутентификацией.

1. Откройте список ключей аутентификации.
2. Установите флажки в первом столбце для адаптеров, подлежащих удалению.
3. Нажмите кнопку «**Удалить**».
4. Подтвердите удаление ключей.

--8<-- "related_topics_heading.md"

- *[Введение в API][api_intro]*
- *[Системные роли. Определения, настройка, объединение, удаление][system_roles]*

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
