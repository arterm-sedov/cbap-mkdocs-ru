# Примеры выражений на N3 для решения различных задач

``` turtle
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix account: <http://comindware.com/ontology/account#>.
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

``` turtle
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.

@prefix object: <http://comindware.com/ontology/object#>.

{
    ("DiscountItem" "DiscountItem_CompensatoryDiscount") object:findProperty ?DiscountItem_CompensatoryDiscountProperty.
    ("DiscountItem" "DiscountItem_CompensatoryDiscountUsed") object:findProperty ?DiscountItem_CompensatoryDiscountUsedProperty.

    ?item ?DiscountItem_CompensatoryDiscountProperty ?DiscountItem_CompensatoryDiscountPropertyVal.

    var:comDisc operator:add ?DiscountItem_CompensatoryDiscountPropertyVal.


    true -> ?value.
}
```

``` turtle
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix cmwsession: <http://comindware.com/ontology/session#>.
{
    var:pos operator:clear ?item.
    true -> ?value.
}
```

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.

{
    ("Uvedomlenieklientu" "BodyMessage") object:findProperty ?BodyMessageProperty. 
    ("Uvedomlenieklientu"  "Tiket") object:findProperty ?TiketProperty.
    ("Uvedomlenieklientu" "TemplateNotification" ) object:findProperty ?TemplateNotificationProperty.

    ("Tiket" "Uslugitranzaktsionnye") object:findProperty ?UslugitranzaktsionnyeProperty.

    ("Usluga" "Naimenovanie") object:findProperty ?NaimenovanieProperty.
    ("Usluga" "Status") object:findProperty ?StatusProperty.
    ("Usluga" "Kolichestvo") object:findProperty ?KolichestvoProperty.
    ("Usluga"  "Prichinaotkaza") object:findProperty ?PrichinaotkazaProperty.
    ("Usluga"  "Dokupka") object:findProperty ?DokupkaProperty.

    ("Prichinyotkazavsoglasovanii"  "Naimenovanie") object:findProperty ?PrichinyotkazavsoglasovaniiNaimenovanieProperty.
    ("Prichinyotkazavsoglasovanii"  "Kod") object:findProperty ?PrichinyotkazavsoglasovaniiKodProperty.

    ("Statussoglasovaniya"  "Kod") object:findProperty ?StatussoglasovaniyaKodProperty.

    # Блок со статусами согласования
    ?declineService ?StatussoglasovaniyaKodProperty "decline".
    ?notRequiredService ?StatussoglasovaniyaKodProperty "not_required".
    ?approvedService ?StatussoglasovaniyaKodProperty "approved".

    ?item ?TemplateNotificationProperty ?TemplateNotificationVal.
    ?TemplateNotificationVal ?BodyMessageProperty ?BodyMessageVal.

    # Блок согласованных услуг
    from 
    {
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal.

        ?UslugitranzaktsionnyeVal ?StatusProperty ?approvedService.
        ?UslugitranzaktsionnyeVal -> ?UslugitranzaktsionnyeValFromName.
        ?UslugitranzaktsionnyeVal -> ?UslugitranzaktsionnyeValFromCount.

        if {?UslugitranzaktsionnyeValFromCount ?KolichestvoProperty ?. }
        then { ?UslugitranzaktsionnyeValFromCount ?KolichestvoProperty ?KolichestvoVal}
        else { 1 -> ?KolichestvoVal}.   

        ?UslugitranzaktsionnyeValFromName ?NaimenovanieProperty ?NaimenovanieVal.
        ("• {0} - {1} шт." ?NaimenovanieVal ?KolichestvoVal) string:format ?approvedServiceStr.

    }	select ?approvedServiceStr -> ?approvedServiceList.

    (" " ?approvedServiceList) cmwstring:join ?approvedServiceListToStr.

    # Блок услуг без согласования
    from 
    {
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal4.

        ?UslugitranzaktsionnyeVal4 ?StatusProperty ?notRequiredService.
        
        ?UslugitranzaktsionnyeVal4 -> ?UslugitranzaktsionnyeValFromName4.
        ?UslugitranzaktsionnyeVal4 -> ?UslugitranzaktsionnyeValFromCount4.

        if {?UslugitranzaktsionnyeValFromCount4 ?KolichestvoProperty ?. }
        then { ?UslugitranzaktsionnyeValFromCount4 ?KolichestvoProperty ?KolichestvoVal4}
        else { 1 -> ?KolichestvoVal4}.   

        ?UslugitranzaktsionnyeValFromName4 ?NaimenovanieProperty ?NaimenovanieVal4.
        ("• {0} - {1} шт." ?NaimenovanieVal4 ?KolichestvoVal4) string:format ?notRequiredAprovallServiceStr.

    }	select ?notRequiredAprovallServiceStr -> ?notRequiredAprovallServiceList.

    (" " ?notRequiredAprovallServiceList) cmwstring:join ?notRequiredAprovallServiceListToStr.
    
    # Блок не согласованных услуг
    from 
    {
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal5.

        ?UslugitranzaktsionnyeVal5 ?StatusProperty ?declineService.
        
        ?UslugitranzaktsionnyeVal5 -> ?UslugitranzaktsionnyeValFromName1.
        ?UslugitranzaktsionnyeVal5 -> ?UslugitranzaktsionnyeValFromCount1.
        ?UslugitranzaktsionnyeVal5 -> ?UslugitranzaktsionnyeValFromPrichinaotkaza.

        if {?UslugitranzaktsionnyeValFromCount1 ?KolichestvoProperty ?. }
        then { ?UslugitranzaktsionnyeValFromCount1 ?KolichestvoProperty ?KolichestvoVal1}
        else { 1 -> ?KolichestvoVal1}.   
        
        ?UslugitranzaktsionnyeValFromPrichinaotkaza ?PrichinaotkazaProperty ?PrichinaotkazaPropertyVal2.
		?PrichinaotkazaPropertyVal2 ?PrichinyotkazavsoglasovaniiNaimenovanieProperty ?PrichinyotkazavsoglasovaniiNaimenovanieVal.
        ("{0}" ?PrichinyotkazavsoglasovaniiNaimenovanieVal ) string:format ?PrichinyotkazavsoglasovaniiNaimenovanieStr.
        ?PrichinyotkazavsoglasovaniiNaimenovanieStr cmwstring:toLower ?PrichinyotkazavsoglasovaniiNaimenovanieStrToLower.
        ?UslugitranzaktsionnyeValFromName1 ?NaimenovanieProperty ?NaimenovanieVal1.
        ("• {0} - {1} шт - не получилось согласовать, так как {2}." ?NaimenovanieVal1 ?KolichestvoVal1 ?PrichinyotkazavsoglasovaniiNaimenovanieStrToLower) string:format ?declineServiceStr.

    }	select ?declineServiceStr -> ?declineServiceList.

    (" " ?declineServiceList) cmwstring:join ?declineServiceListToStr.

    # Блок вывода доп текста в зависимости от причины отказа
    if { 
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal1.

        ?UslugitranzaktsionnyeVal1 ?StatusProperty ?declineService.
        ?UslugitranzaktsionnyeVal1 ?PrichinaotkazaProperty ?PrichinaotkazaPropertyVal1.
        ?PrichinaotkazaPropertyVal1 ?PrichinyotkazavsoglasovaniiKodProperty ?PrichinyotkazavsoglasovaniiKodVal.

        or{?PrichinyotkazavsoglasovaniiKodVal == "ended_contract".}
        or{?PrichinyotkazavsoglasovaniiKodVal == "disease_in_exceptions".}
        or{?PrichinyotkazavsoglasovaniiKodVal == "uninsured_event".}
        or{?PrichinyotkazavsoglasovaniiKodVal == "service_in_exceptions".}
        or{?PrichinyotkazavsoglasovaniiKodVal == "not_in_program".}
        or{?PrichinyotkazavsoglasovaniiKodVal == "limit_exceeded".}
        or{?PrichinyotkazavsoglasovaniiKodVal == "approval_conditions_not_met".}.
    }
    then { "Посмотреть свою программу можно в личном кабинете в разделе «Что включает мой план» или в мобильном приложении:  Профиль → Моя программа → Полные условия в pdf." -> ?reqDescDeniedService.}
    else {"" -> ?reqDescDeniedService. }.
	
    # Блок вывода доп текста в зависимости от причины отказа 2
    if { 
        ?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?UslugitranzaktsionnyeVal2.

        ?UslugitranzaktsionnyeVal2 ?StatusProperty ?declineService.
        ?UslugitranzaktsionnyeVal2 ?PrichinaotkazaProperty ?PrichinaotkazaPropertyVal.
        ?PrichinaotkazaPropertyVal ?PrichinyotkazavsoglasovaniiKodProperty ?PrichinyotkazavsoglasovaniiKodVal1.

        or{?PrichinyotkazavsoglasovaniiKodVal1 == "uninformative_document".}
        or{?PrichinyotkazavsoglasovaniiKodVal1 == "prepaid_program".}

    }
    then { "Помочь вам с записью в доступную клинику?" -> ?reqAdditionalDescDeniedService.}
    else {"" -> ?reqAdditionalDescDeniedService. }.

    # Блок для вывода текста для согласованных услуг
    if {?approvedServiceListToStr == "". }
    then {
        "" -> ?availaible.
        "" -> ?availaible1.
    }
    else {
        "Доступно:" -> ?availaible.
        "Подскажите, когда и в каком районе будет удобно посетить клинику?" -> ?availaible1.}.


    # Блок для вывода текста для услуг без соласования
    if {?notRequiredAprovallServiceListToStr == "". }
    then {
        "" -> ?notRequiredAprovalText.
        "" -> ?notRequiredAprovalText1.
    }
    else {
        "Услуги, которые не нужно с нами согласовывать:" -> ?notRequiredAprovalText.
    "Договорились с клиникой, что доктор самостоятельно принимает решение о возможности проведения услуг по программе." -> ?notRequiredAprovalText1.}.

    # Блок для вывода текста если услуга не входит в программу
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
	
    if {?item ?TiketProperty ?TiketVal.
        ?TiketVal ?UslugitranzaktsionnyeProperty ?. }
	then {    (?BodyMessageVal ?availaible ?approvedServiceListToStr ?declineServiceListToStr  ?reqDescDeniedService ?reqAdditionalDescDeniedService ?notRequiredAprovalText ?notRequiredAprovallServiceListToStr ?notRequiredAprovalText1 ?availaible1 ?additionalServiseText ) string:format ?resultVal.
 }
	else {"" -> ?resultVal}.
    

    ?resultVal -> ?value.

}


@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix object: <http://comindware.com/ontology/object#>.
{	
    ("PartyInvolved" "PartyInvolved_BusinessPartner" ) object:findProperty ?PartyInvolved_BusinessPartnerProp.

    ("PartyInvolved" "PartyInvolved_PartyInvolvedRole" ) object:findProperty ?PartyInvolved_PartyInvolvedRoleProp.
    ("PartyInvolvedRole" "PartyInvolvedRole_Code") object:findProperty ?PartyInvolvedRole_CodeProp.

    ("BusinessPartner" "BusinessPartner_Account") object:findProperty ?BusinessPartner_AccountProp.
    ("Account" "Account_ExternalID" ) object:findProperty ?Account_ExternalIDProp.

    ("BusinessPartner"  "BusinessPartner_Employee") object:findProperty ?BusinessPartner_EmployeeProp.
    ("Employee"  "Employee_StaffNumber") object:findProperty ?Employee_StaffNumberProp.



    ?item ?PartyInvolved_PartyInvolvedRoleProp ?PartyInvolved_PartyInvolvedRoleVal.
    ?PartyInvolved_PartyInvolvedRoleVal ?PartyInvolvedRole_CodeProp ?PartyInvolvedRole_CodeVal.

    if {?PartyInvolvedRole_CodeVal == "account" }
    then {?list ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.
          ?PartyInvolved_BusinessPartnerVal ?BusinessPartner_AccountProp  ?BusinessPartner_AccountVal.
          ?BusinessPartner_AccountVal ?Account_ExternalIDProp ?Account_ExternalIDVal.

          var:massPartyInvolved operator:add ?item.

          (?item var:PartnerRole) operator:replace "AG".
          (?item var:PartnerId) operator:replace ?Account_ExternalIDVal.}
    else{"asdasdsad" -> ?b}.


    if {?PartyInvolvedRole_CodeVal == "middle_officer" }
    then {?item ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.
          ?PartyInvolved_BusinessPartnerVal ?BusinessPartner_EmployeeProp  ?BusinessPartner_EmployeeVal.
          ?BusinessPartner_EmployeeVal ?Employee_StaffNumberProp ?Employee_StaffNumberVal.

          var:massPartyInvolved operator:add ?item.

          (?item var:PartnerRole) operator:replace "Y2".
          (?item var:PartnerId) operator:replace ?Employee_StaffNumberVal. }
    else{"asdasdsad" -> ?b}.

    if {?PartyInvolvedRole_CodeVal == "responsible" }
    then {?item ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.
          ?PartyInvolved_BusinessPartnerVal ?BusinessPartner_EmployeeProp  ?BusinessPartner_EmployeeVal.
          ?BusinessPartner_EmployeeVal ?Employee_StaffNumberProp ?Employee_StaffNumberVal.

          var:massPartyInvolved operator:add ?item.

          (?item var:PartnerRole) operator:replace "Y1".
          (?item var:PartnerId) operator:replace ?Employee_StaffNumberVal. }
    else{"asdasdsad" -> ?b}.

    if {?PartyInvolvedRole_CodeVal == "shipper" }
    then {?item ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.
          ?PartyInvolved_BusinessPartnerVal ?BusinessPartner_AccountProp  ?BusinessPartner_AccountVal.
          ?BusinessPartner_AccountVal ?Account_ExternalIDProp ?Account_ExternalIDVal.

          var:massPartyInvolved operator:add ?item.

          (?item var:PartnerRole) operator:replace "ZE".
          (?item var:PartnerId) operator:replace ?Account_ExternalIDVal. }
    else{"asdasdsad" -> ?b}.

    if {?PartyInvolvedRole_CodeVal == "consignee" }
    then {?item ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.
          ?PartyInvolved_BusinessPartnerVal ?BusinessPartner_AccountProp  ?BusinessPartner_AccountVal.
          ?BusinessPartner_AccountVal ?Account_ExternalIDProp ?Account_ExternalIDVal.

          var:massPartyInvolved operator:add ?item.

          (?item var:PartnerRole) operator:replace "WE".
          (?item var:PartnerId) operator:replace ?Account_ExternalIDVal. }
    else{"asdasdsad" -> ?b}.

    if {?PartyInvolvedRole_CodeVal == "payer" }
    then {?item ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.
          ?PartyInvolved_BusinessPartnerVal ?BusinessPartner_AccountProp  ?BusinessPartner_AccountVal.
          ?BusinessPartner_AccountVal ?Account_ExternalIDProp ?Account_ExternalIDVal.

          var:massPartyInvolved operator:add ?item.

          (?item var:PartnerRole) operator:replace "RG".
          (?item var:PartnerId) operator:replace ?Account_ExternalIDVal. }
    else{"asdasdsad" -> ?b}.

    if {?PartyInvolvedRole_CodeVal == "recipient" }
    then {?item ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.
          ?PartyInvolved_BusinessPartnerVal ?BusinessPartner_AccountProp  ?BusinessPartner_AccountVal.
          ?BusinessPartner_AccountVal ?Account_ExternalIDProp ?Account_ExternalIDVal.

          var:massPartyInvolved operator:add ?item.

          (?item var:PartnerRole) operator:replace "RE".
          (?item var:PartnerId) operator:replace ?Account_ExternalIDVal. }
    else{"asdasdsad" -> ?b}.


    true -> ?value.
}
```

