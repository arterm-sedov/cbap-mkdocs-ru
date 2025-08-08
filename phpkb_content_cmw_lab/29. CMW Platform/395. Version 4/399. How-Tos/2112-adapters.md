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

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
