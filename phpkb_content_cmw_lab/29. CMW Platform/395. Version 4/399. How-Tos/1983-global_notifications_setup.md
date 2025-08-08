---
title: Setting up global notifications
kbId: 1983
---


# Setting up global notifications

Global notifications are global messages, or alerts for all users of the system (for example, a notification about maintenance works). Global notifications are displayed for all logged users in the «Notifications» tab, as well as on the login page, for a specified period of time.

To configure global system notifications, follow these steps:

**1.** Go to the «**Administration**» area, then — to «***Global configuration***». Tick the «***Enable global notifications listening***» checkbox.

_![«Global configuration» section](https://kb.cmwlab.com/assets/2021-12-27_12h49_25.png)_

**2.** Create a process for sending global notifications.

_![Process diagram](https://kb.cmwlab.com/assets/2021-12-27_12h51_07.png)_

**3.** Go to the settings for the send message event, then — to «***Advanced properties***» tab. Select «***Base notification***» in «***Destination***» and specify the communication route. If you don’t have a preconfigured base notification communication route, click the «***Add***» button and create a new route.

_![Configuring communication route for send message event](https://kb.cmwlab.com/assets/2021-12-27_12h53_01.png)_

**4.** After saving the send message event settings, publish the process diagram.

**5.** To trigger the global notification, create a process instance for sending notifications:

_![Global notification on the user interface](https://kb.cmwlab.com/assets/2021-12-27_12h57_08.png)_

Global notification will be also displayed on the login page.

_![Global notification on the login page](https://kb.cmwlab.com/assets/2021-12-27_13h00_47.png)_

**Entering text when triggering a notification**

For convenience, you can add the possibility to enter a notification text when the process starts.

**1.** To do this, add a form for the start event of the notification sending process.

_![Adding a start form](https://kb.cmwlab.com/assets/2021-12-27_13h04_46.png)_

**2.** Create an attribute with the notification text and add it to the form.

_![Configuring the start form](https://kb.cmwlab.com/assets/2021-12-27_13h06_48.png)_

**3.** Now edit the communication route to be able to send the message text.

Go to the settings of the communication route for base notification. In the «***Message Attributes***» tab, add a text attribute:

_![Adding attributes to the communication route](https://kb.cmwlab.com/assets/2021-12-27_13h11_09.png)_

**4.** Then go to the «***Message Properties***» tab and in the «***Message text***» field add the system name of the created attribute in curly braces. For convenience, you can copy the attribute name from the left pane:

_![Message properties configuration](https://kb.cmwlab.com/assets/2021-12-27_13h14_07.png)_

**5.** Then go back to the process diagram and open the settings for the send message event, go to the «***Message Data***» tab and configure the correspondence between the communication route attribute and the attribute that we created earlier:

_![Data mapping](https://kb.cmwlab.com/assets/2021-12-27_13h17_03.png)_

**6.** Save the settings and publish the process diagram.

Now, when starting the process, you will need to enter the notification message.

_![Entering notification message](https://kb.cmwlab.com/assets/2021-12-27_13h18_31.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
