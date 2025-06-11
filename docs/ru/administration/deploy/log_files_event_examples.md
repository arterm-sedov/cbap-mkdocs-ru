---
title: Примеры событий в файловых журналах
kbId: 4618
---

{% if gostech %}
# Примеры событий в журналах {: #log_files_event_examples}
{% else %}
# Примеры событий в файловых журналах {: #log_files_event_examples}
{% endif %}

## Введение

Здесь представлены примеры событий и данных, которые регистрируются в журналах экземпляра ПО **{{ productName }}**. Названия событий даны согласно тре­бованиям по информацион­ной безопасно­сти, предъявляемым к Автоматизированным системам.

## Перечень событий

### Вход пользователя в систему

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000  username XXX.XXX.XXX.XXX http://SERVER_URL/Home/Login/?returnUrl=/ OK HH:mm:ss.SSS 'Builtin: user logged in'
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` – имя пользователя.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/Home/Login/?returnUrl=/` – адрес страницы входа.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `Builtin: user logged in` — описание события: «Способ аутентификации: Встроенная. Пользователь вошёл в систему».

### Выход пользователя из системы {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000  username XXX.XXX.XXX.XXX  http://SERVER_URL/Home/Logout/ OK HH:mm:ss.SSS 'User logout success' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/Home/Login/?returnUrl=/` — адрес страницы выхода.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `User logout success` — описание события: «Пользователь вышел из системы».

### Неуспешный вход пользователя в систему, неверное имя или неверный пароль при входе {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/Home/Login/?returnUrl=/Resolve OK HH:mm:ss.SSS '"Builtin": user login failed for "username"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000  XXX.XXX.XXX.XXX http://SERVER_URL/Home/Login/?failedLogin=InvalidLoginAndPassword&inputID=&returnUrl==%2fResolve   'GET' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/Home/Login/?returnUrl=/` — адрес страницы выхода.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `"Builtin": user login failed for "username"'` — описание события: «Способ аутентификации: Встроенная. Пользователь username не смог войти в систему».
- `http://SERVER_URL/Home/Login/?failedLogin=InvalidLoginAndPassword&inputID=&returnUrl==%2fResolve` — адрес страницы, отображающейся после неудачной попытки входа.
- `GET` — метод запроса.

### Создание учетной записи {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/UserApi/SetSystemInfo   'POST: "{"accountFormChanges":{"PasswordHash":"XXXXXX","OldPasswordHash":null,"DataformChanges":{"WidgetChanges":[{"ObjId":null,"TempId":"cmw.temp.21","TypeId":"cmw.account.Account","Changes": {"cmw.account.form.group0text1":{"Origin":4,"Literal":"FULL_NAME","Clean":null,"Time":1698153500360,"Add":null,"Rem":null,"StreamName":null,"StreamId":null,"Parent":null, "ClearParent":null,"Number":null,"Order":null,"ComplexValues":null}, "cmw.account.form.group0text2":{"Origin":4,"Literal":"USER_NAME","Clean":null,"Time":1698153505344,"Add":null,"Rem":null,"StreamName":null,","StreamId":null,"Parent":null, "ClearParent":null,"Number":null,"Order":null,"ComplexValues":null}, "cmw.account.form.group0text3":{"Origin":4,"Literal":"EMAIL","Clean":null,"Time":1698153518245,"Add":null,"Rem":null,"StreamName":null,"StreamId":null,"Parent":null, "ClearParent":null,"Number":null,"Order":null,"ComplexValues":null}},"CommandId":null,"CommandKind":2,"CommandContextChanges":null}],"ComplexObjectChanges":[]},"Id":"cmw.temp.21","IsActive":null,"IsAnonymous":null,"IsDisabled":null,"Language:"ru","AuthenticationMethod":0,"PasswordValidationParameters":null,"ProfilePhoto":null}}"' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, создавшего учётную запись.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/UserApi/SetSystemInfo` — путь к методу API для создания учётной записи.
- `POST` — тип запроса.
- `accountFormChanges` — тело запроса с данными учётной записи:
    - `"PasswordHash":"XXXXXX"` — хэш пароля.
    - `"DataformChanges":{"WidgetChanges":[{}]}` — поля формы учётной записи.
        - `"ObjId":"null"` — идентификатор временной записи.
        - `"TempId":"cmw.temp.ID"` — идентификатор временной записи.
        - `"TypeId":"cmw.account.Account"` — тип создаваемого объекта: учётная запись.
        - `"Changes":{}` — данные учетной записи.
            - `FULL_NAME` — Ф. И. О. пользователя.
            - `USER_NAME` — имя пользователя.
            - `EMAIL` — адрес эл.&nbsp;почты пользователя.

### Удаление учетной записи {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/UserApi/SetSystemInfo   'DELETE: "{"accountIds":["account.1", "account.2"]}"' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, удалившего учётную запись.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/UserApi/DeleteAccounts` — путь к методу API для удаления учётной записи.
- `DELETE` — тип запроса.
- `{"accountIds":["account.1", "account.2"]}` – тело запроса:
    - `accountIds` — массив идентификаторов удалённых аккаунтов.
    - `account.1`, `account.2`  — идентификаторы аккаунтов.

### Неуспешное создание учетной записи {: .pageBreakBefore }

**Пример события**

``` {: .log .pageBreakAfter .pageBreakInsideAvoid title="Неуспешное создание учётной записи. Пример события" }
-MM-dd HH:mm:ss,SSS ERROR 00000000-0000-0000-0000-000000000000 username SERVER_URL PORT XXX.XXX.XXX.XXX  Core HH:mm:ss.SSS X.X.XXX.X  '   Транзакция нарушает уникальность триплета:  cmw.account.mbox – email@<hostname>

Service name:

   "DataformService"

Method name:

   "ApplyChangesAndQueryData"

Parameters list:

   [0]: {"Changes":{"WidgetChanges":[{"ObjId":"cmw.temp.150","TempId":"cmw.temp.150","TypeId":"cmw.account.Account","Changes":{"cmw.account.form.group0text1":{"Origin":4,"Literal":"FULL_NAME","Time":1700833720019},"cmw.account.form.group0text2":{"Origin":4,"Literal":"USER_NAME","Time":1700833724427},"cmw.account.form.group0text3":{"Origin":4,"Literal":"EMAIL","Time":1700833711581}},"CommandKind":2}],"ComplexObjectChanges":[]},"Queries":[{"WiId":"cmw.account.form.root","QueryChildWidgets":true,"Widgets":[],"QueryObjectTitle":true,"QueryObjectToolbar":true,"TempId":"cmw.temp.150","RootTempId":"cmw.temp.150"}]}

Stack:

  at Comindware.LogicsStorage.Core.Managers.StatementManagers.StatementManagerOneToOneOneToOneUnique.
  ReplaceStatement[TSubject,TValue] (Comindware.LogicsStorage.Api.Transaction transaction, TSubject subject, Comindware.LogicsStorage.Api.Predicate predicate, TValue value) [0x00093] in <7d85b33b773e45b1b9d638b93301c0e9>:0

  at Comindware.LogicsStorage.Core.Managers.StatementManagers.TransactionStatementManager.
  ReplaceStatement[TSubject,TValue] (Comindware.LogicsStorage.Api.Transaction transaction, TSubject subject, Comindware.LogicsStorage.Api.Predicate predicate, TValue value) [0x00011] in <7d85b33b773e45b1b9d638b93301c0e9>:0

  at Comindware.LogicsStorage.Core.Managers.StatementManager.ReplaceStatement[TSubject,TValue] (Comindware.LogicsStorage.Api.Transaction transaction, TSubject subject, Comindware.LogicsStorage.Api.Predicate predicate, TValue value) [0x00000] in <7d85b33b773e45b1b9d638b93301c0e9>:0

  at Comindware.LogicsStorage.Api.TransactionExtensions.ReplaceStatement[TValue] (Comindware.LogicsStorage.Api.Transaction transaction, Comindware.LogicsStorage.Api.Identity subject, Comindware.LogicsStorage.Api.Identity predicate, TValue value) [0x0001f] in <7d85b33b773e45b1b9d638b93301c0e9>:0

  at Comindware.TeamNetwork.Core.Services.PropertyPathWriter.WriteValue[TData] (Comindware.LogicsStorage.Api.Identity qContextObject, System.String[] path, System.Object value, System.String qWidget) [0x00199] in <8025f5369894426089cefdaa59a4c743>:0
{% if pdfOutput %}
```

