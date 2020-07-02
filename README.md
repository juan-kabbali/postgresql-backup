# pg-backup
CLI for backing up remote PostgreSQL database locally or to an AWS S3 bucket.

## Preparing for Development
1. Ensure pip and pipenv are installed.
2. Clone the repository ``git clone https://github.com/juan-kabbali/postgresql-backup.git``
3. Fetch development dependencies ``make install``


## Usage
Pass in a full database url, storage driver and destination.

**S3 example with bucket name:**

````yaml
$ pg-backup postgres://user@example.com:5432/db_name --driver s3 my_bucket_name
````

**Local example with file name:**

````yaml
$ pg-backup postgres://user@example.com:5432/db_name --driver local /var/local/db_name/backups/dump_2018_09_30.sql
````

## Running Tests
Run tests locally using ``make`` if virtualenv is active:

````yaml
$ make test
````

If virtualenv isn't active, use:

````yaml
$ pipenv run make
````
