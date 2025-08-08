---
title: Configuring a CMW Platform Instance
kbId: 2141
---


# Configuring a CMW Platform Instance

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Select a **CMW Platform** instance to configure from the **Product instances** list.

**3.** Click **Configure**.

_![Selecting a CMW Platform instance to configure](https://kb.cmwlab.com/assets/img_6426a712122e7.png)_

**4.** The **Product instance configuration** window appears with the following tabs:

- **IIS**
- **Instance paths**

**5.** **IIS** tab — configure the Internet Information Services for the instance website.

_![Configuring the IIS for the instance](https://kb.cmwlab.com/assets/img_6426acc7d0657.png)_

- **Instance name** — the instance name is read-only. It is set upon the instance creation.
- **Domain name** — enter the website domain name for the instance.
- **Port** — enter the website port number for the instance.
- **Enable IIS Logging** — check this box to turn on the Internet Information Services logging for the instance.
- **Enable Active Directory single sign-on** — check this box to enable login to the instance website via the Active Directory.

**5.1.** Click **Apply**to save the IIS configuration.

**5.2.** A message should appear indicating the successful configuration update.

**5.2.** Click **Close**.

_![The instance configuration update success message](https://kb.cmwlab.com/assets/img_6426acefbb5ad.png)_

**6.**  **Instance paths**tab — view and configure the instance data locations, or move the instance data to the new folders if needed.

_![Moving the instance data to the new locations](https://kb.cmwlab.com/assets/img_6426aec9964f8.png)_

**6.1.** Specify the required paths to store the instance data.

**6.2.** To move the instance data to the new folders, click **Move**.

**6.3.** Confirm the move.

_![Confirming the instance data move](https://kb.cmwlab.com/assets/img_6426af80d5e4d.png)_

**OR…**

**6.3.** To change the instance paths without moving the existing data, click **Save**.

**6.5.** Confirm the paths change without moving the instance data.

_![Confirming the instance paths change without moving the data](https://kb.cmwlab.com/assets/img_6426b03b764e5.png)_

**6.6.**The Administration Tool will change the instance paths and, if necessary, move the data to the new folders.

**6.7.** A message should appear indicating the successful instance paths change.

_![The instance path change success message](https://kb.cmwlab.com/assets/img_6426b5d7e4eec.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
