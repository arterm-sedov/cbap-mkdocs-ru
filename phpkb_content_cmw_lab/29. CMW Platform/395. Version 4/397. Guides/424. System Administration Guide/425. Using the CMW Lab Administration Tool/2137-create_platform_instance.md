---
title: Creating a CMW Platform Instance
kbId: 2137
---


# Creating a CMW Platform Instance

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.**Click **Create**.

_![Creating a new instance](https://kb.cmwlab.com/assets/img_64256ee989e68.png)_

**2.**The **Creating a product instance** window appears.

_![Configuring a new instance](https://kb.cmwlab.com/assets/img_64256fcb775d9.png)_

**3.**Specify the parameters of the new system instance.

- **Instance name** — enter a ***unique*** name to identify the instance. You won't be able to change the instance name after creating the instance.
- **Domain name** — enter a domain name to access the instance website.
- **Port** — enter a port number to access the instance website.
- **Version** — select a CMW Platform software version for the instance.
- **Path** — specify a folder to deploy the instance.
- **Restore from a backup** — check this box and select a `.CDBBZ` backup file to deploy the instance from a backup (see [Creating a CMW Platform Instance from a Backup](https://kb.comindware.ru/article.php?id=2138).
- **Set file paths** — check this box to change the default folders for the instance files.

**4.** If you checked the **Set file paths** box, click **Next**.

**4.1.**The **Set product instance file paths** window appears.

_![Configuring the instance file paths](https://kb.cmwlab.com/assets/img_6425705be3f2c.png)_

**4.2.**Specify the paths for the instance files.

**5.** Click **Create**.

**6.** The Administration Tool will create a new instance.

**7.** A message should appear indicating the instance creation success.

**8.** Click **Close**.

_![The instance creation success message](https://kb.cmwlab.com/assets/img_6425841d34f0c.png)_

**9.** The new instance will appear in the **Product instances** list.

_![New instance in the product instances list](https://kb.cmwlab.com/assets/img_64258451c964e.png)_

**10.** The new instance website will appear in the Internet Information Services (IIS) Manager.

_![The instance website listed in the Internet Information Services (IIS) Manager](https://kb.cmwlab.com/assets/img_642589c4a5ff8.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