``` {: .log title="Неуспешное создание учётной записи. Пример события — продолжение" .pageBreakBefore}
{% endif %}
  at Comindware.TeamNetwork.Core.Services.WidgetsDataWriter.WriteLiteral (Comindware.LogicsStorage.Api.Identity qObject, Comindware.TeamNetwork.Core.Services.PropertyPathWriter writer, Comindware.TeamNetwork.Api.Data.DataSourceInfo ds, System.Object value, System.String widget) [0x000c8] in <8025f5369894426089cefdaa59a4c743>:0

  at Comindware.TeamNetwork.Core.Services.WidgetsDataWriter.ApplyWidgetValueChange (Comindware.TeamNetwork.Core.Services.PropertyPathWriter writer, Comindware.LogicsStorage.Api.Identity qObject, Comindware.LogicsStorage.Api.Identity qWidget, Comindware.TeamNetwork.Api.Data.Forms.WidgetValueChange wChange) [0x00185] in <8025f5369894426089cefdaa59a4c743>:0

  at Comindware.TeamNetwork.Core.Services.WidgetsDataWriter.ApplyWidgetChanges (Comindware.TeamNetwork.Core.Services.PropertyPathWriter writer, System.Collections.Generic.IList\`1[T] changes) [0x00170] in <8025f5369894426089cefdaa59a4c743>:0

  at Comindware.TeamNetwork.Core.Services.WidgetsDataWriter.ApplyChanges (Comindware.TeamNetwork.Api.Data.Forms.DataformChanges changes) [0x0023e] in <8025f5369894426089cefdaa59a4c743>:0

  at Comindware.TeamNetwork.Core.Services.DataformService.ApplyChangesAndQueryData (Comindware.TeamNetwork.Api.Data.Forms.DataformWidgetsQuery fQuery) [0x0002c] in <8025f5369894426089cefdaa59a4c743>:0

  at Castle.Proxies.Invocations.IDataformService_ApplyChangesAndQueryData.InvokeMethodOnTarget () [0x00018] in <9d46134a505745cbb2aa4c1a7704bca1>:0

  at Castle.DynamicProxy.AbstractInvocation.Proceed () [0x0002d] in <99e1b17afc2a44c5b97e5af224da0ae2>:0

  at Comindware.Platform.Core.Logging.ExceptionsInterceptor.Intercept (Castle.DynamicProxy.IInvocation invocation) [0x00000] in <13c6df997e3e467ca2451c9fd9f35e67>:0

 '
```

**Поля события**
{: .pageBreakBefore }

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `ERROR` — тип события: ошибка.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, создающего учётную запись.
- `SERVER_URL` — адрес сервера.
- `PORT` — порт сервера.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `Core` — наименование модуля, в котором произошло событие.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `X.X.XXX.X` — версия ПО {{ productName }}.
- `Транзакция нарушает уникальность триплета:  cmw.account.mbox - email@<hostname>` — описание события: неуникальный адрес эл.&nbsp;почты.
- `Service name: "DataformService"` — наименование службы, обрабатывавшей веб-запрос.
- `Method name: "ApplyChangesAndQueryData"` — наименование метода запроса.
- `Parameters list` — массив параметров запроса.
    - `"Changes":{}` — данные учётной записи.
        - `"WidgetChanges":[{}]` — массив полей формы учётной записи.
        - `"ObjId":"cmw.temp.ID"` — идентификатор временной записи.
        - `"TempId":"cmw.temp.150"` — идентификатор временной записи.
        - `"TypeId":"cmw.account.Account"` — тип создаваемого объекта: учётная запись.
        - `FULL_NAME` — Ф. И. О. пользователя.
        - `USER_NAME` — имя пользователя.
        - `EMAIL` — адрес эл.&nbsp;почты пользователя.
- `Stack` — данные функций, обрабатывавших веб-запрос.

### Неуспешное удаление учетной записи {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS ERROR 00000000-0000-0000-0000-000000000000 username SERVER_URL PORT XXX.XXX.XXX.XXX  Core HH:mm:ss.SSS X.X.XXX.X  '   Вы не можете удалить свой аккаунт

Service name:

   "AccountService"

Method name:

   "Delete"

Parameters list:

   [0]: ["account.1", "account.2"]

Stack:

  at Comindware.Platform.Core.Services.AccountService.Delete (System.String[] accountsIds) [0x00104] in <13c6df997e3e467ca2451c9fd9f35e67>:0

  at Castle.Proxies.Invocations.IAccountService_Delete.InvokeMethodOnTarget () [0x00018] in <9d46134a505745cbb2aa4c1a7704bca1>:0

  at Castle.DynamicProxy.AbstractInvocation.Proceed () [0x0002d] in <99e1b17afc2a44c5b97e5af224da0ae2>:0

  at Comindware.Platform.Core.Logging.ExceptionsInterceptor.Intercept (Castle.DynamicProxy.IInvocation invocation) [0x00000] in <13c6df997e3e467ca2451c9fd9f35e67>:0

 '
```

**Поля события**
{: .pageBreakBefore }

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `ERROR` — тип события: ошибка.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, удаляющего учётную запись.
- `SERVER_URL` — адрес сервера.
- `PORT` — порт сервера.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `Core` — наименование модуля, в котором произошло событие.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `X.X.XXX.X` — версия ПО {{ productName }}.
- `Вы не можете удалить свой аккаунт` — описание события.
- `Service name: "AccountService"` — наименование службы, обрабатывавшей веб-запрос.
- `Method name:` " `Delete`" — наименование метода запроса.
- `Parameters list` — массив параметров запроса.
    - `["account.1", "account.2"]` — массив идентификаторов аккаунтов, выбранных для удаления.
- `Stack` — данные функций, обрабатывавших веб-запрос.

### Блокировка (отключение) учетной записи {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/Dataform/QueryData   'POST: "{"query":{"Changes":{"WidgetChanges":[{"ObjId":"account.ID","TypeId":"cmw.account.Account","Changes":{"cmw.account.form.group2flag1":{"Origin":4,"Literal":false,"Time":1698244978684}},"CommandKind":3}],"ComplexObjectChanges":[]},"Queries":[{"WiId":"cmw.account.form.root","QueryChildWidgets":true,"Widgets":[],"QueryObjectTitle":true,"QueryObjectToolbar":true,"ObjId":"account.ID","RootObjId":"account.ID"}]}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/Dataform/QueryData OK HH:mm:ss.SSS 'POST completed'
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/Dataform/QueryData`  — путь к методу API для изменения данных учётной записи.
- `POST` — тип запроса.
- `query` — тело запроса с данными учётной записи.
    - `"ObjId":"account.ID"` — идентификатор учётной записи.
    - `"TypeId":"cmw.account.Account"` — тип объекта: учётная записи.
    - `"Changes":{"cmw.account.form.group2flag1":{"Origin":4,"Literal":false,"Time":1698244978684}}` — отключение учётной записи: `"Literal":false`.
    - `"ObjId":"account.ID"` — идентификатор временной записи.
    - `"RootObjId":"account.ID"` — идентификатор временной записи.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `POST completed` — результат обработки запроса: выполнен.

