# N3 Тройки - Примеры по категориям

## 1. РАБОТА С ПРОСТЫМИ СВОЙСТВАМИ

### Получение свойства объекта
```n3
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("District" "District_ExternalID") object:findProperty ?District_ExternalID.
    ?item ?District_ExternalID ?District_ExternalIDVal.
    ?District_ExternalIDVal -> ?value.
}
```

### Работа с несколькими свойствами
```n3
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("DiscountItem" "DiscountItem_CompensatoryDiscount") object:findProperty ?DiscountItem_CompensatoryDiscountProperty.
    ("DiscountItem" "DiscountItem_CompensatoryDiscountUsed") object:findProperty ?DiscountItem_CompensatoryDiscountUsedProperty.
    
    ?item ?DiscountItem_CompensatoryDiscountProperty ?DiscountItem_CompensatoryDiscountPropertyVal.
    ?DiscountItem_CompensatoryDiscountPropertyVal -> ?value.
}
```

---

## 2. ОПЕРАЦИИ С КОЛЛЕКЦИЯМИ

### Добавление в коллекцию
```n3
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("District" "District_ExternalID") object:findProperty ?District_ExternalID.
    ?item ?District_ExternalID ?District_ExternalIDVal.
    
    var:mass operator:add ?item.
    (?item var:FEATURE) operator:replace "BZIRK".
    (?item var:VALUE) operator:replace ?District_ExternalIDVal.
    
    true -> ?value.
}
```

### Очистка коллекции
```n3
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.

{
    var:pos operator:clear ?item.
    true -> ?value.
}
```

---

## 3. УСЛОВНАЯ ЛОГИКА

### Простое условие
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.

{
    ("PartyInvolved" "PartyInvolved_PartyInvolvedRole" ) object:findProperty ?PartyInvolved_PartyInvolvedRoleProp.
    ("PartyInvolvedRole" "PartyInvolvedRole_Code") object:findProperty ?PartyInvolvedRole_CodeProp.
    
    ?item ?PartyInvolved_PartyInvolvedRoleProp ?PartyInvolved_PartyInvolvedRoleVal.
    ?PartyInvolved_PartyInvolvedRoleVal ?PartyInvolvedRole_CodeProp ?PartyInvolvedRole_CodeVal.
    
    if {?PartyInvolvedRole_CodeVal == "account" }
    then {
        var:massPartyInvolved operator:add ?item.
        (?item var:PartnerRole) operator:replace "AG".
        (?item var:PartnerId) operator:replace ?Account_ExternalIDVal.
    }
    else {"asdasdsad" -> ?b}.
    
    true -> ?value.
}
```

### Проверка на пустое значение
```n3
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("Usluga" "Kolichestvo") object:findProperty ?KolichestvoProperty.
    
    if {?UslugitranzaktsionnyeValFromCount ?KolichestvoProperty ?. }
    then { ?UslugitranzaktsionnyeValFromCount ?KolichestvoProperty ?KolichestvoVal}
    else { 1 -> ?KolichestvoVal}.
}
```

### Множественные условия с or
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.

{
    if { 
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal1.
        ?UslugitranzaktsionnyeVal1 ?StatusProperty ?declineService.
        ?PrichinyotkazavsoglasovaniiKodVal == "ended_contract".
        
        or{?PrichinyotkazavsoglasovaniiKodVal == "disease_in_exceptions".}
        or{?PrichinyotkazavsoglasovaniiKodVal == "uninsured_event".}
        or{?PrichinyotkazavsoglasovaniiKodVal == "service_in_exceptions".}
    }
    then { "Текст сообщения" -> ?reqDescDeniedService.}
    else {"" -> ?reqDescDeniedService. }.
}
```

### Вложенные условия
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix account: <http://comindware.com/ontology/account#>.

