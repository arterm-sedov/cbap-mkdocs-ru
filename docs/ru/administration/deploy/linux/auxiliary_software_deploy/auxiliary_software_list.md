---
title: Перечень стороннего программного обеспечения
kbTitle: Comindware Platform 5.0. Перечень стороннего программного обеспечения для Linux
kbId: 4582
---

# Перечень стороннего программного обеспечения {: #auxiliary_software_list }

## Введение

Некоторые функции **{{ productName }}** реализованы с использованием сторонних библиотек.

Для обеспечения работы **{{ productName }}** используются сторонние сервисы, такие как веб-сервер, СУБД, обратный прокси-сервер и т.&nbsp;п.

Здесь представлен перечень стороннего программного обеспечения (ПО), которое поставляется вместе с **{{ productName }}** версии 5.0 для операционных систем (ОС) семейства Linux: «Альт Сервер» и Astra Linux.

Состав стороннего ПО для других операционных систем может отличаться.

## Компоненты фронтенда (браузерной части)

Перечисленное ниже ПО входит в состав браузерной клиентской части **{{ productName }}** для любых ОС.

| **Наименование ПО и ссылка** | **Описание** | **Версия** | **Лицензия** |
| --- | --- | --- | --- |
| [apexcharts](https://apexcharts.com/) | Библиотека для построения интерактивных диаграмм на веб-страницах. | 3.35.3 | MIT License |
| [autosize](https://github.com/jackmoore/autosize) | Скрипт для автоматического изменения высоты текстовой области по размеру текста. | 5.0.1 | MIT License |
| [backbone](https://github.com/jashkenas/backbone/) | Библиотека для разработки веб-приложений, основанная на парадигме проектирования «модель-представление-контроллер». Предусмотрено подключение к API через интерфейс RESTful JSON. | 1.4.1 | MIT License |
| [backbone.marionette](https://github.com/marionettejs/backbone.marionette) | Библиотека для разработки больших приложений на Backbone.js. | 4.1.3 | MIT License |
| [backbone.radio](https://github.com/marionettejs/backbone.radio) | Библиотека, предоставляющая дополнительные механизмы обмена сообщениями для приложений на Backbone.js. | 2.0.0 | MIT License |
| [backbone.trackit](https://github.com/nytimes/backbone.trackit) | Плагин для Backbone.js, управляющий изменениями моделей. | 0.1.0 | MIT License |
| [backbone-associations](https://github.com/dhruvaray/backbone-associations) | Библиотека, позволяющая приложениям на Backbone.js формировать связи 1:1 и 1:N между моделями и коллекциями. | 0.6.2 | MIT License |
| [backbone-computedfields](https://github.com/alexbeletsky/backbone-computedfields) | Библиотека, предоставляющая вычисляемые поля для Backbone.Model. | 0.0.12 | MIT License |
| [bwip-js](https://github.com/metafloor/bwip-js) | Генератор штрихкодов на JavaScript. | 3.1.0 | MIT License |
| [ckeditor](https://ckeditor.com/ckeditor-4/) | WYSIWYG-редактор HTML. | 4.12.1 | GPLv2 |
| [ckeditor-wordcount-plugin](https://ckeditor.com/cke4/addon/wordcount) | Плагин для CKEditor. Подсчитывает и показывает количество слов в нижнем колонтитуле редактора. | 1.17.10 | MIT License |
| [codemirror](https://codemirror.net/5/) | Текстовый редактор для браузера, реализованный на JavaScript. | 5.65.6 | MIT License |{% if pdfOutput %}

| **Наименование ПО и ссылка** | **Описание** | **Версия** | **Лицензия** |
| --- | --- | --- | --- |{% endif %}
| [cropperjs](https://github.com/fengyuanchen/cropperjs) | Обрезчик изображений, реализованный на JavaScript. | 1.5.12 | MIT License |{% if not gostech %}
| [crypto-pro](https://github.com/vgoma/crypto-pro) | Асинхронный API для взаимодействия с «КриптоПро ЭЦП». | 2.3.0 | MIT License |{% endif %}
| [css-vars-ponyfill](https://github.com/jhildenbiddle/css-vars-ponyfill) | Библиотека, обеспечивающая клиентскую поддержку переменных CSS в устаревших и современных браузерах. | 2.4.7 | MIT License |
| [d3](https://d3js.org/) | JavaScript-библиотека для управления документами на основе данных. | 5.11.0 | ISC License |
| [handlebars](https://handlebarsjs.com/) | Библиотека, предоставляющая платформу для создания шаблонов. | 4.7.7 | MIT License |
| [html2canvas](https://www.npmjs.com/package/html2canvas) | JavaScript-визуализатор HTML . | 1.4.1 | MIT License |
| [innersvg-polyfill](https://github.com/dnozay/innersvg-polyfill) | JavaScript-библиотека, предоставляющая свойство innerHTML для всех SVGElements. | 0.0.5 | ALv2 |
| [inputmask](https://github.com/RobinHerbots/Inputmask) | JavaScript-библиотека для создания масок ввода. | 5.0.7 | MIT License |
| [jquery](https://jquery.com/) | JavaScript-библиотека, упрощающая обход дерева HTML DOM и манипулирование им, а также обработку событий, CSS-анимацию и Ajax. | 3.6.0 | MIT License |
| [jsencrypt](https://github.com/travist/jsencrypt) | JavaScript-библиотека для шифрования, расшифровки и формирования ключей OpenSSL RSA. | 3.2.1 | MIT License |
| [jssha](https://www.npmjs.com/package/jssha) | Реализация всего семейства хэшей SHA на JavaScript/TypeScript. | 2.3.1 | BSD 3-Clause License |
| [marionette.approuter](https://github.com/marionettejs/marionette.approuter) | JavaScript-библиотека, расширяющая Backbone.Router. | 1.0.2 | MIT License |
| [moment](https://www.npmjs.com/package/moment) | JavaScript-библиотека для синтаксического анализа, проверки, обработки и форматирования дат. | 2.29.4 | MIT License |
| [moment-timezone](https://www.npmjs.com/package/moment-timezone) | Библиотека для Moment.js, реализующая поддержку часовых поясов IANA. | 0.5.34 | MIT License |
| [react](https://react.dev/) | JavaScript-библиотека для создания пользовательских интерфейсов на основе компонентов. | 18.2.0 | MIT License |
| [react-dom](https://legacy.reactjs.org/docs/react-dom.html) | Библиотека для работы с DOM. | 18.2.0 | MIT License |
| [react-linkify](https://www.npmjs.com/package/react-linkify) | Компонент React для преобразования в гиперссылки найденных в тексте ссылок (URL-адресов, адресов эл.&nbsp;почты и т.&nbsp;п.). | 1.0.0-alpha | MIT License |
| [react-redux](https://github.com/reduxjs/react-redux) | Библиотека для привязки React для Redux . | 8.0.2 | MIT License |
| [react-transition-group](https://reactcommunity.org/react-transition-group/) | Набор компонентов React для управления анимацией. | 4.4.2 | BSD 3-Clause License |
| [redux](https://redux.js.org/) | JavaScript-библиотека для управления состоянием приложения и его централизации. | 4.2.0 | MIT License |
| [redux-thunk](https://github.com/reduxjs/redux-thunk) | Промежуточное ПО Thunk для Redux. | 2.4.1 | MIT License |
| [spectrum-colorpicker](https://www.npmjs.com/package/spectrum-colorpicker) | JavaScript-плагин для выбора цвета, использующий библиотеку jQuery. | 1.8.1 | MIT License |
| [style-loader](https://www.npmjs.com/package/style-loader) | Модуль загрузчика стилей для webpack. | 3.3.1 | MIT License |
| [text-mask-addons](https://www.npmjs.com/package/text-mask-addons) | Библиотека масок ввода для React, Angular, Ember, Vue и простого JavaScript. | 3.8.0 | Unlicense License |
| [typescript](https://www.typescriptlang.org/) | Строго типизированный язык программирования, основанный на JavaScript. | 4.7.4 | Apache 2.0 License |
| [underscore](https://underscorejs.org/) | JavaScript-библиотека, предоставляющая полезные функции. | 1.13.4 | MIT License |
| [vanilla-text-mask](https://www.npmjs.com/package/vanilla-text-mask) | JavaScript-функция, обеспечивающая использование масок в HTML-элементе <input/>. | 5.1.1 | Unlicense License |

## Компоненты бэкенда

Перечисленное ниже ПО входит в состав **{{ productName }}** и обеспечивает работу её серверной части.

| **Наименование ПО и ссылка** | **Описание** | **Версия** | **Лицензия** |
| --- | --- | --- | --- |
| [Antlr3.Runtime](https://github.com/antlr/antlr3) | Среда проектирования графического интерфейса пользователя для построения грамматик ANTLR v 3. | 3.3.1.7705 | BSD license |
| [Antlr4.Runtime.Standard](https://github.com/antlr/antlr4) | Среда проектирования графического интерфейса пользователя для построения грамматик ANTLR v4. | 4.11.1.0 | BSD 3-Clause License |{% if not gostech %}
| [Apache.Ignite.Core](https://ignite.apache.org/) | Распределенная база данных для высокопроизводительных вычислений со скоростью операций в памяти. | 2.16.0 | Apache 2.0 License |
| [Apache.Ignite.Linq](https://ignite.apache.org/) | Компонент библиотеки Apache.Ignite.Core. | 16.10.0.0 | Apache 2.0 License |
| [Apache.Ignite.NLog](https://ignite.apache.org/) | Компонент библиотеки Apache.Ignite.Core. | 9.0.0.0 | Apache 2.0 License |
| [Apache.Lucene.NET](https://github.com/apache/lucenenet) | Порт библиотеки Lucene для полнотекстового поиска. | 3.0.3.0 | Apache 2.0 License |
| [Apache.Lucene.Net.Contrib.Highlighter](https://github.com/apache/lucenenet) | Компонент библиотеки Apache.Lucene.Net. | 2.3.2.1 | Apache 2.0 License |
| [Apache.Lucene.Net.Contrib.Memory](https://github.com/apache/lucenenet) | Компонент библиотеки Apache.Lucene.Net. | 1.0.0.0 | Apache 2.0 License |{% endif %}
| [Aspose](https://products.aspose.com/pdf/net/) | Компонент для создания и обработки PDF-документов, который позволяет приложениям .NET считывать, записывать и обрабатывать PDF-документы. | 9.6.0.0 | Aspose Licence |
| [Autofac](https://github.com/autofac/Autofac) | IoC-контейнер для .NET. | 4.9.4 | MIT License |
| [BouncyCastle](https://github.com/chrishaly/bc-csharp) | Пакет, реализующий криптографические алгоритмы. | 1.8.10.0 | MIT License |
| [Castle.Core](https://github.com/castleproject/Core) | Castle Core API для создания прокси-объектов. | 4.0.0.0 | Apache 2.0 License |
| [CsvHelper](https://www.nuget.org/packages/CsvHelper/) | Библиотека .NET для чтения и записи файлов CSV. | 28.0.0.0 | Apache 2.0 License |
| [DDay.Collections](https://github.com/rianjs/ical.net) | Компонент iCal.NET — библиотеки классов для .NET, обеспечивает соответствие RFC 5545 и полную совместимость с популярными приложениями и библиотеками календарей. | 1.0.0.0 | MIT License |{% if pdfOutput %}

| **Наименование ПО и ссылка** | **Описание** | **Версия** | **Лицензия** |
| --- | --- | --- | --- |{% endif %}
| [DDay.iCal](https://github.com/rianjs/ical.net) | Компонент iCal.NET — библиотеки классов для .NET, которая обеспечивает соответствие RFC 5545 и полную совместимость с популярными приложениями и библиотеками календарей. | 1.0.2.0 | MIT License |{% if not gostech %}
| [Elasticsearch.Net](https://github.com/elastic/elasticsearch-net) | Строго типизированная клиентская библиотека, обеспечивающая работу с {{ openSearchVariants }}. | 7.0.0.0 | Apache 2.0 License |{% endif %}
| [Html Agility Pack (HAP)](https://github.com/zzzprojects/html-agility-pack) | Гибкое средство синтаксического анализа HTML, создающее модель чтения-записи DOM, с поддержкой простого XPATH или XSLT. | 1.11.15.0 | MIT License |
| [Humanizer](https://github.com/Humanizr/Humanizer) | Библиотека CS для обработки и отображения строк, перечислений, дат, времени, промежутков времени, чисел и количества. | 2.2.0.0 | MIT License |
| [JWT](https://github.com/jwt-dotnet/jwt) | Библиотека, реализующая JWT (JSON Web Token) для .NET. | 9.0.0.0 | CC0-1.0 License |
| [LdapForNet](https://github.com/flamencist/ldap4net) | Порт OpenLdap для .NET Core. | 2.7.15.0 | MIT License |
| [LibGit2Sharp](https://github.com/libgit2/libgit2sharp) | Библиотека, позволяющая писать собственные высокопроизводительные приложения Git на любом языке. | 0.26.0.0 | MIT License |
| [MailKit](https://github.com/jstedfast/MailKit/blob/master/LICENSE) | Кроссплатформенная клиентская библиотека для работы с почтовыми сообщениями. | 2.15.0.0 | MIT License |
| [Microsoft.AspNet.SignalR.Core](https://www.nuget.org/packages/Microsoft.AspNet.SignalR.Core) | Компонент ASP.NET Framework — библиотека, реализующая .NET для SignalR. | 2.4.3.0 | Apache 2.0 License |
| [Microsoft.AspNet.SignalR.SystemWeb](https://www.nuget.org/packages/Microsoft.AspNet.SignalR.Core) | Компонент ASP.NET Framework — библиотека, реализующая .NET для SignalR. | 2.4.3.0 | Apache 2.0 License |
| [Microsoft.Bcl.AsyncInterfaces](https://www.nuget.org/packages/Microsoft.Bcl.AsyncInterfaces/) | Библиотека, предоставляющая интерфейсы и вспомогательные типы IAsyncEnumerable<T> и IAsyncDisposable для .NET. | 7.0.0.0 | MIT License |
| [Microsoft.CodeAnalysis](https://www.nuget.org/packages/Microsoft.CodeAnalysis) | Компонент компилятора Roslyn .NET — предоставляет языки C# и Visual Basic с API анализа кода. | 3.9.0.0 | MIT License |
| [Microsoft.Data.Edm](https://www.nuget.org/packages/Microsoft.Data.Edm/) | Компонент OData. | 5.8.5.0 | MIT License |
| [Microsoft.Data.OData](https://www.nuget.org/packages/Microsoft.Data.OData/) | Компонент OData. | 5.8.5.0 | MIT License |
| [Microsoft.DiaSymReader](https://github.com/dotnet/symreader) | Управляемые определения интерфейсов COM, предоставляемые API-интерфейсами DiaSymReader. | 1.3.0.0 | MIT License |
| [Microsoft.Exchange.WebServices](https://github.com/OfficeDev/ews-managed-api) | Управляемый API веб-служб Exchange (EWS). | 15.0.0.0 | MIT License |
| [Microsoft.IdentityModel](https://github.com/AzureAD/azure-activedirectory-identitymodel-extensions-for-dotnet) | Библиотека для работы с OpenIdConnect и WsFederation.{% if not gostech %} **Примечание:** это необязательный компонент для входа в **{{ productName }}** через Google, Azure AD/ и другие службы OpenID. Этот компонент не устанавливается по умолчанию. При необходимости его можно установить при развертывании ПО.  {% endif %}| 5.3.0.0 | MIT License |
| [Microsoft.OData](https://www.nuget.org/packages/Microsoft.Data.OData/) | Библиотека для работы с OData. | 7.10.0.0 | MIT License |
| [Microsoft.Owin](https://www.nuget.org/packages/Microsoft.Owin) | Библиотека для работы с OWIN. | 4.1.1.0 | Apache 2.0 License |
| [Microsoft.Spatial](https://www.nuget.org/packages/Microsoft.Spatial/) | Библиотека для работы с геометрическими фигурами. | 7.10.0.0 | MIT License |{% if not gostech %}
| [Microsoft.Win32.Registry](https://www.nuget.org/packages/Microsoft.Win32.Registry/) | Библиотека для работы с реестром Windows. | 4.1.3.0 | MIT License |{% endif %}
| [MimeKit](https://github.com/jstedfast/MimeKit) | Библиотека для создания и обработки сообщений с использованием MIME. | 2.15.0.0 | MIT License |
| [Nest](https://www.nuget.org/packages/NEST) | Библиотека .NET-клиента для работы с {{ openSearchVariants }}. | 7.0.0.0 | Apache 2.0 License |
| [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/) | Json.NET — это высокопроизводительная платформа JSON для .NET. | 13.0.0.0 | MIT License |
| [NLog](https://github.com/NLog/NLog) | Платформа журналирования. | 5.0.0.0 | BSD 3-Clause License |
| [Owin](https://github.com/owin/owin/issues) | Интерфейс OWIN IAppBuilder. | 1.0.0.0 | Apache 2.0 License |
| [RazorGenerator.Mvc](https://www.nuget.org/packages/RazorGenerator.Mvc) | Библиотека для поддержки RazorView. | 2.0.0.0 | Apache 2.0 License |
| [Remotion.Linq](https://www.nuget.org/packages/Remotion.Linq/) | Библиотека для написания своего LINQ-провайдера. | 2.1.0.0 | Apache 2.0 License |
| [RestSharp](https://github.com/restsharp/RestSharp) | Клиент для REST- и HTTP-запросов. | 100.0.0.0 | Apache 2.0 License |
| [Simple.OData.Client](https://github.com/simple-odata-client/Simple.OData.Client) | Мультиплатформенный клиент OData. | 5.26.0.0 | MIT License |
| [Swashbuckle.Core](https://github.com/domaindrivendev/Swashbuckle.WebApi) | Библиотека, обеспечивающая поддержку Swagger для проектов с использованием Web API. | 1.0.0.0 | BSD 3-Clause License |
| [WebActivatorEx](https://www.nuget.org/packages/WebActivatorEx/) | Библиотека, обеспечивающая запуск кода другими пакетами на старте веб-приложений. | 2.0.0.0 | Apache 2.0 License |
| [YamlDotNet](https://github.com/aaubry/YamlDotNet) | Библиотека .NET для YAML. | 11.0.0.0 | MIT License |
| [zxing](https://github.com/zxing/zxing) | Библиотека для сканирования штрихкодов ZXing для Java в Android. | 0.16.8.0 | Apache 2.0 License |

## Вспомогательное ПО для «Альт Сервер»

Перечисленное ниже вспомогательное ПО используется для работы **{{ productName }}** под управлением ОС «Альт Сервер».

| **Наименование ПО и ссылка** | **Описание** | **Версия** | **Лицензия** |
| --- | --- | --- | --- |
| [dotnet-2.1](https://dotnet.microsoft.com/en-us/download/dotnet/2.1) | Виртуальный пакет для полной установки .NET 2.1 — платформы разработки с открытым исходным кодом. | 2.1.25 | MIT License |
| [dotnet-6.0](https://packages.altlinux.org/ru/sisyphus/srpms/dotnet-runtime-6.0/) | Виртуальный пакет для полной установки .NET 6.0 — платформы разработки с открытым исходным кодом. | 6.0.12 | MIT License |
| [dotnet-aspnetcore-runtime-6.0](https://packages.altlinux.org/ru/sisyphus/binary/dotnet-aspnetcore-runtime-6.0/) | Среда выполнения ASP.NET 6. Содержит все необходимые компоненты для запуска веб-приложений .NET Core. | 6.0.12 | MIT License |
| [dotnet-sdk-6.0](https://packages.altlinux.org/ru/sisyphus/srpms/dotnet-sdk-6.0/) | SDK для среды выполнения и библиотек .NET. | 6.0.112 | MIT License |{% if not gostech %}
| [Elasticsearch](https://www.elastic.co/elasticsearch/) | Распределенная облачная поисковая система RESTful. | 8.10.2 | Elastic License |{% endif %}
| [glib2](https://packages.altlinux.org/ru/sisyphus/srpms/glib2/) | GLib — это базовая низкоуровневая библиотека, которая обеспечивает обработку структур данных для C, предоставляет классы-оболочки переносимости и интерфейсы для таких функций времени выполнения, как цикл обработки событий, потоки, динамическая загрузка и объектная система. | 2.68.4 | LGPLv2+ |
| [librdkafka](https://packages.altlinux.org/ru/sisyphus/srpms/librdkafka/) | Реализация протокола Apache Kafka в C-библиотеке, содержащая поддержку как Producer, так и Consumer. | 1.5.3 | BSD-2-CLAUSE |{% if not gostech %}
| [mono-core](https://packages.altlinux.org/ru/sisyphus/binary/mono-core/) | Этот пакет содержит ядро среды выполнения Mono, включая виртуальную машину, компилятор Just-in-time, компилятор C#, инструменты безопасности и библиотеки (corlib, XML, System.Security, ZipLib, I18N, Cairo и Mono). | 6.12 | MIT License |{% endif %}{% if pdfOutput and not gostech %}

| **Наименование ПО и ссылка** | **Описание** | **Версия** | **Лицензия** |
| --- | --- | --- | --- |{% endif %}{% if not gostech %}
| [mono-data](https://packages.altlinux.org/ru/sisyphus/binary/mono-data/) | Этот пакет содержит сборку Mono для облегчения доступа к данным и работы с базами данных, совместимыми с LDAP серверами каталогов, а также обменом данными XML. Помимо сборок ADO.NET, Novell.LDAP и System.DirectoryServices, он также содержит приложение SQL командной строки и поставщики данных Microsoft SQL Server и ODBC. | 6.12 | MIT License |
| [nginx](https://packages.altlinux.org/ru/sisyphus/srpms/nginx/) | HTTP-сервер, обратный прокси-сервер. | 1.22.1 | BSD |{% endif %}
| [xsp](https://packages.altlinux.org/ru/sisyphus/srpms/xsp/) | XSP-сервер — это компактный веб-сервер, на котором размещаются классы{% if not gostech %} System.Webclasses Mono{% endif %} для запуска ASP.NET. | 4.7.1 | MIT License |

## Вспомогательное ПО для Astra Linux

Перечисленное ниже вспомогательное ПО используется для работы **{{ productName }}** под управлением ОС Astra Linux.

| **Наименование ПО и ссылка** | **Описание** | **Версия** | **Лицензия** |
| --- | --- | --- | --- |
| [openjdk-17-jre](https://wiki.astralinux.ru/pages/viewpage.action?pageId=147162398) | OpenJRE — это сборка JRE 17, соответствие спецификациям Java SE которой подтверждено тестами OpenJDK Technology Compatibility Kit.{% if not gostech %} **Примечание:** компания **{{ companyName }}** может заменить данное ПО на аналог по запросу и согласно ТЗ заказчика. {% endif %}| 17.0.7+7 | GPLv2 |{% if not gostech %}
| [Elasticsearch](https://www.elastic.co/) | Распределенная облачная поисковая система RESTful. | 8.10.2 | SSPL |{% endif %}
| [geoip-bin](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — инструменты командной строки для поиска IP-адресов, использующие библиотеку GeoIP. | 1.6.12-1 | Другая |
| [geoip-database](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX —бесплатная база данных GeoLiteCountry. | 20181108-1 | LGPLv2 |
| [libgd3](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGIX — графическая библиотека GD. Пакет библиотеки для среды выполнения. | 2.2.5-5.2+ ci202206301705+ astra1 | GPLv2+ |
| [libgd-tools](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX - инструменты командной строки и примеры кода, использующие графическую библиотеку GD. | 2.2.5-5.2+ ci202206301705+ astra1 | Другая |
| [libgeoip1](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — библиотека для определения страны по IP-адресу. | 1.6.12-1 | LGPLv2 |{% if pdfOutput %}

| **Наименование ПО и ссылка** | **Описание** | **Версия** | **Лицензия** |
| --- | --- | --- | --- |{% endif %}
| [libnginx-mod-http-geoip](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — HTTP-модуль GeoIP для NGINX. Создает переменные со значениями в зависимости от IP-адреса клиента, используя предварительно скомпилированные базы данных MaxMind. | 1.18.0-6.1 +deb11u2 | BSD 2-Clause License |
| [libnginx-mod-http-image-filter](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — HTTP-модуль фильтрации изображений для NGINX. | 1.18.0-6.1 +deb11u2 | BSD 2-Clause License |
| [libnginx-mod-http-xslt-filter](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — модуль преобразований XSLT для NGINX. | 1.18.0-6.1 +deb11u2 | BSD 2-Clause License |
| [libnginx-mod-mail](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — почтовый модуль для NGINX. Поддерживает проксирование всех стандартных почтовых протоколов, таких как IMAP, POP3 и SMTP. | 1.18.0-6.1 +deb11u2 | BSD 2-Clause License |
| [libnginx-mod-stream](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — потоковый модуль для NGINX. Добавляет поддержку потокового прокси. | 1.18.0-6.1 +deb11u2 | BSD 2-Clause License |
| [libnginx-mod-stream-geoip](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX —модуль GeoIP Stream для NGINX. | 1.18.0-6.1 +deb11u2 | BSD 2-Clause License |
| [libxpm4](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — библиотека X11 для работы с пиксельными картами (pixmap). Обеспечивает поддержку формата XPM в среде выполнения. | 1:3.5.12-1 | Другая |
| [libxslt1.1](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — библиотека libxslt, используемая приложениями для преобразований XSLT. | 1.1.32-2.2~ deb10u2 | libxslt |{% if not gostech %}
| [mono](http://www.mono-project.com/) | Mono — это платформа для запуска и разработки приложений. Предоставляемый пакет содержит:- интерфейс командной строки - LLVM - Roslyn - MCS - MSBuild - GAC - GC SGen, GC Boehm - XSP4 Server - FastCGI Mono Server 4 | 6.12.0.200- 0xamarin1+ debian9b1 | MIT License |{% endif %}
| [.NET SDK 6.0](https://packages.microsoft.com/config/debian/) | Платформа разработки с открытым исходным кодом. Предоставляемый пакет содержит:- .NET SDK 6.0.405 - .NETCore.App.Runtime 6.0.13 - dotnet-runtime-deps-debian 6.0.13 - .NETCore.App.Ref 6.0.13 - .NET Host — 7.0.2 - .NET Host FX Resolver — 6.0.13 - .NETCore.App.Host 6.0.13 - NETStandard.Library.Ref 2.1.0 - aspnetcore-runtime-6.0 - aspnetcore-targeting-pack-6.0{% if not gostech %} **Примечание:** компания **{{ companyName }}** может заменить данное ПО на аналог по запросу и согласно ТЗ заказчика. {% endif %}| 6.0.405-1 | MIT License |
| [nginx](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Пакет зависимостей NGINX для установки nginx-core. | 1.18.0-6.1+ deb11u2 | BSD 2-Clause License |
| [nginx-common](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Зависимость NGINX — базовые файлы конфигурации, используемые всеми версиями NGINX. | 1.18.0-6.1+ deb11u2 | BSD 2-Clause License |
| [nginx-core](http://download.astralinux.ru/astra/frozen/1.7_x86-64/1.7.0/repository-base/) | Веб/прокси-сервер NGINX. | 1.18.0-6.1+ deb11u2 | BSD 2-Clause License |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