### Разблокировка (включение) учетной записи {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/Dataform/QueryData   'POST: "{"query":{"Changes":{"WidgetChanges":[{"ObjId":"account.ID","TypeId":"cmw.account.Account","Changes":{"cmw.account.form.group2flag1":{"Origin":4,"Literal":true,"Time":1698245267640}},"CommandKind":3}],"ComplexObjectChanges":[]},"Queries":[{"WiId":"cmw.account.form.root","QueryChildWidgets":true,"Widgets":[],"QueryObjectTitle":true,"QueryObjectToolbar":true,"ObjId":"account.ID","RootObjId":"account.ID"}]}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/Dataform/QueryData OK HH:mm:ss.SSS 'POST completed'
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/Dataform/QueryData`  — путь к методу API для изменения данных учётной записи.
- `POST` — тип запроса.
- `query` — тело запроса с данными учётной записи.
    - `"WidgetChanges":[{}]` — поля формы учётной записи.
    - `"ObjId":"account.ID"` — идентификатор учётной записи.
    - `"TypeId":"cmw.account.Account"` — тип объекта: учётная запись.
    - `"Changes":{"cmw.account.form.group2flag1":{"Origin":4,"Literal":true,"Time":1698245267640}}` — включение учётной записи: `"Literal":true`.
    - `"RootObjId":"account.ID"` — идентификатор временной записи.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `POST completed` — результат обработки запроса: выполнен.

### Смена пароля учетной записи {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/UserApi/SetSystemInfo   'POST: "{"accountFormChanges":{"PasswordHash":"XXXXXXX","OldPasswordHash":null,"DataformChanges":{"WidgetChanges":[{"ObjId":"account.ID","TempId":null,"TypeId":"cmw.account.Account","Changes":{"cmw.account.form.group2flag1":{"Origin":4,"Literal":true,"Clean":null,"Time":1698245267640,"Add":null,"Rem":null,"StreamName":null,"StreamId":null,"Parent":null, "ClearParent":null,"Number":null,"Order":null,"ComplexValues":null}},"CommandId":null,"CommandKind":3,"CommandContextChanges":null}], "ComplexObjectChanges":[]},"Id":"account.ID","IsActive":null,"IsAnonymous":null,"IsDisabled":null,"Language":null,"AuthenticationMethod":0,"PasswordValidationParameters":null,"ProfilePhoto":null}}"' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, создавшего учётную запись.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/UserApi/SetSystemInfo` — путь к методу API для создания учётной записи.
- `POST` — тип запроса.
- `accountFormChanges` — тело запроса с данными учётной записи:
    - `"PasswordHash":"XXXXXXX"` — хэш нового пароля.
    - `"DataformChanges":{"WidgetChanges":[{}]}` — поля формы учётной записи.
    - `"TypeId":"cmw.account.Account"` — тип объекта: учётная запись.
    - `"Changes":{}` — данные учётной записи.
        - `"ObjId":"account.ID"` — идентификатор учётной записи.
        - `"Id":"account.ID"` — идентификатор учётной записи.

### Создание роли {: .pageBreakBefore}

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/Members/GetMembersData 200 03:00:00 'POST completed' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Post   'POST: "{"role":{"Name":"Role Name","Alias":"RoleSystemName","Solution":"sln.1", "Members":[],"IsActive":true,"RoleType":0}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Post OK HH:mm:ss.SSS 'POST completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, создавшего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/RolesCollectionApi/Post` — путь к методу API для создания роли.
- `POST` — тип запроса.
- `role` — тело запроса с данными роли.
    - `"Name":"Role Name"` — название роли.
    - `"Alias":"RoleSystemName"` — системное имя роли.
    - `"Solution":"sln.1"` — идентификатор приложения, в котором создана роль.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `POST` completed — результат обработки запроса: выполнен.

### Создание группы пользователей {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/GroupApi/Post   'POST: "{"group":{"HoldMembersActive":false,"HoldMembersEnabled":false,"Users":[], "MemberOf":[],"Name":"Group Name","Origin":1}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/GroupApi/Post OK HH:mm:ss.SSS 'POST completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, создавшего группу.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/GroupApi/Post` — путь к методу API для создания группы.
- `POST` — тип запроса.
- `group` — тело запроса с данными группы.
    - `"Name":"Group Name"` — название группы.
    - `"MemberOf":[]` — массив идентификаторов родительских групп.
    - `"Users":[]` — массив идентификаторов учётных записей, входящих в группу.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `POST` completed — результат обработки запроса: выполнен.

### Удаление роли {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Delete   'DELETE: "{"rolesIds":["role.1","role.2"]}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Delete NoContent HH:mm:ss.SSS 'DELETE completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, удалившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/RolesCollectionApi/Delete` — путь к методу API для удаления роли.
- `DELETE` — тип запроса.
- `{"rolesIds":["role.1","role.2"]}` — тело запроса:
    - `"rolesIds"` — массив идентификаторов ролей, подлежащих удалению.
    - `"role.1","role.2"` — идентификаторы ролей.
- `NoContent` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `DELETE completed` — результат обработки запроса: выполнен.

### Удаление группы пользователей {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/GroupApi/Delete   'DELETE: "{"ids":["group.1","group.2"]}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/GroupApi/Delete NoContent HH:mm:ss.SSS 'DELETE completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, удалившего группу.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- http://`SERVER_URL`/api/GroupApi/`Delete` — путь к методу API для удаления группы.
- `DELETE` — тип запроса.
- `{"ids":["group.1","group.2"]}` — тело запроса.
    - `"ids"` — массив идентификаторов групп, подлежащих удалению.
    - `"group.1","group.2"` —идентификаторы групп.
- `NoContent` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `DELETE completed` — результат обработки запроса: выполнен.

### Изменение прав группы (роли) пользователей {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'PUT: "{"role":{"Id":"role.ID","Name":"Role Name","Alias":"RoleSystemName","Workspace":{"Id":"workspace.1","Name":"Workspace Name"},"Solution":"sln.1","Creator":"account.6","CreationDate":"2023-10-25T17:58:03+00:00","LastWriteDate":"2023-10-25T17:58:03+00:00", "Members":["account.ID","account.ID"],"IsActive":true,"IsPredefined":false,"RoleType":1,"RootResource":{"Name":"Системное приложение","Description":"","Children":[{"Name":"Organizational unit template","Children":[{"Name":"All records","Children":[],"Target":"lst.13","TargetType":14,"Privileges":4,"AvailablePrivileges":4}],"Target":"os.1","TargetType":22,"Privileges":132,"AvailablePrivileges":204}],"Target":"sln.1","TargetType":4,"Privileges":204,"AvailablePrivileges":716},"CreatorName":"Full Name"}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Read","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"systemSolution", "ResourceType":"BusinessApp"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Create","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"systemSolution", "ResourceType":"BusinessApp"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Update","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[systemSolution] RecordTemplateName", "ResourceType":"RecordTemplate"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Delete","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"systemSolution", "ResourceType":"BusinessApp"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Delete","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[systemSolution] systemSolution_OrganizationalStructure", "ResourceType":"OrgStructureTemplate"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Read","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[systemSolution_OrganizationalStructure] defaultList", "ResourceType":"List"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put OK HH:mm:ss.SSS 'PUT completed' ''
```

**Поля события**
{: .pageBreakBefore }

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/RolesCollectionApi/Put` — путь к методу API для изменения роли.
- `PUT` — тип запроса.
- `role` — тело запроса:
    - `"Id":"role.ID"` — идентификатор роли.
    - `"Name":"Role Name"` — название роли.
    - `"Alias":"RoleSystemName"` — системное имя роли.
    - `"Workspace":{"Id":"workspace.ID","Name":"Workspace Name"}` — свойства раздела навигации, к которому привязана системная роль.
    - `"Solution":"sln.ID"` — идентификатор приложения.
    - `"IsPredefined":false` — непредустановленная роль.
    - `"RoleType":1` — тип роли:
        - 0 — системная стандартная.
        - 1 — роль в приложении.
        - 2 — системная пользовательская.
        - `"Members":[]` — массив идентификаторов учётных записей и групп, входящих в роль.
    - `"RootResource":{}` — приложение, к ресурсам которого роль задаёт разрешения.
    - `"Children":[{"Name":"Resource name","Children":[],"Target":"resource.ID","TargetType":XX,"Privileges":XXX, "AvailablePrivileges":XXX}]`— массив ресурсов, к которым роль задаёт разрешения:
        - `"Target":"resource.ID"` — идентификатор ресурса.
        - `"TargetType":XX` — код типа ресурса.
        - `"Privileges":XXX` — код установленных разрешений.
        - `"AvailablePrivileges":XXX` — код доступных разрешений.