{
    if {?item ?Tipotnosheniy ?otnoshenieYrLic.}
    then { ?value a account:Account.}
    else { 
        if { 
            ?item ?BusinessPartnerRelation_BusinessPartner_1Property ?BusinessPartnerRelation_BusinessPartner_1Val.
            ?BusinessPartnerRelation_BusinessPartner_1Val ?KategoriyaProperty ?TypeKompany.
            ?Tipkontragenta == ?typeKlient.
        }
        then {
            ?item ?CreatorProperty ?CreatorVal.
            ?RecordsKontragent ?AkkauntProperty ?CreatorVal.
            ?RecordsEmployee ?AkkauntProperty ?value.
        }
        else {?value a account:Account. }.
    }.
}
```

### Условие с not
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.
@prefix session: <http://comindware.com/ontology/session#>.

{
    session:context session:requestTime ?now.
    ?now cmwnullable:startOfDay ?nowstart.
    
    if {not{?item ?datazaversheniyraboty ?.}.}
    then {
        ?item ?duedate ?duedateval.
        ?duedateval cmwnullable:startOfDay ?duedatevalstart.
        ?nowstart cmwnullable:greaterThan ?duedatevalstart.
    }
    else {
        ?item ?datazaversheniyraboty ?datezav.
        ?datezav cmwnullable:startOfDay ?datezavstart.
        ?item ?duedate ?duedateval.
        ?duedateval cmwnullable:startOfDay ?duedatevalstart.
        ?datezavstart cmwnullable:greaterThan ?duedatevalstart.
    }.
}
```

### Условие с once
```n3
@prefix object: <http://comindware.com/ontology/object#>.

{
    if {
        once{
            ?item ?TiketProperty ?TiketVal.
            ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal3.
            ?UslugitranzaktsionnyeVal3 ?DokupkaProperty ?DokupkaVal.
            ?DokupkaVal == true.
        }.
    }
    then {
        "Также вижу, что часть услуг не входит в программу, поискать их со скидкой?" -> ?additionalServiseText.
    }
    else {"" -> ?additionalServiseText. }.
}
```

---

## 4. FROM-SELECT КОНСТРУКЦИИ

### Простой from-select
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.

{
    ("Usluga" "Naimenovanie") object:findProperty ?NaimenovanieProperty.
    ("Usluga" "Kolichestvo") object:findProperty ?KolichestvoProperty.
    
    from 
    {
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal.
        ?UslugitranzaktsionnyeVal ?StatusProperty ?approvedService.
        ?UslugitranzaktsionnyeValFromName ?NaimenovanieProperty ?NaimenovanieVal.
        ("• {0} - {1} шт." ?NaimenovanieVal ?KolichestvoVal) string:format ?approvedServiceStr.
    }
    select ?approvedServiceStr -> ?approvedServiceList.
    
    ?approvedServiceList -> ?value.
}
```

### From-select с кортежами
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix list: <http://www.w3.org/2000/10/swap/list#>.

{
    from {
        ?item ?PriceProtocolHeader_PriceProtocolItemProperty ?PriceProtocolHeader_PriceProtocolItemVal.
        ?PriceProtocolHeader_PriceProtocolItemVal ?PriceProtocolItem_StatusProperty ?PriceProtocolItem_StatusVal.
        ?PriceProtocolItem_StatusVal ?Status_CodeProperty ?Status_CodeVal.
        ?PriceProtocolHeader_PriceProtocolItemVal ?PriceProtocolItem_StepProperty ?PriceProtocolItem_StepVal.
        ?PriceProtocolItem_StepVal ?Step_CodeProperty ?Step_CodeVal.
    } 
    select (?Status_CodeVal ?Step_CodeVal ?PriceProtocolItem_PriceVal) -> ?detailingList.
    
    ?detailingList -> ?value.
}
```

### From-select с условиями
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.

{
    from {
        ?item ?ICSRHeaderProp ?ICPHeader.
        ?ICPHeader ?ICPHMillBPProp ?MillBP.
        ?MillBP ?BPOrgModelProp ?MillOrgModel.
        ?MillRates ?MillRateOrgUnitProp ?MillOrgModel.
        ?MillRates ?MillRateIncotermProp ?MillRateIncoterm.
        ?MillRateIncoterm ?IncotermsCodeProp "FOB".
        ?MillRates ?MillRateLocationProp ?MillRateLocation.
        ?MillRateLocation ?LocationCodeProp "221".
        ?MillRates ?MillRateEffDateProp ?MillRateDates.
    }
    select ?MillRateDates -> ?MillRateDatesList.
    
    ?MillRateDatesList cmwnullable:max ?MillRateDatesMax.
    ?MillRateDatesMax -> ?value.
}
```

---

## 5. СТРОКОВЫЕ ОПЕРАЦИИ

### Форматирование строки
```n3
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("Usluga" "Naimenovanie") object:findProperty ?NaimenovanieProperty.
    ?item ?NaimenovanieProperty ?NaimenovanieVal.
    
    ("• {0} - {1} шт." ?NaimenovanieVal ?KolichestvoVal) string:format ?formattedStr.
    ?formattedStr -> ?value.
}
```

### Объединение списка строк
```n3
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.

