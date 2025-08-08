ARCHITECTURE : {
    TEXT : "Architecture",
    CHILDREN : {
        COLUMNS : {
            TEXT : "",
            CHILDREN : {
                CREATEDBY : { TEXT : "Creator" },
                CREATEDON : { TEXT : "Created on" },
                DIAGRAMNAME : { TEXT : "Diagram Name" },
                DIAGRAMTYPE : { TEXT : "Diagram Type" },
                NAME : { TEXT : "Name" }
            }
        },
        DEFAULTNAME : { TEXT : "New Architecture Diagram" },
        DIGRAMTYPE : {
            TEXT : "",
            CHILDREN : {
                ARCHITECTURE : { TEXT : "Architecture" },
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
                                ROLETEMPLATES : { TEXT : "Role templates" }
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
        EMPTYARCHITECTURE : { TEXT : "There are no architecture items to display" },
        ERRORS : {
            TEXT : "errors",
            CHILDREN : {
                CANNOTEXPAND : { TEXT : "Can not expand subprocess which contains pool" },
                ELEMENTCYCLE : { TEXT : "Can not create element that links itself or parent element" }
            }
        },
        EXPENDABLE : { TEXT : "Reverse effect" },
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
                ALL : { TEXT : "All" },
                INSTANCE : { TEXT : "Linked Object" },
                LIST : {
                    TEXT : "Linked Record Type List",
                    CHILDREN : {
                        ALLLISTS : { TEXT : "All lists" }
                    }
                },
                MENU : { TEXT : "Linked Object" },
                RECORDTYPE : { TEXT : "Linked Record Type" },
                TYPE : {
                    TEXT : "Linked Object Type",
                    CHILDREN : {
                        ABSTRACT : { TEXT : "Abstract" },
                        CASE : { TEXT : "Case" },
                        PROCESS : { TEXT : "Process" },
                        PROJECT : { TEXT : "Project" },
                        UNSET : { TEXT : "Not set" }
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
            TEXT : "overview",
            CHILDREN : {
                ENTERPRISENAME : { TEXT : "Enterprise name" },
                ISFAVORITE : { TEXT : "Favorite" },
                SAVE : { TEXT : "Save" }
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
                                    TEXT : "Sequence number",
                                    CHILDREN : {
                                        DESCRIPTION : { TEXT : "Element sequence number" }
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
                        FAIL : { TEXT : "Failed to save the regulation export template." },
                        SUCCESS : { TEXT : "The regulation export template has been saved." }
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
        CLOSE : { TEXT : "Close" },
        ERRORS : {
            TEXT : "",
            CHILDREN : {
                ACTIVEINSTANCES : { TEXT : "There are active instances running on diagram version" },
                ACTIVITYCONNECTORSINVALID : { TEXT : "Reconnect the sequence flows to the element." },
                ACTIVITYDATAINVALID : { TEXT : "Invalid element data." },
                ACTIVITYEMBEDDEDINTOWRONGACTIVITY : { TEXT : "The element is nested into an inappropriate element." },
                ACTIVITYISOLATED : { TEXT : "This element does not have any sequence flows or is not reachable from the start event." },
                ACTIVITYTYPEINVALID : { TEXT : "Invalid element type." },
                ACTIVITYWITHDUPLICATEALIAS : { TEXT : "An element with this system name already exists." },
                ACTIVITYWITHDUPLICATEID : { TEXT : "There are elements with the same ID." },
                ATTACHEDEVENTATTACHEDTOINVALIDACTIVITY : { TEXT : "An event cannot be attached to this element." },
                ATTACHEDEVENTMARKERINVALID : { TEXT : "Invalid attached event marker" },
                ATTACHEDEVENTTHROWSMESSAGE : { TEXT : "Attached event can't throw message" },
                ATTACHEDEVENTTHROWSSIGNAL : { TEXT : "Attached event can't throw signal" },
                ATTACHEDEVENTUNATTACHED : { TEXT : "Attached event is not attached to an element." },
                ATTACHEDEVENTWITHINBOUNDFLOW : { TEXT : "Attached event can't have incoming sequence flows." },
                ATTACHEDEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "Attached event must have only one outgoing sequence flow." },
                CASETASKMARKERASSIGNEEISNOTSET : { TEXT : "Assignee is not set for the case." },
                CASETASKMARKERINVALIDDATA : { TEXT : "Invalid case title." },
                CASETASKMARKERINVALIDINPUTMAPPINGS : { TEXT : "Invalid case input mappings." },
                CASETASKMARKERINVALIDRETURNMAPPINGS : { TEXT : "Invalid case return mappings." },
                CASETASKMARKERINVALIDTEMPLATE : { TEXT : "Invalid case template." },
                CASETASKWITHOUTINBOUNDFLOW : { TEXT : "A case must have at least one incoming sequence flow." },
                CASETASKWITHOUTOUTBOUNDFLOW : { TEXT : "A case must have only one outgoing sequence flow." },
                CSHARPCODEEMPTY : { TEXT : "Empty C# script" },
                CSHARPCOMPILATIONERROR : { TEXT : "Error during C# script compilation" },
                CSHARPREFERENCEINVALID : { TEXT : "Invalid assembly reference in C# script" },
                DIAGRAMEMPTY : { TEXT : "Diagram is empty" },
                DIAGRAMHASNOSTARTEVENT : { TEXT : "The diagram must have at least one start event" },
                DIAGRAMHASNULLACTIVITIES : { TEXT : "The diagram contains unknown elements." },
                DIAGRAMHASNULLIDACTIVITIES : { TEXT : "Some elements have an empty ID." },
                DIAGRAMMDOESNOTEXIST : { TEXT : "There is no such diagram" },
                EMBEDDEDPROCESSCYCLE : { TEXT : "Loop is detected in embedded subprocess" },
                EMBEDDEDPROCESSMUSTHAVESINGLESIMPLESTARTEVENT : { TEXT : "Embedded subprocess must have only one none start event." },
                EMBEDDEDPROCESSWITHOUTINBOUNDFLOW : { TEXT : "Embedded subprocess must have at lease one incoming sequence flow." },
                EMBEDDEDPROCESSWITHOUTOUTBOUNDFLOW : { TEXT : "Embedded subprocess must have only one outgoing sequence flow." },
                ENDEVENTATTACHED : { TEXT : "End event cannot be attached to an element." },
                ENDEVENTCATCHESMESSAGE : { TEXT : "Start event cannot catch a message" },
                ENDEVENTCATCHESSIGNAL : { TEXT : "Start event cannot catch a signal" },
                ENDEVENTMARKERINVALID : { TEXT : "Invalid end event marker" },
                ENDEVENTWITHOUTBOUNDFLOW : { TEXT : "End event cannot have outgoing sequence flows." },
                ENDEVENTWITHOUTINBOUNDFLOW : { TEXT : "End event must have at least one incoming sequence flow." },
                EVENTMARKERINVALID : { TEXT : "Event marker invalid" },
                EVENTMARKERMESSAGEINVALIDDATA : { TEXT : "Invalid message event properties" },
                EVENTMARKERMESSAGEINVALIDNAME : { TEXT : "Invalid message name" },
                EVENTMARKERMESSAGETOUNKNOWNPROCESS : { TEXT : "Unknown process in route1" },
                EVENTMARKERMESSAGETOUNKNOWNPROCESSAPP : { TEXT : "Unknown process application in route" },
                EVENTMARKERMESSAGEWITHINVALIDROUTE : { TEXT : "Invalid message route" },
                EVENTMARKERSIGNALINVALIDDATA : { TEXT : "Invalid signal event data" },
                EVENTMARKERSIGNALINVALIDNAME : { TEXT : "Invalid signal name" },
                EVENTMARKERTIMERINVALIDDATA : { TEXT : "Timer is not configured in the timer event." },
                EXCLUSIVEGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "An exclusive gateway must have at least one incoming sequence flow." },
                EXCLUSIVEGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "An exclusive gateway must have at least one outgoing sequence flow." },
                EXPRESSIONINVALID : { TEXT : "Expression is invalid" },
                FLOWCONNECTORSINVALID : { TEXT : "Reconnect the sequence flow to the process elements." },
                FLOWDEFINITIONINVALID : { TEXT : "Sequence flow definition is invalid." },
                FLOWINVALID : { TEXT : "Sequence flow is invalid." },
                FLOWSOURCEINVALID : { TEXT : "The sequence flow is not connected to a source." },
                FLOWTARGETINVALID : { TEXT : "The sequence flow is not connected to a target." },
                FOREACHLOOPMISSINGINPUTRULE : { TEXT : "Input collection is not set in for any loop" },
                FORLOOPMISSINGCARDINALITYRULE : { TEXT : "Cardinality is not set in for loop settings" },
                GATEWAYMARKEREVENTBASEDOUTBOUNDTWOORMOREFLOWREQUIRED : { TEXT : "Two or more outgoing sequence flows are required for an event gateway." },
                GATEWAYMARKEREVENTBASEDTARGETINTERMEDIATECATCHEVENT : { TEXT : "Target activity for event-based gateway must have a type derived from intermediate catch event" },
                GATEWAYMARKEREVENTBASEDTARGETSINGLEINCOMINGSEQUENCEFLOW : { TEXT : "Event gateway targets must not have any additional incoming sequence flows." },
                GATEWAYMARKEREXLUSIVENOCONDITIONFOROUTBOUNDFLOW : { TEXT : "An exclusive gateway must have a condition set for all non-default outgoing sequence flows." },
                GATEWAYMARKEREXLUSIVENODEFAULTOUTBOUNDFLOW : { TEXT : "An exclusive gateway must have only one default outgoing sequence flow." },
                GATEWAYMARKERINCLUSIVENOCONDITIONFOROUTBOUNDFLOW : { TEXT : "An inclusive gateway must have a condition set for all conditional outgoing sequence flows." },
                GATEWAYMARKERINCLUSIVENODEFAULTOUTBOUNDFLOW : { TEXT : "An inclusive gateway must have only one default outgoing sequence flow." },
                GATEWAYMARKERINVALID : { TEXT : "Invalid gateway marker" },
                GATEWAYMARKERPARALLELWITHNONEMPTYDEFINITION : { TEXT : "A parallel gateway must not have outgoing default sequence flow or conditions for sequence flows." },
                GLOBALFUNCTIONTASKMARKERINVALIDDATA : { TEXT : "Invalid task function properties" },
                INBOUNDFLOWREQUIRED : { TEXT : "At least one incoming sequence flow is required." },
                INCLUSIVEGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "An inclusive gateway must have at least one incoming sequence flow." },
                INCLUSIVEGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "Inclusive gateway must have at least one outgoing sequence flow." },
                INTERMEDIATEEVENTATTACHED : { TEXT : "Intermediate event cannot be attached to an element." },
                INTERMEDIATEEVENTMARKERINVALID : { TEXT : "Invalid intermediate event marker" },
                INTERMEDIATEEVENTWITHOUTINBOUNDFLOW : { TEXT : "Intermediate event must have at least one incoming sequence flow." },
                INTERMEDIATEEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "Intermediate event must have only one outgoing sequence flow." },
                INVALIDDEFINITION : { TEXT : "Invalid activity data" },
                INVALIDSTARTFORMACTIVITYDEFINITION : { TEXT : "Only a none start event can have a starting form." },
                LOOPINVALID : { TEXT : "Loop settings are invalid" },
                MESSAGEESSENCEINVALID : { TEXT : "Invalid message definition" },
                MESSAGEMAPPINGINVALIDMESSAGETYPE : { TEXT : "Invalid message type in mapping" },
                MESSAGEMAPPINGINVALIDPROPERTY : { TEXT : "Invalid property in mapping" },
                MESSAGEMAPPINGINVALIDRULE : { TEXT : "Invalid rule in mapping" },
                MESSAGERECEIVERINVALID : { TEXT : "Invalid message receiver" },
                NODEFAULTOUTBOUNDFLOW : { TEXT : "Default outgoing sequence flow is required." },
                NOINBOUNDFLOWREQUIRED : { TEXT : "No incoming sequence flows are allowed for this element." },
                NOOUTBOUNDFLOWREQUIRED : { TEXT : "No outgoing sequence flows are allowed for this element." },
                OUTBOUNDFLOWREQUIRED : { TEXT : "At least one outgoing sequence flow is required." },
                PARALLELGATEWAYWITHOUTINBOUNDFLOW : { TEXT : "A parallel gateway must have at least one incoming sequence flow." },
                PARALLELGATEWAYWITHOUTOUTBOUNDFLOW : { TEXT : "A parallel gateway must have at least one outgoing sequence flow." },
                RULEERROR : { TEXT : "Rule error" },
                RULEINVALIDDATA : { TEXT : "Rule data is invalid" },
                RULEINVALIDDEFINITION : { TEXT : "Rule definition is invalid " },
                RULEINVALIDTYPE : { TEXT : "Rule type is invalid " },
                RULEISREQUIRED : { TEXT : "Missing mandatory business rule" },
                SCRIPTTASKMARKERINVALIDDATA : { TEXT : "The script is not defined for the script task." },
                SCRIPTTASKWITHOUTINBOUNDFLOW : { TEXT : "Script task must have at least one incoming sequence flow." },
                SCRIPTTASKWITHOUTOUTBOUNDFLOW : { TEXT : "Script task must have only one outgoing sequence flow." },
                SERVICETASKMARKERINVALIDDATA : { TEXT : "Invalid service task properties" },
                SERVICETASKWITHOUTINBOUNDFLOW : { TEXT : "Service task must have at least one incoming sequence flow." },
                SERVICETASKWITHOUTOUTBOUNDFLOW : { TEXT : "Service task must have only one outgoing sequence flow." },
                SINGLEOUTBOUNDFLOWREQUIRED : { TEXT : "This element must have one outgoing sequence flow." },
                STARTEVENTATTACHED : { TEXT : "Start event cannot be attached to an element." },
                STARTEVENTMARKERINVALID : { TEXT : "Invalid start event marker" },
                STARTEVENTMESSAGEDUPLICATED : { TEXT : "The diagram has more than one start event with the same message parameters" },
                STARTEVENTNONEDUPLICATED : { TEXT : "Diagram has more than one plain (undefined) start event" },
                STARTEVENTSCHEDULEMUSTEMPTY : { TEXT : "startEventScheduleMustEmpty" },
                STARTEVENTSIGNALDUPLICATED : { TEXT : "The diagram has more than one start event with the same signal parameters" },
                STARTEVENTTHROWSMESSAGE : { TEXT : "Start event can't throw message" },
                STARTEVENTTHROWSSIGNAL : { TEXT : "Start event can't throw signal" },
                STARTEVENTTIMERSCHEDULEREQUIRED : { TEXT : "Timer is not configured in the start event" },
                STARTEVENTWITHINBOUNDFLOW : { TEXT : "Start event must not have incoming sequence flows." },
                STARTEVENTWITHOUTOUTBOUNDFLOW : { TEXT : "Start event must have only one outgoing sequence flow." },
                SUBPROCESSINVALIDDEFINITION : { TEXT : "Invalid external subprocess properties." },
                SUBPROCESSUNEXISTINGPROCESSAPP : { TEXT : "Invalid process is set as external subprocess" },
                SUBPROCESSUNEXISTINGPROCESSAPPSCHEME : { TEXT : "External sub-process uses an invalid process diagram or the diagram does not exist" },
                SUBPROCESSWITHOUTINBOUNDFLOW : { TEXT : "External subprocess must have at least one incoming sequence flow." },
                SUBPROCESSWITHOUTOUTBOUNDFLOW : { TEXT : "External subprocess must have only one outgoing sequence flow." },
                TASKMARKERINVALID : { TEXT : "User task must have at least one assignee." },
                TWODEFAULTOUTBOUNDFLOWS : { TEXT : "Only one default outgoing sequence flow is allowed." },
                TYPESCOMPILATIONERROR : { TEXT : "Error during user object types compilation" },
                UNKNOWNERROR : { TEXT : "Internal error" },
                UNKNOWNEXCEPTION : { TEXT : "Unknown exception when processing activity: {0}" },
                USERTASKMARKERASSIGNEEISNOTSET : { TEXT : "Assignee is not set for user task" },
                USERTASKMARKERINVALIDDATA : { TEXT : "User task must have at least one assignee." },
                USERTASKWITHOUTINBOUNDFLOW : { TEXT : "A user task must have at least one incoming sequence flow." },
                USERTASKWITHOUTOUTBOUNDFLOW : { TEXT : "User task must have only one outgoing sequence flow." },
                WHILELOOPMISSINGCONDITIONRULE : { TEXT : "Condition is not set in while loop settings" }
            }
        },
        FAILED : { TEXT : "Validation failed." }
    }
}