``` turtle
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://comindware.com/logics/string#>.

{
    ("OfferOrderItem" "OfferOrderItem_Number") object:findProperty ?OfferOrderItem_NumberProp.
    ("OfferOrderItem" "OfferOrderItem_Product") object:findProperty ?OfferOrderItem_ProductProp.
    ("OfferOrderItem" "OfferOrderItem_Quantity") object:findProperty ?OfferOrderItem_QuantityProp.
    ("OfferOrderItem" "OfferOrderItem_Incoterms") object:findProperty ?OfferOrderItem_IncotermsProp.

    ("Product" "Product_ExternalID" ) object:findProperty ?Product_ExternalIDProp.
    ("Product" "Product_Description" ) object:findProperty ?Product_DescriptionProp.

    ("Product" "Product_UnitOfMeasure" ) object:findProperty ?Product_UnitOfMeasureProp.
    ("UnitOfMeasure" "UnitOfMeasure_CodeCRM" ) object:findProperty ?UnitOfMeasure_CodeCRMProp.





    ("OfferOrderItem" "OfferOrderItem_OfferHeader") object:findProperty ?OfferOrderItem_OfferHeaderProp.
    ("OfferHeader" "OfferHeader_Stock") object:findProperty ?OfferHeader_StockProp.
    ("Stock" "Stock_CodeCRM") object:findProperty ?Stock_CodeCRMProp.   

    ("OfferOrderItem" "OfferOrderItem_OrganizationalModel_Mill") object:findProperty ?OfferOrderItem_OrganizationalModel_MillProp.
    ("OrganizationalModel" "OrganizationalModel_ID") object:findProperty ?OrganizationalModel_IDProp.

    ("OfferHeader" "OfferHeader_IncotermsLocation" ) object:findProperty ?OfferHeader_IncotermsLocationProp.

    ("OfferHeader" "OfferHeader_PayTerm" ) object:findProperty ?OfferHeader_PayTermProp.
    ("PayTerm" "PayTerm_ExternalCode" ) object:findProperty ?PayTerm_ExternalCodeProp.

    ("OfferHeader" "OfferHeader_OverdeliveryTolerance" ) object:findProperty ?OfferHeader_OverdeliveryToleranceProp.

    ("OfferHeader" "OfferHeader_UnderdeliveryTolerance" ) object:findProperty ?OfferHeader_UnderdeliveryToleranceProp.

    ("OfferHeader" "OfferHeader_SourceLocation" ) object:findProperty ?OfferHeader_SourceLocationProp.
    ("ShipmentPoint" "ShipmentPoint_CodeCRM") object:findProperty ?ShipmentPoint_CodeCRMProp.

    ("OfferHeader" "OfferHeader_Route") object:findProperty ?OfferHeader_RouteProp.
    ("Route" "Route_ID") object:findProperty ?Route_IDProp.

    ("OfferHeader" "OfferHeader_EvaluationType" ) object:findProperty ?OfferHeader_EvaluationTypeProp.
    ("EvaluationType" "EvaluationType_CodeCRM") object:findProperty ?EvaluationType_CodeCRMProp.

    ("OfferHeader" "OfferHeader_ShipmentType" ) object:findProperty ?OfferHeader_ShipmentTypeProp.
    ("ShipmentMode" "ShipmentMode_ExternalCode") object:findProperty ?ShipmentMode_ExternalCodeProp.

    ("OfferHeader" "OfferHeader_Incoterms") object:findProperty ?OfferHeader_IncotermsProp.
    ("Incoterms" "Incoterms_CodeCRM" ) object:findProperty ?Incoterms_CodeCRMProp.

    ("OfferHeader" "OfferHeader_Mill") object:findProperty ?OfferHeader_MillProp.
    ("PartyInvolved" "PartyInvolved_BusinessPartner" ) object:findProperty ?PartyInvolved_BusinessPartnerProp.
    ("BusinessPartner" "BusinessPartner_OrganizationalModel" ) object:findProperty ?BusinessPartner_OrganizationalModelProp.
    ("OrganizationalModel" "OrganizationalModel_ID") object:findProperty ?OrganizationalModel_IDProp.

    session:context var:product ?productVal.

    ?item ?OfferOrderItem_NumberProp ?OfferOrderItem_NumberVal.

    ?item ?OfferOrderItem_QuantityProp ?OfferOrderItem_QuantityVal.


    #?item ?OfferOrderItem_IncotermsProp ?OfferOrderItem_IncotermsVal.


    #?item ?OfferOrderItem_ProductProp ?OfferOrderItem_ProductVal.
    #?OfferOrderItem_ProductVal ?Product_ExternalIDProp ?Product_ExternalIDVal.

    ?OfferOrderItem_ProductVal ?Product_DescriptionProp ?Product_DescriptionVal.

    ?OfferOrderItem_ProductVal ?Product_UnitOfMeasureProp ?Product_UnitOfMeasureVal.
    ?Product_UnitOfMeasureVal ?UnitOfMeasure_CodeCRMProp ?UnitOfMeasure_CodeCRMVal.


    ?item ?OfferOrderItem_OfferHeaderProp ?OfferOrderItem_OfferHeaderVal.
    ?OfferOrderItem_OfferHeaderVal ?OfferHeader_StockProp ?OfferHeader_StockVal.
    ?OfferHeader_StockVal ?Stock_CodeCRMProp ?Stock_CodeCRMVal.
    (?Stock_CodeCRMVal 4)string:substring ?Stock_CodeCRMSubVal.

    ?OfferOrderItem_OfferHeaderVal ?OfferHeader_IncotermsProp ?OfferHeader_IncotermsVal.
    ?OfferHeader_IncotermsVal ?Incoterms_CodeCRMProp ?Incoterms_CodeCRMVal.





    #?item ?OfferOrderItem_OrganizationalModel_MillProp ?OfferOrderItem_OrganizationalModel_MillVal.
    #?OfferOrderItem_OrganizationalModel_MillVal ?OrganizationalModel_IDProp ?OrganizationalModel_IDVal.

    #if {(?OrganizationalModel_IDVal) string:contains "ZVD_"}
    #then {(?OrganizationalModel_IDVal 4)string:substring ?OrganizationalModel_IDSubVal. }
    #else {?OrganizationalModel_IDVal -> ?OrganizationalModel_IDSubVal }.

    ?OfferOrderItem_OfferHeaderVal ?OfferHeader_MillProp ?OfferHeader_MillVal.
    ?OfferHeader_MillVal ?PartyInvolved_BusinessPartnerProp ?PartyInvolved_BusinessPartnerVal.
    ?PartyInvolved_BusinessPartnerVal ?BusinessPartner_OrganizationalModelProp ?BusinessPartner_OrganizationalModelVar.
    ?BusinessPartner_OrganizationalModelVar ?OrganizationalModel_IDProp ?OrganizationalModel_IDVal.

    if {(?OrganizationalModel_IDVal) string:contains "ZVD_"}
    then {(?OrganizationalModel_IDVal 4)string:substring ?OrganizationalModel_IDSubVal. }
    else {?OrganizationalModel_IDVal -> ?OrganizationalModel_IDSubVal }.

    ?OfferOrderItem_OfferHeaderVal ?OfferHeader_IncotermsLocationProp ?OfferHeader_IncotermsLocationVal.

    ?OfferOrderItem_OfferHeaderVal ?OfferHeader_PayTermProp ?OfferHeader_PayTermVal.
    ?OfferHeader_PayTermVal ?PayTerm_ExternalCodeProp ?PayTerm_ExternalCodeVal.

    #?OfferOrderItem_OfferHeaderVal ?OfferHeader_OverdeliveryToleranceProp ?OfferHeader_OverdeliveryToleranceVal.

    #?OfferOrderItem_OfferHeaderVal ?OfferHeader_UnderdeliveryToleranceProp ?OfferHeader_UnderdeliveryToleranceVal.

    #?OfferOrderItem_OfferHeaderVal ?OfferHeader_SourceLocationProp ?OfferHeader_SourceLocationVal.
    #?OfferHeader_SourceLocationVal ?ShipmentPoint_CodeCRMProp ?ShipmentPoint_CodeCRMVal.

    ?OfferOrderItem_OfferHeaderVal ?OfferHeader_RouteProp ?OfferHeader_RouteVal.
    ?OfferHeader_RouteVal ?Route_IDProp ?Route_IDVal.

    #?OfferOrderItem_OfferHeaderVal ?OfferHeader_EvaluationTypeProp ?OfferHeader_EvaluationTypeVal.
    #?OfferHeader_EvaluationTypeVal ?EvaluationType_CodeCRMProp ?EvaluationType_CodeCRMVal.

    ?OfferOrderItem_OfferHeaderVal ?OfferHeader_ShipmentTypeProp ?OfferHeader_ShipmentTypeVal.
    ?OfferHeader_ShipmentTypeVal ?ShipmentMode_ExternalCodeProp ?ShipmentMode_ExternalCodeVal.

    #var:product2 operator:add ?item.
    #(?item var:MaterialNumberLong) operator:replace ?Product_ExternalIDVal.
    #(?item var:MaterialEnteredLong) operator:replace ?Product_ExternalIDVal.

    #var:product operator:add ?item.
    #(?item var:DocumentItem2) operator:replace var:product2.
    #(?item var:ShippingType) operator:replace ?ShipmentMode_ExternalCodeVal.

    var:offerItems operator:add ?item.
    (?item var:ItemNumber) operator:replace ?OfferOrderItem_NumberVal.
    (?item var:DocumentItem) operator:replace ?productVal.
    (?item var:SalesOrderItemShortText) operator:replace ?Product_DescriptionVal.
    (?item var:TargetQuantityInSalesUnits) operator:replace ?OfferOrderItem_QuantityVal.
    (?item var:IncotermsPartOne) operator:replace ?Incoterms_CodeCRMVal.
    (?item var:StorageLocation) operator:replace ?Stock_CodeCRMSubVal.
    (?item var:Plant) operator:replace ?OrganizationalModel_IDSubVal.
    (?item var:TargetQuantityUnitInISO) operator:replace ?UnitOfMeasure_CodeCRMVal.
    (?item var:IncotermsPartTwo) operator:replace ?OfferHeader_IncotermsLocationVal.
    (?item var:PaymentKeyTerms) operator:replace ?PayTerm_ExternalCodeVal.    
    #(?item var:OverdeliveryToleranceLimit) operator:replace ?OfferHeader_OverdeliveryToleranceVal.    
    #(?item var:UnderdeliveryToleranceLimit) operator:replace ?OfferHeader_UnderdeliveryToleranceVal.
    #(?item var:ShippingPointOrReceivingPoint) operator:replace ?ShipmentPoint_CodeCRMVal.
    (?item var:Route) operator:replace ?Route_IDVal.
    #(?item var:ValuationType) operator:replace ?EvaluationType_CodeCRMVal.   

    true -> ?value.
}


@prefix cmw: <http://comindware.com/logics#>. 
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix object: <http://comindware.com/ontology/object#>.

@prefix string: <http://comindware.com/logics/string#>.
{
    ("OrderHeader" "OrderHeader_IDS4") object:findProperty ?OrderHeader_IDS4Property.
    session:context var:var ?varVal.
    ?varVal var:IDOC ?IDOCVal.
    ?IDOCVal var:SalesOrderData ?SalesOrderDataVal.
    ?SalesOrderDataVal var:DocumentNumber ?DocumentNumberVal.
    (?DocumentNumberVal "^0+" "" ) string:regexReplace ?result.

    if {?order ?OrderHeader_IDS4Property ?result.}

    then { ?order -> ?value.}
    else { "empty" -> ?value.}.

}


@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.
@prefix cmwlist: <http://comindware.com/logics/list#>.
@prefix assert: <http://comindware.com/logics/assert#>.

{

    ("Protokoltsen" "pozitsii") object:findProperty ?pozitsiiProperty.
    ("pozitsiipts"  "chislo") object:findProperty ?chisloProperty.
    ("Protokoltsen" "chislo1") object:findProperty ?firstIndexProperty.
    ("Protokoltsen"  "isFourPos") object:findProperty ?isFourPosProperty.

    {
        ?item ?pozitsiiProperty ?pozitsiiVal.
    } assert:count ?countVal. # Подсчитываем кол-во позиций

    (?countVal 4) cmwnullable:remainder ?resultReminder. # Если значение количество позиций делится на 4 без остатка возвращаем true иначе false

    if {?resultReminder == 0.  }# Если делится 
    then {

        (?countVal 0.25) cmwnullable:product ?firstIndexVal. # Получаем нужный индекс позиции (N*0.25)
        (?firstIndexVal  1) cmwnullable:sum ?secondIndexVal.  # Получаем индекс второго элемента (N*0.25)+1

        from {
            ?item ?pozitsiiProperty ?pozitsiiVal1.        # Берем все позиции
            ?pozitsiiVal1 ?chisloProperty ?chisloPropertyVal.  # У позиций берем значение числа

        } select ?chisloPropertyVal -> ?chisloPropertyValList.  # Получаем лист со списками значений числа у каждой позиции

        ?chisloPropertyValList cmwlist:ascending ?chisloPropertyValListSorted.        # Сортируем список по возрастанию

        (?chisloPropertyValListSorted ?firstIndexVal) cmwlist:at ?valOfFirstIndexVal.    # Получаем значение из списка по первому индексу
        (?chisloPropertyValListSorted ?secondIndexVal) cmwlist:at ?valOsecondIndexValVal.  # Получаем значение из списка по второму индексу

        (?valOfFirstIndexVal ?valOsecondIndexValVal)cmwnullable:average ?resultVal.      # Находим среднее между этими значениями

        ?resultVal -> ?value.                                # Возвращаем данное значение
    }
    else
    {
        from {
            ?item ?pozitsiiProperty ?pozitsiiVal1.          # Берем все позиции
            ?pozitsiiVal1 ?chisloProperty ?chisloPropertyVal1.    # У позиций берем значение числа

        } select ?chisloPropertyVal1 -> ?chisloPropertyValList1.  # Получаем лист со списками значений числа у каждой позиции

        ?chisloPropertyValList1 cmwlist:ascending ?chisloPropertyValListSorted1.  # Сортируем список по возрастанию

        (?countVal 0.25) cmwnullable:product ?firstIndexVal.          # Получаем индекс для первого элемента (N*0.25)
        ?firstIndexVal cmwnullable:ceiling ?firstIndexValAfterCell.       # Округляем его в большую сторону 4.2 -> 5

        (?chisloPropertyValListSorted1 ?firstIndexValAfterCell) cmwlist:at ?ValfirstIndexValAfterCell. # Получаем значение из списка по индексу после округления
        ?ValfirstIndexValAfterCell -> ?value.            # Возвращаем реузльтат
    }
}



@prefix object: <http://comindware.com/ontology/object#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix list: <http://www.w3.org/2000/10/swap/list#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix ui: <http://comindware.com/ontology/ui#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix cmw: <http://comindware.com/logics#>.
@prefix cmwmath: <http://comindware.com/logics/math#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.

{
    ("MillTransportRate" "MillTransportRate_OrganizationalModel" ) object:findProperty ?MillRateOrgUnitProp.
    ("MillTransportRate" "MillTransportRate_Incoterms" ) object:findProperty ?MillRateIncotermProp.
    ("MillTransportRate" "MillTransportRate_Location" ) object:findProperty ?MillRateLocationProp.
    ("MillTransportRate" "MillTransportRate_EffectiveDate" ) object:findProperty ?MillRateEffDateProp.
    ("MillTransportRate" "MillTransportRate_CostUS" ) object:findProperty ?MillRateCostUSProp.

    ("ICSearchResults" "ICSearchResults_IcpricingHeader") object:findProperty ?ICSRHeaderProp.

    ("IcpricingHeader" "IcpricingHeader_BusinessPartner_Mill") object:findProperty ?ICPHMillBPProp.

    ("BusinessPartner" "BusinessPartner_OrganizationalModel" ) object:findProperty ?BPOrgModelProp.

    ("Incoterms" "Incoterms_CodeCRM" ) object:findProperty ?IncotermsCodeProp.

    ("Location" "Location_CodeCRM") object:findProperty ?LocationCodeProp.

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

    ?item ?ICSRHeaderProp ?ICPHeader1.
    ?ICPHeader1 ?ICPHMillBPProp ?MillBP1.
    ?MillBP1 ?BPOrgModelProp ?MillOrgModel1.
    ?MillRates1 ?MillRateOrgUnitProp ?MillOrgModel1.
    ?MillRates1 ?MillRateIncotermProp ?MillRateIncoterm1.
    ?MillRateIncoterm1 ?IncotermsCodeProp "FOB".
    ?MillRates1 ?MillRateLocationProp ?MillRateLocation1.
    ?MillRateLocation1 ?LocationCodeProp "221". 
    ?MillRates1 ?MillRateEffDateProp ?MillRateDatesMax.
    ?MillRates1 ?MillRateCostUSProp ?MillRateCostUSVal1.
    ?MillRateCostUSVal1 -> ?value.

}


@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix convert: <http://comindware.com/logics/convertions#>.
{
    ("test1"  "pair") object:findProperty ?pairProperty.
    ("PAIR"  "Spisokznacheniy") object:findProperty ?SpisokznacheniyProperty.

    ?item ?pairProperty ?pairVal.
    ("Spisokznacheniy" "cancelled") convert:enumValue ?enumVal.
    ?pairVal ?SpisokznacheniyProperty ?enumVal.

    ?pairVal -> ?value.

}


@prefix object: <http://comindware.com/ontology/object#>.
@prefix document: <http://comindware.com/ontology/document#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.
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


@prefix object: <http://comindware.com/ontology/object#>.
@prefix document: <http://comindware.com/ontology/document#>.
@prefix operator: <http://comindware.com/ontology/session/operator#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix var: <http://comindware.com/ontology/session/variable#>.
{
    ("Dokumenty" "Fayl") object:findProperty ?FaylProperty.

    ?item ?FaylProperty ?FaylData.
    ?FaylData document:content ?Document.

    ("data:image/jpeg;base64,{0}" ?Document) string:format ?newString.

    var:metersPhoto operator:add ?newString.

    true -> ?value.
}



@prefix cmw: <http://comindware.com/logics#>. 
@prefix account: <http://comindware.com/ontology/account#>. 
@prefix string: <http://www.w3.org/2000/10/swap/string#>. 
@prefix object: <http://comindware.com/ontology/object#>.
{ 
    ("BusinessPartnerRelation"  "SozdatelTekhNeudalyat") object:findProperty ?CreatorProperty.
    ("BusinessPartnerRelation" "Tipotnosheniy") object:findProperty ?Tipotnosheniy.
    ("BusinessPartnerRelation"  "BusinessPartnerRelation_BusinessPartner_1") object:findProperty ?BusinessPartnerRelation_BusinessPartner_1Property.
    ("BusinessPartner"  "Kategoriya") object:findProperty ?KategoriyaProperty.
    ("Tipyotnosheniy"  "Kod") object:findProperty ?TipyotnosheniyKodProperty.
    ("Sotrudnikikontragentov" "Kontragent") object:findProperty ?KontragentProperty.
    ("Sotrudnikikontragentov" "Akkaunt") object:findProperty ?AkkauntProperty.
    ("Kontragenty" "Tipkontragenta" ) object:findProperty ?TipkontragentaProperty.
    ("Tipykontragentov"  "Kod") object:findProperty ?TipykontragentovKodProperty.
    ("Kategoriidelovykhpartnerov"  "Kod") object:findProperty ?KategoriidelovykhpartnerovKodProperty.
    ("BusinessPartner"  "BusinessPartner_Company") object:findProperty ?BusinessPartner_CompanyProperty.

    ?TypeKompany ?KategoriidelovykhpartnerovKodProperty "Company".		# Находим id записи в справочнике типов стороны с кодом Company
    ?typeKlient ?TipykontragentovKodProperty "Klient".					# Находим id записи в справочнике типов компании с кодом Klient

    ?otnoshenieYrLic ?TipyotnosheniyKodProperty "conductsBusinessThroughLegalEntity". # Находим запись в типах отношений с кодом conductsBusinessThroughLegalEntity

    if {?item ?Tipotnosheniy ?otnoshenieYrLic.}							# Если отношения с юр лицом
    then { ?value a account:Account.}									# Выводить всем
    else { 
        if { ?item ?BusinessPartnerRelation_BusinessPartner_1Property ?BusinessPartnerRelation_BusinessPartner_1Val. 		# У отношения берем сторону 1
            ?BusinessPartnerRelation_BusinessPartner_1Val ?KategoriyaProperty ?TypeKompany.								# Проверяем что данная сторона является компанией
            ?BusinessPartnerRelation_BusinessPartner_1Val ?BusinessPartner_CompanyProperty ?BusinessPartner_CompanyVal.	# Берем у стороны компанию
            ?BusinessPartner_CompanyVal ?TipkontragentaProperty ?Tipkontragenta.											# Берем тип у компании
            ?Tipkontragenta == ?typeKlient.}							# Если компания с типом Клиент
        then {?item ?CreatorProperty ?CreatorVal. 						# Берем создателя у отношения
              ?RecordsKontragent ?AkkauntProperty ?CreatorVal. 			# Из контактных лиц находим запись в которой сотрудник равен создателю из отношения
              ?RecordsKontragent ?KontragentProperty ?KontragentVal. 	# Берем из этой записи компанию
              ?RecordsEmployee ?KontragentProperty ?KontragentVal. 		# Находим все записи с данной компанией
              ?RecordsEmployee ?AkkauntProperty ?value. }				# Берем всех сотрудников этой компании
        else {?value a account:Account. }.								# Выводим всем
    }.

}




@prefix cmw: <http://comindware.com/logics#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.
@prefix object: <http://comindware.com/ontology/object#>.
{
    ("ProjectPlans" "Duedate") object:findProperty ?duedate.
    ("ProjectPlans" "Datazaversheniyraboty") object:findProperty ?datazaversheniyraboty.


    session:context session:requestTime ?now.
    ?now cmwnullable:startOfDay ?nowstart.
    ?template object:alias "ProjectPlans".
  ?item cmw:container ?template.

    if {not{?item ?datazaversheniyraboty ?.}.}
    then{?item ?duedate ?duedateval.
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

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmw: <http://comindware.com/logics#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix process: <http://comindware.com/ontology/process#>.
@prefix w3string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
@prefix cmwlist: <http://comindware.com/logics/list#>.
@prefix assert: <http://comindware.com/logics/assert#>.
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

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix document: <http://comindware.com/ontology/document#>.
{
    ("Documents"  "Document_Attachment") object:findProperty ?foundProperty.

    ?item ?foundProperty ?doc.
   	?doc document:title ?title.
    ("<p><a href='https://system.bau.cbap.ru/DocumentContent?id={0}'>Ссылка на файл {1}</a></p>" ?doc ?title) string:format ?value.
    
}


@prefix object: <http://comindware.com/ontology/object#>.
@prefix list: <http://www.w3.org/2000/10/swap/list#>.



{
    ("istoriyasoglasovaniya_smni" "Zayavka") object:findProperty ?ZayavkaProperty.
	("Zayavka?" "PP") object:findProperty ?PPProperty.
    ("PP?" "TestNumeratsiya") object:findProperty ?TestNumeratsiyaProperty.
    
    ?item ?ZayavkaProperty ?ZayavkaVal.
    ?ZayavkaVal ?PPProperty ?PPVal.
    from { ?PPVal ?TestNumeratsiya ?TestNumeratsiyaVal. }
	select ?PPVal -> ?PPValList.
   
   ?PPValList list:ascending ?value.
}
#from a in db->istoriyasoglasovaniya_smni where (a->id == $istoriyasoglasovaniya) orderby a->Zayavka->PP->TestNumeratsiya select a->id

@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix cmwnullable: <http://comindware.com/ontology/entity/nullable#>.
@prefix list: <http://www.w3.org/2000/10/swap/list#>.
@prefix cmwmath: <http://comindware.com/logics/math#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.

{

    ("PriceProtocolHeader" "PriceProtocolHeader_PriceProtocolItem") object:findProperty ?PriceProtocolHeader_PriceProtocolItemProperty.

    ("PriceProtocolItem"  "PriceProtocolItem_Status") object:findProperty ?PriceProtocolItem_StatusProperty.
    ("PriceProtocolItem"   "PriceProtocolItem_Step") object:findProperty ?PriceProtocolItem_StepProperty.
    ("PriceProtocolItem"   "PriceProtocolItem_Price") object:findProperty ?PriceProtocolItem_PriceProperty.

    ("Step"  "Step_Code") object:findProperty ?Step_CodeProperty.

    ("Status" "Status_Code") object:findProperty ?Status_CodeProperty.



    from {
        ?item ?PriceProtocolHeader_PriceProtocolItemProperty ?PriceProtocolHeader_PriceProtocolItemVal.
        ?PriceProtocolHeader_PriceProtocolItemVal ?PriceProtocolItem_StatusProperty ?PriceProtocolItem_StatusVal.
        ?PriceProtocolItem_StatusVal ?Status_CodeProperty ?Status_CodeVal.

        ?PriceProtocolHeader_PriceProtocolItemVal ?PriceProtocolItem_StepProperty ?PriceProtocolItem_StepVal.
        ?PriceProtocolItem_StepVal ?Step_CodeProperty ?Step_CodeVal.

        or
        {
            ?PriceProtocolHeader_PriceProtocolItemVal ?PriceProtocolItem_PriceProperty ?PriceProtocolItem_PriceVal.
        }
        or
        {
            0 -> ?PriceProtocolItem_PriceVal.
        }.

    } select (?Status_CodeVal ?Step_CodeVal ?PriceProtocolItem_PriceVal) -> ?detailingList.

    from {
        ?detailingList list:member ?datailingListMember1.
        ?datailingListMember1 -> (?code1 ?step1 ?total1).
        ?step1 == "365".

    } select ?total1 -> ?total1List.

    or
	{
		?total1List cmwnullable:max ?result.
        ?result != 0.
	}
	or
	{
		1 -> ?result.
	}.
    
     from {
        ?detailingList list:member ?datailingListMember2.
        ?datailingListMember2 -> (?code2 ?step2 ?total2).
        ?step2 == "362".

    } select ?total2 -> ?total1List2.

    or
	{
		?total1List2 cmwnullable:max ?result2.
        ?result2 != 0.
	}
	or
	{
		1 -> ?result2.
	}.
    
     from {
        ?detailingList list:member ?datailingListMember3.
        ?datailingListMember3 -> (?code3 ?step3 ?total3).
        ?code3 == "ZPP".

    } select ?total3 -> ?total1List3.

  or
	{
		?total1List3 cmwnullable:max ?result3.
	}
	or
	{
		0 -> ?result3.
	}.

    ?result3 -> ?value.
}
```

