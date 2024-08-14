---
title: Отправка почты SMTP
kbId:
---

# Отправка почты SMTP

## Введение

## Настройка подключения и путей передачи данных

1. Создайте новое подключение типа «**Отправка почты через SMTP**» со следующими настройками:

    - **Системное имя:** _smtpconnection_
    - **Название:** _Отправка уведомлений SMTP_
    - **Хост:** _smtp.test.ru_
    - **Порт: 465**
    - **Тип аутентификации: Базовая**
    - **Имя пользователя:** _test_
    - **Пароль:** _Пароль_
    - **Шифрование: SSL**
    - **Адрес эл. почты отправителя:** _test@test.ru_

2. Создайте новый путь передачи данных со следующими свойствами:

    - **Подключение:** _Отправка уведомлений SMTP_
    - **Системное имя:** _smtproute_
    - **Описание:** _Это путь передачи данных через SMTP_
3. На вкладке «**Интеграция**» задайте следующие параметры:

    - **Шаблон темы:** _{Subject}_
    - **Шаблон текста сообщения:** _{Body}_

## Настройка шаблона записи

1. Создайте шаблон записи _«Уведомления»_.
2. Создайте следующие атрибуты:

    - Аккаунт