{
    from {
        ?item ?property ?val.
        ("Text {0}" ?val) string:format ?formatted.
    }
    select ?formatted -> ?list.
    
    (" " ?list) cmwstring:join ?joinedStr.
    ?joinedStr -> ?value.
}
```

### Регулярное выражение
```n3
@prefix string: <http://comindware.com/logics/string#>.
@prefix session: <http://comindware.com/ontology/session#>.

{
    session:context var:var ?varVal.
    ?varVal var:IDOC ?IDOCVal.
    ?IDOCVal var:SalesOrderData ?SalesOrderDataVal.
    ?SalesOrderDataVal var:DocumentNumber ?DocumentNumberVal.
    
    (?DocumentNumberVal "^0+" "" ) string:regexReplace ?result.
    ?result -> ?value.
}
```

### Обрезка пробелов
```n3
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("CertificateItem" "CertificateItem_SmeltingNumber") object:findProperty ?CertificateItem_SmeltingNumberProperty.
    ?item ?CertificateItem_SmeltingNumberProperty ?CertificateItem_SmeltingNumberVal.
    
    ?CertificateItem_SmeltingNumberVal string:trim ?trimedCertificateItem_SmeltingNumber.
    ?trimedCertificateItem_SmeltingNumber -> ?value.
}
```

### Подстрока
```n3
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("Stock" "Stock_CodeCRM") object:findProperty ?Stock_CodeCRMProp.
    ?item ?Stock_CodeCRMProp ?Stock_CodeCRMVal.
    
    (?Stock_CodeCRMVal 4) string:substring ?Stock_CodeCRMSubVal.
    ?Stock_CodeCRMSubVal -> ?value.
}
```

### Преобразование в нижний регистр
```n3
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.

{
    ?PrichinyotkazavsoglasovaniiNaimenovanieStr string:format ?formatted.
    ?formatted cmwstring:toLower ?lowerCaseStr.
    ?lowerCaseStr -> ?value.
}
```

---

## 6. МАТЕМАТИЧЕСКИЕ ОПЕРАЦИИ

### Остаток от деления
```n3
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("Protokoltsen" "pozitsii") object:findProperty ?pozitsiiProperty.
    
    {
        ?item ?pozitsiiProperty ?pozitsiiVal.
    } assert:count ?countVal.
    
    (?countVal 4) cmwnullable:remainder ?resultReminder.
    ?resultReminder -> ?value.
}
```

### Умножение и сложение
```n3
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.

{
    (?countVal 0.25) cmwnullable:product ?firstIndexVal.
    (?firstIndexVal 1) cmwnullable:sum ?secondIndexVal.
    ?secondIndexVal -> ?value.
}
```

### Среднее значение
```n3
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.

{
    (?valOfFirstIndexVal ?valOsecondIndexValVal) cmwnullable:average ?resultVal.
    ?resultVal -> ?value.
}
```

### Максимальное значение
```n3
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.

{
    from {
        ?item ?dateProperty ?dateVal.
    }
    select ?dateVal -> ?dateList.
    
    ?dateList cmwnullable:max ?maxDate.
    ?maxDate -> ?value.
}
```

### Округление вверх
```n3
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.

{
    ?firstIndexVal cmwnullable:ceiling ?firstIndexValAfterCell.
    ?firstIndexValAfterCell -> ?value.
}
```

### Работа с датами
```n3
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.
@prefix session: <http://comindware.com/ontology/session#>.

{
    session:context session:requestTime ?now.
    ?now cmwnullable:startOfDay ?nowstart.
    
    ?item ?duedate ?duedateval.
    ?duedateval cmwnullable:startOfDay ?duedatevalstart.
    
    ?nowstart cmwnullable:greaterThan ?duedatevalstart.
}
```

---

## 7. РАБОТА СО СПИСКАМИ

### Сортировка списка
```n3
@prefix cmwlist: <http://comindware.com/logics/list#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    from {
        ?item ?property ?val.
    }
    select ?val -> ?list.
    
    ?list cmwlist:ascending ?sortedList.
    ?sortedList -> ?value.
}
```

### Получение элемента по индексу
```n3
@prefix cmwlist: <http://comindware.com/logics/list#>.

{
    ?chisloPropertyValList cmwlist:ascending ?chisloPropertyValListSorted.
    (?chisloPropertyValListSorted ?firstIndexVal) cmwlist:at ?valOfFirstIndexVal.
    ?valOfFirstIndexVal -> ?value.
}
```

### Работа с кортежами
```n3
@prefix list: <http://www.w3.org/2000/10/swap/list#>.

