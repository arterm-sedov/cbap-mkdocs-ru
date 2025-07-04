---
title: 'Получение данных от API ФНС с помощью C#'
kbId: 4924
tags: 
    - интеграция
    - ФНС
    - скрипт
hide: tags
---

# Получение данных от API ФНС с помощью C\# {: #example_csharp_tax_service_integrate }

## Введение {: #example_csharp_tax_service_integrate_intro }

Здесь представлен пример скрипта для автоматического получения данных о компании по её ИНН из базы ФНС.

Скрипт запускается по нажатию кнопки на форме контрагента и заполняет поля данными, полученными из ФНС.

Интеграция с сервисом ФНС осуществляется через [API-ФНС](https://api-fns.ru/index) посредством метода `multinfo`.

Приведённый пример скрипта поддерживает получение следующих данных:

- **Наименование юридического лица/ИП**
- **Количество сотрудников**
- **Годовой доход**
- **ФИО руководителя**
- **ОГРН/ОГРНИП**
- **КПП** (для юридических лиц)
- **Юридический адрес**
- **ОКВЭД**
- **Вид деятельности**

## Прикладная задача {: #example_csharp_tax_service_integrate_use_case }

Имеется шаблон записи _«Контрагенты»_, в котором хранятся следующие сведения:

- **Для юридического лица**
    - ИНН
    - Наименование юридического лица
    - Количество сотрудников
    - Годовой доход
    - Ф.&nbsp;И.&nbsp;О. руководителя
    - ОГРН
    - КПП
    - Юридический адрес
    - ОКВЭД
    - Вид деятельности
- **Для индивидуального предпринимателя**
    - ИНН
    - Наименование ИП
    - Ф.&nbsp;И.&nbsp;О. предпринимателя
    - ОГРНИП
    - Юридический адрес
    - ОКВЭД
    - Вид деятельности

Требуется автоматически получать актуальные сведения о контрагенте из базы ФНС по его ИНН.

Данные необходимо получать по нажатию кнопки _«Получить сведения из ФНС»_ на форме контрагента.

Если ИНН является действительным и сервис API-ФНС отправил данные, скрипт должен определить тип контрагента (юридическое лицо или ИП) и заполнить соответствующие поля.

Если какие-либо данные в ответе API отсутствуют, соответствующие поля заполнять не требуется.

При повторном нажатии кнопки _«Получить сведения из ФНС»_ данные должны перезаписываться.

## Настройка интеграции {: #example_csharp_tax_service_integrate_configure .pageBreakBefore }

!!! warning "Логика работы скрипта"

    Представленный здесь скрипт работает следующим образом:

    1. Получает значение ИНН из текущей записи контрагента.
    2. Формирует запрос к API ФНС с полученным ИНН.
    3. Обрабатывает ответ от API и извлекает данные.
    4. Определяет тип контрагента (ЮЛ или ИП) и выбирает соответствующий набор данных.
    5. Записывает полученные данные в соответствующие атрибуты.
    6. Обрабатывает возможные ошибки и выдаёт понятные сообщения пользователю.
    7. Отображает результат выполнения операции.

1. Зарегистрируйтесь на сайте [API-ФНС](https://api-fns.ru/index) и получите ключ API для подключения.
2. Создайте шаблон _«Контрагенты»_.
3. Создайте и поместите на форму шаблона следующие текстовые атрибуты:

    | Название                 | Системное имя           |
    | ------------------------ | ----------------------- |
    | _ИНН_                    | `ИНН`                   |
    | _Наименование ЮЛ_        | `НаименованиеЮЛ`        |
    | _Количество сотрудников_ | `КоличествоСотрудников` |
    | _Годовой доход_          | `ГодовойДоход`          |
    | _ФИО руководителя_       | `ФИОРуководителя`       |
    | _ОГРН_                   | `ОГРН`                  |
    | _КПП_                    | `КПП`                   |
    | _Юридический адрес_      | `ЮридическийАдрес`      |
    | _ОКВЭД_                  | `ОКВЭД`                 |
    | _Вид деятельности_       | `ВидДеятельности`       |
    | _Наименование ИП_        | `НаименованиеИП`        |
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

4. В шаблоне _«Контрагенты»_ создайте кнопку со следующими свойствами:

    - **Отображаемое название:** _Получить данные из ФНС_
    - **Контекст операции: запись**
    - **Операция: C#-скрипт**
    - **Результат выполнения: обновить данные**

5. На вкладке «**Скрипт**» введите следующий код:

    !!! warning "Подстановка фактических имён и значений"

        Замените в коде:

        - значение `123` на ключ API, полученный от ФНС.
        - имя `Контрагенты` на фактическое системное имя вашего шаблона записи с данными контрагентов.
        - системные имена атрибутов на фактически используемые в вашем шаблоне контрагентов.

    ``` cs title="Скрипт для получения данных от ФНС"
    // Импортируем базовые типы и функции .NET Framework.
    using System; 
    // Импортируем классы коллекций и словарей для хранения данных.
    using System.Collections.Generic;
    // Импортируем расширения LINQ для работы с коллекциями и выполнения запросов.
    using System.Linq;
    // Импортируем классы для работы с сущностями данных.
    using Comindware.Data.Entity;
    // Импортируем классы для обработки нажатий кнопок и возврата результатов выполнения скрипта.
    using Comindware.TeamNetwork.Api.Data.UserCommands;
    // Импортируем классы для работы с данными.
    using Comindware.TeamNetwork.Api.Data;
    // Импортируем библиотеку RestSharp для отправки HTTP-запросов в API ФНС.
    using RestSharp;
    // Импортируем библиотеку Newtonsoft.Json для обработки JSON-ответов от API.
    using Newtonsoft.Json.Linq;
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для получения данных от ФНС — продолжение"
    {% else %}

    {% endif %}
    {% raw %}
    class Script{
        public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities) { 
            // Получаем ID текущей записи контрагента.
            var contextObjectId = userCommandContext.ObjectIds[0];
            // Устанавливаем флаг успешного выполнения операции.
            var successFlag = true;
            // Задаём текст сообщения об успешном получении данных от ФНС.
            string text = "Данные контрагента получены";
            // Инициализируем переменные для работы с API.
            IRestResponse response = new RestResponse();
            // Задаём URL-адрес API ФНС для получения данных об организации.
            string url_Source = "https://api-fns.ru/api/multinfo";
            // Инициализируем клиент для отправки HTTP-запросов.
            var client = new RestClient(url_Source);
            // Создаём пустой GET-запрос к API.
            var request = new RestSharp.RestRequest("", Method.GET);
            // Устанавливаем заголовки запроса для получения JSON-ответа.
            request.AddHeader("RestRequest", "application/json");
            request.AddHeader("Accept", "application/json");
            // Создаём переменную для хранения годового дохода компании.
            long revenue = 0;
            // Создаём словарь для хранения и записи данных данных в атрибуты.
            Dictionary<string,object> data = new Dictionary<string,object>();
            // Создаём массив c системным именем атрибута, содержащего ИНН.
            var InnAttributeSystemName = "ИНН";
            try{
                // Получаем значение ИНН из текущей записи.
                var innAttributeValueObject = Api.TeamNetwork.ObjectService.GetPropertyValues(new[]{userCommandContext.ObjectIds[0]}, new[] {"ИНН"});
                // Создаём словарь для хранения ID и значения атрибута "ИНН".
                Dictionary<string, object> innAttributeDictionary = new Dictionary<string, object> {{"id", innAttributeValueObject.FirstOrDefault().Key}};
                // Извлекаем значение ИНН из полученных данных.
                object _Value = null;
                if (innAttributeValueObject.FirstOrDefault().Value.TryGetValue(InnAttributeSystemName, out object obj) && obj != null){_Value = obj;}
                innAttributeDictionary.Add(InnAttributeSystemName, _Value);
                // Добавляем в запрос параметры: ИНН и ключ API.
                request.AddParameter("req", innAttributeDictionary["ИНН"].ToString());
                // 123 — полученный ключ API ФНС.
                request.AddParameter("key", "123");

                try{
                    // Выполняем запрос к API ФНС и сохраняем ответ.
                    response = client.Execute(request);
                    // Проверяем успешность запроса и наличие данных в ответе.
                    if((int)response.StatusCode == 200 && response.Content.Length>15){
                        // Обрабатываем JSON-ответ.
                        JObject jObject = JObject.Parse(response.Content);
                        // Определяем тип контрагента (ЮЛ или ИП).
                        var responseItems = jObject["items"][0].ToString().Split('{');
                        responseItems = responseItems[1].Split(':');
                        responseItems = responseItems[0].Split('"');
                        string companyType = responseItems[1];
    {% endraw %}
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для получения данных от ФНС — продолжение"
    {% endif %}
                        // Обрабатываем данные для юридического лица.
                        if (companyType == "ЮЛ"){
                            // Извлекаем годовой доход (выручку) компании.
                            try{revenue = (long)jObject["items"][0]["ЮЛ"]["Финансы"]["Выручка"] *1000;}catch{}
                            // Извлекаем и сохраняем наименование юридического лица
                            // в атрибут с системным именем "НаименованиеЮЛ".
                            try{data.Add("НаименованиеЮЛ", jObject["items"][0]["ЮЛ"]["НаимСокрЮЛ"].ToString());}catch{}
                            // Извлекаем и сохраняем количество сотрудников
                            // в атрибут с системным именем "КоличествоСотрудников".
                            try{data.Add("КоличествоСотрудников", (int)jObject["items"][0]["ЮЛ"]["ОткрСведения"]["КолРаб"] );
                            }catch{}
                            // Сохраняем годовой доход
                            // в атрибут с системным именем "ГодовойДоход".
                            try{data.Add("ГодовойДоход", revenue);}catch{}
                            // Извлекаем и сохраняем ФИО руководителя
                            // в атрибут с системным именем "ФИОРуководителя".
                            try{data.Add("ФИОРуководителя", jObject["items"][0]["ЮЛ"]["Руководитель"]["ФИОПолн"].ToString());
                            }catch{}
                            // Извлекаем и сохраняем ОГРН
                            // в атрибут с системным именем "ОГРН".
                            try{data.Add("ОГРН", jObject["items"][0]["ЮЛ"]["ОГРН"].ToString());}catch{}
                            // Извлекаем и сохраняем КПП
                            // в атрибут с системным именем "КПП".
                            try{data.Add("КПП", jObject["items"][0]["ЮЛ"]["КПП"].ToString());}catch{}
                            // Извлекаем и сохраняем юридический адрес
                            // в атрибут с системным именем "ЮридическийАдрес".
                            try {data.Add("ЮридическийАдрес", jObject["items"][0]["ЮЛ"]["Адрес"]["АдресПолн"].ToString());
                            }catch{}
                            // Извлекаем и сохраняем код ОКВЭД
                            // в атрибут с системным именем "ОКВЭД".
                            try{data.Add("ОКВЭД", jObject["items"][0]["ЮЛ"]["ОснВидДеят"]["Код"].ToString());}catch{}
                            // Извлекаем и сохраняем описание вида деятельности
                            // в атрибут с системным именем "ВидДеятельности".
                            try{data.Add("ВидДеятельности", jObject["items"][0]["ЮЛ"]["ОснВидДеят"]["Текст"].ToString());}catch{}
                            // Обновляем текущую запись контрагента полученными данными.
                            // Контрагенты — системное имя шаблона записи.
                            Api.TeamNetwork.ObjectService.EditWithAlias("Контрагенты", contextObjectId, data);
                        }
                        // Обрабатываем данные для индивидуального предпринимателя.
                        else if(companyType == "ИП"){
                            // Извлекаем и сохраняем наименование ИП
                            // в атрибут с системным именем "НаименованиеИП".
                            try{data.Add("НаименованиеИП", jObject["items"][0]["ИП"]["НаимПолнЮЛ"].ToString());}catch{}
                            // Извлекаем и сохраняем ФИО ИП
                            // в атрибут с системным именем "ФИОРуководителя".
                            try{data.Add("ФИОРуководителя", jObject["items"][0]["ИП"]["ФИОПолн"].ToString());}catch{}
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для получения данных от ФНС — продолжение"
    {% endif %}
                            // Извлекаем и сохраняем ОГРНИП
                            // в атрибут с системным именем "ОГРН".
                            try{data.Add("ОГРН", jObject["items"][0]["ИП"]["ОГРНИП"].ToString());}catch{}
                            // Извлекаем и сохраняем юридический адрес
                            // в атрибут с системным именем "ЮридическийАдрес".
                            try{data.Add("ЮридическийАдрес", jObject["items"][0]["ИП"]["Адрес"]["АдресПолн"].ToString());
                            }catch{}
                            // Извлекаем и сохраняем код ОКВЭД
                            // в атрибут с системным именем "ОКВЭД".
                            try{data.Add("ОКВЭД", jObject["items"][0]["ИП"]["ОснВидДеят"]["Код"].ToString());}catch{}
                            // Извлекаем и сохраняем описание вида деятельности
                            // в атрибут с системным именем "ВидДеятельности".
                            try{data.Add("ВидДеятельности", jObject["items"][0]["ИП"]["ОснВидДеят"]["Текст"].ToString());
                            }catch{}
                            // Обновляем запись контрагента полученными данными.
                            // Контрагенты — системное имя шаблона записи.
                            Api.TeamNetwork.ObjectService.EditWithAlias("Контрагенты", contextObjectId, data);
                        }
                    }

                    // Обрабатываем случай, когда компания не найдена по ИНН.
                    else if(response.Content.Length<15){
                        text = "Нет компании по такому ИНН";
                        successFlag = false;
                    }
                    // Обрабатываем другие ошибки.
                    else{
                        text = "Непредвиденная ошибка";
                    }
                }
                // Обрабатываем исключения при выполнении запроса к API.
                catch(Exception e){
                    text = "Проблема с ответом от ФНС. Ошибка: "+ e.Message;
                    successFlag = false;
                }
            }
            // Обрабатываем случай, когда ИНН не указан в записи.
            catch{
                text = "Укажите ИНН";
                successFlag = false;
            }
    {% if pdfOutput %}
    ```
    {% include-markdown ".snippets/pdfPageBreakHard.md" %}
    ``` cs title="Скрипт для получения данных от ФНС — продолжение"
    {% endif %}
            // Формируем результат выполнения скрипта с сообщением для пользователя.
            var result = new UserCommandResult{
                Success = successFlag,
                Commited = true,
                ResultType = UserCommandResultType.Notificate,
                Messages = new[]{
                    new UserCommandMessage{
                        Severity = SeverityLevel.Normal,
                        Text = text
                    }
                }
            };
            return result;
        }
    }
    ```

6. Сохраните кнопку.
7. Поместите кнопку _«Получить данные из ФНС»_ на форму контрагента.

## Тестирование {: #example_csharp_tax_service_integrate_test }

1. Откройте или создайте запись контрагента.
2. Введите ИНН существующей компании или ИП.
3. Нажмите кнопку _«Получить данные из ФНС»_.
4. Через некоторое время поля записи должны заполниться данными из ФНС.
5. Убедитесь, что данные соответствуют типу контрагента (юридическое лицо или ИП).

!!! note "Возможные сообщения об ошибках"

    - _Укажите ИНН_ — не указан ИНН контрагента.
    - _Проблема с ответом от ФНС_ — проблема обмена данными с API ФНС.
    - _Нет компании по такому ИНН_ — компания не найдена в базе ФНС.
    - _Непредвиденная ошибка_ — иные проблемы.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
