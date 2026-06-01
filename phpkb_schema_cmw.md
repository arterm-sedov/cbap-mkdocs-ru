# PHPKB Database Schema: CMW

Generated: 2026-05-22 16:25:12
Profile: `cmw`
Database: `phpkbv9`
Tables: 39
Columns: 303
Indexes: 110
Foreign keys: 0

## Tables

| Table | Type | Engine | Rows | Collation | Comment |
|---|---|---|---:|---|---|
| `phpkb_api_keys` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_api_log` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_article_collaboration` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_article_feedback` | BASE TABLE | MyISAM | 1362 | utf8mb3_general_ci |  |
| `phpkb_article_versions` | BASE TABLE | MyISAM | 13354 | utf8mb3_general_ci |  |
| `phpkb_article_visits` | BASE TABLE | MyISAM | 1744297 | latin1_swedish_ci |  |
| `phpkb_articles` | BASE TABLE | MyISAM | 3031 | utf8mb3_general_ci |  |
| `phpkb_attachments` | BASE TABLE | MyISAM | 181 | utf8mb3_general_ci |  |
| `phpkb_authors` | BASE TABLE | MyISAM | 147 | utf8mb3_general_ci |  |
| `phpkb_autosave` | BASE TABLE | MyISAM | 95 | utf8mb3_general_ci |  |
| `phpkb_backups` | BASE TABLE | MyISAM | 7 | utf8mb3_general_ci |  |
| `phpkb_categories` | BASE TABLE | MyISAM | 604 | utf8mb3_general_ci |  |
| `phpkb_comments` | BASE TABLE | MyISAM | 16 | utf8mb3_general_ci |  |
| `phpkb_custom_data` | BASE TABLE | MyISAM | 117 | utf8mb3_general_ci |  |
| `phpkb_custom_fields` | BASE TABLE | MyISAM | 3 | utf8mb3_general_ci |  |
| `phpkb_departments` | BASE TABLE | MyISAM | 1 | utf8mb3_general_ci |  |
| `phpkb_event_log` | BASE TABLE | MyISAM | 8648791 | utf8mb3_general_ci |  |
| `phpkb_favorites` | BASE TABLE | MyISAM | 6 | latin1_swedish_ci |  |
| `phpkb_files` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_folders` | BASE TABLE | MyISAM | 1 | utf8mb3_general_ci |  |
| `phpkb_glossary` | BASE TABLE | MyISAM | 67 | utf8mb3_general_ci |  |
| `phpkb_groups` | BASE TABLE | MyISAM | 15 | utf8mb3_general_ci |  |
| `phpkb_groups_categories` | BASE TABLE | MyISAM | 101 | latin1_swedish_ci |  |
| `phpkb_groups_relations` | BASE TABLE | MyISAM | 260 | latin1_swedish_ci |  |
| `phpkb_languages` | BASE TABLE | MyISAM | 3 | utf8mb3_general_ci |  |
| `phpkb_login_attempts` | BASE TABLE | MyISAM | 647 | latin1_swedish_ci |  |
| `phpkb_login_history` | BASE TABLE | MyISAM | 4480 | utf8mb3_general_ci |  |
| `phpkb_news` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_pending_articles` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_ratings` | BASE TABLE | MyISAM | 4 | latin1_swedish_ci |  |
| `phpkb_referrers` | BASE TABLE | MyISAM | 314739 | utf8mb3_general_ci |  |
| `phpkb_relations` | BASE TABLE | MyISAM | 3953 | latin1_swedish_ci |  |
| `phpkb_saved_searches` | BASE TABLE | MyISAM | 25502 | utf8mb3_general_ci |  |
| `phpkb_subscribers` | BASE TABLE | MyISAM | 1 | utf8mb3_general_ci |  |
| `phpkb_templates` | BASE TABLE | MyISAM | 12 | utf8mb3_general_ci |  |
| `phpkb_ticket_replies` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_tickets` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_translation_assignments` | BASE TABLE | MyISAM | 0 | utf8mb3_general_ci |  |
| `phpkb_user_settings` | BASE TABLE | InnoDB | 0 | utf8mb3_general_ci |  |

