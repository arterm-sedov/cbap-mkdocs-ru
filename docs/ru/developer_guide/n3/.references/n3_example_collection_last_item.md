На данном примере рассмотрим, как написать фильтр для отображения в коллекции самой последней записи, созданной в ней. 



Выражение:
``` turtle
@prefix object: <http://comindware.com/ontology/object#>.
@prefix sort: <http://comindware.com/ontology/dataset/sort#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.

{
    ("Document" "_creationDate") object:findProperty ?creationDate.
    ("Document" "_isDisabled") object:findProperty ?isDisabled.
  ("Document" "Otchety") object:findProperty ?Otcheti.
  

    from {
    ?OtchetiVal ?Otcheti ?item.
    not {?OtchetiVal ?isDisabled true.}.
    ?OtchetiVal ?creationDate ?creationDateVal.
    } select ?creationDateVal -> ?creationDateValList.

    (?creationDateValList sort:timeComparer) assert:sort ?orderedCreationDateValList.
    ?orderedCreationDateValList rdf:last ?maxDate.
  once {?OtchetiVal2 ?Otcheti ?item.
    not {?OtchetiVal2 ?isDisabled true.}.
        ?OtchetiVal2 ?creationDate ?maxDate.
  }.

    ?OtchetiVal2 -> ?value.
}
```


1.	Мы объявляем префиксы, с которыми будем работать:

  ```
  @prefix object: <http://comindware.com/ontology/object#>.
  @prefix sort: <http://comindware.com/ontology/dataset/sort#>.
  @prefix assert: <http://comindware.com/logics/assert#>.
  @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
  ```

2.	*Объявляем системное имя шаблона записи, атрибуты, которые будут участвовать в вычислении и присуждаем им некую переменную, так как этого требует язык выражений N3:
    ```
    {
      ("Document" "_creationDate") object:findProperty ?creationDate.
      ("Document" "_isDisabled") object:findProperty ?isDisabled.
      ("Document" "Otchety") object:findProperty ?Otcheti.
    ```
«Document»- шаблон записи, на который ссылается наша коллекция
«Otchety» - обратная ссылка в отчеты, где есть коллекция
«creationDate» - атрибут «дата создания» записи, в «шаблоне записи» «Document»
«isDisabled» - логический атрибут в архиве, в шаблоне записи «Document»


3.	Необходимо указать для какой сущности мы отображаем записи в коллекции, при учете того, что эта запись не должна находится в архиве (необходимо понимать, что в данном случае мы переходим по связанной с коллекцией ссылке чтобы установить ее связь с коллекцией, а затем проверяем запись из коллекции, чтобы она находилась не в архиве)
    ```
    from {
    ?OtchetiVal ?Otcheti ?item.
    not {?OtchetiVal ?isDisabled true.}.
    ```
4.	Далее мы объявляем, в структуре выражения, атрибут «дата создания», после чего выстраиваем список всех записей по дате создания. После чего мы объявляем запись в коллекции с самой большой датой создания.
    
    ```
    ?OtchetiVal ?creationDate ?creationDateVal.
    } select ?creationDateVal -> ?creationDateValList.
    (?creationDateValList sort:timeComparer) assert:sort ?orderedCreationDateValList.
    ?orderedCreationDateValList rdf:last ?maxDate. 

    ```
5.	 Здесь мы объявляем, что нам нужна лишь одна запись, которая не должна быть в архиве и с максимальной датой создания т.е. Самая новая созданная запись в коллекции 
 once {?OtchetiVal2 ?Otcheti ?item.
    not {?OtchetiVal2 ?isDisabled true.}.
        ?OtchetiVal2 ?creationDate ?maxDate.
  }.
    ?OtchetiVal2 -> ?value.
}

ПРИМЕЧАНИЕ 
	В первых четырех пунктах мы объявляем структуру нашего фильтра, все его условия, а в пятом пункте мы конкретизируем его результат, что нам надо выдать как итог. 