{
    from {
        ?detailingList list:member ?datailingListMember1.
        ?datailingListMember1 -> (?code1 ?step1 ?total1).
        ?step1 == "365".
    }
    select ?total1 -> ?total1List.
    
    ?total1List -> ?value.
}
```

---

## 8. ПОДСЧЕТ И ПРОВЕРКИ

### Подсчет записей
```n3
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("Protokoltsen" "pozitsii") object:findProperty ?pozitsiiProperty.
    
    {
        ?item ?pozitsiiProperty ?pozitsiiVal.
    } assert:count ?countVal.
    
    ?countVal -> ?value.
}
```

### Подсчет с условиями
```n3
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix process: <http://comindware.com/ontology/process#>.
@prefix w3string: <http://www.w3.org/2000/10/swap/string#>.

{
    {
        ?processObject process:businessObject ?item.
        ?processObject process:status ?processStatus.
        ("{0}" ?processStatus) w3string:format ?strprocessStatus.
        ?strprocessStatus == "process.ActiveStatus".
        ?processObject process:name ?nameVal.
        ?nameVal == "Creating_Account".
    } assert:count ?value.
}
```

---

## 9. РАБОТА С ДОКУМЕНТАМИ

### Получение содержимого и заголовка
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix document: <http://comindware.com/ontology/document#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix variable: <http://comindware.com/ontology/session/variable#>.

{
    ("Dokumenty" "Fayl") object:findProperty ?FaylProperty.
    
    ?item ?FaylProperty ?FaylData.
    ?FaylData document:content ?Document.
    ?FaylData document:title ?title.
    
    variable:Document operator:replace ?Document.
    variable:title operator:replace ?title.
    
    true -> ?value.
}
```

### Форматирование ссылки на документ
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix document: <http://comindware.com/ontology/document#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.

{
    ("Documents" "Document_Attachment") object:findProperty ?foundProperty.
    
    ?item ?foundProperty ?doc.
    ?doc document:title ?title.
    
    ("<p><a href='https://system.bau.cbap.ru/DocumentContent?id={0}'>Ссылка на файл {1}</a></p>" ?doc ?title) string:format ?value.
}
```

### Base64 кодирование изображения
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix document: <http://comindware.com/ontology/document#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.

{
    ("Dokumenty" "Fayl") object:findProperty ?FaylProperty.
    
    ?item ?FaylProperty ?FaylData.
    ?FaylData document:content ?Document.
    
    ("data:image/jpeg;base64,{0}" ?Document) string:format ?newString.
    
    var:metersPhoto operator:add ?newString.
    
    true -> ?value.
}
```

---

## 10. РАБОТА С ENUM И ТИПАМИ

### Преобразование enum значения
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix convert: <http://comindware.com/logics/convertions#>.

{
    ("test1" "pair") object:findProperty ?pairProperty.
    ("PAIR" "Spisokznacheniy") object:findProperty ?SpisokznacheniyProperty.
    
    ?item ?pairProperty ?pairVal.
    ("Spisokznacheniy" "cancelled") convert:enumValue ?enumVal.
    ?pairVal ?SpisokznacheniyProperty ?enumVal.
    
    ?pairVal -> ?value.
}
```

### Проверка типа объекта
```n3
@prefix account: <http://comindware.com/ontology/account#>.
@prefix cmw: <http://comindware.com/logics#>.

{
    ?value a account:Account.
    # или
    ?item a cmw:UserTask.
}
```

---

## 11. КОНТЕКСТ СЕССИИ И БЕЗОПАСНОСТЬ

### Получение значения из контекста
```n3
@prefix session: <http://comindware.com/ontology/session#>.

{
    session:context var:product ?productVal.
    ?productVal -> ?value.
}
```

### Текущий пользователь
```n3
@prefix cmw: <http://comindware.com/logics#>.

{
    cmw:securityContext cmw:currentUser ?currentUser.
    
    ?item cmw:assignee ?currentUser.
    # или
    ?item cmw:possibleAssignee ?currentUser.
}
```

### Контейнер объекта
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmw: <http://comindware.com/logics#>.

{
    ?template object:alias "ProjectPlans".
    ?item cmw:container ?template.
    ?item ?contact ?user.
}
```

---

## 12. СЛОЖНЫЕ КОМБИНАЦИИ

