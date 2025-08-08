---
title: Интеграция с Telegram-ботом. Пример: настройка приложения, Telegram и кода бота
kbId: 4923
---

# Интеграция с Telegram-ботом. Пример: настройка приложения, Telegram и кода бота

## Введение

В этой статье разберём пример того, как настроить интеграцию **{{ productName }}** и Telegram-бота.

Telegram-бот будет представлять собой проект в Visual Studio на языке C# (Windows Forms Application).

Скачайте готовый проект Visual Studio с исходным кодом бота по ссылке: [TelegramBotComindwareIntegration.zip](https://kb.comindware.ru/file.php?id=191)

Также можно воспользоваться аналогичным кодом на языке Python в файле `TelegramBotComplete.py` по ссылке: [TelegramBotComindwareIntegrationPython.zip](https://kb.comindware.ru/file.php?id=193)

## Прикладная задача

Требуется создать Telegram-бот, в котором пользователь мог бы взаимодействовать с **{{ productName }}**.

Перед использованием бота пользователь должен пройти авторизацию следующим образом:

- При первом обращении бот запрашивает в адрес эл. почты пользователя.
- Бот ищет аккаунт с указанным адресом в **{{ productName }}**.
- Если аккаунт найден:
  - бот высылает 4-значный код авторизации на эл. почту пользователя с помощью процесса в **{{ productName }}**;
  - бот запрашивает код  авторизации у пользователя в чате
- Если пользователь указывает верный код авторизации, авторизация считается пройденной.

## Алгоритм авторизации

- На сервере выполняется бот, передающий данные между API Telegram и API **{{ productName }}**.
- Пользователь пишет боту сообщение в Telegram.
- Бот предлагает пользователю авторизоваться, указав адрес эл. почты, с которым пользователь зарегистрирован в **{{ productName }}**.
- Пользователь сообщает боту свой адрес эл. почты.
- Бот отправляет ***GET***-запрос в **{{ productName }}** для получения данных аккаунтов в Системе.
- Бот получает ***JSON***-ответ с данными аккаунтов и ищет среди них аккаунт с указанным адресом эл. почты.
- Если аккаунт найден, выполняется следующая процедура:
  - Бот генерирует 4-значный код авторизации.
  - Бот записывает код авторизации в атрибут аккаунта с помощью ***POST***-запроса.
  - С помощью ***POST***-запроса бот отправляет эл. письмо пользователю с кодом авторизации.
  - Пользователь указывает Telegram-боту код авторизации, полученный из эл. письма
- Если код, записанный в **{{ productName }}** и полученный ботом в последнем сообщении совпадают, авторизация считается пройденной.
- После прохождения авторизации пользователь может посредством бота инициировать действия в  **{{ productName }}**.

Примечание

На основе созданного промежуточного ПО и примера настройки взаимодействия бота с **{{ productName }}** можно в дальнейшем реализовать различные сценарии: подача заявок, заявлений на отпуск, запрос какой-либо информации из системы и т.д.

## Предварительная настройка со стороны {{ productName }}

1. Создайте шаблон аккаунта *«Sotrudniki»* (с таким же системным именем). В этом шаблоне уже есть системные атрибуты, такие как имя, почта и т.д.
2. Добавьте атрибут *«ChatID»* типа «**Текст**» (в нашем примере ID атрибута — *op.13*).
3. Добавьте атрибут *«Proverochnyykod»* типа «**Текст**» (в нашем примере ID атрибута — *op.14*).
4. Создайте и настройте шаблон процесса для отправки эл. почты пользователю (в нашем примере ID шаблона — *pa.3*).

   - В связанном с шаблоном процесса шаблоне записи создайте два атрибута типа «**Текст**»:

     - *Код* (в нашем примере ID атрибута — *op.23*) — значение этого атрибута процесс должен отправлять пользователю;
     - *Кому* (в нашем примере ID атрибута — *op.24*) — адрес, на который процесс должен отправлять код.

Примечание

В исходном коде промежуточного ПО замените ID и системные имена атрибутов и шаблонов на фактически используемые.

## Настройка интеграции

1. В Telegram найдите BotFather (<https://t.me/BotFather>) и запросите у него создание бота. Подробные инструкции см. в [официальной документации Telegram](https://core.telegram.org/api).
2. Скачайте и распакуйте проект для Visual Studio с промежуточным ПО по ссылке: [TelegramBotComindwareIntegration.zip](https://kb.comindware.ru/file.php?id=191)
3. Восстановите библиотеки с помощью команды Restore NuGet Packages: Newtonsoft.Json, RestSharp, Telegram.Bot и Telegram.bot.Extensions.Polling.
4. При необходимости установите пакет .Net SDK 3.1.
5. Откройте файл `MainWindow.xaml` с формой приложения.
6. Замените в разделе `Grid` значения атрибутов `Text` на фактические значения:

   ```
   <Grid>
       <Grid.RowDefinitions>
           <RowDefinition Height="0.5*"/>
           <RowDefinition/>
           <RowDefinition/>
           <RowDefinition/>
           <RowDefinition/>
       </Grid.RowDefinitions>
       <Button  Width="150" Height="30"  Click="Button_Click" Grid.Row="0">Старт</Button>
       <StackPanel Grid.Row="1">
           <Label Height="25" Margin="10,5,0,5">Токен API Telegram-бота</Label>
           <TextBox x:Name="apitoken" Text="введите токен API своего Telegram-бота" Width="240" Height="25"/>
       </StackPanel>
       <StackPanel Grid.Row="2">
           <Label Height="25" Margin="10,5,0,5">Путь к API {{ productName }}</Label>
           <TextBox x:Name="Apipath" Text="http://yourinstance/api/public/" Width="240" Height="25" />
       </StackPanel>
       <StackPanel Grid.Row="3">
           <Label Height="25" Margin="10,5,0,5">Имя пользователя</Label>
           <TextBox x:Name="login" Text="введите имя пользователя, у которого есть доступ к API  {{ productName }}" Width="240" Height="25" />
       </StackPanel>
       <StackPanel Grid.Row="4">
           <Label Height="25" Margin="10,5,0,5">Пароль</Label>
           <PasswordBox x:Name="password" Password="введите пароль пользователя API  {{ productName }}" Width="240" Height="25" />
       </StackPanel>
   </Grid>
   ```
7. Откройте файл `MainWindow.xaml.cs` с исходным кодом проекта и вставьте в него приведённый ниже код.

   ```
   using System.Windows;
   using System;
   using System.Threading;
   using System.Threading.Tasks;
   using Telegram.Bot;
   using Telegram.Bot.Extensions.Polling;
   using Telegram.Bot.Types;

   namespace Telegram
   {
       public partial class MainWindow : Window
       {
           static ITelegramBotClient bot;

           public MainWindow()
           {
               InitializeComponent();
           }

           private void Button_Click(object  sender, RoutedEventArgs e)
           {
               bot = new TelegramBotClient(apitoken.Text);
               var cts =   new   CancellationTokenSource();
               var cancellationToken = cts.Token;
               var receiverOptions =   new   ReceiverOptions
               {
                   AllowedUpdates = { }, // receive all update types
               };
               bot.StartReceiving(
                   HandleUpdateAsync,
                   HandleErrorAsync,
                   receiverOptions,
                   cancellationToken
               );
               MessageBox.Show("Бот запущен");
           }

           public async Task HandleUpdateAsync(ITelegramBotClient botClient, Update update, CancellationToken cancellationToken)
           {
               try
               {
                   if (update.Type == Telegram.Bot.Types.Enums.UpdateType.Message)
                   {
                       var message = update.Message;
                       await bot.SendTextMessageAsync(message.Chat.Id,   "Вы написали мне: "   + message.Text, Telegram.Bot.Types.Enums.ParseMode.Markdown);
                   }
               }catch { }
           }

           public async Task HandleErrorAsync(ITelegramBotClient botClient, Exception exception, CancellationToken cancellationToken)
           {
               MessageBox.Show("Ошибка " + exception.Message);
           }
       }}
   ```
8. Сохраните файл.
9. Скомпилируйте и запустите приложение.
10. В окне приложения нажмите кнопку *«Старт»* и подтвердите запуск ПО.
11. Напишите в Telegram-бот сообщение, например: «*Привет».*
12. Бот должен ответить: «*Вы написали мне:* *Привет»*.

    Примечание

    Вы можете воспользоваться аналогичным кодом простейшей реализации бота на языке Python из файла `TelegramBotPrimer.py` по ссылке: [TelegramBotComindwareIntegrationPython.zip](https://kb.comindware.ru/file.php?id=193)

    ![Запуск бота](https://kb.comindware.ru/assets/img_664f1796168fe.png)

    Запуск бота
13. Для взаимодействия с **{{ productName }}** воспользуемся **[Solution API][api_solution]**.
14. Допишите `/Docs/SolutionApi/` в адресной строке браузера после адреса экземпляра **{{ productName }}**.
15. Отобразится страница Swagger с перечнем доступных методов **Solution API**.

    ![Переход в область SolutionApi](https://kb.comindware.ru/assets/telegram_bot1.png)

    Переход в область SolutionApi

    Примечание

    На последующих шагах используйте готовый исходный код ([TelegramBotComindwareIntegration.zip](https://kb.comindware.ru/file.php?id=191)) или копируйте приведённые ниже фрагменты кода.
16. Добавьте в файл `MainWindow.xaml.cs` две функции:

    - `Get()` будет делать ***GET***-запрос для получения данных из шаблона аккаунта *«Sotrudniki»*. Результатом будет ***JSON***-ответ.
    - `ValueFromJSON()` будет извлекать из этого ответа нужный атрибут. 

      ```
      private string Get(string  OA_system_name)
      {
          var client =   new   RestClient(Domain);
          client.Authenticator = new HttpBasicAuthenticator(Login, Password);
          var request =   new   RestRequest("solution/" + OA_system_name, Method.Get);
          request.AddHeader("Accept",   "application/json"  );
          var response = client.Execute(request);
          return response.Content;
      }

      private string ValueFromJSON(string  data,  string attribute_name, string  chat_id)
      {
          var doc = JsonDocument.Parse(data);
          JsonElement root = doc.RootElement;
          var users = root.EnumerateArray();
          while (users.MoveNext())
          {
              var user = users.Current;
              var props = user.EnumerateObject();
              string value_ =   ""  , chat_id_ = "";
              while (props.MoveNext())
              {
                  var prop = props.Current;
                  if (prop.Name.ToLower() == attribute_name.ToLower())
                  {
                      value_ = prop.Value.ToString();
                  }
                  if (prop.Name.ToLower() ==   "chatid"  )
                  {
                      chat_id_ = prop.Value.ToString();
                  }
              }
              if (chat_id_ == chat_id)
              {
                  return value_;
              }
          }
          return "";
      }
      ```
17. Теперь при запуске промежуточного ПО Telegram-бот запросит авторизацию.
18. Реализуем процесс авторизации следующим образом: если пользователь по ChatID не найден, то будем рассматривать 3 варианта:

    - сообщение содержит символ '@', следовательно в сообщении указат адрес эл. почты — запускаем процесс отправки 4-значного кода;
    - длина сообщения — 4 символа — проверка отправленного кода на соответствие;
    - во всех остальных случаях бот отвечает: *«Укажите адрес эл. почты для авторизации»*.
19. Добавьте в файл `MainWindow.xaml.cs` следующую функцию для обработки сообщений от пользователя.

    ```
    public async Task HandleUpdateAsync(ITelegramBotClient botClient, Update update, CancellationToken cancellationToken)
            {
                try
                {
                    if (update.Type == Telegram.Bot.Types.Enums.UpdateType.Message)
                    {
                        var message = update.Message;

                        string data = Get("Sotrudniki");
                        if (ValueFromJSON(data, "ChatID", message.Chat.Id.ToString()) == "")
                        {
                            if (message.Text.Contains("@"))
                            {
                                var doc = JsonDocument.Parse(data);
                                JsonElement root = doc.RootElement;
                                var users = root.EnumerateArray();
                                while (users.MoveNext())
                                {
                                    var user = users.Current;
                                    var props = user.EnumerateObject();
                                    string account_id = "", current_email = "";
                                    while (props.MoveNext())
                                    {
                                        var prop = props.Current;
                                        if (prop.Name.ToLower() == "mbox")
                                        {
                                            current_email = prop.Value.ToString();
                                        }
                                        if (prop.Name.ToLower() == "id")
                                        {
                                            account_id = prop.Value.ToString();
                                        }
                                    }
                                    if (current_email.ToLower() == message.Text.ToLower())
                                    {
                                        var symbols = "0123456789";
                                        string code = "";
                                        var random =   new   Random();
                                        for (  int   i = 0; i < 4; i++)
                                        {
                                            code += symbols[random.Next(symbols.Length)].ToString();
                                        }
                                        // найденному пользователю в системе проставим ChatID с пометкой _NA (т.е. не авторизован)
                                        // и сгенерированный 4-х значный код
                                        var data_ =   new   Dictionary<string,   object  >
                                            {
                                                {"op.13", message.Chat.Id.ToString() + "_NA"},//ChatId
                                                {"op.14", code}//Proverochnyykod
                                            };
                                        var client =   new   RestClient(Domain);
                                        client.Authenticator = new HttpBasicAuthenticator(Login, Password);
                                        var request =   new   RestSharp.RestRequest("system/TeamNetwork/ObjectService/Edit", Method.Post); // POST-запрос к найденному пользователю для обновления данных
                                        request.AddHeader("content-type", "application/json");
                                        var sendData =   new   Dictionary<string,   object  >
                                        {
                                            {"objectId", account_id},
                                            {"objectData", data_ }
                                        };
                                        request.AddParameter("application/json", JsonSerializer.Serialize(sendData), ParameterType.RequestBody);
                                        client.Execute(request);

                                        // запустим процесс отправки сгенерированного кода на email
                                        var data_for_proccess =   new   Dictionary<string,   object  >
                                            {
                                                {"op.23", code}, // Код
                                                {"op.24", current_email} // Кому
                                            };
                                        request = new RestSharp.RestRequest("system/Process/ProcessObjectService/Create1", Method.Post);
                                        request.AddHeader("content-type", "application/json");
                                        data_ = new Dictionary<string, object>
                                            {
                                                {"processAppId", "pa.3"}, // process_id
                                                {"objectName", null},
                                                {"syncActivityQuantity", 2},
                                                {"objectData", data_for_proccess}
                                            };
                                        request.AddParameter("application/json", JsonSerializer.Serialize(data_), ParameterType.RequestBody);
                                        client.Execute(request);

                                        await bot.SendTextMessageAsync(message.Chat.Id, "На указанную почту отправлено письмо с 4-значным кодом, введите его ниже для авторизации");
                                    }
                                }
                            }
                            else if (message.Text.Length == 4)
                            {
                                string value = ValueFromJSON(data, "Proverochnyykod", message.Chat.Id.ToString() + "_NA");
                                if (message.Text ==   value  )
                                {
                                    // у ChatID убираем пометку "_NA" и очищаем поле "Проверочный код"
                                    var data_ =   new   Dictionary<string,   object  >
                                        {
                                            {"op.13", message.Chat.Id.ToString()},//ChatId
                                            {"op.14", null}//Proverochnyykod
                                        };
                                    var client = new RestClient(Domain);
                                    client.Authenticator = new HttpBasicAuthenticator(Login, Password);
                                    value = ValueFromJSON(data, "id", message.Chat.Id.ToString() + "_NA");
                                    var request =   new   RestSharp.RestRequest("system/TeamNetwork/ObjectService/Edit", Method.Post);
                                    request.AddHeader("content-type", "application/json");
                                    var sendData =   new   Dictionary<string, object>
                                    {
                                        {"objectId", value},
                                        {"objectData", data_}
                                    };
                                    request.AddParameter("application/json", JsonSerializer.Serialize(sendData), ParameterType.RequestBody);
                                    client.Execute(request);
                                    await bot.SendTextMessageAsync(message.Chat.Id, "Вы успешно авторизованы");
                                }
                            }
                            else
                            {
                                await bot.SendTextMessageAsync(message.Chat.Id, "Укажите адрес эл. почты для авторизации");
                            }
                        }
                        else
                        {
                            string name = ValueFromJSON(data, "fullName", message.Chat.Id.ToString());
                            await bot.SendTextMessageAsync(message.Chat.Id, "Добрый день, " + name + "! Вы успешно авторизованы");
                        }
                    }
                }
                catch { }
            }

            public async Task HandleErrorAsync(ITelegramBotClient botClient, Exception exception, CancellationToken cancellationToken)
            {
                MessageBox.Show("Ошибка " + exception.Message);
            }
    ```
20. Протестируйте работу промежуточного ПО и Telegram-бота.

    ![Авторизация через бот](https://kb.comindware.ru/assets/img_664f17cea8721.png)

    Авторизация через бот

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
