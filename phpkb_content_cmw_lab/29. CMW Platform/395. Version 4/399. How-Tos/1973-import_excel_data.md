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

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