### Комплексное правило с условиями, from-select и форматированием
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.

{
    ("Uvedomlenieklientu" "BodyMessage") object:findProperty ?BodyMessageProperty.
    ("Uvedomlenieklientu" "Tiket") object:findProperty ?TiketProperty.
    ("Usluga" "Naimenovanie") object:findProperty ?NaimenovanieProperty.
    ("Usluga" "Kolichestvo") object:findProperty ?KolichestvoProperty.
    
    # Блок согласованных услуг
    from 
    {
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal.
        ?UslugitranzaktsionnyeVal ?StatusProperty ?approvedService.
        
        if {?UslugitranzaktsionnyeValFromCount ?KolichestvoProperty ?. }
        then { ?UslugitranzaktsionnyeValFromCount ?KolichestvoProperty ?KolichestvoVal}
        else { 1 -> ?KolichestvoVal}.
        
        ?UslugitranzaktsionnyeValFromName ?NaimenovanieProperty ?NaimenovanieVal.
        ("• {0} - {1} шт." ?NaimenovanieVal ?KolichestvoVal) string:format ?approvedServiceStr.
    }
    select ?approvedServiceStr -> ?approvedServiceList.
    
    (" " ?approvedServiceList) cmwstring:join ?approvedServiceListToStr.
    
    # Условие для вывода текста
    if {?approvedServiceListToStr == "". }
    then {
        "" -> ?availaible.
        "" -> ?availaible1.
    }
    else {
        "Доступно:" -> ?availaible.
        "Подскажите, когда и в каком районе будет удобно посетить клинику?" -> ?availaible1.
    }.
    
    # Форматирование итогового результата
    if {?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?. }
    then {
        (?BodyMessageVal ?availaible ?approvedServiceListToStr ?availaible1) string:format ?resultVal.
    }
    else {"" -> ?resultVal}.
    
    ?resultVal -> ?value.
}
```

### Правило с множественными альтернативами (or блоки)
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.

{
    from {
        ?item ?property ?val.
    }
    select ?val -> ?list.
    
    or
    {
        ?list cmwnullable:max ?result.
        ?result != 0.
    }
    or
    {
        1 -> ?result.
    }.
    
    ?result -> ?value.
}
```

### Правило с множественными условиями поиска (or условия)
```n3
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.

{
    or{
        ?ClaimHeader_ClaimItemVal -> ?ClaimHeader_ClaimItemVal1.
        ?item ?CertificateItem_SmeltingNumberProperty ?CertificateItem_SmeltingNumberVal.
        ?CertificateItem_SmeltingNumberVal string:trim ?trimedCertificateItem_SmeltingNumber.
        ?trimedCertificateItem_SmeltingNumber == ?trimedClaimItem_HeatNoTECHLoad.
        ?ClaimHeader_ClaimItemVal1 -> ?ClaimHeader_ClaimItemValResult.
    }
    
    or {
        ?ClaimHeader_ClaimItemVal -> ?ClaimHeader_ClaimItemVal2.
        ?item ?CertificateItem_CertificateNumberProperty ?CertificateItem_CertificateNumberVal.
        ?CertificateItem_CertificateNumberVal string:trim ?trimedCertificateItem_CertificateNumber.
        ?trimedCertificateItem_CertificateNumber == ?trimedClaimItem_CertificateNumberTECHLoad.
        ?ClaimHeader_ClaimItemVal2 -> ?ClaimHeader_ClaimItemValResult.
    }.
    
    ?ClaimHeader_ClaimItemValResult -> ?value.
}
```

---

## 13. РАБОТА С ЗАДАЧАМИ И ПРОЦЕССАМИ

### Поиск задачи по объекту
```n3
@prefix cmw: <http://comindware.com/logics#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.

{
    ?task task:objectId ?item.
    ?task cmw:taskStatus taskStatus:inProgress.
    ?task -> ?value.
}
```

### Фильтрация задач по пользователю
```n3
@prefix cmw: <http://comindware.com/logics#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.

{
    cmw:securityContext cmw:currentUser ?currentUser.
    
    ?item a cmw:UserTask.
    ?item cmw:taskStatus taskStatus:inProgress.
    
    or
    {
        ?item cmw:assignee ?currentUser.
    }
    or
    {
        ?item cmw:possibleAssignee ?currentUser.
    }
}
```

---

Эти примеры покрывают все основные паттерны использования N3 троек из предоставленного файла. Используйте их как шаблоны для создания собственных правил.