``` turtle
@prefix string: <http://comindware.com/logics/string#>.
@prefix object: <http://comindware.com/ontology/object#>.

{
    ("CertificateItem" "CertificateItem_ClaimHeader_CertPosAdd") object:findProperty ?CertificateItem_ClaimHeader_CertPosAddProperty.
    ("CertificateItem" "CertificateItem_CertificateNumber") object:findProperty ?CertificateItem_CertificateNumberProperty.
    ("CertificateItem" "CertificateItem_CertificateDate") object:findProperty ?CertificateItem_CertificateDateProperty.
    ("CertificateItem" "CertificateItem_CertificateItem") object:findProperty ?CertificateItem_CertificateItemProperty.
    ("CertificateItem" "CertificateItem_InvoiceNumber") object:findProperty ?CertificateItem_InvoiceNumberProperty.
    ("CertificateItem" "CertificateItem_InvoiceItem") object:findProperty ?CertificateItem_InvoiceItemProperty.
    ("CertificateItem" "CertificateItem_InvoiceDate") object:findProperty ?CertificateItem_InvoiceDateProperty.
    ("CertificateItem" "CertificateItem_ProductItemNumber") object:findProperty ?CertificateItem_ProductItemNumberProperty.
    ("CertificateItem" "CertificateItem_SmeltingNumber") object:findProperty ?CertificateItem_SmeltingNumberProperty.
    ("CertificateItem" "CertificateItem_RollPackSlabNumber") object:findProperty ?CertificateItem_RollPackSlabNumberProperty.
    ("CertificateItem" "CertificateItem_PlaceNumber") object:findProperty ?CertificateItem_PlaceNumberProperty.

    ("ClaimHeader" "ClaimHeader_ClaimItem") object:findProperty ?ClaimHeader_ClaimItemProperty.
    ("ClaimItem" "ClaimItem_CertificateNumberTECHLoad") object:findProperty ?ClaimItem_CertificateNumberTECHLoadProperty.
    ("ClaimItem" "ClaimItem_CertificateDateTECHLoad") object:findProperty ?ClaimItem_CertificateDateTECHLoadProperty.
    ("ClaimItem" "ClaimItem_CertificateItemTECHLoad") object:findProperty ?ClaimItem_CertificateItemTECHLoadProperty.
    ("ClaimItem" "ClaimItem_InvoiceNumberTECHLoad") object:findProperty ?ClaimItem_InvoiceNumberTECHLoadProperty.
    ("ClaimItem" "ClaimItem_InvoiceItemTECHLoad") object:findProperty ?ClaimItem_InvoiceItemTECHLoadProperty.
    ("ClaimItem" "ClaimItem_InvoiceDateTECHLoad") object:findProperty ?ClaimItem_InvoiceDateTECHLoadProperty.
    ("ClaimItem" "ClaimItem_ProductItemNoTECHLoad") object:findProperty ?ClaimItem_ProductItemNoTECHLoadProperty.
    ("ClaimItem" "ClaimItem_HeatNoTECHLoad") object:findProperty ?ClaimItem_HeatNoTECHLoadProperty.
    ("ClaimItem" "ClaimItem_RollPackSlabNumberTex") object:findProperty ?ClaimItem_RollPackSlabNumberTexProperty.
    ("ClaimItem" "ClaimItem_PlaceNumber") object:findProperty ?ClaimItem_PlaceNumberProperty.


    ?item ?CertificateItem_ClaimHeader_CertPosAddProperty ?CertificateItem_ClaimHeader_CertPosAddVal.
    ?CertificateItem_ClaimHeader_CertPosAddVal ?ClaimHeader_ClaimItemProperty ?ClaimHeader_ClaimItemVal.

    or{
        ?ClaimHeader_ClaimItemVal -> ?ClaimHeader_ClaimItemVal1.
        ?item ?CertificateItem_SmeltingNumberProperty ?CertificateItem_SmeltingNumberVal.
        ?CertificateItem_SmeltingNumberVal string:trim ?trimedCertificateItem_SmeltingNumber.


        ?item ?CertificateItem_RollPackSlabNumberProperty ?CertificateItem_RollPackSlabNumberVal.
        ?CertificateItem_RollPackSlabNumberVal string:trim ?trimedCertificateItem_RollPackSlabNumber.

        ?ClaimHeader_ClaimItemVal1 ?ClaimItem_RollPackSlabNumberTexProperty ?ClaimItem_RollPackSlabNumberTexLoadVal.
        ?ClaimItem_RollPackSlabNumberTexLoadVal string:trim ?trimedClaimItem_RollPackSlabNumberTexLoad.


        ?ClaimHeader_ClaimItemVal1 ?ClaimItem_HeatNoTECHLoadProperty ?ClaimItem_HeatNoTECHLoadVal.
        ?ClaimItem_HeatNoTECHLoadVal string:trim ?trimedClaimItem_HeatNoTECHLoad.

        ?trimedCertificateItem_RollPackSlabNumber == ?trimedClaimItem_RollPackSlabNumberTexLoad.
        ?trimedCertificateItem_SmeltingNumber == ?trimedClaimItem_HeatNoTECHLoad.

        ?ClaimHeader_ClaimItemVal1 -> ?ClaimHeader_ClaimItemValResult.
    }

    or {
        ?ClaimHeader_ClaimItemVal -> ?ClaimHeader_ClaimItemVal2.

        ?item ?CertificateItem_CertificateNumberProperty ?CertificateItem_CertificateNumberVal.
        ?CertificateItem_CertificateNumberVal string:trim ?trimedCertificateItem_CertificateNumber.

        ?item ?CertificateItem_CertificateDateProperty ?CertificateItem_CertificateDateVal.

        ?item ?CertificateItem_CertificateItemProperty ?CertificateItem_CertificateItemVal.
        ?CertificateItem_CertificateItemVal string:trim ?trimedCertificateItem_CertificateItem.

        ?ClaimHeader_ClaimItemVal2 ?ClaimItem_CertificateNumberTECHLoadProperty ?ClaimItem_CertificateNumberTECHLoadVal.
        ?ClaimItem_CertificateNumberTECHLoadVal string:trim ?trimedClaimItem_CertificateNumberTECHLoad.

        ?ClaimHeader_ClaimItemVal2 ?ClaimItem_CertificateDateTECHLoadProperty ?ClaimItem_CertificateDateTECHLoadVal.

        ?ClaimHeader_ClaimItemVal2 ?ClaimItem_CertificateItemTECHLoadProperty ?ClaimItem_CertificateItemTECHLoadVal.
        ?ClaimItem_CertificateItemTECHLoadVal string:trim ?trimedClaimItem_CertificateItemTECHLoad.

        ?trimedCertificateItem_CertificateNumber == ?trimedClaimItem_CertificateNumberTECHLoad.
        ?CertificateItem_CertificateDateVal == ?ClaimItem_CertificateDateTECHLoadVal.
        ?trimedCertificateItem_CertificateItem == ?trimedClaimItem_CertificateItemTECHLoad.

        ?ClaimHeader_ClaimItemVal2 -> ?ClaimHeader_ClaimItemValResult.
    }

    or {
        ?ClaimHeader_ClaimItemVal -> ?ClaimHeader_ClaimItemVal3.

        ?item ?CertificateItem_InvoiceNumberProperty ?CertificateItem_InvoiceNumberVal.
        ?CertificateItem_InvoiceNumberVal string:trim ?trimedCertificateItem_InvoiceNumber.

        ?item ?CertificateItem_InvoiceItemProperty ?CertificateItem_InvoiceItemVal.
        ?CertificateItem_InvoiceItemVal string:trim ?trimedCertificateItem_InvoiceItem.

        ?item ?CertificateItem_InvoiceDateProperty ?CertificateItem_InvoiceDateVal.

        ?ClaimHeader_ClaimItemVal3 ?ClaimItem_InvoiceNumberTECHLoadProperty ?ClaimItem_InvoiceNumberTECHLoadVal.
        ?ClaimItem_InvoiceNumberTECHLoadVal string:trim ?trimedClaimItem_InvoiceNumberTECHLoad.

        ?ClaimHeader_ClaimItemVal3 ?ClaimItem_InvoiceItemTECHLoadProperty ?ClaimItem_InvoiceItemTECHLoadVal.
        ?ClaimItem_InvoiceItemTECHLoadVal string:trim ?trimedClaimItem_InvoiceItemTECHLoad.

        ?ClaimHeader_ClaimItemVal3 ?ClaimItem_InvoiceDateTECHLoadProperty ?ClaimItem_InvoiceDateTECHLoadVal.

        ?trimedCertificateItem_InvoiceNumber == ?trimedClaimItem_InvoiceNumberTECHLoad.
        ?trimedCertificateItem_InvoiceItem == ?trimedClaimItem_InvoiceItemTECHLoad.
        ?CertificateItem_InvoiceDateVal == ?ClaimItem_InvoiceDateTECHLoadVal.

        ?ClaimHeader_ClaimItemVal3 -> ?ClaimHeader_ClaimItemValResult.
    }

    or {
        ?ClaimHeader_ClaimItemVal -> ?ClaimHeader_ClaimItemVal4.

        ?item ?CertificateItem_ProductItemNumberProperty ?CertificateItem_ProductItemNumberVal.
        ?CertificateItem_ProductItemNumberVal string:trim ?trimedCertificateItem_ProductItemNumber.

        ?item ?CertificateItem_SmeltingNumberProperty ?CertificateItem_SmeltingNumberVal.
        ?CertificateItem_SmeltingNumberVal string:trim ?trimedCertificateItem_SmeltingNumber.


        ?ClaimHeader_ClaimItemVal4 ?ClaimItem_ProductItemNoTECHLoadProperty ?ClaimItem_ProductItemNoTECHLoadVal.
        ?ClaimItem_ProductItemNoTECHLoadVal string:trim ?trimedClaimItem_ProductItemNoTECHLoad.

        ?ClaimHeader_ClaimItemVal4 ?ClaimItem_HeatNoTECHLoadProperty ?ClaimItem_HeatNoTECHLoadVal.
        ?ClaimItem_HeatNoTECHLoadVal string:trim ?trimedClaimItem_HeatNoTECHLoad.

        ?trimedCertificateItem_ProductItemNumber == ?trimedClaimItem_ProductItemNoTECHLoad.
        ?trimedCertificateItem_SmeltingNumber == ?trimedClaimItem_HeatNoTECHLoad.

        ?ClaimHeader_ClaimItemVal4 -> ?ClaimHeader_ClaimItemValResult.
    }

    or {
        ?ClaimHeader_ClaimItemVal -> ?ClaimHeader_ClaimItemVal5.

        ?item ?CertificateItem_PlaceNumberProperty ?CertificateItem_PlaceNumberVal.
        ?CertificateItem_PlaceNumberVal string:trim ?trimedCertificateItem_PlaceNumber.

        ?item ?CertificateItem_SmeltingNumberProperty ?CertificateItem_SmeltingNumberVal.
        ?CertificateItem_SmeltingNumberVal string:trim ?trimedCertificateItem_SmeltingNumber.

        ?ClaimHeader_ClaimItemVal5 ?ClaimItem_PlaceNumberProperty ?ClaimItem_PlaceNumberVal.
        ?ClaimItem_PlaceNumberVal string:trim ?trimedClaimItem_PlaceNumber.


        ?ClaimHeader_ClaimItemVal5 ?ClaimItem_HeatNoTECHLoadProperty ?ClaimItem_HeatNoTECHLoadVal.
        ?ClaimItem_HeatNoTECHLoadVal string:trim ?trimedClaimItem_HeatNoTECHLoad.

        ?trimedCertificateItem_PlaceNumber == ?trimedClaimItem_PlaceNumber.
        ?trimedCertificateItem_SmeltingNumber == ?trimedClaimItem_HeatNoTECHLoad.

        ?ClaimHeader_ClaimItemVal5 -> ?ClaimHeader_ClaimItemValResult.
    }

    or {
        ?ClaimHeader_ClaimItemVal -> ?ClaimHeader_ClaimItemVal6.    

        ?item ?CertificateItem_ProductItemNumberProperty ?CertificateItem_ProductItemNumberVal.
        ?CertificateItem_ProductItemNumberVal string:trim ?trimedCertificateItem_ProductItemNumber.

        ?ClaimHeader_ClaimItemVal6 ?ClaimItem_ProductItemNoTECHLoadProperty ?ClaimItem_ProductItemNoTECHLoadVal.
        ?ClaimItem_ProductItemNoTECHLoadVal string:trim ?trimedClaimItem_ProductItemNoTECHLoad.

        ?trimedCertificateItem_ProductItemNumber == ?trimedClaimItem_ProductItemNoTECHLoad.

        ?ClaimHeader_ClaimItemVal6 -> ?ClaimHeader_ClaimItemValResult.
    }.

    ?ClaimHeader_ClaimItemValResult -> ?value.
}
```

``` turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.

{

  ?task task:objectId ?item.
  ?task cmw:taskStatus taskStatus:inProgress.
    
    ?task -> ?value.

}
```

``` turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix container: <http://comindware.com/ontology/container#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
@prefix session: <http://comindware.com/ontology/session#>.
@prefix list: <http://www.w3.org/2000/10/swap/list#>.
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

``` turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix object: <http://comindware.com/ontology/object#>.
{
    cmw:securityContext cmw:currentUser ?user.
    ?group account:groupName "test". #получаем группу
    ?user account:userGroupMembership ?group. 
    ?true -> ?value.
}
```

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmw: <http://comindware.com/logics#>.
@prefix session: <http://comindware.com/ontology/session#>.
{
    ("ProjectPlans" "Otvetstvennyy") object:findProperty ?contact.
    
	cmw:securityContext cmw:currentUser ?user.
	?template object:alias "ProjectPlans".
	?item cmw:container ?template.
	?item ?contact ?user.
}
```

``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix list: <http://www.w3.org/2000/10/swap/list#>.


{
    ("LegalEntities" "ProductCategories") object:findProperty ?ProductCategoriesProperty.

    ("Quotas" "ProductCategorieslevel3") object:findProperty ?ProductCategorieslevel3Property.
    ("Quotas" "ProductCategorieslevel2") object:findProperty ?ProductCategorieslevel2Property.
    ("Quotas" "ProductCategorieslevel1") object:findProperty ?ProductCategorieslevel1Property.

    ("ProductCategories" "CommonCategory") object:findProperty ?CommonCategoryProperty.

    from {
        ?item ?ProductCategorieslevel3Property ?ProductCategorieslevel3.
        ?ProductCategorieslevel3 ?CommonCategoryProperty ?CommonCategory3.
        ?LegalEntities3 ?ProductCategoriesProperty ?CommonCategory3.
    }
    select ?LegalEntities3 -> ?LegalEntities3List.

    from {
        ?item ?ProductCategorieslevel2Property ?ProductCategorieslevel2.
        ?ProductCategorieslevel2 ?CommonCategoryProperty ?CommonCategory2.
        ?LegalEntities2 ?ProductCategoriesProperty ?CommonCategory2.
    }
    select ?LegalEntities2 -> ?LegalEntities2List.

    (?LegalEntities3List ?LegalEntities2List) list:append ?LegalEntities32List.

    from {
        ?item ?ProductCategorieslevel1Property ?ProductCategorieslevel1.
        ?ProductCategorieslevel1 ?CommonCategoryProperty ?CommonCategory1.
        ?LegalEntities1 ?ProductCategoriesProperty ?CommonCategory1.
    }
    select ?LegalEntities1 -> ?LegalEntities1List.

    (?LegalEntities32List ?LegalEntities1List) list:append ?LegalEntitiesList.

    ?LegalEntitiesList list:member ?value.
}


