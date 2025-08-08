
----------------------

Ingestion date: 2025-07-21 19:31:28
Title: Comindware Platform V4 knowledge base for AI ingestion
Description: Provide this file to your AI agent. For better results, add the prompt below
Source: https://kb.cmwlab.com/category.php?id=29
Files analyzed: 122
Estimated tokens: 115.1k

----------------------

## Prompting instructions

### EN Prompt example

- Answer the following question: <YOUR_QUESTION>
- In your answer, provide links to the referenced articles in the format:
  `https://kb.cmwlab.com/article.php?id={kbId}`
  Take `{kbId}` from the frontmatter of the original Markdown articles.

### RU Пример промпта

- Ответь на следующий вопрос: <ВАШ_ВОПРОС>
- В ответе приведи ссылки на использованные статьи в формате:
  `https://kb.cmwlab.com/article.php?id={kbId}`
  `{kbId}` возьми из frontmatter исходного текста статей в формате Markdown.

## Sections

Directory structure:
└── 29. CMW Platform/
    ├── 2162-platform_4_7_content.md
    └── 395. Version 4/
        ├── 2162-platform_4_7_content.md
        ├── 397. Guides/
        │   ├── 2163-guides_content.md
        │   └── 424. System Administration Guide/
        │       ├── 2163-guides_content.md
        │       ├── 425. Using the CMW Lab Administration Tool/
        │       │   ├── 2130-install_admin_tool.md
        │       │   ├── 2131-change_admin_tool_path.md
        │       │   ├── 2132-launch_admin_tool.md
        │       │   ├── 2133-install_platform_software.md
        │       │   ├── 2134-config_admin_tool.md
        │       │   ├── 2135-diagnose_platform_instance.md
        │       │   ├── 2136-upgrade_platform_instance.md
        │       │   ├── 2137-create_platform_instance.md
        │       │   ├── 2138-create_instance_from_backup.md
        │       │   ├── 2139-uninstall_platform_version.md
        │       │   ├── 2140-delete_platform_instance.md
        │       │   ├── 2141-config_platform_instance.md
        │       │   ├── 2142-instance_status_indication.md
        │       │   ├── 2143-restore_instance_backup.md
        │       │   ├── 2144-add_instance_to_list.md
        │       │   ├── 2145-refresh_instance_list.md
        │       │   ├── 2146-init_platform_instance.md
        │       │   ├── 2148-stop_platform_instance.md
        │       │   ├── 2149-start_platform_instance.md
        │       │   └── 2150-view_instance_paths.md
        │       └── 426. Deploying the CMW Platform/
        │           ├── 2151-platform_system_requirements.md
        │           └── 2152-platform_architecture_config.md
        ├── 398. Training/
        │   ├── 1109-lesson_1_intro.md
        │   ├── 1110-lesson_2_data_register.md
        │   ├── 2147-lesson_3_business.md
        │   ├── 2153-lesson_4_monitoring.md
        │   ├── 2154-lesson_5_data.md
        │   ├── 2155-lesson_6_advanced.md
        │   ├── 2156-lesson_7_auto_calc.md
        │   ├── 2157-lesson_8_accounts.md
        │   ├── 2158-lesson_9_documents.md
        │   └── 2159-lesson_10_files.md
        ├── 399. How-Tos/
        │   ├── 1943-export_template_csharp.md
        │   ├── 1945-export_collections_images.md
        │   ├── 1947-qr_code_csharp_button.md
        │   ├── 1955-import_excel_data.md
        │   ├── 1965-task_notify_change_text.md
        │   ├── 1971-transfer_solution_settings.md
        │   ├── 1973-import_excel_data.md
        │   ├── 1983-global_notifications_setup.md
        │   ├── 1985-button_display_formula.md
        │   ├── 1987-form_rule_hide_field.md
        │   ├── 1989-record_many_many.md
        │   ├── 1991-calculated_attribute_formula.md
        │   ├── 1993-change_process_real_time.md
        │   ├── 1997-import_excel_data.md
        │   ├── 1999-list_color_indicator.md
        │   ├── 2001-receive_mail.md
        │   ├── 2003-combine_values.md
        │   ├── 2005-attribute_date_time_display_config.md
        │   ├── 2007-solution_setup_recommendations.md
        │   ├── 2009-attr_value_color.md
        │   ├── 2020-attr_record_filter.md
        │   ├── 2022-attr_record_account_filter.md
        │   ├── 2050-example_field_filter.md
        │   ├── 2070-form_dynamic_display.md
        │   ├── 2076-object_search_filter.md
        │   ├── 2082-notification_template_body.md
        │   ├── 2084-text_attribute_mask.md
        │   ├── 2085-context_change_bap.md
        │   ├── 2089-account_templates_usage.md
        │   ├── 2090-data_model_class_diagrams.md
        │   ├── 2091-application_data_model.md
        │   ├── 2093-universal_record_url.md
        │   ├── 2096-chevron_coloring_logic.md
        │   ├── 2098-mass_process_local_var.md
        │   ├── 2103-holiday_calendar.md
        │   ├── 2105-record_template_multiapp.md
        │   ├── 2112-adapters.md
        │   ├── 2113-administration.md
        │   ├── 2127-periodic_task_reminders.md
        │   ├── 2129-cancel_process_button.md
        │   ├── 416. Scenarios/
        │   │   ├── 2106-scenario_actions.md
        │   │   ├── 2108-creating_scenario.md
        │   │   ├── 2109-configuring_scenario.md
        │   │   └── 2110-scenario_definition_list.md
        │   ├── 419. Buttons/
        │   │   ├── 2114-buttons.md
        │   │   ├── 2115-deleting_button.md
        │   │   ├── 2116-creating_button.md
        │   │   ├── 2117-button_designer.md
        │   │   ├── 2118-template_button_list.md
        │   │   └── 2119-button_list_operations.md
        │   └── 420. Forms/
        │       ├── 2120-template_form_list.md
        │       ├── 2122-deleting_form.md
        │       ├── 2123-form_list_operations.md
        │       ├── 2124-forms.md
        │       └── 2125-form_designer.md
        ├── 400. Expression examples/
        │   ├── 411. N3 language/
        │   │   ├── 2024-calculate_objects_condition.md
        │   │   ├── 2104-calculate_child_records.md
        │   │   ├── 2107-task_object_value.md
        │   │   └── 2126-substitution_parameters_calc.md
        │   ├── 412. C# language/
        │   │   ├── 2088-upload_file.md
        │   │   ├── 2095-add_group_accounts.md
        │   │   ├── 2097-upload_list_folder.md
        │   │   ├── 2099-delete_related_record.md
        │   │   ├── 2101-goto_showcase_record.md
        │   │   └── 2128-download_table_entries.md
        │   └── 413. Expression language/
        │       ├── 2086-call_related_data.md
        │       ├── 2087-expression_language_operators.md
        │       └── 2094-calculate_hyperlink.md
        ├── 401. Troubleshooting/
        │   ├── 1949-buttons_not_shown.md
        │   ├── 1951-reference_field_empty.md
        │   ├── 1953-invalid_instance_reference.md
        │   ├── 1962-process_fails_several_records.md
        │   ├── 1964-script_operation_error.md
        │   ├── 1967-optimize_calculate_attribute.md
        │   ├── 1969-process_id_not_found.md
        │   ├── 1975-process_notify_no_info.md
        │   ├── 1977-attribute_history_view.md
        │   ├── 1979-change_attribute_data_type.md
        │   ├── 1981-archived_records_in_expression.md
        │   ├── 1995-hard_read_text_table.md
        │   ├── 2016-table_open_error.md
        │   └── 2102-form_reference_field_error.md
        └── 407. Integrations/
            ├── 1941-core_api_methods.md
            ├── 1955-import_excel_data.md
            ├── 2074-solution_api_methods.md
            └── 2161-get_started_with_cmw_api.md

## Articles

================================================
FILE: 2162-platform_4_7_content.md
================================================
---
title: CMW Platform v4.7. Section content
kbId: 2162
---

# CMW Platform v4.7. Section content

- [Deploying the CMW Platform](https://kb.cmwlab.com/category.php?id=426)
- [Using the CMW Lab Administration Tool](https://kb.cmwlab.com/category.php?id=425)
- [Training](https://kb.cmwlab.com/category.php?id=398)
- [How-Tos](https://kb.cmwlab.com/category.php?id=399)
- [Integrations](https://kb.cmwlab.com/category.php?id=407)
- [Expression Examples](https://kb.cmwlab.com/category.php?id=400)
- [Troubleshooting](https://kb.cmwlab.com/category.php?id=401)

================================================
FILE: 395. Version 4/2162-platform_4_7_content.md
================================================
---
title: CMW Platform v4.7. Section content
kbId: 2162
---

# CMW Platform v4.7. Section content

- [Deploying the CMW Platform](https://kb.cmwlab.com/category.php?id=426)
- [Using the CMW Lab Administration Tool](https://kb.cmwlab.com/category.php?id=425)
- [Training](https://kb.cmwlab.com/category.php?id=398)
- [How-Tos](https://kb.cmwlab.com/category.php?id=399)
- [Integrations](https://kb.cmwlab.com/category.php?id=407)
- [Expression Examples](https://kb.cmwlab.com/category.php?id=400)
- [Troubleshooting](https://kb.cmwlab.com/category.php?id=401)

================================================
FILE: 395. Version 4/397. Guides/2163-guides_content.md
================================================
---
title: Guides. Section content
kbId: 2163
---

# Guides. Section content

- [Deploying the CMW Platform](https://kb.cmwlab.com/category.php?id=426)
- [Using the CMW Lab Administration Tool](https://kb.cmwlab.com/category.php?id=425)

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/2163-guides_content.md
================================================
---
title: Guides. Section content
kbId: 2163
---

# Guides. Section content

- [Deploying the CMW Platform](https://kb.cmwlab.com/category.php?id=426)
- [Using the CMW Lab Administration Tool](https://kb.cmwlab.com/category.php?id=425)

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2130-install_admin_tool.md
================================================
---
title: Installing the CMW Lab Administration Tool
kbId: 2130
---

# Installing the CMW Lab Administration Tool

**1.** Download the **CMW Lab Administration Tool** Windows Installer Package, for instance, `CMWPlatform_4.2.495.0.msi`

**2.** Run the downloaded Windows Installer Package.

_![Windows Installer Package](https://kb.cmwlab.com/assets/img_642401c90993b.png)_

**3.**  If the User Account Control window appears, click  **Yes**  to confirm the installation.

**4.** The Administration Tool will be installed (by default on disk  `C`).

**5.** If a **CMW Platform** software version matching the Administration Tool version has not yet been installed, the Administration Tool initial window appears.

_![The Administration Tool initial window](https://kb.cmwlab.com/assets/img_6424046c0456a.png)_

**6.** If a **CMW Platform** software version matching the Administration Tool version has already been installed, the Administration Tool main window appears.

_![The Administration Tool main window](https://kb.cmwlab.com/assets/img_64240810230f9.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2131-change_admin_tool_path.md
================================================
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

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2132-launch_admin_tool.md
================================================
---
title: Launching the CMW Lab Administration Tool
kbId: 2132
---

# Launching the CMW Lab Administration Tool

**1.**Right-click the **CMW Lab Administration Tool** shortcut on the Windows desktop.

_![The Administration Tool shortcut](https://kb.cmwlab.com/assets/img_64241708477c9.png)_

**2.**In the dropdown, select **Run as administrator**.

**3.** If the User Account Control window appears, click **Yes** to confirm the launch.

**4.** If a **CMW Platform** software version matching the Administration Tool version has not yet been installed, the Administration Tool initial window appears.

_![The Administration Tool initial window](https://kb.cmwlab.com/assets/img_6424046c0456a.png)_

**5.** If a **CMW Platform** software version matching the Administration Tool version has already been installed, the Administration Tool main window appears.

_![The Administration Tool main window](https://kb.cmwlab.com/assets/img_64240810230f9.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2133-install_platform_software.md
================================================
---
title: Installing the CMW Platform Software
kbId: 2133
---

# Installing the CMW Platform Software

**1.** Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** If a **CMW Platform** software version matching the Administration Tool version has not yet been installed, the Administration Tool initial window appears.

**3.**Click **Installation and configuration**.

_![The Administration Tool initial window](https://kb.cmwlab.com/assets/img_642551e2f33bd.png)_

**4.** If the **Verifying the minimum software requirements**window appears:

**4.1.** Check the boxes for any missing software components you need to install.

**4.2.** Click **Install**.

![Verifying the minimum software requirements](https://kb.cmwlab.com/assets/img_642551b934000.png)

*Verifying the minimum software requirements*

**4.3.** The Administration Tool will check the system software configuration and install any necessary missing components in a popup window. Wait until this step completes and the popup window closes.

_![The missing software components installation progress](https://kb.cmwlab.com/assets/img_642435cf53120.png)_

**5.** When the missing components are installed, close the **Verifying the minimum software requirements**window.

**6.** Click **Installation and configuration** again in the Administration Tool initial window.

**7.** The **License agreement** window appears.

_![The license agreement](https://kb.cmwlab.com/assets/img_642551992c1e7.png)_

**8.** Check the  **I accept** box, to accept the license agreement.

**9.** Click **Next**.

**10.**The **Installing the new product version** window appears.

**11.** If needed, change the software installation path.

**12.** To upgrade all existing **CMW Platform** instances to the new software version, check the   **Upgrade all product instances** box.

**13.** Click **Install**.

_![Choosing the installation folder for the new software version](https://kb.cmwlab.com/assets/img_6425516654f4d.png)_

**14.** The installation progress window appears. Wait until the installation is complete.

_![The software installation progress](https://kb.cmwlab.com/assets/img_64243c57a0c8d.png)_

**15.** When the installation is complete, a message appears showing the installed software version.

**16.** Click **Close**.

_![The message showing the installed software version](https://kb.cmwlab.com/assets/img_6425512046336.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2134-config_admin_tool.md
================================================
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

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2135-diagnose_platform_instance.md
================================================
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

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2136-upgrade_platform_instance.md
================================================
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

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2137-create_platform_instance.md
================================================
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

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2138-create_instance_from_backup.md
================================================
---
title: Creating a CMW Platform Instance from a Backup
kbId: 2138
---

# Creating a CMW Platform Instance from a Backup

**1.** Follow the instructions in the [Creating a CMW Platform Instance](https://kb.comindware.ru/article.php?id=2137) article.

**2.** At [step 3](https://kb.cmwlab.com/article.php?id=2137), in the **Creating a product instance**window, check the **Restore from a backup** box and select a `.CDBBZ` backup file.

_![Selecting a backup file to create a new instance](https://kb.cmwlab.com/assets/img_642590d860030.png)_

**3.** The new instance will appear in the **Product instances** list and IIS Manager.

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2139-uninstall_platform_version.md
================================================
---
title: Uninstalling a CMW Platform Software Version
kbId: 2139
---

# Uninstalling a CMW Platform Software Version

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Select a **CMW Platform** software version to uninstall from the **Product versions** list.

**3.** The **Uninstall** button activates if no instances use the selected software version. The **Instances** column shows the number of instances using the software version.

**4.** Click **Uninstall**.

_![Selecting a software version to uninstall](https://kb.cmwlab.com/assets/img_64259cd790cfc.png)_

**5.** Confirm the software version uninstallation.

_![Confirming the software version uninstallation](https://kb.cmwlab.com/assets/img_64259d4ba47b4.png)_

**6.** The Administration Tool will remove the software version.

**7.** An message should appear indicating the successful uninstallation.

**8.** Click **Close**.

_![The software uninstallation success message](https://kb.cmwlab.com/assets/img_6425a0b9e1a06.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2140-delete_platform_instance.md
================================================
---
title: Deleting a CMW Platform Instance
kbId: 2140
---

# Deleting a CMW Platform Instance

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Select a **CMW Platform** instance to delete from the **Product instances** list.

**3.** Click **Delete**.

_![Selecting an instance to delete](https://kb.cmwlab.com/assets/img_6425a47365df3.png)_

**4.** The **Deleting the version** window appears.

**5.** To permanently delete all the instance data (along with the instance website), check the **Delete files and folders** box.

**6.** Click **Delete**.

_![Reviewing the instance deletion](https://kb.cmwlab.com/assets/img_6425a5ba84f5d.png)_

**7.** Confirm the instance deletion.

_![Confirming the instance deletion](https://kb.cmwlab.com/assets/img_6425a4ca94d66.png)_

**8.** The Administration Tool deletes the instance.

**9.** An message should appear indicating the successful instance deletion.

**10.** Click **Close**.

_![The instance deletion success message](https://kb.cmwlab.com/assets/img_6425a69582730.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2141-config_platform_instance.md
================================================
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

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2142-instance_status_indication.md
================================================
---
title: CMW Platform Instance Status Indication
kbId: 2142
---

# CMW Platform Instance Status Indication

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.**The first column of the **Product instances** list can show status icons:

- A warning triangle ![](https://kb.cmwlab.com/assets/img_6426beccd714f.png)  — the instance configuration was not found. Try changing the system instance file paths (see   [Configuring a CMW Platform Instance](https://kb.comindware.ru/article.php?id=2141)).
- A stop sign ![](https://kb.cmwlab.com/assets/img_6426bf0b2ac98.png) — the website or IIS application pool for the instance is stopped. To start the website, right-click the instance and select **Start website** from the context menu.

_![CMW Platform instance status icons](https://kb.cmwlab.com/assets/img_6426bde243e28.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2143-restore_instance_backup.md
================================================
---
title: Restoring a CMW Platform Instance from a Backup
kbId: 2143
---

# Restoring a CMW Platform Instance from a Backup

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Select the instance to restore in the **Product i****nstances**  list.

**3.** Click **Restore**.

_![Selecting an instance to restore](https://kb.cmwlab.com/assets/img_6426c4b92e3d4.png)_

**4.** The **Restore the instance**  window appears.

**5.** Select **Restore the instance from a backup file**.

***6.*** Click **Next**.

_![Selecting the restore mode](https://kb.cmwlab.com/assets/img_6426c4a80cdd6.png)_

**7.** Specify the `.CDBBZ` backup file path.

**8.** Click **Restore**.

_![Selecting a backup file to restore the instance](https://kb.cmwlab.com/assets/img_6426c561ea375.png)_

**9.** Confirm the instance restore.

_![Confirming the instance restore from a backup](https://kb.cmwlab.com/assets/img_6426c57548663.png)_

**10.** Click **Yes**.

**11.** The Administration Tool will restore the instance from the backup.

**12.** A message should appear indicating the successful restore.

**13.** Click **Close**.

_![The successful restore message](https://kb.cmwlab.com/assets/img_6426c59458e94.png)_

**13.** If the instance restore fails, the **Error messages** window appears. 

**14.** To view the error log, click **Log**.

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2144-add_instance_to_list.md
================================================
---
title: Adding a Missing CMW Platform Instance to the Instance List
kbId: 2144
---

# Adding a Missing CMW Platform Instance to the Instance List

If a **CMW Platform**instance was present on the computer but does not appear in the **Product instances** list, you can re-register it in the Administration Tool.

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Click **Add**. This button only shows if at least one unregistered instance is present.

_![Adding the missing instances](https://kb.cmwlab.com/assets/img_6426eadb6f225.png)_

**3.** The **Add existing product instances to the list** window appears.

**4.** Select the instance to add, or check the **Add all instances and corresponding product versions** box.

**5.** Click **Add**.

_![Selecting the missing instances to add](https://kb.cmwlab.com/assets/img_6426e9b69f527.png)_

**6.** Click **Refresh list**to update the **Product instances** list.

**7.** The added instance appears in the list.

_![Updating the instance list with the newly added instance](https://kb.cmwlab.com/assets/img_6426eb9ec34eb.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2145-refresh_instance_list.md
================================================
---
title: Refreshing the CMW Platform Instance List
kbId: 2145
---

# Refreshing the CMW Platform Instance List

To view up-to-date **CMW Platform**instance data: newly added instances, database size, log size, and backup size, refresh the **Product instances** list.

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Click **Refresh list**.

**3.** The **Product instances** list will show the updated data.

_![Refreshing the instance list](https://kb.cmwlab.com/assets/img_6426f89301857.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2146-init_platform_instance.md
================================================
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

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2148-stop_platform_instance.md
================================================
---
title: Stopping a CMW Platform Instance
kbId: 2148
---

# Stopping a CMW Platform Instance

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** In the **Product instances** list, right-click the instance to stop.

**3.** Select **Stop the website**from the context menu.

_![Stopping a CMW Platform instance using the Administration Tool](https://kb.cmwlab.com/assets/img_642a8fcc6e312.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2149-start_platform_instance.md
================================================
---
title: Starting a CMW Platform Instance
kbId: 2149
---

# Starting a CMW Platform Instance

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** In the **Product instances** list, right-click the instance to start.

**3.** Select **Start the website**from the context menu.

_![Starting a CMW Platform instance using the Administration Utility](https://kb.cmwlab.com/assets/img_642aa6bf453be.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/425. Using the CMW Lab Administration Tool/2150-view_instance_paths.md
================================================
---
title: Viewing  the Paths to a CMW Platform Instance
kbId: 2150
---

# Viewing the Paths to a CMW Platform Instance

By default, an instance is deployed in the `C:\ProgramData\CMW Lab\Instances\InstanceName` folder. The **Name** column in the **Product instances** list shows the `InstanceName`.

The actual paths to the instance files may differ. Use the Administration Tool to view the instance paths*.*

**1.**Launch the Administration Tool (see [Launching the CMW Lab Administration Tool](https://kb.cmwlab.com/article.php?id=2132)).

**2.** Select an instance from the **Product instances** list.

**3.** Click **Configure**.

_![Selecting an instance to view its paths](https://kb.cmwlab.com/assets/img_642a9a7a1e4af.png)_

4. Go to the Instance paths tab in the Product instance configuration window. To configure the paths, see [Configuring a CMW Platform Instance](https://kb.comindware.ru/article.php?id=2141).

_![Viewing the paths to an instance](https://kb.cmwlab.com/assets/img_642a9ad0bdd07.png)_

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/426. Deploying the CMW Platform/2151-platform_system_requirements.md
================================================
---
title: CMW Platform System Requirements
kbId: 2151
---

# CMW Platform System Requirements

The enterprise-grade low-code **CMW Platform** allows rapidly building business process management solutions.

Below are the minimum system requirements to deploy and use the **CMW Platform**.

## Hardware Requirements

### Database and Application Server

| Specification | Requirement | | |
| --- | --- | --- | --- |
| Up to 500 users and 10,000 processes/month | Up to 5,000 users and 50,000 processes/month | Add for every 4,000 users and 30,000 processes/month |
| Processor | 8 cores, 3.7GHz or faster | 8 cores, 3.7GHz or faster | 4 cores, 3.7GHz or faster |
| RAM | 32GB | 64GB | 32GB |
| Storage | SSD (200GB) + HDD for the uploaded documents | SSD (200GB) + HDD for the uploaded documents | SSD (200GB) + HDD for the uploaded documents |
| Network connection | 1Gbps | 10Gbps |  |

### End-User Computer

| Specification | Requirement |
| --- | --- |
| Processor | x86 or x64 compatible |
| Memory | 8GB |
| Display resolution | 1024x768 and above |
| Network connection | 10Mbs |

## Software Requirements

### Database and Application Server

| Specification | Requirement | |
| --- | --- | --- |
| Windows | Linux |
| OS | Windows Server Standard 2022 | - Fedora Server 40 - Red Hat Enterprise Linux 9.3 |
| Database management system | Apache Ignite | |
| Web server | Internet Information Services (IIS) 10 and above | NGINX 1.24 and above |
| Auxiliary software | - NET 6.0 - .NET Framework 4.8.1 - Kafka 3.6.0 and above - Elasticsearch 8.10 and above | - NET 6.0 - Mono 6.12 - Kafka 3.6.0 and above - Elasticsearch 8.10 and above |

### End-User Computer

| Specification | Requirement |
| --- | --- |
| OS | Windows, macOS, or Linux |
| Web browser | Google Chrome, Mozilla Firefox, or Microsoft Edge (latest public version) |
| Additional software | To open the files downloaded from the system |

================================================
FILE: 395. Version 4/397. Guides/424. System Administration Guide/426. Deploying the CMW Platform/2152-platform_architecture_config.md
================================================
---
title: CMW Platform Architecture, Landscape, and Software &amp; Hardware Configuration
kbId: 2152
---

# CMW Platform Architecture, Landscape, and Software &amp; Hardware Configuration

Version: 1.0

Published: 07.04.2023

## Introduction

The CMW Platform is a low-code business process management software powered by a modern technology stack.

This article contains:

- Brief description of the CMW Platform architecture
- Recommended deployment landscape options
- Recommended software and hardware configurations

## Definitions

**Product** — CMW Platform software.

**Instance** — deployed CMW Platform website.

**System** — complete hardware and software environment powered by the CMW Platform.

**Application server** — deployed instance of the CMW Platform.

**Application** — standalone business solution running on the application server.

**Active users** — users who regularly generate data on the application server.

**DAS** — storage device directly connected to the application server.

**SAN** — storage area network.

**IOPS** — throughput expressed as a number of input/output operations per second.

## System Architecture

The System architecture is client-server, component-multilayer, and service-oriented. It supports extension via plugins and adapters.

The System comprises the following subsystems:

- *Web application*: single page application (SPA) based on Marionette, Backbone, React, and Redux.
- *Mobile app*: React Native powered by Expo.
- *Backend*: service components based on .NET 6.0, .NET Framework 4.8 (Windows), Mono 6.12 (Linux), and JDK 17.
- *Database management system (DBMS)*: CMW Elastic Data (proprietary) that stores the data in the file system or the Apache Ignite (depending on the load requirements and deployment configuration).
- *Full-text search engine*: Lucene.NET.
- *Transaction logging and analysis, and System**data monitoring*: Elasticsearch, Kibana.
- *File logging*: NLog.
- *Integration modules*: see [Integration with External Systems](#mcetoc_1g7eann3f2).

![CMW Platform architecture diagram](https://kb.cmwlab.com/assets/CMW_Platform_Architecture_EN_v1.6.svg)

*CMW Platform architecture diagram*

### System Security and Resilience

The System supports the following security and fault tolerance mechanisms.

- *External security*:
  - Kerberos and OpenID user authentication,
  - firewall,
  - reverse proxy.
- *Internal security*: role-based security model.
- *Fault tolerance:*redundant servers, data storage, and processing nodes.
- *Scalability*: additional request-processing servers.

### Integration with External Systems

The System supports the following external integration types.

- *Git* — version control for applications created in the System.
- *OData* — communication with external systems via the REST API.
- *OpenLDAP (Active Directory)* — authentication, account management, and single sign-on.
- *SMTP/IMAP/Exchange* — receiving and sending e-mail.
- *ESB ( RabbitMQ/MSMQ)* — communication with external systems in distributed and federated environments.

## System deployment landscape

To ensure uninterrupted operation, deploy the System in an environment with adequate performance and fault tolerance.

You can deploy the System for internet or intranet access:

- *Minimum configuration* — deploy on one virtual or physical machine.
- *Production configuration —* deploy on the customer's premises in a fault-tolerant landscape per the customer's requirements.

### Recommended System Deployment Options

#### Minimum Configuration

A minimal System configuration suitable for demonstrations and pilot projects comprises the following components:

1. CMW Platform instance.
2. CMW Elastic Data DBMS.
3. Elasticsearch server in a single-node configuration to log transactions and data changes.

![Minimal System configuration](https://kb.cmwlab.com/assets/CMW_Platform_Minimal_Configuration_EN.svg)

Minimum System configuration

#### Production Configuration

A production System configuration with resource duplication, redundancy, and fault tolerance includes the following components.

1. CMW Platform instance.
2. CMW Elastic Data DBMS.
3. Elasticsearch server to log transactions and data changes.
4. NGINX reverse proxy to filter out unwanted requests and relay valid requests to the internal network.
5. Zabbix server to monitor service availability and free disk space.
6. Mail server (SMTP/IMAP) (optional) to send notifications.
7. LDAP server (optional) for centralized management of the network infrastructure.
8. Git server (optional) for version control of the applications built with the CMW Platform.

_![Production System configuration](https://kb.cmwlab.com/assets/CMW_Platform_Production_Configuration_EN.svg)_

Production use scenarios impose the following System requirements.

- *Security* — implemented by setting up a firewall and a reverse proxy server.
- *Fault tolerance* — implemented by setting up the redundant servers and additional data server nodes.
- *Scalability* — implemented by adding more request-processing servers.

_![Typical landscape of the System services](https://kb.cmwlab.com/assets/CMW_Typical_Service_Landscape_EN.svg)_

### Recommended Set of Application Servers

To improve application development and testing efficiency, as well as application fault tolerance and security, deploy several application servers.

When defining the technical requirements, determine the need for each of these servers:

1. *Development server* to develop the applications.
2. *Testing server (pre-production)* to test the applications.
3. *Primary server (production)* to run the applications.
4. *Standby server* to use in case of primary server overload or failure.

## The System Hardware Configuration

See below the recommended hardware specifications to deploy the System at the customer's premises under Windows or Linux.

### Application Server Configuration

The application server provides user and third-party system interaction, data input, processing, and storage (database, configuration, uploaded files, logs, and backups).

Host the application server on a physical or virtual machine.

The following guidelines will help you configure the application server hardware.

In a minimum configuration, you can deploy a single application server to develop, test, and run the applications.

The following recommended specifications provide a comfortable experience for the end users, citizen developers, and testers of the CMW Platform applications.

Actual hardware requirements may vary significantly and depend on the following factors:

- number of active users,
- number of applications,
- number of running processes,
- number of configured calculations, rules, conditions, and data dependencies,
- size of stored data and documents.

We recommend deploying the subsystems (Apache Ignite, Elasticsearch, NGINX, Zabbix) and the Product instance virtual machines on different physical machines.

Communication channels between the System nodes must provide at least 10 Gbps bandwidth.

#### An Example Hardware Resource Calculation for a Fault-Tolerant System

The table below shows an example of hardware allocation for the following number of users:

- 500 registered
- 200 active
- 25 online

| **Server name** | **Description** | **Logical CPU cores, 3.0 GHz and above** | **RAM, GB** | **Data storage, GB** | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Software partition** **SSD** | **Database** **Highly reliablehigh speed** **SSD** | **Uploads** **HDD** | **Logs** **HDD** | **Backups** **HDD** |
| **Infrastructure services** | | | | | | | | |
| NGINX-reverse-proxy1 | Reverse proxy (VPS) | 2 | 2 | 24 |  |  |  |  |
| NGINX-reverse-proxy2 | Reverse proxy (VPS) | 2 | 2 | 24 |  |  |  |  |
| Zabbix1 | Monitoring and tracking system (VPS) | 2 | 4 | 24 | 128 |  |  |  |
| Zabbix2 | Monitoring and tracking system (VPS) | 2 | 4 | 24 | 128 |  |  |  |
|  |  |  |  |  |  |  |  |  |
| **Production environment** | | | | | | | | |
| CMWP-node1\* | CMW Platform application server (VPS) | 8 | 32 | 64 | 128 | 1024 | 16 | 512 |
| CMWP-node2\* | CMW Platform application server (VPS) | 8 | 32 | 64 | 128 | 16 |
| CMWP-node3\* | CMW Platform application server (VPS) | 8 | 32 | 64 | 128 | 16 |
| Elasticsearch-node1\* | Elasticsearch logging server (VPS) | 4 | 16 | 24 | 128 |  | 16 | 512 |
| Elasticsearch-node2\* | Elasticsearch logging server (VPS) | 4 | 16 | 24 | 128 |  | 16 |
| Elasticsearch-node3\* | Elasticsearch logging server (VPS) | 4 | 16 | 24 | 128 |  | 16 |
| \* Virtual servers of the same service must be hosted on different physical machines. | | | | | | | | |
| The connection speed between the servers must be at least 10 Gbps. | | | | | | | | |
|  | | | | | | | | |
| **Test and development environment** | | | | | | | | |
| Git-server | GitLab | 2 | 4 | 24 | 128 |  |  |  |
| CMWP-test | CMW Platform application server (VPS) | 8 | 24 | 64 | 128 | 32 | 16 | 128 |
| CMWP-dev | CMW Platform application server (VPS) | 8 | 24 | 64 | 128 | 32 | 16 | 128 |
| Elasticsearch | Elasticsearch logging server (VPS) | 4 | 16 | 24 | 128 |  | 16 | 128 |
|  |  |  |  |  |  |  |  |  |
| **Total by resource type** | | **66** | **224** | **536** | **1536** | **1088** | **144** | **1408** |

#### Minimum Primary and Backup Application Server Configuration

| **Number of users** | **CPU cores** 3.7 GHz and above (Add 1 core per 100 active users per application) | **RAM, GB(Add 4GB** per 100 active users per application) | **HDD, GB** | **SSD, GB** |
| --- | --- | --- | --- | --- |
| **Primary Application Server** | | | | |
| 1–200 active | 4 + (1 × app qty) | 16 + (4 × app qty) | 16 | 16 |
| 200 active | 4 + (2 × app qty) | 16 + (8 × app qty) | 16 × app qty | 16 × app qty |
| 300 active | 4 + (3 × app qty) | 16 + (12 × app qty) | 16 × app qty | 16 × app qty |
| 400 active | 4 + (4 × app qty) | 16 + (16 × app qty) | 16 × app qty | 16 × app qty |
| **Standby Application Server** | | | | |
| 1­–200 | 4 + (1 × app qty) | 16 + (4 × app qty) | 16 × app qty | 8 × app qty |
| 200 | 4 + (2 × app qty) | 16 + (8 × app qty) | 16 × app qty | 8 × app qty |
| 300 | 4 + (3 × app qty) | 16 + (12 × app qty) | 16 × app qty | 8 × app qty |
| 400 | 4 + (4 × app qty) | 16 + (16 × app qty) | 16 × app qty | 8 × app qty |

#### Minimum Development and Test Server Configuration

| **Number of users** | **CPU cores** 3.7 GHz and above | **RAM,GB** | **HDD,GB** | **SSD,GB** |
| --- | --- | --- | --- | --- |
| **Development server** | | | | |
| 1–100 | 4 | 16 | 16 | 16 |
| **Test server** | | | | |
| 1–100 | 4 | 16 | 16 | 16 |

### Storage Configuration

In a minimum configuration, all application server data folders can be stored on a single partition on a high-performance SSD.

High-performance storage systems (SSD DAS/SAN) must provide a throughput of at least 100,000 IOPS per application server.

When defining the System specifications, determine the amount of space allocated on the high-performance (SSD DAS/SAN) and low-performance storage systems (HDD DAS/SAN).

To optimize data processing, storage, and backup, configure separate storage for the application server data folders:

- *Database and configuration files* — SSD DAS/SAN. The application server constantly processes this data online, which creates a high load on the storage subsystem.
- *Files uploaded by users* — HDD DAS/SAN. Uploaded files are stored for a long time and outside of the database. They are fetched via links. Hence, a high-performance storage subsystem is optional for them.
- *System logs* — HDD DAS/SAN. Log file writing operations create a minimal load on the storage subsystem.
- *Backups* — HDD DAS/SAN. Backups are created periodically and rarely used. For their storage, the volume is more important than the performance. However, the backup speed may decrease if there are many small uploaded files. In this case, place the backup folder on a high-performance drive.
- *Temporary folder* — SSD DAS/SAN. The temporary file storage and processing load may increase due to various factors, such as many active users and transactions, users uploading many files, etc.

## Change Log

| Date | Version | Changes |
| --- | --- | --- |
| 07.04.2023 | 1.0 | Original version. |

================================================
FILE: 395. Version 4/398. Training/1109-lesson_1_intro.md
================================================
---
title: Lesson 1 &mdash; Getting Started
kbId: 1109
---

# Lesson 1 &mdash; Getting Started

## Introduction

In this lesson, you will learn basic **CMW Platform** concepts and how to log in and configure your account.

To get started, you will need access to the **CMW Platform**. If your organization is a CMW Lab customer, you can get the URL of a new **CMW Platform** instance from your system administrator. If you want to get acquainted with the **CMW Platform**, submit the [inquiry form on our website](https://www.cmwlab.com/company/contact-us/).

The **CMW Platform** is a web-based business process management system. You can use it from a web browser or the CMW Mobile app.

The following web browsers are supported: Google Chrome, Firefox, Microsoft Edge, and Safari. We recommend updating your browser to the latest version to ensure all **CMW Platform** features are available.

Estimated time to complete: 10 min

Prerequisite: get access to the **CMW Platform** instance

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Definitions

**Product** — the **CMW Platform** software.

**Instance** — a deployed **CMW Platform** website.

**System** — a complete hardware and software environment powered by the **CMW Platform**.

## Log in to the CMW Platform

**1.** Launch your browser and enter the URL of the **CMW Platform** (deployed on your company's premises or in the **CMW Lab** cloud if you requested a demo). 

**2.** The login page should appear.

**3.** Enter the username and password provided by your system administrator or the **CMW Lab** support.

**4.** Click **Log in**.

_![CMW Platform login page](https://kb.cmwlab.com/assets/cmw_platform_lesson1_1.png)_

## Configure Your Account

Use **My account** page to view or edit your personal information and change your password.

Note

Some or all actions on **My account** page may be unavailable depending on your permissions (granted by the system administrator).

**1.** Click the icon with your initials in the upper right corner of the screen.

**2.** Select **My account** in the dropdown.

![Navigating to My account](https://kb.cmwlab.com/assets/cmw_platform_lesson1_2.png)

Navigating to **My account** page

**3. My account** page appears.

**3.** To reset your password, click **Change password**.

**4.** To save your changes, click **Save**.

![My account — view and edit your account details or change your password](https://kb.cmwlab.com/assets/cmw_platform_lesson1_3.png)

*My account — view and edit your account details or change your password*

## Results

Congrats! You have learned how to log in to the system and configure your account.
Proceed to [Lesson 2 &mdash; My First Data Registry](https://kb.comindware.ru/article.php?id=1110) to create your first business application and data registry.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/1110-lesson_2_data_register.md
================================================
---
title: Lesson 2 &mdash; My First Data Registry
kbId: 1110
---

# Lesson 2 &mdash; My First Data Registry

## Introduction

In this lesson, you will create and configure an application, a record template and its attributes, a table with data filters, and a form. Then, you will create and fill the records with some data.

Estimated time to complete: 15 min

Prerequisite: complete [Lesson 1 &mdash; Getting Started](https://kb.comindware.ru/article.php?id=1109)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Definitions

- **Application** — a standalone business solution within the **CMW Platform**.
- **Record template** — a data registry in the **CMW Platform** (similar to a relational database table or an Excel sheet).
- **Record** — a data entry (consisting of **attributes**) related to a business object.
- **Attribute** — the simplest data element related to a business object (similar to a column in a relational DB or Excel): pick-up point (string), count of passengers (number), сar delivery time (date/time), car (link), etc.
- **Table** — a list displaying records in rows with attribute values in columns. You can configure table filters to display a subset of records.
- **Form** — a page with fields to display and enter the record data.

## Create Application

Business Requirement

Throughout the tutorial lessons, we will develop a corporate vehicle booking application.

We will implement the following vehicle booking process:

1. The *Initiator* submits a vehicle request.
2. The *Secretary* reviews and approves or rejects it.
3. If the request is approved:
   1. The *Garage manager*assigns a vehicle for the trip.
   2. The *Driver* completes the trip.
4. If the request is rejected, the *Initiator*receives the rejection notification.

Let's create an application to automate corporate vehicle booking.

**1.** Select **System navigation section** – **Applications** in the left navigation pane.

**2.** Click **Create**.

_![Creating an application](https://kb.cmwlab.com/assets/cmw_platform_lesson2_1.png)_

**3.** In the **New application** window, enter the application **Name** — *Vehicle**management*. The **System name** is generated automatically from the application **Name**. Change the system name if needed.

System Name and Display Name

- The System name is an entity identifier used in scripts, rules, formulas, and expressions. The system name can include English letters (A–Z, a–z), numbers (0–9), and underscores (\_). The system name must not start with a number.
- The Name   or Display name is used as a human-readable entity descriptor, can include any characters, and should be concise and self-explanatory.

**4.** Click **Save**.

_![Configuring a new application](https://kb.cmwlab.com/assets/cmw_platform_lesson2_2.png)_

**5.** In the application list, double-click your application to open its **Administration** page.

_![List of applications](https://kb.cmwlab.com/assets/cmw_platform_lesson2_3.png)_

## Create Record Template

Let's define the vehicle request data to store in a record template — the data registry.

**1.** Open the *Vehicle management* application **Administration** page and select **Templates**.

_![Navigating to the application Templates page](https://kb.cmwlab.com/assets/cmw_platform_lesson2_4.png)_

**2.** Go to the **Record templates** tab.

**3.** Click **Create**.

![Creating a record template ](https://kb.cmwlab.com/assets/cmw_platform_lesson2_5.png)

Creating a record template

**4.** In the **New template** window, enter the template **Name** — *Vehicle requests*.

**5.** Make sure the **Template type** is set to **Record template**.

**6.** Click **Create**.

![Configuring and saving a new record template](https://kb.cmwlab.com/assets/cmw_platform_lesson2_6.png)

Configuring a new record template

## Add Record Template Attributes

Let's add the vehicle request attributes.

**1.** Open the *Vehicle Requests* template page and go to the **Attributes** tab.

**2.** Click **Create**.

_![Adding an attribute](https://kb.cmwlab.com/assets/cmw_platform_lesson2_7.png)_

**3.** In the **New attribute** window, select **Text** as the **data type** and enter the attribute **Name** — *Pick-up point*. The **System name** is filled in automatically.

**4.** Click **Save**.

_![Configuring a new attribute](https://kb.cmwlab.com/assets/cmw_platform_lesson2_8.png)_

**5.** The same way as above, create the following attributes:

- *Car delivery time*
  - **Data type**: **Date & time**
- *Route*
  - **Data type**: **Text**
- *Passengers*
  - **Data type: Number**

Attribute Types

- **Text**— string value. Supported display formats:
  - Plain text — no formatting.
  - **Marked text** — basic formatting (bold, italic, lists).
  - **HTML text** — advanced HTML formatting.
  - **Email address**, **Custom mask** — the attribute value is formatted using a regular expression mask.
- Number— numeric value. You can select the number of digits to display after the decimal point:
  - **Do not parse** — display the value as entered.
  - **0** — display the value as an integer.
  - **1**–**6** — display the value with the specified number of decimal places.
- Date & time — date and time value. Several display formats are supported to show the date only or the date and time.
- Document — uploaded data files (DOCX, PDF, ZIP, etc.) Supported display formats: **Without preview**, **With preview**, **Digitally signed document**.
- Image — uploaded image files (PNG, JPG, etc.) Supported display formats: **Original**, **Greyscale**, **1-bit (black & white)**.

The CMW Platform also supports the following attribute types: **Account**, **Hyperlink**, **Barcode**, **Duration**, **Record**, **Boolean**, **Organizational Unit**, **Role**, and **List of Values**. We will learn to use some of them later.

You have created the minimum attribute set required to submit and process a vehicle request.

Note

Following the agile methodology, initially, we don't define all the attributes and create only the necessary minimum.

We aim to develop a functioning application and demonstrate it to the first users as soon as possible.

Then, based on the user feedback, we will add more attributes and improve the app.

## Create a Form

Let's create a form with the fields to enter and edit the vehicle request data.

**1.** On the *Vehicle requests* template page, go to the ***Forms*** tab.

Each record template contains a default form, and we'll customize it.

_![Opening the default form for editing](https://kb.cmwlab.com/assets/cmw_platform_lesson2_9.png)_

**2.** In the form list, double-click the *Vehicle requests - Main Form.* The form designer appears.

_![Form designer](https://kb.cmwlab.com/assets/cmw_platform_lesson2_10.png)_

Form Designer

There are four areas in the form designer:

1. Element pane — a list of elements that you can place on the form: attributes, forms, buttons, and [visual elements](VisualElements).
2. Form layout — the form editing and preview area. To place elements on the form, drag them to the layout from the element pane. To delete elements from the form, drag them outside of the layout.
3. Properties pane — allows you to view and configure the properties of the selected form element.
4. Buttons — Save,   Clear, Clone, Configure template   *‌*,  Relations *‌*.

**3.** The form has a default **New area** element.

**4.** Drag the *Car delivery time* attribute to the **New area**from the element pane.

![Dragging an attribute onto the form](https://kb.cmwlab.com/assets/cmw_platform_lesson2_11.png)

Dragging an attribute to the form

**5.** Drag the attributes *Pick-up point*, *Route*, and *Passengers* to the **New area**.

Business Requirement

In the *Car delivery time* field, the Initiator should enter the date and time. The default display format for this attribute shows only the date. We will change the display format to include the time.

**6.** In the element pane, click the **Edit***‌* icon next to the *Car delivery time* attribute.

_![Editing an attribute using the form designer](https://kb.cmwlab.com/assets/cmw_platform_lesson2_12.png)_

**7.** In the attribute properties window, choose a **display format** that includes time, e. g. **Sep 4. 1986 07:30***,* and click **Save**.

_![Editing the attribute properties](https://kb.cmwlab.com/assets/cmw_platform_lesson2_13.png)_

**8.** Select the *Car delivery time* field on the form. In the ***Access*** dropdown on the *Field properties* panel, select ***Require entry***.

_![Changing the form field access mode](https://kb.cmwlab.com/assets/cmw_platform_lesson2_14.png)_

**9.** Set the ***Require entry*** access mode for the *Pick-up point* field.

Visual Elements on the Form

Use the following elements to make the form more user-friendly:

- ***Area*** — visually groups the fields, has a title, and can contain buttons. The form must have at least one area.
- ***Static text*** — displays a read-only text.
- ***Tabs*** — distribute the fields into user-selectable tabs.
- ***Columns*** — arranges fields in several columns.

**10.** Drag the ***Columns*** element to the form from the element pane.

**11.** Drag the *Car delivery time* and *Pick-up point* attributes into the left and right columns.

![Placing attributes into the columns](https://kb.cmwlab.com/assets/cmw_platform_lesson2_15.png)

Placing fields into the columns

**12.** Rename the default **New area**: select it, and in the **Area properties** panel, enter the new **Display name** — *Vehicle request form*.

**13.** To save the form, click **Save**.

_![Renaming an area and saving the form](https://kb.cmwlab.com/assets/cmw_platform_lesson2_16.png)_

The form designer provides many functions. Try to experiment with the elements and settings in the form designer.

## Test: Enter and Edit the Data

We have created the vehicle request form. Let’s test it as an *Initiator*.

**1.** Click ***Configure template*** *‌*.

_![Navigating to the record template settings](https://kb.cmwlab.com/assets/cmw_platform_lesson2_17.png)_

**2.**Click ***Navigate to instances*** to open the record list.

_![Navigating to the record template instances](https://kb.cmwlab.com/assets/cmw_platform_lesson2_18.png)_

**3.** Click ***Create*** to fill in a new vehicle request.

_![Creating a new record](https://kb.cmwlab.com/assets/cmw_platform_lesson2_19.png)_

**4.** The vehicle request form appears. Fill in all fields and click ***Save***.

_![Filling out and saving the vehicle request form](https://kb.cmwlab.com/assets/cmw_platform_lesson2_20.png)_

**5.** Click the *Vehicle requests* link above the form to return to the request list.

![Navigating to the record list from the record template form](https://kb.cmwlab.com/assets/cmw_platform_lesson2_21.png)

Navigating to the record list from the record form

**6.** Create several vehicle requests as you did above. The records will appear in the list.

**7.** Go to the vehicle request list and double-click a request to open and edit it.

_![Opening an entry by double-clicking on it](https://kb.cmwlab.com/assets/cmw_platform_lesson2_22.png)_

## Finalize the Form: Add the Secretary's Approval Status

The Secretary must review the created request, but our record template lacks an attribute for the approval result. Let's add this attribute.

**1.**To open the record template settings, click the **My settings** *‌* icon above the **All records** table and select **Configure template**.

_![Navigating to the record template settings from the table](https://kb.cmwlab.com/assets/cmw_platform_lesson2_23.png)_

**2.** Go to the **Attributes** tab and click **Create**.

_![Adding an attribute](https://kb.cmwlab.com/assets/cmw_platform_lesson2_7.png)_

**3.** In the **New attribute** window, enter the attribute **Name** —  *Approved*, set **Boolean** **data type**, and click **Save**.

_![Configuring a new boolean attribute](https://kb.cmwlab.com/assets/img_653f7f7a4173a.png)_

## Configure a Table

Each template has the default **All records** table that shows system attributes: **ID**, **Creator**, **Creation date**, **In archive**, **Modified date**. The default table is not informative for the end-user. Let's customize the list of vehicle requests displayed in the default table.

**1.** Go to the **Tables** tab of the *Vehicle requests* template and double-click the **All records** table.

_![Navigating to the table designer](https://kb.cmwlab.com/assets/cmw_platform_lesson2_25.png)_

**2.** The table designer appears with a list of attributes. Drag and drop the attributes to and from the table layout to configure and reorder the table columns.

**3.** Remove the columns that the end-user does not need. Select the **ID** attribute in the table layout and drag it outside of the layout. In the same way, remove the **Creation Date** and **In archive** columns from the table. Leave the **Creator** and **Modified date** columns in the table.

_![Removing the unnecessary attributes from the table](https://kb.cmwlab.com/assets/img_653f8c6de0345.png)_

**4.** Add the relevant columns to the table. The attribute order in the table designer defines the column order: the top item appears as the leftmost column in the table.

**5.** Drag the following attributes from the element pane to the table layout: *Car delivery time*, *Pick-up point*, *Route*, and *Passengers*.

**6.** Click **Save** to save the default table configuration.

**7.** Click **Configure template** to return to the template **Properties**.

_![Adding new attributes and saving the table](https://kb.cmwlab.com/assets/cmw_platform_lesson2_27.png)_

**8.** On the template **Properties** tab, click **Navigate to instances** to open the vehicle requests list that you configured.

_![The customized table of records](https://kb.cmwlab.com/assets/cmw_platform_lesson2_28.png)_

## Search and Filter Records in the Table

Let’s configure the table to filter and reorder the records and then configure grouping and summarization.

### Configure Sorting, Filtering, and Grouping for the Current User

Note

This section provides instructions on configuring the table display settings **for the current user**. These settings are stored individually for each user.
In addition, using the table designer, you can configure the column display options that will be used **for all users by default**. See [Configure Sorting, Grouping, Summarizing, and Filtering for All Users](#mcetoc_1he08sd700).

#### Sort Records

Let's sort the vehicle requests by car delivery time.

**1.** Click the *Car delivery time* column heading to sort the data by this column: ascending, descending, or default. The sorting order is indicated by a down arrow (descending), up arrow (ascending), or no arrow (default) in the column heading.

_![Changing the record sorting order in the table](https://kb.cmwlab.com/assets/cmw_platform_lesson2_29.png)_

#### Filter Records

To display records that contain a specific value, you can use a filter: ***Equal to*** or ***Substring of***.

Let's filter the vehicle requests by the route.

**1.** Click the filter *‌* icon in the *Route* column.

**2.** In the dropdown, check **Filter data** and select **Substring of**.

**3.** Enter the desired value in the **Enter text here** field.

**4.** Click **Apply**.

_![Applying a filter to a table column](https://kb.cmwlab.com/assets/cmw_platform_lesson2_30.png)_

**5.** The records matching your filter will appear in the table.

**6.** To reset the record filter, click the filter *‌* icon in the *Route* column, uncheck **Filter data** in the dropdown, and click **Apply**.

_![Resetting a table column filter](https://kb.cmwlab.com/assets/cmw_platform_lesson2_31.png)_

#### Group Records

Let's group vehicle requests with the same route.

**1.** Click the filter *‌* icon in the *Route* column.

**2.** Select the **Group by this column** checkbox in the dropdown.

**2.** click **Apply**.

_![Grouping records by a column value](https://kb.cmwlab.com/assets/cmw_platform_lesson2_32.png)_

#### Hide Column

Let's hide the **Modified date**column.

**1.** Click the *‌* icon above the table

**2.** Select **Customize display** in the dropdown.

_![Navigating to the table display customization page](https://kb.cmwlab.com/assets/cmw_platform_lesson2_33.png)_

**3.** The table customization page appears.

**4.** Clear the *Modified date* checkbox to hide this column from the table. If needed, click **Reset** to restore the original table display configuration.

**5.** Click **Save**.

_![Table display configuration page](https://kb.cmwlab.com/assets/cmw_platform_lesson2_34.png)_

### Configure Sorting, Grouping, Summarizing, and Filtering for All Users

Note

This section provides instructions on configuring the **default** **table display settings for all users**.

In addition, each user can individually customize the table display. See [Configure Sorting, Filtering, and Grouping for the Current User](#mcetoc_1he08u4l11).

**1.** Click the *‌* icon and select **Edit table** from the dropdown. The table designer appears.

_![Navigating to the table designer](https://kb.cmwlab.com/assets/cmw_platform_lesson2_35.png)_

**2.** Go to the **Advanced** tab in the **Table properties** panel.

**3.** Drag and drop attributes from the table layout into the **Sorting**, **Grouping**, and **Filter** areas.

**4.** Configure the table data sorting, grouping, and filtering for all users.

**5.** Click **Save**.

![Configuring the default sorting, grouping, and filtering for a table using the table designer](https://kb.cmwlab.com/assets/cmw_platform_lesson2_36.png)

Configuring the default table sorting, grouping, and filtering using the table designer

## Results

Congrats! You have created your first data registry (record template), designed a form, learned how to fill it out, and configured a table with records.

Proceed to [Lesson 3 &mdash; My First Business Process](https://kb.comindware.ru/article.php?id=2147)) to learn how to design and run a business process.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/2147-lesson_3_business.md
================================================
---
title: Lesson 3 &mdash; My First Business Process
kbId: 2147
---

# Lesson 3 &mdash; My First Business Process

## Introduction

In this lesson, we'll improve the application from [Lesson 2](https://kb.cmwlab.com/article.php?id=1110) to implement the following business logic:

- The *Initiator* submits a vehicle request.
- The request goes to the *Secretary* for review.
- The *Secretary* either approves or rejects the request.
- The approved request goes to the *Garage manager* for review.
- The *Garage manager*either accepts or rejects the request depending on the vehicle availability in the *Garage*.
- If the *Garage manager* accepts the request, the *Initiator* is notified, and the *Driver* completes the trip.
- If the *Secretary* or *Garage manager*rejects the request*,* the *Initiator* is notified, and the process terminates.

Estimated time to complete: 20 min

Prerequisite: complete [Lesson 2 &mdash; My First Data Registry](https://kb.comindware.ru/article.php?id=1110)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Definitions

### Executable Business Process

An **executable business process** is a process that is automated using a process engine or a business process management system (BPMS), such as the **CMW Platform**.

The executable business process determines who should do what and in what order. It automates task transfer between employees and departments. Thus, the system controls the entire process from the request submission to closing. In the **CMW Platform**, processes can communicate with each other and external systems such as email servers and web services. The executable business process replaces workflows based on e-mail and Excel, streamlining and automating them. On top of that, the **CMP Platform** automatically generates documents from templates.

You can regard the executable business process as an “interactive regulation.” A traditional regulatory document is an instruction for employees to refer to and follow at each process step. With an executable business process, the system orchestrates the employees and systems. A BPMN diagram is loaded into the BPMS that executes it, dispatching tasks to employees and calling the information system functions.

The executable business process allows you to increase work efficiency:

- The tasks are assigned to employees instantly, without errors, together with all the relevant data.
- The process is guaranteed to be carried out according to the approved diagram, and no additional control is needed.
- The process metrics are automatically measured and displayed on the manager's screen.

The executable business process has some similarities with a document flow, yet it gives business advantages:

- The data is stored in a structured, semantic, and searchable form rather than in Excel, Word, or PDF documents.
- The process route can be designed granularly.

### Process Template

In the **CMW Platform**, you can set up an **executable business process**using a **process template**.

A **process template** stores a process diagram, the process instances, and properties that define how each process instance is executed. Each process template is linked to a record template that stores records for process instances.

## Create Process Template

Let's create a vehicle booking process template.

**1.**In the left navigation pane, select **System navigation section** — **Templates**.

**2.** Go to the **Process templates** tab.

**3.** Click  **Create**.

**4.** Enter the template **Name** — *Ordering a corporate vehicle*.

**5.** Select the **Application** — *Vehicle management*.

**6.** Select **Associate with an existing template**.

**7.**Select **Linked record** — *Vehicle requests*.

**8.** Click **Create**.

_![Creating a new process template](https://kb.cmwlab.com/assets/img_6540d2d16f3da.png)_

## Draw Process Diagram

Using the business process diagram designer, you can draw a BPMN diagram simply by dragging and dropping the elements.

BPMN 2.0 Notation

In the **CMW Platform**, you draw the process diagrams using BPMN 2.0 notation.

BPMN notation is simple and widely adopted by businesses. Thanks to straightforward BPMN interpretation, the business stakeholders, analysts, and IT specialists get a common understanding of the diagram.

**1.** On the process template page, go to the **Diagram** tab.

**2.** The business process diagram designer appears.

_![Business process diagram designer](https://kb.cmwlab.com/assets/cmw_platform_lesson3_2.png)_

Business Process Diagram Designer

The business process diagram designer consists of three areas:

1. **Elements pane** — contains the elements to drag and drop on the diagram:

- **Actions:**
  - **User task**
  - **Script task**
  - **Service task**
  - **Process call**
  - **Embedded subprocess**
- **Events:**
  - **Start event**
  - **Intermediate event**
  - **End event**
- **Operators:**
  - **Exclusive gateway**
  - **Parallel gateway**
- **Common:**
  - **Swimlane**
  - **Sequence flow**
  - **Text annotation**

3. **Business process diagram**.
4. **Buttons** — **Select version**, **Clear**, **Publish**, **Validate**, **Export**.

**3.** Drag three **swimlanes** to the process diagram from the element pane.

Swimlane

A **swimlane** or **lane** in BPMN is a box that represents the business process participants. The lanes can be configured arbitrarily at the discretion of the process designer. Typically, they represent a customer, department, position, role, or team. For example, in our process, the *Initiator* is a role (the *Initiator* can belong to any department), the *Garage* is a department, and the *Secretary* is a position.

_![Dragging the swimlanes to the diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson3_3.png)_

**4.** Rename the **swimlanes** as follows: *Initiator*, *Secretary*, *Garage*. To do this, select each **swimlane** by clicking its name and then click **Properties** *‌* in the element menu.

_![Navigating to swimlane properties](https://kb.cmwlab.com/assets/cmw_platform_lesson3_4.png)_

**5.** In the **Lane properties** window, enter a new **Name** and click **Save**.

_![Renaming a swimlane](https://kb.cmwlab.com/assets/img_6540a34665f00.png)_

**6.** Remove the **end event**. To do this, select it and click **Delete** *‌* in the element menu.

_![Deleting an element from the process diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson3_6.png)_

**7.** Drag the **user task** to the *Secretary* lane from the element pane.

User Task

The **user task** is executed by a person. When the process moves to this element, the task is automatically assigned to one or several [**performers**](#mcetoc_1gt5k0mqr0).

**8.** Rename the user task to *Approve request*. To do this, double-click the task name and enter the new name.

**9.** Attach the **sequence flow** from the start event to the *Approve request*task.

**10.** Drag the **exclusive gateway** to the diagram and connect it with the sequence flow to the *Approve request* task.

Exclusive Gateway

The **exclusive gateway** defines alternative sequence flows, of which the process can follow only one.

For each outgoing flow from the gateway, a Boolean condition is specified. The process follows the first flow for which the condition returns `true`. Additionally, you can select the **default flow**, which the process follows if none of the other conditions are met.

**11.** Attach two **sequence flows** to the **exclusive gateway** exit.

**12.** Rename the **exclusive gateway** to  *“**Approved?”* To do this, double-click the gateway name and enter the new name, or select the gateway, click **Properties** *‌* in the element menu, and enter the new name in the **Exclusive gateway properties** window.

_![Navigating to gateway properties](https://kb.cmwlab.com/assets/cmw_platform_lesson3_7.png)_

Business Requirement

If the *Secretary* rejects the request, the *Initiator* receives a notification about this, and the process ends. If the *Secretary* approves the request, the *Garage manager* processes it further. Let's draw this on the process diagram.

**13.** Add two **user tasks** after the *“Approved?”* gateway: *Rejected* on the *Initiator* lane and *Accept request* on the *Garage* lane.

**14.** Select the gateway and click **Properties** *‌* in the element menu. The ***Exclusive gateway properties**window appears.*

**15.** In the **Advanced** tab, enter the **Name** for each outgoing flow: *Yes* and *No*, by double-clicking the appropriate fields. Click **Save**.

_![Renaming the sequence flows in the exclusive gateway properties](https://kb.cmwlab.com/assets/cmw_platform_lesson3_8.png)_

**16.** Add the **end event** after the *Rejected* task.

**17.** Rename the **end event** to *Rejected*.

Events

You can interpret **Events** in BPMN as process stages — start, milestones, and completion. The process can have only one start event. Yet, it can have several end events for different process outcomes.

_![Intermediate process diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson3_9.png)_

Business Requirement

When the request is accepted, the *Garage manager* checks if a car is available. If there is no car, the request is returned to the *Secretary*.

**18.** Add the **exclusive gateway** after the *Accept request*task.

**19**. Add the **sequence flow** from the gateway to the *Approve request* task.

**20.** Rename the gateway to *“Is there an available car?”*

![The “Is there an available car?” gateway](https://kb.cmwlab.com/assets/img_65576c5f8e780.png)

The *“Is there an available car?”*gateway

Business Requirement

If a car is available, the *Initiator* receives the *Car assigned*notification, and the *Garage* commences the trip.

**21.** Add the **parallel gateway** after the *“Is there an available car?”* gateway.

Parallel Gateway

The **parallel gateway** can split the process into multiple flows that run simultaneously.

**22.** Add two **user tasks** after the parallel gateway: *Car assigned* for the *Initiator*and *Complete the trip*for the *Garage*.

**23.** Name the outgoing flows from the *“Is there an available car?” gateway as Yes* and *No*.

**24** Add another **parallel gateway**and connect it to the *Car assigned* and *Complete the trip* tasks.

**25.** Add the **end event** and rename it to *Success*.

The resulting diagram should look as shown below:

_![The vehicle booking process diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson3_11.png)_

Vehicle Booking Process Diagram

Let's summarize the flow of the vehicle booking process diagram.

1. The *Initiator* submits a request.
2. The *Secretary* reviews it:
   1. If the *Secretary* approves the request, Step 4 is executed.
   2. If the *Secretary* rejects the request, Step 3 is executed.
3. The *Initiator* receives notification that their request has been rejected. The vehicle booking process ends as rejected.
4. The *Garage manager* accepts the request:
   1. If a car is available, the *Garage manager* sends the request for execution to the *Driver* — Step 5 is executed.
   2. If no car is available, the request is returned to the *Secretary* — Step 2 is executed.
5. The *Initiator* receives notification that the car has been allocated, and the *Driver* starts the trip.
6. The process ends successfully.
## Configure User Task Forms

### Initiator Start Form

Let's create the **start form**, which will be shown to the *Initiator* when the process starts.

**1.** Select **Start event** on the diagram and click **Start form** *‌* in the element menu.

_![Navigating to the start form settings](https://kb.cmwlab.com/assets/cmw_platform_lesson3_12.png)_

**2.** The form designer will appear.

**3.** To reuse the existing *Vehicle requests - Main Form*, drag it to the form layout from the element pane. Click **Save**. Return to the process diagram by clicking **Back**in the browser.

_![Configuring the start form](https://kb.cmwlab.com/assets/img_6540fc40d0695.png)_

### Secretary Task Form — Approve Request

Let's configure the form for the *Secretary* task.

**1.** Select the *Approve request*task and click **Form***‌* in the element menu.

_![Navigating to the task form settings](https://kb.cmwlab.com/assets/cmw_platform_lesson3_14.png)_

**2.** In the form designer, expand the *Vehicle requests* item in the element pane, and drag the *Vehicle requests - Main Form* to the form layout.

Business Requirement

The Secretary should not edit the *Initiator's* vehicle request form fields, so let's change the access to the subform.

**3.** Select the *Vehicle requests - Main Form*subform and set **Access**to **Read only** in the **Subform properties** panel.

**4.** Drag a new **area** to the form layout under the *Vehicle requests - Main Form* and set its **display name** to *Approval* using the **Area properties** panel.

**5.** Drag the *Approved* attribute to the *Approval* area from the element pane.

**6.** Save the form and return to the process diagram by clicking **Back**in the browser.

_![Editing and saving the task form](https://kb.cmwlab.com/assets/img_6540ff3406c82.png)_

### Garage Manager Task Form — Accept request

Let's configure the form for the *Garage manager* task.

**1.** Select the *Accept request* task and click **Form** *‌* in the element menu. The form designer appears.

**2.** Expand the *Vehicle requests* item in the element pane, and drag the *Vehicle requests - Main Form* to the form layout.

**3.** In the **Subform properties** panel, set **Access** to **Read only**to prevent the *Garage manager* from editing the request*.*

Business Requirement

The *Garage manager* should accept or decline the request depending on the car availability in the garage. We will add an attribute for this.

The **CMW Platform** allows you to add attributes without leaving the form or table designer.

**4.** Click the **Add attribute** *‌* icon on the *Vehicle request* item to add an attribute to this record template.

_![Adding an attribute using the form designer](https://kb.cmwlab.com/assets/cmw_platform_lesson3_16.png)_

**5.** In the **New attribute** window, set **Boolean** as the **data type** and enter the **name** — *Accepted*.

**6.** Click **Save**.

_![Creating and saving a new attribute on the fly](https://kb.cmwlab.com/assets/cmw_platform_lesson3_17.png)_

**7.** Drag a new **area** to the form layout and rename it to *Acceptance* using the **Area properties** panel.

**8.** Drag the created *Accepted* attribute to the *Acceptance* area.

**9.** Select the *Accepted* field, and in the **Field properties** panel, select **Display as** **Radio button**.

**10.** Click **Save**and return to the process diagram using the browser's **Back**button.

![Changing the display mode of the boolean attribute on the form](https://kb.cmwlab.com/assets/cmw_platform_lesson3_18.png)

Changing the display mode of the Boolean attribute on the form

### Initiator Task Form — Request Rejected

Business Requirement

The *Initiator* should be informed about the rejected request. The user task form will contain only the text “Your request was rejected” and the read-only request data.

**1.** On the process diagram, select the *Rejected* task and click **Form** *‌* in the element menu. The form designer appears.

**2.** Drag a new **area** to the form layout and rename it to *Your request was rejected* using the **Area properties** panel.

**3.** Expand the *Vehicle requests* item in the element pane, and drag the *Vehicle requests - Main Form* to the form layout below the *Your request was rejected* area.

**4.** In the **Subform properties** panel, set the **Access** to **Read only***.*

**5.** Save the form and return to the process diagram.

_![Changing the subform access mode](https://kb.cmwlab.com/assets/img_65423013ca0a1.png)_

### Initiator Task Form — Car Assigned

**1.** On the process diagram, select the *Car assigned* task and click **Form** *‌* in the element menu.

**2.** Configure the *Car assigned* task form — add a new **area** and the *Vehicle requests - Main Form* with **Read only** **access**. Save the form and return to the process diagram.

![Setting up "Car assigned" task form](https://kb.cmwlab.com/assets/cmw_platform_lesson3_20.png)

Configuring the Car assigned task form

### Driver Task Form — Complete the Trip

**1.**On the process diagram, select the *Car assigned* task and click **Form** *‌* in the element menu.

**2.**Configure the *Complete the trip* task form — add the *Complete the trip* **area**and the *Vehicle requests - Main Form* subform below it. Set the subform **access**mode to **Read only**. Save the form and return to the process diagram.

## Configure Exclusive Gateway Outgoing Flows

Let's configure the outgoing sequence flows from the gateways: “*Approved?”* and *“Is there an available car?”*

### “Approved?” Gateway

Business Requirement

The flow that the process follows after the *“Approved?”* gateway to the *Accept request*task is defined by the *Approved*attribute value set by the *Secretary*while reviewing the request.

To control the process flow, we'll define the condition for the *Accept request* flow based on the *Approved* attribute value.

**1.** Select the *“Approved?”* gateway and click **Properties** *‌* in the element menu.

_![Navigating to the gateway properties](https://kb.cmwlab.com/assets/cmw_platform_lesson3_21.png)_

**2.** In the **Exclusive gateway properties** window, go to the **Advanced** tab and check the **Default flow** box next to the *Rejected* task flow.

Exclusive Gateway Default Flow

From an **exclusive gateway** the process follows the **default flow** if none of the conditions for the other flows are met (the condition returns `false`).

_![Setting up the default flow](https://kb.cmwlab.com/assets/cmw_platform_lesson3_22.png)_

**3.** On the **Advanced** tab, click the **Condition** column next to the *Accept request* flow. The compact expression editor appears.

_![Compact expression editor](https://kb.cmwlab.com/assets/cmw_platform_lesson3_23.png)_

**4.** Enter `$` and double-click the *Approved* attribute system name in the dropdown to enter it in the formula.

Referencing the Attributes in Formulas

In the formulas, the `$` symbol followed by an attribute system name denotes a reference to attributes of the current object.

So the formula `$Approved` returns the *Approved* attribute value: `false` or `true`.

**5.** Click the green *‌* button.

**6.** Click **Save**.

_![Entering the condition for a sequence flow](https://kb.cmwlab.com/assets/cmw_platform_lesson3_24.png)_

### “Is there an available car?” Gateway

Business Requirement

The process should go from the *“Is there an available car?”* gateway to the parallel gateway if the *Garage manager* sets the Boolean attribute *Accepted* to `true`.

**1.** Select the gateway *“Is there an available car?” and* click **Properties** *‌* in the element menu.

**2.** Go to the **Advanced** tab.

**3.** Enter an expression for the "Yes" flow (`$Accepted`). Click the green check button.

**4.** Set the default flow next to the flow that goes to the task "Approve request".

**5.** Click **Save**.

![Setting up and saving the "Is there an available car?" gateway properties](https://kb.cmwlab.com/assets/cmw_platform_lesson3_25.png)

Setting up and saving the “Is there an available car?” gateway properties

## Configure User Task Performers

Let’s specify performers for the user tasks.

### Approve Request, Accept Request, and Complete the Trip Tasks

**1.** Select the *Approve request* user task and click **Properties** *‌* in the element menu.

_![Navigating to the task's properties](https://kb.cmwlab.com/assets/cmw_platform_lesson3_26.png)_

**2.** On the **Advanced** tab, select an employee from the **Performers** dropdown.

**3.** Enter the **task title** — *Ordering a corporate vehicle - Approve request*.

**4.** Click  **Save**.

![Changing the task title and performer](https://kb.cmwlab.com/assets/img_65576eaf9f89a.png)

Configuring the Approve request task title and performer

**5.** Similarly, specify the performers and **task titles** for the tasks: *Accept request* and *Complete the trip*. At this point, you may use the same performer for all these tasks.

### Rejected and Car Assigned Tasks

For the *Rejected* and *Car assigned*tasks, the performer should be the *Initiator*, the person who created the request. Let's calculate the *Initiator*.

**1.** Select the *Rejected* user task and click **Properties** *‌* in the element menu.

**2.** On the **Advanced** tab, select **Attribute** in the right dropdown of the **Performers** field.

**3.** In the **Performers** field, select the *Creator* attribute.

Creator System Attribute

The system attribute **Creator** points to the user who initiated the business process instance.

**4.** Enter the **task title** — *Ordering a corporate vehicle - Rejected*.

**5.** Click  **Save**.

_![Configuring the Rejected task title and selecting the record creator as the task performer](https://kb.cmwlab.com/assets/cmw_platform_lesson3_28.png)_

**6.** Similarly to the above, set the *Car assigned***task title** and **performer**.

## Validate and Publish the Process Diagram

You have configured the business process template. To execute the process, you need to publish the process diagram. You should publish the business process diagram whenever you change it.

Before publishing, validate the diagram to make sure the expressions are correct and the diagram follows the BPMN notation.

**1.** Click **Validate** in the process diagram designer.

- If any errors are found, the elements with the errors are highlighted in red. Click the exclamation mark next to a highlighted element to see the error messages.
- If the diagram has no errors, the “OK” message appears, and you can publish the diagram.

**2.** Click **Publish**.

_![Validating and publishing the process diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson3_29.png)_

## Test the Business Process and My Tasks

You have configured and published the business process. Now, test it as an end-user.

**1.** Go to the **Properties** tab of the process template.

**2.** Click **Navigate to instances**.

_![Navigating to the process instances](https://kb.cmwlab.com/assets/cmw_platform_lesson3_30.png)_

**3.** In the **All records** list, click **Create**. The configured **start form** should appear in the **New record** window.

**4.** Fill out the form and click **Create**.

_![Creating a new vehicle request](https://kb.cmwlab.com/assets/cmw_platform_lesson3_31.png)_

**5.** A new business process instance appears in the list.

**6.** To perform the *Approve request* task (where the performer is the current user), go to **My tasks** page using the left navigation pane.

**7.** A list of active tasks assigned to you appears.

**8.** To open the task form, click the link with the task title.

_![The active task list for the current user](https://kb.cmwlab.com/assets/cmw_platform_lesson3_32.png)_

**9.** In the vehicle request approval form that appears, check *Approved*and click **Complete task**.

_![Approving the request and completing the task](https://kb.cmwlab.com/assets/cmw_platform_lesson3_33.png)_

**10.** Go to **My tasks**. You should see the *Ordering a corporate vehicle - Accept request* task in the list.

**11.** Set the *Accepted* field to *No* and click **Complete task**.

_![Rejecting the request and returning it to the Secretary](https://kb.cmwlab.com/assets/cmw_platform_lesson3_34.png)_

**12.** Return to **My tasks**. You should see the *Ordering a corporate vehicle - Approve request*in the list.

**14.** Open the task and uncheck the *Approved* box.

**15.** Click **Complete task**.

**16.** Go to **My tasks**. You should see the *Ordering a corporate vehicle - Rejected* task in the list. Open it, and click **Complete task**.

## Results

Congrats! You have created your first business process, configured its task forms, and tested the process tasks initiation and execution.

Proceed to [Lesson 4 &mdash; Monitoring and analytics](https://kb.comindware.ru/article.php?id=2153) to learn how to track the history of a running process and create dashboards with statistical charts for a certain period.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/2153-lesson_4_monitoring.md
================================================
---
title: Lesson 4 &mdash; Monitoring and analytics
kbId: 2153
---

# Lesson 4 &mdash; Monitoring and analytics

## Introduction

In this lesson, you will learn how to view process execution history and create dashboards with statistical charts for a specific period.

Estimated time to complete: 10 min

Precondition: complete [Lesson 3 &mdash; My First Business Process](https://kb.comindware.ru/article.php?id=2147)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Definitions

### Process Instance History

The **CMW Platform**allows you to inspect the status and execution path of the running and completed business process instances. The following process history information is available:

- Current process stage — token positions on the process diagram.
- Process execution path.
- Event chain for each process diagram element.
- Information about each step (task performer, due date, etc.)
- Errors that occurred while executing the process.

### Process Tokens

**Token** is a BPMN concept: it refers to the current process execution point that moves along the process diagram. A business process can have several tokens, each following a separate path.

## Inspect the Business Process Execution

Let's look at the history of a vehicle booking process instance.

**1.** Go to the template list and open the *Ordering a corporate vehicle* process template by double-clicking it.

**2.** Open the process instance list by clicking **Navigate to instances** on the **Properties** tab.

**3.** Select a running process instance by double-clicking its row or clicking its **ID** link.

_![List of process instances](https://kb.cmwlab.com/assets/cmw_platform_lesson4_1.png)_

**4.** The process history view appears with the active diagram element highlighted in green.

Process History View

The process history view shows the process instance diagram and provides controls to inspect and manipulate the process flow.

The **buttons** above the diagram control the process instance:

- Stop process **—** remove all tokens from the process instance and set the process status to **Canceled**. This button appears if there is at least one token on the process diagram and no diagram element is selected.
- **Archive** — archive the process instance. Archived instances are not shown in the process instance list (unless it is configured to **Show archived records**.)
- **Create new token** — spawn a token on the selected diagram element. This button appears when you select a diagram element.
- **Change log** — show the change log tab.

The **Information** pane on the right of the process history view displays the following tabs:

**Properties** — information about the process instance:

- **Status**
  - **Active**— there is at least one token on the process elements.
  - **Inactive** — there are no tokens on the process elements.
  - **Completed** — the process ended as expected and has no tokens.
  - **Canceled** — the process has been stopped by removing all tokens.
- **Created on** — the process instance creation date and time.
- **Creator** — the account that created the process instance. Click the link to open the account details.
- **Process template** — process template name. Click the link to open the process diagram designer.
- **Record** — the ID of the record linked to the process instance. Click the link to open the record form.
- **Record template** — the linked record template name. Click the link to open the list of records.
- **Version** — the version number of the process diagram used to execute this process instance.

Tokens — a list of process elements with tokens. When you select an element, the **Actions** panel appears with the following buttons:

- **Go to** *‌* the user task form or subprocess diagram. You can also double-click a user task or subprocess on the diagram.
- **Restart token** *‌*  on the element.
- **Delete token** *‌*  from the element.

Change log — a list of events that occurred during the process execution. The Change log tab displays detailed information about all process tokens and steps:

- Token creation date and time
- Initiator account — the user who created the token
- Start date and time
- Completion date and time
- Assignees — the performers specified in the task properties
- Actual performer — the user who completed the step
- Event chain — click an icon next to an item in the **Change log** to view the chain of events for this item.

_![Viewing the history of a running business process instance](https://kb.cmwlab.com/assets/cmw_platform_lesson4_2.png)_

**6.** On the **Change log** tab in the **Information** pane, select the *Approve request* task.

**7.** The *Approve request* task is highlighted in yellow on the process diagram.

**8.** Click the  ![](https://kb.cmwlab.com/assets/img_6544ce95f2ce8.png)  icon next to the *Approve request* task to view its event chain.

**9.** Try to select other process elements to view their history.

_![Viewing the change log of a running process instance](https://kb.cmwlab.com/assets/img_6544c228301b8.png)_

## Configure a Page with a Pie Chart

Let's create a page with a chart displaying vehicle request percentage by month.

Pages

Pages in the **CMW Platform** are customizable dashboards to visualize and analyze the data. A page can contain charts, lists, metrics, and other widgets to visualize the business data.

Business Requirement

Before configuring and using the charts, generate relevant data: create and run several requests through the business process, filling in the *Car delivery time* with dates from different months.

**1.** Select **Applications i**n the left navigation pane to open the application list.

**2.** Double-click the *Vehicle management* application to open its **Administration** page.

_![Navigating to the application Administration page](https://kb.cmwlab.com/assets/cmw_platform_lesson4_4.png)_

**3.** Go to the **Navigation sections**.

_![Going to the navigation section list of an application](https://kb.cmwlab.com/assets/cmw_platform_lesson4_5.png)_

**4.**In the n**avigation section** list, click **Create**to create a new navigation section.

_![Creating a navigation section](https://kb.cmwlab.com/assets/img_6544d09815080.png)_

**5.**The navigation section designer appears.

**6.**In the **Navigation section properties** panel, enter the **Display name** —  *Summary*.

**7.** **Save** the *Summary* navigation section.

**8.** Refresh the page in your browser after saving the navigation section so that the next steps work correctly.

_![Configuring a navigation section](https://kb.cmwlab.com/assets/cmw_platform_lesson4_6.png)_

**9.** Go to the **New page** tab.

**10.** On the **Page properties** panel, specify the page **name** — *Requests statistics*.

**11.****Save** the page.

**12.** Refresh the page in the browser after saving the page so that the next steps work correctly.

**13.** On the element pane, click **Create chart** *‌* next to the **Charts** item.

_![Creating a new page in the navigation section](https://kb.cmwlab.com/assets/cmw_platform_lesson4_7.png)_ and adding a chart

**14.** Customize the chart using the **Widget properties** panel:

- **Name** —  *Requests by month.*
- **Display name** —  *Requests by month.*
- **Type** — **Pie chart**.
- **Template** — *Vehicle requests:*data source for the chart.
- **Categories** — *Car delivery time*: the **date & time** attribute used to group the records shown on the chart.
- **Date filter**
  - **Attribute** — *Car delivery time*: the **date & time** attribute used to filter records shown on the chart.
  - **Periods** — **Adjacent months**: the interval to group the records shown on the chart.
  - **Default period** — **Current month**: the period to group the records shown in the chart by default.

**15.** **Save** the chart.

**16.** Click **Refresh** on the chart layout to view the resulting chart.

_![Configuring a pie chart](https://kb.cmwlab.com/assets/img_65576ffd057ef.png)_

**17.**Click **Back** in your browser to return to the *Requests statistics* page.

**18.** Drag a new **area** to the page layout and rename it to *Reports*.

**19.** Drag the *Requests by month* chart from the element pane to the *Reports* area.

**20.** **Save** the page.

_![Adding a chart to the page](https://kb.cmwlab.com/assets/img_6557707941143.png)_

**21.** Go to the **Navigation** tab to return to the *Summary* navigation section.

**22.** Drag the *Requests statistics* page from the element pane to the navigation section layout.

**23.** **Save** the navigation section.

_![Adding a page to the navigation section](https://kb.cmwlab.com/assets/img_655770b139204.png)_

## Results

You learned how to view the process execution history and create pages with charts.

You will use the *Summary* navigation later in [Lesson 8 &mdash; Accounts](https://kb.comindware.ru/article.php?id=2157).

Proceed to [Lesson 5 &mdash; Data Structures](https://kb.comindware.ru/article.php?id=2154) to learn how to use the **record attribute** and create a reference data registry and a master data registry.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/2154-lesson_5_data.md
================================================
---
title: Lesson 5 &mdash; Data Structures
kbId: 2154
---

# Lesson 5 &mdash; Data Structures

## Introduction

In this lesson, you will learn how to use the entity relationship diagram designer to visually configure your application data model, create record templates (for reference data, master data, and transactional data), and establish relationships between them.

Estimated time to complete: 30 min

Prerequisite: complete [Lesson 2 &mdash; My First Data Registry](https://kb.comindware.ru/article.php?id=1110)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Definitions

### Entity Relationship Diagram — Application Data Model

In the **CMW Platform**, the application **data model** is visualized and designed using the **entity relationship (ER) diagram**. It shows the record templates (data registries), attributes, and their relationships with each other.

The **data model diagram** designer allows you to create and configure new record templates and attributes. This way, you can customize your business application while viewing its model as a whole.

## Create an ER Diagram

**1.** In the navigation pane on the left, select **Diagrams**. A list of diagrams of all applications appears.

Note

By default, the diagram list contains **class diagrams** and business **process diagrams**. A **class diagram** is generated automatically for each application. A **process diagram** is generated for each process template.

**2.** Click **Create** to add a new diagram.

**3.** In the **New diagram** window, configure the diagram:

- **Name:** *Data model - Vehicle management*
- **Type:** *Data model diagram*
- **Application:** *Vehicle management*

_![Creating a new data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_1.png)_

**4.** Click **Save**. The data model diagram designer appears.

Data Model Diagram Designer

The data model diagram designer consists of the following areas:

1. **Element pane** — contains the templates and elements you can add to the diagram.
2. **Diagram** — drag and drop the elements to the diagram from the element pane.
3. **Toolbar**
   - **Select version**— load an earlier saved version of the diagram.
   - **Create new version** — save the current diagram as a new version.
   - **Clone** — create a new diagram by copying the current one.
   - **Settings** — rename the diagram.
   - **Refresh data** — pull the up-to-date application data model to the diagram.
   - **Export**— export the diagram in SVG format.
   - **Show system names** — show **system names** instead of **display names** for templates and attributes in the diagram.
   - **Clean** — remove all elements from the diagram.

The diagram changes are saved automatically to the current diagram version.

_![Diagram designer](https://kb.cmwlab.com/assets/cmw_platform_lesson5_2.png)_

**5.** Drag and drop the *Vehicle requests* record template from the element pane to the diagram.

_![Adding a record template to the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_3.png)_

## Configure a Reference Data Registry

Business Requirement

We need a registry of vehicle types so that the *Initiator* can specify the requested car type.

First, we will create the *Vehicle types* record template to store the reference data. Then, we will configure a form and a table for the vehicle type records. Finally, we will fill in the vehicle types.

We will use the **data model diagram** designer to create and configure the record template.

### Create the Record Template — Vehicle Types

**1.** Drag the **New record type** from the element pane to the diagram.

_![Adding a new record template using the data model diagram designer](https://kb.cmwlab.com/assets/cmw_platform_lesson5_4.png)_

**2.** In the **New template** window, enter the template **Name**— *Vehicle types*, and click **Create**.

_![Configuring a new record template](https://kb.cmwlab.com/assets/cmw_platform_lesson5_5.png)_

### Set a Text Attribute as a Record Title

Business Requirement

By default, the record title is an **ID**. So, when selecting a vehicle type, users see its ID, which is not informative. We will allow the users to specify the vehicle type by name. For this, we will create a **text attribute** in the *Vehicle types* record template and set it as a record title. You should select a record title attribute in each template to improve the end-user experience.

Record-Title Attribute

A template record has a title displayed in the forms and tables. By default, it shows the record **ID** — a system alphanumeric identifier.

To show a relevant record title, use an attribute value: select the **Use as a record title** checkbox in the attribute properties.

You can use the following attribute types as the record title: **Account**, **Date & time**, **Duration**, **Text**, and **Number**.

You can only use one attribute as the record title for a template.

**1.** Select the *Vehicle types* record template in the diagram.

**2.** In the element menu, click **Add new attribute**.

_![Adding a new attribute using the data model diagram designer](https://kb.cmwlab.com/assets/cmw_platform_lesson5_6.png)_

**2.** In the **New attribute** window, specify the attribute ***Data type*** — **Text** and  **Name**— *Title*.

**3.** Select  **Use as a record title**.

**4.**Click **Save**.

_![Configuring a new attribute used as a record title](https://kb.cmwlab.com/assets/cmw_platform_lesson5_7.png)_

### Configure the Vehicle Type Form

Let's configure a form to fill out the *Vehicle types* records.

**1.** Select the *Vehicle types* record template in the diagram. In the element menu, click **Go to template** —  **Forms**.

_![Navigating to the template form list from the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_8.png)_

**2.** In the displayed form list, double-click *Vehicle types - Main Form* form to open it.

**3.** Rename the default area to *Vehicle type*.

**4.** Drag the *Title* attribute from the element pane to the *Vehicle type* area.

**5.** Click  ***Save***.

**6.** Click ***Configure template*** *‌*.

_![Configuring and saving the form](https://kb.cmwlab.com/assets/cmw_platform_lesson5_9.png)_

### Configure the Vehicle Types Table

Let's configure a table to list the vehicle types.

**1.** In the *Vehicle types* template, go to the **Tables** tab.

**2.** Double-click the *All records* table to open the table designer.

_![Opening the table designer from the template table list](https://kb.cmwlab.com/assets/cmw_platform_lesson5_10.png)_

**3.** In the table designer, click **Clear** to remove all table columns. Confirm the cleanup.

**4.** Drag the *Title* attribute to the table layout.

**5.** Click  **Save**.

**6.** Click the *Vehicle types* link above the table designer to go to the record template properties.

_![Navigating to the record template properties from the table designer](https://kb.cmwlab.com/assets/cmw_platform_lesson5_11.png)_

**7.** On the **Properties** tab, click **Navigate to instances**.

**8.** Click **Create** to add a new record.

**9.** In the *Title* field, enter *Car* and click ***Save***.

_![Creating a new record](https://kb.cmwlab.com/assets/cmw_platform_lesson5_12.png)_

**10.** Click the *Vehicle types* link above the form to return to the record list.

**11.** Likewise, create two more vehicle types — *Limo* and *Bus*.

_![Vehicle types records](https://kb.cmwlab.com/assets/cmw_platform_lesson5_13.png)_

### Create an Attribute Linking Two Record Templates

Business Requirement

We need to add the *Vehicle type* field to the vehicle request form, where the *Initiator* will select a record from the *Vehicle types* record template.

For this, we will link the *Vehicle requests* and *Vehicle types*templates using a **record attribute**.

Record Attribute

A **record** **attribute**links two record templates using a many-to-one, one-to-one, or many-to-many relationship.

When configuring a **record attribute**, you always specify a **linked template**.

**1.** Return to the data model diagram, select the *Vehicle requests* record template, and click **Add new attribute** in the element menu.

_![Adding a new attribute using the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_14.png)_

**2.** In the **New Attribute** window, specify the attribute **data type** — **Record,**and **name** — *Vehicle type*.

**3.** Select the **linked template** — *Vehicle types*.

**4.** Click **Save**.

_![Configuring a new record attribute](https://kb.cmwlab.com/assets/cmw_platform_lesson5_15.png)_

**5.** The data model diagram shows the relationship between the record templates as a line.

Relationship Lines on the Data Model Diagram

For the templates we linked, the relationship line shows that a vehicle request can only refer to one vehicle type — the ![One symbol in ER diagram](https://kb.cmwlab.com/assets/img_654de3429ba62.png) symbol, and several requests can refer to a vehicle type — the ![Many symbol in ER diagram](https://kb.cmwlab.com/assets/img_654de2e21e931.png) symbol.

Note

If a template relationship line does not appear automatically, select any template and click **Show linked** items in the element menu.

_![Record template relationship in the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_16.png)_

## Configure a Master Data Registry

Business Requirement

*Garage* staff need to keep vehicle records and see the available vehicles.

To achieve this, we will create a record template to store the master data of each vehicle.

Master Data

**Master data** refers to data about business entities that provide context for business transactions, such as vehicles, customers, or product models.

### Configure the Record Template — Vehicles

**1.** Drag the **New record type** to the data model diagram to create the new record template — *Vehicles*.

**2.** Select the newly added record template and click **Go to template** — **Attributes**in the element menu.

_![Navigating to the record template attribute list from the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_17.png)_

**3.** Add three **text** attributes: *Brand*, *Model*, and *Registration number*.

**4.** For the *Registration number*attribute, select the **Custom mask** **display format** and enter the following regular expression: `[A-Z0-9]{6,7}` (where `[A-Z0-9]` defines the allowed range of letters and numbers, and `{6,7}` defines the allowed number of characters). Select the **Use as record title** checkbox.

**5.** Create a **record** attribute — *Type*. For the **linked template**, select *Vehicle types*.

![The list of the attributes in the "Vehicles" record template](https://kb.cmwlab.com/assets/cmw_platform_lesson5_18.png)

The attribute list of the Vehicles record template

### Configure the Vehicle Form

**1.** On the **Forms** tab, open the *Vehicles - Main Form*.

**2.** Rename the default area to *Vehicle*.

**3.** Drag the newly created attributes from the element pane to the *Vehicle* area.

**4.** Click  **Save**.

_![Setting up the form for the "Vehicles" record template](https://kb.cmwlab.com/assets/cmw_platform_lesson5_19.png)_

### Configure the Vehicles Table

Let's configure the table to show all the relevant vehicle attributes.

**1.** Click **Configure template** *‌* and go to the **Tables** tab.

**2.** Double-click the *All records* table to open the table designer.

**3.** In the table designer, click **Clear** to remove all table columns. Confirm the cleanup.

**4.** Drag the *Brand*, *Model*, *Registration number*, and *Type* attributes to the table layout.

**5.** Click **Save**.

**6.** Click the *Vehicle* link above the designer to go to the record template properties.

_![Navigating to the record template properties from the table designer](https://kb.cmwlab.com/assets/cmw_platform_lesson5_20.png)_

## Test the Reference Data and Master Data Registries

### Create the Vehicle Records

Let's test the created reference data and master data registries.

**1.** Go to the **Properties** tab of the *Vehicles* record template and click **Navigate to instances**.

**2.** Click **Create**.

**3.**Fill out the form. In the *Type* field, specify the vehicle type.

**4.** Click **Save**.

**5.**click the *Vehicles* link above the form to return to the record list.

![Creating a new record in the "Vehicles" record template](https://kb.cmwlab.com/assets/cmw_platform_lesson5_21.png)

Creating a new record in the Vehicles record template

**6.** Create a few more records with different vehicle types.

_![Records in the Vehicles record template](https://kb.cmwlab.com/assets/cmw_platform_lesson5_22.png)_

### Group the Vehicles in the Table

Let's group the records in the table by vehicle type.

**1.** Click the *‌* icon in the *Type* column header.

**2.** Select **Group by this column**.

**3.** Click **Save**.

_![Grouping the vehicle records in the table by vehicle type](https://kb.cmwlab.com/assets/cmw_platform_lesson5_23.png)_

## Link the Vehicles with Vehicle Requests

Business Requirement

Let's add information about completed requests per vehicle.

To do this, we need an attribute that will link *Vehicles* and *Vehicle requests* record templates with a 1:M (one-to-many) relationship — there can be several requests for one vehicle. Configure this type of relationship using a **multivalue** **record attribute** with **attribute interlinking**.

Multivalue Record Attribute

A **record** **attribute** allows you to store, display, and modify a collection of links to records in another template. The records can be **interlinked**.

When creating a **record attribute**, you can configure **attribute interlinking** by creating a new link or using an existing one. For example, when you create an attribute in the *Vehicles* template linked to the *Vehicle requests* template, you can create a new interlinked **record** **attribute** in the *Vehicle requests* template, and the two templates become interconnected.

### Create a Multivalue Record Attribute — Vehicle Requests

**1.** In the *Vehicles* template, create a **record** **attribute**:

- **Name**: *Vehicle requests*
- **Store multiple values**: selected
- **Linked template**: *Vehicle requests*
- **Attribute interlinking**: **With a new one**
  - **New attribute properties**
    - **Name**: *Vehicle*

2. Click **Save**.

_![Configuring a new record attribute with interlinking](https://kb.cmwlab.com/assets/cmw_platform_lesson5_24.png)_

### Configure the Table on the Vehicle Form to Show the Related Vehicle Requests

Table on the Form

You can display a **multivalue record** **attribute** as a table on a form. You can configure the columns to show the attributes of the linked template, access mode, child record display, and filter for the table records.

**1.** Go to the **Forms** tab of the *Vehicles* template and double-click the *Vehicles - Main Form*.

**2.** In the form designer, drag the newly created *Vehicle requests* attribute from the element pane to the *Vehicle* area.

**3.** Click the *Vehicle requests*field on the form, and in the **Properties** panel, select **Table** from the **Appearance** dropdown.

_![Adding a table to the form](https://kb.cmwlab.com/assets/cmw_platform_lesson5_25.png)_

**4.** Expand the *Vehicle requests* attribute in the element pane and drag the following attributes to the table: *Car delivery time, Route,* and *Creator*.

_![Adding columns to a table on the form](https://kb.cmwlab.com/assets/cmw_platform_lesson5_26.png)_

**5.** Select the table toolbar.

**6.** From the element pane, drag **Add**and **Navigate**buttons to the table toolbar. These buttons will allow you to link existing requests to the vehicle and go to the related request form.

**7.**Click **Save**.

_![Adding buttons to the table toolbar](https://kb.cmwlab.com/assets/img_654bb5bc9f7c9.png)_

## Configure a Transactional Data Registry

Business Requirement

We have learned how to work with reference and master data. In addition, we need transactional data for our business process.

For example, we may store a list of passengers or waypoints in addition to the final destination. Or the driver can report the costs incurred during the trip.

To do this, we need two new data registries (record templates): travel costs (transactional data) and cost types (reference data). We will link the vehicle requests with the travel costs and the costs with the cost types.

### Configure the Record Template — Cost Types

Let's create a record template to store the cost types. We'll do this using the data model diagram designer.

**1.** In the navigation pane on the left, select **Diagrams**.

**2.** Double-click the *Data model - Vehicle management* diagram.

**3.** Create a new record template — *Cost types*.

**4.** Select the *Cost types*record template and click **Add new attribute** in the element menu.

_![Adding a new attribute using the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_28.png)_

**5.** Create a **text** attribute named *Title*. Select the **Use as record title** checkbox.

**6.** Go to the *Cost types* record template's **Forms** tab using the element menu.

_![Navigating to the template form list from the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_29.png)_

**7.** In the form list, open the *Cost types - Main Form* by double-clicking it.

**8.** Rename the default area to *Cost type*.

**9.** From the element pane, drag the *Title* attribute to the *Cost type* area.

**10.** Click **Save**.

**11.** Click **Configure template** *‌*.

_![Configuring the Cost type form](https://kb.cmwlab.com/assets/cmw_platform_lesson5_30.png)_

**12.** Go to the *Cost types* record template's **Tables** tab.

**13.** Configure the *All records* table to display only the *Title* attribute.

**14.** Click **Save**.

**15.**Click the *Cost types* link to go to the record template properties.

_![Configuring the Cost types table](https://kb.cmwlab.com/assets/cmw_platform_lesson5_31.png)_

**16.** Click **Navigate to instances** and create the following cost types: *Fuel*, *Service*, and *Other*.

![Records in the "Cost types" registry](https://kb.cmwlab.com/assets/cmw_platform_lesson5_32.png)

Records in the Cost types registry

### Configure the Record Template — Costs

Now, let's create a record template to store the costs.

**1.** Using the data model diagram, create the *Costs* record template.

**2.** Add the following attributes:

- *Amount*
  - **Data type**: **Number**
  - **Number of digits after decimal point**: 2
- *Type*
  - **Data type**: **Record**
  - **Linked template** — *Cost types*

**3.** In the *Costs* record template's element menu, select **Forms**.

**4.** In the form list, open the *Costs - Main Form* form by double-clicking it.

**5.** Rename the default area to *Cost*.

**9.** From the element pane, drag the *Amount* and *Type* attributes to the *Cost* area.

**10.** Click **Save**.

**11.** Click **Configure template** *‌*.

_![Configuring the Costs form](https://kb.cmwlab.com/assets/cmw_platform_lesson5_33.png)_

**12.**Return to the data model diagram. The diagram should show the relationship between the *Cost types* and *Costs* record templates. If you don't see the relationship line, click **Show linked items** in any element menu.

_![Relations between the record templates on the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_34.png)_

### Link the Vehicle Requests with the Costs

Now, we will link the *Vehicle requests* and *Costs* record template using the **record** attribute **interlinking**.

**1.** In the data model diagram, select the *Vehicle requests* record template and click **Add new attribute** in the element menu.

**2.** Create an attribute with the following properties:

- **Name:** *Costs*
- **Data type**: **Record**
- **Store multiple values**: selected
- **Linked template:** *Costs*
- **Attribute interlinking:** **With a new one**
  - **New attribute properties**
    - **Name:** *Vehicle request*

_![Creating a new record attribute with interlinking](https://kb.cmwlab.com/assets/cmw_platform_lesson5_35.png)_

**3.** The diagram should show the relationship between the *Vehicle requests* and *Costs* record templates. If you don't see the relationship line, click **Show linked items** in any element menu.

_![Showing linked items on the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_36.png)_

### Configure the Costs Table

**1.** Go to the *Costs* record template's **Tables** tab using the element menu.

![Navigating to the template table list the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson5_37.png)

Navigating to the template table list using the data model diagram

**2.** Configure the *All records* table to display the following attributes: *Vehicle request*, *Type*, and *Amount*.

![Setting the "Costs" default table](https://kb.cmwlab.com/assets/cmw_platform_lesson5_38.png)

Configuring the Costs table

## Results

In this lesson, you learned how to link and interlink the record templates using **record attributes**.

You have improved your application by adding the *Vehicle types* and *Cost types* reference data registries, *Vehicles* master data registry, and *Costs* transactional data registry.

Proceed to [Lesson 6 &mdash; Advanced Process](https://kb.comindware.ru/article.php?id=2155) to improve the vehicle booking process using the reference, master, and transactional data.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/2155-lesson_6_advanced.md
================================================
---
title: Lesson 6 &mdash; Advanced Process
kbId: 2155
---

# Lesson 6 &mdash; Advanced Process

## Introduction

In this lesson, you will improve the vehicle booking process by using the record templates created in the previous lesson (*Vehicle types*, *Vehicles*, *Costs*, and *Cost types*). You will configure the app to enable vehicle type selection during request submission, manage the corporate vehicles, and track the costs.

Estimated time to complete: 10 min

Prerequisite: complete [Lesson 5 &mdash; Data Structures](https://kb.comindware.ru/article.php?id=2154)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Enable Vehicle Type Selection at the Request Submission

Let's add the option to select the vehicle type when submitting a request. To do this, we will configure the vehicle request form.

**1.** Go to the *Vehicle requests* record template. Select the **Forms** tab.

**2.** Open the *Vehicle requests – Main Form*.

**3.** Drag the *Vehicle type* attribute to the form layout.

**4.**Click **Save**.

![Adding an attribute onto the form layout](https://kb.cmwlab.com/assets/cmw_platform_lesson6_1.png)

Adding an attribute to the form layout

## Enable Vehicle Selection for the Trip

Let's configure the *Accept request* task form so the *Garage manager* can select a vehicle for the trip.

**1.** Go to the *Ordering a corporate vehicle* business process diagram and click **Edit**.

**2.** Select the *Accept request* task and click **Form**in the element menu.

_![Navigating to the task form designer from the process diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson6_2.png)_

**3.** Expand the *Vehicle requests* attribute in the element pane and drag the *Vehicle* attribute to the *Acceptance* area.

**4.**Set the *Vehicle* field **Access** mode to **Require entry** and click **Save**.

_![Adding the Vehicle dropdown to the Accept request task form](https://kb.cmwlab.com/assets/img_6557824124af8.png)_

## Enable Trip Expense Accounting and On-The-Fly Vehicle Adding

Business Requirement

When the *Driver* receives the *Complete the trip* task, they should see the license plate number of the booked vehicle.

We'll also enable them to add a new vehicle to the list and track the trip expenses.

To achieve this, let's add the *Vehicle* dropdown and *Costs* table to the *Complete the trip* task form.

### Configure the Vehicle Field and Costs Table on the Complete the Trip Form

**1.** In the process diagram, select the *Complete the trip* task and click **Form**in the element menu.

**2.**Expand the *Vehicle requests* attribute in the element pane and drag the *Vehicle* attribute to the *Complete the trip* area.

**3.** Drag the *Costs* attribute to the *Complete the trip* area.

**4.** In the *Costs* **Field properties** panel, set the **Appearance** to **Table**.

_![Configuring and saving the Complete the trip task form](https://kb.cmwlab.com/assets/cmw_platform_lesson6_4.png)_

**5.** Expand the *Costs* attribute in the element pane and drag the *Type* and *Amount* attributes to the *Costs* table on the form.

**6.**Select the table toolbar. Drag the following buttons from the element pane to the toolbar: **Create**, **Edit**, and **Navigate**. This allows the end-users to create, edit, and view cost records from the *Costs* table on the form.

_![Adding buttons to the table toolbar using the form designer](https://kb.cmwlab.com/assets/img_6557827ca8ef6.png)_

### Configure the Total Costs Attribute

Let's add an attribute showing the total costs incurred for a vehicle request.

**1.** In the *Complete the trip* form designer, click **Add attribute** *‌* next to the *Vehicle requests* attribute in the element pane.

**2.** Create a new attribute:

- **Name:***Total costs*
- **Data type:** **Number**
- **Numbers of digits after decimal point:** 2

_![Adding the Total costs attribute to the Vehicle requests record template](https://kb.cmwlab.com/assets/cmw_platform_lesson6_6.png)_

**3.** Drag the *Total costs* attribute to the *Complete the trip* area under the *Costs* table.

**4.** Click **Save**.

**5.**Go back to the business process diagram and click **Publish**.

Note

Changes to the business process diagram will not take effect until the diagram is published. When publishing, you can update the current diagram version or create a new version. If you create a new diagram version, all process instances running the old version will be completed using the old version. New instances will run using the new version.

## Test the Vehicle Selection and Cost Tracking

**1.** Go to the *Ordering a corporate vehicle* process template. Click **Navigate to instances** on the **Properties**tab.

**2.** Start a new process by clicking **Create** in the process instance list.

**3.**Fill in the fields of the start form and indicate the vehicle type. Click **Create** to submit the form.

**4.** Go to **My tasks** using the navigation pane on the left.

**5.** Open the *Ordering a corporate vehicle - Approve request* task and select the *Approved* checkbox.

**6.** Click **Complete task**.

**7.** Return to **My tasks** and open the *Ordering a corporate vehicle - Accept request* task.

**8.** Select a car from the *Vehicle* dropdown.

**9.** Select *Yes* in the *Accepted* field and click **Complete task**.

**10.** Return to **My tasks**and open the *Ordering a corporate vehicle - Complete the trip* task.

**11.** Click **Create**in the *Costs* table.

**12.** Specify the cost *Type* and *Amount* and click **Save**.

**13.** Add more entries to the *Costs* table.

**14.** Click **Complete task**.

## Enable On-The-Fly Master Data Creation

Let's enable the *Driver* to add a new *Vehicle* record before commencing the trip.

**1.** Return to the business process diagram and click ***Edit***.

**2.** Open the *Complete the trip* task form designer.

**3.** Select the *Vehicle* attribute. In the **Field properties** panel select the **Records creation** checkbox.

Note

The **Records creation** checkbox in the field properties enables the end-user to create records using the linked template form.

Selecting this box for the *Vehicle* field enables the *Driver* to add a new vehicle to the registry on the fly.

**4.** Specify the **form** to use when adding a vehicle — *Vehicles - Main Form*.

_![Enabling on-the-fly record creation via a record attribute on the form](https://kb.cmwlab.com/assets/cmw_platform_lesson6_7.png)_

**5.** Save the task form and publish the business process diagram.

### Create a New Vehicle on the Fly

Let's test the on-the-fly new vehicle creation.

**1.** Start and go through the process up to the *Complete the trip* task.

**2.** Click **Create**in the *Vehicle* dropdown.

_![Adding a new vehicle record on the fly](https://kb.cmwlab.com/assets/cmw_platform_lesson6_8.png)_

**3.** Fill in the fields and click **OK** to add a new vehicle to the list.

**4.** Click **Complete task**.

## Results

In this lesson, you have configured the *Garage* staff task forms, enabled them to select a vehicle type and create vehicle records on the fly, and tested the improved vehicle booking process.

Proceed to [Lesson 7 &mdash; Automatic Calculations](https://kb.comindware.ru/article.php?id=2156) to configure automatic request number calculation, status, and total costs. You'll also learn how to filter vehicle records by the vehicle type.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/2156-lesson_7_auto_calc.md
================================================
---
title: Lesson 7 &mdash; Automatic Calculations
kbId: 2156
---

# Lesson 7 &mdash; Automatic Calculations

## Introduction

In this lesson, you will learn how to show the initiator name and request date and implement automatic calculations: total costs, request number, request status, and task title.

Estimated time to complete: 20 min

Prerequisite: complete [Lesson 6 &mdash; Advanced Process](https://kb.comindware.ru/article.php?id=2155)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Automatic Attribute Value Calculation

Business Requirement

We need to identify the requests by the request number and submission date. Also, we want the *Secretary* to know the request *Initiator* during the request approval. And we need to calculate the *Total costs*.

- The request *Initiator* is its creator, and the submission date is the request creation date. The **Creator** and **Creation date**system attributes are automatically set for each record. So, we will simply place these attributes on the request form.
- To calculate the request number and total cost amount, we will define the formulas.
## Display the Request Initiator's Full Name and Submission Date

Let's add the request creator and submission date fields to the vehicle request form.

**1.** Open the **Forms** tab of the *Vehicle requests* record template.

**2.** Open the *Vehicle requests - Main Form* form.

**3.** Expand the **Creator** attribute in the element pane and drag the **Full name** attribute to the form layout.

**4.** Then drag the **Creation date** attribute to the form layout.

**5.** Click **Save**.

_![Adding system fields onto the request form](https://kb.cmwlab.com/assets/cmw_platform_lesson7_1.png)_

## Calculate Total Costs

Let's configure the automatic *Total costs*calculation.

To do this, we will select the **Calculate using an expression** checkbox in the *Total costs* attribute properties. Then, we will enter a formula to calculate the attribute value. We will compose the formula using the expression editor and predictive input.

**1.** Go to the *Ordering a corporate vehicle* process template, open the process diagram, and click **Edit**.

**2.** Select the *Complete the trip* task.

**3.**In the element menu, click **Form**.

**4.** In the form designer, expand the *Vehicle requests* attribute in the element pane.

**5.** Click **Edit** next to the *Total costs* attribute.

**6.** In the attribute properties window, select the **Calculate using an expression** checkbox.

**7.** In the **Calculated value** field, click **Open in editor**.

**8.** In the expression editor that appears, enter the following function: `SUM()`.

**9.** Place the cursor inside the brackets and press `Ctrl+Space`.

**10.** In the dropdown that appears, double-click the *Costs* attribute.

_![Configuring an expression in the expression editor](https://kb.cmwlab.com/assets/cmw_platform_lesson7_2.png)_

**11.** The following expression should be inserted into the `SUM` function: `from a in db->Costs where Your condition select a->id`

_![Request query statement for a record template](https://kb.cmwlab.com/assets/cmw_platform_lesson7_3.png)_

**12.** Replace the `Your condition` text with `a->` and press `Ctrl+Space`.

**13.** In the dropdown that appears, double-click `Vehiclerequest` (system name of the *Vehicle request* attribute in the Costs record template).

_![Entering the Vehicle request attribute's system name in the formula](https://kb.cmwlab.com/assets/cmw_platform_lesson7_4.png)_

**14.** Enter `== $` after `Vehiclerequest`.

**15.** In the dropdown that appears, double-click the `id` (system name of the *ID* attribute in the *Vehicle requests* record template).

_![Entering the ID attribute's system name in the formula](https://kb.cmwlab.com/assets/cmw_platform_lesson7_5.png)_

**16.** Delete the `id` text after `select a->` and press `Ctrl+Space`.

**17.** In the dropdown that appears, double-click the `Amount` (the system name of the *Amount* attribute in the *Costs* record template).

_![Entering the Amount attribute's system name in the formula](https://kb.cmwlab.com/assets/cmw_platform_lesson7_6.png)_

**18.**The resulting formula should look as follows:

```
SUM(from a in db->Costs where a->Vehiclerequest == $id select a->Amount)
```

Total Costs Formula and Database Query Syntax

- `SUM()` — this function takes a value list and returns the sum of values.

As an argument to the `SUM()` function, we pass the list (array) of *Amount* values ​​from the *Costs* template. To get these values, we use a database query:

- `from a` — local variable `a` declaration.
- `in db->Costs` — data source declaration: *Costs* record template.
- `where a->Vehiclerequest == $id` — condition to sample the records from the *Costs* template, where the *Vehicle request* attribute value equals the ID attribute value of the current vehicle request.
- `select a->Amount` — query clause to get the *Amount* attribute values from the *Costs* template.
- `Costs` — the system name of the *Costs* record template.
- `Vehiclerequest` — system name of the *Vehicle request* attribute in the *Costs* template.
- `$id` — system name of the *ID* attribute in the *Vehicle requests* record template.
- `Amount` — system name of the *Amount* attribute in the *Costs* record template.

**19.** Click **Apply**, close the expression editor, and click **Save**.

_![The total costs formula](https://kb.cmwlab.com/assets/img_6553362c14b7e.png)_

**20.** Go to the business process diagram and click **Publish**.

### Test the Total Costs Calculation

**1.** Go to the instance list of the *Ordering a corporate vehicle* process template and click **Create**.

**2.** Go through the process up to the *Complete the trip* task.

**3.** Go to **My tasks** and open the *Ordering a corporate vehicle - Complete the trip* task.

**4.** Fill in the *Costs* table. The *Total costs* field should update automatically.

_![Total costs automatic calculation](https://kb.cmwlab.com/assets/img_6552158c7ac0b.png)_

## Generate Request Number

Let’s set up automatic request numbering.

**1.** Go to the **Attributes** tab of the *Vehicle requests* record template.

**2.** Create a new attribute:

- **Name:** *Number*
- **Data type: Text**
- **Use as a record title**: selected.

**3.** Go to the *Ordering a corporate vehicle* process diagram and click **Edit**.

**4.** Select the start event and click **Exit scenario**in the element menu.

_![Navigating to the start event exit scenario](https://kb.cmwlab.com/assets/cmw_platform_lesson7_9.png)_

**5.** The scenario designer appears.

**6.** Inside the **Change the context** action, click **Add action** and select **Change attribute values**from the dropdown.

_![Adding the Change attribute values action to the scenario](https://kb.cmwlab.com/assets/cmw_platform_lesson7_10.png)_

**7.**The new **Change attribute values**action appears inside the **Change the context** action.

**8.** Click **Change**in the **Change attribute values** ​​header.

_![Going to the scenario action properties](https://kb.cmwlab.com/assets/cmw_platform_lesson7_11.png)_

**9.** The **Action: Change attribute values** window appears.

**10.** Click **Create** above the attribute table.

**11.** In the **Attribute** column, select the *Number* attribute.

**12.** In the **Value operation** column, select **Replace**.

**13.** In the **Value** column, select **Formula**.

![Configuring the "Change attribute values" action](https://kb.cmwlab.com/assets/cmw_platform_lesson7_12.png)

Configuring the Change attribute values action

**14.** In the **Value** field, click  **Open in editor**.

**15.** Enter the following formula:

```
FORMAT("RE-{0}",LIST(COUNT(from a in db->Vehiclerequests select a->id)))
```

Request Number Formula Syntax

- `FORMAT()` — this function takes a string and a value list, replaces the `{0}`–`{n}` placeholders with the list values, and returns the resulting string.
- `LIST()` — this function combines its arguments into a list.
- `COUNT()` — this function takes a value list and returns the number of list items.
- `Vehichlerequests` — the system name of the *Vehicle requests* record template.

**16.** Click **Apply**, close the expression editor, and click **Save**.

_![Expression for the request's number calculation](https://kb.cmwlab.com/assets/cmw_platform_lesson7_13.png)_

**17.** Go to the process diagram and click **Publish**.

### Display the Request Number on the Form

Let's add the request number field on the form.

**1.**Open the **Forms** tab of the *Vehicle requests* record template.

**2.** Open the *Vehicle requests - Main Form*.

**3.** Add the *Number* attribute to the form layout.

**4.** For the *Number* field, set **Access** to **Read only**.

**5.** **Save** the form.

_![Adding the request number to the vehicle request form](https://kb.cmwlab.com/assets/img_65522e68174ca.png)_

### Test the Request Number Generation

**1.** Go to the instance list of the *Ordering a corporate vehicle* process template.

**2.** Click **Create** to initiate a new vehicle request.

**3.** In **My tasks**, open the *Ordering a corporate vehicle - Approve* *request* task.

**4.** The *Number* field should display the auto-generated request number.

_![The automatically generated request number](https://kb.cmwlab.com/assets/img_65532325f0787.png)_

## Track Vehicle Request Status

Let's configure the application to automatically change the vehicle request status depending on the process stage.

### Configure the Statuses Registry

We'll store the statuses in a new record template.

**1.** In the navigation pane on the left, select **Diagrams**.

**2.** Open the *Data model - Vehicle management* diagram.

**3.** Drag the **New record type** element to the diagram and create a new record template — *Statuses*.

**4.** Select the *Statuses*record template and add a new attribute:

- **Name:***Title*
- **Data type: Text**
- **Use as a record title:** selected

**5.** Select the *Statuses* template and click **Tables** in the element menu.

![Navigating to the template tables list from the data model diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson7_16.png)

Navigating to the template table list from the data model diagram

**6.** In the table list, open the *All records*table by double-clicking it.

**7.** Configure the table to display only the *Title* column.

**9.** Click **Save**.

![Configuring the Statuses default table](https://kb.cmwlab.com/assets/img_65523a010a825.png)

Configuring the Statuses table

**9.** Go to the **Forms** tab and open the *Statuses - Main Form*.

**10.** Add the *Title* attribute to the form.

![Configuring the "Statuses" main screen form](https://kb.cmwlab.com/assets/cmw_platform_lesson7_18.png)

Configuring the Statuses main screen form

**11.** Go to the record list and create the following status records: *Created*, *In Approval*, *Completed*, *Rejected*, and *Trip in Progress*.

_![Vehicle status records](https://kb.cmwlab.com/assets/cmw_platform_lesson7_19.png)_

**12.**Return to the data model diagram and select the *Vehicle requests* record template.

**13.** Using the element menu, create a new attribute:

- **Name:** *Status*
- **Data type:** **Record**
- **Linked template:** *Statuses*

_![Selected template relationships on the data model diagram are highlighted in blue](https://kb.cmwlab.com/assets/cmw_platform_lesson7_20.png)_

### Configure the Status Calculation

Let's configure the vehicle request status calculation depending on the process stage:

- *Created*
- *In Approval*
- *Rejected*
- *Trip in Progress*
- *Completed*

#### Set Status to Created

**1.**Go to the *Ordering a corporate vehicle* process diagram and click **Edit**.

**2.**Select the start event and click **Exit scenario** in the element menu.

**3.** Double-click the title of the **Change attribute values**action to configure its properties.

_![Editing the start event exit scenario](https://kb.cmwlab.com/assets/img_655336ce87765.png)_

**4.** Click **Create** above the attribute table.

**6.** In the **Attribute** column, select the *Status* attribute.

**7.** In the **Value operation** column, select **Replace**.

**8.** In the **Value** column, select **Formula**.

**9.** In the **Value** field, click **Open in editor**.

**10.** Enter the following formula:

```
OBJECT("Vehiclemanagement","Statuses","Title","Created")
```

Request Status Formula Syntax

- `OBJECT()` — this function takes the application system name, template system name, attribute system name, and attribute value. It returns the ID of the record where the attribute has the specified value.
- `Vehiclemanagement` — the system name of the *Vehicle management* application.
- `Statuses` — the system name of the *Statuses*record template.
- `Title` — the system name of the *Title* attribute in the *Statuses*  record template.
- `Created` — the *Title* attribute value to search.

_![A formula to change the vehicle request status to Created](https://kb.cmwlab.com/assets/cmw_platform_lesson7_22.png)_

**11.** Click **Apply**, close the expression editor, and click **Save**.

#### Set Status to In Approval

**1.** Return to the process diagram, but do not publish it yet.

**2.** If the business process diagram is not in the editing mode, click **Edit**.

**3.** Select the *Approve request* user task and click **Entry scenario**in the element menu.

**4.** Add the **Change attribute values** action inside the default **Change the context** action.

**5.** In the **Change attribute values** action, add the *Status*attribute with the **Replace** **value operation** and the following **Value formula**:

```
OBJECT("Vehiclemanagement","Statuses","Title","In Approval")
```
#### Set the Status to Rejected

**1.** Select the Rejected user task and use the element menu to open the **Entry scenario**.

**2.** Add the **Change attribute values** action inside the default **Change the context** action.

**3.** In the **Change attribute values** action, add the *Status*attribute with the **Replace** **value operation** and the following **Value formula**:

```
OBJECT("Vehiclemanagement","Statuses","Title","Rejected")
```
#### Set Status to Trip in Progress

**1.** Select a parallel gateway before the *Car assigned* and *Complete the trip*user tasks*.*

**2.** Similarly to the above, configure the **Exit scenario** to change the request *Status* to *Trip in Progress*:

```
OBJECT("Vehiclemanagement","Statuses","Title","Trip in Progress")
```
#### Set Status to Completed

**1.** Select the *Success* end event.

**2.** Configure the **Entry scenario** to change the request *Status* to *Completed*:

```
OBJECT("Vehiclemanagement","Statuses","Title","Completed")
```

**3.**Publish the business process diagram for the changes to take effect.

### Display the Request Status on the Form

We have configured a new attribute — vehicle request *Status*. Let's add it to the request form.

**1.** Open the **Forms** tab of the *Vehicle requests* record template.

**2.** Open the *Vehicle requests - Main Form*.

**3.** Arrange the form fields in two or three **columns**.

**4.** Drag the *Status* attribute to the form.

**5.** Set the  *Status* field **Access** mode to **Read only**.

**6.** Click **Save**.

_![Adding the Status attribute to the vehicle request form](https://kb.cmwlab.com/assets/img_655248a7e701e.png)_

### Display the Request Status and Number in the Request List

Let's add the vehicle request status and number to the table listing the vehicle requests.

**1.** Go to the **Tables** tab of the *Vehicle requests* record template.

**2.** Open the *All records* table designer.

**3.** Add the *Number*and *Status*columns to the table.

**4.**Click **Save**.

![Adding attributes to the "Vehicle requests" default table](https://kb.cmwlab.com/assets/cmw_platform_lesson7_24.png)

Adding attributes to the Vehicle requests default table

### Test the Request Status Change

**1.** Go to the instance list of the *Ordering a corporate vehicle* process template and create a new request.

**2.** In **My tasks**, open the *Ordering a corporate vehicle - Approve request* task.

**3.** The *Status* should be *In Approval*.

_![Automatically calculated Status attribute value](https://kb.cmwlab.com/assets/img_65532ffb54f9f.png)_

## Customize Task Titles

Business Requirement

The default task titles are not very informative — they only contain the process and task names.

For user convenience, we can add relevant request details to the task titles, e.g., the route and the Initiator's full name.

![The list of tasks with default titles](https://kb.cmwlab.com/assets/cmw_platform_lesson7_26.png)

The task list with default titles

**1.** Go to the *Ordering a corporate vehicle* business process diagram and click **Edit**.

**2.** Select the *Approve request* user task.

**3.** Click **Properties** in the element menu.

_![Navigating to the user task properties](https://kb.cmwlab.com/assets/cmw_platform_lesson7_27.png)_

**4.** In the **User task properties** window, go to the **Advanced** tab.

**5.** Select **Formula** in the **Task title** field.

**6.** Enter the following formula:

```
FORMAT(Approve request ({0} — {1}),LIST($Route,$_creator->fullName))
```

Task Title Formula Syntax

- `Route` — the system name of the *Route* attribute.
- `_creator->fullName` — full name of the user who created the request.
- `FORMAT()` — this function takes a string and a value list, replaces the `{0}`–`{n}` placeholders with the list values, and returns the resulting string.
- `LIST()` — this function combines its arguments into a list.

**7.** Click **Save**.

_![The Approve request task title formula](https://kb.cmwlab.com/assets/cmw_platform_lesson7_28.png)_

**8.** Similarly to the above, enter the **Task title** formulas for other tasks, specifying the appropriate task names:

- `FORMAT(Accept request ({0} — {1}),LIST($Route,$_creator->fullName))`
- `FORMAT(Rejected ({0} — {1}),LIST($Route,$_creator->fullName))`
- `FORMAT(Complete the trip ({0} — {1}),LIST($Route,$_creator->fullName))`
- `FORMAT(Car assigned ({0} — {1}),LIST($Route,$_creator->fullName))`

**9.** Publish the business process diagram.

### Test the Task Title Display in My Tasks

Let's view the custom task titles in the task list.

**1.** Go to the instance list of the *Ordering a corporate vehicle* process template and create a new request.

**2.** Go to **My tasks**.

**2.** The new task title should contain the route and the request creator's full name.

![A task with the calculated task title containing the route and the initiator's name](https://kb.cmwlab.com/assets/cmw_platform_lesson7_29.png)

A task with the calculated title including the route and the Initiator's name

## Results

Congrats! You have learned how to configure automatic calculations for attribute values and task titles.

Proceed to [Lesson 8 &mdash; Accounts](https://kb.comindware.ru/article.php?id=2157) to configure user accounts, roles, and permissions in your business application.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/2157-lesson_8_accounts.md
================================================
---
title: Lesson 8 &mdash; Accounts
kbId: 2157
---

# Lesson 8 &mdash; Accounts

## Introduction

In this lesson, you will learn how to design an organizational structure, create and manage user accounts: assign roles, issue and restrict access rights,  assign task performers, and configure navigation sections. You will:

- Create roles and define their permissions for the templates used in the vehicle ordering process.
- Create account groups and link them to the roles.
- Assign the created roles as the task performers.
- Create several accounts and add them to the groups.
- Customize the navigation pane for each role.

Estimated time to complete: 15 min

Prerequisite: complete [Lesson 4 &mdash; Monitoring and analytics](https://kb.comindware.ru/article.php?id=2153)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Configure Roles

Business Requirement

We need the following user roles for our application:

- *Initiator* — an employee who submits a vehicle request. They need to create the requests and view the completed requests.
- *Secretary* — approves the vehicle request. They need access to editing and viewing requests.
- *Garage manager*— accepts a vehicle request and assigns a car. They need to edit the request and generate reports.
- *Driver*— performs the trip and records the costs. They need to enter the costs.

Account Roles

**Roles**define account permissions to access application resources: record templates, tables, buttons, forms, business process tasks, etc.

To configure a **role**, you need:

- Set the role permissions to access the application resources.
- Assign a role to accounts or account groups.
- Specify the navigation section to display for the users belonging to this role.
### Create the Initiator Role

**1.** Select **Applications** in the navigation pane. Double-click the *Vehicle management* application to open its **Administration** page.

**2.** Go to the **Roles**.

_![Navigating to the application Roles](https://kb.cmwlab.com/assets/img_6554cf875717b.png)_

**3.** Click **Create**. The **Role properties** page appears.

**4.** Specify the role **name** — *Initiator*.

![Creating the "Initiator" role](https://kb.cmwlab.com/assets/cmw_platform_lesson8_2.png)

Creating the Initiator role

Business Requirement

The *Initiator* needs to create vehicle requests (i.e., initiate the vehicle booking process) and complete tasks. So, we will configure the permissions to access the process template and buttons.

**5.** Go to the **Permissions** tab.

**6.** Expand the *Ordering a corporate vehicle* process template in the resource pane on the left. Drag the **Create**, **Save**, and **Complete task** buttons to the resource permissions table.

**7.** Select the **View** checkbox for the *Vehicle management application*.

**8.** Select the **Create** and **View** checkboxes for the *Ordering a corporate vehicle* process template.

**9.** For the **Create**, **Save**, and **Complete task**buttons, select the **Use buttons** checkbox, as shown in the screenshot below.

_![Setting the process template access permissions for the Initiator role](https://kb.cmwlab.com/assets/img_6555cf4ae7d19.png)_

Business Requirement

To select a vehicle type when submitting a request, the *Initiator* needs to view the vehicle type records.

**10.** Drag the *Vehicle types* record template to the resource permissions table and select the **View** checkbox.

_![Setting the Initiator role access permissions to the reference data registry](https://kb.cmwlab.com/assets/cmw_platform_lesson8_4.png)_

Business Requirement

The *Initiator* needs to create vehicle requests and view the request list and request form.

**11.** Expand the *Vehicle requests* record template In the resource pane. Drag the *All records* table to the resource permissions table.

**12.** Drag the *Vehicle requests - Main Form* form to the resource permissions table.

**13.** Select the **Create** and **View** checkboxes for the *Vehicle requests* record template.

**14.** Select the **View** checkbox for the *Vehicle requests - Main Form* and *All records* table.

**15.** Click **Save**.

_![Setting the Initiator role access permissions to the transactional data registry](https://kb.cmwlab.com/assets/cmw_platform_lesson8_5.png)_

### Create the Secretary Role

**1.** Create the *Secretary* role and go to its **Permissions** tab.

**2.** Drag the *Ordering a corporate vehicle* process template to the resource permissions table and select the **View** and **Enter data** checkboxes.

**3.**Expand the *Ordering a corporate vehicle* process template and drag the **Create** and **Complete task** buttons to the resource permissions table.

**4.** For these buttons, select the **Use buttons** checkbox.

**5.** Drag the Vehicle requests record template to the resource permissions table and set its permission to **Full access**.

**6.** Drag the Vehicle types and Statuses record templates to the resource permissions table and set their permission to **View**.

**7.** Click **Save**.

_![Setting the Secretary role permissions](https://kb.cmwlab.com/assets/cmw_platform_lesson8_6.png)_

### Create the Garage Manager Role

**1.**Create the *Garage manager* role and go to its **Permissions** tab.

**2.** Drag the following templates to the resource permissions table: *Ordering a corporate vehicle, Vehicle requests, Statuses, Vehicle types, Vehicles, Cost types,* and *Costs*.

**3.** Set the **Full access**permission for these templates.

**4.** Click **Save**.

_![Setting the Garage manager role permissions](https://kb.cmwlab.com/assets/cmw_platform_lesson8_7.png)_

### Create the Driver Role

**1.**Create the *Driver* role and go to its **Permissions** tab.

**2.** Drag the following templates to the resource permissions table: *Statuses, Vehicle types,* and *Cost types*.

**3.** Set the **View** permission for these templates.

**4.** Drag the *Vehicles* record template and set its permission to **Create**, **View**, and **Enter data**.

**5.**Drag the *Vehicle requests* record template to the resource permissions table and set its permissions to **View** and **Enter data**.

**6.** Expand the *Ordering a corporate vehicle* process template.

**7.** Drag the **Save** and **Complete task** buttons to the resource permissions table. Set the **Use buttons** for these buttons.

**8.** For the *Ordering a corporate vehicle* process template, set the **View** and **Enter data** permissions.

**9.** Drag the *Costs* record template to the resource permission table and set its permissions to **Create**, **View**, and **Enter data**.

**10.** Expand the *Costs* record template, drag the *All records* table from it to the resource permissions table, and set its permission to **View**.

**11.** From the *Costs* record template, drag the **Create** button to the permission table and set its permission to **Use buttons**.

**12.** Click **Save**.

_![Setting the Driver role permissions](https://kb.cmwlab.com/assets/cmw_platform_lesson8_8.png)_

## Configure Account Groups

We have created the *Initiator, Secretary, Driver*, and *Garage manager* roles and defined their permissions to access application resources.

Now, let's create account groups and assign roles to them.

**1.** Select **Groups i**n the navigation pane to open the group list.

**2.** Click **Create**. Specify group **name** — *Secretaries*. Click **Create**to save the group.

_![Creating a new account group](https://kb.cmwlab.com/assets/cmw_platform_lesson8_9.png)_

**3.**  Similarly to the above, create the *Garage managers* and *Drivers* groups.

**4.** Create the *Employees* group and add all employees to it:

- Go to the **Members** tab.
- In the **Select the accounts and subgroups** pane, click the *Garage managers, Drivers*, and *Secretaries* groups to add them to the *Employees* group.
- Click **Create**to save the group.

_![Adding members to the Employees group](https://kb.cmwlab.com/assets/img_65548184837dd.png)_

**5.** The group list should contain *Employees, Drivers,**Garage managers, Secretaries,* and *Everyone* groups.

_![The list of all account groups](https://kb.cmwlab.com/assets/cmw_platform_lesson8_11.png)_

## Assign Roles to Groups

Business Requirement

Any employee can initiate a vehicle request. So, we will assign the *Initiator* role to the *Employees* group.

We will assign the *Secretary,* *Garage* manager, and *Driver*roles to the *Secretaries,* *Garage* *managers*, and *Drivers*groups, respectively.

**1.** In the navigation pane, select **Roles**.

**2.** Open the *Initiator* role by double-clicking it in the role list.

![Navigating to the "Initiator" role from the list of roles](https://kb.cmwlab.com/assets/cmw_platform_lesson8_12.png)

Navigating to the Initiator role from the role list

**3.** Go to the **Role properties** tab.

**4.** In the **Assign this role to accounts and groups** list, click the *Employees* group to move it to the **Selected accounts and groups** list.

**5.** Click **Save**.

![Assigning the "Initiator" role to the "Employees" account group](https://kb.cmwlab.com/assets/cmw_platform_lesson8_13.png)

Assigning the Initiator role to the Employees account group

**6.** Similarly to the above, configure the remaining roles:

- Add the *Secretaries* group to the *Secretary* role.
- Add the *Garage managers* group to the *Garage manager* role.
- Add the *Drivers* group to the *Driver* role.

## Assign Task Performers

We have created roles, specified account groups, and their access rights.

Business Requirement

Up to this point, all user tasks were assigned to the current user.

Now, we will assign the *Secretary, Garage manager,*and *Driver* roles as performers for the respective user tasks.

As before, the *Rejected* and *Car assigned*tasks will be assigned automatically to the vehicle request creator.

**1.** Select **Applications** in the navigation pane**.**Navigate to the *Vehicle management* application.

**2.** Open **Templates** and go to the *Ordering a corporate vehicle* process template.

**3.** Go to the **Diagram** tab and click **Edit**.

**4.**Select the *Approve request user* task and click **Properties** in the element menu.

_![Navigating to the user task properties from the process diagram](https://kb.cmwlab.com/assets/cmw_platform_lesson8_14.png)_

**5.** Go to the **Advanced** tab.

**6.** In the **Performers** field, uncheck your account and check Secretary.

**7.** Click **Save**.

_![Changing the task performer](https://kb.cmwlab.com/assets/cmw_platform_lesson8_15.png)_

**8.** For the *Accept request* user task, specify the *Garage manager* role as the performer.

**9.**For the *Complete the trip* user task, specify the *Driver* role as the performer.

**10.** Publish the business process diagram.

## Create Accounts

Let's create the *Secretary, Garage manager*, and *Driver* accounts.

**1.** In the navigation pane, go to **Accounts**.

**2.** Click **Create**.

_![Creating a new account](https://kb.cmwlab.com/assets/cmw_platform_lesson8_16.png)_

**3.** Select the English **language**.

**4.** Enter the user's **full name** and **e-mail**.

**5.** Enter the **username** to log in to the account.

**6.** Enter and confirm the **password**.

**7.** Enter the **job title** — *Garage manager*and **department** — *Garage*.

**8.** Click **Create**to save the account.

_![Configuring an account](https://kb.cmwlab.com/assets/cmw_platform_lesson8_17.png)_

**9.** Similarly to the above, create a driver account (**job title** — *Driver*, the **department** — *Garage*).

**10.** Create two *Secretary* accounts and one *Initiator* account.

_![Accounts for the vehicle booking process](https://kb.cmwlab.com/assets/cmw_platform_lesson8_18.png)_

## Add Accounts to Groups

Let's add the accounts to groups according to their job function.

**1.** In the navigation pane, go to **Groups**.

**2.** Double-click the *Drivers* group and go to the **Members** tab.

**3**. Add the *Driver*'s account to this group.

**4.** Click **Save**.

_![Editing the group members](https://kb.cmwlab.com/assets/img_6554e2730d144.png)_

**5.** Similarly to the above, add the *Garage manager* account to the *Garage managers* group

**6.** Add the *Secretary* accounts to the *Secretaries* group.

**7.** To the *Employees* group, add an account that should be able to create vehicle requests.

_![Adding a user account to the Employees group](https://kb.cmwlab.com/assets/cmw_platform_lesson8_20.png)_

## Configure Navigation Sections

Navigation sections appear in the navigation pane and provide a convenient way to navigate within the **CMW Platform.**

Up to this point, we have been using the system navigation section. Now, we will configure a navigation section for each role.

### Create the Initiator Navigation Section

Let's configure a navigation section for the *Initiator* role. They need to create vehicle requests and view their tasks.

**1.** Select **Applications**from the navigation pane.

**2.** Double-click the *Vehicle management application* to open its **Administration** page.

**3.** Go to the **Navigation sections**.

**4.** Click **Create**. The navigation section designer appears.

**5.** In the **Navigation section properties**, set the navigation section **display name**— *Initiator*. Ensure that the *Vehicle management* application is selected.

**6.** Assing the navigation section to the *Initator* role:

- Click the **0 roles** label in the **Navigation section properties** panel.
- In the **Roles** window, add the *Initiator* role to the right list by double-clicking it in the left list.
- Click **Apply**.

_![Selecting a role for the navigation section](https://kb.cmwlab.com/assets/cmw_platform_lesson8_21.png)_

**8.**Drag the **My tasks** item from the resource pane to the navigation section layout.

**9.** Expand **Process templates** > *Ordering a corporate vehicle >***Buttons** in the resource pane and drag the **Create**button to the navigation section layout.

**10.**Click **Save**.

_![Configuring the Initiator navigation section](https://kb.cmwlab.com/assets/cmw_platform_lesson8_22.png)_

### Create the Secretary Navigation Section

Let's create a navigation section for the *Secretary* role. They need to view all vehicle requests and their tasks.

**1.** Create a new navigation section using the navigation section list of the *Vehicle management application*.

**2.** Rename the navigation section to *Secretary*.

**3.** Assign the navigation section to the *Secretary* role.

**4.**Drag the **My tasks** item to the navigation section layout.

**5.** Expand **Record templates** > *Vehicle requests >* **Tables** in the resource pane and drag the *All records*table to the navigation section layout.

**6.**Select the *All records* item and rename it to *Vehicle requests*.

**7.** Click **Save**.

_![Configuring the Secretary navigation section](https://kb.cmwlab.com/assets/cmw_platform_lesson8_23.png)_

### Create the Garage Employee Navigation Section

Let's configure a navigation section for garage employees — *garage managers* and *drivers.* They need to process vehicle requests and view costs and monthly request summary.

**1.** Open the *Summary* navigation section you created in [Lesson 4 &mdash; Monitoring and analytics](https://kb.comindware.ru/article.php?id=2153). It is available in the *Vehicle management* application navigation section list.

**2.** Rename the navigation section to *Garage employee*.

**3.** Assign two roles to this navigation section: *Garage manager* and *Driver*.

**4.** Drag the **My tasks** item to the navigation section layout.

**5.** Expand **Record templates >** *Vehicle requests >* **Tables** in the resource pane and drag *All records*table to the navigation section layout.

**6.**Rename the *All records* navigation item to *Vehicle requests*.

**7.** Expand **Record templates** > *Costs >* **Tables** and drag *All records* table to the navigation section layout.

**8.** Rename the *All records* navigation item to *Costs.*

**10.** Click **Save**.

_![Configuring the Garage employee navigation section](https://kb.cmwlab.com/assets/cmw_platform_lesson8_24.png)_

## Test the Roles and Task Performer Assignment

Note

To test the configured roles and task performer assignment, you will log in to the accounts with different roles (*Initiator, Secretary, Garage manager*, and *Driver*) several times.

You can view the account usernames on the **Administration — Accounts**page.

For your convenience, log in to each account using incognito mode and a new window in a different browser.

**1.** Sign in to the *Initiator* account.

**2.** Click **Create**in the navigation pane and fill in the start form fields to create a vehicle request and start the business process.

![Creating a vehicle request under the Initiator account](https://kb.cmwlab.com/assets/cmw_platform_lesson8_25.png)

*Creating a vehicle request under the Initiator account*

**3.** Log out. To do this, click the user icon in the upper right corner of the page and click **Log out**.

_![Logging out](https://kb.cmwlab.com/assets/img_6554e54017f22.png)_

**4.** Log in to one of your *Secretary* accounts.

**5.** Go to **My tasks** using the left navigation pane.

**6.** Open the *Approve request* task by double-clicking its name.

_![Viewing My tasks as the Secretary](https://kb.cmwlab.com/assets/cmw_platform_lesson8_27.png)_

**7.** Select the *Approved* checkbox and complete the task.

**8.** Log out.

**9.** Sign in to your *Garage manager's* account.

**10.** Go to **My tasks** and open the *Accept request* task.

**11.** Select a vehicle, select the *Accepted* checkbox, and complete the task.

**12.** Log out.

_![Completing a task as the Garage manager](https://kb.cmwlab.com/assets/cmw_platform_lesson8_28.png)_

**13.** Log in to the *Driver*’s account.

**14.** Open the *Complete the trip* task and fill in the cost data.

**15.**Complete the task.

_![Completing a task as the Driver](https://kb.cmwlab.com/assets/cmw_platform_lesson8_29.png)_

**16.** Log in to the *Initiator*’s account and complete the *Car assigned*task.

## Results

Congrats! You learned how to configure roles and define access rights, configure accounts and groups, and configure navigation sections. You have improved the vehicle booking process: now, different users perform their tasks according to their roles and access only the pages intended for them.

Proceed to [Lesson 9 &mdash; Document Generation](https://kb.comindware.ru/article.php?id=2158) to learn how to generate documents using the **CMW Platform**.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/2158-lesson_9_documents.md
================================================
---
title: Lesson 9 &mdash; Document Generation
kbId: 2158
---

# Lesson 9 &mdash; Document Generation

## Introduction

In this lesson, you will learn how to generate a PDF report from the business process data using a Microsoft Excel template.

Estimated time to complete: 15 min

Prerequisite: complete [Lesson 6 &mdash; Advanced Process](https://kb.comindware.ru/article.php?id=2155)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Generate Cost Report

Business Requirement

After completing the trip, the *Driver* needs to download a PDF report detailing the expenses they filed.

Let's configure the cost report generation on a button click in the *Complete the trip* user task.

To export a record as a formatted document, you need to:

1. Create an Excel or Word file with data placeholders and arbitrary static content.
2. Configure an export template using your Excel or Word template file.
3. Configure a button to generate the document filled with the exported data.
4. Click the button to download the generated document.

### Configure Excel Template File

Let's configure an Excel file with placeholders for the export template.

**1.** Create an Excel file (in XLSX format).

**2.** Fill in the Excel sheet as shown in the figure below:

_![Cost report Excel template file](https://kb.cmwlab.com/assets/cmw_platform_lesson9_1.png)_

Export Template File Syntax

The export template replaces placeholders in an Excel or Word file with the exported data. The rest of the template file content remains intact during the export.

The export template file may contain arbitrary content and placeholders to hold the exported data. You can export single attribute values and datasets.

This way, you can create a sophisticated layout, e.g., an invoice, and fill it with the exported data.

- To export an attribute value, enter its system name in curly brackets: `{systemname}`
- To export a linked template attribute value, enter its system name after the record attribute system name separated by a full stop: `{RecordAttribute.LinkedTemplateAttribute}`
- To export a dataset ​​from a record template linked to a multivalue record attribute, use the `foreach` and end statements:
  ```
  {foreach:MultiValueRecordAttribute} {RecordAttribute.LinkedTemplateAttribute1} {LinkedTemplateAttribute2} {end:MultiValueRecordAttribute}
  ```
  - A table row with the `foreach and``end` statements is converted to several rows — a row per linked record.
  - In the first column, enter the `foreach:` operator and the record attribute system name (no spaces allowed): {foreach:MultiValueRecordAttribute}
  - In the last column, enter the `end:` operator and the record attribute system name (no spaces allowed): {end:MultiValueRecordAttribute}
  - Between the `foreach` and `end` statements, enter the linked template attribute system names in curly braces: {LinkedTemplateAttribute}.

To export data from the *Vehicle request* record template, enter attribute system names in curly brackets:

- `{Totalcosts}` — the total amount of costs.
- `{Number}` — the request number.
- `{Cardeliverytime}` — car delivery time.

To export the cost records linked to a vehicle request, enter the following:

```
{foreach:Costs} {Type.Title} {Amount} {end:Costs}
```

- `Costs` — the multivalue record attribute in the *Vehicle requests* record template linked to the *Costs* record template.
- `Amount` — the attribute in the *Costs* record template.
- `Type` — the record attribute in the *Costs* record template linked to the *Cost types* record template.
- `Title` — the attribute in the *Cost types* record template.
### Configure Export Template

**1.** In the *Vehicle requests* record template, go to the **Export templates** tab.

**2.** Click **Create**.

_![Creating an export template](https://kb.cmwlab.com/assets/cmw_platform_lesson9_2.png)_

**3.** The **New export template** window appears.

**4.** Specify the export template **name**— *Cost report*.

**5.** In the **Template file** field, select **Value** and upload the XLSX template file you created earlier.

**6.** In the **Output file name** field, select **Value** and specify the required name of the exported data file *without the file extension — Cost report*.

**7.** Check the **Export as PDF** checkbox.

**8.**Click **Save**.

_![Configuring an export template](https://kb.cmwlab.com/assets/cmw_platform_lesson9_3.png)_

## Configure Export Button

When you create an export template, a corresponding button to download the exported document is automatically created.

Let's verify the export button properties and add the button to the user task form.

### Verify Export Button Properties

**1.** In the *Vehicle requests* record template, go to the **Buttons** tab.

_![The list of buttons in the record template](https://kb.cmwlab.com/assets/cmw_platform_lesson9_4.png)_

**2.** Open the *Cost report* button by double-clicking on it. Check that its properties are correct:

- **Display name:** *Cost report*
- **Operation context:** **Record**
- **Operation:** **Export record**
- **Operation result:** **Download document**
- **Export template:** *Cost report*

_![The Cost report button properties](https://kb.cmwlab.com/assets/cmw_platform_lesson9_5.png)_

### Add Export Button to the User Task Form

Let's add the *Cost report* button to the *Complete the trip* user task form:

- Create the *Report download*form with only the *Cost report* button.
- Place the *Report download* form on the *Complete the trip* user task form.

**1.** Open the *Vehicle requests* record template and go to the **Forms** tab.

**2.** Click **Create**.

**3.** Rename the form to *Report download*.

**4.** Rename the default area to *Report download*.

**5.** Select the toolbar in the *Report download* area and drag the *Cost report* button to the toolbar.

**6.** Save the form.

_![Adding a button to the form](https://kb.cmwlab.com/assets/img_655630b02a0c2.png)_

**7.** In the *Ordering a corporate vehicle* process template, go to the **Diagram** tab and click **Edit**.

**8.** Select the *Complete the trip* user task and click **Form** in the element menu.

**9.** Expand the *Vehicle requests* template in the element pane and drag the *Report download* form below the *Complete the trip* area.

**10.**Save the form.

_![Adding the Report download subform to the Complete the trip user task form](https://kb.cmwlab.com/assets/img_6556314418e53.png)_

**5.**Publish the *Ordering a corporate vehicle* process diagram.

### Configure Export Button Display Condition

To use the *Cost report* button, the *Driver* needs the appropriate permission in the *Driver* role.

**1.** In the *Vehicle management* application, go to **Roles**.

**2.** Open the *Driver* role and go to the **Permissions** tab.

**3.** Expand the *Vehicle request* record template in the resources pane and drag the *Cost report* button to the resource permissions table.

**4.** Select the **Use buttons** checkbox for the *Cost report* button.

**5.** Save the role.

![Adding the permission to use a button in the "Driver" role](https://kb.cmwlab.com/assets/cmw_platform_lesson9_8.png)

Adding the permission to use a button in the Driver role

## Test the Cost Report Export

Note

If you completed [Lesson 8 &mdash; Accounts](https://kb.comindware.ru/article.php?id=2157), the user tasks are assigned to different accounts.

To go through the business process, you can perform user tasks in one of the three ways:

- Log in several times with different accounts: *Initiator, Secretary, Driver, Garage manager*.
- Order a vehicle, open the running process instance diagram, and go through the tasks using the **Navigate** button in the **Tokens** panel.
- Set your account as the performer of all user tasks.

**1.** Submit a new vehicle request using the instance list of the *Ordering a corporate vehicle* process template.

**2.** Go through the business process up to the *Complete the trip*task using **My tasks**.

**3.**Open the *Complete the trip*task and add some costs to the table.

**4.** Click **Save**.

**5.**Click *Cost report* and wait for the generated PDF document to download.

_![Downloading the cost report from the Complete the trip task](https://kb.cmwlab.com/assets/img_655636a793e24.png)_

**6.** Open the exported document.

**7.** Complete the task.

_![The exported PDF document](https://kb.cmwlab.com/assets/cmw_platform_lesson9_10.png)_

## Results

Congrats! You have learned how to automatically generate and export documents based on templates, substituting data from a business application.

Proceed to [Lesson 10 &mdash; Working with Files](https://kb.comindware.ru/article.php?id=2159) to learn how to work with the files.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/398. Training/2159-lesson_10_files.md
================================================
---
title: Lesson 10 &mdash; Working with Files
kbId: 2159
---

# Lesson 10 &mdash; Working with Files

## Introduction

In this lesson, you will learn how to use the **document attribute** to attach files to a template record.

Estimated time to complete: 10 min

Prerequisite: you complete [Lesson 9 &mdash; Document Generation](https://kb.comindware.ru/article.php?id=2158)

**Note:** This lesson is for the **CMW Platform** version 4.2.571.0. In other versions, the page and menu appearance may differ from the screenshots.

## Configure Document Uploading

Business Requirement

The *Driver* needs to upload scanned receipts and other documents to the system after completing the trip.

Document Attribute

The **document attribute** stores the files uploaded by end-users.

You can configure the **document attribute** to allow uploading only specific file types or any files.

The document field on the form allows you to upload, download, delete, and preview the files.

### Create Document Attribute

Let’s add a **document attribute** to the *Costs* record template.

**1.** In the *Costs* record template, go to the ***Attributes*** tab.

**2.** Create a new attribute:

- **Name:***Attachments*
- **Data type:** **Document**
- **Store multiple values:**selected to allow attaching multiple files to a record

_![Creating a document attribute to store multiple files](https://kb.cmwlab.com/assets/cmw_platform_lesson10_1.png)_

### Add Document Field to a Form

Let's add the *Attachments*attribute to the *Costs* table on the *Complete the trip* user task form.

**1.** In the *Ordering a corporate vehicle* process template, go to the **Diagram** tab and click **Edit**.

**2.** Select the *Complete the trip* user task and click **Form**in the element menu.

**3.** Expand the *Vehicle requests* and *Costs* templates in the element pane.

**4.** Drag the *Attachments* attribute to the *Costs* table.

**5.**Save the form.

_![Adding a document attribute to a table on the task form](https://kb.cmwlab.com/assets/img_65572a5aa091e.png)_

**6.**Go back to the process diagram and publish it.

## Test Uploading and Downloading a Document for a Cost Entry

**1.** Submit a new vehicle request and go through the business process up to the *Complete the trip* user task.

Note

If you completed [Lesson 8 &mdash; Accounts](https://kb.comindware.ru/article.php?id=2157), the user tasks are assigned to different accounts.

To go through the business process, you can perform user tasks in one of the three ways:

- Log in several times with different accounts: *Initiator, Secretary, Driver, Garage manager*.
- Order a vehicle, open the running process instance diagram, and go through the tasks using the **Navigate**button in the **Tokens** panel.
- Set your account as the performer of all user tasks.

**2.**Open the *Complete the trip* user task and add a record to the *Costs* table.

**3.**Upload any file to the created record:

- Click the *Attachments* field in the cost record row.
- Click ***Add document**.*

**4.**Create another entry in the Costs table.

**5.**Upload any file for the second cost record.

**6.** Click ***Save***.

![Adding a file to the "Attachments" field](https://kb.cmwlab.com/assets/cmw_platform_lesson10_3.png)

Adding a file to the Attachments field

**7.** To test an attached file downloading, click the file name in the *Costs* table. Your browser should download the file.

## Results

Congrats! You have learned how to upload and download the files in the **CMW Platform**.

 [*‌* Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/1943-export_template_csharp.md
================================================
---
title: Configure an Export Template with C# Data Processing
kbId: 1943
---

# Configure an Export Template with C# Data Processing

## Use Case

In addition to the standard export template feature, you can configure a custom data export using a C# script with more flexible data processing. For example, you can apply data filters, replace data, or reformat the values.

In this article, we will configure the Excel and Word export templates and C# scripts to export the files with each collection element on a separate line (by default, all collection elements are listed on one line separated by a space). The export templates and C# scripts slightly differ for Word and Excel formats.

## Prerequisites

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Clients* | *Contracts\_collection* | **Record** | The *Contracts* attribute is linked to the *Contracts* template and stores multiple values (a *collection*). |
| *Title, Contact, Phone, Email* | **Text** | The client details. |
| *Contracts* | *Status* | Record | The *Status* attribute is linked to the *Contract Statuses* template. |
| *Title, Date, Total* | Text | The contract details. |
| *Contract Statuses* | **Title** | **Text** | The status name. |

## Instructions

### Create an Excel Export Template

1. Create an XLSX document as shown below:

_![Example of an Excel export template](https://kb.cmwlab.com/assets/exp1_en.png)_

In the Excel export template the `&=data.class_property` placeholders are the `MainData` class property references filled by the C# script.

**Note:** You must specify the required cell format in the Excel file. Otherwise, the data will not be exported correctly. For numeric attributes set a numeric format, for date & time attributes set a date format, etc.

1. Add the XLSX document as an export template to the *Clients* record template.

_![The export template listed on the export templates tab](https://kb.cmwlab.com/assets/img_6437fe0b2b90d.png)_

1. A button with the **Export record** operation will be automatically added to the *Clients* template:

_![The button for the Export record operation](https://kb.cmwlab.com/assets/img_643800d4628a9.png)_

1. Open the button properties, and on the **Script** tab, enter the following C# code:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Aspose.Cells;
using Aspose.Cells.Pivot;
      
class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
var objectsData = Api.TeamNetwork.ObjectService.ListWithAlias("Clients"); // system name of the Clients record template
var dataToExport = new List();
foreach (var objectDict in objectsData)
{
var ContractDataInIds = getterListSTR("Contracts_collection", objectDict); // system name of the Contracts_collection record attribute in the Clients records template
     
if(ContractDataInIds.Count == 0) {ContractDataInIds.Add("tempID");}
var ContractDataInList = new List();
foreach (var ContractDataInId in ContractDataInIds)
{
var ContractDataInData = GetData(ContractDataInId);
      
var Status_Id = getterSTR("Status", ContractDataInData); // system name of the Status record attribute in the Contracts record template
var Status_Data = GetData(Status_Id);
      
var ContractDataInT = new ContractData
{
Name = getterSTR("Title", ContractDataInData), // system name of the Title attribute in the Contracts record template
Date = getterDT("Date", ContractDataInData), // system name of the Date attribute in the Contracts record template
Total = getterDC("Total", ContractDataInData), // system name of the Total attribute in the Contracts record template
      
Status = getterSTR("Title", Status_Data) // system name of the Title attribute in the Contract Status record template
      
};
ContractDataInList.Add(ContractDataInT);
}
      
var Data_ = new MainData
{
Client = getterSTR("Title", objectDict), // system name of the Title attribute in the Clients record template
Contact = getterSTR("Contact", objectDict), // system name of the Contact person attribute in the Clients record template
Phone = getterSTR("Phone", objectDict), // system name of the Phone attribute in the Clients record template
Email = getterSTR("Email", objectDict), // system name of the Email attribute in the Clients record template
Contract = ContractDataInList
};
dataToExport.Add(Data_);
}
      
var content = Api.TeamNetwork.ObjectAppExportService.ExecuteExcelExportTemplate(userCommandContext.DocumentTemplateId, dataToExport);
var result = new UserCommandResult
{
Success = true,
Commited = true,
ResultType = UserCommandResultType.File,
File = new UserCommandFileResult()
{
Name = "Excel_Data.xlsx",
Type = "Excel",
Content = content
      
},
Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = "Generated the file"
}
}
};
return result;
    }
      
public static Decimal getterDC(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return 0;
}
var stringValue = getterSTR(key, dictionary);
if (stringValue != null && Decimal.TryParse(stringValue, out var result))
{
return result;
}
else
{
return 0;
}
}
      
public static DateTime? getterDT(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return null;
}
var stringValue = getterSTR(key, dictionary);
if (stringValue != null && DateTime.TryParse(stringValue, out var result))
{
return result.AddHours(5);
}
else
{
return null;
}
}
      
public static string getterSTR(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return null;
}
if (dictionary.TryGetValue(key, out var result))
{
if (result == null) return null;
return result.ToString();
}
else
{
return null;
}
      
}
      
public static IList getterListSTR(string key, IDictionary<string, object> dictionary = null)
{
var result = new List();
if (dictionary != null && key != null)
{
if (dictionary.TryGetValue(key, out var objectData))
{
var objectDataArray = objectData as object[];
foreach (var singlObject in objectDataArray)
{
if (singlObject == null) continue;
result.Add(singlObject.ToString());
}
}
}
return result;
}
      
public static IDictionary<string, object> GetData(string objectId = null)
{
if (objectId == null || objectId.Contains("account") || objectId == "tempID")
{
return null;
}
var container = Api.TeamNetwork.ObjectAppService.GetByObject(objectId);
var result = Api.TeamNetwork.ObjectService.GetWithAlias(container.Alias, objectId);
return result;
}
}
      
[Serializable]
public class MainData
{
public string Client { get; set; }
public string Contact { get; set; }
public string Phone { get; set; }
public string Email { get; set; }
public List Contract { get; set; }
}
      
[Serializable]
public class ContractData
{
public string Name { get; set; }
public decimal Total { get; set; }
public DateTime? Date { get; set; }
public string Status { get; set; }
}
```
**Note:**In the script above, the lines with the attribute and template system names are marked with comments. In these lines, substitute the actual system names from your application.
### Create a Word Export Template

1. Create a DOCX document as shown below:

_![Example of a Word export template](https://kb.cmwlab.com/assets/img_643801f95205b.png)_

In the Word export template:

- The `row.class_property` placeholders are `MainData` class property references filled by the C# script.
- The `row` variable is the iterator for `MainData_` array, that contains `MainData` class instances.

1. Add the DOCX document as an export template to the *Clients* record template.
2. A button with the **Export record** operation will be automatically added to the *Clients* template.
3. Open the button properties, and on the **Script** tab, enter the following C# code:

```
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text.RegularExpressions;
using Comindware.Data.Entity;
using Comindware.Platform.Api.Data;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using System.IO;
using System.Data;
      
class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
var objectsData = Api.TeamNetwork.ObjectService.ListWithAlias("Clients"); // system name of the Clients record template
List Data_ = new List();
foreach (var objectDict in objectsData)
{
var ContractDataInIds = getterListSTR("Contracts_collection", objectDict); // system name of the attribute-collection in the Clients record template
if(ContractDataInIds.Count == 0) {ContractDataInIds.Add("tempID");}
bool first_element = true;
foreach (var ContractDataInId in ContractDataInIds)
{
var ContractDataInData = GetData(ContractDataInId);
      
var Status_Id = getterSTR("Status", ContractDataInData); // system name of the Status record attribute in the Contracts record template
var Status_Data = GetData(Status_Id);
      
if(first_element == true)
{
first_element = false;
var temp = new MainData
{
Client = getterSTR("Title", objectDict), // system name of the Title attribute in the Clients record template
Contact = getterSTR("Contact", objectDict), // system name of the Contact person attribute in the Clients record template
Phone = getterSTR("Phone", objectDict), // system name of the Phone attribute in the Clients record template
Email = getterSTR("Email", objectDict), // system name of the Email attribute in the Clients record template
      
Name = getterSTR("Title", ContractDataInData), // system name of the Title attribute in the Contracts record template
Date = getterDT("Date", ContractDataInData), // system name of the Date attribute in the Contracts record template
Total = getterDC("Total", ContractDataInData), // system name of the Total attribute in the Contracts record template
Status = getterSTR("Title", Status_Data) // system name of the Title attribute in the Contract statuses record template
};
             Data_.Add(temp);
}
else
{
var temp = new MainData
{
Name = getterSTR("Title", ContractDataInData), // system name of the Status attribute in the Contracts record template
Date = getterDT("Date", ContractDataInData), // system name of the Date attribute in the Contracts record template
Total = getterDC("Total", ContractDataInData), // system name of the Total attribute in the Contracts record template
Status = getterSTR("Title", Status_Data) // system name of the Title attribute in the Contract statuses record template
};
Data_.Add(temp);
}
}
}
      
var dataToExport = new RESULT
{
MainData_ = Data_
};
      
        var content = Api.TeamNetwork.ObjectAppExportService.ExecuteWordExportTemplate(userCommandContext.DocumentTemplateId,dataToExport,false);
      
var result = new UserCommandResult
        {
            Success = true,
            Commited = true,
            File=new UserCommandFileResult(){
                Content = content,
Name = "Word_Data.doc",
Type = "Word"
            },
            ResultType = UserCommandResultType.Notificate,
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "Generated the file"
                }
            }
        };
        return result;
    }
      
public static Decimal getterDC(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return 0;
}
var stringValue = getterSTR(key, dictionary);
if (stringValue != null && Decimal.TryParse(stringValue, out var result))
{
return result;
}
else
{
return 0;
}
}
      
public static DateTime? getterDT(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return null;
}
var stringValue = getterSTR(key, dictionary);
if (stringValue != null && DateTime.TryParse(stringValue, out var result))
{
return result.AddHours(5);
}
else
{
return null;
}
}
      
public static string getterSTR(string key, IDictionary<string, object> dictionary = null)
{
if (dictionary == null || key == null)
{
return null;
}
if (dictionary.TryGetValue(key, out var result))
{
if (result == null) return null;
return result.ToString();
}
else
{
return null;
}
}
      
public static IList getterListSTR(string key, IDictionary<string, object> dictionary = null)
{
var result = new List();
if (dictionary != null && key != null)
{
if (dictionary.TryGetValue(key, out var objectData))
{
var objectDataArray = objectData as object[];
foreach (var singlObject in objectDataArray)
{
if (singlObject == null) continue;
result.Add(singlObject.ToString());
}
}
}
return result;
}
      
public static IDictionary<string, object> GetData(string objectId = null)
{
if (objectId == null || objectId.Contains("account") || objectId == "tempID")
{
return null;
}
var container = Api.TeamNetwork.ObjectAppService.GetByObject(objectId);
var result = Api.TeamNetwork.ObjectService.GetWithAlias(container.Alias, objectId);
return result;
}
}
      
[Serializable]
public class MainData
{
public string Client { get; set; }
public string Contact { get; set; }
public string Phone { get; set; }
public string Email { get; set; }
public string Name { get; set; }
public decimal Total { get; set; }
public DateTime? Date { get; set; }
public string Status { get; set; }
}
      
public class RESULT
{
    public List MainData_ { get; set; }
}
```
**Note:**In the script above, the lines with the attribute and template system names are marked with comments. In these lines substitute the actual system names from your application.

================================================
FILE: 395. Version 4/399. How-Tos/1945-export_collections_images.md
================================================
---
title: Configuring Export Template for Several Collections and Images Using C#
kbId: 1945
---

# Configuring Export Template for Several Collections and Images Using C#

## Use Case

In addition to the standard export template feature, you can configure a custom data export using a C# script with more flexible data processing. For example, you can export several collections or multi-value attributes from a record.

In this article, we will create a Word export template file with two tables (from two collections) and several images (from a multi-value attribute).

## Prerequisites

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
|  | *Photo\_1\_Atr* | **Image** | Stores one or several images (**Store multiple values** box is checked). |
|  | *Table\_1\_Atr* | **Record** | Linked to the *Table\_1* record template and stores multiple values (a *collection*). |
|  | *Table\_2\_Atr* | **Record** | Linked to the *Table\_2* record template and stores multiple values (a *collection*). |
| *Table\_1* | *Faсtor* | **Record** | Linked to a record template, which has the *Title* text attribute. |
| *Parameter* | **Record** | Linked to a record template, which has the *Title* text attribute. |
| *Value* | **Number** | Stores a numeric value, e.g., order amount. |
| *Table\_2* | Destination | **Text** | Stores a business trip destination. |
| Order | **Text** | Stores an order number. |
| Date | **Date** | Stores an order date. |
| Responsible | Account | Stores a user account ID. |

## Instructions

1. Create an export template as shown below using the [template.docx](https://kb.cmwlab.com/file.php?id=171) attached below the article:

_![Example template](https://kb.cmwlab.com/assets/2021-12-15_08h18_25.png)_

**Note:** In the export template, the image field is placed inside a table to accommodate several images.

1. A button with the **Export record**   operation will be automatically created.
2. Open the **Export record**button properties.
3. On the **Script** tab, paste the script attached below the article ([script for export.cs](https://kb.cmwlab.com/file.php?id=182)).

### Script Syntax

- In lines 17–24, the `GetPropertyValues()` API function is used to query the database for specific attribute values. This function improves the script performance with large datasets.

  ```

  var data_ = Api.TeamNetwork.ObjectService.GetPropertyValues(
      userCommandContext.ObjectIds, // getting an array of one or multiple record IDs
      new[] {
         "Photo_1_Atr", // the system name of an Image attribute
         "Table_1_Atr", // the system name of a Record attribute
         "Table_2_Atr" // the system name of a Record attribute
      });
  Dictionary<string, object> data = data_.FirstOrDefault().Value;

  ```
- Lines 39–40 show how to get the linked template attribute values via the **record** attributes.

```

string Faсtor_ = getByRef("Title", getString("Faсtor", Table_Data)); // getting the "Title" attribute value by reference via the "Factor" record attribute
string Parameter_ = getByRef("Title", getString("Parameter", Table_Data)); // getting the "Title" attribute value by reference via the "Parameter" record attribute

```

- Lines 56 and 67 show how to get the **FullName** attribute value via an account attribute.
  ```

  var Responsible_ = Api.Base.AccountService.Get(getString("Responsible", Table_Data)); // getting the "Responsible" Account attribute value (account ID)
  ...
  Responsible = Responsible_.FullName, // getting the responsible person's full name

  ```
- Lines 173–178 and 185–190 show how to check the image format.
  ```

  if (FileName.EndsWith("png") || FileName.EndsWith("PNG") || FileName.EndsWith("jpeg") || FileName.EndsWith("jpg") || FileName.EndsWith("JPG"))
  {
  byte[] content = (Api.TeamNetwork.DocumentService.GetContent((string)result)).Data;
  listImages.Add(content);
  }

  ```

- Lines 232–258 define the data model:
  ```

  public class IMG
  {
      public byte[] Image_data { get; set; }
  }
  public class TBL_1
  {
      public string Factor { get; set; }
      public string Parameter { get; set; }
      public string Value { get; set; }
  }
  public class TBL_2
  {
      public string Destination { get; set; }
      public string Order { get; set; }
      public string Date { get; set; }
      public string Responsible { get; set; }
  }
  public class RESULT
  {
      public List<IMG> Photo_1 { get; set; }
      public List<TBL_1> Table_1 { get; set; }
      public List<TBL_2> Table_2 { get; set; }
  }
  ```

  **Note:** Define a unique class for each table in the export template.

## See Also

[Configure an Export Template with C# Data Processing](https://kb.comindware.ru/article.php?id=1943)

================================================
FILE: 395. Version 4/399. How-Tos/1947-qr_code_csharp_button.md
================================================
---
title: Generate a QR Code Using C# and a Third-Party Service on Button Click
kbId: 1947
---

# Generate a QR Code Using C# and a Third-Party Service on Button Click

## Use Case

Apart from using the built-in **QR code** attribute, you can generate a QR code using C# and a third-party service on a button click. You might want to do this to generate a special barcode or customize the QR code: change its size, color, image format or correction level, ad a logo overlay, etc.

In this article, we will configure a button to generate a 300x300px QR code pointing to [https://cmwlab.com](https://mycompany.com) via the `api.qrserver.com` service.

## Prerequisites

To proceed with the example, create the attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *QRCodes* | *QRinBase64* | **Text** | Select any **display format**.  .This attribute stores the generated QR code in the `base64` format. |
| *QRcodeImage* | **Text** | Select **HTML text** as the **display format**.  This attribute stores the QR code image and is placed on the form. |

## Instructions

1. In the *QRcodeImage* attribute properties, check the **Auto calculate** box and enter the following **Calculated value**:
   ```
   FORMAT("<img align='center' src='data:image/png;base64,{0}'</img>",LIST($QRinBase64))
   ```
2. In the *QRCodes* template, *c*reate a button with the following properties:
   - **Display name** — *Generate QR code*
   - **Operation** — **C# script**
   - **Operation context** — **Record**
   - **Operation result** — **Refresh data**

   On the **Script** tab, enter the following script:

   ```
   using System;
   using System.Collections.Generic;
   using System.Linq;
   using Comindware.Data.Entity;
   using Comindware.TeamNetwork.Api.Data.UserCommands;
   using Comindware.TeamNetwork.Api.Data;
   using RestSharp;

   class Script  
   {  
         public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)  
         {  
             ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;  
             byte[] AsBytes = new
             System.Net.WebClient().DownloadData
             ("https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://cmwlab.com" + userCommandContext.ObjectIds[0]);
   // 300x300 is desired QR code size
   // https://cmwlab.com is the URL to open upon scanning the QR-code
             string AsBase64String = Convert.ToBase64String(AsBytes);  
             var data = new Dictionary<string, object>
             {
                  { "QRinBase64", AsBase64String }
   // QRinBase64 is the system name of the attribute to store the QR code in base64 format  
              };  
              Api.TeamNetwork.ObjectService.EditWithAlias("QRCodes", userCommandContext.ObjectIds[0], data);
   // QRCodes is the system name of the record template where the button is located  
         var result = new UserCommandResult
         {  
           Success = true,  
           Commited = true,  
           Messages = new[]  
           {  
             new UserCommandMessage  
             {  
               Severity = SeverityLevel.Normal,  
               Text = "QR code was generated"
   // "QR code was generated" is the success message displayed upon generating the QR code  
             }  
            }  
         };  
     return result;  
       }
   }

   ```
3. In the *QRCodes* template, place the *QRcodeImage*attribute on a form.
4. Place the *Generate QR code* button on the form's toolbar.
5. Save the form.
6. Open or create a record in the *QRCodes* template.
7. Click the *Generate QR code* button: you should see the generated QR code on the form.

================================================
FILE: 395. Version 4/399. How-Tos/1955-import_excel_data.md
================================================
---
title: Import Data into Excel via API
kbId: 1955
---

# Import Data into Excel via API

## Use Case

Using the **CMW Platform** API, you can import the application data to Excel (via Power Query) or BI systems.

In this article, we will import the data from a record template into an Excel file using the **CMW Platform** API and the Power Query add-in.

## Instructions

### Obtaining the GET Request URL for a Template

1. Open your **{{ productName }}** instance website.
2. To open the API web interface, type `/docs` after the domain name in the browser address bar, for instance:
   `mycompany.com/docs`
3. Go to the **Solution API**section that lists all application templates.
4. Find the template you need by its system name and click it.
5. Select the **GET** method (without the `{id}` suffix) that returns all the records from the record template.
6. Click **Try it out**.
7. Copy the value in the **Request URL** field, for example:
   `https://mycompany.com/api/public/solution/Vehiclerequests`

_![Obtaining the template GET request URL](https://kb.cmwlab.com/assets/img_6442b00578cfd.png)_

**Note:** The **CMW Platform** API presents the data in JSON format.
### Importing Data to Excel

The Power Query add-in is built into Excel 2016 and above. For earlier versions of Excel, you need to [install it](https://support.microsoft.com/en-us/office/about-power-query-in-excel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a?redirectsourcepath=%252fru-ru%252foffice%252fpower-query-%2525e2%252580%252594-%2525d0%2525be%2525d0%2525b1%2525d0%2525b7%2525d0%2525be%2525d1%252580-%2525d0%2525b8-%2525d0%2525be%2525d0%2525b1%2525d1%252583%2525d1%252587%2525d0%2525b5%2525d0%2525bd%2525d0%2525b8%2525d0%2525b5-ed614c81-4b00-4291-bd3a-55d80767f81d).

1. On the **Data** tab in the ribbon, click **From Web**
2. In the **URL** field, paste the [**Request URL** you copied from the **CMW Platform** API](#RequestURL).

   ![Initializing the Power Query in Excel](https://kb.cmwlab.com/assets/img_6442afcc8b705.png)

   Initializing the Power Query in Excel
3. In the **Access Web content** window:
   - Select **Basic**.
   - Enter the **user name** and **password** of the account with permission to view the selected record template.
   - Click **Connect**.

     _![     Configuring the credentials for API access](https://kb.cmwlab.com/assets/img_6446481f27823.png)_
4. The received data appears in the **Power Query Editor** window.

   ![Power Query Editor with the imported data](https://kb.cmwlab.com/assets/img_644649e72f2d0.png)

   Power Query Editor with the imported data
5. Click **To Table** in the ribbon. Click **OK**in the **To Table** window .

   ![Configuring the query table](https://kb.cmwlab.com/assets/img_64464c555a6b4.png)

   Configuring the query table
6. Expand the list of all record template attributes and select the attributes to load in the table.

   _![   Configuring the columns](https://kb.cmwlab.com/assets/img_64464c3c94675.png)_
7. Click **Close & Load** in the ribbon to import the data into the Excel spreadsheet.

   ![Loading the query table to the Excel spreadsheet](https://kb.cmwlab.com/assets/img_64464d4357314.png)

   *Loading the query table to the Excel spreadsheet*
8. The data will appear in the Excel spreadsheet as shown below.

   ![A query table imported to the Excel spreadsheet](https://kb.cmwlab.com/assets/img_64464d8ecaf5a.png)

   A query table imported to the Excel spreadsheet

================================================
FILE: 395. Version 4/399. How-Tos/1965-task_notify_change_text.md
================================================
---
title: Customizing Notification E-mail Message
kbId: 1965
---

# Customizing Notification E-mail Message

## Use Case

The **CMW Platform** can send users notifications about the tasks assigned to them.

You can use the [default task notification e-mail](#mcetoc_1gtl1ap9e2) or create a [custom task notification e-mail](#mcetoc_1gtl9cege4).

## Enabling Task Notification Sending

1. Set up **E-mail sending** connection under **E-mail connections** in **Administration – Connections**.
2. Check the **Use by default box** in the **E-mail sending** connection properties to use it for task notification sending.
3. Check the **Enable task notifications** box in **Administration –** **Global configuration**.

## Default Task Notification E-mail

The default new task notification e-mail is shown below and contains the following details:

- *Subject* *line* — the task type and title.
- *Task title*(e.g., *Approve Capex Request*) — set on the **Advanced** tab of the **user task** properties on the process diagram. The task title is a hyperlink to the **user task form**.
- *Record title*(e.g., *item 9794*) — the value of the attribute **used as a record title** of the record linked to the process instance. The record title is a hyperlink to the record template **default form**.
- *Task link* — generated automatically. It leads to the **user task form**, defined on the process diagram.
- *Deadline*(e.g., *Dec 17*) — calculated from the **Duration** value on the **Advanced** tab of the **user task** properties on the process diagram.
- *Process name*(e.g., *Capex Approval process*) — set in the **process template**properties.

_![Default new task e-mail notification](https://kb.cmwlab.com/assets/img_6433b85fce381.png)_

To open the task form, click ***Go to the task***or the task title (*Approve Capex Request* in the illustration).

To open the record form linked to the task, click the record title (*item 9794* in the illustration).

## Customizing the Task Notification E-mail

To customize the subject or body of the task notification e-mail (e.g., to include specific information):

1. Go to **Administration — Communication routes**.
2. Create a new **Task notification** communication route under **System connections**.
3. In properties of the **Task notification** communication route:
   - On the **Message attributes**tab, configure the attributes to use in the e-mail.
   - On the **Message properties** tab, configure the e-mail **Subject**and **Body** using the attributes from the **Message attributes**tab.
4. Open the **user task** properties on the process diagram.
   - On the **Message data** tab:
     - Specify the communication route created in Step 2.
     - Configure the attribute values to substitute in the task notification e-mail (configured in Step 3).
5. Publish the process diagram.
6. Test the process task notifications.

================================================
FILE: 395. Version 4/399. How-Tos/1971-transfer_solution_settings.md
================================================
---
title: Transferring business solutions
kbId: 1971
---

# Transferring business solutions

When building a business solution, it is a good practice to create several instances for different purposes: development instance, test instance, production instance; and then transferring solution settings between instances. Business solution settings can be transferred in 4 ways:

**1.** Transferring a database.

In this case, all the settings of the instance, as well as all the data, will be transferred.

**2.** Pulling business application configuration from Git.

**3.** Transferring all the settings manually.

Manual transfer implies a step-by-step transfer of data and settings between instances manually, that is, a new business application is configured from scratch. It is recommended to use this method with a small amount of data.

**4.** Export / import of a business application configuration (see the article [Exporting and Importing Applications](https://kb.comindware.ru/article.php?id=1973)).

This method is limited to transferring records in business application templates, all the settings and data will be transferred, with the exception of template records. This method is characterized by a fast speed of data transfer.

================================================
FILE: 395. Version 4/399. How-Tos/1973-import_excel_data.md
================================================
---
title: Exporting and Importing Applications
kbId: 1973
---

# Exporting and Importing Applications

## Use Case

You can export and import the applications to transfer your business solution configuration between the **CMW Platform** instances. For example, you may develop and test the application on a development server and then transfer it to the production server.

## Exporting an Application

The application configuration is exported as a `.CTF` file. Export a separate file for each application.

1. Open the application you want to export.
2. From the application ***Administration*** page, go to ***Version control***. 

   _![   Going to the application Version control page](https://kb.cmwlab.com/assets/img_64479750e2762.png)_
3. Click the down arrow *‌* next to the **Git version control** heading and select **Manual version control** in the dropdown.

   _![   Going to the application Manual version control page](https://kb.cmwlab.com/assets/img_64479780726bb.png)_
4. Click ***Export***.
5. The browser will download the `.CTF` file.
6. If a file save prompt appears, enter the `.CTF` file name and choose the location to save it.

   _![   Exporting the CTF file with application configuration](https://kb.cmwlab.com/assets/img_644797a7860b6.png)_

## Importing an Application

1. Open the **CMW Platform** instance where you want to import the application.
2. Create a new application or open an existing one.
   Notes
   - The target application system name ***must*** be the same as the imported application system name.
   - Application import does not affect the existing data: it overwrites the application configuration.
3. From the application ***Administration*** page, go to ***Version control***.

   _![   Going to the application Version control page](https://kb.cmwlab.com/assets/img_64479750e2762.png)_
4. Click the down arrow *‌* next to the **Git version control** heading and select **Manual version control** in the dropdown.

   _![   Going to the application Manual version control page](https://kb.cmwlab.com/assets/img_64479780726bb.png)_
5. Upload the `.CTF` file to the Select file field.
6. Click **Validate**.
7. Make sure the **Validation result**  window does not report errors or conflicts.   

   _![   Successful CTF file validation result](https://kb.cmwlab.com/assets/img_6447a597297e0.png)_
8. Configure the import:

   - **Publish process diagrams after import** — check this box to publish all imported process diagrams.
   - **Application component activity** — select an action to activate or deactivate the process elements, scenarios, and communication routes upon import:
     - **Import the configuration** — activate the imported components with the **Active** status.
     - **Use current configuration**— keep the current component statuses.
     - **Activate all**— activate all components.
     - **Pause all** — deactivate all components.
9. Click **Import**.

   _![   Configuring the application import](https://kb.cmwlab.com/assets/img_64479d972de9e.png)_

================================================
FILE: 395. Version 4/399. How-Tos/1983-global_notifications_setup.md
================================================
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

================================================
FILE: 395. Version 4/399. How-Tos/1985-button_display_formula.md
================================================
---
title: Configuring Button Display Condition with Formula
kbId: 1985
---

# Configuring Button Display Condition with Formula

## Use Case

You can show or hide a button depending on the application context. For this, define the button **Display condition** using a **formula** or an **N3 expression.**

In this article, we will create and configure the **Add new item**button to be visible only when the *Request* *Status* is *New*or *AddedToCart*.

## Prerequisites

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Request* | *Status* | **Record** | The *Status* attribute is linked to the *Request\_status* template. |
| *Request\_status* | *Status\_code* | **Text** | The *Request\_status* template contains records with the following *Status\_code* values:   - *New* - *AddedToCart* - *Pending* |

## Instructions

1. In the *Request* record template, go to the ***Buttons*** tab.
2. Create the **Add new item** button.
3. On the ***Display condition*** tab enter the [**formula**](#mcetoc_1gtntho192):
   ```
   OR($Status->Status_code == "New",$Status->Status_code == "AddedToCart")
   ```
4. Click **Save** to save the button.
5. Place the **Add new item** button on the default form toolbar in the *Request* record template.
6. Test the resulting button:
   - Create a *Request* with the *New* or *AddedToCart*status: the **Add new item** button should be visible.
   - Create a *Request* with the *Pending*status: the **Add new item** button should not appear.

### Formula Syntax

| Element | Description |
| --- | --- |
| `OR()` | This function takes two arguments and returns `true` if any of the arguments is `true`. In our case, we evaluate if the *Status\_code* attribute value equals *New*or *AddedToCart*. |
| `$` | This prefix refers to an attribute in the current record context. |
| `->` | This operator refers to an attribute of the linked *Request\_status* template. |

================================================
FILE: 395. Version 4/399. How-Tos/1987-form_rule_hide_field.md
================================================
---
title: Configuring Form Rule Using Formula
kbId: 1987
---

# Configuring Form Rule Using Formula

## Use Case

In the **CMW Platform**, you can define a set of rules for any form to control its element behavior.

Each rule can include several conditional actions:

- Set field values
- Show field validation warnings and error messages
- Change element access mode: require entry, allow entry, read-only
- Hide elements

In this article, we will create a form rule to hide the *Recipient* field from the form when this field is empty and the *Enter new customer details* box is checked.

## Prerequisites

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute and field display name (system name)** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Request* | *Recipient (recipient)* | **Record** | Place this attribute on the form as the *Recipient* field. |
| *Enter new customer details (create\_flag)* | **Boolean** | Place this attribute on the form as the *Enter new customer details* checkbox. |

 
## Instructions

1. In the *Request* template, open the default form.
2. Open the ***Form rules*** designer using the dropdown next to the form heading.
3. Add a rule and an action to the rule.
4. Select the action to display the **Action properties** pane.
5. From the **Form element** dropdown, select the *Recipient* field**.**
6. From the **Action** dropdown, select **Change access****.**
7. From the **New value**dropdown, select **Hide****.**
8. In the **Execution condition** field, enter the [**formula**](#mcetoc_1gtqijebq0):
   ```
   AND(EMPTY($recipient),$create_flag == true)
   ```
9. Click ***Save***.

### Formula Syntax

| Element | Description |
| --- | --- |
| `AND()` | This function takes two arguments and returns `true` if both arguments resolve to `true`, i.e., when the *Recipient* field is empty and the *Enter new customer details* box is checked. |
| `$` | This prefix refers to an attribute in the current record context. |
| `EMPTY()` | This function returns `true` if its argument has an empty value, i.e., when the *Recipient* attribute value is null. |

## See Also

[Configuring Dynamic Field Display Using a Form Rule](https://kb.comindware.ru/article.php?id=2070)

================================================
FILE: 395. Version 4/399. How-Tos/1989-record_many_many.md
================================================
---
title: Configuring Many-To-Many Relationship
kbId: 1989
---

# Configuring Many-To-Many Relationship

## Use Case

In the **CMW Platform**, you can define a many-to-many relationship between two record templates.

A many-to-many relationship links several records from one template to several records in another template.

For example, several employees may work on a project, and each employee can work on several projects.

In this article, we will configure a many-to-many relationship between the *Projects* and *Employees* templates using two different approaches: a direct link and an intermediate template.

## Prerequisites

To proceed with the example, create the templates as shown in the table below:

| **Record template** | **Description** |
| --- | --- |
| *Projects* | Stores the project records. |
| *Employees* | Stores the employee records. |

## Instructions

### Link the Templates Directly

1. In the *Projects*template, create the *Project Employees* attribute:
   - **Data type** — **Record**.
   - **System name**— *Project\_employees*.
   - **Linked template** — *Employees*.
   - Store multiple values — checked.
   - **Attribute interlinking** — **With a new one**.
     - **New attribute properteies**:
       - **Name** — *Employee Projects*.
       - **System name** — *Employee\_projects*.
       - Store multiple values — checked.

_![Configuring a many-to-many relationship with direct template linking](https://kb.cmwlab.com/assets/img_643e56f571d70.png)_

**Note**

This approach has certain limitations:

- You cant store project-specific employee details, such as their project role, rate, or workload percentage.
- You cant process or filter the interlinked attribute values in some contexts.
### Link the Templates via an Intermediate Template

1. Create the *Projects and Employees*record template.
2. In the *Projects and Employees*template, create the *Project* attribute:
   - **Data type** — **Record**.
   - **System name**— *Project*.
   - **Linked template** — *Projects*.
   - Store multiple values — unchecked.
   - **Attribute interlinking** — **With a new one**.
     - **New attribute properteies**:
       - **Name** — *Employee Link*.
       - **System name** — *Employee\_link*.
       - Store multiple values — checked.
3. In the *Projects and Employees*template, create the *Employee*attribute:
   - **Data type** — **Record**.
   - **System name**— *Employee*.
   - **Linked template** — *Employees*.
   - Store multiple values — unchecked.
   - **Attribute interlinking** — **With a new one**.
     - **New attribute properteies**:
       - **Name** — *Project Link*.
       - **System name** — *Project\_link*.
       - Store multiple values — checked.

**Note**

Using this approach, you can store project-specific employee data in the *Projects and Employees*template, such as time spent on the project, employee role, payment rate, etc.

================================================
FILE: 395. Version 4/399. How-Tos/1991-calculated_attribute_formula.md
================================================
---
title: Configuring a Calculated Attribute with a Formula
kbId: 1991
---

# Configuring a Calculated Attribute with a Formula

## Use Case

The **CMW Platform** can calculate an attribute value on the fly (without storing it in the database) using a **formula**, **N3** expression, **DMN** table, or another **attribute**.

In this article, we will configure the automatic client assignment for the currently logged-in user.

## Prerequisites

In our example, we have a database of clients, company managers, and requests. A client is attached to each manager. So, we can automatically assign a client when the manager creates a request.

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Request* | *ClientForCurrentUser* | **Record** | The *ClientForCurrentUser* attribute is linked to the *Clients* template and calculated based on the data stored in the *Contact\_persons*template. |
| *Contact\_persons* | *Client* | **Record** | The *Client* attribute is linked to the *Clients* template. |
| *Manager* | **Account** | The *Manager* attribute stores the manager account ID. |
| *Clients* | *Name* | **Text** | The *Clients* template contains the client records. The *Name* attribute stores the client name. |

## Instructions

1. In the *Request* template, open the *ClientForCurrentUser* attribute.
2. Check the **Calculate using an expression** box
3. In the **Calculated value** field, enter the [**formula**](#mcetoc_1gto5h8ao2):
   ```
   from a in db->Contact_persons where EQUALS(a->Manager,USER()) select a->Client->name
   ```
4. Click **Save** to save the attribute.

### Formula Syntax

| Element | Description |
| --- | --- |
| `from a in db->Contact_persons` | `from` operator defines the data source:   - Declares a local variable: **`a`** - Declares the *Contact\_persons* template as the data source: `in db->Contact_persons` - Collects all records from the *Contact\_persons* template to the variable **`a`** |
| `where EQUALS(a>Manager,USER())` | `where` operator defines the data selection condition:   - `USER()` function returns the current user ID. - `EQUALS()` function returns `true` if the *Manager*attribute value in a *Contact\_persons* record equals the current user ID. |
| `select a->Client->Name` | `select` operator collects the entities matching the selection condition:   - Returns an array of the *Name* attribute values from the *Clients* records that correspond to the current user. |

================================================
FILE: 395. Version 4/399. How-Tos/1993-change_process_real_time.md
================================================
---
title: Making changes to a workflow in real time
kbId: 1993
---

# Making changes to a workflow in real time

Over time, your company may need to adjust previously configured business processes. This could be due to a change in company structure, industry standards, or business requirements. One way or another, you need to promptly make the required changes to the processes. A key benefit of the **CMW Platform** is the ability to change your workflow on the fly.

Thanks to the Elastic Data technology, you don't need to have programming skills and special knowledge to do this. You can simply go into the workflow settings and change them.

If your business process has become more complex, for example, another department (a group of employees) has been added or a certain role has to perform a new task, you can easily add the necessary steps and transitions, as well as delete them with one click.

To do this, go to the settings of the required process template and open the «***Diagram***» tab. Here you can adjust your business process: add and remove steps, change responsible persons and deadlines, indicate possible scenarios for token movement, and much more.

_![«Diagram» tab](https://kb.cmwlab.com/assets/2021-12-29_09h00_24.png)_

Then click the «***Edit***» button to enable the ability to make changes. The next step is, in fact, making changes to the executable process. After all the necessary changes have been made, click the «***Publish***» button and you will have two options: «***Change current version***» and «***Create new version***».

_![Choosing publishing option](https://kb.cmwlab.com/assets/2021-12-29_09h04_36.png)_

When you change the current version, the new diagram will be applied to the already running process instances from the previous version. It is important to consider the position of tokens in running instances. Tokens will be moved to their previous positions on the diagram (position is the system name of the process element on which the token is located). Accordingly, tokens for which no previous positions will be found will be deleted. The missing tokens will need to be manually placed using the token management feature in each process instance.

When you choose to create a new version, all new instances will be launched according to the new version, and the process instances launched according to the old version of the process diagram will be finalized according to their version.

**Diagram versioning**

In addition, **CMW Platform** supports versioning of process diagrams, which means that every published version is saved in the system. If you need to restore any of the versions, just click «***Select version***» in the ribbon, double-click on the required version and click «***Edit***» and then «***Publish***».

_![Selecting a version](https://kb.cmwlab.com/assets/2021-12-29_09h10_17.png)_

================================================
FILE: 395. Version 4/399. How-Tos/1997-import_excel_data.md
================================================
---
title: Importing Linked Records From an Excel Spreadsheet
kbId: 1997
---

# Importing Linked Records From an Excel Spreadsheet

## Use Case

In the **CMW Platform,**you can import data to a record template and link the imported records to the records in other templates.

In this article, we will import an Excel sheet containing several clients' requests and link the imported requests to the corresponding client records.

## Prerequisites

To link the records imported from an Excel spreadsheet to the records in another template, you must specify the linked records' key values in the spreadsheet. As the key values, specify the values of the **ID** system attribute or an attribute **used as a record title**.

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template** | **Attribute name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Clients* | *Client requests* | **Record** | Linked to the *Requests* template, the **Store multiple values** box is checked.  This *Client requests*attribute is placed as a table on the *Client* form. |
| *Name* | **Text** | The **Use as record title** box is checked for the *Name*attribute.  The *Clients* template contains two records with the following *Name* attribute values: *Client A* and *Client B*.  The *Name* attribute values will be used as the key values for Excel data import. |
| *Requests* | *Client* | **Record** | Linked to the *Clients* template. |
| *Name* | **Text** | Stores the request name. |
| *Sum* | **Number** | Stores the request amount. |

## Instructions

1. Create the Excel spreadsheet to import, as shown below. In the *Client* column, specify the *Name* attribute values stored in the *Clients* template: *Client A* or *Client B*.   These are the key values to link the *Clients* template records with the *Requests* template records. 

   ![The Excel spreadsheet iwht clients' requests to import](https://kb.cmwlab.com/assets/2021-12-30_14h20_56.png)

   The Excel spreadsheet with clients' requests to import
2. Open the *Requests* record template.
3. Go to the **Import** tab.
4. Load the Excel file to import.
5. In the **Data mapping** section, map the spreadsheet columns to the *Requests* template attributes:
   - Map the *Client* column to the Client attribute and specify ***name***as the value **format**  .
   - Map the *Name* column to the *Name* attribute.
   - Map the *Sum* column to the *Sum* attribute and specify ***currency*** as the value **format**.
6. Click **Upload** to import the data.

   ![Mapping the imported Excel spreadsheet columns to the record template attributes ](https://kb.cmwlab.com/assets/img_64468c71cc130.png)

   Mapping the imported Excel spreadsheet columns to the record template attributes
7. The imported requests will appear in the *Requests* record template, each linked to its client.

   ![Imported records in the Requests template](https://kb.cmwlab.com/assets/img_64468946eea69.png)

   Imported records in the Requests template
8. Open the *Client A* record.
9. In the *Client requests* table, you should see the imported requests for *Client A.*

   ![The table of requests linked to the client record](https://kb.cmwlab.com/assets/img_64468af96d1f6.png)

   The table of requests linked to the client record

================================================
FILE: 395. Version 4/399. How-Tos/1999-list_color_indicator.md
================================================
---
title: Configuring Color Indicator
kbId: 1999
---

# Configuring Color Indicator

## Use Case

In some cases, you might want to display a color indicator in a field to quickly understand whether a date has passed, a status has changed, a deadline is overdue, etc. To achieve this, use an HTML text attribute that changes its formatting conditionally.

In this article, we will create an indicator that will be red when the actual project completion date is past the planned completion date, or green otherwise.

## Prerequisites

To proceed with the example, create the attributes as shown in the table below:

| **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- |
| *Actual\_date* | **Date & time** | The actual project completion date. |
| *Planned\_date* | **Date & time** | The planned project completion date. |

## Instructions

1. Create a new **Text** attribute *Overdue indicator*:
   - **Display format** — **HTML text**
   - **Calculate using an expression** — checked.
2. In the **Calculated value**, enter the **formula**:

   | `IF(GREATEREQ($Actual_date, $Planned_date),`  `"<span style='color:#B22222; font-size: 200%; text-shadow: 0 0 1px black;`  `position: absolute; top:0px;'> ● </span>",`  `"<span style='color:#45A521; font-size: 200%; text-shadow: 0 0 1px black;`  `position: absolute; top:0px;'> ● </span>"`  `)` |
   | --- |

   Note: If you export this value to an Excel file, it will be displayed as unformatted HTML code. To export an HTML-formatted value to Excel, you need to reformat it using C#.
3. Place the *Overdue indicator*attribute on a form or in a table.

### Formula Syntax

| Element | Description |
| --- | --- |
| `IF(Argument1, Argument2, Argument3)` | `IF()` function takes three arguments. If `Argument1` resolves to `true`, it returns `Argument2`. Otherwise, it returns `Argument3`. |
| `GREATEREQ($Actual_date, $Planned_date)` | `Argument1` — condition. The `GREATEREQ()` function returns `true`if `Actual_date` is greater than or equal to the `Planned_date`. |
| `$` | The `$` prefix refers to an attribute in the current record context. |
| `"<span style = 'color: #B22222; font-size: 200%; text-shadow: 0 0 1px black; position: absolute; top: 0px;'> ● </span>"` | `Argument2` — red indicator HTML code:  ●. The `color: #B22222` CSS statement sets red color. Other CSS statements define the indicator size and position. |
| `"<span style = 'color: #45A521; font-size: 200%; text-shadow: 0 0 1px black; position: absolute; top: 0px;'> ● </span>"` | `Argument3` — green indicator HTML code:  ●. The `color: #45A521`CSS statement sets green color. Other CSS statements define the indicator size and position. |

## See Also

[Configuring Conditional Coloring of an Attribute Value](https://kb.comindware.ru/article.php?id=2009)

================================================
FILE: 395. Version 4/399. How-Tos/2001-receive_mail.md
================================================
---
title: Configuring E-mail Receiving
kbId: 2001
---

# Configuring E-mail Receiving

## Use Case

The **CMW Platform** can send and receive e-mail messages with any data: requests, inquiries, etc.

In this article, we will set up the e-mail connection and communication route to receive and parse requests in a business process.

## Instructions

1. Create a new **E-mail receiving** connection. Specify the e-mail server and account to receive the requests.
   **Note:** Each unread message in this e-mail account will be processed and marked as read.
2. Create a new **Incoming messages** communication route.
   - On the **Main properties** tab:
     - Select the **Connection**, created in Step 1.
     - Select a **Process** to execute upon receiving an e-mail message.
       - To use one e-mail account for one request type (e.g., new requests only), specify the corresponding business process.
       - To use one e-mail account for different request types or subsequent responses, create an intermediate process that will handle them.
     - Based on your use case select the **Route target**:
       - To process all messages as new requests, select **New process instance**.
       - To parse subsequent responses for existing requests and send the data further to a pending process, select **Existing process instance**.

         ![Example of an intermediate process to handle new requests and subsequent responses](https://kb.cmwlab.com/assets/img_643d277cf0e5f.png)

         Example of an intermediate process to handle different new requests and subsequent responses
   - On the **Message attributes** tab, specify the attributes to store the incoming e-mail message elements:
     - **From address**
     - **From name**
     - **To address**
     - **To name**
     - **Subject**
     - **Body**
     - **CC address**
     - **CC name**
     - **BCC address**
     - **BCC name**
     - ******Attachments******

_![Mapping e-mail elements to the CMW Platform attributes](https://kb.cmwlab.com/assets/img_643d28bfee1f7.png)_

1. On the process diagram, create or select a **Receive message start event**.
   - On the **Advanced** tab, select the communication route created in [Step 2](#STEP2).
   - On the **Input mapping** tab, map the record template attributes to the e-mail message attributes.

_![Mapping the record template attributes to the e-mail message attributes](https://kb.cmwlab.com/assets/img_643d2ac91896f.png)_

**Note:** Using the CMW formula or N3 language expressions and scenarios, you might need to parse the e-mail subject line, body, or other elements (e.g., to determine the request type or decide if the message is a new request or a response regarding an existing one).

================================================
FILE: 395. Version 4/399. How-Tos/2003-combine_values.md
================================================
---
title: Combine Several Values Into a Record Title
kbId: 2003
---

# Combine Several Values Into a Record Title

## Use Case

You can calculate an attribute value ​​from several values and use it as the record title. This can be useful for more convenient searching, composing user-friendly titles for records, tasks and reference fields, and other purposes.

In this article, we will create the *Case name* attribute to combine three other attribute values and use it as a title for the records and record links.

## Instructions

1. Create a **Text** attribute *Case name*.
2. Check ***Use as record title*** and ***Calculate using an expression*****.**
3. In the ***Calculated value***, enter the [**formula**](#mcetoc_1gtntho192):
   ```
   FORMAT("{0} / {1} / {2}",LIST($CityRef->Name,$Applicant,$StatusRef->Name))
   ```
4. Save the attribute.
5. Create or open a record and fill in the fields for the attributes passed to the `LIST()` function in Step 3.
6. The calculated composite value of the *Case name* attribute should appear in the form header.

_![A form heading showing the calculated attribute value](https://kb.cmwlab.com/assets/img_64341fdbbdd83.png)_

### Formula Syntax

| Element | Description |
| --- | --- |
| `FORMAT(originalString, placeholderArray)` | This function takes a string and array as arguments, replaces the placeholders in the string with the array values, and returns the resulting string. |
| `LIST(argument1, argument2, ... argumentN)` | This function takes several values (e.g., *City name, Applicant's name*, and *Case status*) and returns them as an array. |
| `"{0} / {1} / {2}"` | The string to parse. In addition to placeholders, it may contain arbitrary text, numbers, symbols, etc. |
| `{0}, {1}, ... {N}` | These placeholders are replaced with the array values returned by the `LIST()` function. The placeholders are numbered from 0. |

Note

- When you pass a Date & time or Duration attribute value to the `FORMAT()` function, it ignores the configured attribute display format. For example, any Date & time attribute value is output as *MM/DD/YY HH:MM:SS*.
- You can pass any values to the `LIST()` function, not necessarily attribute references. For example, you could pass the current user's full name as a second argument:
  `LIST($CityName,USER()->fullName,$StatusName)`.

================================================
FILE: 395. Version 4/399. How-Tos/2005-attribute_date_time_display_config.md
================================================
---
title: Working with Date &amp; time attribute
kbId: 2005
---

# Working with Date &amp; time attribute

The attribute with the «Date & time» data type is used in **CMW Platform** to record and display data in date and time format.

The attribute with the «Date & time» data type is stored in the database in the «UTC 0» time zone:

```
"op.117": "2020-12-10T07:45:00Z"
```

On the form or on the table, it is displayed in the server time zone, which is specified in the global configuration:

_![Defining the time zone](https://kb.cmwlab.com/assets/2022-02-10_14h05_00.png)_

When **importing** an attribute of the «Date & time» data type, it is loaded into the database in «UTC 0» time zone, but displayed in the time zone specified in the global configuration.

For example, the server time zone is UTC+3, so if you upload from a file to the system with the following date and time: *03.12.2020 17:00*, in the system in the attribute of the «Date & time» data type you will see the same time, but in the database it will be stored as follows: *03.12.2020 14:00*.

When **exporting** an attribute of the «Date & time» data type, it is unloaded in the server time zone specified in the global configuration.

For example, if you export the attribute of the «Date & time» data type with the value «*12/03/2020 17:00*» to Excel, then this field will store exactly the same time as in the system.

When **changing the display format** of the attribute of the «Date & time» data type from «*dd.MM.YYYY hh: mm*» to the display format «*dd.MM.YYYY*», hours and minutes are reset to the zero time zone to avoid incorrect time display and display errors when importing and exporting.

**Note :** the IANA library is used to determine the time zones in which to store information in the database.

================================================
FILE: 395. Version 4/399. How-Tos/2007-solution_setup_recommendations.md
================================================
---
title: Recommendations for setting up a business solution
kbId: 2007
---

# Recommendations for setting up a business solution

After installing **CMW Platform** and logging into the product for the first time, the administrator is granted access to all sections of the system.

Setting up a business solution starts with a business application. A business application is a collection of related sections, settings, and data, and is also the main element for transferring configurations between environments.

By default, a system application «*System business app*» is created in the new product, where all sections for configuring the system are located. It can be used to create a specific business solution, such as Contract approval, CRM, HR or MRO, but it is recommended that you create your own business applications for each specific solution.

Before you start setting up a business solution, you need a basic understanding of the following points (we use CRM system as an example):

- List of information (master data/reference information) required and used during work:
  - Counterparties;
  - Contact persons;
  - Inquiries;
  - Contracts;
  - etc.
- List of processes for automation:
  - Inquiry processing;
  - Formation of a commercial offer;
  - Contract approval;
  - etc.
- List of roles involved in the processes:
  - Sales manager;
  - Head of Sales;
  - CFO
  - etc.
- List of required reports:
  - Sales plan;
  - Managers’ workload;
  - etc.

When the list of all the necessary data, processes, roles, etc. is defined, you can proceed to creating and configuring record templates, processes, roles, etc.

For visual modeling, you can use the following diagrams:

- Business capabilities diagram;
- Class diagram;
- Data model diagram.

**Note :** keep in mind that one record template can only be stored in one business application. To transfer an record template to another business application, open the record template settings and on the «***Properties***» tab, click the «*Change the business application*» button.

================================================
FILE: 395. Version 4/399. How-Tos/2009-attr_value_color.md
================================================
---
title: Configuring Conditional Coloring of an Attribute Value
kbId: 2009
---

# Configuring Conditional Coloring of an Attribute Value

## Use Case

In the **CMW Platform**, the applied theme defines display formatting for all fields. You cannot specify formatting for the individual fields. But you can customize the font, color, or other formatting properties for the **Text** attribute with the **HTML text** display format. The **HTML text** attribute value is displayed with the configured HTML formatting in tables and forms.

In this article, we will conditionally color the task status: when the task is overdue, highlight the status in red; otherwise highlight the status in green.

## Prerequisites

To proceed with the example, create the attributes as shown in the table below:

| **Record template system name** | **Attribute system name** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Statuses* | *Name* | **Text** | The *Name* attribute stores a status name.  The *Statuses* template contains two records:   - *Name* = Overdue - *Name* = Complete |
| *Tasks* | *StatusRef* | **Record** | The *StatusRef* attribute is linked to the *Statuses* template *.* |

## Instructions

1. In the *Tasks* template, create the *Colored Status* **Text** attribute with the following properties:
   - **Display format** —  **HTML text**
   - **Calculate using an expression** — checked
   - **Calculated value** — [**formula**](#mcetoc_1gtntho192):
     ```
     FORMAT(
     IF(EQUALS($StatusRef->Name,"Overdue"),
     "<p><span style='color:#000000'><span style='background-color:#f02626'>{0}</span></span></p>",
     "<p><span style='color:#000000'><span style='background-color:#3ee028'>{0}</span></span></p>"),
     LIST($StatusRef->Name))
     ```
2. Place the *Colored Status* attribute on a form or table. The attribute value will be colored depending on the status name.

### Formula Syntax

| Element | Description |
| --- | --- |
| `FORMAT()` | This function takes a string and array as arguments, replaces the placeholders in the string with the array values, and returns the resulting string. Placeholders are numbered from 0. |
| `IF(Argument1, Argument2, Argument3)` | This function takes three arguments. If `Argument1` resolves to `true`, it returns `Argument2`. Otherwise, it returns `Argument3`. |
| `EQUALS($StatusRef->Name,"Overdue")` | `Argument1` — condition. The `EQUALS``()` function returns `true` if the `$``StatusRef->Name` value is `Overdue`. |
| `$StatusRef` | The `$` prefix refers to the *StatusRef*attribute in the current record context. |
| `->Name` | The `->`operator refers to the *Name* attribute of the linked *Statuses* template. |
| `"<p><span style='color:#000000'><span style='background-color:#f02626'>{0}</span></span></p>"` | `Argument2` — red status HTML code. The `color:#000000` CSS statement sets the text color to white. The `background-color``: #f02626` statement sets the background color to red. |
| `"<p><span style='color:#000000'><span style='background-color:#3ee028'>{0}</span></span></p>"` | `Argument3` — green status HTML code. The `background-color``:#3ee028` statement sets the background color to green. |
| `{0}` | This placeholder is replaced with the array value returned by the `LIST()` function. |
| `LIST($StatusRef->Name)` | This function takes the `$StatusRef->Name` value and returns it as an array of one element. You have to use the `LIST()` function because the `FORMAT()` function only accepts an array of placeholder values and will not accept a single value. |

**Note:** The *Status* attribute value will not be colored, but the calculated *Colored Status*attribute.

**Tip:** You can customize the **HTML text** using most HTML features: text or background color, font family and size, HTML tags, etc.

## See Also

[Configuring Color Indicator](https://kb.comindware.ru/article.php?id=1999)

================================================
FILE: 395. Version 4/399. How-Tos/2020-attr_record_filter.md
================================================
---
title: Configuring Filters for Record Attributes
kbId: 2020
---

# Configuring Filters for Record Attributes

## Use Case

The **CMW Platform** allows restricting the field value display and selection using the **Filter** property in the form designer.

The field **Filter** property is available for the following attribute types:

1. **Account** — filter accounts to display.
2. **Record** — filter records to display.
3. **Record** with multiple values:
   - filter records to display
   - filter records to add

## Instructions

To configure a filter for a field on a form:

1. Select a field on the form to display its **Field properties** pane.
2. In the **Filter** property, define the filter using one of the following options:
   - **Attribute** — select an attribute from the dropdown. The values of this attribute will appear in the form field.
   - **Formula** — write an expression in the CMW formula language. The values returned by the formula ​​will appear in the form field.
   - **N3** — write an expression in the N3 language. The values returned by the expression will appear in the form field.
   - **DMN** — create a table in the DMN notation. The table output values will appear in the form field.

**Tip:** You can configure different filters for different fields on each form.

## See Also

[Configuring Context-Dependent Filter for Record Attribute](https://kb.comindware.ru/article.php?id=2022)

================================================
FILE: 395. Version 4/399. How-Tos/2022-attr_record_account_filter.md
================================================
---
title: Configuring Context-Dependent Filter for Record Attribute
kbId: 2022
---

# Configuring Context-Dependent Filter for Record Attribute

## Use Case

In the **CMW Platform**, a **Record** attribute is used to select values from another record template.

By default, a **Record** field lists all records linked to the attribute. But in some scenarios, you might want to show only certain records.

To limit the record set displayed in the **Record** field, use the **Filter** field in the **Field properties** pane of the form designer.

In this article, we will configure a city selector dropdown to display the cities from the country where an employee plans to travel.

## Prerequisites

In our example, we have a database of countries, cities, and travel requests. When creating a travel request, an employee selects a destination city. Instead of displaying all the cities from all the countries, we will filter the cities list by the selected country of the business trip.

To proceed with the example, create the templates and attributes as shown in the table below:

| **Record template display name (system name)** | **Attribute display name (system name)** | **Attribute type** | **Description** |
| --- | --- | --- | --- |
| *Countries (countries)* | *Title (title)* | **Text** | Stores the country name. |
| *Cities of the country (cities\_of\_the\_country)* | **Record** | The  *cities\_of\_the\_country*attribute is linked to the *Cities* template.  The  **Store multiple values** box is checked. |
| *Cities (cities)* | *Title (title)* | **Text** | Stores the city name. |
| *Country (country)* | **Record** | The *country* attribute is linked to the *Countries* template. |
| *Travel requests (travel\_requests)* | *Title (title)* | **Text** | Stores the request name. |
| *Country (request\_country)* | **Record** | The *request\_country* attribute is linked to the *Countries* template. |
| *City (request\_city)* | **Record** | The *request\_citiy*attribute is linked to the *Cities* template. |

## Instructions

1. Open the default form for the *Travel requests* template for editing.
2. Place the following attributes on the form: *Title, Country*, and *City*from the *Travel requests* template.
3. Select the *Cities* field on the form to display its **Field properties** pane.
4. In the **Appearance** property, select **Dropdown**.
5. In the **Filter** property, define the filter using one of the following options:
   - **Attribute** — select the *Countries → Cities of the country*attribute from the dropdown***.***
   - **Formula** — write the following expression in CMW formula language:
     ```

     from a in db->cities where a-> country == $request_country select a->id

     ```
   - **N3** — write the following expression in N3 language:
     ```

     @prefix container: <http://comindware.com/ontology/container#>.
     @prefix object: <http://comindware.com/ontology/object#>.
     @prefix math: <http://www.w3.org/2000/10/swap/math#>.
      
     {
         ("cities" "country") object:findProperty ?citiescountryProp.
         ("travel_requests" "request_country") object:findProperty ?tr_countryProp.
      
         ?item ?tr_countryProp ?tr_country.
         ?value a [object:alias "cities"].
         ?value ?citiescountryProp ?tr_country.
     }

     ```
   - **DMN** — select the *Cities* template as the **Data source** and configure the DMN table as shown below:

     ![DMN filter example](https://kb.cmwlab.com/assets/img_64358119dbc92.png)

     *DMN filter example*
6. Save the form.
7. Create or open a *Travel requests* record.
8. Test the filter:
   - Select the *Country*.
   - Select the *City*.
   - The *City* dropdown should list the cities of the selected country.

**Note:**The user needs sufficient access rights to view the country and city records. If a dropdown does not show any entries, check the access rights in the user's role.

**Tip:**Use the form rules to configure a dynamic field behavior for more convenient data entry. See [Configuring Form Rule Using Formula](https://kb.comindware.ru/article.php?id=1987).

## See Also

[Configuring Filters for Record Attributes](https://kb.comindware.ru/article.php?id=2020)

================================================
FILE: 395. Version 4/399. How-Tos/2050-example_field_filter.md
================================================
---
title: Reference Attribute Filter Example
kbId: 2050
---

# Reference Attribute Filter Example

This article describes an example of a client contracts filter on the request form.

The system names of the record templates and attributes used in the example are given in the table:

| Record template | Attributes |
| --- | --- |
| Requests | contractclient\_requestor |
| Contracts | client |

The following functions and operators will be used in the expression:

- "***EQUALS()***" function to select a record that corresponds to the client in the request;
- "***from***" operator for listing all records from the "Contracts" record template;
- "***where***" operator to select records that match the condition;
- "***select***" operator for selecting attribute values.

**Step-by-step instruction:**

**1.** Create and customize record templates and attributes.

**2.** In the "*Requests*" record template, open "*Forms*".

**3.** Add the "*contract*" attribute to the form.

**4.** Enter an expression in the filter box.

```
from a in db->Contracts where EQUALS($client_requestor,a->client) select a->id
```

**Syntax**

| Element | Definition |
| --- | --- |
| from a in db->Contracts | Declaring a local variable *a*.  Declaring the "*Contracts*" record template as a data source: *db->Contracts*. Enumerate all entries from the "*Contracts*" record template. |
| where EQUALS($client\_requestor,a->client) | Selecting a record in which the value in "*client\_requestor*" of the current request matches the value of the "*client*" attribute in the “*Contracts*” record template. |
| select a->id | Select the required record IDs. |

================================================
FILE: 395. Version 4/399. How-Tos/2070-form_dynamic_display.md
================================================
---
title: Configuring Dynamic Field Display Using a Form Rule
kbId: 2070
---

# Configuring Dynamic Field Display Using a Form Rule

## Use Case

In the **CMW Platform**, you can define a set of rules for any form to control its element behavior.

Each rule can include several conditional actions:

- Set field values
- Show field validation warnings and error messages
- Change element access mode: require entry, allow entry, read-only
- Hide elements

In this article, we will define a form rule to show the hidden fields only when the preceding fields are filled.

## Prerequisites

In the example scenario, when creating a business trip request, an employee selects the destination country, city, and airport.

To streamline the user experience, we initially show the *Country* hide field and hide the *City* and *Airport* fields. When the user selects the country, the *City* field appears. When the user selects the city, the *Airport* field appears.

To proceed with the example, set up the template, attributes, and form fields as shown in the table below:

| **Record template name** | **Attribute and field display name (system name)** | **Field Access setting on the form** |
| --- | --- | --- |
| *Travel requests* | *Country (request\_country)* | **Require entry** |
| *City (request\_city)* | **Hide** |
| *Airport (request\_airport).* | **Hide** |

## Instructions

1. In the *Travel requests*template, open the default form.
2. Open the ***Form rules*** designer using the dropdown next to the form heading.
3. Add a rule and an action to the rule.
4. Configure the **Action properties**.
   - From the **Form element** dropdown, select the *City (request\_city)* field**.**
   - From the **Action** dropdown, select **Change access****.**
   - From the **New value**dropdown, select **Require entry**.
   - In the **Execution condition** field, enter the [**formula**](#mcetoc_1gtqijebq0):
     ```
     NOT(EMPTY($request_country))
     ```
5. Add a second action to the rule.
6. Configure the **Action properties**.
   - From the **Form element** dropdown, select the *Airport**(request\_airport)* field**.**
   - From the **Action** dropdown, select **Change access****.**
   - From the **New value**dropdown, select **Require entry**.
   - In the **Execution condition** field, enter the [**formula**](#mcetoc_1gtqijebq0):
     ```
     NOT(EMPTY($request_city))
     ```
7. Click ***Save***.

### Formula Syntax

| Element | Description |
| --- | --- |
| `NOT()` | This function returns `true` if its argument resolves to `false`. |
| `$` | This prefix refers to an attribute in the current record context. |
| `EMPTY()` | This function returns `true` if its argument has an empty value. |

## See Also

[Configuring Context-Dependent Filter for Record Attribute](https://kb.comindware.ru/article.php?id=2022)

[Configuring Form Rule Using Formula](https://kb.comindware.ru/article.php?id=1987)

================================================
FILE: 395. Version 4/399. How-Tos/2076-object_search_filter.md
================================================
---
title: Setting up advanced object search by parameters
kbId: 2076
---

# Setting up advanced object search by parameters

Usually, users select the necessary value from the drop-down attribute with the “Record” data type that shows either the display attribute or the object ID of the specified record template. In some cases, this information is not enough, and then the values ​​of several attributes can be joined to form a complex displayed attribute (see article [Combine Several Values Into a Record Title](https://kb.comindware.ru/article.php?id=2003)).

Besides, you can configure an advanced search for an object by certain parameters. To do that:

**1.** Create a technical record template “*Advanced object search*”.

**2.** Create attributes by which you plan to search for the objects, for example, “*Date from*” and “*Date to*”.

**3.** Create an attribute with the “Record” data type and select the record template from which you plan to initiate the advanced search.

**4.** In the «*Advanced object search*» record template, create a «*Search*» form and bring out the attributes created in step 2.

**5.** In the record template from which you plan to initiate the advanced search, create an “*Advanced search*” button with the “*Create linked record*” operation and select the “*Advanced object search*” record template by the attribute created in step 3.

**6.** On the “*Search*” form, open the attribute created in step 2 and drag out the required attribute that you want to search for and write a “*Filter*” for it. Filter example: *from a in db->Projects where AND(GREATER(a->DueDate,$DateFrom),LESS(a->DueDate,$DateTo))*

**7.** In the initial record template, got to the form and place the “Advanced search” button next to the attribute that you want to search for by the advanced parameters.

**8.** When clicking on the button, a window with the “*Search*” form should pop up, with the attributes for the advanced search and the attribute that you are looking for, with filtered values. Select a required value in it and when you save it, this value will be also saved in the main record.

**Note :** you can use this record template to find objects from different record templates. To do this, you need to create the required number of forms, attributes for the search and create different buttons to select the required search forms.

================================================
FILE: 395. Version 4/399. How-Tos/2082-notification_template_body.md
================================================
---
title: Generate Notification Body Using a Template with Placeholders
kbId: 2082
---

# Generate Notification Body Using a Template with Placeholders

## Use Case

You might want to generate the e-mail body using a template with placeholders for variable data, for example, to notify the users about work results or deadline changes.

In this article, we will generate the notification text sent to employees during the vacation request approval process.

## Prerequisites

To proceed with the example, create the attributes as shown in the table below:

| **Record template name** | **Attribute name** | **Attribute system name** | **Attribute type** |
| --- | --- | --- | --- |
| *Vacation Requests* | *Notification template* | *message**Template* | **Text** |
| *Employee's full name* | *employeefullname* | **Text** |
| *Signing date* | *signingD**ate* | **Date & time** |
| *HR's full name* | *HRfullname* | **Text** |
| *Notification body* | *notificationbody* | **Text** |

## Instructions

1. In the *Vacation Requests* template, place the *Notification template, Employee's full name, Signing date, HR's full name,*and *Notification body*attributes on the form.
2. In the *Notification body* attribute properties, check the **Auto calculate** box.
3. In the **Calculated value**, enter the following [**formula**](#mcetoc_1gtqijebq0):
   ```
   FORMAT($messageTemplate, LIST($employeefullname, $signingDate, $HRfullname))
   ```

   Note

   Instead of calculating the attribute value, you can populate the message template using form rules or scenarios.
4. Create a record in the *Vacation Requests* template and fill in the *Notification template* field with the following text
   ```

   Good day, {0}!
   Please come to the HR Director's office on {1} to sign the vacation leave paperwork.
   Sincerely, Human Resources Specialist {2}

   ```

   Here the numbers in curly brackets `{0}` denote the placeholders to substitute with the *Employee's full name, Signing date,* and *HR's full name*.
5. Fill in the *Employee's full name, Signing date,* and *HR's full name* on the form.
6. The *Notification body*field should now contain the message body filled with the data you filled in.
7. Use the resulting *Notification body* attribute value in the notification messages.

### Formula Syntax

| Element | Description |
| --- | --- |
| `FORMAT(originalText, replacerTextList)` | The `FORMAT()` function takes two arguments:   - `originalText` — a string with numbered placeholders in curly braces: `{0}...{N}`. The placeholders are numbered from 0. - `replacerTextList` — an array of strings to replace the placeholders in the `originalText`.   The `FORMAT()` function looks up the placeholders in the `originalText`, replaces them with the corresponding `replacerTextList` elements and returns the resulting string. |
| `LIST(argument1, ..., argumentN)` | The `LIST()` function takes several arguments and returns an array of the argument values. |
| `$` | The `$` prefix refers to an attribute system name in the current record context. |

================================================
FILE: 395. Version 4/399. How-Tos/2084-text_attribute_mask.md
================================================
---
title: Configuring Custom Mask
kbId: 2084
---

# Configuring Custom Mask

## Use Case

In the **CMW Platform**, you can define a regular expression mask for the **Text** attribute display format. When the user enters the attribute value, the mask restricts it to the specified format. You can use the preconfigured **E-mail address** mask or specify a **Custom mask**.

In this article, we will create the *Name* attribute that can consist maximum of 10 Latin letters and the *Phone* attribute restricted to the US phone numbers in international format: *+1 (XXX) XXX-XXXX*.

## Instructions

1. Create the *Name* attribute:
   - **Data type** — **Text**
   - **Display format** — **Custom mask**
   - **Mask regular expression:**`[A-Za-z]{10}`
2. Create the *Phone* attribute:
   - **Data type** — **Text**
   - **Display format** — **Custom mask**
   - **Mask regular expression:** `\+1 \([0-9]{3}\) \([0-9]{3}\)-\([0-9]{4}\)`
     **Tip:** To validate the attribute value (e.g., to make sure the user does not omit phone number digits), configure the validation expression and message on the **Value validation** tab.
3. Place the *Name* and *Phone* attributes on a form.
4. The *Name* field will allow entering up to 10 upper and lower case Latin letters.
5. The *Phone*field will allow entering up to 10 digits. Other phone number elements will be fixed.

_![Name and Phone fields with custom masks](https://kb.cmwlab.com/assets/img_643ec6f918a6d.png)_

## Mask Regular Expression Syntax

| Element | Description |
| --- | --- |
| `[A-Za-z]{10}` | - The `[ ]` square brackets define a character range. - The number in the `{ }` curly brackets defines the preceding token repetition number. - The `[A-Za-z]{10}` token defines a string 10 Latin upper and lower case letters. |
| `\+1` | - The `\` backslash escapes the reserved `+` character. Otherwise, it is interpreted as a regex token. - The `+``1` are fixed characters. They are automatically entered in the field. |
| `\([0-9]{3}\) \([0-9]{3}\)-\([0-9]{4}\)` | - The \ backslash escapes the reserved ( and ) characters. Otherwise, they are interpreted as a regex group token. - The  `[0-9]{3}` token defines a string of 3 Arabic numbers. - The parentheses, hyphen, and space are fixed characters. They are automatically entered in the field. |

**Tip:** You can learn more and experiment with regular expressions at <https://regex101.com/>

================================================
FILE: 395. Version 4/399. How-Tos/2085-context_change_bap.md
================================================
---
title: Understanding and changing the context in CMW Platform
kbId: 2085
---

# Understanding and changing the context in CMW Platform

The concept of context is always used to set up business logic and calculations in CMW Platform. First of all, any information system has a database, and in order to get some data from it, you need to write a query to the database.

The context is the starting point of a database query. Context boundaries are record templates, process templates, and user tasks and are defined in the query (in the form of calculated attributes, form rules, filters, etc.), and they must be distinguished so that the expression is written correctly.

**$** is the designation of the original context.

To change the context, use attributes with the "Record" data type or expressions of the "***from a in db***" type. To change the context to a related entry, use the system name of the attribute with the "Record" data type after "***$***" and the characters "***->***" after the system name. In scenarios, you can change the context by specifying the actual attribute with the "Record" data type or by writing an expression of the "***from a in db***" type.

**Context Change Examples**

**Example 1:** the attribute you are looking for is in a different record template, and the current context (record template) has a reference to this record template.

```
$link->field
```

where *link* is the system name of the attribute with the “Record” data type and *field* is the system name of the attribute in the linked entry.

Read more about calling related data in the article [Retrieving Related Data](https://kb.comindware.ru/article.php?id=2086).

**Example 2:** The attribute you are looking for is in another record template, but the current context (record template) does not refer to this record template.

```
from a in db->recordtemplate_systemname where EQUALS(a->field1, $field2) select a->id
```

where *recordtemplate\_systemname* is the system name of the record template you want to search in, *field1* is the system name of the attribute in this record template, and *field2* is the system name of the attribute in the current record template against which *field1* is to be compared.

Read more about customizing a select expression in the article [List of Comindware Expression Language Operators](https://kb.comindware.ru/article.php?id=2087).

**Example 3:** The current context is a task context, and the attribute you are looking for is in the record template associated with the process template.

```
$cmw.task.objectId->op.11
```

where op.11 is the ID of the attribute in the associated record template.

**Example 4:** The current context is a process context and the attribute you are looking for is in the associated record template.

```
$$BusinessObject->field
```

where *field* is the system attribute name in the associated record template.

================================================
FILE: 395. Version 4/399. How-Tos/2089-account_templates_usage.md
================================================
---
title: Usage of account templates
kbId: 2089
---

# Usage of account templates

Information about all users of the system is contained in the system section "Accounts". The "Account" form displays some basic information:

- Full name
- Login
- Email
- Manager
- etc.

When creating your own solution, you may want to extend the user information with additional attributes. For example:

- for the HR personnel: employee number, date of entry to work, current number of vacation days, personal documents, etc.
- for the IT department: preferred way of contact, level of service, etc.

Within the application you can create several templates with the "Account template" type, for example, "Employees of the company", "Employees of the clients/partners", "Outsourcers", etc., within which you can expand the attributive composition of the system accounts. One user of the system can belong to several templates with the "Account Template" type.

When creating an attribute with the "Account" data type in the record template, you can additionally select an associated template with the "Account Template" type. This setting will allow you to use additional information about the user for:

- displaying in the record forms
- displaying in the tables
- building reports
- calculation of other attributes
- setting up business logic for the processes

Also, when you select an associated template with the "Account Template" type on the form in the "Accounts" drop-down list, this field will display only users attached to the associated template with the "Account Template" type.

In the settings of the template with the "Account template" type, sections similar to the template with the "Record template" type are displayed, with the exception of the import function, because in order to create a user, additional parameters are required, such as login and password.

In the button area for tables in the template with the "Account template" type, by default there is a “Create” button that allows you to create a new user and automatically add him/her to the current template with the "Account template" type.

Adding a user to a template with the "Account template" type is available:

- In the button area for tables in a template with the "Account template" type, by clicking on the "Add to template" button. It is possible to add several users at once to the current template with the "Account template" type.
- In the "Accounts" section, by selecting a user and clicking on the "Link to template" button. It is possible to add multiple users to multiple templates with the "Account Template" type.

================================================
FILE: 395. Version 4/399. How-Tos/2090-data_model_class_diagrams.md
================================================
---
title: Viewing and Editing Data Model and Class Diagrams
kbId: 2090
---

# Viewing and Editing Data Model and Class Diagrams

## Use Case

In each **CMW Platform** application, you can create **data model diagrams**and **class****diagrams**. See [Understanding the Application Data Model](https://kb.comindware.ru/article.php?id=2091).

The data model and class diagrams visually represent and help to design the application architecture and define the template relationships.

You can also use the data model and class diagrams to visualize the existing application architecture. For instance, you can view all the templates linked to a template of interest.

## Using the Data Model or Class Diagram Designer

Use the data model diagram designer to view or configure the account and record templates along with their relationships and attributes.

Use the class diagram designer to view and configure the account, process, and record templates along with their associations, cardinality, attributes, and button operations.

1. Go to the **Data model diagrams** or **Class Diagrams** tab on the application **Administration** – **Diagrams** page.
2. Create or open a diagram.
3. View, create, or configure the templates, their relationships, and attributes.

### Operations in the Diagram Designer

#### Diagram operations

- **Create a template** — drag the **New record template**, **New account template**, or **New process template** (only on the class diagram) to the diagram from the element pane.
- **Add a template to the diagram** — drag the template to the diagram from the element pane.
- **Select version** — select a saved diagram version. The current diagram will be replaced with the selected one.
- **Create new version**— save the current diagram as a new version.
- **Clone**— select a saved diagram version and duplicate it. The cloned version will appear in the diagram designer.
- **Settings** — rename the diagram or its current version *(for the class diagram)*.
- **Refresh data**— update the diagram with the newly created attributes and links.
- **Export** — save the diagram as an SVG file.
- **Show system names**— check this box to view the attribute and template system names instead of display names.
- **Clean** — permanently remove all the elements from the diagram. The templates and attributes will not be deleted.
- **Show archive** *(on the class diagram)* — check this box to show archived elements on the diagram.
- **Go to application administration** *(on the class diagram)* — go to the application **Administration** page.

#### Selected template operations

When you select a template on the diagram, the element menu appears where y can perform the following operations.

- **Add attribute** — create and configure the new attribute properties.
- **Go to template** — open the template properties page.
- **Go to template** — create a new relationship between the templates. Click this button and drag the arrow to the target template.
- **View linked items** — show the templates linked to the selected template on the diagram.
- **Collapse/expand group** *(on the data model diagram)* — minimize the template element to its header or expand to show the attributes.
- **Delete** — delete the element from the diagram. The template itself will not be deleted from the application.

**Notes**

- When you edit the data model diagram, all the changes are applied to the database automatically.
- You can save several versions of a data model diagram and recall them to have different class visualizations. Choosing a different data model or class diagram version does not change the application data model.
- You can create several data model diagrams and class diagrams for an application, for example, to show only certain record template relationships.
## See Also

[Understanding the Application Data Model](https://kb.comindware.ru/article.php?id=2091)

================================================
FILE: 395. Version 4/399. How-Tos/2091-application_data_model.md
================================================
---
title: Understanding the Application Data Model
kbId: 2091
---

# Understanding the Application Data Model

## Record Template Definition

The application data model in the **CMW Platform** is built upon the **record templates**. You can think of a record template as a registry, table, entity, or class.

The record template is defined by its **attributes** (similar to the class attributes or table fields). The attributes are used in the forms, tables, export templates, and other application elements.

The analysts (developing the application) and end users view the data stored in the record template (the **records**) in forms or tables similar to Excel sheets.

The underlining database stores the data in a graph structure.

**Note:** account templates, organizational unit templates, and role templates are **record templates** with special system attributes and behavior.
## Data Model Diagrams

To visually build the application data model, use the **Data model diagrams**.

Use the data model diagram designer to view or configure the account and record templates along with their relationships and attributes.

You can save several versions of a data model diagram and recall them to have different data model visualizations.

## Class Diagrams

You can also draw **Class diagrams** that represent the application templates as classes.

Use the class diagram designer to view and configure the account, process, and record templates along with their associations, cardinality, attributes, and button operations.

You can save several versions of a class diagram and recall them to have different class visualizations.

## See Also

[Viewing and Editing Data Model and Class Diagrams](https://kb.comindware.ru/article.php?id=2090)

================================================
FILE: 395. Version 4/399. How-Tos/2093-universal_record_url.md
================================================
---
title: Universal URL to open any record in the system
kbId: 2093
---

# Universal URL to open any record in the system

When setting up solutions, it may be necessary to calculate a direct URL link to objects with a dynamically affixed object ID, whose belonging to a particular template is not known in advance. Such a problem can arise, for example, when generating notification templates that require one reference to objects from potentially different templates, or when conditionally calculating links in calculated fields.

Standard direct links to records and tasks always contain an indication of the template (and sometimes also the template form) in which the object is stored and putting down the object ID from another template will open a form that does not correspond to this object.

To avoid this, the link must be in the following format:

```
https://<product instance URL>/#Resolver/<ID>
```

where the product instance URL should be replaced with the address of the product instance, and <ID> with the contextual ID of the object you are looking for, for example, using the ***FORMAT*** function.

See also: [Computing a hyperlink to a process instance](https://kb.comindware.ru/article.php?id=1891).

================================================
FILE: 395. Version 4/399. How-Tos/2096-chevron_coloring_logic.md
================================================
---
title: Setting up coloring logic for chevrons
kbId: 2096
---

# Setting up coloring logic for chevrons

{{ productName }} has a tool for visually displaying stages — chevrons. A distinctive feature of chevrons is the ability to paint each stage with a different color according to a specified rule.

To correctly set the color representation of the chevron, it is important to set the correct conditions. The coloring logic is the same for all chevrons, it is recommended not to use the attributes of the main record template where the collection is planned to be displayed.

Let's analyze an example of visualization of the stages of an application for a car.

**1.** In the record template referenced by the chevron attribute, create two attributes:

- Stage start date (data type — Date and time, display format — any);
- Stage completion date (data type - Date and time, display format — any).

**2.** On the diagram of the main process for approving an application for a car, configure the filling of the attributes created in step 1 for each stage (at the entrance and exit of the corresponding tasks).

**3.** On the form where the chevron is located, in the attribute properties, add the rules for coloring entries:

- Color #efbb3a — Condition ***AND(NOT(EMPTY($StartDate)),EMPTY($EndDate))*** (the chevron will be colored orange if the stage has started);
- Color #338320 — Condition ***AND(NOT(EMPTY($EndDate)),NOT(EMPTY($StartDate)))*** (the chevron will be colored green if the stage is completed);
- Color #a8a8a8 - Condition **AND(EMPTY($StartDate),EMPTY($EndDate))** (the chevron will be gray if the stage has not started).

These conditions set the order of coloring individual chevron windows, that is, for each stage, a check for these conditions will be carried out, the chevron element will change color in accordance with the dates filled in.

================================================
FILE: 395. Version 4/399. How-Tos/2098-mass_process_local_var.md
================================================
---
title: Using a Local Variable to Mass Process Records
kbId: 2098
---

# Using a Local Variable to Mass Process Records

In {{ productName }} you can configure the ability to mass process multiple records in a table, for example, if you need to change the status of several requests at the same time, confirm the payment of several invoices, etc. This article considers an example of the mass assignment of responsible persons for requests and the subsequent launch of the process for each of the request.

Since it is impossible to open any form when selecting several records (the form shows only the attributes of one record), it is proposed to use the mechanism of local variables. You can put a certain value in a local variable, which can then be applied or duplicated for all the selected records.

**Initial data:**

- Record template "Requests".
- Attribute of the "Accounts" data type — "Responsible".
- Process template "Request processing".

**Set-up:**

**1.** In the "Requests" record template, create a button with the following parameters:

- Display name — Assign responsible;
- Operation context — Record;
- Operation — Save;
- Operation result — Update data;
- Show the dialog— check this checkbox.

Save the button settings and go to the "Local variables" tab. Create a variable "Responsible" (data type — Account).

Go to the "Properties" tab and click on "Configure the dialog". Move the created local variable to the central area. Save the settings and move the button to the toolbar for tables.

**2.** Go to the application settings and click "Scenarios". Create a new scenario with the following parameters:

- Name — Assign responsible for requests
- Execution context — By initiator;
- Status — Active.

**3.** Set up the beginning of the scenario upon the button click that was created in step 1, add an action to change attribute values. Select the "Responsible" attribute, specify the operation on the values — Replace and in the "Value" field, select N3 and insert the following expression:

```

@prefix cmwsession: <http://comindware.com/ontology/session#>.
@prefix user: <http://comindware.com/ontology/user#>.
@prefix variable: <http://comindware.com/ontology/session/variable#>.
@prefix debug: <http://comindware.com/ontology/debug#>.

{
    cmwsession:context variable:dialogVariables ?v1.
    ?v1 variable:responsible ?value.
}

```

It is important to specify the system name written in the local variable after "***variable:***".

Then add the "Start a Process" action, select the "Request processing" process. Go to the "Additional" tab and check the boxes "Execute separately from the scenario" and "Ignore all errors", if this is not done, the process will not start on each of the entries, but only one of them.

**4.** Test. Select several requests, click on the "Assign responsible" button. A dialog box will open with the local variable "Responsible". Select a user, confirm the operation.

================================================
FILE: 395. Version 4/399. How-Tos/2103-holiday_calendar.md
================================================
---
title: Setting up and using the holiday calendar
kbId: 2103
---

# Setting up and using the holiday calendar

To control the due dates of the tasks assigned to users, **CMW Platform** has a built-in functionality in the task settings that allows you to specify the amount of time, up to seconds, within which the user must complete the task. But there are cases when the due dates must be set taking into account working days and hours.

For this purpose there are ***WORKDAYS()*** and ***WORKHOURS()*** functions, which return a date based on the number of working days or hours since a particular date. However, these functions have a limitation: they only take into account weekends and do not consider national or other holidays. Therefore, in these functions it is possible to additionally specify a list of dates that are non-working. In order not to register all holidays inside the function, we recommend creating a separate reference record template with a calendar of holidays, and refer to it when writing an expression with ***WORKDAYS()*** and ***WORKHOURS()*** functions.

**1.** Create a "*Holiday Calendar*" record template.

**2.** Create an attribute with the "Date and time" data type and name it "*Date*".

**3.** Customize the form and table by placing the newly created attribute.

**4.** Create records. Go to the table, click the "***Create***" button and in the "*Date*" field, select one of the holidays, for example, January 1 of the current year.

**5.** Next, in the same way, create records for all the holidays that are in the current year (for the subsequent years, you will also need to create separate records in this record template).

**6.** Go to the task settings where you want to set the due date with taking into account working days. Click the "***Advanced***" tab, then select the "*Formula*" option in the "***Execution time***" field, then insert the following:

```
WORKHOURS(NOW(),18,DURATION("PT9H"),DURATION("PT9H"),LIST((from a in db->holliday_calendar select a->Date)))
```

**where:**

***holiday\_calendar*** — system name of the record template created in step 1;

***Date***— the system name of the attribute created in step 2.

This formula is deciphered as follows: starting from the current moment (when the process created the task), count 18 working hours (the duration of the task), considering that the working day starts at 9 am and lasts 9 hours, and taking into account all the exceptions indicated in the holiday calendar.

**Note:** if you add a weekend (Saturday or Sunday) to the holiday calendar, then when calculating the expression, it will be considered as a working day.

================================================
FILE: 395. Version 4/399. How-Tos/2105-record_template_multiapp.md
================================================
---
title: Working with a record template from different applications
kbId: 2105
---

# Working with a record template from different applications

Record template in **CMW Platform** is a data registry, like an Excel sheet or table in a relational database.

Application in **CMW Platform** is a separate business solution, which has its own set of templates, diagrams, roles and variables, as well as its own navigation, integration and data path sections.

**CMW Platform** provides many options for how applications interact. This article will consider the scenario of working with one record template in different applications. This may be necessary when the same record template must be used in two applications, for example: CRM and SRM applications use a single directory "Clients". In order not to duplicate data and not create two "Clients" record templates, you can create one such record template in one application, specify all the necessary relationships, and then transfer it to another application. Old links will remain, but you can build new links in another application.

**1.** To move a record template to another application, go to the properties of the record template and click the "***Change the application***" button.

_![Record template properties](https://kb.cmwlab.com/assets/2022-11-11_10h00_08.png)_

**2.** Then select a new application, click the "***Save***" button in the application change window and the "***Save***" button in the properties of the record template.

_![Application change](https://kb.cmwlab.com/assets/2022-11-11_10h00_25.png)_

In the current record templates in the CRM application, all links to the "Clients" record template are preserved and continue to work, and now you can create attributes in the SRM application that refer to the "Clients" record template. In order to create new links to the "Clients" record template in the CRM application, you need to change the application again.

================================================
FILE: 395. Version 4/399. How-Tos/2112-adapters.md
================================================
---
title: Adapters
kbId: 2112
---

# Adapters

# Definitions

An adapter is a module (compiled as a DLL) that provides custom connection and communication route to integrate the **Platform** with external systems

Use the **Adapters** section to load and compile custom modules to connect the **{{ productName }}** to external systems.

Loaded modules are compiled on the server side, and corresponding connections become available when creating connections and communication routes.

## Viewing the adapter list

1. Select **Adapters** in the [**Administration** — **Infrastructure**](https://kb.cmwlab.com/secure/administration-imported-from-the-cmw-help-2113.html#mcetoc_1gk32a3hh4) section.

_![Adapters item on the Administration page](https://kb.cmwlab.com/assets/adapters.png)_

2. You will see the adapter list on the **Adapters** page.

_![Adapter list](https://kb.cmwlab.com/assets/adapter_list.png)_

## Creating an adapter

1. Open the [adapter list](#mcetoc_1gk31vchh1).
2. Click **Create**.
3. The adapter properties page opens.

_![Adapter properties page](https://kb.cmwlab.com/assets/adapter_properties.png)_

4. Upload a ZIP archive with the adapter source code in the **Adapter source code** field. The archive must contain the Visual Studio solution:
   - Project with adapter source code.
   - Projects containing the interfaces for the development and subsequent compilation of the adapter.
   - Necessary additional projects for the adapter, for example, a localization project.
   - Folder with the connected libraries.
   - Single solution file (.sln) in the archive's root folder.

_![Adapter source code archive contents example](https://kb.cmwlab.com/assets/adapter_archive_content.png)_

5. Click **Save**.
6. Click **Publish** button to compile the adapter.
7. Upon successful compilation, the adapter name will be displayed in the adapter list and adapter properties.
8. After compilation, view the **compilation log**.

_![Compilation log example](https://kb.cmwlab.com/assets/adapter_compilation_log.png)_

9. To download the archive with adapter execution logs (for example, *CBAP.adapters.20221026.logs.zip*), click **Get execution log**.

_![Adapter execution log example](https://kb.cmwlab.com/assets/adapter_execution_log.png)_

1. The connection item for the compiled adapter will be displayed in the **Custom connections** submenu when creating a connection or communication route.

_![Creating a connection using a custom adapter](https://kb.cmwlab.com/assets/adapter_custom_connection_create_menu.png)_

_![Creating a communication route using a custom adapter](https://kb.cmwlab.com/assets/adapters_custom_communication_route_create_menu.png)_

## Adapter setup

1. Open the [adapter list](#mcetoc_1gk31vchh1).
2. Double-click the adapter row.
3. The adapter property page will be displayed.
4. Configure the adapter similarly to [creating](#creating-an-adapter) it.
   - Upload the new source code archive.
   - Save the adapter.
   - Publish the adapter
5. If necessary view the compilation log or download the execution log.

## Deleting an adapter

**Attention!** Connections and communication routes generated for the deleted adapter will be deactivated and stop working.

1. Open the [adapter list](#mcetoc_1gk31vchh1).
2. Select the adapter to be deleted using the checkbox in the first column.
3. Click **Delete**.
4. In the confirmation window, click **Delete**.

_![Adapter delete confirmation](https://kb.cmwlab.com/assets/adapter_delete_confirmation.png)_

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/2113-administration.md
================================================
---
title: Administration
kbId: 2113
---

# Administration

## Opening the Administration section

The **Administration** section contains subsections to configure various system parameters, both global and for individual business applications.

To access this section select **Administration** in the **Personal area** menu on the right of the top information panel.

_![Personal area menu with the Administration item](https://kb.cmwlab.com/assets/personal_menu.png)_

The **Administration** page appears with the following sections:

- ## Appearance

  - Themes
  - Login and registration page design
- ## Architecture

  - Business applications
  - Navigation sections
  - Templates
  - Diagrams
  - Functions
  - Communication routes
- ## Account Management

  - Accounts
  - Groups
  - System roles
  - Account permissions audit
  - Substitution
  - Registration and login
- ## Infrastructure

  - Monitoring
  - Journals
  - Licensing
  - Backup
  - Manage system services
  - Connections
  - Performance
  - Logging configuration
  - Global configuration
  - [Adapters](https://kb.comindware.ru/article.php?id=2112)

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/2127-periodic_task_reminders.md
================================================
---
title: Setting up periodic reminders for open tasks
kbId: 2127
---

# Setting up periodic reminders for open tasks

CMW Platform, in its basic configuration, supports sending system notifications to a user on a given task as well as process notifications with information from a business process.

Sometimes it becomes necessary to set up reminders for an employee about his open tasks, for example, every day at a certain time.

For this setup, it is necessary to create 2 business processes:

- Search for employees to send a reminder
- Sending daily reminder

The first process will be started by timer every day, for example, at 7am and search for employees who have open tasks at this point in time, and for each employee the system will initiate the subprocess "Sending daily reminder", which in its turn will form and send the list of the employee's open tasks in the form of a table by email.

**Configuring the "Sending daily reminder" process**

**1.** Create a new Process Template.

_![New Process Template](https://kb.cmwlab.com/assets/remind_eng5.jpg)_

**2.** In the associated Record Template, create the following attributes:

- ***Employee*** — an attribute of the "Account" data type to whom the reminder will be sent;
- ***Body*** — a calculated text attribute of the HTML text display format that will contain a task table. Tick the box "Calculate using an expression" and insert the following expression in the "Calculated value":

```
 
@prefix cmw: <http://comindware.com/logics#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
@prefix object: <http://comindware.com/ontology/object#>.
@prefix configuration: <http://comindware.com/ontology/configuration#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
 
{
           ?confid a configuration:Configuration.
           ?confid configuration:baseUri ?baseUri.
           ("Searchesforemployeestosendareminder" "Employee") object:findProperty ?Employee.
 
           ?item ?Employee ?EmployeeVal.
                      
    #First table
    ("<p style='font-size: 100%' >List of tasks</p>" "<table border='1' style='width: 60%; border-collapse: collapse; border: 1px solid black' ><tbody> <tr><td style='padding: 2px; width: 200px; border: 1px solid black'>Task</td> <td style='width: 200px; padding: 2px; border: 1px solid black'>Срок</td></tr>") string:concatenation ?firstHeaderRow.
 
    from {
                       ?tasks a cmw:UserTask.
                       or {?tasks cmw:assignee ?EmployeeVal.}
                       or {?tasks cmw:possibleAssignee ?EmployeeVal.}.
                       ?tasks cmw:taskStatus taskStatus:inProgress.
                       ?tasks cmw:title ?title.
                       ?tasks cmw:id ?id.
        ("{0}" ?title) string:format ?titleVal.
        ("{0}" ?id) string:format ?idVal.
                      
                       or {?tasks cmw:dueDate ?dueDate.}
                       or {"" -> ?dueDate.}.
                      
        ("{0}" ?dueDate) string:format ?dueDateVal.
                      
        ("<tr><td class='A' style='padding: 2px; border: 1px solid black; '><a href='" ?baseUri "#task/" ?idVal "'>" ?titleVal "</a></td><td align='right' style='padding: 2px; border: 1px solid black; text-align: right'>" ?dueDateVal "</td></tr>") string:concatenation ?firstRow.
    } select ?firstRow -> ?firstFactrow.
    (" " ?firstFactrow) cmwstring:join ?firstFact.
    (?firstHeaderRow ?firstFact "</tbody></table> <br/>") string:concatenation ?first.
    ?first  -> ?value.
}

```

- ***To*** — a calculated text attribute that will contain the employee’s email address. Tick the box "Calculate using an expression" and insert the following expression in the "Calculated value":

```
 $Employee->cmw.account.mbox
```

**3.** Create a process diagram as follows:

_![Process scheme](https://kb.cmwlab.com/assets/remind_eng6.jpg)_

**4.** Configure the settings for the sending message event.

**5.** Publish the process.

**Configuring the "Search for employees to send a reminder" process**

**1.** Create a new Process Template.

_![New Process Template](https://kb.cmwlab.com/assets/remind_eng1.jpg)_

**2.** In the associated Record Template, create an attribute:

- ***Employees*** — an attribute of the "Account" data type. Tick the boxes "Store multiple values" and "Calculate using an expression" and insert the following expression in the "Calculated value":

```
 
@prefix cmw: <http://comindware.com/logics#>.
@prefix container: <http://comindware.com/ontology/container#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
 
{
            ?class cmw:className "Account".
            ?value a ?class.
            ?value account:active true.
            not {?value cmw:isDisabled true.}.
            or {?tasks cmw:assignee ?value.}
            or {?tasks cmw:possibleAssignee ?value.}.
            ?tasks cmw:taskStatus taskStatus:inProgress.
}

```

- ***Reminders*** — an attribute with the "Record" data type, linked template is "Daily reminders". Establish a relationship with the new interlinking attribute — Search. Tick the box "Store multiple values".

**3.** Create a process diagram as follows:

_![Process scheme](https://kb.cmwlab.com/assets/remind_eng2.jpg)_

**4.** Configure the start timer event.

_![Timer configuration](https://kb.cmwlab.com/assets/remind_eng3.jpg)_

**Note :** If needed, also provide a plain start event to be able to manually start the process without having to wait for a new work day.

**5.**Set up a scenario at the entrance to the reusable subprocess to create records that the subprocess will then run on.

_![Scenario setup](https://kb.cmwlab.com/assets/2023-02-09_12h50_34.png)_

**5.1.** The first two actions are added by default, so start by adding the "Object loop" action and setting it up.

_![Action "Object loop"](https://kb.cmwlab.com/assets/2023-02-09_12h54_30.png)_

The variable "local" will store one instance from the specified selection at a loop. At the bottom, specify the "Employees" attribute, in which employees with active tasks are calculated.

**5.2.** Add the "Create a record" action and configure it.

_![Action "Create a record"](https://kb.cmwlab.com/assets/2023-02-09_12h57_57.png)_

- Target record template — Specify the record template "Daily Reminders"
- New record reference — specify the "Reminders" attribute created in step 3.
- Operation on the values — specify "Add".

**5.3.**Add the "Change attribute values" action and configure it.

_![Action "Create attribute values"](https://kb.cmwlab.com/assets/2023-02-09_13h17_47.png)_

Click "Create", select the "Employee" attribute, select "Replace" for "Operation on the values", and paste the $$local formula in the last column.

**6.** Configure the reusable subprocess.

_![Subprocess configuration](https://kb.cmwlab.com/assets/2023-02-09_13h21_21.png)_

In the "Record to execute the process", specify the attribute "Reminders", and in the "Called process template" — "Sending daily reminder".

**7.** Publish the process and test.

Before starting testing, check the operability of the E-mail sending connection and the correct configuration of the outgoing communication route.

**Note :** for the correct computation of the calculated fields and the sub-process launch formulas, check the exact match of the system name of each Record Template and attribute, as well as Process Templates.

================================================
FILE: 395. Version 4/399. How-Tos/2129-cancel_process_button.md
================================================
---
title: Stopping the Process on a Button Click
kbId: 2129
---

# Stopping the Process on a Button Click

## Use Case

When setting up a process, you often get several options for its completion logic. For example, you stop the process when an inquiry may be approved or rejected. Or you might need to end the process from the outside, for instance, if the initiator wants to withdraw a contract already sent for approval. For such a case, you can create a button that will stop the whole process at any step.

**Scenario:** In the *Contract Approval* process, the initiator decides that a contract is no longer valid and wants to cancel its approval.

**Solution:** We will use inter-process communication and create a button to cancel the contract approval.

## Setting up the Processes and Templates

1. In the **record** **template** (for instance, *Contract Approvals*) linked to the main *Contract Approval* **process template**, create a **Text** attribute:  ***ProcessID***.
2. On the *Contract Approval* process diagram:
   - Open the exit scenario of the start event.
   - Add **Change attribute values** action.
   - In the action properties, specify the ***ProcessID*** attribute value using the following **formula**: `FORMAT("{0}", LIST($$ProcessObject))`. This formula returns the active process ID.
3. On the same process diagram:

- Add a parallel gateway between the **Start event** and *User Task 1*.
- To the parallel gateway, add **Receive message intermediate event** and **End event**. One token will go to the *User Task 1*, and the other will go to the **Receive message intermediate event**.
- In the **Receive message event properties**:
  - Specify a unique **Message name** (you will later use it in the **Send message event**) on the **Advanced** tab.
  - Configure the attribute mapping on the **Message data** tab if needed.

Thus, when the process starts, two tokens are active. The process will end according to the configured logic (for example, upon the contract approval) or when a cancellation message is sent to the **Receive message intermediate event**.

![Main process diagram](https://kb.cmwlab.com/assets/canceleng1.png)

Main *Contract Approval*process diagram

**Note:**For this scenario, all end events in the process must be terminators so that they stop the whole process, not just one of its tokens.

1. Create an auxiliary **process** **template** *Contract Withdrawal* with a new linked **record template** (for example, *Contract Withdrawals*).
2. In this new **record template,**create the attributes:
   - **Record** attribute *Contract* linked to the *Contact Approvals***record template** (with **attribute interlinking**)
   - **Text** attribute *Comment* (place it on the *Contract Withdrawal* process **Start form**).

![Auxiliary process diagram](https://kb.cmwlab.com/assets/img_6430203a82d6d.png)

Auxiliary *Contract Withdrawal*process diagram

1. On the *Contract Withdrawal* diagram *:*
   - Add a **Send message intermediate event** between the **Start event** and **End event.**
   - In the **Send message event properties:**
     - Specify the same **Message name** as in the [**Receive message event** **properties**](#Receive-Message-Properties) on the *Contract Approval* process diagram,
     - Specify the **Process instance** using the following **formula**: ***$Contract->ProcessID**,*where:
       - [***$Contract*** is the attribute](#Contract-Record-Attribute) linked to the *Contract Approvals* record template.
       - ***ProcessID*** is the attribute created in [step 1](#ProcessID-Attribute). It stores the active process ID.
       - Configure the attribute mapping on the **Message data** tab, if necessary.
   - Configure the **Start form** if needed.
2. In the *Contract Approvals* **record template** (linked to the *Contract Approvals* process), create a new button: *Withdraw contract**.*
3. Configure the *Withdraw contract* button properties:
   - **Operation context** — **Record**
   - **Operation** — **Start process from linked template**
   - **Operation result** — **Refresh data**
   - **Template** — *Contract Withdrawal* (**attribute**: *Contract Approval*)
   - **Display condition** — specify when to show the button if needed.
4. Place the *Withdraw contract* button on any form or table toolbar.
5. Test the process.

================================================
FILE: 395. Version 4/399. How-Tos/416. Scenarios/2106-scenario_actions.md
================================================
---
title: Scenario Actions
kbId: 2106
---

# Scenario Actions

 **{{ productName }}**scenarios may consist of the following actions. For specific action properties description, see the [Scenario Action Types](#mcetoc_1gj42f3a31).

For information on configuring scenario actions, see [Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109).

## Common Action Properties

All actions have the ***Description*** field on the ***General***tab — an optional comment about the action purpose.

All actions have the following properties on the ***Additional*** tab:

- ***Type** —* the action type.
- ***Context template*** — the action will be executed for this template.
- ***Ignore all errors** —* if this box is checked, the scenario action will continue to run despite any errors: exceptions, invalid data, etc.
- ***Execute Separately from the scenario** —* if this box is checked, the action and all its child actions will be executed asynchronously with the remaining scenario actions.
- ***Clear cache** —* if this box is checked, the data is refreshed before executing the action to avoid using obsolete cached values.

![Common actions properties on the Additional tab](https://kb.cmwlab.com/assets/img_6388a68d3d365.png)

*Common actions properties on the Additional tab*

## Scenario Action Types

### Validate the Expression Result

This action validates a condition in the context template (specified on the ***Additional*** tab). If the condition is not met, an error message is displayed with the specified text.

The ***General*** tab provides the following properties:

- ***Failure message** —*the text that will be displayed to the user if the expression returns `false`.
- ***Expression** —* the condition to validate. The action will be triggered if the expression (***formula***, ***N3**,* or ***DMN***) returns `false`.

_![Validate the Expression Result action general properties](https://kb.cmwlab.com/assets/img_6388a63c2b977.png)_

### Create a Record

This action creates a record in the specified template.

_![Create a Record action general properties](https://kb.cmwlab.com/assets/img_6388a49fbe381.png)_

The **General** tab provides the following properties:

- ***Target record template*** — the record will be created in this template.
- ***New record reference***— a ***Record***attribute of the***context template*** (specified on the ***Additional*** tab) that will contain a link to the created record. You can set this field if the context template is linked with the target template.
- ***Value operation*** ​— available if a new record reference is selected:
  - ***Add** —*adds a created record link to the specified attribute (if the attribute’s ***Store multiple values*** check box is checked).
  - ***Replace***— replaces the existing links in the specified attribute with a created record link.

### Clone a Record

This action duplicates the specified records. The target template must match the context template (specified on the ***Additional*** tab).

_![Clone a Record action properties](https://kb.cmwlab.com/assets/img_6388b07ccf52c.png)_

The **General** tab provides the following properties:

- ***Target record template*** — the duplicate record will be created in this template.
- ***New record reference***— a ***Record***attribute of the***context template*** (specified on the ***Additional*** tab) that will contain a link to the created record. You can set this field if the context template is linked with the target template.
- ***An attribute or expression to find the objects***— a ***Record*** attribute linked to the records being cloned, or an expression (***formula***, ***N3***, or ***DMN***) that returns the ID of the records to clone.
- ***Value operation*** ​— available if a new record reference is selected:
  - ***Add**—*adds a created record link to the specified attribute (if the attribute’s ***Store multiple values*** check box is checked).
  - ***Replace***— replaces the existing links in the specified attribute with a created record link.
- ***Clone with child records*** — check this box to clone the record and the records it references. In this case, the action will only clone the child records referenced by the attributes with the checked ***Delete related records*** checkbox.
  - ***Cloning depth***— the number of child record levels to clone.

### Change the Context

This action changes the scenario execution context to the specified records in the target template. The subsequent actions in the scenario will be executed for these records.

_![Change the Context action properties](https://kb.cmwlab.com/assets/img_6388b6b8c4f8a.png)_

The **General** tab provides the following properties:

- ***Target record******template*** — the scenario execution context will be changed to this template.
- ***An attribute or expression to find the objects***— a ***Record*** attribute or an expression (***formula***, ***N3***, or ***DMN***) that returns the IDs of one or more records to which the context will be changed. If an attribute or expression refers to multiple records, a loop for each of the referred records will be run with the actions nested within the ***Change the context*** action.

### Change Attribute Values

This action changes the specified attribute values in the context template record (listed on the ***Additional*** tab).

_![Change Attribute Values ​​action properties](https://kb.cmwlab.com/assets/img_6388bc8e23d2e.png)_

The **General** tab provides the following properties and buttons.

- ***Attribute***— the context template attribute to be modified (the context template is specified on the ***Additional*** tab).
- ***Value operation***
  - ***Replace***— sets the attribute value specified in the ***Value*** column.
  - ***Delete***— removes all attribute values.
  - ***Add*** dd the value specified in the **Value** column to the attribute (this item is displayed for ***Record**,* ***Account***, ***Role***, ***Organizational unit***, ***Document***, and ***Image*** attributes with the checked ***Store multiple values***​ checkbox).
  - ***Exclude***— removes object references specified in the **Value** column from the attribute (this item is displayed for ***Record**,* ***Account***, ***Role***, ***Organizational unit***, ***Document***, and ***Image*** attributes with the checked ***Store multiple values***​ checkbox). The associated objects themselves will not be deleted.
  - ***Create***— click this button to add an attribute.
  - ***Delete***  — check the boxes for the attributes to be deleted and click this button to delete them.
- ***Value***— specify one or more attribute values ​​using an ***attribute***, ***formula**,* ***N3*** expression, or ***DMN*** table.

### Change Variable Values

This action changes the values in a structured variable set.

_![Change Variable Values ​​action properties](https://kb.cmwlab.com/assets/img_6388c34dbddf4.png)_

The **General** tab provides the following properties:

- ***Variable set*** — the name of the variable set to change. This variable set is a key-value dictionary.
- ***Value operation***
  - ***Add** —*adds the variables and values specified in the variable table to the variable set.
  - ***Replace***— sets the variables and values specified in the variable table to the variable set.
  - ***Exclude***— removes all variables and values ​​from the variable set.
- Variable table
  - ***Variable name*** — a variable to change.
  - ***Value***  — an attribute or expression (***formula***, ***N3***, or ***DMN***) that specifies one or more variable values.
  - ***Create***— click this button to add a variable.
  - ***Delete***  — check the boxes for the variables to be deleted and click this button to delete them.

### Start a Process

This action creates an instance of the specified process template.

_![Start a Process action properties](https://kb.cmwlab.com/assets/img_6389c1276d862.png)_

The **General** tab provides the following properties:

- ***Process template*** — a process template in which a new instance will be created based on the current record of the context template (specified on the ***Additional*** tab). To start the process with a new record, execute the ***Create a record*** action before this action.

### Send a Message

This action sends a message through the specified connection and communication route.

_![Send a Message action properties](https://kb.cmwlab.com/assets/img_6389c316db2fa.png)_

The **General** tab provides the following properties:

- ***Connection** —* the connection used to send the message.
- ***Communication route****—*the communication route used to generate the message.
- ***Message variable name***— a variable that stores message content. This variable must be set using the preceding ***Change variable values*** action. This variable is a key-value dictionary. The specified data path translates the message variable into a message. The resulting message will be sent over the specified connection.
- ***Successful response variable name*** — a variable to store the server response if message sending succeeds.
- ***Error response****variable** **name***— a variable to store the server response if message sending fails.

### Import Data from a File

This action imports the data from the file into the context template (specified on the ***Additional*** tab). Each line of data from the file is imported as a separate entry in the context template.

![Import Data From a File action properties](https://kb.cmwlab.com/assets/img_6389c64d38c26.png)

Import Data from a File action properties

The **General** tab provides the following properties:

- ***Data fil****e*** — load a data file (by selecting the ***Value*** item), specify *an****attribute**,* ***formula**,* ***N3***expression, or ***DMN*** table that returns a document link.
- ***Encoding***— imported file data encoding.
- ***Time zone***— the time zone in which the date and time values are stored in the imported file.
- ***Column****separator*** — imported file data column separator (used for CSV file import): comma, semicolon, period, tab, space.
- ***Ignore parsing errors***— if this box is checked, the data will be imported even if errors occur during data processing.
- ***Update existing records with data from the file*** — check this box to update existing records in the context template with the data from the corresponding rows of the imported file and create the missing records. If this check box is not checked, a new record will be created for each row of the imported file. When this box is checked, the ***Key attribute*** table is displayed.
- ***Key attribute***— this table maps the context template key attribute to the imported file key column:
  - ***Attribute***  — an attribute containing *unique values* ​​by which rows in the imported file will be mapped to the database records.
  - ***Format***  — key column value format.
  - ***Column***— the column number in the imported file corresponding to the key attribute.
- ***Data mapping***— this table maps the context template attributes to the imported file columns:
  - ***Attribute***  — the attribute to import the values from the corresponding column.
  - ***Format***  — imported column value format.
  - ***Column***— imported column number corresponding to the specified attribute.

### Create a Document Using a Template

This action generates a file using an export template and stores the generated file link in a variable.

_![Create a Document Using a Template action properties](https://kb.cmwlab.com/assets/img_638ef501bb9af.png)_

The **General** tab provides the following properties:

- ***Place the document in a variable***
  - ***Variable*** — a variable to store the generated file link.
  - ***Variable value operation***
    - ***Add** —*adds the generated file link to the variable.
    - ***Replace***  — replaces all file links stored in the variable with the generated file link (does not replace the files).
    - ***Remove*** *—* removes all file links from the variable (does not delete the files).
- ***Export template***
  - ***Create****—* create an export template to generate a file.
    - ***Name*** *—*a descriptive export template name.
    - ***System name***— a unique export template name, auto-transliterated from the template name.
    - ***Template file***— load an export template file (by selecting the ***Value*** item), specify a ***Document*** **attribute** that contains an export template file, or enter a ***formula***, ***N3*** expression, or ***DMN***table that returns such an attribute.
    - ***Output file name***— specify an ***attribute***,  ***formula**,* ***N3***  expression, or ***DMN*** table that returns the name for the generated file.
    - ***Export as PDF*** — check this box to generate a PDF file.

![Creating a new export template for the Create a Document Using a Template action](https://kb.cmwlab.com/assets/img_6389db296395a.png)

*Creating a new export template for the Create a Document Using a Template action*

- - ***Select existing****:*
    - ***Select an export template***— specify an export template that will be used to generate a new file.

_![Selecting an existing export template for the Create a Document Using a Template action](https://kb.cmwlab.com/assets/img_6389db63e2cf2.png)_

### Store a Document in a Variable

This action stores file links from the specified attributes or variables in a variable set.

_![Store a Document in a Variable action properties](https://kb.cmwlab.com/assets/img_6389e955bc155.png)_

The **General** tab provides the following properties:

- ***Variable set** —* the variable set name to store the file links. This variable set is a key-value dictionary.
- ***Value operation***
  - ***Add*** — adds the file links specified in the ***Value*** column to the variable set.
  - ***Replace***  — replaces all file links in the variable set with the file links specified in the ***Value*** column (does not replace the files).
  - ***Remove***— removes all variables and file links from the variable set (does not delete the files).
- *Variable table*
  - ***Variable name*** — a variable to store the file links specified in the ***Value*** column.
  - ***Value***  — specify the variable value (a file link) using an ***attribute***,  ***formula****,* ***N3***  expression, *or* ***DMN*** table.
  - ***Create***— click this button to add a variable.
  - ***Delete***  — check the boxes for the variables to be deleted and click this button to delete them.

### Attach a Document to an Attribute

This action stores file links from the specified attributes or variables in the attributes.

_![Attach a Document to an Attribute action properties](https://kb.cmwlab.com/assets/img_6389ebf0925c6.png)_

The **General** tab provides the following properties:

- ***Attribute** —* an attribute to store file links specified in the ***Value*** column.
- ***Value operation***
  - ***Adds***— adds file link to the attribute.
  - ***Replace***  — replaces all file links in the attribute with the file links specified in the ***Value*** column (does not replace the files).
  - ***Create*** — creates new file links in the attribute.
- ***Value** —*  set attribute value (a file link) using an **attribute**,  ***formula****,* ***N3***  expression, *or* ***DMN*** table.
- ***Create***— click this button to add an attribute.
- ***Delete***  — check the boxes for the attributes to be deleted and click this button to delete them.

### Execute on Conditions

This action executes the nested actions on the specified conditions. You can set several conditions. The nested action is executed if the conditional expression returns `true`. If none of the conditions returns `true`, the ***Execute on Conditions*** action and its nested actions are skipped.

_![Execute on Conditions action properties](https://kb.cmwlab.com/assets/img_6389f8c30c118.png)_

The **General** tab provides the following properties and buttons.

- ***Condition name***  — a brief condition description.
- ***Expression***  — a tribute, ***formula****,* ***N3***  exp ion, *or* ***DMN*** table that specifies the nested action execution condition. For each condition, a track is created inside the ***Execute on Conditions*** action for nested actions that are executed if the expression returns `true`.
- ***Create***— click this button to add a condition.
- ***Delete***  — check the boxes for the conditions to be deleted and click this button to delete them.

### Iterate by Numeric Counter

This action executes the nested actions a specified number of times.

_![Iterate by Numeric Counter action properties](https://kb.cmwlab.com/assets/img_63eb66f010005.png)_

The **General** tab provides the following properties:

- ***Variable**—*a counter variable to iterate the loop, similar to the `for` loop counter. The variable value increments from 0 to the value set in the ***Number of Iterations*** field, minus 1.
- ***Number of iterations** —* specify the loop iteration number using a numeric ***value***, ***attribute***, ***formula***, ***N3*** expression*,* *or* ***DMN*** table.

### Iterate by Object Counter

This action executes the nested actions with the objects returned by the specified ***attribute***, ***formula***, ***N3*** expression, or ***DMN*** table. The number of iterations equals the number of returned objects.

_![Iterate by Object Counter action properties](https://kb.cmwlab.com/assets/img_63eb666142ecd.png)_

The **General** tab provides the following properties:

- ***Variable**—*an iterator variable to execute the loop, similar to the `for each` loop iterator. This variable will be assigned the value of the given attribute or expression in the same way.
- ***An attribute or expression to find the objects**—* specify a value an ***attribute***,  ***formula****,* ***N3***  expression, or ***DMN*** table that returns the object references to iterate the loop through*.*

## Related Articles

**[Creating a Scenario](https://kb.comindware.ru/article.php?id=2108)**

**[Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109)**

**[Scenario Definition and List](https://kb.comindware.ru/article.php?id=2110)**

================================================
FILE: 395. Version 4/399. How-Tos/416. Scenarios/2108-creating_scenario.md
================================================
---
title: Creating a Scenario
kbId: 2108
---

# Creating a Scenario

## Creating a Scenario from the Application Scenario List

1. Open the scenario list in an application. See [Viewing the Scenario List](https://kb.cmwlab.com/article.php?id=2110#mcetoc_1ginkc2is3).
2. Click **Create**.
3. The **New scenario** window will be displayed.
4. Configure the [scenario properties](#mcetoc_1gjo9vh451).

   _![   New scenario properties windowподпись](https://kb.cmwlab.com/assets/img_638ef4685ff7a.png)_
5. Click   ***Sa*****v*****e***.
6. The scenario designer will open.
7. Configure the scenario, see [Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109).

## Creating a Scenario for a Business Process Diagram Element

1. Open a business process diagram.
2. Select a diagram element.
3. In the item menu, click **Entry scenario***![](https://kb.comindware.ru/assets/img_6387209488025.png) or* **Exit scenario***![](https://kb.comindware.ru/assets/img_638720b096fbd.png)*.
4. The diagram element entry or exit scenario will be automatically generated.
5. The scenario designer will be displayed.
6. Configure the scenario. See [Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109).

   ![Creating the scenarios for process diagram element entry and exit](https://kb.cmwlab.com/assets/img_638efd311a50e.png)

   Creating the scenarios for process diagram element entry and exit

## Scenario Properties

- **Name**  — a descriptive name of the script.
- **System name** — a unique scenario name, transliterated automatically from the scenario name.
- **Description**  — an optional comment about the scenario's purpose.
- **Execution context**  — the account on behalf of which the scenario will be executed:
  - **By system** — the scenario will be executed with full rights of the **System** account, ignoring the role and permissions of the user who initiated the start event of the scenario. That is, the scenario will be able to *perform any actions*.
  - **By initiator** — the scenario will be executed if the user who initiated the start event has sufficient rights. If the user has insufficient rights, the system will generate an error.
- **Status**  — state of the scenario:
  - **Active**— every time the start event triggers, the configured action sequence will be executed.
  - **Suspended**— when the start event triggers, the configured action sequence will not be executed.

## Related Articles

**[Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109)**

**[Scenario Definition and List](https://kb.comindware.ru/article.php?id=2110)**

**[Scenario Actions](https://kb.comindware.ru/article.php?id=2106)**

================================================
FILE: 395. Version 4/399. How-Tos/416. Scenarios/2109-configuring_scenario.md
================================================
---
title: Configuring a Scenario
kbId: 2109
---

# Configuring a Scenario

## Scenario Designer

**{{ productName }}** provides an easy-to-use visual scenario designer.

There are two ways to open the scenario designer:

1. Double-click the scenario row in the scenario list (see [Scenario Definition and List](https://kb.comindware.ru/article.php?id=2110)).
2. Click ***Entry scenario*** or ***Exit******scenario*** in the business process diagram element menu (see [Creating a Scenario for a Business Process Diagram Element](https://kb.cmwlab.com/article.php?id=2108#mcetoc_1gj3ssj8l2)).

_![Scenario designer](https://kb.cmwlab.com/assets/img_63906ed9d0478.png)_

## Scenario Configuration Buttons

The scenario designer provides the following buttons to configure the scenario.

1. ***Properties** —* configure the scenario properties. See [Scenario Properties](https://kb.cmwlab.com/article.php?id=2108#mcetoc_1gjo9vh451).
2. ***Clean*** — permanently delete all scenario elements. When you click this button, an empty ***Button click*** start event is placed in the scenario, as if the scenario was re-created.
3. ***Delete***— permanently delete the scenario.
4. ***Validate*** — check the scenario's integrity and functioning. Click this button to see the ***Validation result*** panel with a list of scenario errors.

   ![Scenario validation result](https://kb.cmwlab.com/assets/img_63907963b6c6c.png)

   Scenario validation result

## Scenario Element Configuration Buttons

Hover the mouse pointer over a scenario element to display the element configuration buttons.

1. ***Edit*** — configure the scenario element properties. See [Configuring the Scenario Elements](#mcetoc_1giv6huua1).
2. ***Go to context template*** — view the context template for scenario element execution.
3. ***Delete***  — permanently delete the scenario element.
4. ***Add action*** — create an action nested in or after the current scenario element.

   ![Scenario element configuration buttons](https://kb.cmwlab.com/assets/img_63907dcef1270.png)

   Scenario element configuration buttons

## Configuring the Scenario Elements

When you configure a scenario, the changes are saved and applied automatically.
### Configuring the Start Event

_![Scenario start event properties window](https://kb.cmwlab.com/assets/img_63908adf02d7d.png)_

1. Hover the mouse pointer over the scenario start event and click ***Edit***.
2. The start event properties window appears with the following properties.

- ***Description*** — a brief start event's purpose description.
- ***Type*** — a type of event that triggers the scenario. See the [Scenario Start Event Types and Properties](#mcetoc_1gj1c4ck70).
- ***Context template*** — the scenario will run in this record or process template when the specified event triggers.

#### Scenario Start Event Types and Properties

The start event types available in scenarios are listed below.

Some event types have additional properties to configure.

- ***Button******click*** — the scenario will run when the specified button in the ***context template*** is clicked***.***
  - ***Button*** — the button clicked to run the scenario.
- ***Record creation*** — the scenario will run when a record is created in the ***context template***.
- ***Record change*** — the scenario will run when the specified record attribute values in the ***context template*** change. If the attributes are not specified, the scenario will run when any attribute value in the ***context template*** is changed.
  - ***Attributes***— a list of ***context template*** attributes. Changes to these attribute values will trigger the scenario.
- ***Process start*** — the scenario will run when the ***context template***process instance is started.
- ***Message receipt*** — the scenario will run when a message is received through the specified connection and communication route.
  - ***Connection*** — the scenario will run when a message is received through this connection.
  - ***Communication route****—* a communication route to parse the message.
  - ***Variable name*** — a variable to store the message content parsed by the communication route.
- ***Token entry***— the scenario will run when a token enters the selected element of the ***context*** process ***template***diagram.
  - ***Diagram*** ***element*** — a token entering this process diagram element will trigger the scenario.
- ***Token exit***— the scenario will run when a token exits the selected element of the ***context*** process ***template*** diagram.
  - ***Diagram*** ***element*** — a token exiting this process diagram element will trigger the scenario.

## Configuring the Actions

### Creating an Action

1. Hover the mouse pointer over the scenario element to add an action after or inside it.
2. Click ***Add action***.
3. An of available actions will appear.
4. Select the desired action.
5. A new action will appear in the scenario designer.
6. Configure the action. See [Setting Up Action Properties](#mcetoc_1giv6k5ut4).

For detailed information about action properties, see `_![](https://kb.cmwlab.com/images/marker.png){Article-ID:2106}`[`.`](https://kb.comindware.ru/article/%d0%a2%d0%b8%d0%bf%d1%8b-%d0%b0%d0%ba%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d1%81%d1%82%d0%b5%d0%b9-1775.html)__![Creating an action in a scenario](https://kb.cmwlab.com/assets/img_63eb6556f41b0.png)_

### Creating Nested Actions

Other actions can be nested inside the ***Change the context**,* ***Execute on conditions***, ***Counter loop***, and ***Object loop*** actions.

To create a nested action, click the ***Add action*** button inside an action.

_![Creating a nested action in a scenario](https://kb.cmwlab.com/assets/img_63eb67cfc6608.png)_

### Setting Up Action Properties

1. Hover the mouse pointer over an action.
2. Click ***Edit***.
3. The action properties window appears.
4. Configure the action properties.
5. Click ***Save***.

_![Opening action properties in a scenario](https://kb.cmwlab.com/assets/img_63908d0e3269e.png)_

For detailed information about action properties, see `_![](https://kb.cmwlab.com/images/marker.png){Article-ID:2106}`[`.`](https://kb.comindware.ru/article/%d0%a2%d0%b8%d0%bf%d1%8b-%d0%b0%d0%ba%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d1%81%d1%82%d0%b5%d0%b9-1775.html)_### Deleting an Action

1. Hover the mouse pointer over the action to be deleted.
2. Click ***Delete***.
3. A delete confirmation window will appear.
4. Confirm the action deletion.

_![Deleting a scenario action](https://kb.cmwlab.com/assets/img_639094ddad17b.png)_

## Related Articles

**[Creating a Scenario](https://kb.comindware.ru/article.php?id=2108)**

**[Scenario Definition and List](https://kb.comindware.ru/article.php?id=2110)**

**[Scenario Actions](https://kb.comindware.ru/article.php?id=2106)**

================================================
FILE: 395. Version 4/399. How-Tos/416. Scenarios/2110-scenario_definition_list.md
================================================
---
title: Scenario Definition and List
kbId: 2110
---

# Scenario Definition and List

## Scenario Definition

A **S****cenario**is a validation and data processing algorithm executed when a certain event is triggered. The scenario contains an action sequence executed when the specified event is triggered.

Use the convenient visual designer to configure the scenarios.

_![A scenario example](https://kb.cmwlab.com/assets/img_63909fe24c9bf.png)_

## Viewing the Scenario List

Click **Scenarios** on the application ***Administration*** page.

_![Scripts button on the application administration page](https://kb.cmwlab.com/assets/img_638f011d12f29.png)_

_![List of scenarios in the application](https://kb.cmwlab.com/assets/img_638f00b790f11.png)_

## Details and Operations in the Scenario List

- **ID** — a unique scenario identifier.
- **Title**— a descriptive scenario name.
- **Event** — a description of the event that triggers the scenario.
- **Execution context**— the account on behalf of which the scenario will be executed:
  - **By system** — the scenario will be executed with full rights of the **System** account, ignoring the role and permissions of the user who initiated the start event of the scenario. That is, the scenario will be able to *perform any actions*.
  - **By initiator** — the scenario will be executed if the user who initiated the start event has sufficient rights. If the user has insufficient rights, the system will generate an error.
- **Status**
  - **Active**— the scenario is executed every time the specified event occurs.
  - **Paused**— the scenario is not executed when the specified event occurs.
- New — click this button to create a new scenario. See [Creating a Scenario](https://kb.comindware.ru/article.php?id=2108).
- **Delete** — check the boxes for the scenarios to be deleted and click this button to delete them.
- **Properties**— check the box for a scenario and click this button to configure its properties. See [Scenario Properties](https://kb.cmwlab.com/article.php?id=2108#mcetoc_1gjo9vh451).
- **Open**  — double-click the scenario row to open the scenario designer. See [Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109).

## Related Articles

**[[Creating a Scenario](https://kb.comindware.ru/article.php?id=2108)](https://kb.comindware.ru/article.php?id=2152)**

**[Configuring a Scenario](https://kb.comindware.ru/article.php?id=2109)**

**[Scenario Actions](https://kb.comindware.ru/article.php?id=2106)**

================================================
FILE: 395. Version 4/399. How-Tos/419. Buttons/2114-buttons.md
================================================
---
title: Buttons
kbId: 2114
---

# Buttons

## Definitions

A button is a visual element on a form that performs a configured action on a click.

## Related Articles

**[Viewing the Template Button List](https://kb.comindware.ru/article.php?id=2118)**

**[[Button List Operations](https://kb.comindware.ru/article.php?id=2119)](button_list_operations.html)**

**[Creating a Button](https://kb.comindware.ru/article.php?id=2116)**

**[[Button Designer](https://kb.comindware.ru/article.php?id=2117)](button_designer.html)**

**[Deleting a Button](https://kb.comindware.ru/article.php?id=2115)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/419. Buttons/2115-deleting_button.md
================================================
---
title: Deleting a Button
kbId: 2115
---

# Deleting a Button

## How to Delete a Button

1. Open the template [button list](https://kb.cmwlab.com/article.php?id=2118).
2. Check the box in the first column for the button to be removed.
3. Click **Delete**.

   ![Selecting a button to delete](https://kb.cmwlab.com/assets/button_delete_button.png)

   Selecting a button to delete
4. In the delete confirmation window, click **Delete**.

   ![Confirming button deletion](https://kb.cmwlab.com/assets/button_delete_confirmation.png)

   Confirming button deletion

## Related Articles

**[Viewing the Template Button List](https://kb.comindware.ru/article.php?id=2118)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/419. Buttons/2116-creating_button.md
================================================
---
title: Creating a Button
kbId: 2116
---

# Creating a Button

## How to Create a Button

1. Open the template [button list](https://kb.cmwlab.com/article.php?id=2118).
2. Click the **Create**.
3. The [button designer](https://kb.cmwlab.com/article.php?id=2117) will be displayed.
4. [Configure](https://kb.cmwlab.com/secure/button-designer-2117.html#mcetoc_1gk32u0ai2) and save the button.

_![Creating a button from the button list](https://kb.cmwlab.com/assets/button_create_button.png)_

## Related Articles

**[Viewing the Template Button List](https://kb.comindware.ru/article.php?id=2118)**

**[[Button Designer](https://kb.comindware.ru/article.php?id=2117)](button_designer.html)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/419. Buttons/2117-button_designer.md
================================================
---
title: Button Designer
kbId: 2117
---

# Button Designer

## Opening the Button Designer

The button designer allows you to customize the appearance, behavior, and result of clicking the button.

1. Open the template [button list](https://kb.cmwlab.com/article.php?id=2118).
2. Double-click a button row.
3. The button designer will be displayed.
4. [Configure the button](#mcetoc_1gk32u0ai2).
5. Click **Save**.

_![Button designer — Properties tab](https://kb.cmwlab.com/assets/button_designer.png)_

## Configuring a Button

The button designer has the following tabs to configure display options and the button click operation.

Configure the button and click **Save**.

### Properties

On the **Properties** tab, configure the general button parameters.

- **Display name** — the button label. After placing the button within a button area (on a form or a table), you can change its display name on that button area, this change will not affect the name of the original button in the template.
- **System name** - a unique button name for use in scripts, expressions, and scenarios.
- **Description** — a relevant description of the button's purpose.
- **Operation context** — defines the available operations, the operation execution context, and the ability to use the button on the corresponding forms and tables.
  - **Record** in a **record**, **account**, **role**, or **organizational unit** **template**.
  - **User task** — an element of the process diagram.
  - **Process** — **process template** or process instance.
  - **Account** — a record in an **account template**.
  - **Diagram** — a process diagram.
- **Operation** — available operation set depends on the selected **operation context**. The following operations are provided:
  - **C# Script** — execute a C# script.
  - **Start process** — launch a process instance from the current record or a new record.
  - **Stop process** — stop the current process instance.
  - **Start process from linked template** — launch the process from a record template linked to the current template.
  - **Export record** — export the record using an export template.
  - **Export table** — export a table in XLSX format.
  - **Archive** — archive a record or process instance.
  - **Unarchive** — unarchive a record or process instance.
  - **Create** — create a record.
  - **Create related record** — create a record in the template linked to the current template.
  - **Save** — save the current record.
  - **Delete** — delete a record or process instance.
  - **Reopen** — assign **In Progress** status to the task.
  - **Complete task** — complete the current process task.
  - **Defer** — this operation will be implemented in future versions of the product.
  - **Accept** — set the current account as the task assignee.
  - **Migrate** — upgrade the process instance to the latest process diagram version.
  - **Generate new token** — create a new token on the selected process instance diagram element.
  - **Link to a template** — link the account to the selected account template.
  - **Unlink from the template** — unlink the account from the selected account template.
  - **Trigger the “Button clicked” event** — the button click will trigger the **Button clicked** event, for example, to run a script in the application.
  - **Edit** — configure the process diagram.

Operations are executed on **records** in the **record**, **account**, **role**, and **organizational unit** **templates**, as well as on the **process instances** in the **process templates**.

- **Save the record after execution** — check this checkbox to save the current record upon the button click operation execution.
- **Skip validation** — if you check this checkbox, data validation won't be performed when entering and saving record data and validation errors won't be displayed.
- **Operation result** — select an action to perform upon the operation execution.
  - **Refresh data** — reload the record data.
  - **Navigation** — go to the object specified in the **Navigate to** field:
    - **Related record** — go to a record linked with the process instance.
    - **Process instance** — go to the process instance.
    - **Started process task** — go to the current task of the process instance.
    - **Next task in list** — go to the next task of the process instance.
    - **Previous page** — go to the current table previous page.
    - **Diagram** — go to the process instance diagram.
    - **Table** — go to a table listing template records or process instances.
  - **Download document** generated using an export template.
- **Set form access mode**
  - **Read** — on the button click the form will become read-only.
  - **Edit** — after clicking the button the user will be able to enter data into the form (subject to the appropriate permissions).
  - **No change** — use the original form access mode.
- **Show the button** — use this dropdown together with the **Set form access mode** dropdown.
  - **In edit mode** — the button will be displayed only in the form data entry mode.
  - **In read mode** — the button will be displayed only in the form read-only mode.
  - **Always** — the button will be displayed in data entry and read-only modes.
- **Show the dialog** — if you check this checkbox, clicking the button will open the operation confirmation dialogue you configure.
  - **Configure the dialog** — go to the operation confirmation [form designer](../forms/form_designer.html#form-designer). The element panel in this designer shows the operation **[local variables](#local-variables)** that you can drag and drop on the dialogue.

_![Operation dialogue designer with a local variable](https://kb.cmwlab.com/assets/button_designer_dialogue_designer.png)_

### Script

On the **Script** tab, you can enter a C# script to execute on the button click.

To generate a C# script template, click **Generate C# template**.

_![Button designer — Script tab with a C# script template](https://kb.cmwlab.com/assets/button_designer_script.png)_

### Display Condition

On the **Display condition** tab, you can configure a formula or N3 expression. The button will be displayed if the formula or N3 expression returns `true`. Otherwise, the button will be hidden.

_![Button Designer — Display condition tab with a formula](https://kb.cmwlab.com/assets/button_designer_display_condition.png)_

### Local Variables

On the **Local variables** tab, you can create variables to use in a C# script or scenario executed on the button click.

Local variables are essentially the attributes.

For each variable, you can set:

- **Display name** — a relevant variable name.
- **Data type** — variables have the same types as attributes.
- **Display format** — variables have the same display formats as attributes.
- **System name** — a unique variable name for use in scripts, expressions, and scenarios.
- **Description** — a relevant variable's purpose description.
- **Template** — can be set for the following variable types: **Record**, **Account**, **Role**, and **Organizational Unitattribute\_organizational\_unit.md**.
- **Store multiple values** — you can check this checkbox for the following variable types: **File** (see attribute types **Document**, **Image**), **Record**, **Account**, **Role**, and **Organizational Unit**.

_![Button Designer - Local Variables Tab](https://kb.cmwlab.com/assets/button_designer_local_variables.png)_

### Relations

The **Relations** tab displays the list of all application objects and resources associated with the button.

_![Button designer — Relations tab](https://kb.cmwlab.com/assets/button_designer_relations.png)_

## Related Articles

**[Viewing the Template Button List](https://kb.comindware.ru/article.php?id=2118)**

**[[Creating a Button](https://kb.comindware.ru/article.php?id=2116)](button_creation.html)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/419. Buttons/2118-template_button_list.md
================================================
---
title: Viewing the Template Button List
kbId: 2118
---

# Viewing the Template Button List

## How to Open the Button List

The list of buttons is provided for templates of all types.

1. Open a template.
2. Go to the **Buttons** tab.
3. The list of buttons in the template opens.

_![Template button list](https://kb.cmwlab.com/assets/button_list.png)_

## Related Articles

**[Button List Operations](https://kb.comindware.ru/article.php?id=2119)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/419. Buttons/2119-button_list_operations.md
================================================
---
title: Button List Operations
kbId: 2119
---

# Button List Operations

## Available Operations

The [button list](https://kb.cmwlab.com/article.php?id=2118) provides the following operations and buttons.

- **Select** — check a box in the first column to select the button.
- **Open** — double-click a button row to open the [button designer](https://kb.cmwlab.com/article.php?id=2117).
- **Create** — [create a new button](https://kb.cmwlab.com/article.php?id=2116).
- **Delete** — [delete a button](https://kb.cmwlab.com/article.php?id=2115) (displayed when one button is selected).
- **Search** — click this button and enter keywords in the **Search** field. The lines containing the keywords will be shown.

## Related Articles

**[Viewing the Template Button List](https://kb.comindware.ru/article.php?id=2118)**

**[Creating a Button](https://kb.comindware.ru/article.php?id=2116)**

**[Button Designer](https://kb.comindware.ru/article.php?id=2117)**

**[Deleting a Button](https://kb.comindware.ru/article.php?id=2115)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/420. Forms/2120-template_form_list.md
================================================
---
title: Viewing the Template Form List
kbId: 2120
---

# Viewing the Template Form List

## How to Open the Form List

The form list is available for record template, account template, role template, and organizational unit template.

In the process template the form list is not available, and forms are created and configured using the process diagram element properties.

1. Open a record template, account template, role template, or organizational unit template.
2. Select the **Forms** tab.
3. The list of forms in the template opens.

![Template form list](https://kb.cmwlab.com/assets/form_list.png)\*

Template form list

## Related Articles

**[Operations In the Form List](https://kb.comindware.ru/article.php?id=2123)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/420. Forms/2122-deleting_form.md
================================================
---
title: Deleting a Form
kbId: 2122
---

# Deleting a Form

## How to Delete a Form

1. Open the [form list](https://kb.cmwlab.com/article.php?id=2120) template.
2. Check the box in the first column for the form to be deleted.
3. Click **Delete**.

   ![Selecting the form to delete](https://kb.cmwlab.com/assets/form_delete_button.png)

   Selecting the form to delete
4. In the delete confirmation window, click **Delete**.

   ![Confirming form deletion](https://kb.cmwlab.com/assets/form_delete_confirmation.png)

   Confirming form deletion

## Related Articles

**[Viewing the Template Form List](https://kb.comindware.ru/article.php?id=2120)**

**[[Operations In the Form List](https://kb.comindware.ru/article.php?id=2123)](form_list_operations.html)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/420. Forms/2123-form_list_operations.md
================================================
---
title: Operations In the Form List
kbId: 2123
---

# Operations In the Form List

## Available Operations

The [form list](https://kb.cmwlab.com/article.php?id=2120) provides the following operations and buttons.

- **Select** — check a box in the first column to select a form.
- **Open** — double-click a form row to open the [form designer](form_designer.html).
- **Create** — [create a new form](https://kb.cmwlab.com/article.php?id=2121).
- **Delete** — [delete a form](https://kb.cmwlab.com/article.php?id=2122) (the button is displayed when one form is selected).
- **Default** — click this button set the selected form as default for viewing the template records (the button is displayed when one form is selected).
- **Search** — click this button and enter keywords in the **Search** field. The lines containing the keywords will be shown.

## Related Articles

**[Viewing the Template Form List](https://kb.comindware.ru/article.php?id=2120)**

**[Form Designer](https://kb.comindware.ru/article.php?id=2121)**

**[Deleting a Form](https://kb.comindware.ru/article.php?id=2125)**

**[`![](https://kb.cmwlab.com/images/marker.png)Deleting a Form {Article-ID:2122}`](form_deletion.html)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/420. Forms/2124-forms.md
================================================
---
title: Forms
kbId: 2124
---

# Forms

## Definitions

A form is a web page designed to enter and display data. You can place fields associated with attributes, static text, and various visual elements on the form.

## Related Articles

**[Viewing the Template Form List](https://kb.comindware.ru/article.php?id=2120)**

**[[Operations In the Form List](https://kb.comindware.ru/article.php?id=2123)](form_list_operations.html)**

**[[Form Designer](https://kb.comindware.ru/article.php?id=2121)](form_creation.html)**

**[Deleting a Form](https://kb.comindware.ru/article.php?id=2125)**

**[`![](https://kb.cmwlab.com/images/marker.png)Deleting a Form {Article-ID:2122}`](form_deletion.html)**

 [Back to top](#)

================================================
FILE: 395. Version 4/399. How-Tos/420. Forms/2125-form_designer.md
================================================
---
title: Form Designer
kbId: 2125
---

# Form Designer

## Opening the Form Designer

Use the form designer to configure the form layout, properties, and [elements](#form-elements).

1. Open the template [form list](https://kb.cmwlab.com/article.php?id=2120).
2. Double-click a form row.
3. The form designer will be displayed.
4. [Configure the form](#mcetoc_1gk35dl3l5).

   ![Form Designer](https://kb.cmwlab.com/assets/form_designer.png)

   Form Designer

## Form Designer Elements

1. Element panel — a palette of [elements](#mcetoc_1gk35dl3l4) to drag onto the form: attributes and visual elements. See [Element Panel Operations](#mcetoc_1gk35dl3l7). Use this panel to:
   - Drag and drop elements on the form layout.
   - Search for elements.
   - Filter element list by element type.
   - Create and edit attributes, buttons, and forms.
2. Form layout sets the form's visual appearance.
3. Properties panel — view and configure the properties of the selected element.
4. Buttons:
   - **Save** — save the form.
   - **Clear** — remove all elements from the form layout.
   - **Clone** — [create a form duplicate](#mcetoc_1gk35dl3lb).
   - **Configure template** — go to the template **Properties** page.
   - **Relations** — view a list of application objects that use the form.

## Form Properties

1. **Display name** — the form name that will be displayed in its header when viewing template records.
2. **System name** — a unique form name, for use scripts, expressions, and scenarios.
3. **Is default** — check this box to display this form by default when viewing template records.
4. **Type**:
   - **Public** — select this type for the form to be viewed using the form selection dropdown next to the form title.
   - **Internal** — select this type for the form to be displayed only if it is embedded in another form or is set as a record form (eg. for process start, record creation, dialogues).

## Form Elements

You can place the following elements on the form.

- **Region** — contains all other form elements. You can drag other elements only onto the area. The form must have at least one region. There can be several areas on a form.
- **Tabs** — arrange form elements on several tabs.
- **Columns** — arrange elements in several columns.
- **Static text** — arbitrary text with HTML formatting.
- **Attribute field** — when you drag an attribute to the form layout, a field associated with the attribute is created. Field properties correspond to the associated attribute type.
- **Embedded form** — you can drag another form onto the form layout to embed it into the current form.
- **Button area** — provided for each form and each area. Buttons can be placed only in the button areas.
- **Button group** — combines buttons into a dropdown.
- **Button Separator** — visually separates buttons within button areas.

## Configuring the Form

1. Drag the required [elements](#mcetoc_1gk35dl3l4) from the elements panel to the form layout.
2. To set the [form properties](#mcetoc_1gk35dl3l3), click an empty layout area and configure the properties using the properties panel.
3. To set the properties of a form element, select it in the layout and configure the properties in the properties panel.
4. Click **Save**.

## Editing the Form Rules

1. Click the selector button next to the form title in the designer.
2. Select **Form Rules** from the dropdown.
3. The rule builder for the form is displayed.
4. Edit the form rules.
5. Click **Save**.

   ![Jump menu to form rules designer](https://kb.cmwlab.com/assets/form_designer_goto_form_rules.png)

   Jump menu to form rules designer

## Element Panel Operations

### Creating an Attribute

1. In the element panel:
   - Hover over the **Attributes** heading to create an attribute in the current template, or…
   - Hover over the template name in the element list to create an attribute in the corresponding template.
2. Click the **Add Attribute** button that appears.
3. The attribute creation window will be displayed.

   ![Creating an attribute using the form designer](https://kb.cmwlab.com/assets/form_designer_create_attribute.png)

   Creating an attribute using the form designer

### Editing an Attribute, Button, or Form

1. Hover the mouse pointer over an attribute, button, or form name in the elements panel.
2. Click **Edit Attribute**, **Edit Button**, or **Edit Form** button that appears.
3. The attribute properties window, the [button designer](https://kb.cmwlab.com/article.php?id=2117), or the [form designer](#mcetoc_1gk35dl3l2) will be displayed.

   ![Editing a form using the form designer](https://kb.cmwlab.com/assets/form_designer_edit_form.png)

   Editing a form using the form designer

### Creating a Button

1. In the element pane, hover over the **Buttons** heading.
2. Click the **Add button** button that appears.
3. The button creation page will be displayed.

   ![Creating a button in the form designer](https://kb.cmwlab.com/assets/form_designer_create_button.png)

   Creating a button in the form designer

## Cloning a Form

1. Click **Clone**.
2. In the form cloning window, enter the form **name** and **system name**.
3. Click **Save**.
4. The new form will be opened in the form designer.

   ![Form cloning](https://kb.cmwlab.com/assets/form_designer_clone_form.png)

   Form cloning

## Related Articles

**[Viewing the Template Form List](https://kb.comindware.ru/article.php?id=2120)**

**`![](https://kb.cmwlab.com/images/marker.png)Creating a Form {Article-ID:2121}`**

 [Back to top](#)

================================================
FILE: 395. Version 4/400. Expression examples/411. N3 language/2024-calculate_objects_condition.md
================================================
---
title: Calculation of objects that meet the condition
kbId: 2024
---

# Calculation of objects that meet the condition

Task example: in the table on the project form, it is necessary to display only those employees who have the skills necessary for the project. An employee is displayed only if all the requested skills are present.

The project "Space tourism", the necessary skills to work in the project: Astronomy, Foreign languages, Logistics.

Employee #1 has the following skills: Astronomy, Logistics, Programming, Network technologies.

Employee #2 has the following skills: Web design, Astronomy, Foreign languages, Logistics.

Employee #1 does not have all the required skills to participate in the project and does not need to be displayed in the table. And employee #2 has all the necessary skills, so he needs to be displayed.

Data model:

- Record template "Projects" (projects):
  - Attribute "Required skills" (required\_skills), referring to the record template "Skills" (multiple values);
  - Attribute "Employees fit for the project", referring to the record template "Employees" (multiple values).
- Record template "Employees" (employees):
  - Attribute "Employee skills" (available\_skills), referring to the record template "Skills" (multiple values).
- Record template "Skills".

In order to calculate objects that meet the condition specified in the main object (in this case, employees with the necessary skills), enter the following expression:

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
@prefix cmw: <http://comindware.com/logics#>.
{
    ("projects" "required_skills") object:findProperty ?PropertyLittle. 
    ("employees" "available_skills") object:findProperty ?PropertyBig.

    ?container object:alias "employees". 
    ?allObjs cmw:container ?container.

    {
        ?item ?PropertyLittle ?resultL.
        ?allObjs ?PropertyBig ?resultL.
    } assert:count ?c.

    {
        ?item ?PropertyLittle ?resultA.
    } assert:count ?d.
    
    if {?c == ?d}
    then {?allObjs -> ?value.}
}

```

================================================
FILE: 395. Version 4/400. Expression examples/411. N3 language/2104-calculate_child_records.md
================================================
---
title: Calculating child records of all levels of the tree structure
kbId: 2104
---

# Calculating child records of all levels of the tree structure

In **CMW Platform** it is possible to create mutual links both between record templates and within a single record template, for example, to build a tree structure (works, departments, etc.). This article is applicable in the case of implementing a tree structure of relationships and provides an example of an expression for obtaining all child records of a record, taking into account all levels the tree structure.

```

@prefix object: <http://comindware.com/ontology/object#>.
@prefix assert: <http://comindware.com/logics/assert#>.
{
    ("Projectworks" "Childrenworks") object:findProperty ?CWprop.
    ("Projectworks " "Allchildrenworks") object:findProperty ?ACWprop.
   
    (
               {?item ?CWprop ?value.}
        {
            ?item ?CWprop ?CW.
            ?CW ?ACWprop ?value.
        }
    )assert:union true
}

```

**where****:**

***Projectworks*** — the system name of the record template, where the tree structure of the relationships is implemented (in this example, it is “Project Works”);

***Childrenworks*** — the system name of an attribute with the "Record" data type, which is located in the specified record template, refers to it, and which stores the relationship for child records;

***Allchildrenworks*** — the system name of an attribute with the "Record" data type, which is located in the specified record template, and in which this calculation occurs (i.e., we reuse the calculated attribute in which this calculation occurs).

================================================
FILE: 395. Version 4/400. Expression examples/411. N3 language/2107-task_object_value.md
================================================
---
title: Calculating the Display Value of an Object Associated with a Task
kbId: 2107
---

# Calculating the Display Value of an Object Associated with a Task

In **CMW Platform** one can calculate the system task table in a separate record template in order to display more task parameters and set up more convenient grouping (for example, by related object). At the same time, each of the attribute/parameters must be created in such a record template, and in each of them a calculated expression in the N3 language must be configured. This article provides an example of an expression to calculate the display name of the record that the task is associated with.

```

@prefix task: <http://comindware.com/ontology/task#>.
@prefix cmwui: <http://comindware.com/ontology/ui#>.
@prefix cmw: <http://comindware.com/logics#>.

{

?item task:objectId ?objectId.
?objectId cmw:container ?cmwcontainer.
?cmwcontainer cmwui:displayNamePredicate ?cmwuidisplayNamePredicate.
?objectId ?cmwuidisplayNamePredicate ?value.

}

```

================================================
FILE: 395. Version 4/400. Expression examples/411. N3 language/2126-substitution_parameters_calc.md
================================================
---
title: Calculating substitution parameters
kbId: 2126
---

# Calculating substitution parameters

**CMW Platform** has a system substitution functionality available by default to system administrators. This functionality allows you to appoint deputies for the period of absence of a certain employee, indicating the delegated roles. Deputies can complete tasks for an absent employee during the replacement period and perform other actions based on the delegated roles. Since the Substitution section is part of the system administration, information about the availability of current substitutions or information about the deputies of a particular employee is not available to end users by default. If you need to show any information about employee substitutions or set up any calculations that take into account substitutions, this article is for you.

In order to be able to connect to the substitution parameters library in the N3 expression, the following prefix must be used:

@prefix substitution: <<http://comindware.com/ontology/substitution>#>.

This prefix stores the following substitution parameters:

- name — substitution’s short description;
- deputies — one or several employees who will be replacing the absentee in the system;
- absentee — a person who needs to be substituted during the substitution period;
- roles — delegated roles;
- startDate — start of the substitution period;
- endDate — end of the substitution period.

In order to get the value of a particular parameter, you need to use the following predicate construction: *substitution:parameter*.

================================================
FILE: 395. Version 4/400. Expression examples/412. C# language/2088-upload_file.md
================================================
---
title: Uploading a file from a local folder
kbId: 2088
---

# Uploading a file from a local folder

To add a file from a local folder on your computer to an attribute with the “Document” data type, enter the following expression:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
using System.IO;
 
class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
        try
        {
            var id = userCommandContext.ObjectIds[0];
            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{id}, new []{"Path"});
            var path = data[id]["Path"].ToString();
            var fs = new FileStream(@path, FileMode.OpenOrCreate);
            var arrayTitle = path.Split('\\','/');
            var arrayExtension = path.Split('.');
            var docData = new Document
            {
                Title = arrayTitle[arrayTitle.Length-1],
                Extension = arrayExtension[arrayExtension.Length-1]
                };
            string doc = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(docData, fs, "");
            Api.TeamNetwork.ObjectService.EditWithAlias(id, new Dictionary<string,object>{{"Attachment",doc}});
        }
        catch
        {
            var result1 = new UserCommandResult
            {
                Success = true,
                Commited = true,
                ResultType = UserCommandResultType.Notificate,
                Messages = new[]
                {
                    new UserCommandMessage
                    {
                        Severity = SeverityLevel.Normal,
                        Text = "Error"
                        }
                }
            };
            return result1;
        }
        var result = new UserCommandResult
        {
            Success = true,
            Commited = true,
            ResultType = UserCommandResultType.Notificate,
            Messages = new[]
            {
                new UserCommandMessage
                {
                    Severity = SeverityLevel.Normal,
                    Text = "Success"
                    }
            }
        };
        return result;
    }
}

```

**where:**

***Path***— system name of the attribute with the "Text" data type, which stores the path to the file that needs to be uploaded into the system (for example, *C:\myfolder\1.cs*);

***Attachment***— system name of the attribute with the "Document" data type where you want to upload the file.

================================================
FILE: 395. Version 4/400. Expression examples/412. C# language/2095-add_group_accounts.md
================================================
---
title: Adding users to a group
kbId: 2095
---

# Adding users to a group

In order to enable a process to add a user or users to a specific system group (for example, to manage the role model), enter the following expression:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
{
string[] OA = new string[] {
"Clients"
};
string[] OP = new string[] {
"Manager"
};
string[] GROUP = new string[] {
"group.28"
};

for(int j = 0; j < GROUP.Length; j++)
{
var group = GROUP[j];
var old_users = Api.Base.AccountGroupService.Get(group);
Api.Base.AccountGroupService.ExcludeMembers(group, old_users.Users);

var my_list = Api.TeamNetwork.ObjectService.ListWithAlias(OA[j]);
foreach (var i in my_list)
{
var data = i as Dictionary<string,object>;
data.TryGetValue(OP[j], out object obj);
if (obj == null)
{
continue;
}

if (obj is string)
{
Api.Base.AccountGroupService.IncludeMembers(group, new List<string>(){ obj.ToString() }); ÿ
}
else
{
var accounts = obj as object[];
var accountsIds = accounts.Select(x => x.ToString());
Api.Base.AccountGroupService.IncludeMembers(group, accountsIds);
}
}
}
}
}

```

**where:**

***Clients*** — system name of the record template;

***Manager*** — system name of the attribute of the "Account" data type in the specified record template;

***group.28*** — ID of a system group.

This script, when called, firstly removes all users from the group, and then iterates through all records in the specified record template and adds users from the specified attribute to the group, thus updating the composition of the system group.

================================================
FILE: 395. Version 4/400. Expression examples/412. C# language/2097-upload_list_folder.md
================================================
---
title: Uploading attachments to a local folder
kbId: 2097
---

# Uploading attachments to a local folder

To save the attached file(s) from an attribute with the "Document" data type to a local folder, enter the following expression:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
using System.IO;
 
class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
                              try
                              {
                                             var path = @"C:\document\";
                                             var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new string[] {userCommandContext.ObjectIds[0]}, new string[] {"Document"});
                                             var documentIdsObj = data[userCommandContext.ObjectIds[0]]["Document"];
               var documentIds = documentIdsObj as IEnumerable<object>;
                                             if (documentIds == null)
                                             {
                                                            documentIds = new string[] {documentIdsObj as string};
                                             }
                                             foreach (var documentIdObj in documentIds)
                                             {
                                                            var documentId = documentIdObj as string;
                                                            var documentData = Api.TeamNetwork.DocumentService.GetContent(documentId);
                                                            var documentInfo = Api.TeamNetwork.DocumentService.GetDocument(documentId);
                                                            var docData = new Document
                                                            {
                                                                           Title = documentData.Name,
                                                                           Extension = documentInfo.Extension
                                                            };
                                                            var stream = new MemoryStream();
                                                            stream.Write(documentData.Data, 0, documentData.Data.Length);
                                                            stream.Seek(0, SeekOrigin.Begin);
                                                            var filepath = path + documentData.Name;
                                                            using(FileStream outstr = new FileStream(filepath, FileMode.Create))
                                                            {
                                                                           stream.CopyTo(outstr);
                                                            }
                                             }
                              }
                              catch
                              {
                                             var badresult = new UserCommandResult
                                             {
                                                            Success = true,
                                                            Commited = true,
                                                            ResultType = UserCommandResultType.DataChange,
                                                            Messages = new[]
                                                            {
                                                                           new UserCommandMessage
                                                                           {
                                                                              Severity = SeverityLevel.Normal,
                                                                              Text = "Failed to upload"
                                                               }
                                                            }
                                 };
                                 return badresult;
                              }
                              var result = new UserCommandResult
                              {
                                             Success = true,
                                             Commited = true,
                                             ResultType = UserCommandResultType.DataChange,
                                             Messages = new[]
                                             {
                                                            new UserCommandMessage
                                                            {
                                                               Severity = SeverityLevel.Normal,
                                                               Text = "Success"
                                                }
                                             }
                  };
                  return result;
    }
}

```

**where:**

***C:\document\*** — path for uploading file/s;

***Document*** – system name of the attribute with the "Document" data type.

================================================
FILE: 395. Version 4/400. Expression examples/412. C# language/2099-delete_related_record.md
================================================
---
title: Deleting a related object when a condition is met
kbId: 2099
---

# Deleting a related object when a condition is met

In order to delete the associated object in the context of a process if a certain condition is met (in this article the condition is the following: the value in the attribute with the data type "Number" in the associated object is zero), enter the following expression:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
{
try
{
var id = context.BusinessObjectId;
var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{id}, new[]{"Link"});
var deleteid = data[id]["Link"].ToString();

var atr = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{data[id]["Link"] as string}, new[]{"Qty"});
var val = atr[data[id]["Link"] as string]["Qty"];

if(int.Parse(val.ToString()) == 0)
{
Api.TeamNetwork.ObjectService.Delete(deleteid);
}
}
catch
{}
}
}

```

**where:**

***Link***— system name of the attribute with the "Record" data type in the current record template;

***Qty***— system name of the attribute with the "Number" data type in the associated record template.

================================================
FILE: 395. Version 4/400. Expression examples/412. C# language/2101-goto_showcase_record.md
================================================
---
title: Navigating to the object from the storefront widget
kbId: 2101
---

# Navigating to the object from the storefront widget

In order to be able to switch from the product card in the storefront widget to the object form, enter the following expression:

```

using System; 
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;

class Script
{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    { 
                    var objectid = userCommandContext.ObjectIds[0];
        var result = new UserCommandResult()
        {

Success = true,
            Messages =  null,

ResultType = UserCommandResultType.Navigate ,
            NavigationResult = new UserCommandNavigationResult
            {
                ContainerId = "oa.8",
                ObjectId = objectid,
                Context = ContextType.Record
            }
        };
        return result;
    }
}

```

**where:**

***oa.8*** — ID of the record template where the objects from the storefront are located.

================================================
FILE: 395. Version 4/400. Expression examples/412. C# language/2128-download_table_entries.md
================================================
---
title: Exporting Selected Records from a Custom Table
kbId: 2128
---

# Exporting Selected Records from a Custom Table

This script is designed to download selected records from the table, taking into account user settings. That is, the user selects the columns and records that should be uploaded to Excel. Records are selected with a checkmark in the leftmost column, and columns are configured through the "***My settings***"-> "***Customize display***" button.

The script works with attributes with data type:

- Boolean;
- Number;
- Duration;
- Text;
- Record;
- Date and time;
- Account.

```

using System;
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
using Comindware.TeamNetwork.Api.Data.Forms;
using Comindware.Platform.Api.Data;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Tables;

class Script
{
public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
{
var items = userCommandContext.ObjectIds as string[];
if(items.Count() > 0)
{
try
{
var listId = userCommandContext.Query.DatasetId;
var paging = userCommandContext.Query.Paging;
var sorting = userCommandContext.Query.Sorting;
var filtr = userCommandContext.Query.Filter;
var containerId = Api.Base.OntologyService.GetAxioms(items.First())["container"].First().ToString();
var dataTablts = Api.TeamNetwork.DatasetService.GetQueries(containerId);

Dataset dataset;
Workbook workbook = new Workbook();
Worksheet wh = workbook.Worksheets[0];

var style = workbook.CreateStyle();
var flag = new StyleFlag();
flag.NumberFormat = true;

foreach(var table in dataTablts)
{
table.Paging = paging;
table.Sorting = sorting;
table.Filter = filtr;
if(table.DatasetId == listId)
{
var personaldataset = Api.TeamNetwork.DatasetConfigurationService.GetPersonalDataset(table.DatasetId);
dataset = Api.TeamNetwork.DatasetService.QueryData(table);
var columnsTabale = new Container[personaldataset.Columns.Count()];
var i=0;
foreach(var coll in personaldataset.Columns)
{
if(!coll.IsHidden)
{
columnsTabale[i] = new Container(coll.DataSourceInfo.Id, i);
wh.Cells[0,i].PutValue(coll.Name);
var prop = coll.DataSourceInfo.PropertyPath.Last().ToString();

if(prop != "id" && prop != "lastWriteDate" && prop != "creationDate" && prop != "archived" && prop != "creator")
{
var propData = Api.Base.OntologyService.GetAxioms(prop);
prop = propData["propertyType"].Last().ToString();
}

switch(prop)
{
case "xsd.decimal":
{
style.Number = 1;
wh.Cells.Columns[i].ApplyStyle(style, flag);
}break;
case "lastWriteDate":
{
style.Number = 22;
wh.Cells.Columns[i].ApplyStyle(style, flag);
wh.Cells.Columns[i].Width = 15;
}break;
case "creationDate":
{
style.Number = 22;
wh.Cells.Columns[i].ApplyStyle(style, flag);
wh.Cells.Columns[i].Width = 15;
}break;
case "xsd.dateTime":
{
style.Number = 22;
wh.Cells.Columns[i].ApplyStyle(style, flag);
wh.Cells.Columns[i].Width = 15;
}break;
}
i++;
}
}
var j=1;
var y = 0;
foreach(var coll in dataset.Columns)
{
try
{
var ds = coll.DataSourceInfo.Id;
var t = Array.Find(columnsTabale, x=> x.DS == ds).Id;
columnsTabale[t].Place = y;
}catch{}
y++;
}

foreach(var row in dataset.Rows)
{
if(Array.Find(items, v => v == row.Id) != null)
{
var rowData = row.Data;
for(var jj = 0; jj < i; jj++)
{
var ii = columnsTabale[jj].Place;
if(rowData[ii] != null)
{
if(rowData[ii].GetType() != typeof(Comindware.TeamNetwork.Api.Data.Forms.AccountReference) && rowData[ii].GetType() != typeof(System.Boolean) && rowData[ii].GetType() != typeof(Comindware.Platform.Api.Data.Reference))
{
wh.Cells[j,jj].PutValue(rowData[ii]);
}
else if (rowData[ii].GetType() == typeof(Comindware.TeamNetwork.Api.Data.Forms.AccountReference))
{
wh.Cells[j,jj].PutValue(((AccountReference)rowData[ii]).Name);
}
else if(rowData[ii].GetType() == typeof(System.Boolean))
{
if((bool)rowData[ii])
{
wh.Cells[j,jj].PutValue("True");
}
else
{
wh.Cells[j,jj].PutValue("False");
}
}
else if(rowData[ii].GetType() == typeof(Comindware.Platform.Api.Data.Reference))
{
wh.Cells[j,jj].PutValue(((Comindware.Platform.Api.Data.Reference)rowData[ii]).Name);
}
}
}
j++;
}
}
ListObject listObject = wh.ListObjects[wh.ListObjects.Add(0,0, j-1,i-1, true)];
}
}

MemoryStream stream = new MemoryStream();
workbook.Save(stream, SaveFormat.Xlsx);

var result = new UserCommandResult
{
Success = true,
Commited = true,

File=new UserCommandFileResult(){
Content = stream.ToArray(),
Name = "File.xlsx"
},

Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = "Success"
}
}
};
return result;

}
catch
{
var result1 = new UserCommandResult
{
Success = false,
Commited = true,
Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = "Failure"
}
}
};
return result1;
}
}
else
{
var result1 = new UserCommandResult
{
Success = false,
Commited = true,
Messages = new[]
{
new UserCommandMessage
{
Severity = SeverityLevel.Normal,
Text = "Failure"
}
}
};
return result1;
}
}

public class Container
{
public int Id {get;set;}
public int Place {get;set;}
public string DS {get;set;}

public Container(string ds , int id )
{
DS = ds; Id = id;
}
}
}

```

================================================
FILE: 395. Version 4/400. Expression examples/413. Expression language/2086-call_related_data.md
================================================
---
title: Retrieving Related Data
kbId: 2086
---

# Retrieving Related Data

In order to retrieve the data of an associated record template using an attribute with the “Record” data type that references the required record template, add the "***->***" character and the system name of the associated record template attribute that needs to be called.

| Record template | Attributes |
| --- | --- |
| Car | Driver – system name of the attribute of the "Record" type that references the “Staff” record template |
| Staff | Name – system name of the attribute |

To retrieve the name of a driver from thr “Car” entry, use the following expression: ***$Driver->Name***.

You can use the links an unlimited number of times, but be careful not to create a loop.

================================================
FILE: 395. Version 4/400. Expression examples/413. Expression language/2087-expression_language_operators.md
================================================
---
title: List of Comindware Expression Language Operators
kbId: 2087
---

# List of Comindware Expression Language Operators

This article provides the syntax and usage of operators in the CMW Platform Expression Language.

| from |  |
| --- | --- |
| Description | The query expression must begin with the ***from*** operator. The query expression can also contain subqueries also starting with ***from***. The ***from*** operator consists of the following components:  The data source which the request is made for (for example, record template, user database, etc.).A local variable that represents each element of the data source (for example, an entry in a template or a user account). |
| Syntax | from *variable* in *datasource* |
| Arguments | variable: local variabledatasource: record template or user database |
| where |  |
| Description | The ***where***operator is used in a query expression and determines which elements from the data source will be returned. It applies a boolean condition (predicate) to each element of the source (represented by a local variable) and returns those elements for which the condition is true. A single query expression can contain multiple ***where*** statements, and a single ***where*** statement can contain multiple predicates. |
| Syntax | where *predicate* |
| Arguments | Predicate: A Boolean value or an expression that evaluates to a Boolean value. |
| select |  |
| Description | In a query expression, the ***select*** operator determines which property of the object will be the result of the query. The final result takes into account both the work of previous operators and any expressions in the ***select*** operator itself. |
| Syntax | Select *object\_property* |
| Arguments | Object\_property: record template attribute, database field, etc. |

The following words cannot be used as local variables:

- item;
- source;
- db;
- group;
- any word that starts with an underscore (\_).

================================================
FILE: 395. Version 4/400. Expression examples/413. Expression language/2094-calculate_hyperlink.md
================================================
---
title: Calculating a hyperlink to a record
kbId: 2094
---

# Calculating a hyperlink to a record

In order to calculate a link to a specific record in the system, for example, to be sent in a notification, enter the following expression:

```
FORMAT("<a href=https://cmw.com/#form/oa.2/form.3/{0}>Request</a>",LIST($id))
```

**where:**

***https://cwm.com/#form/oa.1/form.1*** — link to the entry form;

***Request***— the displayed text;

***$id*** — record ID.

The calculated attribute must be in the HTML display format to display the link correctly.

================================================
FILE: 395. Version 4/401. Troubleshooting/1949-buttons_not_shown.md
================================================
---
title: Buttons are not displayed
kbId: 1949
---

# Buttons are not displayed

As part of creating a solution, buttons are often configured with the help of which users can perform certain operations (save a record, export a record to a customized template, initiate a process, etc.). Buttons can be located both in the upper panel of tables and forms, and on the forms themselves.

What if you customize and place the buttons, but the users can't see them?

**Solution**

1. Check the user role permissions settings. The «Use buttons» flag next to the button must be checked.
2. Check the button’s display condition. To do this, go to the button’s settings, then to the «Display condition» tab. Make sure that the expression, if it is written there, is correct.

================================================
FILE: 395. Version 4/401. Troubleshooting/1951-reference_field_empty.md
================================================
---
title: Reference field is empty
kbId: 1951
---

# Reference field is empty

When configuring the attributes for a record template in **CMW Platform**, it is possible to create a reference attribute to select values from a list of records in another record template.

Sometimes a user may face a situation when there is no possibility of choosing any of the values in the reference field on the form. One of the reasons may be an incorrectly configured property of the displayed attribute in the referenced record template. Another reason may be insufficient role permissions configuration.

**Solution:**

1. Go to the settings of the record template that the attribute refers to and open the «Attributes» tab.
2. In the opened list, find the displayed attribute whose values ​​will be shown when referencing the current record template. As a rule, this is a text field with the name of the entry, which uniquely identifies it, for example, the name of the Client, Project or Agreement.
3. If the displayed attribute is calculated, check that the expression you wrote is correct.
4. If items 1-3 have been worked out, and the values ​​in the reference field did not appear for the user, check the settings of permissions in his/her role. The template referenced by the link attribute must have view permissions.

**Note:** If there is no display attribute chosen, the record IDs will be displayed in the reference field by default.

================================================
FILE: 395. Version 4/401. Troubleshooting/1953-invalid_instance_reference.md
================================================
---
title: Invalid instance hyperlink
kbId: 1953
---

# Invalid instance hyperlink

If a user receives a system notification about a task assigned to him/her, and when he/she clicks on a link to a task, the system either gives an error or leads him/her to the wrong place, then most likely the system notifications were configured incorrectly.

Pay special attention to which external server address is specified in the global configuration. It must match the current URL.

================================================
FILE: 395. Version 4/401. Troubleshooting/1962-process_fails_several_records.md
================================================
---
title: Can&#039;t start a process based on several records
kbId: 1962
---

# Can&#039;t start a process based on several records

In **CMW Platform** you can configure a button to start a process by a record. However, the possibility to select multiple records on the list can be somewhat confusing. It is impossible to start a process based on several records, since conflicts in attributes, actions, rules, etc. will arise.

Thus, one process = one record.

**Solution:**

If you still want to provide users with the ability to select several records to start the process, then you will need to create a button with the script operation that will start a process for each record, or start a related process using several records.

================================================
FILE: 395. Version 4/401. Troubleshooting/1964-script_operation_error.md
================================================
---
title: Script operation error
kbId: 1964
---

# Script operation error

When setting up a button with the C# script operation, it is always important to do everything correctly. Incorrectly written logic, system names for templates, attributes, etc. may result in the script failure. What should you pay attention to when finding the causes for the script operation error in case it occurs?

**Solution:**

1. Check the correctness of the script.
2. Check roles permissions. It is important that the role has permissions to the button itself and to all the templates specified in the script.

================================================
FILE: 395. Version 4/401. Troubleshooting/1967-optimize_calculate_attribute.md
================================================
---
title: Optimizing Calculated Attributes
kbId: 1967
---

# Optimizing Calculated Attributes

One possible reason for the performance degradation of CMW Platform is the use of calculated attributes. According to the existing logic, the value in the calculated attribute is not stored, but is calculated every time it is referred to. Depending on the complexity and correctness of the written expression, for example, a cyclic formula, recalculation can take a significant amount of time, and a calculated attribute can significantly affect the performance of some sections of the system:

- Table of records — when a calculated attribute is displayed on a table of records, at the moment the table is opened, all values ​​are recalculated according to the specified calculated expression;
- Record form — when a calculated attribute is displayed on a record form, the value is recalculated not only at the moment the form is opened, but also at any click on the attribute, changing the value of any other attribute, adding a record to the collection, etc .;
- API, C# scripts — when accessing data through the API, for example, obtaining information on a specific record or an array of records, the value for a calculated attribute will be recalculated before sending the request, which may increase the time it takes to receive a response to a request.

**Solution**

1. Whenever possible, we recommend not to transfer calculated attributes to tables frequently used by employees to obtain operational information. Drag them out only for reports with warning users about a possible increase in data loading time.
2. When writing a calculated expression in Comindware Expression Language, we recommend rewriting it in N3 (you can find examples of expressions in N3 in the [N3 language](https://kb.cmwlab.com/category/411/) category).
3. Use alternative options for obtaining a similar result instead of using calculated fields (items 4 and 5).
4. When using a calculated attribute in a process, it is possible to replace it with setting an entry or exit scenarios for a process element.
5. When using a calculated attribute on a record form, it is possible to replace it with setting a value in the rules for a specific form.

================================================
FILE: 395. Version 4/401. Troubleshooting/1969-process_id_not_found.md
================================================
---
title: Error “Identifier “…” not found on the process diagram
kbId: 1969
---

# Error “Identifier “…” not found on the process diagram

It is important to understand the context when writing formulas as part of customizing a process diagram. The initial context within a process template is the context of the associated record template.

If, when checking or publishing a process diagram, you encounter the error ***"Identifier "..." not found, location [...]"***, this means that in some expression on this element you used an attribute that does not exist in the current context, that is, in the associated record template. In this case, the system name of such an attribute is indicated in quotes, and its positioning in the written calculated expression is indicated in square brackets.

**Solution**

1. The easiest way is to create the required attribute in the associated record template.
2. If you need to use this particular attribute located in another record template, refer to it through the expression language.

================================================
FILE: 395. Version 4/401. Troubleshooting/1975-process_notify_no_info.md
================================================
---
title: Information in the process notification was not sent
kbId: 1975
---

# Information in the process notification was not sent

As part of the process, it is possible to configure the sending of an external notification (for example, to notify the client about the approval of the contract), with which you can transfer various kinds of data: text, attachments, or any other data connected with the process.

If, after the process has started, it turned out that some of the information was not sent, in this case it is worth paying attention to the following possible places where it could have been lost:

1. **The mapping of the message attributes and the process data was configured incorrectly.**

   On the business process diagram, go to the settings of the «***Send message event***» element and in the «***Message Data***» tab check the correctness of the data mapping.

   After making your changes, publish the process diagram.
2. **The mapping of the message attributes in the communication routes was configured incorrectly.**

   Go to the «**Communication routes**» section, select the outgoing route used in the process and check the correct use of the attributes in the «***Message properties***» tab.

================================================
FILE: 395. Version 4/401. Troubleshooting/1977-attribute_history_view.md
================================================
---
title: Calculated attribute change log cannot be viewed
kbId: 1977
---

# Calculated attribute change log cannot be viewed

In the settings of the attribute there is a «***Track changes***» flag, after applying which any changes in the attribute will be recorded. This flag can be set only for non-calculated attributes. History cannot be saved for calculated attributes, since calculated attributes are subject of computation and their value is always unstable.

All changes to the attribute values ​​are saved in the system change log. To view the change log, open a record, click on the «Information» button on the ribbon of the form and select «***Change log***».

**Solution**

If you still need to store change log of calculated attributes, then:

1. Create a non-calculated attribute (for each calculated one).
2. Manually (or by scenario) write the calculated value in the new attribute.

================================================
FILE: 395. Version 4/401. Troubleshooting/1979-change_attribute_data_type.md
================================================
---
title: How to change the data type of an existing attribute?
kbId: 1979
---

# How to change the data type of an existing attribute?

**CMW Platform** has a useful feature for changing the data type of an attribute. Situations may occur when an attribute was quickly created and its data type was defined incorrectly, or during further design there appeared a need to change it.

There are a few things to keep in mind when changing the data type:

- Whether this attribute is used in any calculated expressions in the system;
- How many forms and tables the attribute is dragged on.

**Solution**

1. If the attribute is used in calculated expressions, then they may stop working, since some functions require only the numeric type of the attribute, or only the text type, etc. In this case, it is better to create a new attribute with the desired type.
2. If an attribute is dragged on several forms and tables, then it is also better to create a new attribute with the required type, or, after changing the type of the attribute, drag it to all the forms and tables again.

If the attribute is dragged on a large number of forms and tables and is used in a number of calculated expressions, it is better to create a new attribute with the desired type.

**Note :** when you change the display format of an attribute, you do not need to drag it on the form or on a table again, these changes are applied automatically.

================================================
FILE: 395. Version 4/401. Troubleshooting/1981-archived_records_in_expression.md
================================================
---
title: Calculated expression returns archived records
kbId: 1981
---

# Calculated expression returns archived records

When a new record template is created in **CMW Platform**, a button with the «Archive» operation is automatically generated (it archives the selected records (i.e. it sets the value of the «*\_isDisabled*» system attribute to «*true*»)) and is available for users to use.

When working with the data late on, for example, while using Comindware Expression Language, you may find out that the result of the calculated expression is incorrect. One of the reasons may be the inclusion of archived records in the result of the calculation.

**Solution**

To exclude archived records from the calculation result, add the «***EQUALS (a->\_isDisabled, false)***» condition to the calculated expression. For example, when counting the number of records and excluding archived ones.

**Note :** archived records are not displayed in the tables by default. To enable their display, select the «***Show archived records***» flag in the table properties.

================================================
FILE: 395. Version 4/401. Troubleshooting/1995-hard_read_text_table.md
================================================
---
title: Unreadable text fields in a table on the form
kbId: 1995
---

# Unreadable text fields in a table on the form

By default, a limited amount of text is displayed in the table cells. To view all the text in a cell, the user can hover the mouse pointer over it — the text will be displayed in a tooltip. However, if the text is very large, it can be inconvenient to read it this way. In this case, the user should be able to view the entire record in a separate form.

**Solution**

1. In the form settings, add the «***Navigate***» button to the table toolbar.
2. Click on the added button, and in the right menu select the form which will open up for each record from the table.
3. Save the form.
4. Open any record, right-click on the cell with the text and select «***Navigate***».

================================================
FILE: 395. Version 4/401. Troubleshooting/2016-table_open_error.md
================================================
---
title: Table stopped working (error «Object reference not set to an instance of an object»)
kbId: 2016
---

# Table stopped working (error «Object reference not set to an instance of an object»)

If a table that used to work stopped working for a user or several users: the table does not open and the error message «Object reference not set to an instance of an object» is displayed, then most likely there is a conflict between the personal configuration of the table and the system configuration of the table. Perhaps some changes were made to the system settings of the table, for example, an attribute was removed that was filtered in the personal configuration of the table.

**Solution**

This problem can only be fixed by deleting the personal configuration of the table where the error occurred. The appearance of the table for the end user will thus be returned to the default settings.

1. Go to the API area by typing «***/docs***» after the domain name of the site.
2. Select «***System Core Api***» from the list.
3. Select «***Ontology***» and then «***GetReferences***». Enter the table ID in the query field and click «***Try it out!***». Thus, you’ll get a list of all personal configurations of the specified table.
4. Then you need to find the personal configuration of the table created by the user who encountered the error. Select «***Ontology***» and then «***GetAxioms***». In the query field, enter the table's personal configuration ID and click «***Try it out!***». Thus, you’ll get information on the specified personal configuration of the table.
5. Once you have determined the personal configuration of the table you want to remove, select «***Ontology***» and then «***Remove***». In the query field, enter the table's personal configuration ID and click «***Try it out!***».

================================================
FILE: 395. Version 4/401. Troubleshooting/2102-form_reference_field_error.md
================================================
---
title: Unable to place some elements on a form through a reference field
kbId: 2102
---

# Unable to place some elements on a form through a reference field

In {{ productName }} there is an attribute data type called record. In the attribute settings, you can specify how many records can be stored in it: one or more, i.e., how many records in the target record template are referenced by the record in the current record template. This setting also affects the ability to add elements from an attribute with the “Record” data type to a form or a table.

If only one associated value can be stored in an attribute, any of the available elements of the target record template can be transferred to the form of the main object by expanding the attribute with the “Record” data type in the form designer. In this case, one record in the main record template corresponds to one record in the target record template.

But, if several values ​​can be stored in an attribute with the “Record” data type, then not all elements from this attribute can be transferred to the form of the main object. So, for example, you can't move a form, because the attribute stores multiple records, and the form always corresponds to just one record. The attributes of the target record template also cannot be placed on the form of the main object in an arbitrary order, but only by changing the representation of the attribute with the "Record" data type on the form to "Table" and transferring the attributes as columns of the table.

================================================
FILE: 395. Version 4/407. Integrations/1941-core_api_methods.md
================================================
---
title: Web API Methods
kbId: 1941
---

# Web API Methods

## Introduction

The **CMW Platform** RESTful Web API provides generic REST API methods. These methods are the same for all **CMW Platform**versions.

This article contains the Web API methods overview. See complete API details in the Swagger UI.

## Accessing Web API

- Base URL for the Web API requests:
  `https://your-host/webapi/`
- Web API supports `GET`, `PUT`, `POST`  , and   `DELETE` queries.
- Web API supports JSON or XML content types.
- Web API supports basic authentication.

## Using Swagger

The Swagger UI provides detailed API method references, including request and response descriptions and data models with example values.

With the Swagger UI, you can execute the requests and view the responses.

Access the Swagger UI for Web API at:

`https://your-host/Docs/WebApi/`

Here `your-host` is the domain name of the **CMW Platform** instance.

_![Swagger UI for the method that creates an account template](https://kb.cmwlab.com/assets/img_661e5d5fbf8ed.png)_

### Definitions

The Web API methods and Swagger documentation use the following names for the CMW Platform entities:

- *activity*— process diagram element
- *alias*— system name
- *behaviour*— scenario, process diagram element
- *container*— template, application
- *dataset*— table in a template
- *global alias*— object path, consisting of its type, parent system name, and object system name
- *id*— object identifier
- *list*— array
- *property*— attribute
- *solution*— application
- *scheme*— process diagram
- *stream*— file stored in the system
- *transfer*— application version management
- *trigger*— scenario
- *user command*— button
- *worker*— system service
- ***object*** — a collection of property/value pairs
## Web API Method Descriptions

| Account — individual accounts | | | | |
| --- | --- | --- | --- | --- |
| Method | Query | Description | Input | Output |
| GET | /webapi/Account | Gets all accounts. |  | Array of objects with account properties |
| POST | /webapi/Account | Creates account. | Account properties object | Account ID |
| PUT | /webapi/Account | Edits account properties. | Account properties object | Status object |
| DELETE | /webapi/Account/{accountId} | Deletes account. | Account ID | Status object |
| GET | /webapi/Account/{accountId} | Gets account properties. | Account ID | Account properties object |
| AccountTemplate — account templates and accounts linked to them | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/AccountTemplate/{solutionAlias} | Creates account template. | Application system name, account template properties object | Object with account template system name |
| PUT | /webapi/AccountTemplate/{solutionAlias} | Edits account template properties. | Application system name, account template properties object | Status object |
| DELETE | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias} | Deletes account template. | Application system name, account template system name | Status object |
| GET | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias} | Gets account template properties. | Application system name, account template system name | Account template properties object |
| PUT | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/Disable | Archives account template. | Application system name, account template system name. | Status object |
| PUT | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/Enable | Unarchives account template. | Application system name, account template system name | Status object |
| PUT | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/Exclude | Unlinks accounts from the specified account template. | Application system name, account template system name, array of account IDs | Status object |
| PUT | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/Include | Links specified accounts to the specified account template. | Application system name, account template system name, array of account IDs | Status object |
| GET | /webapi/AccountTemplate/{solutionAlias}/{accountTemplateAlias}/ListIncluded | Gets accounts linked to the specified account template. | Application system name, account template system name | Array of objects with account properties |
| GET | /webapi/AccountTemplate/List/{solutionAlias} | Gets all account templates in the specified application. | Application system name | Array of objects with account template properties |
| Attribute — template attributes | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Attribute/{solutionAlias} | Creates attribute. | Application system name, attribute properties object | Object with attribute system name |
| PUT | /webapi/Attribute/{solutionAlias} | Edits attribute properties. | Application system name, attribute properties object | Status object |
| DELETE | /webapi/Attribute/{solutionAlias}/{attributeGlobalAlias} | Deletes attribute. | Application system name, attribute global alias: `Attribute@templateSystemName.attributeSystemName` | Status object |
| GET | /webapi/Attribute/{solutionAlias}/{attributeGlobalAlias} | Gets attribute properties. | Application system name, attribute global alias: `Attribute@templateSystemName.attributeSystemName` | Attribute properties object |
| PUT | /webapi/Attribute/{solutionAlias}/{attributeGlobalAlias}/Disable | Archives attribute. | Application system name, attribute global alias: `Attribute@templateSystemName.attributeSystemName` | Status object |
| PUT | /webapi/Attribute/{solutionAlias}/{attributeGlobalAlias}/Enable | Unarchives attribute. | Application system name, attribute global alias: `Attribute@templateSystemName.attributeSystemName` | Status object |
| GET | /webapi/Attribute/List/{templateGlobalAlias} | Gets all attributes for the specified template. | Template global alias: `Template@applicationSystemName.templateSystemName` | Array of objects with attribute properties |
| Backup — backup configurations and sessions | | | | |
| Method | Query | Description | Input | Output |
| DELETE | /webapi/Backup/Configuration | Deletes specified backup configurations. | Array of backup configuration IDs | Status object |
| GET | /webapi/Backup/Configuration | Gets all backup configurations. |  | Array of backup configuration objects |
| POST | /webapi/Backup/Configuration | Creates backup configuration. | Backup configuration object | Backup configuration ID |
| PUT | /webapi/Backup/Configuration | Edits backup configuration. | Backup configuration object | Status object |
| GET | /webapi/Backup/Configuration/{configurationId} | Gets backup configuration. | Backup configuration ID | Backup configuration object |
| DELETE | /webapi/Backup/Session | Deletes specified backup sessions. | Array of backup session IDs | Status object |
| POST | /webapi/Backup/Session | Returns backup sessions matching the specified filter. | Backup session filter object | Array of objects with backup session details |
| POST | /webapi/Backup/Session/{configurationId} | Initiates backup session using the specified configuration. | Backup configuration ID | Object with backup session details |
| GET | /webapi/Backup/Session/{sessionId} | Gets backup session. | Backup session ID | Object with backup session details |
| PUT | /webapi/Backup/Session/{sessionId} | Aborts backup session. | Backup session ID | Object with backup session details |
| POST | /webapi/Backup/SetElasticsearchRepository/{name} | Sets Elasticsearch snapshots repository. | Name of existing Elasticsearch snapshots repository | Status object |
| BehaviourState — scenarios and process elements | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/BehaviourState/{solutionAlias} | Gets scenario and process element states in the specified application. | Application system name | Object with scenario and process element states |
| PUT | /webapi/BehaviourState/{solutionAlias} | Updates scenario and process element states in the specified application. | Object with scenario and process element states | Status object |
| CaseTemplate — case templates (legacy) | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/CaseTemplate/{solutionAlias} | Creates case template with/without related record template. | Application system name, case template properties object | Object with case template system name |
| PUT | /webapi/CaseTemplate/{solutionAlias} | Edits case template. | Application system name, case template properties object | Status object |
| DELETE | /webapi/CaseTemplate/{solutionAlias}/{caseTemplateAlias} | Deletes case template. | Application system name, case template system name | Status object |
| GET | /webapi/CaseTemplate/{solutionAlias}/{caseTemplateAlias} | Gets case template properties. | Application system name, case template system name | Case template properties object |
| PUT | /webapi/CaseTemplate/{solutionAlias}/{caseTemplateAlias}/Disable | Archives case template. | Application system name, case template system name | Status object |
| PUT | /webapi/CaseTemplate/{solutionAlias}/{caseTemplateAlias}/Enable | Unarchives case template. | Application system name, case template system name | Status object |
| GET | /webapi/CaseTemplate/List/{solutionAlias} | Gets all case templates in the specified application. | Application system name | Array of objects with case template properties |
| Dataset — tables | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Dataset/{solutionAlias} | Creates table. | Application system name, table configuration object | Table configuration object |
| PUT | /webapi/Dataset/{solutionAlias} | Edits table configuration. | Application system name, table configuration object | Status object |
| DELETE | /webapi/Dataset/{solutionAlias}/{datasetGlobalAlias} | Deletes table. | Application system name, table global alias: `Dataset@templateSystemName.tablesystemName` | Status object |
| GET | /webapi/Dataset/{solutionAlias}/{datasetGlobalAlias} | Gets table configuration. | Application system name, table global alias: `Dataset@templateSystemName.tablesystemName` | Table configuration object |
| GET | /webapi/Dataset/List/{templateGlobalAlias} | Gets all tables of the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Array of table configuration objects |
| Document — files attached to Document attributes | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Document | Creates document. | Document properties object | Object with document ID |
| PUT | /webapi/Document | Edits document properties. | Document properties object | Status object |
| DELETE | /webapi/Document/{documentId} | Deletes document. | Document ID | Status object |
| GET | /webapi/Document/{documentId} | Gets document properties. | Document ID | Document properties object |
| GET | /webapi/Document/{documentId}/Content | Gets document content. | Document ID | Document content (`application/octet-stream`) |
| POST | /webapi/Document/Content | Creates document by uploading a file. | Object with filename and content (`byte array`) | Object with document ID |
| POST | /webapi/Document/Revision/{documentId}/Content | Creates revision by uploading a file. | Document ID, object with filename and content (`byte array`) | Object with revision ID |
| GET | /webapi/Document/Revision/{revisionId} | Gets revision properties. | Revision ID | Revision properties object |
| GET | /webapi/Document/Revision/{revisionId}/Content | Gets revision content. | Revision ID | Revision content (`application/octet-stream`). |
| DocumentExportTemplate — export templates | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/DocumentExportTemplate/{solutionAlias} | Creates export template. | Application system name, object with export template properties | Export template system name |
| PUT | /webapi/DocumentExportTemplate/{solutionAlias} | Edits export template. | Application system name, object with export template properties | Status object |
| DELETE | /webapi/DocumentExportTemplate/{solutionAlias}/{exportTemplateGlobalAlias} | Deletes export template. | Application system name, export template global alias: `ExportTemplate@templateSystemName.exportTemplateSystemName` | Status object |
| GET | /webapi/DocumentExportTemplate/{solutionAlias}/{exportTemplateGlobalAlias} | Gets export template properties. | Application system name, export template global alias: `ExportTemplate@ templateSystemName.exportTemplateSystemName` | Object with export template properties |
| GET | /webapi/DocumentExportTemplate/List/{templateGlobalAlias} | Gets all export templates for the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Array of objects with export template properties |
| Form — forms and form rules (except process start forms and user task forms) | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Form/{solutionAlias} | Creates form. | Application system name, form configuration object | Form system name |
| PUT | /webapi/Form/{solutionAlias} | Edits form. | Application system name, form configuration object | Status object |
| DELETE | /webapi/Form/{solutionAlias}/{formGlobalAlias} | Deletes form. | Application system name, form global alias: `Form@templateSystemName.formSystemName` | Status object |
| GET | /webapi/Form/{solutionAlias}/{formGlobalAlias} | Gets form configuration. | Application system name, form global alias: `Form@templateSystemName.formSystemName` | Form configuration object |
| GET | /webapi/Form/FormRules/{solutionAlias}/{formGlobalAlias} | Gets form rules. | Application system name, form global alias: `Form@templateSystemName.formSystemName` | Form rules object |
| PUT | /webapi/Form/FormRules/{solutionAlias}/{formGlobalAlias} | Sets form rules. | Application system name, form global alias (`Form@templateSystemName.formSystemName`), form rules object. | Status object |
| GET | /webapi/Form/List/{templateGlobalAlias} | Gets all forms of the specified template. | Application system name, template global alias: `Template@solutionSystemName.templateSystemName` | Array of form configuration objects |
| SolutionGitIntegration — application version control via Git | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Git/AddRemoteBranch | Creates branch in the remote repository. | Repository and branch configuration object | Status object |
| POST | /webapi/Git/Connect | Initializes connection with the specified repository. | Repository configuration object | Status object |
| POST | /webapi/Git/GetRepositoryDetails | Gets repository commits. | Repository configuration object | Array of objects with commit properties |
| GET | /webapi/Git/GetUserConfiguration | Gets repository user credentials. |  | Object with repository user credentials |
| GET | /webapi/Git/GetUserSolutionConfig | Gets repository configuration and user details. |  | Object with repository configuration and user credentials |
| POST | /webapi/Git/ListBranches | Gets all repository branches. | Repository configuration object | Array of objects with branch properties |
| GET | /webapi/Git/ListRepositories | Gets all repositories of Git connections. |  | Array of repository configuration objects |
| POST | /webapi/Git/SaveUserCredentials | Saves user credentials. | Repository configuration and user credentials object | Status object |
| Heartbeat — server, process, scripts, and service status monitoring | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/Heartbeat/Details | Gets service usage statistics. |  | Heartbeat details object |
| GET | /webapi/Heartbeat/IsAlive | Gets service availability status. |  | Status object |
| GET | /webapi/Heartbeat/ServerDetails | Gets server details. |  | Server information object |
| ProcessObjects — process diagram version migration | | | | |
| Method | **Query** | Description | Input | Output |
| POST | /webapi/ProcessObjects/Migrate | Changes process instances diagram version and moves tokens. | Process template global alias (`ProcessTemplate@applicationSystemName.templateSystemName`), target diagram ID, process instance IDs | Status object |
| ProcessTemplate — process templates | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/ProcessTemplate/{solutionAlias} | Creates process template. | Application system name, process template properties object | Process template system name |
| PUT | /webapi/ProcessTemplate/{solutionAlias} | Edits process template properties. | Application system name, process template properties object | Status object |
| DELETE | /webapi/ProcessTemplate/{solutionAlias}/{processTemplateAlias} | Deletes process template. | Application system name, process template system name | Status object |
| GET | /webapi/ProcessTemplate/{solutionAlias}/{processTemplateAlias} | Gets process template properties. | Application system name, process template system name | Process template properties object |
| PUT | /webapi/ProcessTemplate/{solutionAlias}/{processTemplateAlias}/Disable | Archives process template. | Application system name, process template system name | Status object |
| PUT | /webapi/ProcessTemplate/{solutionAlias}/{processTemplateAlias}/Enable | Unarchives process template. | Application system name, process template system name | Status object |
| GET | /webapi/ProcessTemplate/List/{solutionAlias} | Gets all process templates in the specified application. | Application system name | Array of objects with process template properties |
| Record — single record (except process templates) | | | | |
| Method | Query | Description | Input | Output |
| DELETE | /webapi/Record/{recordId} | Deletes record. | Record ID | Status object |
| GET | /webapi/Record/{recordId} | Gets record. | Record ID | Object with attribute values:  `{"attributeSystemName": "value"}` |
| PUT | /webapi/Record/{recordId} | Edits record. | Record ID, object with record attribute values:`[{"attributeSystemName": "value"}]` | Status object |
| POST | /webapi/Record/{recordId}/{deepClone} | Clones record. | Record ID, deep cloning flag (`true` — clone linked records) | Cloned record ID |
| PUT | /webapi/Record/{recordId}/Disable | Archives record. | Record ID | Status object |
| PUT | /webapi/Record/{recordId}/Enable | Unarchives record. | Record ID | Status object |
| POST | /webapi/Record/{templateGlobalAlias} | Creates record. | Application system name, template global alias (`Template@applicationSystemName.templateSystemName`), object with record attribute values: `[{"attributeSystemName": "value"}]` | Record ID |
| Records — multiple records and record export/import (except process templates) | | | | |
| Method | Query | Description | Input | Output |
| DELETE | /webapi/Records | Deletes specified records. | Array of record IDs | Status object |
| PUT | /webapi/Records | Edits specified records. | Array of record IDs and objects with record attribute values: `[{"attributeSystemName": "value"}]` | Status object |
| DELETE | /webapi/Records/{templateGlobalAlias} | Deletes all records from the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Status object |
| GET | /webapi/Records/{templateGlobalAlias} | Gets all records of the specified template. | Application system name, template global alias :`Template@applicationSystemName.templateSystemName` | Array of objects with record attribute values: `[{"attributeSystemName": "value"}]` |
| POST | /webapi/Records/{templateGlobalAlias} | Creates records. | Template global alias (`Template@applicationSystemName.templateSystemName`), array of objects with record attribute values: `[{"attributeSystemName": "value"}]` | Array of record IDs |
| GET | /webapi/Records/{templateGlobalAlias}/Export | Exports all records of the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Serialized records data |
| PUT | /webapi/Records/BulkEdit | Updates specified records with the same data. | Record properties and values to update | Status object |
| PUT | /webapi/Records/Disable | Archives specified records. | Array of record IDs | Status object |
| PUT | /webapi/Records/Enable | Unarchives specified records. | Array of record IDs | Status object |
| POST | /webapi/Records/Export | Exports specified records. | Record template global alias object, array of record IDs | Serialized records data |
| POST | /webapi/Records/Import | Imports records from a file. | ID of an uploaded file with serialized records data | The number of imported records |
| RecordTemplate — record templates | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/RecordTemplate/{solutionAlias} | Creates record template. | Application system name, record template properties object | Record template system name |
| PUT | /webapi/RecordTemplate/{solutionAlias} | Edits record template. | Application system name, record template properties object | Status object |
| DELETE | /webapi/RecordTemplate/{solutionAlias}/{recordTemplateAlias} | Deletes record template. | Application system name, record template system name | Status object |
| GET | /webapi/RecordTemplate/{solutionAlias}/{recordTemplateAlias} | Gets template by system name. | Application system name, record template system name | Record template properties object |
| PUT | /webapi/RecordTemplate/{solutionAlias}/{recordTemplateAlias}/Disable | Archives record template. | Application system name, record template system name | Status object |
| PUT | /webapi/RecordTemplate/{solutionAlias}/{recordTemplateAlias}/Enable | Unarchives record template. | Application system name, record template system name | Status object |
| GET | /webapi/RecordTemplate/List/{solutionAlias} | Gets all record templates in the specified application. | Application system name | Array of objects with record template properties |
| ReferenceData — records with specified attribute values | | | | |
| Method | Query | Description | Input | Output |
| DELETE | /webapi/ReferenceData/Delete | Deletes a record with specified key attribute values. | Template global alias object, object with key attribute system names and values | Deleted record ID. If several records are matched, returns null and no records are deleted |
| POST | /webapi/ReferenceData/Get | Gets attribute values of a record with specified key attribute values. | Template global alias object, object with key attribute system names and values, array of attribute system names to get | Object with record attribute values. If several records are matched, returns null and no records are returned |
| PUT | /webapi/ReferenceData/Put | Edits record with specified key attribute values. | Template global alias object, array of key attribute system names, object with key attribute system names and values, object with attribute system names and their new values | Edited record ID. If several records are matched, returns null and no records are edited |
| Solution — applications | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/Solution | Gets all applications. |  | Array of objects with application properties |
| POST | /webapi/Solution | Creates application. | An object with application properties | Application system name |
| PUT | /webapi/Solution | Edits application properties. | An object with application properties | Status object |
| DELETE | /webapi/Solution/{solutionAlias} | Deletes application. | Application system name | Status object |
| GET | /webapi/Solution/{solutionAlias} | Gets application properties. | Application system name | Object with application properties |
| Toolbar — toolbars and buttons on them | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/Toolbar/{solutionAlias} | Creates toolbar. | Application system name, toolbar configuration object | Toolbar system name |
| PUT | /webapi/Toolbar/{solutionAlias} | Edits toolbar. | Application system name, toolbar configuration object | Status object |
| DELETE | /webapi/Toolbar/{solutionAlias}/{toolbarGlobalAlias} | Deletes toolbar. | Application system name, toolbar global alias: `Toolbar@templateSystemName.toolbarAlias` | Status object |
| GET | /webapi/Toolbar/{solutionAlias}/{toolbarGlobalAlias} | Gets toolbar by system name. | Application system name, toolbar global alias: `Toolbar@templateSystemName.toolbarAlias` | Toolbar configuration object |
| GET | /webapi/Toolbar/List/{templateGlobalAlias} | Gets all toolbars for the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Array of toolbar configuration objects |
| Transfer — application model export/import | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/Transfer/{fileId}/Validate | Validates application model. | Application model file ID | Validation summary object |
| GET | /webapi/Transfer/{solutionAlias} | Exports application model. | Application system name | An object with application model ZIP file in Base64 format and export summary |
| POST | /webapi/Transfer/{solutionAlias}/{fileId}/{publishAfterImport}/{policy} | Imports application model. | Application system name, application model ZIP/CTF file ID, imported process diagrams publishing flag (`true` — publish), behaviour state policy (`ApplyNew`, `ApplyOld`, `DisableAll`, or `EnableAll`). | Application import summary object |
| POST | /webapi/Transfer/Upload | Uploads application model file. | Application model ZIP file in Base64 format | An object with the uploaded file ID |
| UserCommand — buttons | | | | |
| Method | Query | Description | Input | Output |
| POST | /webapi/UserCommand/{solutionAlias} | Creates button. | Application system name, button configuration object | Button system name |
| PUT | /webapi/UserCommand/{solutionAlias} | Edits button. | Application system name, button configuration object | Status object |
| DELETE | /webapi/UserCommand/{solutionAlias}/{userCommandGlobalAlias} | Deletes button. | Application system name, button global alias: `UserCommand@templateSystemName.userCommandAlias` | Status object |
| GET | /webapi/UserCommand/{solutionAlias}/{userCommandGlobalAlias} | Gets button configuration. | Application system name, button global alias: `UserCommand@templateSystemName.userCommandAlias` | Button configuration object |
| PUT | /webapi/UserCommand/{solutionAlias}/{userCommandGlobalAlias}/Disable | Archives button. | Application system name, button global alias: `UserCommand@templateSystemName.userCommandAlias` | Status object |
| PUT | /webapi/UserCommand/{solutionAlias}/{userCommandGlobalAlias}/Enable | Unarchives button. | Application system name, button global alias: `UserCommand@templateSystemName.userCommandAlias` | Status object |
| GET | /webapi/UserCommand/List/{templateGlobalAlias} | Gets all buttons of the specified template. | Application system name, template global alias: `Template@applicationSystemName.templateSystemName` | Array of button configuration objects |
| WorkerEngine — system services | | | | |
| Method | Query | Description | Input | Output |
| GET | /webapi/WorkerEngine/GetConfiguration | Gets system service statuses (`true` — enabled). |  | Object with system service statuses |
| PUT | /webapi/WorkerEngine/SetConfiguration | Sets system service statuses. | Object with system service statuses (`true` — enabled) | Status object |

================================================
FILE: 395. Version 4/407. Integrations/1955-import_excel_data.md
================================================
---
title: Import Data into Excel via API
kbId: 1955
---

# Import Data into Excel via API

## Use Case

Using the **CMW Platform** API, you can import the application data to Excel (via Power Query) or BI systems.

In this article, we will import the data from a record template into an Excel file using the **CMW Platform** API and the Power Query add-in.

## Instructions

### Obtaining the GET Request URL for a Template

1. Open your **{{ productName }}** instance website.
2. To open the API web interface, type `/docs` after the domain name in the browser address bar, for instance:
   `mycompany.com/docs`
3. Go to the **Solution API**section that lists all application templates.
4. Find the template you need by its system name and click it.
5. Select the **GET** method (without the `{id}` suffix) that returns all the records from the record template.
6. Click **Try it out**.
7. Copy the value in the **Request URL** field, for example:
   `https://mycompany.com/api/public/solution/Vehiclerequests`

_![Obtaining the template GET request URL](https://kb.cmwlab.com/assets/img_6442b00578cfd.png)_

**Note:** The **CMW Platform** API presents the data in JSON format.
### Importing Data to Excel

The Power Query add-in is built into Excel 2016 and above. For earlier versions of Excel, you need to [install it](https://support.microsoft.com/en-us/office/about-power-query-in-excel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a?redirectsourcepath=%252fru-ru%252foffice%252fpower-query-%2525e2%252580%252594-%2525d0%2525be%2525d0%2525b1%2525d0%2525b7%2525d0%2525be%2525d1%252580-%2525d0%2525b8-%2525d0%2525be%2525d0%2525b1%2525d1%252583%2525d1%252587%2525d0%2525b5%2525d0%2525bd%2525d0%2525b8%2525d0%2525b5-ed614c81-4b00-4291-bd3a-55d80767f81d).

1. On the **Data** tab in the ribbon, click **From Web**
2. In the **URL** field, paste the [**Request URL** you copied from the **CMW Platform** API](#RequestURL).

   ![Initializing the Power Query in Excel](https://kb.cmwlab.com/assets/img_6442afcc8b705.png)

   Initializing the Power Query in Excel
3. In the **Access Web content** window:
   - Select **Basic**.
   - Enter the **user name** and **password** of the account with permission to view the selected record template.
   - Click **Connect**.

     _![     Configuring the credentials for API access](https://kb.cmwlab.com/assets/img_6446481f27823.png)_
4. The received data appears in the **Power Query Editor** window.

   ![Power Query Editor with the imported data](https://kb.cmwlab.com/assets/img_644649e72f2d0.png)

   Power Query Editor with the imported data
5. Click **To Table** in the ribbon. Click **OK**in the **To Table** window .

   ![Configuring the query table](https://kb.cmwlab.com/assets/img_64464c555a6b4.png)

   Configuring the query table
6. Expand the list of all record template attributes and select the attributes to load in the table.

   _![   Configuring the columns](https://kb.cmwlab.com/assets/img_64464c3c94675.png)_
7. Click **Close & Load** in the ribbon to import the data into the Excel spreadsheet.

   ![Loading the query table to the Excel spreadsheet](https://kb.cmwlab.com/assets/img_64464d4357314.png)

   *Loading the query table to the Excel spreadsheet*
8. The data will appear in the Excel spreadsheet as shown below.

   ![A query table imported to the Excel spreadsheet](https://kb.cmwlab.com/assets/img_64464d8ecaf5a.png)

   A query table imported to the Excel spreadsheet

================================================
FILE: 395. Version 4/407. Integrations/2074-solution_api_methods.md
================================================
---
title: Solution API Methods
kbId: 2074
---

# Solution API Methods

## Introduction

Solution API provides RESTful methods that are automatically generated for all record, account, organizational unit, and role templates (but not for process templates) in the current **CMW Platform** instance.

There are five methods for each template:

- Delete a record
- Get data of a record
- Edit data of a record
- Get data of all records
- Create a record

This article provides an overview of the Solution API methods. See complete API details in the Swagger UI.

## Access to Solution API

- Base URL for the Solution API requests:
  `https://your-host/api/public/solution/`
- Solution API supports `GET`, `PUT`, `POST`, and   `DELETE` queries.
- Solution API methods support JSON content type.
- Solution API supports basic authentication.

## Using Swagger

The Swagger UI provides detailed API method references, including request and response descriptions and data models with example values.

With the Swagger UI, you can execute the requests and view the responses.

Access the Swagger UI for Solution API at:

`http://your-host/Docs/SolutionApi`

Here `your-host` is the domain name of the **CMW Platform** instance.

_![Swagger UI for the method that creates a template record](https://kb.cmwlab.com/assets/img_64d4a6580acd8.png)_

## Solution API Method Descriptions

| TemplateSystemName — records in a template by its system name | | | | |
| --- | --- | --- | --- | --- |
| Method | Query | Description | Input | Output |
| DELETE | /TemplateSystemName/{id} | Deletes a record from the TemplateSystemName template | Record ID | Status object |
| GET | /TemplateSystemName/{id} | Gets data of a record in the TemplateSystemName template | Record ID | Object with record attribute values:`{"attributeSystemName": "value"}` |
| PUT | /TemplateSystemName/{id} | Edits data of a record in the TemplateSystemName template | Record ID, object with record attribute values: `{"attributeSystemName": "value"}` | Status object |
| GET | /TemplateSystemName | Gets data of all records in the TemplateSystemName template |  | Array of objects with record attribute values:`[{"attributeSystemName": "value"}]` |
| POST | /TemplateSystemName | Creates a record in the TemplateSystemName template | Object with record attribute values: `{"attributeSystemName": "value"}` | Record ID |

================================================
FILE: 395. Version 4/407. Integrations/2161-get_started_with_cmw_api.md
================================================
---
title: Get Started With CMW API
kbId: 2161
---

# Get Started With CMW API

## Introduction

The **CMW Platform** can communicate with external system APIs via **connections**and   **communication routes** and can also process requests from external systems via the three **REST APIs**:

- [**Solution API**](https://kb.comindware.ru/article.php?id=2074)
- **System Core API**
- [**Web API**](https://kb.comindware.ru/article.php?id=1941)

### Definitions

- **API** (Application Programming Interface) is a set of methods, classes, libraries, and functions that enable communication between different systems.
- **REST API** is an API that conforms to the Representational State Transfer architecture. The REST API allows you to efficiently utilize HTTP, scale services, and develop applications using almost any programming language in compliance with the REST design principles:
  - Stateless — the server does not store the request state. Each incoming request contains all the data necessary to process it and is processed independently of other requests.
  - Uniform interface — the server transmits data in a well-defined format.
  - Client and server independence — the client can interact with the server only through the resource URI. The server can only transfer the requested data to the client via HTTP.
  - Resource cacheability — responses indicate their cacheability. Resources can be cached at the server or client.
  - Layered architecture — the client can connect to authorized intermediaries between the client and the server to receive responses from the server, and the server can forward requests to other servers.
  - Code on demand (optional) — the server can extend the client capabilities by transferring executable logic, for example, to validate user-entered data.
- **RESTful** is a web service that implements the **REST** architecture.
- **Resource** is an object or information in an application, such as a template, account, or document, that an API provides access to.
- **Resource URI** is a Uniform Resource Identifier in an API.
- **Client** is a person or system that accesses resources via an API.
## Access the API

In its simplest case, **RESTful** services send and receive HTTP requests in a URL string to retrieve or send data, execute a command, or perform another action.

To configure integrations using **REST API**, you can follow this general principle:

- Develop an integration scenario — which system initiates the API call, how often, what methods it uses to transfer what data, what happens next, etc.
- Use the API documentation to test requests, configure connections, and generate final production requests.

### API Methods

The **CMW Platform** supports the following API methods:

- `GET` — get a list of all records.
- `GET {id}` — get a record with identifier   `{id}`.
- `DELETE {id}` — delete a record with identifier   `{id}`.
- `POST` — create a new record.
- `PUT {id}` — change a record with identifier   `{id}`.

### Initiate a Request From an External System

The **CMW Platform** can receive HTTP API requests in two ways:

- `GET` or   `DELETE` request as a URL string containing all request parameters.
  - The external system sends the request in a URL string. You can generate a query template for an external system using [Swagger](#mcetoc_1h7csahj80).
  - You can test this request in a browser: copy the received   **Request URL** into the address bar and press `Enter`. If you are logged in to the **CMW Platform**, no authentication is needed.
- `POST` or   `PUT` request with a body containing all the parameters (e.g., username and password, data to send or receive, etc.).
  - The external system sends a request in JSON or XML format. You can generate a query template for an external system using [Swagger](#mcetoc_1h7csahj80).
  - This option is more flexible, allowing you to transfer more data in a structured form. But you can't test this type of request in a browser. You can test it using the built-in Swagger or external services like Postman, SoapUI, Insomnia, etc.
- **CMW Platform** returns a response in JSON or XML format.

### Authenticate External System to Access CMW API

The   **CMW Platform** API supports two methods to authenticate external systems:

- Basic authentication — specify the username and password of the account used to execute the request.
- HMAC — specify the token and secret key generated for the account on the **Administration** –   **Authentication Keys** page.

Notes

- To use API and [Swagger](#mcetoc_1h7csahj80), you should create a special account and grant it the **API calls** permission in a system role. Also, the API and Swagger are available to users in the   **System Administrators** system role.
- When calling API methods in the   [Swagger](#mcetoc_1h7csahj80) using the `https://your-host/docs` page, you're logged in to the **CMW Platform**, and no authentication is required.
- When calling API methods from an external system, you must add request headers to authenticate using the account with API access.
- Most external systems provide means to configure the authentication method. Otherwise, add the `Authorization` parameter to the request `Header` containing the username and password encrypted in `Base64` format.
### Initiate External API Request

The **REST API** is adopted widely, and you can often find **API** documentation for a specific system by googling: *<system name> REST API*.

The   **CMW Platform**can access external APIs using the following methods:

- A C# script (triggered by a button or a process script task) establishes a connection to an external system, generates a request, sends it, and receives a response.
- A scenario generates and sends the request through a configured external system connection. The script generates the request body, analyze the response, and place the response data into post attributes.
- A send message intermediate or end event in a process generates and sends the request.

Note

To send requests using scripts or process events, you need to configure an external service connection and communication route.

### Authenticate CMW Platform to Access External API

When accessing an external API, use the authentication method supported by the external system. Refer to the external API documentation and see if you must include the username and password in the request URL or body or generate and use a security token instead of sending the password in plain text.

## Use Swagger

The **CMW Platform** provides a built-in API sandbox powered by Swagger.

- Swagger provides a detailed reference on API methods, including request and response descriptions, and data models with example values.
- Swagger allows you to execute requests and view responses.
- When executing a request, Swagger generates an API resource URI to use in external systems, including the request body syntax template.

1. To open the Swagger page, enter   `https://your-host/docs`, where   `your-host` is the domain name of your server, in your browser address bar.
2. The **CMW Platform API** page appears with the following sections:
   - **RESTful Web API** —immutable methods common for all software versions (see [Web API Methods](https://kb.comindware.ru/article.php?id=1941));
   - **System Core API** — system methods that may differ for different software versions;
   - **Solution API** — methods for business application templates (see [Solution API Methods](https://kb.comindware.ru/article.php?id=2074)).
3. Go to the required API page.
4. Expand an API method in the list.
5. Select the request and response format in the **Response Content Type** field.
6. Run a method by clicking **Try it out**.
7. The request template will be generated: 
   - **Request URL** — copy this string to an external system as the request URI. For `GET` and   `DELETE` requests, it contains the entire request.
   - **Example Value** — copy this string to an external system as the request body.

_![Swagger page with the CMW Platform API sections](https://kb.cmwlab.com/assets/img_661e5cf63fc5a.png)_

## Example: Call a System Core API Method

To create a record template using the System Core API, send the following `POST` request to the **Request URL**obtained in Swagger:

```
http://your-host/api/public/system/TeamNetwork/ObjectAppService/Create
```

- `Substitute your-host` with your **CMW Platform** instance URL.
- In the request `body`, specify the system name of the record template (for example,   `"Car"`).
- In the response, the **CMW Platform**will return the ID of the created record template (for example,   `"oa.1"`).

## Related Articles

**[Solution API Methods](https://kb.comindware.ru/article.php?id=2074)**

**[Web API Methods](https://kb.comindware.ru/article.php?id=1941)**

 [*‌*Back to top](#)

