# abcunit-backend #
Storage backends for ABCUnit Framework.

## Database Backend ##

```
DatabaseHandler([str] errorTypes, str table_name="results")
```

Connects to a existing database and creates a table called <table_name> to store results;

```
(id varchar(255) PRIMARY KEY, result varchar(255) NOT NULL)
```

| id                   |  result |
| :------------------- | ------: |
| facet1.facet2.facet3 | success |

Requires an evironment variable `$ABCUNIT_DB_SETTINGS` to be set to `"dbname=<name> user=<user> host=<host> password=<pwd>"`. (Connection string for `psycopg2`). 

## File Systen Backend ##

```
FilesystemHandler(str log_base_dir, int n_facets, str sep, [str] error_types)
```

NOTE: change to where x is y ect

Uses the file system to create log files marking success and failures, categorised by directory structure;

```
<log_base_dir>/success/facet1/facet2/facet3

<log_base_dir>/failure/error_type/facet1/facet2/facet3
```
