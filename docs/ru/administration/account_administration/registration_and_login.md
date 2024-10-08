# Регистрация и вход

Страница «**Регистрация и вход**» позволяет просмотреть и настроить параметры самостоятельной регистрации новых аккаунтов, включить CAPTCHA на страницах входа и регистрации, а также настроить аутентификацию и синхронизацию аккаунтов с внешними службами: Azure Active Directory, AD Federation Services, Google OpenID Connect, Active Directory.

1. В разделе «**[Администрирование][administration]**» — «**[Администрирование аккаунтов][администрирование-аккаунтов]**» выберите пункт «**Регистрация и вход**».
*![Пункт «Регистрация и вход»](registration_and_login_button.png)*
2. Отобразится страница «**Регистрация и вход**».
*![Страница «Регистрация и вход»](registration_and_login.png)*

## Настройка самостоятельной регистрации аккаунтов

Помимо создания аккаунтов с помощью раздела «**[Аккаунты][аккаунты]**» можно разрешить их самостоятельную регистрацию со страницы входа в систему.

1. Установите флажок «**Разрешить самостоятельную регистрацию**».
2. При необходимости выберите или создайте группу, в которую следует включать самостоятельно зарегистрированные аккаунты. См. раздел «**[Группы][группы]**»
3. При необходимости выберите шаблон аккаунта, к которому следует привязывать самостоятельно зарегистрированные аккаунты.
4. Чтобы на страницах самостоятельной регистрации и сброса пароля требовалось вводить контрольный код CAPTCHA, установите флажок «**Включить CAPTCHA для публичных страниц**».
5. Нажмите кнопку «**Сохранить**».

## Настройка подключения к внешней службе

1. Нажмите плитку подключения или выберите в меню с троеточием на плитке пункт «**Настроить**».
2. В отобразившемся окне «Свойства подключения» настройте параметры синхронизации аккаунтов с внешней службой.
3. Чтобы включить или отключить возможность входа в систему для аккаунтов из внешней службы, используйте переключатель «**Разрешить вход**».

*![Плитка подключения к AD](registration_and_login_connection_tile.png)*

## Создание подключения к Active Directory

1. Нажмите плитку Active Directory со ссылкой «**Добавить**».

*![Плитка нового подключения к Active Directory](registration_and_login_add_ad.png)*

2. Отобразится окно «**Новое подключение: Active Directory**».
3. Настройте свойства подключения.
4. Нажмите кнопку «**Создать**».

*![Свойства нового подключения к AD](registration_and_login_new_ad_connection.png)*

## Удаление подключения

1. В меню с троеточием на плитке подключения выберите пункт «**Удалить**».
2. Подтвердите удаление в отобразившемся окне.

*![Меню с троеточием](registration_and_login_connection_ellipsis_menu.png)*
</br>
*![Подтверждение удаления подключения](registration_and_login_delete_confirmation.png)*
