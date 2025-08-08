---
title: Configuring the CMW Lab Administration Tool
kbId: 2134
---


# Configuring the CMW Lab Administration Tool

**1.** Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.**  Click the three bars in the upper right corner of the Administration Tool.

_![Configuration button in the Administration Tool](https://kb.cmwlab.com/assets/img_642448d17571d.png)_

**3.** The **Administration tool configuration** window appears.

**4.** Configure the settings on the following tabs:

- **General**
- **IIS**
- **Paths**
- **Diagnostics**

**5.****General** tab — view the status of the system software components powering the **CMW Platform** and install any missing components.

_![General configuration](https://kb.cmwlab.com/assets/img_64255351df43f.png)_

- The **P****roduct components status** table lists third-party software powering the **CMW Platform**:
  - The boxes for the installed required software in the first column are checked.
  - To install the missing software:
    - Check its box and click **Save**.
    - The selected software will be automatically installed in the background.

**6.****IIS** tab — configure the default website settings for new **CMW Platform** instances. You can change these settings later while creating an instance.

_![IIS configuration](https://kb.cmwlab.com/assets/img_64244cc2b10a1.png)_

- **Domain Name** — specify the website domain name for new instances.
- **Port** — specify the website network port for new instances.
- **Enable IIS logging** — check this box to turn on the Internet Information Services logging on new instances.

**7.**  **Paths** tab — specify the default paths for new **CMW Platform**instances. You can change these paths later while installing the product or creating a new instance.

_![Paths configuration](https://kb.cmwlab.com/assets/img_64244d2578dd9.png)_

- **Product version install path** — specify the installation folder for new **CMW Platform** software versions.
- **Product** i**nstances** — specify the deployment folder for new instances.
- **Backups** — specify the backup folder for new instances.
- **System log** — specify the system log folder for new instances.
- **Uploaded files** — specify the uploaded files folder for new instances.
- **Elasticsearch server** — specify the Elasticsearch server URL for new system instances.

**8.****Diagnostics** tab — configure the paths for various logs and diagnose the instances.

_![Diagnostics tab](https://kb.cmwlab.com/assets/img_64244d36eeda7.png)_

- **Administration tool log** — specify the Administration Tool log folder. To view the log, click **Show log**.

  ![Administration Tool log example](https://kb.cmwlab.com/assets/img_64244e870ef55.png)

  Administration Tool log example
- **MSI package installer log** — specify the folder to store the **CMW Platform** software installation log. To view the log, click **Show log**.

  ![MSI package installer log example](https://kb.cmwlab.com/assets/img_64244e50a108d.png)

  MSI package installer log example
- **Diagnostics results** — specify the diagnostic logs folder for the instances. To open the diagnostic logs folder, click **Show result**.

  ![Diagnostic results folder example](https://kb.cmwlab.com/assets/img_64246376a7d72.png)

  Diagnostic results folder example
- **Diagnostics** button — click to run diagnostics on a **CMW Platform** instance. See [Diagnosing a CMW Platform Instance](https://kb.comindware.ru/article.php?id=2135) .

**9.**  After configuring the parameters, click **Save**.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
