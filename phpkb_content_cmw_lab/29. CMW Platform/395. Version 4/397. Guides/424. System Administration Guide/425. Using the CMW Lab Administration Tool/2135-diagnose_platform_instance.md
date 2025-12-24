---
title: Diagnosing a CMW Platform Instance
kbId: 2135
---


# Diagnosing a CMW Platform Instance

**1**. Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Click the three bars button in the upper right corner of the Administration Tool.

_![The Configuration button in the Administration Tool](https://kb.cmwlab.com/assets/img_64245a593d229.png)_

**3.** The **Administration tool configuration** window appears.

**4.** Go to the **Diagnostics** tab.

**5.** Click the **Diagnostics** button.

_![The Diagnostics tab in the Administration Tool configuration](https://kb.cmwlab.com/assets/img_64245dc602927.png)_

**5.** The **Product instance profiling** window appears.

_![Collecting the memory dump for an instance](https://kb.cmwlab.com/assets/img_64245da1e2dc5.png)_

**6.** Select an instance that you want to diagnose.

**7.** To collect an instance memory dump, click **Save d****ump**.

**7.1.**A message appears indicating the start of the instance dump collection.

**7.2.**Click **OK**.

_![The memory dump collection start message](https://kb.cmwlab.com/assets/img_64245df8efe0d.png)_

**7.3.**A window appears with the `procdump.exe` program running.

![Running program procdump.exe](https://kb.cmwlab.com/assets/img_64245cf44f097.png)

Procdump.exe program running

**7.4.**Wait for the `procdump.exe` program to close.

**7.5.** The **`procdump.exe`**program will save the instance memory dump to a `.DMP` file in the `temp` subfolder of the folder specified in the **Diagnostics results** field on the **[Diagnostics](#diagnostics_tab)** [tab](#diagnostics_tab) in the Administration Tool configuration window.

**7.6.**To view the dump, click **Show result** on the **[Diagnostics](#diagnostics_tab)** [tab](#diagnostics_tab).

**7.7.**The **Diagnostics**folder opens (see the actual folder name may differ).

**7.8.** Open the `temp` subfolder.

_![The location of the instance memory dump files](https://kb.cmwlab.com/assets/img_64245fc354db0.png)_

**8.** To collect an instance diagnostic data, select the instance and click **Start** in the **Product instance profiling** window.

_![The instance diagnostics window](https://kb.cmwlab.com/assets/img_64246019a26d0.png)_

**8.1.** A message appears indicating the start of the instance diagnostics.

**8.2.**Click **OK**.

_![The diagnostics start message](https://kb.cmwlab.com/assets/img_6424616374201.png)_

**8.3.**The **Progress** column of the instances list shows the diagnostics progress bar.

**8.4.** The diagnostics will continue until you click **Stop**.

**8.5.**Click **Stop**.

_![The diagnostics progress bar](https://kb.cmwlab.com/assets/img_642460c957f82.png)_

**8.6.**A message appears indicating the start of the diagnostic data collection.

**8.7.**Click **OK**.

_![The diagnostic data collection start message](https://kb.cmwlab.com/assets/img_642460f932e62.png)_

**8.8.**A window appears with the `PerfVew.exe` program running.

![Running program PerfVew.exe](https://kb.cmwlab.com/assets/img_64246133b77dc.png)

PerfVew.exe program running

**8.9.**Wait for the `PerfVew.exe` program to close.

**8.10.**The message appears indicating that the data collection is complete.

**8.11.**Click **OK**.

_![Diagnostic data collection completion message](https://kb.cmwlab.com/assets/img_6424626d2bf16.png)_

**8.12.**The `PerfVew.exe` program will save the instance diagnostic data to a `.ZIP` archive in the folder specified in the **Diagnostics results** field on the [**Diagnostics** tab](#diagnostics_tab) of the **Administration Tool c****onfiguration**window.

**8.13.**To view the diagnostic files folder, click **Show result** on the [**Diagnostics** tab](#diagnostics_tab).

_![Diagnostic results folder example](https://kb.cmwlab.com/assets/img_64246376a7d72.png)_

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