- `Разрешение добавлено в роль` — описание события.
- `'{"Privilege":"Read","Role":"[applicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'` — тело запроса:
    - `"Privilege":"Read"` — тип добавленного разрешения:
        - `Create` — создание.
        - `Delete` — удаление.
        - `Read` — чтение.
        - `Update` — запись.
    - `"Role":"[ApplicationSystemName] RoleSystemName"` — свойства роли:
        - `ApplicationSystemName` — системное имя приложения.
        - `RoleSystemName` — системное имя роли.
    - `"RoleType":"BusinessApp"` — тип роли:
        - `BusinessApp` — роль в приложении.
        - `System` — системная.
    - `"Resource":"[ParentSystemName] ResourceSystemName"` путь к ресурсу, на доступ к которому предоставлено разрешение:
        - `parentSystemName` — системное имя родительского ресурса.
        - `ResourceSystemName` — системное имя ресурса.
    - `"ResourceType":"RecordTemplate"` — тип ресурса, на доступ к которому предоставлено разрешение:
        - `BusinessApp` — приложение.
        - `ChangeJournal` — журнал изменений.
        - `From` — форма.
        - `List` — таблица.
        - `OrgStructureTemplate` — шаблон оргединицы.
        - `Operation` — кнопка.
        - `ProcessTemplate` — шаблон процесса.
        - `RecordTemplate` — шаблон записи.
        - `RoleTemplate` — шаблон роли.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `PUT completed` — результат обработки запроса: выполнен.

### Включение пользователя в состав группы (роли) {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'PUT: "{"role":{"Id":"role.26","Name":"ТЕст","Alias":"TEst","Workspace":{"Id":"workspace.1","Name":"Workspace Name"},"Solution":"sln.1","Creator":"account.6","CreationDate":"2023-10-25T17:58:03+00:00","LastWriteDate":"2023-10-25T20:15:39+00:00", "Members":["account.194"],"IsActive":true,"IsPredefined":false,"RoleType":1,"RootResource":{"Id":"rrpd.2329","Name":"Application name","Role":"role.26","Children":[{"Name":"Resource name","Children":[],"Target":"oa.89","TargetType":20,"Privileges":76,"AvailablePrivileges":719},{"Id":"rrpd.2330","Name":"Organizational unit template","Role":"role.26","Children":[{"Id":"rrpd.2331","Name":"All records","Role":"role.26","Children":[],"Target":"lst.13","TargetType":14,"Privileges":4,"AvailablePrivileges":4}],"Target":"os.1","TargetType":22,"Privileges":132,"AvailablePrivileges":204}],"Target":"sln.1","TargetType":4,"Privileges":204,"AvailablePrivileges":716},"CreatorName":"Full Name"}}' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение удалено из роли' '{"Privilege":"Delete","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put OK HH:mm:ss.SSS 'PUT completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/RolesCollectionApi/Put` — путь к методу API для изменения роли.
- `PUT` — тип запроса.
- `role` — тело запроса:
    - `"Id":"role.ID"` — идентификатор роли.
    - `"Name":"Role Name"` — название роли.
    - `"Alias":"RoleSystemName"` — системное имя роли.
    - `"Workspace":{"Id":"workspace.ID","Name":"Workspace Name"}` — свойства раздела навигации, к которому привязана системная роль.
    - `"Solution":"sln.ID"` — идентификатор приложения.
    - `"IsPredefined":false` — непредустановленная роль.
    - `"RoleType":1` — тип роли:
        - 0 — системная стандартная.
        - 1 — роль в приложении.
        - 2 — системная пользовательская.
        - `"Members":[]` — массив идентификаторов учётных записей и групп, входящих в роль.
    - `"RootResource":{}` — приложение, к ресурсам которого роль задаёт разрешения.
    - `"Children":[{"Name":"Resource name","Children":[],"Target":"resource.ID","TargetType":XX,"Privileges":XXX, "AvailablePrivileges":XXX}]`— массив ресурсов, к которым роль задаёт разрешения:
        - `"Target":"resource.ID"` — идентификатор ресурса.
        - `"TargetType":XX` — код типа ресурса.
        - `"Privileges":XXX` — код установленных разрешений.
        - `"AvailablePrivileges":XXX` — код доступных разрешений.
- `Разрешение добавлено в роль` — описание события.
- `'{"Privilege":"Read","Role":"[applicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'` — тело запроса:
    - `"Privilege":"Read"` — тип добавленного разрешения:
        - `Create` — создание.
        - `Delete` — удаление.
        - `Read` — чтение.
        - `Update` — запись.
    - `"Role":"[ApplicationSystemName] RoleSystemName"` — свойства роли:
        - `ApplicationSystemName` — системное имя приложения.
        - `RoleSystemName` — системное имя роли.
    - `"RoleType":"BusinessApp"` — тип роли:
        - `BusinessApp` — роль в приложении.
        - `System` — системная.
    - `"Resource":"[ParentSystemName] ResourceSystemName"` путь к ресурсу, на доступ к которому предоставлено разрешение:
        - `parentSystemName` — системное имя родительского ресурса.
        - `ResourceSystemName` — системное имя ресурса.
    - `"ResourceType":"RecordTemplate"` — тип ресурса, на доступ к которому предоставлено разрешение:
        - `BusinessApp` — приложение.
        - `ChangeJournal` — журнал изменений.
        - `From` — форма.
        - `List` — таблица.
        - `OrgStructureTemplate` — шаблон оргединицы.
        - `Operation` — кнопка.
        - `ProcessTemplate` — шаблон процесса.
        - `RecordTemplate` — шаблон записи.
        - `RoleTemplate` — шаблон роли.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `PUT completed` — результат обработки запроса: выполнен.

### Исключение пользователя из состава группы (удаление роли) {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/Members/GetMembersData   'POST: "{"model":{"FilterType":3,"Selected":["account.ID"]}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/Members/GetMembersData 200 03:00:00 'POST completed' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'PUT: "{"role":{"Id":"role.ID","Name":"Role Name","Alias":"RoleSystemName","Workspace":{"Id":"workspace.1","Name":"Workspace Name"},"Solution":"sln.1","Creator":"account.6","CreationDate":"2023-10-25T17:58:03+00:00","LastWriteDate":"2023-10-25T17:58:03+00:00", "Members":["account.ID","account.ID"],"IsActive":true,"IsPredefined":false,"RoleType":1,"RootResource":{"Name":"Системное приложение","Description":"","Children":[{"Name":"Organizational unit template","Children":[{"Name":"All records","Children":[],"Target":"lst.13","TargetType":14,"Privileges":4,"AvailablePrivileges":4}],"Target":"os.1","TargetType":22,"Privileges":132,"AvailablePrivileges":204}],"Target":"sln.1","TargetType":4,"Privileges":204,"AvailablePrivileges":716},"CreatorName":"Full Name"}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Аккаунт удален из роли' '{"User":"username","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put OK HH:mm:ss.SSS 'PUT completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/Members/GetMembersData`— путь к методу API для получения идентификатора учётной записи участника роли.
- `POST` — тип запроса.
- `{"model":{"FilterType":3,"Selected":["account.ID"]}}` — тело запроса:
    - `"FilterType":3` — тип фильтра учётных записей:
        - 1 — только учётные записи.
        - 2 — только группы.
        - 3 — учётные записи и группы.
    - `"Selected":["account.ID"]` — массив идентификаторов исключённых учётных записей.
- `http://SERVER_URL/api/RolesCollectionApi/Put` — путь к методу API для изменения роли.
{: .pageBreakBefore }
- `PUT` — тип запроса.
- `Role` — тело запроса:
    - `"Id":"role.ID"` — идентификатор роли.
    - `"Name":"Role Name"` — название роли.
    - `"Alias":"RoleSystemName"` — системное имя роли.
    - `"Workspace":{"Id":"workspace.ID","Name":"Workspace Name"}` — свойства раздела навигации, к которому
    - `"Solution":"sln.ID"` — идентификатор приложения.
    - `"IsPredefined":false` — непредустановленная роль.
    - `"RoleType":1` — тип роли:
        - 0 — системная предустановленная.
        - 1 — роль в приложении.
        - 2 — системная непредустановленная.
        - `"Members":["account.ID","account.ID"]` — массив идентификаторов учётных записей и групп, входящих в роль.
    - `"RootResource":{}` — объект корневого ресурса, к которому роль задаёт разрешения: приложение.
    - `"Children":[{}]` — массив объектов с ресурсами, к которым роль задаёт разрешения.
- Аккаунт удален из роли — описание события.
- `'{"User":"username","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp"}'` — тело запроса:
    - `"User":"username"` — имя пользователя.
    - `"Role":"[ApplicationSystemName] RoleSystemName"` — свойства роли:
        - `ApplicationSystemName` — системное имя приложения.
        - `RoleSystemName` — системное имя роли.
    - `"RoleType":"BusinessApp"` — тип роли:
        - `BusinessApp` — роль в приложении.
        - `System` — системная роль.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `PUT` completed — результат обработки запроса: выполнен.