## `phpkb_api_keys`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `key_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `created_on` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 3 | `key_value` | `varchar(100)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `key_md5` | `varchar(50)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `key_status` | `enum('active','inactive')` | NO | `active` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `PRIMARY` | Yes | 1 | `key_id` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_api_log`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `log_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `api_module` | `varchar(30)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `ip` | `varchar(40)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `api_result` | `enum('success','failure')` | NO | `success` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `api_input` | `text` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `api_output` | `longtext` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `api_datetime` | `datetime` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `PRIMARY` | Yes | 1 | `log_id` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_article_collaboration`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `collaboration_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `collaborated_by` | `int unsigned` | NO | `NULL` |  |  |  |  |  |
| 4 | `collaboration` | `text` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `collaborated_on` | `datetime` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 0 |  |
| `collaboration` | No | 1 | `collaboration` | FULLTEXT |  | 0 |  |
| `PRIMARY` | Yes | 1 | `collaboration_id` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_article_feedback`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `1362`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `feedback_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `0` | MUL |  |  |  |  |
| 3 | `user_id` | `int unsigned` | NO | `0` | MUL |  |  |  |  |
| 4 | `ip_address` | `varchar(60)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `feedback` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `reason` | `text` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `email` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `feedback_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 1362 |  |
| `PRIMARY` | Yes | 1 | `feedback_id` | BTREE |  | 1362 |  |
| `user_id` | No | 1 | `user_id` | BTREE |  | 28 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_article_versions`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `13354`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `version_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `article_title` | `varchar(250)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `article_content` | `longtext` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `article_keywords` | `varchar(250)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `article_metadesc` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `version_saved_on` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 8 | `version_saved_by` | `int unsigned` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 2225 |  |
| `content` | No | 1 | `article_content` | FULLTEXT |  | 13354 |  |
| `keywords` | No | 1 | `article_keywords` | FULLTEXT |  | 494 |  |
| `mixed_tck` | No | 1 | `article_title` | FULLTEXT |  | 13354 |  |
| `mixed_tck` | No | 2 | `article_content` | FULLTEXT |  | 13354 |  |
| `mixed_tck` | No | 3 | `article_keywords` | FULLTEXT |  | 13354 |  |
| `PRIMARY` | Yes | 1 | `version_id` | BTREE |  | 13354 |  |
| `title` | No | 1 | `article_title` | FULLTEXT |  | 2670 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_article_visits`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `1744297`; Collation: `latin1_swedish_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `visit_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `article_hits` | `int unsigned` | NO | `NULL` |  |  |  |  |  |
| 4 | `visit_date` | `date` | NO | `NULL` |  |  |  |  |  |
| 5 | `ip_address` | `varchar(40)` | NO | `` |  |  | latin1 | latin1_swedish_ci |  |
| 6 | `country_code` | `varchar(10)` | NO | `` |  |  | latin1 | latin1_swedish_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 2850 |  |
| `PRIMARY` | Yes | 1 | `visit_id` | BTREE |  | 1744297 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_articles`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `3031`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `article_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `unlisted` | `tinyint(1)` | YES | `0` |  |  |  |  |  |
| 3 | `author_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 4 | `article_title` | `varchar(250)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `article_content` | `longtext` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `article_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 7 | `article_status` | `enum('approved','disapproved','draft','featured','pending','pending-deleted','approved-deleted','featured-deleted','disapproved-deleted')` | NO | `pending` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `article_show` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 9 | `article_last_updation` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 10 | `article_keywords` | `varchar(250)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 11 | `article_metadesc` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 12 | `article_expiry_date` | `date` | YES | `NULL` |  |  |  |  |  |
| 13 | `article_email_count` | `int` | YES | `0` |  |  |  |  |  |
| 14 | `article_print_count` | `int` | YES | `0` |  |  |  |  |  |
| 15 | `article_publish_date` | `date` | NO | `NULL` |  |  |  |  |  |
| 16 | `article_review_date` | `date` | YES | `NULL` |  |  |  |  |  |
| 17 | `article_comments_allow` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 18 | `article_ratings_allow` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 19 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |
| 20 | `article_hits` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 21 | `locked_by` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 22 | `lock_expiry_time` | `datetime` | YES | `NULL` |  |  |  |  |  |
| 23 | `last_updated_by` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 24 | `article_rej_reason` | `varchar(800)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 25 | `article_protected` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 26 | `base_article_id` | `int unsigned` | NO | `0` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `author_id` | No | 1 | `author_id` | BTREE |  | 5 |  |
| `content` | No | 1 | `article_content` | FULLTEXT |  | 1 |  |
| `keywords` | No | 1 | `article_keywords` | FULLTEXT |  | 1 |  |
| `language_id` | No | 1 | `language_id` | BTREE |  | 3 |  |
| `mixed_tck` | No | 1 | `article_title` | FULLTEXT |  | 1 |  |
| `mixed_tck` | No | 2 | `article_content` | FULLTEXT |  | 1 |  |
| `mixed_tck` | No | 3 | `article_keywords` | FULLTEXT |  | 1 |  |
| `PRIMARY` | Yes | 1 | `article_id` | BTREE |  | 3031 |  |
| `title` | No | 1 | `article_title` | FULLTEXT |  | 1 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_attachments`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `181`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `attachment_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `file_guid` | `varchar(45)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `file_name` | `varchar(250)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `file_type` | `varchar(10)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `file_views` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 7 | `file_status` | `enum('pending','approved')` | NO | `approved` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 90 |  |
| `PRIMARY` | Yes | 1 | `attachment_id` | BTREE |  | 181 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_authors`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `147`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `author_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `author_name` | `varchar(60)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `author_status` | `enum('active','inactive')` | NO | `inactive` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `author_username` | `varchar(100)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `author_password` | `varchar(40)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `author_email` | `varchar(100)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `author_level` | `enum('Superuser','Editor','Writer','Writer-Trusted','Translator','Member')` | NO | `Member` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `author_flag` | `int` | NO | `0` |  |  |  |  |  |
| 9 | `author_signup_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 10 | `author_last_login` | `datetime` | YES | `NULL` |  |  |  |  |  |
| 11 | `author_forgot_password` | `varchar(20)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 12 | `author_forgot_password_token` | `varchar(40)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 13 | `author_login_session` | `varchar(40)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 14 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `author_email` | No | 1 | `author_email` | BTREE |  | 147 |  |
| `author_username` | No | 1 | `author_username` | BTREE |  | 147 |  |
| `language_id` | No | 1 | `language_id` | BTREE |  | 2 |  |
| `PRIMARY` | Yes | 1 | `author_id` | BTREE |  | 147 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_autosave`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `95`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `autosaved_draft_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `draft_type` | `enum('article','news')` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `draft_title` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `draft_content` | `longtext` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `draft_datetime` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 6 | `draft_reference_id` | `int unsigned` | NO | `NULL` |  |  |  |  |  |
| 7 | `author_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 8 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `author_id` | No | 1 | `author_id` | BTREE |  | 3 |  |
| `language_id` | No | 1 | `language_id` | BTREE |  | 2 |  |
| `PRIMARY` | Yes | 1 | `autosaved_draft_id` | BTREE |  | 95 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_backups`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `7`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `backup_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `file_name` | `varchar(120)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `backup_type` | `varchar(10)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `creation_date` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 5 | `created_by` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `created_by` | No | 1 | `created_by` | BTREE |  | 1 |  |
| `PRIMARY` | Yes | 1 | `backup_id` | BTREE |  | 7 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_categories`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `604`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `category_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `category_name` | `varchar(100)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `category_description` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `parent_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 5 | `category_date` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 6 | `category_status` | `enum('public','private')` | NO | `public` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `category_hits` | `int` | YES | `0` |  |  |  |  |  |
| 8 | `category_show` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 9 | `category_priority` | `int unsigned` | NO | `NULL` |  |  |  |  |  |
| 10 | `category_icon` | `varchar(60)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 11 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |
| 12 | `is_product_cat` | `tinyint unsigned` | NO | `0` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `category_name` | No | 1 | `category_name` | BTREE |  | 604 |  |
| `language_id` | No | 1 | `language_id` | BTREE |  | 3 |  |
| `parent_id` | No | 1 | `parent_id` | BTREE |  | 201 |  |
| `PRIMARY` | Yes | 1 | `category_id` | BTREE |  | 604 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_comments`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `16`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `comment_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `person_name` | `varchar(60)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `person_email` | `varchar(100)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `comment` | `text` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `comment_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 7 | `comment_status` | `enum('approved','pending')` | NO | `pending` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 16 |  |
| `PRIMARY` | Yes | 1 | `comment_id` | BTREE |  | 16 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_custom_data`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `117`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `data_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `field_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 4 | `field_data` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 117 |  |
| `field_id` | No | 1 | `field_id` | BTREE |  | 2 |  |
| `PRIMARY` | Yes | 1 | `data_id` | BTREE |  | 117 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_custom_fields`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `3`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `field_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `field_name` | `varchar(60)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `field_required` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `field_type` | `enum('checkbox','dropdown','text','url','date','date-time')` | NO | `text` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `field_options` | `text` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |
| 7 | `field_status` | `enum('internal','external')` | NO | `external` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `language_id` | No | 1 | `language_id` | BTREE |  | 1 |  |
| `PRIMARY` | Yes | 1 | `field_id` | BTREE |  | 3 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_departments`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `1`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `department_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `department_name` | `varchar(100)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `department_show` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `department_type` | `enum('default','normal')` | NO | `normal` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `language_id` | `int unsigned` | NO | `1` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `PRIMARY` | Yes | 1 | `department_id` | BTREE |  | 1 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_event_log`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `8648791`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `event_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `event_area` | `varchar(10)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `item_id` | `int unsigned` | NO | `NULL` |  |  |  |  |  |
| 4 | `event_datetime` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 5 | `user_id` | `int unsigned` | NO | `0` | MUL |  |  |  |  |
| 6 | `user_ip` | `varchar(40)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `event_section` | `varchar(40)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `event_subsection` | `varchar(25)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 9 | `additional_id` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 10 | `event_action` | `varchar(25)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 11 | `event_details` | `text` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 12 | `language_id` | `int unsigned` | NO | `0` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `PRIMARY` | Yes | 1 | `event_id` | BTREE |  | 8648791 |  |
| `user_id` | No | 1 | `user_id` | BTREE |  | 164 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_favorites`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `6`; Collation: `latin1_swedish_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `favorite_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `member_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 4 | `favorite_date` | `datetime` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 6 |  |
| `member_id` | No | 1 | `member_id` | BTREE |  | 6 |  |
| `PRIMARY` | Yes | 1 | `favorite_id` | BTREE |  | 6 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_files`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `file_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `file_name` | `varchar(150)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `file_guid` | `varchar(45)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `file_caption` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `folder_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 6 | `file_datetime` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 7 | `file_type` | `varchar(10)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `download_count` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 9 | `file_status` | `enum('active','inactive')` | NO | `active` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 10 | `file_added_by` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 11 | `file_size` | `bigint unsigned` | NO | `0` |  |  |  |  |  |
| 12 | `quick_access` | `enum('no','yes')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 13 | `language_id` | `int unsigned` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `folder_id` | No | 1 | `folder_id` | BTREE |  | 0 |  |
| `PRIMARY` | Yes | 1 | `file_id` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_folders`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `1`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `folder_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `folder_name` | `varchar(100)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `parent_id` | `int unsigned` | NO | `NULL` |  |  |  |  |  |
| 4 | `folder_status` | `enum('public','private')` | NO | `public` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `folder_show` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `language_id` | `int unsigned` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `folder_name` | No | 1 | `folder_name` | BTREE |  | 1 |  |
| `PRIMARY` | Yes | 1 | `folder_id` | BTREE |  | 1 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_glossary`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `67`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `glossary_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `glossary_term` | `varchar(100)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `glossary_content` | `text` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `glossary_show` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `language_id` | No | 1 | `language_id` | BTREE |  | 3 |  |
| `PRIMARY` | Yes | 1 | `glossary_id` | BTREE |  | 67 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_groups`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `15`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `group_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `group_name` | `varchar(60)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `creation_date` | `date` | NO | `NULL` |  |  |  |  |  |
| 4 | `group_type` | `varchar(15)` | NO | `frontend` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `PRIMARY` | Yes | 1 | `group_id` | BTREE |  | 15 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_groups_categories`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `101`; Collation: `latin1_swedish_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `group_category_relation_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `group_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `category_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `category_id` | No | 1 | `category_id` | BTREE |  | 101 |  |
| `group_id` | No | 1 | `group_id` | BTREE |  | 12 |  |
| `PRIMARY` | Yes | 1 | `group_category_relation_id` | BTREE |  | 101 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_groups_relations`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `260`; Collation: `latin1_swedish_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `group_member_relation_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `group_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `member_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `group_id` | No | 1 | `group_id` | BTREE |  | 7 |  |
| `member_id` | No | 1 | `member_id` | BTREE |  | 130 |  |
| `PRIMARY` | Yes | 1 | `group_member_relation_id` | BTREE |  | 260 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_languages`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `3`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `language_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `language_name` | `varchar(25)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `language_title` | `varchar(100)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `language_code` | `varchar(10)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `file_name` | `varchar(10)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `set_default` | `int` | NO | `NULL` |  |  |  |  |  |
| 7 | `visible` | `enum('True','False')` | NO | `False` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `text_direction` | `varchar(20)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 9 | `language_last_updation` | `datetime` | YES | `NULL` |  |  |  |  |  |
| 10 | `author_id` | `int unsigned` | NO | `0` | MUL |  |  |  |  |
| 11 | `base_language` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `author_id` | No | 1 | `author_id` | BTREE |  | 1 |  |
| `PRIMARY` | Yes | 1 | `language_id` | BTREE |  | 3 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_login_attempts`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `647`; Collation: `latin1_swedish_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `attempt_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `author_username` | `varchar(150)` | YES | `NULL` |  |  | latin1 | latin1_swedish_ci |  |
| 3 | `machine_IP` | `varchar(50)` | NO | `NULL` |  |  | latin1 | latin1_swedish_ci |  |
| 4 | `attempt_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 5 | `attempt_count` | `int` | YES | `0` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `PRIMARY` | Yes | 1 | `attempt_id` | BTREE |  | 647 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_login_history`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `4480`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `login_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `user_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `ip_address` | `varchar(100)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `last_login` | `datetime` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `PRIMARY` | Yes | 1 | `login_id` | BTREE |  | 4480 |  |
| `user_id` | No | 1 | `user_id` | BTREE |  | 149 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_news`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `news_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `author_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `news_title` | `varchar(250)` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `news_content` | `longtext` | NO | `NULL` | MUL |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `news_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 6 | `news_last_updation` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 7 | `news_show` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `news_hits` | `int` | YES | `0` |  |  |  |  |  |
| 9 | `news_expiry_date` | `date` | YES | `NULL` |  |  |  |  |  |
| 10 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `author_id` | No | 1 | `author_id` | BTREE |  | 0 |  |
| `content` | No | 1 | `news_content` | FULLTEXT |  | 0 |  |
| `language_id` | No | 1 | `language_id` | BTREE |  | 0 |  |
| `mixed_tc` | No | 1 | `news_title` | FULLTEXT |  | 0 |  |
| `mixed_tc` | No | 2 | `news_content` | FULLTEXT |  | 0 |  |
| `PRIMARY` | Yes | 1 | `news_id` | BTREE |  | 0 |  |
| `title` | No | 1 | `news_title` | FULLTEXT |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_pending_articles`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `pending_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `author_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 4 | `article_title` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `article_content` | `longtext` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `article_keywords` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `article_metadesc` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `article_categories` | `varchar(500)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 9 | `article_status` | `varchar(100)` | NO | `pending` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 10 | `article_show` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 11 | `article_last_updation` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 12 | `article_publish_date` | `date` | NO | `NULL` |  |  |  |  |  |
| 13 | `article_review_date` | `date` | YES | `NULL` |  |  |  |  |  |
| 14 | `article_expiry_date` | `date` | YES | `NULL` |  |  |  |  |  |
| 15 | `article_print_count` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 16 | `article_comments_allow` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 17 | `article_ratings_allow` | `enum('yes','no')` | NO | `yes` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 18 | `article_protected` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 19 | `article_hits` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 20 | `article_rej_reason` | `varchar(800)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 21 | `saved_on` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 22 | `saved_by` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 23 | `language_id` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 24 | `base_article_id` | `int unsigned` | NO | `0` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 0 |  |
| `author_id` | No | 1 | `author_id` | BTREE |  | 0 |  |
| `base_article_id` | No | 1 | `base_article_id` | BTREE |  | 0 |  |
| `PRIMARY` | Yes | 1 | `pending_id` | BTREE |  | 0 |  |
| `saved_by` | No | 1 | `saved_by` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_ratings`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `4`; Collation: `latin1_swedish_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `rating_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `0` | MUL |  |  |  |  |
| 3 | `article_rating` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 4 | `machine_IP` | `varchar(50)` | NO | `NULL` |  |  | latin1 | latin1_swedish_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 4 |  |
| `PRIMARY` | Yes | 1 | `rating_id` | BTREE |  | 4 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_referrers`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `314739`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `referrer_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `referrer` | `varchar(20)` | NO | `other` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `referrer_url` | `text` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `referrer_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 5 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 2264 |  |
| `PRIMARY` | Yes | 1 | `referrer_id` | BTREE |  | 314739 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_relations`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `3953`; Collation: `latin1_swedish_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `relation_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `article_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `category_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 4 | `article_priority` | `int unsigned` | NO | `0` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `article_id` | No | 1 | `article_id` | BTREE |  | 3953 |  |
| `category_id` | No | 1 | `category_id` | BTREE |  | 658 |  |
| `PRIMARY` | Yes | 1 | `relation_id` | BTREE |  | 3953 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_saved_searches`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `25502`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `search_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `search_keyword` | `varchar(200)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `search_count` | `int` | YES | `0` |  |  |  |  |  |
| 4 | `search_results` | `int` | YES | `0` |  |  |  |  |  |
| 5 | `search_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 6 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `language_id` | No | 1 | `language_id` | BTREE |  | 3 |  |
| `PRIMARY` | Yes | 1 | `search_id` | BTREE |  | 25502 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_subscribers`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `1`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `subscriber_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `item_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `subscriber_name` | `varchar(60)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `subscriber_email` | `varchar(75)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `subscription_key` | `varchar(20)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `subscription_date` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 7 | `subscription_status` | `enum('active','inactive')` | NO | `inactive` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `subscription_type` | `enum('article','category','knowledgebase')` | NO | `knowledgebase` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 9 | `user_id` | `int unsigned` | NO | `0` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `item_id` | No | 1 | `item_id` | BTREE |  | 1 |  |
| `PRIMARY` | Yes | 1 | `subscriber_id` | BTREE |  | 1 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_templates`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `12`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `template_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `author_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `template_title` | `varchar(250)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `template_content` | `longtext` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `template_date_time` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 6 | `template_last_updation` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 7 | `template_status` | `enum('active','inactive')` | NO | `active` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `template_default` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 9 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `author_id` | No | 1 | `author_id` | BTREE |  | 3 |  |
| `language_id` | No | 1 | `language_id` | BTREE |  | 3 |  |
| `PRIMARY` | Yes | 1 | `template_id` | BTREE |  | 12 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_ticket_replies`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `reply_id` | `int` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `ticket_id` | `int` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `reply_datetime` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 4 | `member_id` | `int` | NO | `NULL` | MUL |  |  |  |  |
| 5 | `content` | `text` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `reply_read` | `enum('yes','no')` | NO | `no` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `replier_type` | `enum('Admin','Member')` | NO | `Member` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `member_id` | No | 1 | `member_id` | BTREE |  | 0 |  |
| `PRIMARY` | Yes | 1 | `reply_id` | BTREE |  | 0 |  |
| `ticket_id` | No | 1 | `ticket_id` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_tickets`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `ticket_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `ticket_status` | `enum('open','closed')` | NO | `open` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `contact_name` | `varchar(60)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `contact_email` | `varchar(75)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 5 | `ticket_subject` | `varchar(100)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 6 | `ticket_content` | `text` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 7 | `ticket_priority` | `enum('Low','Medium','High','Urgent')` | NO | `Low` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 8 | `ticket_date` | `datetime` | NO | `NULL` |  |  |  |  |  |
| 9 | `member_id` | `int unsigned` | NO | `0` | MUL |  |  |  |  |
| 10 | `ip_address` | `varchar(100)` | YES | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 11 | `language_id` | `int unsigned` | NO | `1` | MUL |  |  |  |  |
| 12 | `department_id` | `int unsigned` | NO | `0` |  |  |  |  |  |
| 13 | `attachment` | `varchar(250)` | NO | `` |  |  | utf8mb3 | utf8mb3_general_ci |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `language_id` | No | 1 | `language_id` | BTREE |  | 0 |  |
| `member_id` | No | 1 | `member_id` | BTREE |  | 0 |  |
| `PRIMARY` | Yes | 1 | `ticket_id` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_translation_assignments`

