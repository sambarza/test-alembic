Example of using alembic, sql alchemy with sql server.

- Models migrations
- Sync inserts (10.000 records 130 ms)
- Async inserts (10.000 records in 157 ms)

Steps used to create:

Create the alembic main files:
```
alembic init alembic

  Creating directory '/Users/samuelebarzaghi/temp/test-alembic-solo/alembic' ...  done
  Creating directory '/Users/samuelebarzaghi/temp/test-alembic-solo/alembic/versions' ...  done
  Generating /Users/samuelebarzaghi/temp/test-alembic-solo/alembic/script.py.mako ...  done
  Generating /Users/samuelebarzaghi/temp/test-alembic-solo/alembic/env.py ...  done
  Generating /Users/samuelebarzaghi/temp/test-alembic-solo/alembic/README ...  done
  Generating /Users/samuelebarzaghi/temp/test-alembic-solo/alembic.ini ...  done
  Please edit configuration/connection/logging settings in '/Users/samuelebarzaghi/temp/test-alembic-solo/alembic.ini'
  before proceeding.
```

Inside `alembic.ini` set the db connection info in `sqlalchemy.url`.

Change `env.py`