### Создание объекта {: .pageBreakBefore }

**Создание шаблона**

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/TemplatesApi/Create   'POST: "{"template":{"Alias":"TemplateSystemName","Name":"Template Name","IsDisabled":false,"Type":4,"Solution":"sln.ID","CreationDate":"0001-01-01T00:00:00","IsReferenceData":false, "IsTransferable":false,"ConversationDisplayConfig":{"DisableSidePanelConversations":true,"DisableWidgetConversations":true,"ProhibitedReferenceTypes":[],"HideArchivedMessages":false}}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/TemplatesApi/Create OK 03:00:00.296 'POST completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/TemplatesApi/Create` — путь к методу API для создания шаблона.
- `POST` — тип запроса.
- `"template":{}` — тело запроса с данными шаблона:
    - `"Alias":"TemplateSystemName"` — системное имя шаблона.
    - `"Name":"Template Name"` — название шаблона.
    - `"IsDisabled":false` — статус шаблона: включен (false) / отключен (true).
    - `"Type":4` — тип шаблона.
        - 3 — шаблон процесса.
        - 4 — шаблон записи.
        - 5 — шаблон аккаунта.
    - `"Solution":"sln.ID"` — идентификатор приложения, в котором создан шаблон.
    - `"CreationDate":"0001-01-01T00:00:00"` — дата создания шаблона.
    - `"IsReferenceData":false` — флаг «Шаблон является справочником».
    - `"IsTransferable":false` — флаг «Переносить данные шаблона при трансфере».
    - `"ConversationDisplayConfig":{}` — конфигурация обсуждений в шаблоне.

### Чтение объекта {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/TemplatesApi/Get/oa.91   'GET: "{"id":"oa.91"}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/TemplatesApi/Get/oa.91 OK 03:00:00 'GET completed' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/SolutionConfigurationApi/List   'GET' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/SolutionConfigurationApi/List OK HH:mm:ss.SSS 'GET completed' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RecordTypeContextApi?recordTypeId=oa.91   'GET: "{"recordTypeId":"oa.91"}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/TemplatesApi/GetUsages/oa.91   'GET: "{"id":"oa.91"}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/TemplatesApi/List   'POST: "{"filter":{"Type":0,"OnlyEnabled":true,"OnlyAdmin":false,"IncludeDocumentTemplates":false}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/TemplatesApi/GetUsages/oa.91 OK HH:mm:ss.SSS 'GET completed' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RecordTypeContextApi?recordTypeId=oa.91 OK HH:mm:ss.SSS 'GET completed' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/TemplatesApi/List OK 03:00:00.046 'POST completed' ''
```

**Поля события**
{: .pageBreakBefore }

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, считавшего объект.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.

**Чтение свойств шаблона записи**

- `http://SERVER_URL/api/TemplatesApi/Get/oa.ID` — путь к методу API для чтения шаблона записи.
- `http://SERVER_URL/api/RecordTypeContextApi?recordTypeId=oa.ID` — путь к методу API для чтения свойств шаблона записи.
- `oa.ID` — идентификатор шаблона записи.
- `GET` — тип запроса.
- `"{"id":"oa.ID"}"` — тело запроса с идентификатором шаблона.
- `OK` — статус обработки запроса.
- `hh:mm:ss` — длительность обработки запроса.
- `GET completed` — результат обработки запроса: выполнен.

**Чтение списка приложений**

- `http://SERVER_URL/api/SolutionConfigurationApi/List` — путь к методу API для чтения списка приложений на сервере.
- `GET` — тип запроса.
- `OK` — статус обработки запроса.
- `hh:mm:ss` — длительность обработки запроса.
- `GET completed` — результат обработки запроса: выполнен.

**Чтение списка шаблонов**

- `http://SERVER_URL/api/TemplatesApi/List` — путь к методу API для чтения списка шаблонов приложений.
- `POST` — тип запроса.
- `"filter":{}` — фильтр шаблонов.
- `OK` — статус обработки запроса.
- `hh:mm:ss` — длительность обработки запроса.
- `POST completed` — результат обработки запроса: выполнен.

**Чтение списка связанных шаблонов**
{: .pageBreakBefore }

- `http://SERVER_URL/api/TemplatesApi/GetUsages/oa.ID`— путь к методу API для чтения списка шаблонов, связанных с указанным шаблоном.
- `GET`— тип запроса.
- `{"id":"oa.ID"}` — тело запроса с идентификатором шаблона.
- `OK` — статус обработки запроса.
- `hh:mm:ss` — длительность обработки запроса.
- `GET completed` — результат обработки запроса: выполнен.

### Копирование объекта {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/FormDesigner/CloneRecordForm   'POST: "{"recordTypeId":"oa.91","cloningFormId":"form.3355","newName":"New Form Name","newAlias":"NewFormSystemName"}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/FormDesigner/CloneRecordForm 200 HH:mm:ss.SSS 'POST completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/FormDesigner/CloneRecordForm` — путь к методу API для копирования формы.
- `POST` — тип запроса.
- `{"recordTypeId":"oa.ID","cloningFormId":"form.ID","newName":"New Form Name","newAlias":"NewFormSystemName"}` — тело запроса:
- `"recordTypeId":"oa.ID"` — идентификатор шаблона записи.
    - `"cloningFormId":"form.ID"` — идентификатор исходной формы.
    - `"newName":"New Form Name"` — название новой формы.
    - `"newAlias":"NewFormSystemName"` — системное имя новой формы.
- `200` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `POST completed` — результат обработки запроса: выполнен.

### Изменение объекта {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RecordTypeContextApi   'POST: "{"property":{"Unique":false,"Obsolete":false,"Indexed":true,"Tracked":true,"DigitGrouping":true,"Calculated":false,"CalculateExpression":"","RecordTypeId":"oa.91","DisplayAttribute":false,"IgnoreUniqueErrors":false,"Type":0,"Format":29,"Name":"Attribute Name","Alias":"AttributeSystemName","IsSystem":false,"IsMultiValue":false,"IsMandatory":false, "IsOwnership":false,"PossibleValueExpression":""}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RecordTypeContextApi OK HH:mm:ss.SSS 'POST completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/RecordTypeContextApi` — путь к методу API для изменения атрибута шаблона.
- `POST` — тип запроса.
- `"property":{}` — тело запроса со свойствами атрибута:
    - `"RecordTypeId":"oa.ID"`— идентификатор шаблона записи, атрибут которого требуется изменить.
    - `"Name":"Attribute Name"` — название атрибута.
    - `"Alias":"AttributeSystemName"` — системное имя атрибута.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.

`POST completed` — результат обработки запроса: выполнен.

### Удаление объекта {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/RecordTypeContextApi/Delete/op.941   'DELETE: "{"id":"op.941"}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/RecordTypeContextApi/Delete/op.941 OK HH:mm:ss.SSS 'DELETE completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/RecordTypeContextApi/Delete/op.ID` — путь к методу API для удаления шаблона.
- `DELETE` — тип запроса.
- `{"id":"op.ID"}"` — тело запроса: идентификатор шаблона, подлежащего удалению.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `DELETE completed` — результат обработки запроса: выполнен.

