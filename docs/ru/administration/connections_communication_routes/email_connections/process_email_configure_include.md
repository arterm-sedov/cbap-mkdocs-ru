
{% if not pdfOutput and not kbExport %}

# Отправка, получение и обработка эл.&nbsp;почты в процессе. Пример: настройка подключений, путей передачи данных, диаграммы процесса и сценария

{%
include-markdown "examples/process_email_configure.md"
rewrite-relative-urls=false
start="<!--include-start-->"
end="<!--include-end-->"
%}

{% endif %}