Type: `BASE TABLE`; Engine: `MyISAM`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `assignment_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `language_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 3 | `author_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |
| 4 | `assignment_date` | `datetime` | NO | `NULL` |  |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `author_id` | No | 1 | `author_id` | BTREE |  | 0 |  |
| `language_id` | No | 1 | `language_id` | BTREE |  | 0 |  |
| `PRIMARY` | Yes | 1 | `assignment_id` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |

## `phpkb_user_settings`

Type: `BASE TABLE`; Engine: `InnoDB`; Rows estimate: `0`; Collation: `utf8mb3_general_ci`

### Columns

| # | Column | Type | Null | Default | Key | Extra | Charset | Collation | Comment |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `setting_id` | `int unsigned` | NO | `NULL` | PRI | auto_increment |  |  |  |
| 2 | `setting_name` | `varchar(50)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 3 | `setting_value` | `varchar(50)` | NO | `NULL` |  |  | utf8mb3 | utf8mb3_general_ci |  |
| 4 | `user_id` | `int unsigned` | NO | `NULL` | MUL |  |  |  |  |

### Indexes

| Index | Unique | Seq | Column | Type | Nullable | Cardinality | Comment |
|---|---|---:|---|---|---|---:|---|
| `PRIMARY` | Yes | 1 | `setting_id` | BTREE |  | 0 |  |
| `user_id` | No | 1 | `user_id` | BTREE |  | 0 |  |

### Constraints

| Constraint | Type |
|---|---|
| `PRIMARY` | PRIMARY KEY |