### Установка прав доступа на объект {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'PUT: "{"role":{"Id":"role.26","Name":"Role Name","Alias":"RoleSystemName","Workspace":{"Id":"workspace.1","Name":"Workspace Name"},"Solution":"sln.1","Creator":"account.6","CreationDate":"2023-10-25T17:58:03+00:00","LastWriteDate":"2023-10-25T20:15:39+00:00", "Members":["account.194"],"IsActive":true,"IsPredefined":false,"RoleType":1,"RootResource":{"Id":"rrpd.2329","Name":"Application Name","Role":"role.26","Children":[{"Name":"Resource name","Children":[],"Target":"oa.89","TargetType":20,"Privileges":204,"AvailablePrivileges":719},{"Id":"rrpd.2330","Name":"Organizational unit template","Role":"role.26","Children":[{"Id":"rrpd.2331","Name":"All records","Role":"role.26","Children":[],"Target":"lst.13","TargetType":14,"Privileges":4,"AvailablePrivileges":4}],"Target":"os.1","TargetType":22,"Privileges":132,"AvailablePrivileges":204}],"Target":"sln.1","TargetType":4,"Privileges":204,"AvailablePrivileges":716},"CreatorName":"Full Name"}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Read","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Create","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Update","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение добавлено в роль' '{"Privilege":"Delete","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put OK HH:mm:ss.SSS 'PUT completed' ''
```

**Поля события**
{: .pageBreakBefore }

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/RolesCollectionApi/Put` — путь к методу API для изменения роли
- `PUT` — тип запроса.
- `role` — тело запроса:
    - `"Id":"role.ID"` — идентификатор роли.
    - `"Name":"Role Name"` — название роли.
    - `"Alias":"RoleSystemName"` — системное имя роли.
    - `"Workspace":{"Id":"workspace.ID","Name":"Workspace Name"}` — свойства раздела навигации, к которому привязана системная роль.
    - `"Solution":"sln.ID"` — идентификатор приложения.
    - `"IsPredefined":false` — непредустановленная роль.
    - `"RoleType":1` — тип роли:
        - 0 — системная стандартная.
        - 1 — роль в приложении.
        - 2 — системная пользовательская.
        - `"Members":[]` — массив идентификаторов учётных записей и групп, входящих в роль.
    - `"RootResource":{}` — приложение, к ресурсам которого роль задаёт разрешения.
    - `"Children":[{"Name":"Resource name","Children":[],"Target":"resource.ID","TargetType":XX,"Privileges":XXX, "AvailablePrivileges":XXX}]`— массив ресурсов, к которым роль задаёт разрешения:
        - `"Target":"resource.ID"` — идентификатор ресурса.
        - `"TargetType":XX` — код типа ресурса.
        - `"Privileges":XXX` — код установленных разрешений.
        - `"AvailablePrivileges":XXX` — код доступных разрешений.
- `Разрешение добавлено в роль` — описание события.
{: .pageBreakBefore }
- `'{"Privilege":"Read","Role":"[applicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'` — тело запроса:
    - `"Privilege":"Read"` — тип добавленного разрешения:
        - `Create` — создание.
        - `Delete` — удаление.
        - `Read` — чтение.
        - `Update` — запись.
    - `"Role":"[ApplicationSystemName] RoleSystemName"` — свойства роли:
        - `ApplicationSystemName` — системное имя приложения.
        - `RoleSystemName` — системное имя роли.
    - `"RoleType":"BusinessApp"` — тип роли:
        - `BusinessApp` — роль в приложении.
        - `System` — системная.
    - `"Resource":"[ParentSystemName] ResourceSystemName"` путь к ресурсу, на доступ к которому предоставлено разрешение:
        - `parentSystemName` — системное имя родительского ресурса.
        - `ResourceSystemName` — системное имя ресурса.
    - `"ResourceType":"RecordTemplate"` — тип ресурса, на доступ к которому предоставлено разрешение:
        - `BusinessApp` — приложение.
        - `ChangeJournal` — журнал изменений.
        - `From` — форма.
        - `List` — таблица.
        - `OrgStructureTemplate` — шаблон оргединицы.
        - `Operation` — кнопка.
        - `ProcessTemplate` — шаблон процесса.
        - `RecordTemplate` — шаблон записи.
        - `RoleTemplate` — шаблон роли.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `PUT completed` — результат обработки запроса: выполнен.

### Изменение прав доступа на объект {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'PUT: "{"role":{"Id":"role.26","Name":"ТЕст","Alias":"TEst","Workspace":{"Id":"workspace.1","Name":"Workspace Name"},"Solution":"sln.1","Creator":"account.6","CreationDate":"2023-10-25T17:58:03+00:00","LastWriteDate":"2023-10-25T20:15:39+00:00", "Members":["account.194"],"IsActive":true,"IsPredefined":false,"RoleType":1,"RootResource":{"Id":"rrpd.2329","Name":"Application name","Role":"role.26","Children":[{"Name":"Resource name","Children":[],"Target":"oa.89","TargetType":20,"Privileges":76,"AvailablePrivileges":719},{"Id":"rrpd.2330","Name":"Organizational unit template","Role":"role.26","Children":[{"Id":"rrpd.2331","Name":"All records","Role":"role.26","Children":[],"Target":"lst.13","TargetType":14,"Privileges":4,"AvailablePrivileges":4}],"Target":"os.1","TargetType":22,"Privileges":132,"AvailablePrivileges":204}],"Target":"sln.1","TargetType":4,"Privileges":204,"AvailablePrivileges":716},"CreatorName":"Full Name"}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put   'Разрешение удалено из роли' '{"Privilege":"Delete","Role":"[ApplicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/api/RolesCollectionApi/Put OK HH:mm:ss.SSS 'PUT completed' ''
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — имя пользователя, изменившего роль.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/RolesCollectionApi/Put` — путь к методу API для изменения роли.
- `PUT` — тип запроса.
- `role` — тело запроса:
    - `"Id":"role.ID"` — идентификатор роли.
    - `"Name":"Role Name"` — название роли.
    - `"Alias":"RoleSystemName"` — системное имя роли.
    - `"Workspace":{"Id":"workspace.ID","Name":"Workspace Name"}` — свойства раздела навигации, к которому привязана системная роль.
    - `"Solution":"sln.ID"` — идентификатор приложения.
    - `"IsPredefined":false` — непредустановленная роль.
    - `"RoleType":1` — тип роли:
    {: .pageBreakBefore }
        - 0 — системная стандартная;
        - 1 — роль в приложении;
        - 2 — системная пользовательская.
        - `"Members":[]` — массив идентификаторов учётных записей и групп, входящих в роль.
    - `"RootResource":{}` — приложение, к ресурсам которого роль задаёт разрешения.
    - `"Children":[{"Name":"Resource name","Children":[],"Target":"resource.ID","TargetType":XX,"Privileges":XXX, "AvailablePrivileges":XXX}]`— массив ресурсов, к которым роль задаёт разрешения.
        - `"Target":"resource.ID"` — идентификатор ресурса.
        - `"TargetType":XX` — код типа ресурса.
        - `"Privileges":XXX` — код установленных разрешений.
        - `"AvailablePrivileges":XXX` — код доступных разрешений.
- `Разрешение удалено из роли` — описание события.
- `'{"Privilege":"Read","Role":"[applicationSystemName] RoleSystemName","RoleType":"BusinessApp","Resource":"[ParentSystemName] ResourceSystemName", "ResourceType":"RecordTemplate"}'` — тело запроса:
    - `"Privilege":"Read"` — тип добавленного разрешения:
        - `Create` — создание;
        - `Delete` — удаление;
        - `Read` — чтение;
        - `Update` — запись.
    - `"Role":"[ApplicationSystemName] RoleSystemName"` — свойства роли:
        - `ApplicationSystemName` — системное имя приложения;
        - `RoleSystemName` — системное имя роли.
    - `"RoleType":"BusinessApp"` — тип роли:
        - `BusinessApp` — роль в приложении;
        - `System` — системная.
    - `"Resource":"[ParentSystemName] ResourceSystemName"` путь к ресурсу, на доступ к которому предоставлено разрешение:
        - `parentSystemName` — системное имя родительского ресурса;
        - `ResourceSystemName` — системное имя ресурса.
        {: .pageBreakBefore }
    - `"ResourceType":"RecordTemplate"` — тип ресурса, на доступ к которому предоставлено разрешение:
        - `BusinessApp` — приложение;
        - `ChangeJournal` — журнал изменений;
        - `From` — форма;
        - `List` — таблица;
        - `OrgStructureTemplate` — шаблон оргединицы;
        - `Operation` — кнопка;
        - `ProcessTemplate` — шаблон процесса;
        - `RecordTemplate` — шаблон записи;
        - `RoleTemplate` — шаблон роли.
- `OK` — статус обработки запроса.
- `hh:mm:ss.SSS` — длительность обработки запроса.
- `PUT completed` — результат обработки запроса: выполнен.

### Начало работы (запуск) системы {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 systemAccount ::1   Экземпляр {{ productName }} запущен.

Системная информация:

  Сервер: ubuntu-vm-server-gen2

  База данных: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

  Операционная система: Unix 5.15.0.89

  Версия: X.X.XXXX.X

  Часовой пояс: Europe/Moscow

  Язык: ru

  Путь к конфигурации: /var/www/instancename

  Путь к базе данных: /var/lib/comindware/instancename/Database

  Путь к загруженным файлам: /var/lib/comindware/instancename/Streams

Аутентификация IIS: Anonymous

  Аутентификация приложения: Ldap | Builtin

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 systemAccount    PerformanceHelper.Perform: FullTextSearchService.RebuildThreadWorker() succeed Time:59184ms TotalGCMemory:472MB DeltaGCMemory:-146MB TotalProcessMemory:462MB DeltaProcessMemory:0MB
```

