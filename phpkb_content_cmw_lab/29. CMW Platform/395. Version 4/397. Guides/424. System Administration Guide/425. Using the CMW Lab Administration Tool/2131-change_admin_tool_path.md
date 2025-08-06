---
title: Changing the CMW Lab Administration Tool Installation Path
kbId: 2131
---


# Changing the CMW Lab Administration Tool Installation Path

By default, the **CMW Lab** **Administration Tool** is installed on drive `C`.

**1.** To change the installation path, specify it in the  `INSTALLFOLDER` parameter of the `msiexec` command line utility.

**2.** For example, use the following command to install the Administration Tool on drive `D`:

```
msiexec /i "D:\Platform.Install.msi" INSTALLFOLDER="D:\Program Files\CMW Lab\Install and Administration Tool"
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
