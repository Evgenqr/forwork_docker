forwork-web-1  | Watching for file changes with StatReloader
forwork-web-1  | Performing system checks...
forwork-db-1   | The files belonging to this database system will be owned by user "postgres".
forwork-db-1   | This user must also own the server process.
forwork-db-1   | 
forwork-db-1   | The database cluster will be initialized with locale "en_US.utf8".
forwork-db-1   | The default database encoding has accordingly been set to "UTF8".
forwork-web-1  | 
forwork-web-1  | System check identified no issues (0 silenced).
forwork-web-1  | Exception in thread django-main-thread:
forwork-web-1  | Traceback (most recent call last):
forwork-db-1   | The default text search configuration will be set to "english".
forwork-db-1   | 
forwork-db-1   | Data page checksums are disabled.

psql -p 5432 -h 127.0.0.1 -d fasdb -U fasdbadmin

forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/base/base.py", line 219, in ensure_connection
forwork-web-1  |     self.connect()
forwork-db-1   | 
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/utils/asyncio.py", line 33, in inner
forwork-web-1  |     return func(*args, **kwargs)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/base/base.py", line 200, in connect
forwork-web-1  |     self.connection = self.get_new_connection(conn_params)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/utils/asyncio.py", line 33, in inner
forwork-db-1   | fixing permissions on existing directory /var/lib/postgresql/data ... ok
forwork-web-1  |     return func(*args, **kwargs)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/postgresql/base.py", line 187, in get_new_connection
forwork-web-1  |     connection = Database.connect(**conn_params)
forwork-db-1   | creating subdirectories ... ok
forwork-db-1   | selecting dynamic shared memory implementation ... posix
forwork-db-1   | selecting default max_connections ... 100
forwork-db-1   | selecting default shared_buffers ... 128MB
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/psycopg2/__init__.py", line 122, in connect
forwork-db-1   | selecting default time zone ... Etc/UTC
forwork-web-1  |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
forwork-web-1  | psycopg2.OperationalError: could not connect to server: Connection refused
forwork-db-1   | creating configuration files ... ok
forwork-db-1   | running bootstrap script ... ok
forwork-db-1   | performing post-bootstrap initialization ... ok
forwork-web-1  |        Is the server running on host "localhost" (127.0.0.1) and accepting
forwork-db-1   | initdb: warning: enabling "trust" authentication for local connections
forwork-web-1  |        TCP/IP connections on port 5432?
forwork-web-1  | could not connect to server: Cannot assign requested address
forwork-web-1  |        Is the server running on host "localhost" (::1) and accepting
forwork-web-1  |        TCP/IP connections on port 5432?
forwork-web-1  | 
forwork-web-1  | 
forwork-web-1  | The above exception was the direct cause of the following exception:
forwork-web-1  | 
forwork-web-1  | Traceback (most recent call last):
forwork-web-1  |   File "/usr/local/lib/python3.9/threading.py", line 954, in _bootstrap_inner
forwork-web-1  |     self.run()
forwork-web-1  |   File "/usr/local/lib/python3.9/threading.py", line 892, in run
forwork-web-1  |     self._target(*self._args, **self._kwargs)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/utils/autoreload.py", line 64, in wrapper
forwork-web-1  |     fn(*args, **kwargs)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
forwork-web-1  |     self.check_migrations()
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/core/management/base.py", line 486, in check_migrations
forwork-web-1  |     executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS])
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/migrations/executor.py", line 18, in __init__
forwork-web-1  |     self.loader = MigrationLoader(self.connection)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/migrations/loader.py", line 53, in __init__
forwork-web-1  |     self.build_graph()
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/migrations/loader.py", line 220, in build_graph
forwork-web-1  |     self.applied_migrations = recorder.applied_migrations()
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/migrations/recorder.py", line 77, in applied_migrations
forwork-web-1  |     if self.has_table():
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/migrations/recorder.py", line 55, in has_table
forwork-db-1   | initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
forwork-db-1   | syncing data to disk ... ok
forwork-web-1  |     with self.connection.cursor() as cursor:
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/utils/asyncio.py", line 33, in inner
forwork-web-1  |     return func(*args, **kwargs)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/base/base.py", line 259, in cursor
forwork-web-1  |     return self._cursor()
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/base/base.py", line 235, in _cursor
forwork-web-1  |     self.ensure_connection()
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/utils/asyncio.py", line 33, in inner
forwork-web-1  |     return func(*args, **kwargs)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/base/base.py", line 219, in ensure_connection
forwork-web-1  |     self.connect()
forwork-db-1   | 
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/utils.py", line 90, in __exit__
forwork-db-1   | 
forwork-db-1   | Success. You can now start the database server using:
forwork-db-1   | 
forwork-db-1   |     pg_ctl -D /var/lib/postgresql/data -l logfile start
forwork-db-1   | 
forwork-web-1  |     raise dj_exc_value.with_traceback(traceback) from exc_value
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/base/base.py", line 219, in ensure_connection
forwork-web-1  |     self.connect()
forwork-db-1   | waiting for server to start....2023-02-14 17:06:42.268 UTC [49] LOG:  starting PostgreSQL 15.2 (Debian 15.2-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
forwork-db-1   | 2023-02-14 17:06:42.285 UTC [49] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
forwork-db-1   | 2023-02-14 17:06:42.325 UTC [52] LOG:  database system was shut down at 2023-02-14 17:06:41 UTC
forwork-db-1   | 2023-02-14 17:06:42.341 UTC [49] LOG:  database system is ready to accept connections
forwork-db-1   |  done
forwork-db-1   | server started
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/utils/asyncio.py", line 33, in inner
forwork-web-1  |     return func(*args, **kwargs)
forwork-db-1   | CREATE DATABASE
forwork-db-1   | 
forwork-db-1   | 
forwork-db-1   | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
forwork-db-1   | 
forwork-db-1   | waiting for server to shut down....2023-02-14 17:06:45.216 UTC [49] LOG:  received fast shutdown request
forwork-db-1   | 2023-02-14 17:06:45.225 UTC [49] LOG:  aborting any active transactions
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/base/base.py", line 200, in connect
forwork-web-1  |     self.connection = self.get_new_connection(conn_params)
forwork-db-1   | 2023-02-14 17:06:45.249 UTC [49] LOG:  background worker "logical replication launcher" (PID 55) exited with exit code 1
forwork-db-1   | 2023-02-14 17:06:45.251 UTC [50] LOG:  shutting down
forwork-db-1   | 2023-02-14 17:06:45.257 UTC [50] LOG:  checkpoint starting: shutdown immediate
forwork-db-1   | 2023-02-14 17:06:45.481 UTC [50] LOG:  checkpoint complete: wrote 918 buffers (5.6%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.095 s, sync=0.104 s, total=0.231 s; sync files=250, longest=0.014 s, average=0.001 s; distance=4217 kB, estimate=4217 kB
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/utils/asyncio.py", line 33, in inner
forwork-web-1  |     return func(*args, **kwargs)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/django/db/backends/postgresql/base.py", line 187, in get_new_connection
forwork-web-1  |     connection = Database.connect(**conn_params)
forwork-web-1  |   File "/usr/local/lib/python3.9/site-packages/psycopg2/__init__.py", line 122, in connect
forwork-db-1   | 2023-02-14 17:06:45.501 UTC [49] LOG:  database system is shut down
forwork-db-1   |  done
forwork-db-1   | server stopped
forwork-db-1   | 
forwork-db-1   | PostgreSQL init process complete; ready for start up.
forwork-db-1   | 
forwork-db-1   | 2023-02-14 17:06:45.665 UTC [1] LOG:  starting PostgreSQL 15.2 (Debian 15.2-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
forwork-db-1   | 2023-02-14 17:06:45.696 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
forwork-db-1   | 2023-02-14 17:06:45.704 UTC [1] LOG:  listening on IPv6 address "::", port 5432
forwork-db-1   | 2023-02-14 17:06:45.773 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
forwork-db-1   | 2023-02-14 17:06:45.819 UTC [65] LOG:  database system was shut down at 2023-02-14 17:06:45 UTC
forwork-db-1   | 2023-02-14 17:06:45.858 UTC [1] LOG:  database system is ready to accept connections
forwork-web-1  |     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
forwork-web-1  | django.db.utils.OperationalError: could not connect to server: Connection refused
forwork-web-1  |        Is the server running on host "localhost" (127.0.0.1) and accepting
forwork-web-1  |        TCP/IP connections on port 5432?
forwork-web-1  | could not connect to server: Cannot assign requested address
forwork-web-1  |        Is the server running on host "localhost" (::1) and accepting
forwork-web-1  |        TCP/IP connections on port 5432?
forwork-web-1  | 
