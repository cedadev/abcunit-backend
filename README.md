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
FilesystemHandler(int n_facets, str sep, [str] error_types)
```

Uses the file system to create log files marking success and failures, categorised by directory structure;

```
$ABCUNIT_LOG_DIR/sucess/facet1/facet2/facet3

$ABCUNIT_LOG_DIR/failure/error_type/facet1/facet2/facet3
```

Set `$ABCUNIT_LOG_DIR` before using.