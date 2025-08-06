---
title: Initializing a CMW Platform Instance
kbId: 2146
---


# Initializing a CMW Platform Instance

At the first **CMW Platform** start, you need to initialize the instance: create an administrator account, activate the product, and configure a connection to the Elasticsearch server.

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** In the **Product instances** list, right-click the instance to initialize.

**3.** Select **Go to website** from the context menu.

_![Navigate to the system instance website](https://kb.cmwlab.com/assets/img_6426ff0c61860.png)_

**4.** Wait for the instance website to launch.

**5.** The administrator account creation screen opens.

**6.** Enter the administrator account credentials and click **Create the account**.

**Warning!**The **CMW Platform** instance must always have at least one administrator account. You might need it for system recovery. You should not delete the administrator account created during the instance initialization, even if the accounts are synchronized later with the Active Directory.

_![Creating the system administrator account](https://kb.cmwlab.com/assets/img_64270351ede64.png)_

**7.** The instance activation screen opens.

_![Skipping the product activation on the first instance start](https://kb.cmwlab.com/assets/img_6426fa995b671.png)_

**8.** Click **Skip** to skip the activation. You can activate the product later.

**9.** The Elasticsearch connection configuration screen opens.

_![Configuring the Elasticsearch connection](https://kb.cmwlab.com/assets/img_64270284a2c37.png)_

**10.** In the **URI** field, enter the previously configured Elasticsearch server address, for example, `http://localhost:9200`.

**11.** If required, enter the Elasticsearch credentials: **Username** and **Password**.

**11.** Specify the desired Elasticsearch **Index prefix**.

**12.** Click **Next**.

**13.** If the data initialization screen opens, click **Update**.

**15.** Wait until the **CMW Platform** home page opens.

**16.** The instance deployment is complete. Now you can create and use the applications powered by the **CMW Platform**.

_![CMW Platform home page](https://kb.cmwlab.com/assets/img_6426fd1327c26.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
