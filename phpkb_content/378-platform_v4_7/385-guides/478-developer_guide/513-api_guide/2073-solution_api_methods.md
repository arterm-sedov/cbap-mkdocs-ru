---
title: 'Методы Solution API'
kbId: 2073
url: 'https://kb.comindware.ru/article.php?id=2073'
updated: '2024-05-23 10:32:36'
---

# Методы Solution API

## Введение

Solution API предоставляет RESTful-методы, которые автоматически генерируются для всех шаблонов записей, аккаунтов, оргединиц и ролей (но не для шаблонов процессов) в текущем экземпляре **{{ productName }}**. Эти методы одинаковы для всех версий **{{ productName }}**. Для каждого шаблона предусмотрено пять методов:

- удаление записи;
- получение данных записи;
- изменение данных записи;
- получение данных всех записей;
- создание записи.

В этой статье представлен обзор методов Solution API. Полную информацию см. в Swagger.

## Доступ к Solution API

- Базовый URL-адрес для запросов Solution API:
  `https://your-host/api/public/solution/`
- Solution API поддерживает запросы `GET`, `PUT`, `POST`, `DELETE`.
- Методы Solution API передают данные в формате JSON.
- Solution API поддерживает базовую проверку подлинности.

## Использование Swagger

Swagger предоставляет подробную справку по методам API, включая описания запросов и ответов, а также модели данных с примерами значений.

Swagger позволяет выполнять запросы и просматривать ответы.

Интерфейс Swagger для Solution API доступен по адресу:

`http://your-host/Docs/SolutionApi`

Здесь `your-host` — доменное имя вашего сервера.

_![Интерфейс Swagger для метода Solution API, создающего запись в шаблоне](https://kb.comindware.ru/assets/img_64d362ff9cd63.png)_

## Описание методов Solution API

| TemplateSystemName — записи в шаблоне с системным именем TemplateSystemName | | | | |
| --- | --- | --- | --- | --- |
| **Метод** | **Запрос** | **Описание** | **Входные данные** | **Выходные данные** |
| DELETE | /TemplateSystemName/{id} | Удалить запись из шаблона `TemplateSystemName` | ID записи | Объект статуса |
| GET | /TemplateSystemName/{id} | Получить данные записи из шаблона `TemplateSystemName` | ID записи | Объект cо значениями атрибутов записи |
| PUT | /TemplateSystemName/{id} | Изменить данные записи из шаблона `TemplateSystemName` | ID записи и объект cо значениями атрибутов записи | Объект статуса |
| GET | /  TemplateSystemName | Получить данные всех записей из шаблона `TemplateSystemName` |  | Массив объектов со значениями атрибутов всех записей |
| POST | /  TemplateSystemName | Создать запись в шаблоне `TemplateSystemName` | Объект cо значениями атрибутов записи | ID записи |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