{% if completeGuide or userGuide or adminGuideWindows or kbExport %}

#### Версия 4.2 (Windows) {: .pageBreakAfterAvoid }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 systemAccount    {{ productName }} has started.

System information:

 Server: SERVERNAME

 Database: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

 OperatingSystem: Microsoft Windows NT XXX.XXX.XXX.XXX

 Version: X.X.XXXX.X

 Timezone: Europe/Moscow

 Language: ru

 Config path: E:\instancename\Config

 Database path: E:\instancename\Data

 Streams path: F:\instancename\Streams

IIS authentication: Anonymous

 Application authentication: Anonymous

```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `systemAccount` — учётная запись, запустившая систему.
- `::1` — идентификатор локального хоста вместо IP-адреса.
- `{{ productName }} has started` — описание события: система запущена.
- `System information` — сведения о системе.
    - `Server: SERVERNAME` — имя сервера.
    - `Database: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` — идентификатор базы данных экземпляра ПО.
    - `OperatingSystem: Microsoft Windows NT XXX.XXX.XXX.XXX` — наименование и номер версии операционной системы сервера.
    - `Version: X.X.XXXX.X` — версия ПО {{ productName }}.
    - `Timezone: Europe/Moscow` — часовой пояс экземпляра ПО.
    - `Language: ru` — язык экземпляра ПО.
    - `Config path: E:\npd\Config` — путь к конфигурации.
    - `Database path: E:\xxx\Data` — путь к базе данных.
    - `Streams path: F:\xxx\Streams` — путь к загруженным файлам.
    - `IIS authentication: Anonimous | Ldap | Builtin` — способ Windows-аутентификации экземпляра ПО.
    - `Application authentication: Anonimous | Ldap | Builtin` — способ аутентификации экземпляра ПО.
- `PerformanceHelper.Perform: FullTextSearchService.RebuildThreadWorker() succeed` — запущена системная служба полнотекстового поиска.
- `Time:59184ms` — длительность запуска службы.
- `TotalGCMemory:XXXMB` — память, выделенная сборщику мусора.
- `DeltaGCMemory:-XXXMB` — изменение памяти, выделенной сборщику мусора.
- `TotalProcessMemory:XXXMB` — память, выделенная системе.
- `DeltaProcessMemory:XXXMB` — изменение памяти, выделенной системе.

{% endif %}

### Окончание (остановка) работы системы {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 systemAccount    {{ productName }} has stopped.
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `systemAccount` — учётная запись, запустившая систему.
- `{{ productName }} has started` — описание события: система остановлена.

### Запуск сервиса/службы/модуля {: .pageBreakBefore }

**Пример события**

``` log
2023-11-30 14:34:23,448 INFO 00000000-0000-0000-0000-000000000000 systemAccount    Core is loading

2023-11-30 14:34:25,586 INFO 00000000-0000-0000-0000-000000000000 systemAccount    Initialize account cache: 425ms

2023-11-30 14:34:34,407 INFO 00000000-0000-0000-0000-000000000000 systemAccount    Restore Sessions: 8821ms

2023-11-30 14:34:34,491 INFO 00000000-0000-0000-0000-000000000000 systemAccount    Initialize license service: 83ms

2023-11-30 14:34:34,533 INFO 00000000-0000-0000-0000-000000000000 systemAccount    Initialize routers: 0ms

2023-11-30 14:34:35,113 INFO 00000000-0000-0000-0000-000000000000 systemAccount    Initialize document converters: 501ms

2023-11-30 14:34:35,116 INFO 00000000-0000-0000-0000-000000000000 systemAccount    Synchronization with platform configuration 2ms
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `systemAccount` — учётная запись, запустившая сервис.
- `Core is loading` — запуск сервиса Core.
- `Initialize account cache: 425ms` — запущен сервис Core.
- `Restore Sessions: 8821ms` — запущен сервис Core.
- `Initialize license service: 83ms` — запущен сервис Core.
- `Initialize routers: 0ms` — запущен сервис Core.
- `Initialize document converters: 501ms` — запущен сервис Core.

### Остановка/сбой системы (компонентов, сервисов, экземпляров) {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 systemAccount    {{ productName }} has stopped.
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `systemAccount` — учётная запись, остановившая систему.
- `{{ productName }} has stopped` — описание события: система остановлена.

### Успешный результат выполнения процесса {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/UserCommandExecution/Prepare   'POST: "{"contextChanges":{"CommandId":"event.ID","ContextObjects":[]}}"' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 username XXX.XXX.XXX.XXX http://SERVER_URL/UserCommandExecution/Prepare 200 HH:mm:ss.SSS 'POST completed' ''

-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 systemAccount    Process runned count=11 (completed=3) lastRunTime="DD.MM.YYYY HH:mm:ss"; scripts started=1 (failed=0); worker threads started=7 (failed=0); messages total=0 (failed=0).
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `username` — учётная запись, запустившая процесс.
- `XXX.XXX.XXX.XXX` — IP-адрес сервера.
- `http://SERVER_URL/api/TemplatesApi/Create` — путь к методу API для создания шаблона
- `POST` — тип запроса.
- `"contextChanges":{}` — данные для запуска процесса:
    - `"CommandId":"event.ID"` — идентификатор кнопки, по нажатию которой был запущен процесс;
    - `"ContextObjects":[]` — массив идентификаторов записей, по которым был запущен процесс.
- `systemAccount` — учётная запись, запустившая службу.
- `Process runned count=11 (completed=3)` — количество запущенных экземпляров процесса (количество завершённых экземпляров процесса).
- `lastRunTime="DD.MM.YYYY hh:mm:ss"` — время последнего выполнения процесса.
- `scripts started=1 (failed=0)` — количество запущенных сценариев (количество завершившихся с ошибкой сценариев).
- `worker threads started=7 (failed=0)` — количество запущенных потоков системных служб (количество завершившихся с ошибкой системных служб).
- `messages total=0 (failed=0)` — количество переданных сообщений (количество сообщений, переданных с ошибкой).

### Успешный результат выполнения сервиса {: .pageBreakBefore }

**Пример события**

``` log
-MM-dd HH:mm:ss,SSS INFO 00000000-0000-0000-0000-000000000000 systemAccount    Core Loaded
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `00000000-0000-0000-0000-000000000000` — идентификатор сеанса.
- `systemAccount` — учётная запись, запустившая сервис.
- `Core Loaded` — запущен сервис Core.

### Статус подключения {: #log_files_event_examples_connection_status}

**Пример события**

``` yaml
[yyyy-MM-dd HH:mm:ss,SSS][INFO] PlatformKey: instanceName. Endpoint: connectionName (endpoint.XX). Adapter: incomingAdapter Connection test started 
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `PlatformKey: instanceName` — имя экземпляра ПО.
- `Endpoint: connectionName (endpoint.XX)` — имя и ID подключения.
- `Adapter: incomingAdapter` — имя адаптера.
- `Connection test started` — тестовое подключение запущено.

### Примеры событий в журналах адаптеров {: #log_files_event_examples_adapter_event .pageBreakBefore }

#### Событие в адаптере

**Пример события**

``` log
[yyy-MM-dd HH:mm:ss,SSS][INFO][Getting meta for plugin XxxSenderAdapter.] Platform key: XXX_AdapterAgent5b28ad88a4cb4d4f8078c4deef1ee08b; Service name: ServiceName; Runtime: .NET 6.0.21

[2023-12-08 00:10:20,667][INFO][Meta is ready for XxxSenderAdapter.] Platform key: XXX_AdapterAgent5b28ad88a4cb4d4f8078c4deef1ee08b; Service name: ServiceName; Runtime: .NET 6.0.21
data: {"Name":"XxxSenderAdapter","Description":"Адаптер для связи с системой «XXX»","Direction":"Outgoing","EndpointDefinitionJson":{}}
```

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `Getting meta for plugin XxxSenderAdapter` — описание события.
- `Platform key: XXX_AdapterAgent5b28ad88a4cb4d4f8078c4deef1ee08b; Service name: ServiceName; Runtime: .NET 6.0.21` — контекст события.
- `data: {}` — содержимое сообщения.

