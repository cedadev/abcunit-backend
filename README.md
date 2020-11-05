# abcunit-backend #

Storage backends for an ABCUnit Framework, logging success and failures of process units.

<br/>

## Database Backend ##

```
DatabaseHandler(error_types, table_name="results")
```

Where;
 * `error_types` is a list of the string names of the different types of errors that you want to log
 *  `table_name` is the name of the table logs will be insert into

Connects to an existing database and creates a table to store results;

```
<table_name> (id varchar(255) PRIMARY KEY, result varchar(255) NOT NULL)
```
|          id          |  result  |
| :------------------: | :------: |
| facet1.facet2.facet3 | success  |
| facet1.facet2.facet3 | bad_file |
|       &#8942;        | &#8942;  |

<br/>

Requires an evironment variable `$ABCUNIT_DB_SETTINGS` to be set to `"dbname=<name> user=<user> host=<host> password=<pwd>"` (Connection string for `psycopg2`).

<br/>

## File Systen Backend ##

```
FilesystemHandler(base_log_dir, n_facets, sep, error_types)
```

Where;
 * `base_log_dir` is the string path to top level directory for logs
 * `n_facets` is the number of facets used to describe each unit result
 * `sep` is the separator used for a result identifier
 * `error_types` is a list of the string names of the different types of errors that you want to log

Uses the file system to create log files marking success and failures, categorised by directory structure;

```
<log_base_dir>/success/facet1/facet2/facet3

<log_base_dir>/failure/error_type/facet1/facet2/facet3
```