@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmw: <http://comindware.com/logics#>.

{
    ("storony_dogovorov" "client") object:findProperty ?faultFeature.
    

	?template object:alias "storony_dogovorov".
	?item cmw:container ?template.
	not{?item ?faultFeature ?.}.


}


@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmw: <http://comindware.com/logics#>.
@prefix account: <http://comindware.com/ontology/account#>.
{
    ("Obraschenie" "Statusobrascheniya" ) object:findProperty ?StatusobrascheniyaProperty.
    ("SpravochnikStatusyobrascheniya" "Kod") object:findProperty ?StatusKodProperty.
    ("Obraschenie" "_creator") object:findProperty ?creatorProperty.
    
   
    
    ?template object:alias "Obraschenie".
	?item cmw:container ?template.
	
    ?item ?StatusobrascheniyaProperty ?StatusobrascheniyaVal.
    ?StatusobrascheniyaVal ?StatusKodProperty ?StatusKodVal.
    ?StatusKodVal == "Q0".
    ?item ?creatorProperty ?creatorVal.
    ?creatorVal != account:systemAccount.




}
```

``` turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix object: <http://comindware.com/ontology/object#>. 
@prefix list: <http://www.w3.org/2000/10/swap/list#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
    ("Perechenzayavok" "ZayavkinarassmotreniiTekhnicheskiy") object:findProperty ?VseZayavki. 
    ("Perechenzayavok" "Istoriyasoglasovaniya") object: findProperty ?UtverZayavki.
    
    from {
        ?item ?VseZayavki ?VseZayavkival.
        {
            ?item ?UtverZayavki ?UtverZayavkival.
            ?UtverZayavkival == ?VseZayavkiVal.
        }
        assert:count 2c.
        ?c == 0.
    } select ?VseZayavkiVal ->?VseZayavkiList.
    ?VseZayavkiList list:member value.
}
```

``` turtle
@prefix session: <http://comindware.com/ontology/session#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmw: <http://comindware.com/logics#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix cmwlocal: <http://comindware.com/logics/time/local#>.
@prefix cmwdur: <http://comindware.com/logics/time/duration#>.
{
    ("Claim" "_creationDate" ) object:findProperty ?CreationDateProperty.

    ?template object:alias "Claim".
    ?item cmw:container ?template.

    session:context session:requestTime ?now.

    "P1D" cmwdur:parseDuration ?DurationVal.
    (?now ?DurationVal)cmwlocal:sub ?nowDayAgo.


    ?template object:alias "Claim".
    ?item cmw:container ?template.

    ?item ?CreationDateProperty ?CreationDateVal.
    ?CreationDateVal cmwlocal:between (?nowDayAgo ?now).

}
```

``` turtle
@prefix cmwsession: <http://comindware.com/ontology/session#>.
@prefix context: <http://comindware.com/ontology/session/context#>.
@prefix axioms: <http://comindware.com/ontology/axioms#>.
@prefix cmwlist: <http://comindware.com/logics/list#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
    {
    cmwsession:context context:selectedIds ?zapis.
    }assert:count 1.
    true -> ?value.
}
```
