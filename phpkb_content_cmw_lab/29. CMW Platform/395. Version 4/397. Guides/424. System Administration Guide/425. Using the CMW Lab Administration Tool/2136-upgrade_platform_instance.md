---
title: Upgrading a Deployed Instance to a New CMW Platform Software Version
kbId: 2136
---


# Upgrading a Deployed Instance to a New CMW Platform Software Version

You can upgrade a deployed instance to a new **CMW Platform** software version.

During the upgrade, the Administration Tool performs the following:

- Stops the instance website and IIS application pool.
- Deletes the old configuration files and symbolic links to software the binaries from the instance configuration folder (`C:\ProgramData\CMW Lab\Instances\Instance Name\Config` by default).
- Creates new configuration files and symbolic links to software binaries in the instance configuration folder (`C:\ProgramData\CMW Lab\Instances\Instance Name\Config` by default).
- Restarts the instance website and IIS application pool.

**1.** Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Select the instance to upgrade in the **Product instances** list.

**3.** Click **Change version**.

_![Selecting an instance to upgrade](https://kb.cmwlab.com/assets/img_64255d0ea86a2.png)_

**4.**  The **Product instance version update** window appears.

**5.** Select the desired software **Version** from the dropdown.

**6.** Click **Change version**.

_![Choosing a new software version for the instance](https://kb.cmwlab.com/assets/img_64255f25e86c8.png)_

**7.** The Administration Tool will upgrade the instance.

**8.** A successful upgrade message should appear.

**9.** Click **Close**.

_![The instance upgrade success message](https://kb.cmwlab.com/assets/img_64255f3a4460e.png)_

**10.** To open the instance website, right-click it in the **Product instances** list.

**11.** Select **Go to the website** from the context menu.

_![Opening the instance website](https://kb.cmwlab.com/assets/img_64255ef0bc8f4.png)_

**12.**The **CMW Platform** login page opens in a web browser.

_![CMW Platform login page](https://kb.cmwlab.com/assets/img_6425606220031.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
