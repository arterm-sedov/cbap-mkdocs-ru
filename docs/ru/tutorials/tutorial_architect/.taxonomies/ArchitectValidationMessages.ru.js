ARCHITECTURE : {
    TEXT : "Архитектура",
    CHILDREN : {
        COLUMNS : {
            TEXT : "",
            CHILDREN : {
                CREATEDBY : { TEXT : "Создатель" },
                CREATEDON : { TEXT : "Дата создания" },
                DIAGRAMNAME : { TEXT : "Название диаграммы" },
                DIAGRAMTYPE : { TEXT : "Тип диаграммы" },
                NAME : { TEXT : "Имя" }
            }
        },
        DEFAULTNAME : { TEXT : "Новая схема архитектуры" },
        DIGRAMTYPE : {
            TEXT : "",
            CHILDREN : {
                ARCHITECTURE : { TEXT : "Архитектурная диаграмма" },
                DATADIAGRAM : { TEXT : "Диаграмма данных" }
            }
        },
        DOCUMENTATION : {
            TEXT : "documentation",
            CHILDREN : {
                PROPERTIES : {
                    TEXT : "",
                    CHILDREN : {
                        PARENTPROCESS : { TEXT : "Родительский процесс" },
                        PARENTPROCESSGROUP : { TEXT : "Родительская группа процессов" },
                        PARENTSUBPROCESS : { TEXT : "Родительский подпроцесс" }
                    }
                },
                TEMPLATENAME : { TEXT : "Конфигурация панели свойств: {0}" },
                TYPES : {
                    TEXT : "",
                    CHILDREN : {
                        ANNOTATIONNONE : { TEXT : "Комментарии" },
                        BPMNGROUP : { TEXT : "BPMN-группа" },
                        DATAOBJECT : { TEXT : "Объекты данных" },
                        DATASTORE : { TEXT : "Хранилища данных" },
                        ENDEVENTCANCEL : { TEXT : "Конечные события-отмены" },
                        ENDEVENTCOMPENSATION : { TEXT : "Конечные события-компенсации" },
                        ENDEVENTERROR : { TEXT : "Конечные события-ошибки" },
                        ENDEVENTESCALATION : { TEXT : "Конечные события-эскалации" },
                        ENDEVENTNONE : { TEXT : "Конечные события" },
                        ENDEVENTTERMINATE : { TEXT : "Конечные события-остановки" },
                        ENDEVENTTHROWINGMESSAGE : { TEXT : "Конечные события-сообщения (инициаторы)" },
                        ENDEVENTTHROWINGMULTIPLE : { TEXT : "Множественные конечные события (инициаторы)" },
                        ENDEVENTTHROWINGSIGNAL : { TEXT : "Конечные события-сигналы (инициаторы)" },
                        FLOWASSOCIATION : { TEXT : "Ассоциативные связи" },
                        FLOWCONDITIONAL : { TEXT : "Conditional flows" },
                        FLOWDATA : { TEXT : "Потоки данных" },
                        FLOWDEFAULT : { TEXT : "Потоки управления «иначе»" },
                        FLOWMESSAGE : { TEXT : "Потоки сообщений" },
                        FLOWSEQUENCE : { TEXT : "Потоки управления" },
                        GATEWAYCOMPLEX : { TEXT : "Комплексные развилки" },
                        GATEWAYEVENTBASED : { TEXT : "Развилки по событиям" },
                        GATEWAYEXCLUSIVE : { TEXT : "Развилки «или/или»" },
                        GATEWAYEXCLUSIVEEVENTBASED : { TEXT : "Развилки «или/или» по событию" },
                        GATEWAYINCLUSIVE : { TEXT : "Развилки «и/или»" },
                        GATEWAYPARALLEL : { TEXT : "Развилки «и»" },
                        GATEWAYPARALLELEVENTBASED : { TEXT : "Параллельные развилки по событию" },
                        INSCRIPTIONNONE : { TEXT : "Надпись" },
                        INTERMEDIATEEVENTCATCHINGCANCEL : { TEXT : "Промежуточные события-отмены (обработчики)" },
                        INTERMEDIATEEVENTCATCHINGERROR : { TEXT : "Промежуточные события-ошибки (обработчики)" },
                        INTERMEDIATEEVENTCATCHINGLINK : { TEXT : "Промежуточные события-ссылки (обработчики)" },
                        INTERMEDIATEEVENTCATCHINGMESSAGE : { TEXT : "Промежуточные события-сообщения (обработчики)" },
                        INTERMEDIATEEVENTCATCHINGMULTIPLE : { TEXT : "Множественные промежуточные события (обработчики)" },
                        INTERMEDIATEEVENTCATCHINGSIGNAL : { TEXT : "Промежуточные события-сигналы (обработчики)" },
                        INTERMEDIATEEVENTCOMPENSATION : { TEXT : "Промежуточные события-компенсации" },
                        INTERMEDIATEEVENTCONDITIONAL : { TEXT : "Промежуточные события-условия" },
                        INTERMEDIATEEVENTESCALATION : { TEXT : "Промежуточные события-эскалации" },
                        INTERMEDIATEEVENTNONE : { TEXT : "Промежуточные события" },
                        INTERMEDIATEEVENTPARALLELMULTIPLE : { TEXT : "Параллельные множественные промежуточные события" },
                        INTERMEDIATEEVENTTHROWINGLINK : { TEXT : "Промежуточные события-ссылки (инициаторы)" },
                        INTERMEDIATEEVENTTHROWINGMESSAGE : { TEXT : "Промежуточные события-сообщения (инициаторы)" },
                        INTERMEDIATEEVENTTHROWINGMULTIPLE : { TEXT : "Множественные промежуточные события (инициаторы)" },
                        INTERMEDIATEEVENTTHROWINGSIGNAL : { TEXT : "Промежуточные события-сигналы (инициаторы)" },
                        INTERMEDIATEEVENTTIMER : { TEXT : "Промежуточные события-таймеры" },
                        LANENONE : {
                            TEXT : "Дорожка",
                            CHILDREN : {
                                ROLETEMPLATES : { TEXT : "Шаблоны ролей" }
                            }
                        },
                        ORGUNITDEPARTMENT : { TEXT : "Оргединица-подразделение" },
                        ORGUNITPOSITION : { TEXT : "Оргединица-должность" },
                        POOLBLACKBOX : { TEXT : "Скрытый пул" },
                        POOLNONE : { TEXT : "Пул" },
                        POOLWHITEBOX : { TEXT : "Основной пул" },
                        PROCESSGROUPNONE : { TEXT : "Группы процессов" },
                        PROCESSGROUPREFNONE : { TEXT : "Ссылки на группы процессов" },
                        PROCESSMODELNONE : { TEXT : "Процессы" },
                        PROCESSMODELREFNONE : { TEXT : "Ссылки на процессы" },
                        RESOURCENONE : { TEXT : "Ресурсы" },
                        STARTEVENTCATCHINGMESSAGE : { TEXT : "Начальные события-сообщения (обработчики)" },
                        STARTEVENTCATCHINGMULTIPLE : { TEXT : "Множественные начальные-события (обработчики)" },
                        STARTEVENTCATCHINGSIGNAL : { TEXT : "Начальные события-сигналы (обработчики)" },
                        STARTEVENTCONDITIONAL : { TEXT : "Начальные события-условия" },
                        STARTEVENTNONE : { TEXT : "Начальные события" },
                        STARTEVENTPARALLELMULTIPLE : { TEXT : "Параллельные множественные начальные события" },
                        STARTEVENTTIMER : { TEXT : "Начальные события-таймеры" },
                        SUBPROCESSEMBEDDED : { TEXT : "Встроенные подпроцессы" },
                        SUBPROCESSREUSABLE : { TEXT : "Повторно используемые подпроцессы" },
                        TASKABSTRACT : { TEXT : "Абстрактные задачи" },
                        TASKBUSINESSRULE : { TEXT : "Задачи-выполнения бизнес-правила" },
                        TASKMANUAL : { TEXT : "Задачи, выполняемые вручную" },
                        TASKRECEIVE : { TEXT : "Задачи-получения сообщения" },
                        TASKSCRIPT : { TEXT : "Задачи-выполнения сценария" },
                        TASKSEND : { TEXT : "Задачи-отправки сообщения" },
                        TASKSERVICE : { TEXT : "Задачи-вызовы сервиса" },
                        TASKUSER : { TEXT : "Задачи, выполняемые пользователем" }
                    }
                }
            }
        },
        EMPTYARCHITECTURE : { TEXT : "Элементов архитектуры не найдено" },
        ERRORS : {
            TEXT : "errors",
            CHILDREN : {
                CANNOTEXPAND : { TEXT : "Невозможно развернуть подпроцесс, содержащий пул" },
                ELEMENTCYCLE : { TEXT : "Нельзя создать элемент который связан сам с собой или родительским элементом" }
            }
        },
        EXPENDABLE : { TEXT : "Обратное воздействие" },
        IMPORTVALIDATION : {
            TEXT : "",
            CHILDREN : {
                ELEMENTWILLBEREPLACEDWITHCOLLAPSEDSUBPROCESS : { TEXT : "Элемент «{1}: {0}» будет заменен на встроенный подпроцесс «{2}».\t" },
                FLOWISNOTCONNECTEDTODIAGRAMELEMENTS : { TEXT : "Поток «{0}» не соединен с элементами диаграммы. Этот поток не будет импортирован." },
                MORETHANONEWHITEBOX : { TEXT : "Раскрытый пул «{0}» будет преобразован в архитектуре в отдельный процесс «{1}»." }
            }
        },
        LINKEDOBJECT : {
            TEXT : "linkedObject",
            CHILDREN : {
                ALL : { TEXT : "Все" },
                INSTANCE : { TEXT : "Связанный объект" },
                LIST : {
                    TEXT : "Список из связанного шаблона записи",
                    CHILDREN : {
                        ALLLISTS : { TEXT : "Все списки" }
                    }
                },
                MENU : { TEXT : "Связанный объект" },
                RECORDTYPE : { TEXT : "Связанный шаблон записи" },
                TYPE : {
                    TEXT : "Тип связанного объекта",
                    CHILDREN : {
                        ABSTRACT : { TEXT : "Абстрактный" },
                        CASE : { TEXT : "Кейс" },
                        PROCESS : { TEXT : "Процесс" },
                        PROJECT : { TEXT : "Проект" },
                        UNSET : { TEXT : "Не задано" }
                    }
                }
            }
        },
        MAINPAGE : {
            TEXT : "fastCreation",
            CHILDREN : {
                GROUPTITLE : { TEXT : "Группа процессов" },
                IMPORTINFO : { TEXT : "Импорт диаграмм бизнес-процессов в формате .BPMN" },
                IMPORTTITLE : { TEXT : "Импорт процессов" },
                KNOWLEDGEBASE : { TEXT : "База знаний" },
                PROCESSGROUPINFO : { TEXT : "Создание семейства логически связанных процессов или подгрупп процессов" },
                PROCESSINFO : { TEXT : "Создание диаграммы бизнес-процесса в нотации BPMN" },
                PROCESSTITLE : { TEXT : "Процесс" },
                QUICKCREATE : { TEXT : "Быстрое создание" }
            }
        },
        OVERVIEW : {
            TEXT : "overview",
            CHILDREN : {
                ENTERPRISENAME : { TEXT : "Название" },
                ISFAVORITE : { TEXT : "Любимый" },
                SAVE : { TEXT : "Сохранить" }
            }
        },
        PROCESSESREGISTRYPAGE : {
            TEXT : "",
            CHILDREN : {
                CHANGEDON : { TEXT : "Дата изменения" },
                DIAGRAMM : { TEXT : "Диаграмма" },
                PROCESSES : { TEXT : "Процессы" }
            }
        },
        VALIDATION : {
            TEXT : "",
            CHILDREN : {
                CHANGEENDEVENTTYPETOEXECUTABLE : { TEXT : "Этот элемент не предназначен для автоматизированных моделей. Чтобы модель была автоматизированной, рекомендуется использовать вместо него один из следующих элементов: Конечное событие, Событие-сообщение, Событие-остановка" },
                CHANGEFLOWTYPETOEXECUTABLE : { TEXT : "Этот элемент не предназначен для автоматизированных моделей. Чтобы модель была автоматизированной, рекомендуется использовать вместо него «развилку или/или»" },
                CHANGEGATEWAYTYPETOEXECUTABLE : { TEXT : "Этот элемент не предназначен для автоматизированных моделей. Чтобы модель была автоматизированной, рекомендуется использовать вместо него один из следующих элементов: Развилка «или/или», Развилка «и»" },
                CHANGEINTERMEDIATEEVENTTYPETOEXECUTABLE : { TEXT : "Этот элемент не предназначен для автоматизированных моделей. Чтобы модель была автоматизированной, рекомендуется использовать вместо него один из следующих элементов: Простое событие, Событие-получение сообщения, Событие-отправка сообщения, Событие-таймер" },
                CHANGEMOUNTEDINTERMEDIATEEVENTTYPETOEXECUTABLE : { TEXT : "Этот элемент не предназначен для автоматизированных моделей. Чтобы модель была автоматизированной, рекомендуется использовать вместо него один из следующих элементов: Событие-получение сообщения, Событие-таймер" },
                CHANGESTARTEVENTTYPETOEXECUTABLE : { TEXT : "Этот элемент не предназначен для автоматизированных моделей. Чтобы модель была автоматизированной, рекомендуется использовать вместо него один из следующих элементов: Простое событие, Событие-получение сообщения, Событие-таймер" },
                CHANGETASKTYPETOEXECUTABLE : { TEXT : "Этот элемент не предназначен для автоматизированных моделей. Чтобы модель была автоматизированной, рекомендуется использовать вместо него один из следующих элементов: Пользовательская задача, Задача-выполнение сценария, Задача-вызов сервиса" },
                CREATEINCOMINGFLOW : { TEXT : "Рекомендуется создать хотя бы один входящий поток" },
                CREATEOUTPUTFLOW : { TEXT : "Рекомендуется создать хотя бы один исходящий поток" },
                ENDEVENTNOINPUT : { TEXT : "Необходим входящий поток" },
                ENDEVENTOUTPUT : { TEXT : "Конечное событие не должно иметь исходящих потоков" },
                ERRORS : { TEXT : "Ошибки" },
                FLOWNOTCONNECTED : { TEXT : "Поток не соединен ни с одним элементом" },
                GATENOINPUT : { TEXT : "Развилка должна иметь минимум один входящий поток управления" },
                GATENOOUTPUT : { TEXT : "Развилка должна иметь минимум один исходящий поток управления" },
                MESSAGEFLOWINSAMEPOOL : { TEXT : "Поток сообщений не может соединять элементы, расположенные внутри одного пула" },
                MISSINGSTARTANDENDEVENT : { TEXT : "В автоматизированных моделях рекомендуется использовать хотя бы одно конечное и одно начальное событие " },
                NODEFAULTFLOW : { TEXT : "В автоматизированных моделях рекомендуется указать один исходящий из развилки поток, как поток «иначе»" },
                NOENDEVENT : { TEXT : "Необходимо хотя бы одно конечное событие" },
                NOINPUTOROUTPUT : { TEXT : "Рекомендуется использовать хотя бы один входящий или исходящий поток данных" },
                NONEXECUTABLEMODIFIER : { TEXT : "Модификатор не предназначен для автоматизированных моделей" },
                NOSTARTEVENT : { TEXT : "Необходимо хотя бы одно начальное событие" },
                RECOMMENDEDSINGLEOUTPUTFLOW : { TEXT : "Рекомендуется определять для элемента один исходящий поток" },
                SEVERALSIMPLESTARTS : { TEXT : "На диаграмме не может быть более одного простого начального события" },
                STARTINPUT : { TEXT : "Начальное событие не должно иметь входящих потоков" },
                STARTNOOUTPUT : { TEXT : "Необходим исходящий поток" },
                UNCONNECTEDINONEPOOL : { TEXT : "Несвязанные друг с другом фрагменты диаграммы процесса не могут располагаться в одном пуле" },
                VERIFY : { TEXT : "Проверить" },
                WARNINGS : { TEXT : "Предупреждения" }
            }
        },
        VERSION : {
            TEXT : "",
            CHILDREN : {
                DESCRIPTION : { TEXT : "Описание" },
                ELEMENT : {
                    TEXT : "element",
                    CHILDREN : {
                        PROPERTY : {
                            TEXT : "",
                            CHILDREN : {
                                ASSIGNEE : {
                                    TEXT : "Исполнитель",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Исполнитель задачи" }
                                    }
                                },
                                DEFAULTPROPERTIESGROUP : { TEXT : "Атрибуты по умолчанию" },
                                DESCRIPTION : {
                                    TEXT : "Описание",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Описание элемента диаграммы" }
                                    }
                                },
                                LABORINPUT : {
                                    TEXT : "Трудоемкость ",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Трудоёмкость задачи" }
                                    }
                                },
                                NAME : {
                                    TEXT : "Наименование",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Название элемента диаграммы" }
                                    }
                                },
                                ORDER : {
                                    TEXT : "Порядковый номер",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Порядковый номер элемента" }
                                    }
                                },
                                PARTICIPANT : {
                                    TEXT : "Участники процесса",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Участники процесса" }
                                    }
                                },
                                PROCESSOWNER : {
                                    TEXT : "Владелец процесса",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Владелец процесса" }
                                    }
                                },
                                REGULATIONPDF : {
                                    TEXT : "Регламент в PDF",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Регламент в формате PDF" }
                                    }
                                },
                                REGULATIONWORD : {
                                    TEXT : "Регламент в Word",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Регламент в формате DOCX" }
                                    }
                                },
                                STANDARTTIMELIMIT : {
                                    TEXT : "Нормативный срок",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Нормативный срок выполнения задачи" }
                                    }
                                },
                                TASK : {
                                    TEXT : "Задачи процесса",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Задачи в процессе" }
                                    }
                                }
                            }
                        }
                    }
                },
                ELEMENTGROUPTITLE : { TEXT : "Элементы диаграммы" },
                EXPORTTEMPLATE : {
                    TEXT : "exportTemplate",
                    CHILDREN : {
                        FAIL : { TEXT : "Не удалось сохранить шаблон экспорта регламента." },
                        SUCCESS : { TEXT : "Шаблон экспорта регламента сохранён." }
                    }
                },
                FAILRESTORE : { TEXT : "Не удалось восстановить версию" },
                FAILSAVE : { TEXT : "Не удалось сохранить версию" },
                KEEPVURRENTVERSION : { TEXT : "Сохранить текущую версию" },
                MULTIPLETEMPLATE : { TEXT : "Для этой версии уже создан шаблон экспорта" },
                PROCESSDESCRIPTION : { TEXT : "Описание процесса" },
                REPLACECURRENTVERSION : { TEXT : "Заменить текущую версию" },
                RESTOREDESCRIPTION : { TEXT : "1. Заменить текущую версию версией {0}. Несохранённые изменения в текущей версии будут безвозвратно утрачены.<br>2. Сохранить текущую версию как версию {1}. Версия {0} станет текущей." },
                RESTOREVERSIONTITLE : { TEXT : "Восстановить версию" },
                RESTOREWAY : { TEXT : "Выберите способ восстановления" },
                SAVEDON : { TEXT : "Дата сохранения" },
                SAVEVERSIONBUTTON : { TEXT : "Сохранить версию" },
                SAVEVERSIONTITLE : { TEXT : "Сохранение версии" },
                SUCCESSRESTORE : { TEXT : "Версия восстановлена" },
                SUCCESSSAVE : { TEXT : "Версия сохранена" },
                VERSIONCONTROL : { TEXT : "Управление версиями" },
                VERSIONPROPERTIES : { TEXT : "Свойства версии" },
                VERSIONS : { TEXT : "Версии" },
                WARNING : { TEXT : "Текущая версия будет заменена версией {0}. Несохранённые изменения в текущей версии будут безвозвратно утрачены." }
            }
        }
    }
},          
VALIDATION : {
    TEXT : "validation",
    CHILDREN : {
        CLOSE : { TEXT : "Закрыть" },
        ERRORS : {
            TEXT : "",
            CHILDREN : {
                ACTIVEINSTANCES : { TEXT : "Существуют активные экземпляры процесса, запущенные на данной версии диаграммы" },
                ACTIVITYCONNECTORSINVALID : { TEXT : "Заново подсоедините потоки управления к элементу." },
                ACTIVITYDATAINVALID : { TEXT : "Недопустимые данные элемента." },
                ACTIVITYEMBEDDEDINTOWRONGACTIVITY : { TEXT : "Элемент вложен в неподходящий элемент." },
                ACTIVITYISOLATED : { TEXT : "У этого элемента нет потоков управления или к нему невозможно перейти из начального с события." },
                ACTIVITYTYPEINVALID : { TEXT : "Недопустимый тип элемента." },
                ACTIVITYWITHDUPLICATEALIAS : { TEXT : "Элемент с таким системным именем уже существует." },
                ACTIVITYWITHDUPLICATEID : { TEXT : "Имеются элементы с совпадающим ID." },
                ATTACHEDEVENTATTACHEDTOINVALIDACTIVITY : { TEXT : "К этому элементу нельзя прикрепить событие." },
                ATTACHEDEVENTMARKERINVALID : { TEXT : "Неверная метка прикрепленного события." },
                ATTACHEDEVENTTHROWSMESSAGE : { TEXT : "Прикрепленное событие не может отправить сообщение." },
                ATTACHEDEVENTTHROWSSIGNAL : { TEXT : "Прикрепленное событие не может отправить сигнал." },
                ATTACHEDEVENTUNATTACHED : { TEXT : "Прикрепленное событие не прикреплено к элементу." },
                ATTACHEDEVENTWITHINBOUNDFLOW : { TEXT : "У прикрепленного события не должно быть входящих потоков управления." },
                ATTACHEDEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "У прикрепленного события должен быть только один исходящий поток управления." },
                CASETASKMARKERASSIGNEEISNOTSET : { TEXT : "Не указан исполнитель кейса." },
                CASETASKMARKERINVALIDDATA : { TEXT : "Недопустимый заголовок кейса." },
                CASETASKMARKERINVALIDINPUTMAPPINGS : { TEXT : "Недопустимые входные параметры кейса." },
                CASETASKMARKERINVALIDRETURNMAPPINGS : { TEXT : "Недопустимые выходные параметры кейса." },
                CASETASKMARKERINVALIDTEMPLATE : { TEXT : "Недопустимый шаблон кейса." },
                CASETASKWITHOUTINBOUNDFLOW : { TEXT : "У кейса должен быть хотя бы один входящий поток управления." },
                CASETASKWITHOUTOUTBOUNDFLOW : { TEXT : "У кейса должен быть только один исходящий поток управления." },
                CSHARPCODEEMPTY : { TEXT : "Пустой скрипт C# " },
                CSHARPCOMPILATIONERROR : { TEXT : "Ошибка при компиляции скрипта C#" },
                CSHARPREFERENCEINVALID : { TEXT : "Неверная ссылка для сборки в скрипте C#" },
                DIAGRAMEMPTY : { TEXT : "Диаграмма пуста" },
                DIAGRAMHASNOSTARTEVENT : { TEXT : "Диаграмма должна содержать хотя бы одно начальное событие" },
                DIAGRAMHASNULLACTIVITIES : { TEXT : "Диаграмма содержит неизвестные элементы." },
                DIAGRAMHASNULLIDACTIVITIES : { TEXT : "У некоторых элементов отсутствует ID." },
                DIAGRAMMDOESNOTEXIST : { TEXT : "Диаграмма не существует" },
                EMBEDDEDPROCESSCYCLE : { TEXT : "Во вложенном подпроцессе присутствует цикл" },
                EMBEDDEDPROCESSMUSTHAVESINGLESIMPLESTARTEVENT : { TEXT : "У встроенного подпроцесса должно быть только одно простое начальное событие." },
                EMBEDDEDPROCESSWITHOUTINBOUNDFLOW : { TEXT : "У вложенного подпроцесса должен быть хотя бы один входящий поток управления." },
                EMBEDDEDPROCESSWITHOUTOUTBOUNDFLOW : { TEXT : "У встроенного подпроцесса должен быть только один исходящий поток управления." },
                ENDEVENTATTACHED : { TEXT : "Конечное событие нельзя прикрепить к элементу." },
                ENDEVENTCATCHESMESSAGE : { TEXT : "Начальное событие не может получить сообщение." },
                ENDEVENTCATCHESSIGNAL : { TEXT : "Начальное событие не может получить сигнал." },
                ENDEVENTMARKERINVALID : { TEXT : "Неверная метка конечного события." },
                ENDEVENTWITHOUTBOUNDFLOW : { TEXT : "У конечного события не должно быть исходящих потоков управления." },
                ENDEVENTWITHOUTINBOUNDFLOW : { TEXT : "У конечного события должен быть хотя бы один входящий поток управления." },
                EVENTMARKERINVALID : { TEXT : "Event marker invalid" },
                EVENTMARKERMESSAGEINVALIDDATA : { TEXT : "Недопустимые свойства события-сообщения" },
                EVENTMARKERMESSAGEINVALIDNAME : { TEXT : "Неверное имя сообщения." },
                EVENTMARKERMESSAGETOUNKNOWNPROCESS : { TEXT : "Неизвестный процесс на маршруте 1." },
                EVENTMARKERMESSAGETOUNKNOWNPROCESSAPP : { TEXT : "Неизвестный процесс на маршруте." },
                EVENTMARKERMESSAGEWITHINVALIDROUTE : { TEXT : "Неверный маршрут для сообщения" },
                EVENTMARKERSIGNALINVALIDDATA : { TEXT : "Недопустимые данные события-сигнала" },
                EVENTMARKERSIGNALINVALIDNAME : { TEXT : "Неверное имя сигнала." },
                EVENTMARKERTIMERINVALIDDATA : { TEXT : "В событии-таймере не настроен таймер." },
                EXCLUSIVEGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "У развилки «или/или» должен быть хотя бы один входящий поток управления." },
                EXCLUSIVEGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "У развилки «или/или» должен быть хотя бы один исходящий поток управления." },
                EXPRESSIONINVALID : { TEXT : "Недопустимое выражение" },
                FLOWCONNECTORSINVALID : { TEXT : "Заново подсоедините поток управления к элементам процесса." },
                FLOWDEFINITIONINVALID : { TEXT : "Недопустимое определение потока управления." },
                FLOWINVALID : { TEXT : "Недопустимый поток управления." },
                FLOWSOURCEINVALID : { TEXT : "Поток управления не соединен с отправной точкой." },
                FLOWTARGETINVALID : { TEXT : "Поток управления не соединен с конечной точкой." },
                FOREACHLOOPMISSINGINPUTRULE : { TEXT : "Набор входных параметров не задан ни для одного цикла" },
                FORLOOPMISSINGCARDINALITYRULE : { TEXT : "В настройках цикла не задано кардинальное число" },
                GATEWAYMARKEREVENTBASEDOUTBOUNDTWOORMOREFLOWREQUIRED : { TEXT : "У развилки по событиям должно быть минимум два исходящих потока управления." },
                GATEWAYMARKEREVENTBASEDTARGETINTERMEDIATECATCHEVENT : { TEXT : "Target activity for event-based gateway must have a type derived from intermediate catch event" },
                GATEWAYMARKEREVENTBASEDTARGETSINGLEINCOMINGSEQUENCEFLOW : { TEXT : "У конечных точек развилки по событиям не должно быть дополнительных входящих потоков управления." },
                GATEWAYMARKEREXLUSIVENOCONDITIONFOROUTBOUNDFLOW : { TEXT : "У развилки «или/или» для всех исходящих потоков управления кроме потока «иначе» должны быть заданы условия." },
                GATEWAYMARKEREXLUSIVENODEFAULTOUTBOUNDFLOW : { TEXT : "У развилки «или/или» должен быть только один исходящий поток управления «иначе»." },
                GATEWAYMARKERINCLUSIVENOCONDITIONFOROUTBOUNDFLOW : { TEXT : "У развилки «и/или» условия должны быть заданы для всех условных исходящих потоков управления." },
                GATEWAYMARKERINCLUSIVENODEFAULTOUTBOUNDFLOW : { TEXT : "У развилки «и/или» должен быть только один исходящий поток управления «иначе»." },
                GATEWAYMARKERINVALID : { TEXT : "Недопустимая метка развилки" },
                GATEWAYMARKERPARALLELWITHNONEMPTYDEFINITION : { TEXT : "У развилки «и» не должно быть исходящего потока управления «иначе» и условий для потоков управления." },
                GLOBALFUNCTIONTASKMARKERINVALIDDATA : { TEXT : "Недопустимые свойства функции в задаче" },
                INBOUNDFLOWREQUIRED : { TEXT : "Необходим хотя бы один входящий поток управления." },
                INCLUSIVEGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "У развилки «и/или» должен быть хотя бы один входящий поток управления." },
                INCLUSIVEGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "У развилки «и/или» должен быть хотя бы один исходящий поток управления." },
                INTERMEDIATEEVENTATTACHED : { TEXT : "Промежуточное событие нельзя прикрепить к элементу." },
                INTERMEDIATEEVENTMARKERINVALID : { TEXT : "Неверная метка промежуточного события" },
                INTERMEDIATEEVENTWITHOUTINBOUNDFLOW : { TEXT : "У промежуточного события должен быть хотя бы один входящий поток управления." },
                INTERMEDIATEEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "У промежуточного события должен быть только один исходящий поток управления." },
                INVALIDDEFINITION : { TEXT : "Invalid activity data" },
                INVALIDSTARTFORMACTIVITYDEFINITION : { TEXT : "Cтартовая форма может быть только у простого начального события." },
                LOOPINVALID : { TEXT : "Неверные настройки цикла" },
                MESSAGEESSENCEINVALID : { TEXT : "Invalid message definition" },
                MESSAGEMAPPINGINVALIDMESSAGETYPE : { TEXT : "Неверный шаблон сообщения при сопоставлении" },
                MESSAGEMAPPINGINVALIDPROPERTY : { TEXT : "Неверное свойство при сопоставлении" },
                MESSAGEMAPPINGINVALIDRULE : { TEXT : "Неверное правило при сопоставлении" },
                MESSAGERECEIVERINVALID : { TEXT : "Неверный получатель сообщения" },
                NODEFAULTOUTBOUNDFLOW : { TEXT : "Необходимо указать исходящий поток управления «иначе»." },
                NOINBOUNDFLOWREQUIRED : { TEXT : "У этого элемента не должно быть входящих потоков управления." },
                NOOUTBOUNDFLOWREQUIRED : { TEXT : "У этого элемента не должно быть исходящих потоков управления." },
                OUTBOUNDFLOWREQUIRED : { TEXT : "Необходим хотя бы один исходящий поток управления." },
                PARALLELGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "У развилки «и» должен быть как хотя бы один входящий поток управления." },
                PARALLELGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "У развилки «и» должен быть как хотя бы один исходящий поток управления." },
                RULEERROR : { TEXT : "Ошибка в правиле" },
                RULEINVALIDDATA : { TEXT : "Недопустимые данные для правила" },
                RULEINVALIDDEFINITION : { TEXT : "Недопустимое определение правила" },
                RULEINVALIDTYPE : { TEXT : "Недопустимый тип правила" },
                RULEISREQUIRED : { TEXT : "Missing mandatory business rule" },
                SCRIPTTASKMARKERINVALIDDATA : { TEXT : "Не задан сценарий для задачи-выполнения сценария." },
                SCRIPTTASKWITHOUTINBOUNDFLOW : { TEXT : "У задачи-выполнения сценария должен быть хотя бы один входящий поток управления." },
                SCRIPTTASKWITHOUTOUTBOUNDFLOW : { TEXT : "У задачи-выполнения сценария должен быть только один исходящий поток управления." },
                SERVICETASKMARKERINVALIDDATA : { TEXT : "Недопустимые свойства задачи-вызова сервиса" },
                SERVICETASKWITHOUTINBOUNDFLOW : { TEXT : "У задачи-вызова сервиса должен быть хотя бы один входящий поток управления." },
                SERVICETASKWITHOUTOUTBOUNDFLOW : { TEXT : "У задачи-вызова сервиса должен быть только один исходящий поток управления." },
                SINGLEOUTBOUNDFLOWREQUIRED : { TEXT : "У этого элемента должен быть один исходящий поток управления." },
                STARTEVENTATTACHED : { TEXT : "Начальное событие нельзя прикрепить к элементу." },
                STARTEVENTMARKERINVALID : { TEXT : "Неверная метка начального события" },
                STARTEVENTMESSAGEDUPLICATED : { TEXT : "Диаграмма содержит несколько начальных событий с одинаковыми параметрами сообщения" },
                STARTEVENTNONEDUPLICATED : { TEXT : "На диаграмме не может быть более одного простого (нетипизированного) начального события" },
                STARTEVENTSCHEDULEMUSTEMPTY : { TEXT : "startEventScheduleMustEmpty" },
                STARTEVENTSIGNALDUPLICATED : { TEXT : "Диаграмма содержит несколько начальных событий с одинаковыми параметрами сигнала" },
                STARTEVENTTHROWSMESSAGE : { TEXT : "Начальное событие не может отправить сообщение" },
                STARTEVENTTHROWSSIGNAL : { TEXT : "Начальное событие не может отправить сигнал" },
                STARTEVENTTIMERSCHEDULEREQUIRED : { TEXT : "В начальном событии не настроен таймер" },
                STARTEVENTWITHINBOUNDFLOW : { TEXT : "Начальное событие не должно иметь входящих потоков управления." },
                STARTEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "У начального события должен быть только один исходящий поток управления." },
                SUBPROCESSINVALIDDEFINITION : { TEXT : "Недопустимые свойства внешнего подпроцесса." },
                SUBPROCESSUNEXISTINGPROCESSAPP : { TEXT : "В качестве внешнего подпроцесса задан недействительный процесс" },
                SUBPROCESSUNEXISTINGPROCESSAPPSCHEME : { TEXT : "Диаграмма процесса, используемая во внешнем подпроцессе, неверна или не существует" },
                SUBPROCESSWITHOUTINBOUNDFLOW : { TEXT : "У внешнего подпроцесса должен быть хотя бы один входящий поток управления." },
                SUBPROCESSWITHOUTOUTBOUNDFLOW : { TEXT : "У внешнего подпроцесса должен быть только один исходящий поток управления." },
                TASKMARKERINVALID : { TEXT : "Пользовательская задача должна иметь минимум одного ответственного." },
                TWODEFAULTOUTBOUNDFLOWS : { TEXT : "Допустим только один исходящий поток управления «иначе»." },
                TYPESCOMPILATIONERROR : { TEXT : "Ошибка при компиляции типов пользовательских объектов" },
                UNKNOWNERROR : { TEXT : "Внутренняя ошибка." },
                UNKNOWNEXCEPTION : { TEXT : "Unknown exception when processing activity: {0}" },
                USERTASKMARKERASSIGNEEISNOTSET : { TEXT : "Для пользовательской задачи не выбран ответственный" },
                USERTASKMARKERINVALIDDATA : { TEXT : "Пользовательская задача должна иметь минимум одного ответственного." },
                USERTASKWITHOUTINBOUNDFLOW : { TEXT : "У пользовательской задачи должен быть хотя бы один входящий поток управления." },
                USERTASKWITHOUTOUTBOUNDFLOW : { TEXT : "У пользовательской задачи должен быть только один исходящий поток управления." },
                WHILELOOPMISSINGCONDITIONRULE : { TEXT : "В настройках цикла «Пока» не задано условие" }
            }
        },
        FAILED : { TEXT : "Ошибка при проверке." }
    }
}