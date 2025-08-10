ARCHITECTURE : {
    TEXT : "Architecture",
    CHILDREN : {
        COLUMNS : {
            TEXT : "",
            CHILDREN : {
                CREATEDBY : { TEXT : "Erstellt von" },
                CREATEDON : { TEXT : "Erstellt am" },
                DIAGRAMNAME : { TEXT : "Diagrammname" },
                DIAGRAMTYPE : { TEXT : "Diagrammtyp" },
                NAME : { TEXT : "Name" }
            }
        },
        DEFAULTNAME : { TEXT : "Neues Architekturdiagramm" },
        DIGRAMTYPE : {
            TEXT : "",
            CHILDREN : {
                ARCHITECTURE : { TEXT : "Architektur" },
                DATADIAGRAM : { TEXT : "Data diagram" }
            }
        },
        DOCUMENTATION : {
            TEXT : "documentation",
            CHILDREN : {
                PROPERTIES : {
                    TEXT : "",
                    CHILDREN : {
                        PARENTPROCESS : { TEXT : "Parent process" },
                        PARENTPROCESSGROUP : { TEXT : "Parent process group" },
                        PARENTSUBPROCESS : { TEXT : "Parent subprocess" }
                    }
                },
                TEMPLATENAME : { TEXT : "Properties panel configuration: {0}" },
                TYPES : {
                    TEXT : "",
                    CHILDREN : {
                        ANNOTATIONNONE : { TEXT : "Annotations" },
                        BPMNGROUP : { TEXT : "BPMN group" },
                        DATAOBJECT : { TEXT : "Data objects" },
                        DATASTORE : { TEXT : "Data stores" },
                        ENDEVENTCANCEL : { TEXT : "Cancel end events" },
                        ENDEVENTCOMPENSATION : { TEXT : "Compensation end events" },
                        ENDEVENTERROR : { TEXT : "End events errors" },
                        ENDEVENTESCALATION : { TEXT : "Escalation end events" },
                        ENDEVENTNONE : { TEXT : "End events" },
                        ENDEVENTTERMINATE : { TEXT : "Terminate end events" },
                        ENDEVENTTHROWINGMESSAGE : { TEXT : "Message end events (throw)" },
                        ENDEVENTTHROWINGMULTIPLE : { TEXT : "Multiple end events (throw)" },
                        ENDEVENTTHROWINGSIGNAL : { TEXT : "Signal end events (throw)" },
                        FLOWASSOCIATION : { TEXT : "Association flows" },
                        FLOWCONDITIONAL : { TEXT : "Conditional flows" },
                        FLOWDATA : { TEXT : "Data flows" },
                        FLOWDEFAULT : { TEXT : "Default flows" },
                        FLOWMESSAGE : { TEXT : "Message flows" },
                        FLOWSEQUENCE : { TEXT : "Sequence flows" },
                        GATEWAYCOMPLEX : { TEXT : "Complex gateways" },
                        GATEWAYEVENTBASED : { TEXT : "Event gateways" },
                        GATEWAYEXCLUSIVE : { TEXT : "Exclusive gateways" },
                        GATEWAYEXCLUSIVEEVENTBASED : { TEXT : "Exclusive event gateways" },
                        GATEWAYINCLUSIVE : { TEXT : "Inclusive gateways" },
                        GATEWAYPARALLEL : { TEXT : "Parallel gateways" },
                        GATEWAYPARALLELEVENTBASED : { TEXT : "Parallel event gateways" },
                        INSCRIPTIONNONE : { TEXT : "Inscription" },
                        INTERMEDIATEEVENTCATCHINGCANCEL : { TEXT : "Cancel intermediate events (catch)" },
                        INTERMEDIATEEVENTCATCHINGERROR : { TEXT : "Error intermediate events (catch)" },
                        INTERMEDIATEEVENTCATCHINGLINK : { TEXT : "Link intermediate events (catch)" },
                        INTERMEDIATEEVENTCATCHINGMESSAGE : { TEXT : "Message intermediate events (catch)" },
                        INTERMEDIATEEVENTCATCHINGMULTIPLE : { TEXT : "Multiple intermediate events (catch)" },
                        INTERMEDIATEEVENTCATCHINGSIGNAL : { TEXT : "Signal intermediate events (catch)" },
                        INTERMEDIATEEVENTCOMPENSATION : { TEXT : "Compensation intermediate events" },
                        INTERMEDIATEEVENTCONDITIONAL : { TEXT : "Conditional intermediate events" },
                        INTERMEDIATEEVENTESCALATION : { TEXT : "Escalation intermediate events" },
                        INTERMEDIATEEVENTNONE : { TEXT : "Intermediate events" },
                        INTERMEDIATEEVENTPARALLELMULTIPLE : { TEXT : "Parallel multiple intermediate events" },
                        INTERMEDIATEEVENTTHROWINGLINK : { TEXT : "Link intermediate events (throw)" },
                        INTERMEDIATEEVENTTHROWINGMESSAGE : { TEXT : "Message intermediate events (throw)" },
                        INTERMEDIATEEVENTTHROWINGMULTIPLE : { TEXT : "Multiple intermediate events (throw)" },
                        INTERMEDIATEEVENTTHROWINGSIGNAL : { TEXT : "Signal intermediate events (throw)" },
                        INTERMEDIATEEVENTTIMER : { TEXT : "Intermediate timer events" },
                        LANENONE : {
                            TEXT : "Lane",
                            CHILDREN : {
                                ROLETEMPLATES : { TEXT : "Rollenvorlagen" }
                            }
                        },
                        ORGUNITDEPARTMENT : { TEXT : "Department organizational unit" },
                        ORGUNITPOSITION : { TEXT : "Job title organizational unit" },
                        POOLBLACKBOX : { TEXT : "Black-box pool" },
                        POOLNONE : { TEXT : "Pool" },
                        POOLWHITEBOX : { TEXT : "White-box pool" },
                        PROCESSGROUPNONE : { TEXT : "Process groups" },
                        PROCESSGROUPREFNONE : { TEXT : "Process group links" },
                        PROCESSMODELNONE : { TEXT : "Processes" },
                        PROCESSMODELREFNONE : { TEXT : "Process links" },
                        RESOURCENONE : { TEXT : "Resources" },
                        STARTEVENTCATCHINGMESSAGE : { TEXT : "Message start events (catch)" },
                        STARTEVENTCATCHINGMULTIPLE : { TEXT : "Multiple start events (catch)" },
                        STARTEVENTCATCHINGSIGNAL : { TEXT : "Signal start events (catch)" },
                        STARTEVENTCONDITIONAL : { TEXT : "Conditional start events" },
                        STARTEVENTNONE : { TEXT : "Start events" },
                        STARTEVENTPARALLELMULTIPLE : { TEXT : "Parallel multiple start events" },
                        STARTEVENTTIMER : { TEXT : "Timer start events" },
                        SUBPROCESSEMBEDDED : { TEXT : "Embedded subprocesses" },
                        SUBPROCESSREUSABLE : { TEXT : "Reusable subprocesses" },
                        TASKABSTRACT : { TEXT : "Abstract tasks" },
                        TASKBUSINESSRULE : { TEXT : "Business rule tasks" },
                        TASKMANUAL : { TEXT : "Manual tasks" },
                        TASKRECEIVE : { TEXT : "Receive tasks" },
                        TASKSCRIPT : { TEXT : "Script tasks" },
                        TASKSEND : { TEXT : "Send tasks" },
                        TASKSERVICE : { TEXT : "Service tasks" },
                        TASKUSER : { TEXT : "User tasks" }
                    }
                }
            }
        },
        EMPTYARCHITECTURE : { TEXT : "Es sind keine anzuzeigenden Architekturelemente vorhanden" },
        ERRORS : {
            TEXT : "errors",
            CHILDREN : {
                CANNOTEXPAND : { TEXT : "Der Unterprozess, der den Pool enthält, kann nicht expandieren werden" },
                ELEMENTCYCLE : { TEXT : "Es kann kein Element erstellt werden, das sich selbst oder das übergeordnete Element verknüpft" }
            }
        },
        EXPENDABLE : { TEXT : "Umgekehrter Effekt" },
        IMPORTVALIDATION : {
            TEXT : "",
            CHILDREN : {
                ELEMENTWILLBEREPLACEDWITHCOLLAPSEDSUBPROCESS : { TEXT : "The “{0}” {1} will be replaced with “{2}” Embedded subprocess." },
                FLOWISNOTCONNECTEDTODIAGRAMELEMENTS : { TEXT : "The “{0}” flow is not connected to diagram elements. This flow won't be imported." },
                MORETHANONEWHITEBOX : { TEXT : "“{0}” white-box pool will be converted in the architecture to the separate “{1}” process." }
            }
        },
        LINKEDOBJECT : {
            TEXT : "linkedObject",
            CHILDREN : {
                ALL : { TEXT : "Alle" },
                INSTANCE : { TEXT : "Verknüpftes Objekt" },
                LIST : {
                    TEXT : "Liste Verknüpfter Datensatztypen",
                    CHILDREN : {
                        ALLLISTS : { TEXT : "Alle Listen" }
                    }
                },
                MENU : { TEXT : "Verknüpftes Objekt" },
                RECORDTYPE : { TEXT : "Verknüpfter Datensatztyp" },
                TYPE : {
                    TEXT : "Verknüpfter Objekttyp",
                    CHILDREN : {
                        ABSTRACT : { TEXT : "Abstrakt" },
                        CASE : { TEXT : "Fall" },
                        PROCESS : { TEXT : "Prozess" },
                        PROJECT : { TEXT : "Projekt" },
                        UNSET : { TEXT : "Nicht spezifiziert" }
                    }
                }
            }
        },
        MAINPAGE : {
            TEXT : "fastCreation",
            CHILDREN : {
                GROUPTITLE : { TEXT : "Process group" },
                IMPORTINFO : { TEXT : "Import business process diagrams in .BPMN format" },
                IMPORTTITLE : { TEXT : "Process import" },
                KNOWLEDGEBASE : { TEXT : "Knowledgebase" },
                PROCESSGROUPINFO : { TEXT : "Create a family of logically related processes or process subgroups" },
                PROCESSINFO : { TEXT : "Create a business process diagram in BPMN notation" },
                PROCESSTITLE : { TEXT : "Process" },
                QUICKCREATE : { TEXT : "Quick create" }
            }
        },
        OVERVIEW : {
            TEXT : "Übersicht",
            CHILDREN : {
                ENTERPRISENAME : { TEXT : "Name des Unternehmens" },
                ISFAVORITE : { TEXT : "Favorit" },
                SAVE : { TEXT : "Speichern" }
            }
        },
        PROCESSESREGISTRYPAGE : {
            TEXT : "",
            CHILDREN : {
                CHANGEDON : { TEXT : "Changed on" },
                DIAGRAMM : { TEXT : "Diagramm" },
                PROCESSES : { TEXT : "Processes" }
            }
        },
        VALIDATION : {
            TEXT : "",
            CHILDREN : {
                CHANGEENDEVENTTYPETOEXECUTABLE : { TEXT : "This element is not applicable for executable models. To make the model executable, consider using either of the following: End event, Message event, Terminate event" },
                CHANGEFLOWTYPETOEXECUTABLE : { TEXT : "This element is not applicable for executable models. To make the model executable, consider using an exclusive gateway instead" },
                CHANGEGATEWAYTYPETOEXECUTABLE : { TEXT : "This element is not applicable for executable models. To make the model executable, consider replacing this element with either of the following: Exclusive gateway, Parallel gateway" },
                CHANGEINTERMEDIATEEVENTTYPETOEXECUTABLE : { TEXT : "This element is not applicable for executable models. To make the model executable, consider replacing this element with either of the following: None event, Receive message event, Send message event, Timer event" },
                CHANGEMOUNTEDINTERMEDIATEEVENTTYPETOEXECUTABLE : { TEXT : "This element is not applicable for executable models. To make the model executable, consider replacing this element with either of the following: Receive message event, Timer event" },
                CHANGESTARTEVENTTYPETOEXECUTABLE : { TEXT : "This element is not applicable for executable models. To make the model executable, consider using either of the following: None event, Receive message event, Timer event" },
                CHANGETASKTYPETOEXECUTABLE : { TEXT : "This element is not applicable for executable models. To make the model executable, consider replacing this element with either of the following: User task, Script task, Service task" },
                CREATEINCOMINGFLOW : { TEXT : "Consider creating at least one incoming flow" },
                CREATEOUTPUTFLOW : { TEXT : "Consider creating at least one outgoing flow" },
                ENDEVENTNOINPUT : { TEXT : "Incoming flow is required" },
                ENDEVENTOUTPUT : { TEXT : "End event must not have any outgoing flows" },
                ERRORS : { TEXT : "Errors" },
                FLOWNOTCONNECTED : { TEXT : "The flow is not connected to any element" },
                GATENOINPUT : { TEXT : "The gate must have at least one incoming sequence flow" },
                GATENOOUTPUT : { TEXT : "The gate must have at least one outgoing sequence flow" },
                MESSAGEFLOWINSAMEPOOL : { TEXT : "A message flow cannot connect elements located within the same pool" },
                MISSINGSTARTANDENDEVENT : { TEXT : "Executable models should have at least one start event and one end event" },
                NODEFAULTFLOW : { TEXT : "In executable model, the gateway should have a default flow" },
                NOENDEVENT : { TEXT : "At least one end event is required" },
                NOINPUTOROUTPUT : { TEXT : "Consider defining at least one incoming or outgoing data flow" },
                NONEXECUTABLEMODIFIER : { TEXT : "This modifier is not applicable for executable models" },
                NOSTARTEVENT : { TEXT : "At least one start event is required" },
                RECOMMENDEDSINGLEOUTPUTFLOW : { TEXT : "The element should have only one outgoing flow" },
                SEVERALSIMPLESTARTS : { TEXT : "Only one none start event is allowed in the diagram" },
                STARTINPUT : { TEXT : "Start event must not have any incoming flows" },
                STARTNOOUTPUT : { TEXT : "Outgoing flow is required" },
                UNCONNECTEDINONEPOOL : { TEXT : "Unconnected process diagram fragments cannot be placed in one pool" },
                VERIFY : { TEXT : "Verify" },
                WARNINGS : { TEXT : "Warnings" }
            }
        },
        VERSION : {
            TEXT : "",
            CHILDREN : {
                DESCRIPTION : { TEXT : "Description" },
                ELEMENT : {
                    TEXT : "element",
                    CHILDREN : {
                        PROPERTY : {
                            TEXT : "",
                            CHILDREN : {
                                ASSIGNEE : {
                                    TEXT : "Assignee",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Task assignee" }
                                    }
                                },
                                DEFAULTPROPERTIESGROUP : { TEXT : "Default properties" },
                                DESCRIPTION : {
                                    TEXT : "Description",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Diagram element description" }
                                    }
                                },
                                LABORINPUT : {
                                    TEXT : "Labor input",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Labor input for the task" }
                                    }
                                },
                                NAME : {
                                    TEXT : "Name",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Diagram element name" }
                                    }
                                },
                                ORDER : {
                                    TEXT : "Sequenznummer",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Element-Sequenznummer" }
                                    }
                                },
                                PARTICIPANT : {
                                    TEXT : "Process participants",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Process participants" }
                                    }
                                },
                                PROCESSOWNER : {
                                    TEXT : "Process owner",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Process owner" }
                                    }
                                },
                                REGULATIONPDF : {
                                    TEXT : "Regulation in PDF",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Regulation in PDF format" }
                                    }
                                },
                                REGULATIONWORD : {
                                    TEXT : "Regulation in Word",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Regulation in DOCX format" }
                                    }
                                },
                                STANDARTTIMELIMIT : {
                                    TEXT : "Standart time limit",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Standart time limit for the task" }
                                    }
                                },
                                TASK : {
                                    TEXT : "Process tasks",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Process tasks" }
                                    }
                                }
                            }
                        }
                    }
                },
                ELEMENTGROUPTITLE : { TEXT : "Diagram elements" },
                EXPORTTEMPLATE : {
                    TEXT : "exportTemplate",
                    CHILDREN : {
                        FAIL : { TEXT : "Die Exportvorlage für Verordnung konnte nicht gespeichert werden." },
                        SUCCESS : { TEXT : "Die Exportvorlage für die Verordnung wurde gespeichert." }
                    }
                },
                FAILRESTORE : { TEXT : "Failed to restore the version" },
                FAILSAVE : { TEXT : "Failed to save the version" },
                KEEPVURRENTVERSION : { TEXT : "Keep current version" },
                MULTIPLETEMPLATE : { TEXT : "An export template has already been created for this version" },
                PROCESSDESCRIPTION : { TEXT : "Process description" },
                REPLACECURRENTVERSION : { TEXT : "Replace current version" },
                RESTOREDESCRIPTION : { TEXT : "1. Replace the current version with version {0}. Unsaved changes in the current version will be permanently lost.<br>2. Save the current version as version {1}. Version {0} will become current." },
                RESTOREVERSIONTITLE : { TEXT : "Restore version" },
                RESTOREWAY : { TEXT : "How do you want to restore the version?" },
                SAVEDON : { TEXT : "Saved on" },
                SAVEVERSIONBUTTON : { TEXT : "Save version" },
                SAVEVERSIONTITLE : { TEXT : "Save version" },
                SUCCESSRESTORE : { TEXT : "Version has been restored" },
                SUCCESSSAVE : { TEXT : "Version has been saved" },
                VERSIONCONTROL : { TEXT : "Version control" },
                VERSIONPROPERTIES : { TEXT : "Version properties" },
                VERSIONS : { TEXT : "Versions" },
                WARNING : { TEXT : "Current version will be replaced with version {0}. Unsaved changes in the current version will be permanently lost." }
            }
        }
    }
},
VALIDATION : {
    TEXT : "validation",
    CHILDREN : {
        CLOSE : { TEXT : "Schließen" },
        ERRORS : {
            TEXT : "",
            CHILDREN : {
                ACTIVEINSTANCES : { TEXT : "In der Diagrammversion werden aktive Instanzen ausgeführt" },
                ACTIVITYCONNECTORSINVALID : { TEXT : "Verbinden Sie die Sequenzflüsse erneut mit dem Element." },
                ACTIVITYDATAINVALID : { TEXT : "Ungültige Elementdaten." },
                ACTIVITYEMBEDDEDINTOWRONGACTIVITY : { TEXT : "Das Element ist in einem ungeeigneten Element verschachtelt." },
                ACTIVITYISOLATED : { TEXT : "Dieses Element hat keine Sequenzflüsse oder ist vom Startereignis aus nicht erreichbar." },
                ACTIVITYTYPEINVALID : { TEXT : "Ungültiger Elementtyp." },
                ACTIVITYWITHDUPLICATEALIAS : { TEXT : "Ein Element mit diesem Systemnamen ist bereits vorhanden." },
                ACTIVITYWITHDUPLICATEID : { TEXT : "Es sind Elemente mit derselben ID vorhanden." },
                ATTACHEDEVENTATTACHEDTOINVALIDACTIVITY : { TEXT : "Diesem Element kann kein Ereignis zugeordnet werden." },
                ATTACHEDEVENTMARKERINVALID : { TEXT : "Ungültiger angehängter Ereignismarker" },
                ATTACHEDEVENTTHROWSMESSAGE : { TEXT : "Angehängtes Ereignis kann keine Nachricht auslösen" },
                ATTACHEDEVENTTHROWSSIGNAL : { TEXT : "Angehängtes Ereignis kann kein Signal auslösen" },
                ATTACHEDEVENTUNATTACHED : { TEXT : "Angehängtes Ereignis ist keinem Element zugeordnet." },
                ATTACHEDEVENTWITHINBOUNDFLOW : { TEXT : "Angehängtes Ereignis kann keine eingehenden Sequenzflüsse haben." },
                ATTACHEDEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "Angehängtes Ereignis darf nur einen ausgehenden Sequenzfluss haben." },
                CASETASKMARKERASSIGNEEISNOTSET : { TEXT : "Für den Fall ist kein zuständiger festgelegt." },
                CASETASKMARKERINVALIDDATA : { TEXT : "Ungültiger Falltitel." },
                CASETASKMARKERINVALIDINPUTMAPPINGS : { TEXT : "Ungültige Falleingabezuordnungen." },
                CASETASKMARKERINVALIDRETURNMAPPINGS : { TEXT : "Ungültige Zuordnungen für die Rückgabe von Fällen." },
                CASETASKMARKERINVALIDTEMPLATE : { TEXT : "Ungültige Fallvorlage." },
                CASETASKWITHOUTINBOUNDFLOW : { TEXT : "Ein Case muss mindestens einen eingehenden Sequenzfluss haben." },
                CASETASKWITHOUTOUTBOUNDFLOW : { TEXT : "Ein Case darf nur einen ausgehenden Sequenzablauf haben." },
                CSHARPCODEEMPTY : { TEXT : "Leeres C#-Skript" },
                CSHARPCOMPILATIONERROR : { TEXT : "Fehler bei der Kompilierung des C#-Skripts" },
                CSHARPREFERENCEINVALID : { TEXT : "Ungültige Baugruppenreferenz in C#-Skript" },
                DIAGRAMEMPTY : { TEXT : "Diagramm ist leer" },
                DIAGRAMHASNOSTARTEVENT : { TEXT : "Das Diagramm muss mindestens ein Startereignis haben" },
                DIAGRAMHASNULLACTIVITIES : { TEXT : "Das Diagramm enthält unbekannte Elemente." },
                DIAGRAMHASNULLIDACTIVITIES : { TEXT : "Einige Elemente haben eine leere ID." },
                DIAGRAMMDOESNOTEXIST : { TEXT : "Es gibt kein solches Diagramm" },
                EMBEDDEDPROCESSCYCLE : { TEXT : "Schleife in eingebettetem Unterprozess erkannt" },
                EMBEDDEDPROCESSMUSTHAVESINGLESIMPLESTARTEVENT : { TEXT : "Eingebetteter Unterprozess darf nur ein Startereignis vom Typ „Keine“ haben." },
                EMBEDDEDPROCESSWITHOUTINBOUNDFLOW : { TEXT : "Eingebetteter Unterprozess muss mindestens einen eingehenden Sequenzfluss haben." },
                EMBEDDEDPROCESSWITHOUTOUTBOUNDFLOW : { TEXT : "Eingebetteter Unterprozess darf nur einen ausgehenden Sequenzfluss haben." },
                ENDEVENTATTACHED : { TEXT : "Endereignis kann nicht an ein Element angehängt werden." },
                ENDEVENTCATCHESMESSAGE : { TEXT : "Startereignis kann keine Nachricht abfangen" },
                ENDEVENTCATCHESSIGNAL : { TEXT : "Startereignis kann kein Signal erfassen" },
                ENDEVENTMARKERINVALID : { TEXT : "Ungültiger Marker für Endereignis" },
                ENDEVENTWITHOUTBOUNDFLOW : { TEXT : "Endereignis kann keine ausgehenden Sequenzflüsse haben." },
                ENDEVENTWITHOUTINBOUNDFLOW : { TEXT : "Endereignis muss mindestens einen eingehenden Sequenzfluss haben." },
                EVENTMARKERINVALID : { TEXT : "Ereignismarkierung ungültig" },
                EVENTMARKERMESSAGEINVALIDDATA : { TEXT : "Ungültige Eigenschaften für Nachrichtenereignis" },
                EVENTMARKERMESSAGEINVALIDNAME : { TEXT : "Ungültiger Nachrichtenname" },
                EVENTMARKERMESSAGETOUNKNOWNPROCESS : { TEXT : "Unbekannter Prozess in route1" },
                EVENTMARKERMESSAGETOUNKNOWNPROCESSAPP : { TEXT : "Unbekannte Prozessanwendung in Weiterleitung" },
                EVENTMARKERMESSAGEWITHINVALIDROUTE : { TEXT : "Ungültige Nachrichtenroute" },
                EVENTMARKERSIGNALINVALIDDATA : { TEXT : "Ungültige Signalereignisdaten" },
                EVENTMARKERSIGNALINVALIDNAME : { TEXT : "Ungültiger Signalname" },
                EVENTMARKERTIMERINVALIDDATA : { TEXT : "Timer ist im Timer-Ereignis nicht konfiguriert." },
                EXCLUSIVEGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "Ein exklusives Gateway muss mindestens einen eingehenden Sequenzfluss haben." },
                EXCLUSIVEGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "Ein exklusives Gateway muss mindestens einen ausgehenden Sequenzfluss haben." },
                EXPRESSIONINVALID : { TEXT : "Ausdruck ist ungültig" },
                FLOWCONNECTORSINVALID : { TEXT : "Verbinden Sie den Sequenzfluss erneut mit den Prozesselementen." },
                FLOWDEFINITIONINVALID : { TEXT : "Sequenzfluss-Definition ist ungültig." },
                FLOWINVALID : { TEXT : "Sequenzablauf ist ungültig." },
                FLOWSOURCEINVALID : { TEXT : "Der Sequenzablauf ist nicht mit einer Quelle verbunden." },
                FLOWTARGETINVALID : { TEXT : "Der Sequenzablauf ist nicht mit einem Ziel verbunden." },
                FOREACHLOOPMISSINGINPUTRULE : { TEXT : "Eingabesammlung ist für keine Schleife festgelegt" },
                FORLOOPMISSINGCARDINALITYRULE : { TEXT : "Kardinalität ist in für Schleifeneinstellungen nicht festgelegt" },
                GATEWAYMARKEREVENTBASEDOUTBOUNDTWOORMOREFLOWREQUIRED : { TEXT : "Für ein Ereignis-Gateway sind mindestens zwei ausgehende Sequenzflüsse erforderlich." },
                GATEWAYMARKEREVENTBASEDTARGETINTERMEDIATECATCHEVENT : { TEXT : "Zielaktivität für ereignisbasiertes Gateway muss einen Typ aufweisen, der von einem Zwischenereignis abgeleitet ist" },
                GATEWAYMARKEREVENTBASEDTARGETSINGLEINCOMINGSEQUENCEFLOW : { TEXT : "Ereignis-Gateway-Ziele dürfen keine zusätzlichen eingehenden Sequenzflüsse aufweisen." },
                GATEWAYMARKEREXLUSIVENOCONDITIONFOROUTBOUNDFLOW : { TEXT : "Für ein exklusives Gateway muss eine Bedingung für alle nicht standardmäßigen ausgehenden Sequenzflüsse festgelegt sein." },
                GATEWAYMARKEREXLUSIVENODEFAULTOUTBOUNDFLOW : { TEXT : "Ein exklusives Gateway darf nur einen standardmäßigen ausgehenden Sequenzfluss haben." },
                GATEWAYMARKERINCLUSIVENOCONDITIONFOROUTBOUNDFLOW : { TEXT : "Für ein inklusives Gateway muss eine Bedingung für alle bedingten ausgehenden Sequenzflüsse festgelegt sein." },
                GATEWAYMARKERINCLUSIVENODEFAULTOUTBOUNDFLOW : { TEXT : "Ein inklusives Gateway darf nur einen standardmäßigen ausgehenden Sequenzfluss haben." },
                GATEWAYMARKERINVALID : { TEXT : "Ungültiger Gateway-Marker" },
                GATEWAYMARKERPARALLELWITHNONEMPTYDEFINITION : { TEXT : "Ein paralleles Gateway darf keinen ausgehenden Standardsequenzfluss oder Bedingungen für Sequenzflüsse haben." },
                GLOBALFUNCTIONTASKMARKERINVALIDDATA : { TEXT : "Ungültige Eigenschaften der Aufgabenfunktion" },
                INBOUNDFLOWREQUIRED : { TEXT : "Mindestens ein eingehender Sequenzfluss ist erforderlich." },
                INCLUSIVEGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "Ein inklusives Gateway muss mindestens einen eingehenden Sequenzfluss haben." },
                INCLUSIVEGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "Inklusives Gateway muss mindestens einen ausgehenden Sequenzfluss haben." },
                INTERMEDIATEEVENTATTACHED : { TEXT : "Zwischenereignis kann nicht an ein Element angehängt werden." },
                INTERMEDIATEEVENTMARKERINVALID : { TEXT : "Ungültiger Marker für Zwischenereignis" },
                INTERMEDIATEEVENTWITHOUTINBOUNDFLOW : { TEXT : "Zwischenereignis muss mindestens einen eingehenden Sequenzfluss haben." },
                INTERMEDIATEEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "Zwischenereignis darf nur einen ausgehenden Sequenzfluss haben." },
                INVALIDDEFINITION : { TEXT : "Ungültige Aktivitätsdaten" },
                INVALIDSTARTFORMACTIVITYDEFINITION : { TEXT : "Nur ein „kein Start“-Ereignis kann ein Startformular haben." },
                LOOPINVALID : { TEXT : "Schleifeneinstellungen sind ungültig" },
                MESSAGEESSENCEINVALID : { TEXT : "Ungültige Nachrichtendefinition" },
                MESSAGEMAPPINGINVALIDMESSAGETYPE : { TEXT : "Ungültiger Nachrichtentyp in Zuordnung" },
                MESSAGEMAPPINGINVALIDPROPERTY : { TEXT : "Ungültige Eigenschaft in Zuordnung" },
                MESSAGEMAPPINGINVALIDRULE : { TEXT : "Ungültige Regel in Zuordnung" },
                MESSAGERECEIVERINVALID : { TEXT : "Ungültiger Nachrichtenempfänger" },
                NODEFAULTOUTBOUNDFLOW : { TEXT : "Standardmäßiger ausgehender Sequenzfluss ist erforderlich." },
                NOINBOUNDFLOWREQUIRED : { TEXT : "Für dieses Element sind keine eingehenden Sequenzflüsse zulässig." },
                NOOUTBOUNDFLOWREQUIRED : { TEXT : "Für dieses Element sind keine ausgehenden Sequenzflüsse zulässig." },
                OUTBOUNDFLOWREQUIRED : { TEXT : "Mindestens ein ausgehender Sequenzfluss ist erforderlich." },
                PARALLELGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "Ein paralleles Gateway muss mindestens einen eingehenden Sequenzfluss haben." },
                PARALLELGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "Ein paralleles Gateway muss mindestens einen ausgehenden Sequenzfluss haben." },
                RULEERROR : { TEXT : "Regelfehler" },
                RULEINVALIDDATA : { TEXT : "Regeldaten sind ungültig" },
                RULEINVALIDDEFINITION : { TEXT : "Regeldefinition ist ungültig " },
                RULEINVALIDTYPE : { TEXT : "Regeltyp ist ungültig " },
                RULEISREQUIRED : { TEXT : "Erforderliche Geschäftsregel fehlt" },
                SCRIPTTASKMARKERINVALIDDATA : { TEXT : "Das Skript ist für die Skript-Aufgabe nicht definiert." },
                SCRIPTTASKWITHOUTINBOUNDFLOW : { TEXT : "Skriptaufgabe muss mindestens einen eingehenden Sequenzfluss haben." },
                SCRIPTTASKWITHOUTOUTBOUNDFLOW : { TEXT : "Skriptaufgabe darf nur einen ausgehenden Sequenzfluss haben." },
                SERVICETASKMARKERINVALIDDATA : { TEXT : "Ungültige Eigenschaften für Serviceaufgabe" },
                SERVICETASKWITHOUTINBOUNDFLOW : { TEXT : "Serviceaufgabe muss mindestens einen eingehenden Sequenzfluss haben." },
                SERVICETASKWITHOUTOUTBOUNDFLOW : { TEXT : "Serviceaufgabe darf nur einen ausgehenden Sequenzablauf haben." },
                SINGLEOUTBOUNDFLOWREQUIRED : { TEXT : "Dieses Element muss einen ausgehenden Sequenzablauf haben." },
                STARTEVENTATTACHED : { TEXT : "Startereignis kann nicht an ein Element angehängt werden." },
                STARTEVENTMARKERINVALID : { TEXT : "Ungültiger Marker für Startereignis" },
                STARTEVENTMESSAGEDUPLICATED : { TEXT : "Das Diagramm hat mehr als ein Startereignis mit denselben Meldungsparametern" },
                STARTEVENTNONEDUPLICATED : { TEXT : "Diagramm hat mehr als ein einfaches (nicht definiertes) Startereignis" },
                STARTEVENTSCHEDULEMUSTEMPTY : { TEXT : "StartEventScheduleMustEmpty" },
                STARTEVENTSIGNALDUPLICATED : { TEXT : "Das Diagramm hat mehr als ein Startereignis mit denselben Signalparametern" },
                STARTEVENTTHROWSMESSAGE : { TEXT : "Startereignis kann keine Nachricht auslösen" },
                STARTEVENTTHROWSSIGNAL : { TEXT : "Startereignis kann kein Signal auslösen" },
                STARTEVENTTIMERSCHEDULEREQUIRED : { TEXT : "Timer ist im Startereignis nicht konfiguriert" },
                STARTEVENTWITHINBOUNDFLOW : { TEXT : "Startereignis darf keine eingehenden Sequenzflüsse aufweisen." },
                STARTEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "Startereignis darf nur einen ausgehenden Sequenzfluss haben." },
                SUBPROCESSINVALIDDEFINITION : { TEXT : "Ungültige Eigenschaften für externen Unterprozess." },
                SUBPROCESSUNEXISTINGPROCESSAPP : { TEXT : "Ungültiger Prozess ist als externer Unterprozess festgelegt" },
                SUBPROCESSUNEXISTINGPROCESSAPPSCHEME : { TEXT : "Externer Unterprozess verwendet ein ungültiges Prozessdiagramm, oder das Diagramm ist nicht vorhanden" },
                SUBPROCESSWITHOUTINBOUNDFLOW : { TEXT : "Externer Subprozess muss mindestens einen eingehenden Sequenzfluss haben." },
                SUBPROCESSWITHOUTOUTBOUNDFLOW : { TEXT : "Externer Subprozess darf nur einen ausgehenden Sequenzfluss haben." },
                TASKMARKERINVALID : { TEXT : "Benutzeraufgabe muss mindestens einen Bearbeiter haben." },
                TWODEFAULTOUTBOUNDFLOWS : { TEXT : "Nur ein standardmäßiger ausgehender Sequenzfluss ist zulässig." },
                TYPESCOMPILATIONERROR : { TEXT : "Fehler beim Kompilieren der Benutzerobjekttypen" },
                UNKNOWNERROR : { TEXT : "Interner Fehler" },
                UNKNOWNEXCEPTION : { TEXT : "Unbekannte Ausnahme beim Verarbeiten der Aktivität: {0}" },
                USERTASKMARKERASSIGNEEISNOTSET : { TEXT : "Beauftragter ist für Benutzeraufgabe nicht festgelegt" },
                USERTASKMARKERINVALIDDATA : { TEXT : "Benutzeraufgabe muss mindestens einen Bearbeiter haben." },
                USERTASKWITHOUTINBOUNDFLOW : { TEXT : "Eine Benutzeraufgabe muss mindestens einen eingehenden Sequenzfluss haben." },
                USERTASKWITHOUTOUTBOUNDFLOW : { TEXT : "Benutzeraufgabe darf nur einen ausgehenden Sequenzablauf haben." },
                WHILELOOPMISSINGCONDITIONRULE : { TEXT : "Bedingung ist in While-Schleifeneinstellungen nicht festgelegt" }
            }
        },
        FAILED : { TEXT : "Validierung nicht erfolgreich." }
    }
}