#### Статус работы адаптера

**Пример события**

``` yaml
[MM-dd HH:mm:ss,SSS][INFO] machineName_instanceName 
Kestrel. Incoming adapters:
[WHITE] Urls: http://127.0.1.1:8080
[GREEN] Status: Started
[WHITE] Number of subscribed integrations 1
[WHITE] Adapter name: incomingAdapter
[GREEN] Integration: messageTypeName. Route: Integration/SendRoute, HttpMethod: Post, AuthorizationType: Basic, ProcedureName: communicationRouteName, DataBusNumber: 0,  ProcedureIsDisable: False, EndpointIsAvailable: True
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `machineName` — имя машины.
- `instanceName` — имя экземпляра ПО.
- `COLOR` — цветовое обозначение статуса информации. `WHITE` — общая информация, `GREEN` — корректная работа, `RED` — некорректная работа.
- `Urls: <ipAddress>:<portNumber>` — адрес и порт, по которым доступен адаптер.
- `Status: Started` — статус адаптера: запущен.
- `Number of subscribed integrations 1` — количество типов сообщения пути передачи данных адаптера.
- `Adapter name: incomingAdapter` — имя адаптера.
- `Integration: messageTypeName` — имя типа сообщения пути передачи данных адаптера.
- `Route: Integration/SendRoute` — URI-путь типа сообщения пути передачи данных адаптера.
- `HttpMethod: Post` — тип метода.
- `AuthorizationType: Basic` — тип аутентификации: базовая.
- `ProcedureName: communicationRouteName` — имя пути передачи данных адаптера.
- `DataBusNumber: 0` — номер шины данных.
- `ProcedureIsDisable: False` — статус пути передачи данных адаптера.
- `EndpointIsAvailable: True` — статус подключения адаптера.

#### Сведения о созданных подключениях адаптера

**Пример события**

``` yaml
[yyyy-MM-dd HH:mm:ss,SSS][INFO] machineName_instanceName
Проверка подключений:
[GREEN] connectionName (endpoint.XX) - Соединение установлено (адаптер: incomingAdapter) 
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `machineName` — имя машины.
- `instanceName` — имя экземпляра ПО.
- `COLOR` — цветовое обозначение статуса информации. `WHITE` — общая информация, `GREEN` — корректная работа, `RED` — некорректная работа.
- `connectionName` — имя подключения.
- `endpoint.XX` — ID подключения.
- `incomingAdapter` — имя адаптера.

#### Статистика по процессу адаптера

**Пример события**

``` yaml
[yyyy-MM-dd HH:mm:ss,SSS][INFO] machineName_instanceName
Статистика по процессу:
[WHITE] Количество потоков 25 
[WHITE] Выделенный объем физической памяти 287,8 MB
[WHITE] Максимальный выделенный объем физической памяти 746,2 MB
[WHITE] Выделенный объем частной памяти 490,5 MB
[WHITE] Выделенный объем выгружаемой памяти 0 B
[WHITE] Максимальный выделенный объем выгружаемой памяти 0 B
[WHITE] Выделенный объем виртуальной памяти 4,8 GB
[WHITE] Максимальный выделенный объем виртуальной памяти 5,4 GB 
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `machineName` — имя машины.
- `instanceName` — имя экземпляра ПО.
- `COLOR` — цветовое обозначение статуса информации. `WHITE` — общая информация, `GREEN` — корректная работа, `RED` — некорректная работа.

### Сведения о созданных путях передачи данных адаптера

**Пример события**

``` yaml
[yyyy-MM-dd HH:mm:ss,SSS][INFO] machineName_instanceName
Созданные экземпляры путей передачи данных:
[WHITE] communicationRouteName (procedure.XX) - Адаптер: incomingAdapter. Подключение: connectionName (endpoint.XX). Запущен: True.
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `machineName` — имя машины.
- `instanceName` — имя экземпляра ПО.
- `COLOR` — цветовое обозначение статуса информации. `WHITE` — общая информация, `GREEN` — корректная работа, `RED` — некорректная работа.
- `communicationRouteName` — имя пути передачи данных адаптера.
- `procedure.XX` — ID пути передачи данных.
- `incomingAdapter` — имя адаптера.
- `connectionName` — имя подключения.
- `endpoint.XX` — ID подключения.

### Информация об адаптере

**Пример события**

``` yaml
[yyyy-MM-dd HH:mm:ss,SSS][INFO] machineName_instanceName
Загруженные адаптеры:
[WHITE] incomingAdapter Описание: adapterDescription. 
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `machineName` — имя машины.
- `instanceName` — имя экземпляра ПО.
- `incomingAdapter` — имя адаптера.
- `adapterDescription` — описание адаптера.

### Настройки подключения адаптера к брокеру сообщений

**Пример события**

``` yaml
[yyyy-MM-dd HH:mm:ss,SSS][INFO]  [AgentService::AgentService] 
platformKey: machineName_instanceName
loaderFolder: /var/www/instanceName/data/Plugins/Agent/LoadData
deployRequestQueue: request_queue_machineName_instanceName_deploy_external
deployReplyQueue: reply_queue_machineName_instanceName_external
outgoingRequestQueue: request_queue_machineName_instanceName_outgoing_external
outgoingReplyQueue: reply_queue_machineName_instanceName_outgoing_external
incomingRequestQueue: request_queue_machineName_instanceName_incoming_external
incomingReplyQueue: reply_queue_machineName_instanceName_incoming_external
bootstrapServers: 0.0.0.0:9092
groupId: instanceName
exclusiveGroupId: 
serverLanguage: ru
logFolder: /var/log/comindware/instanceName/Logs/
archiveFolder: /var/log/comindware/instanceName/Logs/Archive/
maxArchiveFiles: 100
archiveAboveSize: 1048576000
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `AgentService::AgentService` — тип подключения: агент к агенту.
- `platformKey: machineName_instanceName` — имя машины и имя экземпляра ПО.
- `loaderFolder` — имя папки загрузчика экземпляра ПО.
- `deployRequestQueue`, `deployReplyQueue`, `outgoingRequestQueue`, `outgoingReplyQueue`, `incomingRequestQueue`, `incomingReplyQueue` — идентификаторы типов сообщений в брокере сообщений для адаптера.
- `bootstrapServers: <kafkaIP>:<kafkaPortNumber>` — адрес и порт брокера сообщений.
- `groupId` — идентификатор группы в брокере сообщений.
- `serverLanguage` — язык сервера экземпляра ПО.
{% if not gostech %}
- `logFolder` — путь к файлам журналирования экземпляра ПО.
- `archiveFolder` — путь к архивам файлам журналирования экземпляра ПО.
- `maxArchiveFiles` — максимально количество файлов в одном архиве.
- `archiveAboveSize` — максимальный размер файлов журналов (в байтах).
{% endif %}

#### Взаимодействие адаптера с брокером сообщения

**Пример события**

``` yaml
[yyyy-MM-dd HH:mm:ss,SSS][INFO]  [88c1a6eb92f140fabs652bb8d9a630e8] [Metadata][Topic] reply_queue_instanceName_deploy_external:NoError 1:1:NoError:1:1 4:1:NoError:1:1 13:1:NoError:1:1 10:1:NoError:1:1 2:1:NoError:1:1 7:1:NoError:1:1 15:1:NoError:1:1 12:1:NoError:1:1 5:1:NoError:1:1 9:1:NoError:1:1 8:1:NoError:1:1 0:1:NoError:1:1 14:1:NoError:1:1 6:1:NoError:1:1 3:1:NoError:1:1 11:1:NoError:1:1 
```

**Поля события**

- `yyyy-MM-dd HH:mm:ss,SSS` — дата и время события.
- `INFO` — тип события: информационное.
- `[Metadata][Topic]` — тип события брокера сообщений.
- `reply_queue_instanceName_deploy_external` — ответ брокера сообщений на запрос экземпляра ПО с именем `instanceName`.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Подсистема журналирования][logging_engine]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
