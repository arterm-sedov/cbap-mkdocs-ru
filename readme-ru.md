## Репозиторий с поддержкой ИИ

Задавайте вопросы о **Comindware Platform** по этому репозиторию через DeepWiki:

[Ask DeepWiki](https://deepwiki.com/arterm-sedov/cbap-mkdocs-ru)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/arterm-sedov/cbap-mkdocs-ru)

**Английская версия:** [readme.md](readme.md).

# База знаний MkDocs — рабочие процессы и руководство оператора

В репозитории хранится исходный код MkDocs для базы знаний **Comindware Platform**.
Статьи в Markdown — в `docs/ru/`, HTML для импорта в PHPKB — в `for_kb_import_ru/`, снимки PHPKB — в `phpkb_content/` и `phpkb_content_rag/`, пакеты для LLM (RAG), а также по желанию **веб-скрапинг** публичных сайтов (`comindware.ru`, `cmwlab.com`) в `scraping/`.

**Назначение:** это **руководство оператора** — структура репозитория, команды терминала, конфиги MkDocs, публикация в PHPKB, RAG и PDF.

**Редактируете статьи или пишете новый контент?** Действуют **те же правила, что и для ИИ-агентов** — оформление, ссылки, якоря, теги и плейсхолдеры продуктов описаны в [`AGENTS.md`](AGENTS.md). В настоящем файле правила не дублируются, приведены только ссылки на них. Здесь описано, *как* собирать, импортировать и публиковать; в `AGENTS.md` — *как* писать корректный Markdown.

**Команды:** из корня репозитория. В сценариях — блоки **PowerShell** (Windows) и **bash** (WSL / Ubuntu / Linux / macOS).

**Python — два эквивалентных стиля:**

| Стиль | Когда | Пример |
| --- | --- | --- |
| **Полный путь** (в сценариях ниже) | Новое окно терминала, venv не активирован; надёжное копирование команд | `.\.venv\Scripts\python.exe -m mkdocs build …` (Win) · `.venv/bin/python -m mkdocs build …` (Linux) |
| **Короче** (venv **активирован**) | После `Activate.ps1` / `source .venv/bin/activate` в этой сессии | `python -m mkdocs build …` · `pip install …` · `python phpkb_update_articles.py …` |

**Как это работает:** *venv* (virtual environment) — папка `.venv` со своим `python.exe`. Команда с **полным путём** сразу указывает на него — отдельно «включать» venv не нужно. **Активация** (*activate*: `Activate.ps1` / `source .venv/bin/activate`) один раз настраивает текущее окно терминала: дальше достаточно писать `python` и `pip` без длинного пути — удобно, если подряд идёт много команд. Оба способа запускают **один и тот же** интерпретатор и пакеты.

Прочее: `$env:CMW_KB_REPO_PATH` → `$CMW_KB_REPO_PATH` (сначала `export` из `.env`). Подробнее: [Первоначальная настройка → venv](#1-виртуальное-окружение-python).

**Обозначения:** там, где в командах и интерфейсе Git/GitHub встречается иностранная терминология, русский термин сопровождается **английским эквивалентом в скобках** — например, перенос коммитов (*cherry-pick*), слияние веток (*merge*), отправка (*push*).

## Карта документа

| Раздел | Назначение |
| --- | --- |
| [Структура репозитория](#структура-репозитория) | Где лежат файлы; что в Git |
| [Первоначальная настройка](#первоначальная-настройка) | `.venv`, `.env`, репозиторий ассетов PHPKB |
| [Быстрый выбор сценария](#быстрый-выбор-сценария) | Какой рабочий процесс (*workflow*) запустить |
| Редактирование / публикация / RAG / изображения / пакет для LLM (*bundle*) | Пошаговые команды |
| [JSON-карты сопоставления](#json-карты-сопоставления) | Карты статей (*article maps*); карты клонирования (*clone mappings*) |
| [Конфигурация MkDocs](#конфигурация-mkdocs) | Выбор `mkdocs*.yml`; наследование YAML (*inheritance*) |
| [Скрипты репозитория](#скрипты-репозитория) | Python-скрипты в корне репозитория |
| [Переопределения темы](#переопределения-темы) | Каталоги `overrides/`, `pdf_templates/` |
| [Основы Jinja](#основы-jinja) | Плейсхолдеры и условия `{% if %}` в статьях |
| [Сборка PDF-руководств](#сборка-pdf-руководств) | GTK3, WeasyPrint; пакетная сборка |
| [Хуки сборки MkDocs](#хуки-сборки-mkdocs) | Скрипт `kb_html_cleanup_hook.py` |
| [Git-хуки](#git-хуки) | Каталог `.githooks/`; формат сообщений коммитов |
| [MkDocs serve (локальный предпросмотр)](#mkdocs-serve-локальный-предпросмотр) | Конфигурации и параметры `mkdocs serve` |
| [Удалённые репозитории Git](#удалённые-репозитории-git-remotes) | *Remotes*: `origin`; форк команды; зеркала |
| [Ежедневная работа с Git](#ежедневная-работа-с-git-platform_v5--platform_v6) | Начало дня; ветки задач; отправка (*push*) |
| [Перенос коммитов и слияние между версиями платформы](#перенос-коммитов-и-слияние-между-версиями-платформы) | *Cherry-pick* / *merge*: правила для `platform_v5` ↔ `platform_v6` |
| [GitHub CLI (gh)](#github-cli-gh) | `gh pr`, `gh issue`; проверки CI |
| [Деплой ассетов PHPKB](#деплой-репозитория-ассетов-копирование-push-ssh-pull) | Соседний репозиторий (*sibling*); *push* и SSH *pull* на сервер БЗ |
| [Веб-скрапинг для LLM](#веб-скрапинг-для-llm) | Обход сайтов → очистка → коммит |
| [Стандарты редактирования](#стандарты-редактирования-контента) | Правила статей — индекс в `AGENTS.md` + раздел Jinja ниже |
| [Skills для агентов](#skills-для-агентов-справка-agent-skills) | Сценарии (*skills*); полный список в `AGENTS.md` |
| [Каталог `.scratch/`](#каталог-scratch) | Временные одноразовые файлы |
| [Устранение неполадок](#устранение-неполадок) | Типичные ошибки и их устранение |

**Пишете или правите `docs/ru/`?** → [`AGENTS.md`](AGENTS.md) · [Стандарты редактирования](#стандарты-редактирования-контента). **Запускаете сборки, импорт или скрипты?** → разделы ниже · [`AGENTS.md` → Перекрёстные ссылки для операторов](AGENTS.md#human-operators--readme-cross-reference) · [Справочник навыков](AGENTS.md#skills-reference).

## Стандарты редактирования контента

У людей и агентов один свод правил: [`AGENTS.md`](AGENTS.md). Перед правкой откройте строки, относящиеся к вашей задаче.

**Содержимое статей**

| Тема | `AGENTS.md` | Этот readme (механика сборки) |
| --- | --- | --- |
| Перекрёстные `[текст][anchor_name]`; центральный справочник именованных якорей; `autorefs` | [Оформление ссылок](AGENTS.md#link-formatting) | [Подключение сниппетов](#подключение-сниппетов) · [Ссылки в статьях](#ссылки-в-статьях) |
| Внутри страницы — только `[текст](#anchor_name)` | [Оформление ссылок](AGENTS.md#link-formatting) | [Ссылки в статьях](#ссылки-в-статьях) |
| Подключение карты в **конце каждой** статьи в `docs/` | [Include карты](AGENTS.md#hyperlink-map-include-required-on-every-article) | [Подключение сниппетов](#подключение-сниппетов) |
| URL раздела БЗ (`kbId#fragment`) — только в карте | [Фрагменты в карте](AGENTS.md#map-urls-with-kbidsection_anchor-fragments) | — |
| `{% if %}` в карте и флаги руководств / `kbExport` | [Условия в карте](AGENTS.md#how-map-conditionals-mirror-yaml-configs) | [Флаги руководств](#флаги-руководств-extra) · [Условный контент](#условный-контент) |
| Маркированные и нумерованные списки | [Списки](AGENTS.md#list-formatting) | — |
| Курсив и полужирный | [Курсив](AGENTS.md#italic) · [Полужирный](AGENTS.md#bold) | — |
| `**{{ productName }}**` и плейсхолдеры брендов | [Имена продуктов и брендов](AGENTS.md#product--brand-names) | [Плейсхолдеры продуктов](#плейсхолдеры-продуктов) |
| Теги в frontmatter | [Теги](AGENTS.md#tags) | — |
| `&nbsp;` и подобное | [HTML-сущности](AGENTS.md#html-entities) | — |
| `{: #anchor .pageBreak_* }` у заголовков (только `docs/ru/`) | [Заголовки](AGENTS.md#headings) · [Правила](AGENTS.md#rules) (сохранять якоря/классы) | — |
| Жёсткий разрыв страницы в PDF | [Заголовки](AGENTS.md#headings) | [Разрывы страниц в PDF](#разрывы-страниц-в-pdf) |

**Репозиторий и Git** (операторы — команды в разделах ниже)

| Тема | `AGENTS.md` | Этот readme |
| --- | --- | --- |
| Не править `phpkb_content/` вручную | [Контекст](AGENTS.md#context) | [Структура репозитория](#структура-репозитория) |
| Временные файлы только в `.scratch/` | [Каталог `.scratch/`](AGENTS.md#scratch-directory) | [Каталог `.scratch/`](#каталог-scratch) |
| Формат коммита `[#ticket]` | [Сообщения коммитов](AGENTS.md#commit-messages) | [Git-хуки](#git-хуки) · навык `cmwhelp-commit` |
| *Cherry-pick* / раздельные коммиты по слоям артефактов | [Перенос между версиями](AGENTS.md#cherry-picking-between-platform-versions) | [Перенос коммитов и слияние](#перенос-коммитов-и-слияние-между-версиями-платформы) |
| Python `.venv` / вызов скриптов | [Окружение Python](AGENTS.md#python-environment) | [Первоначальная настройка](#первоначальная-настройка) |
| Сквозные сценарии | [Справочник навыков](AGENTS.md#skills-reference) | [Skills](#skills-для-агентов-справка-agent-skills) · [Быстрый выбор сценария](#быстрый-выбор-сценария) |

Обратный индекс (readme → `AGENTS.md`): [`AGENTS.md` → Перекрёстные ссылки для операторов](AGENTS.md#human-operators--readme-cross-reference).

## Структура репозитория

| Путь | Назначение | В Git | Кто меняет |
| --- | --- | --- | --- |
| `docs/ru/` | Исходники MkDocs (Markdown) | Да | Редакторы / агенты |
| `for_kb_import_ru/` | HTML для импорта в PHPKB | Да | `mkdocs build -f mkdocs_for_kb_import_ru.yml` |
| `phpkb_content/` | Снимок PHPKB с преобразованиями MkDocs | Да | Только `phpkb_import.py` — **не править вручную** |
| `phpkb_content_rag/` | Снимок PHPKB для RAG (только Markdown) | Да | Только `phpkb_import_for_rag.py` — **не править вручную** |
| `phpkb_content_cmw_lab/` | Снимок PHPKB для CMW Lab / v4 | Да | Только `phpkb_import_cmw_lab.py` — **не править вручную** |
| `kb.comindware.ru.platform_v*_for_llm_ingestion.md` | Однофайловый пакет для LLM | Да | `phpkb_ingest.py` |
| `kb.comindware.ru/platform/` | Символическая ссылка (junction) на репозиторий ассетов PHPKB | **Нет** (в `.gitignore`) | Скрипты копирования |
| `scraping/{site}/` | Очищенный результат веб-обхода и контрольные точки | Да | Скрипты обхода и очистки |
| `.scratch/` | Временные файлы (в т.&nbsp;ч. сырые `*_dirty_*.md`) | Нет | Операторы (каталог в `.gitignore`) |

Папки `phpkb_content/` и `phpkb_content_rag/` подчиняются **асимметричному** правилу переноса коммитов (*cherry-pick*): деревья v5 (`798-platform_v5/`) и пакет LLM для v5 можно переносить **только на ветку `platform_v6`**; **не переносите** на `platform_v5` деревья импорта v6 и пакет v6. Каталог **`for_kb_import_ru/`** между ветками не переносят — пересоберите его на целевой ветке. Подробнее: [Перенос коммитов и слияние между версиями платформы → Перенос коммитов и пересборка (cherry-pick vs rebuild)](#перенос-коммитов-и-пересборка-cherry-pick-vs-rebuild).

**Два отдельных Git-репозитория:**

1. **Этот репозиторий** (`cbap-mkdocs-ru`) — Markdown, HTML-экспорт, RAG-деревья, пакет LLM в корне.
2. **Репозиторий статических ассетов PHPKB** (соседняя локальная копия, *sibling checkout*) — путь в `.env`: `CMW_KB_REPO_PATH`. Изображения и пакеты LLM публикуются в `platform/v5.0/` или `platform/v6.0/`.

**Не** выполняйте `git add kb.comindware.ru/` в этом репозитории. Коммитьте ассеты в репозитории PHPKB (вручную или через флаги `--git` у скриптов).

**Исходный код платформы** (соседний репозиторий, проверка поведения функций): `PLATFORM_SOURCE_CODE` в `.env` (см. `.env.example`). Обычно: `../CBAP_MONO`.

## Первоначальная настройка

### 1. Виртуальное окружение Python

Все пакеты Python для репозитория перечислены в `install/requirements.txt` (MkDocs, плагины, скрипты PHPKB, инструменты скрапинга и т.д.). Устанавливайте их в локальный `.venv` в корне репозитория — не в системный Python.

**Первый раз** (ещё нет `.venv`) — запустите скрипт развёртывания через **системный** Python:

```powershell
# Windows — интерактивно: создаёт .venv, обновляет pip, ставит requirements.txt
py install\deploy_venv.py
# На запрос имени папки venv — Enter: по умолчанию `.venv` (зашито в install/deploy_venv.py, не в .env)

# Проверка
.\.venv\Scripts\python.exe -c "import mkdocs; print('OK')"
```

```bash
# WSL / Ubuntu / Linux — то же самое
python3 install/deploy_venv.py

# Проверка
.venv/bin/python -c "import mkdocs; print('OK')"
```

`install/deploy_venv.py` создаёт `.venv`, обновляет `pip` и выполняет `pip install -U -r install/requirements.txt`. Альтернатива для Windows без диалога: `install\deploymkdocs.ps1`.

**Обновление зависимостей**, если изменился `install/requirements.txt` (например после `git pull`) — `.venv` уже должен существовать:

```powershell
# Windows — с активированным venv или полным путём к python.exe
.\.venv\Scripts\python.exe -m pip install -U -r install\requirements.txt
```

```bash
# WSL / Ubuntu / Linux
.venv/bin/python -m pip install -U -r install/requirements.txt
```

**Активация venv** (в каждой новой сессии терминала). Из корня репозитория:

| Среда | Команда |
| --- | --- |
| Windows (PowerShell) | `.\.venv\Scripts\Activate.ps1` |
| Windows (cmd.exe) | `.\.venv\Scripts\activate.bat` |
| WSL / Ubuntu / Linux | `source .venv/bin/activate` |

Если PowerShell блокирует активацию (execution policy), в текущей сессии: `Set-ExecutionPolicy -Scope Process Bypass`, затем снова `Activate.ps1`.

**Полный путь vs активированный venv** — результат один, выбор по ситуации:

| Задача | Без активации (на лету) | С активированным venv |
| --- | --- | --- |
| Сборка MkDocs | `.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml` | `python -m mkdocs build -f mkdocs_for_kb_import_ru.yml` |
| MkDocs serve | `.\.venv\Scripts\python.exe -m mkdocs serve` | `python -m mkdocs serve` |
| Скрипт PHPKB | `.\.venv\Scripts\python.exe phpkb_update_articles.py …` | `python phpkb_update_articles.py …` |
| Обновление deps | `.\.venv\Scripts\python.exe -m pip install -U -r install\requirements.txt` | `pip install -U -r install/requirements.txt` |

```bash
# Linux — без активации
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
.venv/bin/python phpkb_update_articles.py --profile cmw --article-id 123 --yes

# Linux — после: source .venv/bin/activate
python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
python phpkb_update_articles.py --profile cmw --article-id 123 --yes
```

В сценариях ниже — **полные пути**, чтобы команды работали в новой сессии без активации. После `Activate.ps1` или `source .venv/bin/activate` замените `.\.venv\Scripts\python.exe` / `.venv/bin/python` на `python` (и `pip` вместо `python -m pip`).

Если venv сломан (неверный путь `pip`, нет плагинов), снова запустите `install/deploy_venv.py` или см. `.agents/skills/python-env-setup/SKILL.md`.

### Окончания строк Git

Текстовые файлы в репозитории — **LF** (`\n`). Политика в `.gitattributes` (`eol=lf`); генераторы на Python пишут через `tools/text_io.py`. Git нормализует текст при `git add` — отдельная проверка после каждого прогона не нужна.

На Windows, если `git status` показывает массовые «ложные» изменения, исчезающие после `git add`, отключите глобальное CRLF-преобразование:

```powershell
git config --global core.autocrlf false
```

После обновления `.gitattributes` один раз на ветке:

```powershell
git add --renormalize .
git status
```

Подробнее: [Git line endings](readme.md#git-line-endings) в английском readme.

### 2. Конфигурация `.env`

```powershell
Copy-Item .env.example .env
# Заполните SSH, SQL и пути к репозиторию PHPKB
```

```bash
cp .env.example .env
# Заполните SSH, SQL и пути к репозиторию PHPKB
```

Загрузка переменных в bash (из корня репозитория):

```bash
set -a && source .env && set +a
```


| Переменная | Нужна для | Назначение |
| --- | --- | --- |
| `SERVER_PROFILE` | Скрипты БД | `cmw` (kb.comindware.ru) или `cmwlab` |
| `CMW_SSH_*`, `CMW_SQL_*` | Публикация, импорт | SSH-туннель + MySQL к PHPKB |
| `CMW_KB_REPO_PATH` | `--git` для изображений/бандла | Локальная копия (*checkout*) ассетов PHPKB |
| `CMW_SSH_KB_REPO_PATH` | `--pull` | Путь на продакшене для `git pull` |

Опционально: `SSH_USE_STORED_CREDENTIALS=1` — без запросов keychain. Полный список: `.env.example`.

### 3. Локальная копия репозитория ассетов PHPKB (*checkout*)

Клонируйте репозиторий **статических ассетов** kb.comindware как **соседнюю локальную копию** (*sibling checkout*) рядом с этим репозиторием и укажите путь в `.env`.

**Пример (Windows):** если этот репозиторий — `C:\Repos\cbap-mkdocs-ru`, клонируйте ассеты в `C:\Repos\kb.comindware.ru`:

```ini
# В .env (gitignore — не коммитить)
CMW_KB_REPO_PATH=C:/Repos/kb.comindware.ru
CMW_SSH_KB_REPO_PATH=/var/www/html
```

`CMW_KB_REPO_PATH` — локальная копия (*checkout*), куда скрипты копируют изображения и пакеты LLM (`platform/v5.0/`, `platform/v6.0/`).

`CMW_SSH_KB_REPO_PATH` — на **продакшен-сервере БЗ** путь к тому же git-репозиторию (для `utilities/ssh_pull.py` при `--pull`). Обычно **не совпадает** с Windows-путём.

SSH для публикации/импорта в PHPKB использует тот же профиль (`CMW_SSH_HOST`, `CMW_SSH_USERNAME`, …) — см. `.env.example`. `SSH_USE_STORED_CREDENTIALS=1` — если вход по ключу/agent, без пароля в `.env`.

Проверка соседней локальной копии (*sibling checkout*):

```powershell
Test-Path "$env:CMW_KB_REPO_PATH\.git"
Get-ChildItem "$env:CMW_KB_REPO_PATH\platform\v6.0" -ErrorAction SilentlyContinue | Select-Object -First 5
```

```bash
test -d "$CMW_KB_REPO_PATH/.git"
ls "$CMW_KB_REPO_PATH/platform/v6.0" 2>/dev/null | head
```

При необходимости создайте junction **внутри этого репозитория** (не обязательно, если задан `CMW_KB_REPO_PATH`):

```powershell
# Подставьте свои пути
New-Item -ItemType Junction -Path "kb.comindware.ru\platform\v6.0" -Target "D:\Repo\kb.comindware.ru\platform\v6.0"
Get-Item kb.comindware.ru\platform\v6.0 | Format-List LinkType, Target
```

```bash
# Симлинк вместо junction (Windows)
ln -s /path/to/kb.comindware.ru/platform/v6.0 kb.comindware.ru/platform/v6.0
ls -la kb.comindware.ru/platform/v6.0
```


Проверьте junction перед копированием изображений или бандлов.

### 4. Справочник по версиям платформы

| Платформа | Корневая категория PHPKB | Папка RAG | Карта статей | Файл бандла | Цель ассетов |
| --- | --- | --- | --- | --- | --- |
| v5.0 | `798` | `phpkb_content_rag/798-platform_v5` | `.article_id_filename_map_v5.json` | `kb.comindware.ru.platform_v5_for_llm_ingestion.md` | `kb.comindware.ru/platform/v5.0` |
| v6.0 | `896` | `phpkb_content_rag/896-platform_v6` | `.article_id_filename_map_v6.json` | `kb.comindware.ru.platform_v6_for_llm_ingestion.md` | `kb.comindware.ru/platform/v6.0` |

Работайте в ветке Git, соответствующей целевой платформе (`platform_v5`, `platform_v6` и т.&nbsp;д.).

## Быстрый выбор сценария

| Задача | Раздел |
| --- | --- |
| Правка существующей статьи и публикация в PHPKB | [Правка → HTML → публикация → коммит](#правка-сборка-html-публикация-коммит) |
| Пакетная публикация изменённых статей | [Пакетная публикация по git diff](#пакетная-публикация-по-git-diff) |
| Новая статья в PHPKB | [Публикация новой статьи](#публикация-новой-статьи) |
| Копирование новых/обновлённых изображений | [Синхронизация изображений](#синхронизация-изображений-с-репозиторием-ассетов-phpkb) |
| Обновление RAG-корпуса из БД PHPKB | [Обновление phpkb_content_rag](#обновление-phpkb_content_rag) |
| Снимок PHPKB для MkDocs | [Обновление phpkb_content](#обновление-phpkb_content) |
| Пересборка LLM-бандла | [Сборка AI-бандла](#сборка-ai-бандла) |
| Бандл в репозиторий PHPKB + продакшен | [Публикация бандла в соседний репозиторий](#публикация-ai-бандла-в-соседний-репозиторий) |
| Ассеты в соседнем KB (*sibling*) + SSH *pull* на сервере | [Деплой ассетов PHPKB](#деплой-репозитория-ассетов-копирование-push-ssh-pull) |
| Краул публичного сайта для LLM | [Веб-скрапинг](#веб-скрапинг-для-llm) |
| Локальный просмотр документации | [MkDocs serve](#mkdocs-serve-локальный-предпросмотр) |
| Сборка PDF-руководств | [Сборка PDF](#сборка-pdf-руководств) |
| Конфиги MkDocs | [Конфигурация MkDocs](#конфигурация-mkdocs) |
| Плейсхолдеры и условный текст | [Основы Jinja](#основы-jinja) |
| Тема HTML / экспорт PHPKB | [Переопределения темы](#переопределения-темы) |
| Git-хуки для коммитов | [Git-хуки](#git-хуки) |
| Правка контента статей | [`AGENTS.md`](AGENTS.md) · [Стандарты редактирования](#стандарты-редактирования-контента) |
| Перенос коммитов (*cherry-pick*) `platform_v5` / `platform_v6` | [Перенос коммитов и слияние между версиями платформы](#перенос-коммитов-и-слияние-между-версиями-платформы) (также в `AGENTS.md`) |
| Git: *remotes*, ежедневный цикл, `gh` | [Remotes](#удалённые-репозитории-git-remotes) · [Ежедневная работа](#ежедневная-работа-с-git-platform_v5--platform_v6) · [GitHub CLI](#github-cli-gh) |

## Правка → сборка HTML → публикация → коммит

Стандартный цикл для **существующей** статьи с `kbId:` во frontmatter.

### 1. Правка Markdown

Файл в `docs/ru/`. Те же стандарты, что у агентов — [Стандарты редактирования](#стандарты-редактирования-контента) (полный текст в `AGENTS.md`).

### 2. Сборка HTML для PHPKB

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

```bash
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

Дождитесь `Documentation built in N seconds`. Предупреждения о якорях не критичны.

### 3. Проверка изменений экспорта

```powershell
git diff --name-only for_kb_import_ru/
git status --short for_kb_import_ru/
```

### 4. Извлечение `kb-id` и публикация в PHPKB

```powershell
# Подставьте путь к HTML статьи
Select-String -Path for_kb_import_ru\administration\deploy\script_keys.html -Pattern 'kb-id="(\d+)"' |
  ForEach-Object { $_.Matches.Groups[1].Value } | Select-Object -First 1

# Публикация (--yes без подтверждений)
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --article-id <kb-id> --yes
```

```bash
# Подставьте путь к HTML статьи
rg -o 'kb-id="([0-9]+)"' for_kb_import_ru/administration/deploy/script_keys.html -r '$1' | head -1

# Публикация (--yes без подтверждений)
.venv/bin/python phpkb_update_articles.py --profile cmw --article-id <kb-id> --yes
```

В выводе: `Updated article <kb-id>`.

URL статьи: `https://kb.comindware.ru/article.php?id=<kb-id>`.

### 5. Синхронизация изображений (если добавлены или изменены)

См. [Синхронизацию изображений](#синхронизация-изображений-с-репозиторием-ассетов-phpkb).

### 6. Коммит и отправка (*push*) — этот репозиторий

```powershell
git add docs/ru/<файл>.md for_kb_import_ru/<экспорт>.html
git commit -m "[#<ticket>] <краткое описание>"
git push
```

Формат: `[#XXXXX] Описание в повелительном наклонении`. См. `.agents/skills/cmwhelp-commit/SKILL.md`.

## Пакетная публикация по git diff

Несколько статей уже отредактированы, HTML пересобран в `for_kb_import_ru/`.

### 1. Пересборка (если ещё не делали)

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

```bash
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

### 2. Список изменённых HTML

```powershell
git diff --name-only for_kb_import_ru/
```

### 3. Сбор значений `kb-id`

Из каждого изменённого `.html` — атрибут `kb-id="…"`. Пропускайте `kb-id=""` — в PHPKB ещё нет записи; добавьте `kbId:` в `.md` или клонируйте заглушку.

```powershell
Select-String -Path for_kb_import_ru\**\*.html -Pattern 'kb-id="(\d+)"' |
  ForEach-Object { $_.Matches.Groups[1].Value } | Where-Object { $_ } | Sort-Object -Unique
```

```bash
rg -o 'kb-id="([0-9]+)"' for_kb_import_ru/ -r '$1' | sort -u
```

### 4. Публикация всех ID одной командой

```powershell
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --yes `
  --article-id 5451 --article-id 5558
```

```bash
.venv/bin/python phpkb_update_articles.py --profile cmw --yes \
  --article-id 5451 --article-id 5558
```

Или всё дерево категории:

```powershell
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --category-id 896 --yes
```

```bash
.venv/bin/python phpkb_update_articles.py --profile cmw --category-id 896 --yes
```

### 5. Коммит исходников и экспорта

```powershell
git add docs/ru/ for_kb_import_ru/
git commit -m "[#<ticket>] Publish updated articles to PHPKB"
git push
```

## Публикация новой статьи

Локальный Markdown **без** `kbId:`, который должен стать новой статьёй PHPKB.

1. Клонирование соседней статьи: `utilities/phpkb_cloning/phpkb_clone.py` (сначала dry-run). См. `.agents/skills/phpkb-cloning/SKILL.md`.
2. `kbId: <new-id>` во frontmatter.
3. При необходимости — запись в `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`.
4. Сборка и публикация:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --article-id <new-id> --yes
```

```bash
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
.venv/bin/python phpkb_update_articles.py --profile cmw --article-id <new-id> --yes
```

5. Коммит `docs/ru/`, `for_kb_import_ru/` и карты гиперссылок.

## Синхронизация изображений с репозиторием ассетов PHPKB

Копирует изображения из `for_kb_import_ru/` в `{CMW_KB_REPO_PATH}/platform/{version}/`.

**Сначала** пересоберите HTML, чтобы `for_kb_import_ru/` был актуален.

```powershell
# Только копирование
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0

# Копирование + commit + push в репозитории ассетов
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git

# + git pull на продакшене по SSH
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git --pull

# Без интерактивных запросов
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git --pull --no-ask
```

```bash
# Только копирование
.venv/bin/python phpkb_copy_images.py --version v6.0

# Копирование + commit + push в репозитории ассетов
.venv/bin/python phpkb_copy_images.py --version v6.0 --git

# + git pull на продакшене по SSH
.venv/bin/python phpkb_copy_images.py --version v6.0 --git --pull

# Без интерактивных запросов
.venv/bin/python phpkb_copy_images.py --version v6.0 --git --pull --no-ask
```

`--version` **обязателен** (`v4.7`, `v5.0` или `v6.0`).

Скрипт копирует **все** изображения из дерева экспорта. Если изменилась одна статья — проверьте diff в репозитории PHPKB:

```powershell
git -C "$env:CMW_KB_REPO_PATH" status --short -- platform/v6.0
git -C "$env:CMW_KB_REPO_PATH" diff --name-status -- platform/v6.0
```

```bash
git -C "$CMW_KB_REPO_PATH" status --short -- platform/v6.0
git -C "$CMW_KB_REPO_PATH" diff --name-status -- platform/v6.0
```

### Вручную (репозиторий ассетов PHPKB)

```powershell
git -C "$env:CMW_KB_REPO_PATH" add platform/v6.0/
git -C "$env:CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6.0 images"
git -C "$env:CMW_KB_REPO_PATH" push
```

```bash
git -C "$CMW_KB_REPO_PATH" add platform/v6.0/
git -C "$CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6.0 images"
git -C "$CMW_KB_REPO_PATH" push
```

## Обновление phpkb_content_rag

Импорт статей из БД PHPKB в `phpkb_content_rag/` (только markdown, для RAG/LLM). **Только чтение PHPKB** — пишет локальные файлы.

**Длительность:** 5–10+ минут на полную категорию. Дождитесь `Import finished. Total articles imported: <N>`.

### v6

```powershell
.\.venv\Scripts\python.exe phpkb_import_for_rag.py `
  --category-id 896 `
  --article-map .article_id_filename_map_v6.json
```

```bash
.venv/bin/python phpkb_import_for_rag.py \
  --category-id 896 \
  --article-map .article_id_filename_map_v6.json
```

### v5

```powershell
.\.venv\Scripts\python.exe phpkb_import_for_rag.py `
  --category-id 798 `
  --article-map .article_id_filename_map_v5.json
```

```bash
.venv/bin/python phpkb_import_for_rag.py \
  --category-id 798 \
  --article-map .article_id_filename_map_v5.json
```

### После импорта — коммит

```powershell
git status --short phpkb_content_rag/
git add phpkb_content_rag/
git commit -m "[#<ticket>] Refresh phpkb_content_rag from PHPKB"
git push
```

**Не правьте `phpkb_content_rag/` вручную.** Перегенерируйте из PHPKB или исправьте `docs/ru/`.

## Обновление phpkb_content

Импорт в `phpkb_content/` с полными преобразованиями MkDocs. Независим от `phpkb_content_rag/` — оба читают БД напрямую.

`--article-map` **обязателен**.

### v6

```powershell
.\.venv\Scripts\python.exe phpkb_import.py `
  --category-id 896 `
  --article-map .article_id_filename_map_v6.json
```

```bash
.venv/bin/python phpkb_import.py \
  --category-id 896 \
  --article-map .article_id_filename_map_v6.json
```

### v5

```powershell
.\.venv\Scripts\python.exe phpkb_import.py `
  --category-id 798 `
  --article-map .article_id_filename_map_v5.json
```

```bash
.venv/bin/python phpkb_import.py \
  --category-id 798 \
  --article-map .article_id_filename_map_v5.json
```

### После импорта — коммит

```powershell
git status --short phpkb_content/
git add phpkb_content/
git commit -m "[#<ticket>] Refresh phpkb_content from PHPKB"
git push
```

## Сборка AI-бандла

Собирает `phpkb_content_rag/` в один Markdown для LLM. Без доступа к БД.

Все четыре аргумента **обязательны**: `--folder`, `--output`, `--target-dir`, `--category-id`.

### v6

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896
```

### v5

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/798-platform_v5 `
  --output kb.comindware.ru.platform_v5_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v5.0 `
  --category-id 798
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/798-platform_v5 \
  --output kb.comindware.ru.platform_v5_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v5.0 \
  --category-id 798
```

### Проверка заголовка бандла

- `Ingestion date` — текущая дата/время
- `Files analyzed` — число markdown-файлов
- `Estimated tokens` — оценка tiktoken

В консоли: `File copied to: kb.comindware.ru\platform\v6.0\...`

### Только бандл (RAG уже актуален)

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896
```

С git-sync и pull на продакшене:

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896 `
  --version v6.0 --git --pull --no-ask
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896 \
  --version v6.0 --git --pull --no-ask
```

**Безопасность:** `phpkb_import_for_rag.py` — только чтение PHPKB; `phpkb_ingest.py` — только локальное дерево. Не путать с `phpkb_update_articles.py` (запись в БД). **`--article-map` обязателен** для обоих импорт-скриптов.

### Полное обновление (RAG + снимок + бандл)

```powershell
# Пример v6 — для v5 подставьте свои ID и пути
.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896 --article-map .article_id_filename_map_v6.json
.\.venv\Scripts\python.exe phpkb_import.py --category-id 896 --article-map .article_id_filename_map_v6.json
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896
```

```bash
# Пример v6 — для v5 подставьте свои ID и пути
.venv/bin/python phpkb_import_for_rag.py --category-id 896 --article-map .article_id_filename_map_v6.json
.venv/bin/python phpkb_import.py --category-id 896 --article-map .article_id_filename_map_v6.json
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896
```

### Коммит бандла

**Три отдельных коммита** — не объединяйте деревья импорта и бандл:

```powershell
git add phpkb_content/
git commit -m "[#<ticket>] Refresh phpkb_content from PHPKB"

git add phpkb_content_rag/
git commit -m "[#<ticket>] Refresh phpkb_content_rag from PHPKB"

git add kb.comindware.ru.platform_v6_for_llm_ingestion.md
git commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git push
```

```bash
git add phpkb_content/
git commit -m "[#<ticket>] Refresh phpkb_content from PHPKB"

git add phpkb_content_rag/
git commit -m "[#<ticket>] Refresh phpkb_content_rag from PHPKB"

git add kb.comindware.ru.platform_v6_for_llm_ingestion.md
git commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git push
```

Правки статей, HTML-экспорт и каждый артефакт импорта/бандла (`phpkb_content/`, `phpkb_content_rag/`, пакет LLM) коммитьте **раздельно** — проще переносить коммиты (*cherry-pick*) между ветками версий.

## Публикация AI-бандла в соседний репозиторий

После `phpkb_ingest.py` бандл в **двух местах**:

1. Корень этого репозитория — `kb.comindware.ru.platform_v*_for_llm_ingestion.md`
2. `{CMW_KB_REPO_PATH}/platform/{version}/` — репозиторий ассетов PHPKB

### Автоматически (рекомендуется)

`--git` — commit/push в PHPKB; `--pull` — `git pull` на продакшене по SSH.

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896 `
  --version v6.0 `
  --git --pull --no-ask
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896 \
  --version v6.0 \
  --git --pull --no-ask
```

`--git` → `utilities/git_sync.py`. `--pull` → `utilities/ssh_pull.py`.

Подробно (локальный `C:/Repos/kb.comindware.ru`, SSH pull на сервере): [Деплой ассетов PHPKB](#деплой-репозитория-ассетов-копирование-push-ssh-pull).

### Вручную

```powershell
git add kb.comindware.ru.platform_v6_for_llm_ingestion.md
git commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git push

git -C "$env:CMW_KB_REPO_PATH" add platform/v6.0/kb.comindware.ru.platform_v6_for_llm_ingestion.md
git -C "$env:CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git -C "$env:CMW_KB_REPO_PATH" push
```

```bash
git add kb.comindware.ru.platform_v6_for_llm_ingestion.md
git commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git push

git -C "$CMW_KB_REPO_PATH" add platform/v6.0/kb.comindware.ru.platform_v6_for_llm_ingestion.md
git -C "$CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git -C "$CMW_KB_REPO_PATH" push
```


## Деплой репозитория ассетов: копирование, push, SSH pull

*push — отправка в удалённый репозиторий; pull — выгрузка на сервер.*

Статические ассеты (изображения, LLM-бандлы) хранятся в **отдельном git-репозитории**, не в `cbap-mkdocs-ru`. Типичная структура на машине разработчика:

```
C:\Repos\
  cbap-mkdocs-ru\          ← этот репозиторий (Markdown, HTML, копия бандла в корне)
  kb.comindware.ru\        ← sibling (CMW_KB_REPO_PATH в .env)
    platform\
      v5.0\                ← изображения + kb.comindware.ru.platform_v5_for_llm_ingestion.md
      v6.0\                ← изображения + kb.comindware.ru.platform_v6_for_llm_ingestion.md
```

На **сервере БЗ** тот же репозиторий ассетов развёрнут по пути `CMW_SSH_KB_REPO_PATH` (часто `/var/www/html` — задаётся в `.env`, не в git).

### Схема конвейера

| Шаг | Где | Действие |
| --- | --- | --- |
| 1. Копирование | Ваш ПК | Запись в `CMW_KB_REPO_PATH/platform/{version}/` |
| 2. `--git` | Ваш ПК | `utilities/git_sync.py` → `git add`, `commit`, `push` **в sibling-репозитории** |
| 3. `--pull` | Сервер БЗ по SSH | `utilities/ssh_pull.py` → `git pull` в `CMW_SSH_KB_REPO_PATH` |
| 4. Раздача | Продакшен | PHPKB отдаёт файлы из checkout на сервере |

HTML статей по-прежнему попадает в **БД PHPKB** через `phpkb_update_articles.py` — это отдельно от репозитория ассетов.

### Переменные `.env` (профиль `cmw`)

| Переменная | Пример | Назначение |
| --- | --- | --- |
| `CMW_KB_REPO_PATH` | `C:/Repos/kb.comindware.ru` | Локальный sibling checkout |
| `CMW_SSH_KB_REPO_PATH` | `/var/www/html` | Удалённый путь для `git pull` на сервере БЗ |
| `CMW_SSH_HOST` | (ваш хост) | SSH для `--pull` и туннеля к БД |
| `CMW_SSH_USERNAME` | (ваш пользователь) | Логин SSH |
| `CMW_SSH_PASSWORD` | (опционально) | Если не ключ/agent — **только в `.env`** |

Загрузка переменных перед ручным `git -C`:

```powershell
Get-Content .env | ForEach-Object {
  if ($_ -match '^\s*([^#][^=]+)=(.*)$') { Set-Item -Path "env:$($matches[1].Trim())" -Value $matches[2].Trim() }
}
```

```bash
set -a && source .env && set +a
```

### Изображения: полная цепочка

**Сначала:** `mkdocs build -f mkdocs_for_kb_import_ru.yml`.

**Копирование → push → pull (одной командой):**

```powershell
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git --pull
```

```bash
.venv/bin/python phpkb_copy_images.py --version v6.0 --git --pull
```

Без диалогов:

```powershell
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git --pull --no-ask
```

```bash
.venv/bin/python phpkb_copy_images.py --version v6.0 --git --pull --no-ask
```

**По шагам:**

```powershell
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0
git -C "$env:CMW_KB_REPO_PATH" status --short -- platform/v6.0
git -C "$env:CMW_KB_REPO_PATH" add platform/v6.0/
git -C "$env:CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6.0 images"
git -C "$env:CMW_KB_REPO_PATH" push
.\.venv\Scripts\python.exe utilities/ssh_pull.py
```

```bash
.venv/bin/python phpkb_copy_images.py --version v6.0
git -C "$CMW_KB_REPO_PATH" status --short -- platform/v6.0
git -C "$CMW_KB_REPO_PATH" add platform/v6.0/
git -C "$CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6.0 images"
git -C "$CMW_KB_REPO_PATH" push
.venv/bin/python utilities/ssh_pull.py
```

На ветке `platform_v5` используйте `--version v5.0`.

### LLM-бандл: полная цепочка

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896 `
  --version v6.0 --git --pull
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896 \
  --version v6.0 --git --pull
```

Если бандл изменился и в **корне** `cbap-mkdocs-ru` — два отдельных commit/push (этот репозиторий и sibling).

### Только SSH *pull* (отправка *push* уже выполнена)

```powershell
.\.venv\Scripts\python.exe utilities/ssh_pull.py
```

```bash
.venv/bin/python utilities/ssh_pull.py
.venv/bin/python utilities/ssh_pull.py --no-ask
```

Скрипт подключается по `CMW_SSH_*` и на сервере выполняет:

```bash
cd $CMW_SSH_KB_REPO_PATH && git pull
```

(путь из `.env`, не локальный `C:\Repos\…`).

### Ручной SSH на сервере БЗ

```bash
ssh <CMW_SSH_USERNAME>@<CMW_SSH_HOST>
cd /var/www/html    # или ваш CMW_SSH_KB_REPO_PATH
git pull
git log -1 --oneline
ls platform/v6.0/ | head
exit
```

Хост и путь — из `.env`; не коммитьте реальные hostname и пароли в репозиторий.

### Чего не делать

- Не `git add kb.comindware.ru/` **внутри `cbap-mkdocs-ru`** — это junction или внешний каталог.
- Не храните `CMW_KB_REPO_PATH` и SSH-секреты в статьях БЗ и не коммитьте `.env`.
- **`--git` без `--pull`** обновляет remote, но на сервере БЗ файлы могут остаться старыми, пока не выполнен `git pull`.


## Веб-скрапинг для LLM

Обход **публичных сайтов** (не PHPKB) в один очищенный Markdown на сайт. Отдельно от [платформенного RAG](#обновление-phpkb_content_rag).

| Конвейер | Источник | Результат |
| --- | --- | --- |
| Platform RAG | БД PHPKB | `kb.comindware.ru.platform_v*_for_llm_ingestion.md` |
| Веб-скрапинг | Публичный sitemap | `scraping/{site}/{site}_sanitized_{date}.md` |

Скрипты: `.agents/skills/scrape-sanitize/scripts/` (подробнее: `.agents/skills/scrape-sanitize/SKILL.md`).

### Сайты

| `--site` | Sitemap | Краулер |
| --- | --- | --- |
| `comindware_ru` | https://www.comindware.ru | `crawl4ai_ingest.py` |
| `cmwlab_com` | https://www.cmwlab.com | `crawl4ai_ingest.py` |

Удаление шаблонного текста: `patterns_comindware_ru.py`, `patterns_cmwlab_com.py`.

### Поток файлов

```
crawl4ai_ingest.py
  → .scratch/{site}_dirty_{YYYYMMDD}.md     (сырой, gitignore)
  → scraping/{site}/progress_{YYYYMMDD}.json

sanitize.py
  → scraping/{site}/sanitize_checkpoint.json
  → scraping/{site}/{site}_sanitized_{YYYYMMDD}.md
```

Для crawl и sanitize используйте **одинаковый `--date`** (по умолчанию — сегодня, `YYYYMMDD`).

### Стандартный порядок работ (*standard workflow*)

```powershell
$ss = ".agents/skills/scrape-sanitize/scripts"
```

```bash
ss=".agents/skills/scrape-sanitize/scripts"
```

**1. Краул** (нужна сеть, может занять долго):

```powershell
.\.venv\Scripts\python.exe $ss\crawl4ai_ingest.py --site comindware_ru
```

```bash
.venv/bin/python $ss/crawl4ai_ingest.py --site comindware_ru
```

**2. Очистка:**

```powershell
.\.venv\Scripts\python.exe $ss\sanitize.py --site comindware_ru --date 20260616
```

```bash
.venv/bin/python $ss/sanitize.py --site comindware_ru --date 20260616
```

**3. Проверка** `scraping/comindware_ru/comindware_ru_sanitized_20260616.md`.

**4. Коммит:**

```powershell
git add scraping/comindware_ru/
git commit -m "[#<ticket>] Refresh comindware.ru scraped LLM bundle"
git push
```

Не коммитьте `.scratch/*_dirty_*.md`.

### Продолжить или начать заново

Прерванный запуск продолжается по чекпоинтам. **С нуля:**

```powershell
.\.venv\Scripts\python.exe $ss\crawl4ai_ingest.py --site comindware_ru --fresh
.\.venv\Scripts\python.exe $ss\sanitize.py --site comindware_ru --date 20260616 --fresh
```

```bash
.venv/bin/python $ss/crawl4ai_ingest.py --site comindware_ru --fresh
.venv/bin/python $ss/sanitize.py --site comindware_ru --date 20260616 --fresh
```

| Флаг | При crawl очищает | При sanitize очищает |
| --- | --- | --- |
| `--fresh` на crawl | dirty `.md`, `progress_*.json` | — |
| `--fresh` на sanitize | — | checkpoint, sanitized output |

Повторная очистка без краула: только `sanitize.py`.

### Зависимости

В `install/requirements.txt`: `crawl4ai`, `beautifulsoup4`, `markdownify`, `tiktoken`. Ошибки: `.scratch/ralph/{site}_failures.log`.

### Устаревший скрипт

`http_bs4_ingest.py` — старый краулер; для новых запусков используйте `crawl4ai_ingest.py`.

## MkDocs serve (локальный предпросмотр)

Из корня репозитория с активированным venv (или `.venv/bin/python` / `.\.venv\Scripts\python.exe`). По умолчанию: http://127.0.0.1:8000 — сервер следит за `docs/` и перезагружает страницы при сохранении.

### Какой конфиг запускать

| Конфиг | Когда | `site_dir` |
| --- | --- | --- |
| `mkdocs.yml` | **По умолчанию** — полная RU-навигация для авторинга | `compiled_help/` |
| `mkdocs_guide_complete_ru.yml` | То же явно | (наслед.) |
| `mkdocs_guide_user_ru.yml` | Только **руководство пользователя** | (наслед.) |
| `mkdocs_guide_admin_windows_ru.yml` | Администрирование (Windows) | (наслед.) |
| `mkdocs_guide_admin_linux_ru.yml` | Администрирование (Linux) | (наслед.) |
| `mkdocs_en_local.yml` | Локальный английский preview | (наслед.) |
| `mkdocs_for_kb_import_ru.yml` | **Не serve** — только `mkdocs build` для PHPKB | `for_kb_import_ru/` |

Согласуйте конфиг с **веткой платформы** (`platform_v5` → v5 в YAML; `platform_v6` → v6).

### Типовые команды

**Полная русская справка (по умолчанию):**

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve
```

```bash
.venv/bin/python -m mkdocs serve
```

**Явно полная навигация:**

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve -f mkdocs_guide_complete_ru.yml
```

```bash
.venv/bin/python -m mkdocs serve -f mkdocs_guide_complete_ru.yml
```

**Только руководство пользователя:**

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve -f mkdocs_guide_user_ru.yml
```

```bash
.venv/bin/python -m mkdocs serve -f mkdocs_guide_user_ru.yml
```

**Английская версия:**

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve -f mkdocs_en_local.yml
```

```bash
.venv/bin/python -m mkdocs serve -f mkdocs_en_local.yml
```

**Другой хост/порт** (если 8000 занят):

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve --dev-addr 127.0.0.1:8001
```

```bash
.venv/bin/python -m mkdocs serve --dev-addr 127.0.0.1:8001
```

**Строгий режим** (ошибка при битых ссылках — перед крупной публикацией):

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve --strict
```

```bash
.venv/bin/python -m mkdocs serve --strict
```

Остановка: `Ctrl+C`. Preview использует веб-тему (`overrides/`), не HTML экспорта PHPKB (`overrides_for_kb_import/`).


## JSON-карты сопоставления

В корне репозитория (и отдельные файлы под `docs/ru/`) лежат **JSON-карты**: связь ID в БД PHPKB со стабильными локальными именами файлов или журнал миграций при клонировании. Файлы в git — коммитьте после обновления скриптами импорта или клонирования.

### Карты статей и категорий (*article map*, `--article-map`)

Используются **`phpkb_import.py`**, **`phpkb_import_for_rag.py`** и родственными скриптами. **Обязательны** — параметр `--article-map` при каждом импорте.

| Файл | Платформа | Назначение |
| --- | --- | --- |
| `.article_id_filename_map_v5.json` | v5.0 (категория `798`) | ID статьи PHPKB → stem имени файла; ID категории → slug папки в `phpkb_content*` |
| `.article_id_filename_map_v6.json` | v6.0 (категория `896`) | То же для v6 |
| `.article_id_filename_map_v4.7.json` | v4.7 | Импорт v4.7 |
| `.article_id_filename_map_v4_cmw_lab.json` | CMW Lab | `phpkb_import_cmw_lab.py` → `phpkb_content_cmw_lab/` |

Структура (упрощённо):

```json
{
  "Articles": {
    "5451": "script_keys",
    "5558": "deploy_linux"
  },
  "Categories": {
    "896": "platform_v6",
    "914": "general"
  }
}
```

**Зачем нужны:**

- Заголовки статей в PHPKB меняются; **имена файлов** при re-import должны оставаться стабильными (`5451-script_keys.md`).
- Скрипты **дополняют** карту: известные ID сохраняют stem; новым ID назначается stem и файл обновляется.
- Карты согласуют импортированные деревья с именованием в **`docs/ru/`**, если статья сначала authored в MkDocs.

**Действия оператора:**

- Передавайте карту, соответствующую `--category-id` и ветке платформы (v5 на `platform_v5`, v6 на `platform_v6`).
- После полного импорта закоммитьте карту, если скрипт добавил записи.
- Не правьте вручную без понимания связи ID ↔ stem; предпочтительнее правка `docs/ru/` и re-import.

### Карты миграции клонов (*clone mapping*, `--mapping`)

Для **`utilities/phpkb_cloning/phpkb_clone.py`** и post-clone скриптов. **Обязателен** `--mapping`.

| Файл | Назначение | Срок хранения |
| --- | --- | --- |
| `.v5mapping.json`, `.v6mapping.json`, `.v6.5mapping.json`, … | **Старый ID PHPKB → новый ID** после клона категории/статьи (миграция версии) | **Постоянные** артефакты репозитория |
| `.scratch/<purpose>_mapping.json` | Разовый клон / публикация статьи | Одноразово (gitignore) |

Карты клонов ≠ article maps: они фиксируют **перенумерацию строк БД**, а не stem файлов для импорта.

Подробнее: `.agents/skills/phpkb-cloning/SKILL.md`. **Не смешивайте** `.v6mapping.json` с картой из `.scratch/`.

### Прочий JSON в репозитории

| Расположение | Назначение |
| --- | --- |
| `docs/ru/tutorials/**/.taxonomies/*.json` | Структура учебных курсов — не PHPKB article maps |
| `scraping/*/progress_*.json`, `sanitize_checkpoint.json` | Чекпоинты веб-скрапинга |
| `for_kb_import_ru/**/comindware_default_mapping.json` | Метаданные ассетов в экспорте — не корневые article maps |


## Конфигурация MkDocs

Конфиги MkDocs в этом репозитории используют **наследование YAML** (*YAML inheritance*, ключ `INHERIT:`): дочний файл наследует родительский конфиг и переопределяет только нужные ключи. Общая база — `mkdocs_common.yml`; языковые и прикладные конфиги добавляют лишь отличия.

### Цепочка наследования (*inheritance chain*)

```
mkdocs_common.yml          ← тема, плагины, extra, PDF
    └── mkdocs_ru.yml      ← docs_dir RU, URL БЗ
            ├── mkdocs_guide_*_ru.yml
            │       └── mkdocs_guide_*_ru_pdf.yml
            ├── mkdocs_guide_complete_ru.yml
            ├── mkdocs_for_kb_import_ru.yml
            └── mkdocs_ru_local_files.yml
mkdocs.yml                 ← INHERIT: mkdocs_guide_complete_ru.yml
mkdocs_en.yml / mkdocs_en_local.yml
```

### Подход к наследованию (*YAML inheritance*)

Уровни конфигурации (от базы к листовому файлу под задачу):

1. **`mkdocs_common.yml`** — тема (Material), плагины (`search`, `macros`, `minify`, …), markdown-расширения, **`extra:` плейсхолдеры** (`productName`, `companyName`, …). Напрямую почти не запускают.

2. **`mkdocs_ru.yml`** — `INHERIT: mkdocs_common.yml`, `docs_dir: docs/ru`, `site_dir: compiled_help`, URL БЗ в `extra`, настройки PDF по умолчанию.

3. **Конфиги под задачу** — `INHERIT: mkdocs_ru.yml` (или `mkdocs_en.yml`), переопределяют только отличия:

   | Тип override | Типичные ключи | Пример |
   | --- | --- | --- |
   | Каталог вывода | `site_dir` | `for_kb_import_ru` в `mkdocs_for_kb_import_ru.yml` |
   | Базовый URL | `site_url` | `https://kb.comindware.ru/platform/v5.0/` (должен совпадать с веткой) |
   | Шаблоны темы | `theme.custom_dir` | `overrides_for_kb_import/` для PHPKB |
   | Флаги сборки | `extra.userGuide`, `extra.kbExport`, `extra.pdfOutput`, … | Каждый `mkdocs_guide_*_ru.yml` |
   | Навигация | `nav:` | Подмножество страниц (user, admin, API, …) |
   | Пост-обработка | `hooks:` | `kb_html_cleanup_hook.py` только для экспорта PHPKB |
   | Исключения | `exclude_docs:` | Не экспортировать `AGENTS.md` |

4. **PDF** — `mkdocs_guide_*_ru_pdf.yml` наследуют соответствующий guide и включают `extra.pdfOutput: true`, `plugins.with-pdf`, `site_dir: pdf/`.

5. **Точка входа** — корневой `mkdocs.yml` = `INHERIT: mkdocs_guide_complete_ru.yml`, поэтому `mkdocs serve` открывает **полную** RU-навигацию.

**Правила:**

- Общие настройки — один раз в **`mkdocs_common.yml`**; не дублируйте плагины в guide-файлах.
- Выбирайте **листовой** конфиг под задачу (`-f mkdocs_for_kb_import_ru.yml` для PHPKB, `*_pdf.yml` для PDF).
- **Булевы `extra`** управляют Jinja в статьях — [Основы Jinja](#основы-jinja).
- На **`platform_v5` / `platform_v6`** проверяйте `site_url` и `productVersion` в активной **цепочке наследования** YAML.

Примеры:

```yaml
# mkdocs_for_kb_import_ru.yml — только экспорт PHPKB
INHERIT: mkdocs_ru.yml
site_url: https://kb.comindware.ru/platform/v5.0/
site_dir: for_kb_import_ru
use_directory_urls: false
theme:
  custom_dir: overrides_for_kb_import
extra:
  kbExport: true
hooks:
  - kb_html_cleanup_hook.py
```

```yaml
# mkdocs_guide_user_ru.yml — подмножество nav + флаги
INHERIT: mkdocs_ru.yml
extra:
  userGuide: true
  completeGuide: false
nav:
  - Общие сведения: …
  - Использование системы: …
```

### Справочник конфигов

| Файл | Назначение | `site_dir` | Команда |
| --- | --- | --- | --- |
| `mkdocs.yml` | Локальный предпросмотр (полная RU-навигация) | `compiled_help` | `mkdocs serve` |
| `mkdocs_guide_complete_ru.yml` | Полная навигация для авторинга | (наслед.) | `mkdocs serve -f mkdocs_guide_complete_ru.yml` |
| `mkdocs_guide_user_ru.yml` | Руководство пользователя | (наслед.) | `mkdocs build -f mkdocs_guide_user_ru.yml` |
| `mkdocs_guide_*_ru.yml` | Другие руководства | (наслед.) | `-f mkdocs_guide_<name>_ru.yml` |
| `mkdocs_for_kb_import_ru.yml` | HTML для PHPKB | `for_kb_import_ru` | `mkdocs build -f mkdocs_for_kb_import_ru.yml` |
| `mkdocs_for_kb_import_ru_v4.7.yml` | Экспорт v4.7 | `for_kb_import_ru` | аналогично |
| `mkdocs_for_kb_import_en.yml` | Английский экспорт PHPKB | `for_kb_import_en` | аналогично |
| `mkdocs_guide_*_ru_pdf.yml` | Сборка PDF | `pdf/` | [Сборка PDF](#сборка-pdf-руководств) |
| `mkdocs_guide_*_ru_pdf_gostech.yml` | PDF ГосТех | `pdf/` | наследует `*_pdf.yml` |
| `mkdocs_en_local.yml` | Локальный EN | (наслед.) | `mkdocs serve -f mkdocs_en_local.yml` |

### Флаги руководств (`extra`)

Каждый `mkdocs_guide_*_ru.yml` задаёт булевы флаги для условий Jinja — включать или исключать фрагменты контента:

| Флаг | Руководство |
| --- | --- |
| `userGuide` | Пользовательское |
| `adminGuideWindows` / `adminGuideLinux` | Администрирование |
| `apiGuide` | API |
| `developerGuide` | Разработчик |
| `aiGuide` | ИИ |
| `completeGuide` | Полное / локальный preview |
| `tutorial` | Учебники |
| `kbExport` | Экспорт PHPKB |
| `pdfOutput` | Сборка PDF |
| `gostech` | Варианты PDF ГосТех |

Плейсхолдеры продуктов и брендов (`productName`, `companyName`, `nginxVariants`, …) — в `mkdocs_common.yml` `extra:`; можно переопределять в дочернем конфиге (например, в PDF ГосТех `nginxVariants` → «Сервис IAM Proxy»).

### Путь к сниппетам

`pymdownx.snippets` в `mkdocs_common.yml` задаёт `base_path: docs/ru/.snippets/` — переиспользуемые фрагменты (`hyperlinks_mkdocs_to_kb_map.md`, `pdfPageBreakHard.md`, …).

## Скрипты репозитория

Скрипты — в корне репозитория, если не указано иное. Запуск из корня: `.\.venv\Scripts\python.exe <script>.py` (Windows) или `.venv/bin/python <script>.py` (WSL/Linux). С активированным venv: `python <script>.py`.

Полный перечень: [`python_scripts_roster.md`](python_scripts_roster.md).

### Сборка MkDocs

| Скрипт | Назначение |
| --- | --- |
| `buildhelp.py` | Устарел — используйте `mkdocs build` (см. `.legacy/buildhelp.py`) |
| `pdf_build_guides.py` | Пакетная сборка всех стандартных PDF; лог `build_log.txt` |
| `pdf_duplicate_with_date.py` | Копии PDF из корня в `PDF_DATED_DIR` с суффиксом `YYYY.MM.DD` |
| `install/deploy_venv.py` | Создание `.venv` и установка `install/requirements.txt` |

### PHPKB: публикация и импорт

| Скрипт | Назначение |
| --- | --- |
| `phpkb_update_articles.py` | HTML → БД PHPKB |
| `phpkb_import.py` | PHPKB → `phpkb_content/` |
| `phpkb_import_for_rag.py` | PHPKB → `phpkb_content_rag/` |
| `phpkb_ingest.py` | RAG → LLM-бандл |
| `phpkb_ingest_cmw_lab.py` | Бандл CMW Lab / v4 |
| `phpkb_import_cmw_lab.py` | Импорт → `phpkb_content_cmw_lab/` |
| `phpkb_copy_images.py` | Изображения → репозиторий ассетов |
| `phpkb_replace_related_topics.py` | Связанные темы в PHPKB |
| `phpkb_update_article_ids.py` | Миграция ID статей |

### Клонирование PHPKB (`utilities/phpkb_cloning/`)

| Скрипт | Назначение |
| --- | --- |
| `phpkb_clone.py` | Клон категорий/статей в БД |
| `phpkb_clone_update_links.py` | Обновление ссылок |
| `phpkb_clone_update_mapped_ids.py` | `kbId` в `docs/ru/` и карте ссылок |
| `phpkb_clone_rollback.py` | Откат клона |

### Утилиты

| Скрипт | Назначение |
| --- | --- |
| `tools/ssh_kb_ru.py` | SSH + MySQL к PHPKB |
| `tools/text_io.py` | LF в генераторах (только импорт) |
| `utilities/git_sync.py` | Commit/push ассетов (`--git`) |
| `utilities/ssh_pull.py` | `git pull` на продакшене (`--pull`) |
| `kb_html_cleanup_hook.py` | Хук MkDocs (не CLI) |

**Веб-скрапинг:** `crawl4ai_ingest.py`, `sanitize.py` — [раздел выше](#веб-скрапинг-для-llm).

Устаревшее: `.legacy/`.

## Переопределения темы

Шаблоны темы Material переопределяются через `theme.custom_dir`. В репозитории два каталога overrides:

| Каталог | Используется | Назначение |
| --- | --- | --- |
| `overrides/` | `mkdocs_common.yml` → большинство сборок | Веб-справка: логотип, CSS, footer, meta `kbUrl` |
| `overrides_for_kb_import/` | `mkdocs_for_kb_import_ru.yml` | Экспорт PHPKB: упрощённый HTML, CSS под PHPKB |

### Ключевые файлы overrides

| Файл | Назначение |
| --- | --- |
| `overrides/main.html` | Расширяет Material `base.html`; добавляет `<meta property="kbUrl" …>` при `page.meta.kbId` |
| `overrides/partials/copyright.html` | Строка copyright в footer |
| `overrides/assets/stylesheets/extra.css` | Стили бренда для веб-справки |
| `overrides_for_kb_import/base.html` | Базовый шаблон экспорта PHPKB (без оболочки Material) |
| `overrides_for_kb_import/assets/stylesheets/extra.css` | Стили notice/admonition для PHPKB |
| `overrides_for_kb_import/partials/toc.html` | Оглавление для экспорта |

Файлы overrides используют синтаксис **Jinja2** (`{% extends %}`, `{% block %}`, `{{ config.extra… }}`). Меняйте overrides только при изменении HTML-структуры или глобальных стилей — содержимое статей остаётся в `docs/ru/`.

### Шаблоны PDF

Каталог `pdf_templates/` — шаблоны WeasyPrint для `mkdocs-with-pdf`:

| Файл | Назначение |
| --- | --- |
| `cover.html.j2` | Обложка PDF (логотип, `productName`, `productVersion`, `cover_subtitle`) |
| `styles.scss` | Стили для печати |

В `mkdocs_common.yml`: `plugins.with-pdf.custom_template_path: pdf_templates`.

## Основы Jinja

Механика сборки для статей — правила формулировок и ссылок: [`AGENTS.md`](AGENTS.md) · [Стандарты редактирования](#стандарты-редактирования-контента). MkDocs обрабатывает Markdown через Jinja2; плагин `mkdocs-macros` (`plugins.macros` в `mkdocs_common.yml`) открывает значения `config.extra` как переменные шаблона.

### Плейсхолдеры продуктов

В Markdown статей — **двойные фигурные скобки** для значений из `extra:` в `mkdocs_common.yml`:

```markdown
**{{ productName }}** позволяет настраивать шаблоны.
```

Частые плейсхолдеры: `{{ productName }}`, `{{ companyName }}`, `{{ productNameMobile }}`, `{{ nginxVariants }}`, `{{ openSearchVariants }}`.

- Без пробелов в имени: `{{ product Name }}` — ошибка.
- Имена продуктов полужирным: `**{{ productName }}**`.
- Подстановка выполняется при сборке, не в редакторе исходника.

### Условный контент

Опциональные блоки — в `{% if … %} … {% endif %}`:

```markdown
{% if pdfOutput %}
<p class="pdfEndOfBlockHack pageBreakAfter">.</p>
{% endif %}
```

```markdown
{% if adminGuideLinux %}
Шаги развёртывания для Linux…
{% endif %}
```

```markdown
{% if (not gostech) or adminGuideWindows or completeGuide or kbExport %}
Настройка IIS на Windows…
{% endif %}
```

Типичные переменные: `pdfOutput`, `kbExport`, `userGuide`, `adminGuideLinux`, `adminGuideWindows`, `apiGuide`, `developerGuide`, `completeGuide`, `gostech`.

### Подключение сниппетов

Переиспользуемые фрагменты — в `docs/ru/.snippets/`.

**Карта гиперссылок (обязательно в конце каждой статьи):**

```markdown
{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
```

Подключайте include в **конце каждой** статьи в каталоге `docs/`, чтобы при сборке разрешались все существующие и будущие ссылки вида `[текст][anchor_name]` — через **`mkdocs-autorefs`** или **карту гиперссылок**, в зависимости от контекста (см. [`AGENTS.md` → Оформление ссылок](AGENTS.md#link-formatting)):

1. **`mkdocs-autorefs`** — если целевая статья входит в **текущую сборку** (`nav:` активного YAML), формируется внутренняя перекрёстная ссылка на заголовок `{: #anchor }` (HTML/PDF).
2. **Карта гиперссылок** — URL из справочника (сторонние ресурсы, сайт БЗ, запасной вариант вне `nav`, экспорт PHPKB); условия (`userGuide`, `adminGuideLinux`, `kbExport`, …) совпадают с флагами `extra:` активного конфига.

Карта — центральный справочник **именованных якорей** (портативность, дедупликация, версионирование через `kbArticleURLPrefix`). В тексте используется один синтаксис ссылки; при сборке выбирается соответствующий механизм.

### Ссылки в статьях

| Область | Синтаксис | Где задана цель |
| --- | --- | --- |
| **Та же статья** (заголовок на этой странице) | `[текст](#anchor_name)` | `{: #anchor_name }` в этом файле |
| **Другая статья / БЗ / сторонний ресурс** | `[текст][anchor_name]` | Именованный якорь в карте гиперссылок или `autorefs` (в сборке) |

- **Внутри страницы:** только `#anchor_name` — не в карте.
- **Ссылка на другую статью:** `[текст][anchor_name]` — запись в карте и/или `autorefs`; в тексте статьи не используйте встроенные URL и не `[текст](path.md)`.

### Разрывы страниц в PDF

Жёсткий разрыв страницы в PDF:

```markdown
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
```

Сниппет срабатывает только при `pdfOutput: true`.

## Сборка PDF-руководств

Плагин `mkdocs-with-pdf` (WeasyPrint). Подробности Windows/GTK3: `.agents/skills/mkdocs-pdf-build/SKILL.md`.

### Однократная настройка GTK3 (Windows)

1. Установите GTK3: `install\gtk3-runtime-…-win64.exe` или `install\installgtk3.ps1`.
2. Переменные окружения:

```powershell
[Environment]::SetEnvironmentVariable(
  "WEASYPRINT_DLL_DIRECTORIES",
  "C:\Program Files\GTK3-Runtime Win64\bin", "User")
$gtk = "C:\Program Files\GTK3-Runtime Win64\bin"
$cur = [Environment]::GetEnvironmentVariable("PATH", "User")
[Environment]::SetEnvironmentVariable("PATH", "$gtk;$cur", "User")
```

_WSL / Linux / macOS:_ GTK3 и WeasyPrint — `.agents/skills/mkdocs-pdf-build/SKILL.md` (не установщик Windows выше).

3. Проверка:

```powershell
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
.\.venv\Scripts\python.exe -c "import weasyprint; print(weasyprint.__version__)"
```

_WSL / Linux / macOS:_ см. `.agents/skills/mkdocs-pdf-build/SKILL.md`.

### Одно PDF

```powershell
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_guide_user_ru_pdf.yml --clean
```

```bash
# После настройки GTK3/WeasyPrint — см. .agents/skills/mkdocs-pdf-build/SKILL.md
.venv/bin/python -m mkdocs build -f mkdocs_guide_user_ru_pdf.yml --clean
```

| Конфиг | PDF в корне репозитория |
| --- | --- |
| `mkdocs_guide_user_ru_pdf.yml` | `Comindware Platform 5.0. Руководство пользователя.pdf` |
| `mkdocs_guide_admin_windows_ru_pdf.yml` | Администрирование (Windows) |
| `mkdocs_guide_admin_linux_ru_pdf.yml` | Администрирование (Linux) |
| `mkdocs_guide_api_ru_pdf.yml` | API |
| `mkdocs_guide_developer_ru_pdf.yml` | Разработчик |
| `mkdocs_guide_ai_ru_pdf.yml` | ИИ |
| `mkdocs_guide_complete_ru_pdf.yml` | Полное руководство |
| `mkdocs_guide_*_ru_pdf_gostech.yml` | Варианты ГосТех |

### Пакетная сборка

```powershell
.\.venv\Scripts\python.exe pdf_build_guides.py
```

```bash
.venv/bin/python pdf_build_guides.py
```

Порядок: complete → user → developer → admin Linux → admin Windows → API. Лог: `build_log.txt`.

### PDF с датой в имени

```powershell
.\.venv\Scripts\python.exe pdf_duplicate_with_date.py
```

```bash
.venv/bin/python pdf_duplicate_with_date.py
```

Каталог из `PDF_DATED_DIR` в `.env`.

### Mermaid в PDF

WeasyPrint не выполняет JavaScript — см. [Поддержка Mermaid в PDF](#поддержка-mermaid-в-pdf).

### Устранение неполадок PDF

| Симптом | Решение |
| --- | --- |
| `OSError: cannot load library` при `import weasyprint` | GTK3 не установлен или не в `PATH` |
| PDF 0 байт / сбой при рендере | То же — проверьте переменные GTK3 в текущей сессии |
| Кириллица отображается «квадратиками» | Задайте `WEASYPRINT_DLL_DIRECTORIES` |
| `Could not find cross-reference target` | Обычно не критично; отсутствует якорь в другой статье |
| `render_js: true` | **Не работает** — используйте `mkdocs-mermaid-to-svg` + `mmdc` |

## Хуки сборки MkDocs

MkDocs поддерживает Python-модули хуков в `hooks:` YAML-конфигурации. Это отдельно от Git-хуков (следующий раздел).

### `kb_html_cleanup_hook.py`

Зарегистрирован в `mkdocs_for_kb_import_ru.yml` (и вариантах `_en`, `_v4.7`). Выполняет `on_post_page` после рендера каждой страницы — преобразует HTML для совместимости с PHPKB:

- Классы admonition Material → `notice-*` PHPKB
- Удаление лишнего `<h1>` (заголовок даёт PHPKB)
- Удаление HTML-комментариев, пустых `<p>`
- Добавление `class="mkdocs_imported_link"` к ссылкам
- Преобразование `<pre>` для отображения кода в PHPKB
- Замена `<body>` на `<div class="md-body" kb-id="…" kb-title="…">` из front matter страницы
- Исправление относительных путей изображений для хостинга ассетов PHPKB

**Когда запускается:** только при `mkdocs build -f mkdocs_for_kb_import_ru.yml` (или `_en`, `_v4.7`). Не используется для веб-предпросмотра и PDF.

`kb_html_cleanup_hook_v4.7.py` — вариант для v4.7.

## Git-хуки

В `.githooks/`. Включить один раз:

```powershell
git config core.hooksPath .githooks
```

См. `.gitconfig-hooks.md`.

| Хук | Когда | Действие |
| --- | --- | --- |
| `prepare-commit-msg` | Перед редактором сообщения | **Подсказывает** `[#XXXXX] …` в stderr по ветке или прошлым коммитам (сообщение не меняет) |
| `commit-msg` | После ввода сообщения | Предупреждение о формате (не блокирует) |
| `pre-push` | Перед *push* | Git LFS pre-push |
| `post-commit` | После коммита | Git LFS post-commit |
| `post-merge` | После *merge* | Git LFS post-merge |
| `post-checkout` | После *checkout* | Git LFS post-checkout |

Формат коммита: `[#XXXXX] Описание`. См. `.agents/skills/cmwhelp-commit/SKILL.md`.

Хуки Git LFS требуют `git-lfs` в `PATH`. Установите Git LFS или удалите LFS-хуки, если LFS не используете.

## Устранение неполадок

| Симптом | Вероятная причина | Решение |
| --- | --- | --- |
| `import mkdocs` падает | Сломан venv | `install/deploy_venv.py` или skill `python-env-setup` |
| Публикация / нет SSH | Нет `.env` или VPN | `SERVER_PROFILE`, `CMW_SSH_*`, `CMW_SQL_*` |
| `CMW_KB_REPO_PATH not set` | Неполный `.env` | Путь к checkout ассетов PHPKB |
| `phpkb_copy_images.py: --version required` | Старая команда | `--version v5.0` или `v6.0` |
| Ошибка импорта при старте | Нет `--article-map` | `.article_id_filename_map_v5.json` / `_v6.json` |
| Импорт «завис» | Норма для полной категории | Ждать `Import finished. Total articles imported:` |
| Устаревший бандл | Пропущен RAG-импорт | Сначала `phpkb_import_for_rag.py` |
| Изображения не на проде | Нет pull | `--pull` или SSH `git pull` |
| `kb-id=""` в HTML | Нет `kbId:` | Добавить `kbId:` или клонировать статью |
| PDF 0 байт / WeasyPrint | Нет GTK3 | [Сборка PDF](#сборка-pdf-руководств) |
| `{{ product Name }}` | Пробел в макросе | `{{ productName }}` |
| Виден блок Jinja в HTML PHPKB | Неверный `{% if %}` | Флаги `kbExport` / guide в конфиге |
| Material-классы в HTML PHPKB | Неверный конфиг | `mkdocs_for_kb_import_ru.yml`, не `mkdocs_ru.yml` |
| Очистка (*sanitize*): нет входного файла | Неверный `--date` | Совпадение с краулом; `.scratch/{site}_dirty_*.md` |
| Краул тормозит / таймаут | Сеть / лимиты | Повтор (*resume*); `.scratch/ralph/*_failures.log` |
| Публикация без обновления | Несовпадение `kbId:` | `kbId:` = статья в PHPKB |
| SSH: отказ в соединении | VPN / ключи | `.env`, `SERVER_PROFILE` |
| Синхронизация изображений: путь не задан | `.env` | `CMW_KB_REPO_PATH`, `CMW_SSH_*` |

## Поддержка Mermaid в PDF

WeasyPrint не выполняет JavaScript — диаграммы Mermaid нужно пререндерить в статические изображения.

### Рекомендуется: `mkdocs-mermaid-to-svg` + `mmdc`

#### Зависимости

1. **Python-пакет** (уже в `install/requirements.txt`):
   ```
   pip install mkdocs-mermaid-to-svg
   ```

2. **Node.js** (нужен для `mmdc`):
   - Установка: https://nodejs.org/ или пакетный менеджер
   - Проверка: `node --version` (проверено с v18.20.7+)

3. **Mermaid CLI** (глобальный npm-пакет):
   ```
   npm install -g @mermaid-js/mermaid-cli
   ```
   - Проверка: `mmdc --version` (проверено с 11.12.0+)

#### Конфигурация

Добавьте в YAML-конфиг MkDocs:

```yaml
plugins:
  mermaid-to-svg:
    output_dir: _mermaid_assets
  with-pdf:
    # ... существующий with-pdf
```

#### Как это работает

1. `mkdocs-mermaid-to-svg` находит блоки mermaid в markdown
2. Каждая диаграмма рендерится в SVG через `mmdc`
3. SVG сохраняются в `_mermaid_assets/`
4. Блоки mermaid заменяются на `<img>` со ссылкой на SVG
5. WeasyPrint включает SVG в итоговый PDF

### Альтернатива: `render_js: true` (не работает)

У плагина `with-pdf` есть опция `render_js: true` (Headless Chrome). **Не работает** в текущих версиях из-за бага `mkdocs-with-pdf` v0.9.3:

```
AttributeError: property 'text' of 'Tag' object has no setter
```

**Вывод:** используйте только `mkdocs-mermaid-to-svg` + `mmdc` — единственный рабочий способ Mermaid в PDF.

## Skills для агентов (справка, *agent skills*)

Полные сценарии: `.agents/skills/<name>/SKILL.md`. **ИИ-агенты:** индекс в [`AGENTS.md`](AGENTS.md) — подключайте навык (*skill*), когда его описание подходит задаче.

Люди: читайте навыки как расширенные инструкции или используйте [Стандарты редактирования](#стандарты-редактирования-контента) и [`AGENTS.md` → Перекрёстные ссылки для операторов](AGENTS.md#human-operators--readme-cross-reference) для перехода между правилами статей и сценариями.

| Задача | Навык (*skill*) |
| --- | --- |
| Правка → сборка → публикация → коммит | `kb-edit-publish` |
| RAG + LLM-бандл | `phpkb-ingestion` |
| PDF на Windows | `mkdocs-pdf-build` |
| Клон / новая статья PHPKB | `phpkb-cloning` |
| Починка venv | `python-env-setup` |
| Веб-скрапинг | `scrape-sanitize` |

Полный список: [`AGENTS.md` → Skills Reference](AGENTS.md#skills-reference).

## Удалённые репозитории Git (*remotes*)

Документация ведётся в **долгоживущих ветках платформы**. В клоне могут быть несколько remotes (набор зависит от настройки):

| Remote | Типичный URL | Назначение |
| --- | --- | --- |
| `origin` | `https://github.com/<user-or-org>/cbap-mkdocs-ru.git` | Основной fetch/push |
| `github` | `https://github.com/arterm-sedov/cbap-mkdocs-ru.git` | Личный форк (опционально) |
| `github-cmw-team` | `https://github.com/cmw-team/cbap-mkdocs-ru.git` | Репозиторий команды (опционально) |
| `gitverse` | `https://gitverse.ru/arterm-sedov/cbap-mkdocs-ru.git` | Зеркало GitVerse (опционально) |

У некоторых клонов у `origin` несколько **push URL** (GitHub + GitVerse). Проверка без раскрытия секретов:

```bash
git remote -v
git remote show origin
```

**Основные ветки:**

| Ветка | Платформа БЗ | Категория PHPKB | Примечание |
| --- | --- | --- | --- |
| `platform_v5` | v5.0 | `798` | `site_url` …/v5.0/ в YAML импорта |
| `platform_v6` | v6.0 | `896` | `site_url` …/v6.0/ |
| `master` | — | — | Интеграция / default на части remotes |
| `<YYYYMMDD>_<ticket>_<topic>` | — | — | Короткоживущие ветки от `platform_v5` или `platform_v6` |

Ветки тикетов (например `20260624_10291999_scripts_keys`) обычно сливаются в соответствующую platform-ветку через pull request.

**Не коммитьте:** `.env`, SSH-ключи, пароли, абсолютные пути вашей машины. Пути вроде `CMW_KB_REPO_PATH` — только в `.env` (gitignore).


## Ежедневная работа с Git (platform_v5 / platform_v6)

### Начало дня

```bash
git fetch --all --prune
git status
git branch -vv
```

Переключитесь на нужную platform-ветку:

```bash
# документация v6
git switch platform_v6
git pull origin platform_v6

# или v5
git switch platform_v5
git pull origin platform_v5
```

В PowerShell команды те же.

### Ветка тикета

```bash
git switch platform_v6
git pull origin platform_v6
git switch -c 20260624_10291999_scripts_keys

# … правка docs/ru/, сборка, публикация …

git add docs/ru/ for_kb_import_ru/
git commit -m "[#10291999] Обновить статью о ключах скриптов"
git push -u origin HEAD
```

Откройте PR в `platform_v6` (или `platform_v5`) — см. [GitHub CLI](#github-cli-gh).

### После слияния (*merge*) — обновить локальную ветку

```bash
git switch platform_v6
git pull origin platform_v6
```

### Отправка (*push*) в team-remote (если настроен)

```bash
git push origin platform_v6
git push github-cmw-team platform_v6
```

Используйте только remotes из вашего `git remote`.


## Перенос коммитов и слияние между версиями платформы

*Git: **cherry-pick** — перенос отдельных коммитов; **merge** — слияние целой ветки.*

Правила также в [`AGENTS.md`](AGENTS.md).

**Разделение коммитов:** на одной ветке платформы — **отдельные коммиты** для (1) **`docs/ru/`**, (2) **`for_kb_import_ru/`**, (3) **`phpkb_content/`**, (4) **`phpkb_content_rag/`**, (5) **`kb.comindware.ru.platform_v*_for_llm_ingestion.md`** — не объединяйте 3–5 в один коммит — чтобы при кросс-версионном *cherry-pick* можно было взять только коммиты со статьями и пересобрать остальное на целевой ветке.

### Перенос коммитов и пересборка (*cherry-pick vs rebuild*)

Не каждое дерево в git одинаково переносится между `platform_v5` и `platform_v6`.

| Путь | Перенос (*cherry-pick*) между ветками? | Почему | На целевой ветке |
| --- | --- | --- | --- |
| `docs/ru/` | **Да** (в обе стороны) | Исходный Markdown — исправьте `kbId:` и карту ссылок на v5 | Проверьте diff; восстановите v5 `kbId:` |
| `for_kb_import_ru/` | **Нет** | HTML-экспорт ветки (`kb-id`, `site_url`, тема) | `mkdocs build -f mkdocs_for_kb_import_ru.yml`, commit |
| `phpkb_content/798-platform_v5/`, `phpkb_content_rag/798-platform_v5/`, `kb.comindware.ru.platform_v5_for_llm_ingestion.md` | **Да — только v5 → v6** | Снимок v5 + пакет LLM v5, зеркало на `platform_v6` | На v6 обычно без действий |
| `phpkb_content/896-platform_v6/`, `phpkb_content_rag/896-platform_v6/`, `kb.comindware.ru.platform_v6_for_llm_ingestion.md` | **Нет — никогда на v5** | v6 `kbId` не должны попадать на `platform_v5` | Повторный импорт (*re-import*) только на `platform_v6` |
| `phpkb_content_cmw_lab/` | **Да** (Lab / v4; вне правила v5↔v6) | Отдельное дерево CMW Lab | `phpkb_import_cmw_lab.py` при изменении БД |
| Деревья **текущей** версии на своей ветке (`798-*` на v5, `896-*` на v6) | **Нет** (кросс-версия) | Привязаны к ID БД этой ветки | `phpkb_import*.py` на этой ветке |

**Кратко:** *cherry-pick* **`docs/ru/`** в обе стороны (исправьте v5 `kbId:`); *cherry-pick* **v5-деревья + пакет LLM v5 только на `platform_v6`**; **никогда** v6-артефакты импорта на v5; **`for_kb_import_ru/` не переносят**; **пересоберите** `phpkb_content*` текущей версии локально на каждой ветке.

После *cherry-pick* статей — пересборка экспорта:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
git add for_kb_import_ru/
git commit -m "[#<ticket>] Rebuild PHPKB export after cherry-pick"
```

```bash
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
git add for_kb_import_ru/
git commit -m "[#<ticket>] Rebuild PHPKB export after cherry-pick"
```

### Правила безопасности

**Статьи (`docs/ru/`) — в обе стороны:**

- **Не переносите v6 `kbId:` в v5.** Восстановление: `git show platform_v5:docs/ru/<path>.md`
- **Держите `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` версии целевой ветки** — v6 ID ломают v5-ссылки.
- **Перенос (*cherry-pick*) небезопасен при смене `kbId` или новой статье** — проверяйте после каждого кросс-версионного переноса.

**HTML-экспорт — ни в одну сторону:**

- **`site_url` в `mkdocs_for_kb_import_ru.yml`** — `v5.0/` или `v6.0/` по целевой ветке.
- **Не переносите (*cherry-pick*) `for_kb_import_ru/`** — пересборка: `mkdocs build -f mkdocs_for_kb_import_ru.yml` на целевой ветке.

**Деревья импорта и пакеты LLM — асимметрично (только v5 → v6):**

- **На `platform_v6`:** *cherry-pick* коммитов с `phpkb_content/798-platform_v5/`, `phpkb_content_rag/798-platform_v5/` и/или `kb.comindware.ru.platform_v5_for_llm_ingestion.md`.
- **На `platform_v5`:** **никогда** v6-деревья импорта и `kb.comindware.ru.platform_v6_for_llm_ingestion.md` — повторный импорт (*re-import*) на `platform_v6`.
- **На любой ветке:** пересоберите **текущую** версию деревьев (`798-*` на v5, `896-*` на v6) локально; не переносите (*cherry-pick*) их между версиями.

**Документация и навыки — в обе стороны:**

- **Безопасно:** `.agents/skills/*`, `AGENTS.md`, `discovery_log.md`, `readme.md`, `readme-ru.md`.
- Избегайте смены `toc_depth` без необходимости.

### Перенос одного коммита (*cherry-pick*, пример v6 → v5)

```bash
git switch platform_v5
git pull origin platform_v5
git log platform_v6 --oneline -5
git cherry-pick <commit-sha>
```

Пустой перенос (*cherry-pick*, уже применено):

```bash
git cherry-pick --skip
```

При конфликтах — исправить, затем:

```bash
git add <resolved-files>
git cherry-pick --continue
```

Отмена:

```bash
git cherry-pick --abort
```

### Восстановить v5 `kbId:` после неудачного *cherry-pick*

```bash
git show platform_v5:docs/ru/administration/deploy/script_keys.md > .scratch/kbId-restore.md
# Скопируйте строку kbId: из .scratch/kbId-restore.md в рабочий файл, затем:
git add docs/ru/administration/deploy/script_keys.md
git commit -m "[#<ticket>] Восстановить v5 kbId после cherry-pick"
```

Или весь файл с ветки v5 (перезапишет локальные правки в этом файле):

```bash
git restore --source=platform_v5 -- docs/ru/administration/deploy/script_keys.md
```

### Слияние platform-веток (*merge*, реже)

Только по явному плану — например влить `platform_v6` в `platform_v5`:

```bash
git switch platform_v5
git pull origin platform_v5
git merge origin/platform_v6
# разрешить конфликты; проверить kbId, карту ссылок, site_url
git commit
git push origin platform_v5
```

Для переноса правок документации предпочтительнее **перенос отдельных коммитов (*cherry-pick*)**, а не полное слияние (*merge*).

### Убрать плохой коммит с конца ветки

```bash
git rebase --onto <good-commit> <bad-commit> HEAD
```

### Пустой cherry-pick

Если коммит уже применён на целевой ветке:

```bash
git cherry-pick --skip
```


## GitHub CLI (`gh`)

Установка: https://cli.github.com/ — один раз `gh auth login` на машине. Токены и пароли в репозиторий не попадают.

### Статус и репозиторий

```bash
gh auth status
gh repo view
gh repo view --web
```

### Pull requests

```bash
gh pr list
gh pr list --base platform_v6
gh pr view 123
gh pr view 123 --web
gh pr checks 123
gh pr checkout 123
```

Создать PR после push ветки тикета:

```bash
git push -u origin HEAD
gh pr create --base platform_v6 --title "[#10291999] Обновить статью о ключах скриптов" --body "## Summary
- Обновлена статья о ключах скриптов

## Test plan
- [ ] mkdocs serve
- [ ] mkdocs build -f mkdocs_for_kb_import_ru.yml
- [ ] Публикация в PHPKB"
```

### Issues и CI

```bash
gh issue list
gh issue view 10291999
gh run list --limit 5
gh run view <run-id> --log-failed
```

### PR из форка в team-репозиторий

```bash
gh pr create --repo cmw-team/cbap-mkdocs-ru --base platform_v6 --head <your-user>:<branch>
```


## Настройка навигации

При включённом awesome-pages можно ограничить папки в `mkdocs.yml`:

```
nav:
  - ... | administration/**
  - ... | using_the_system/**
```

## Каталог `.scratch/`

Общее место для временных и одноразовых файлов: вывод скриптов, отладочные логи, извлечённые данные, черновые карты клонирования и прочие транзиентные артефакты.

- Содержимое **в gitignore** — в Git отслеживается только `.gitkeep`.
- Используйте для одноразовых скриптов, результатов анализа и данных, которые не должны попадать в репозиторий.
- Не ссылайтесь на файлы из `.scratch/` в документации и продакшен-коде.
- Агенты: все временные выходы — в `.scratch/` (см. [`AGENTS.md`](AGENTS.md)).

## Самоэволюция (*self-evolution*)

После нетривиальных задач фиксируйте находки по [`AGENTS.md`](AGENTS.md) и `.agents/skills/self-evolution/SKILL.md`.

## Устаревшие файлы

Устаревшие скрипты и конфиги архивированы в `.legacy/`. В текущих процессах не используются.
