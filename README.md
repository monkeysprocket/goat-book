Run unit tests (including functional tests using djangos test server). Needs to be run from src folder for django to 
find tests.

```python manage.py test```

Run functional tests against local server:

```TEST_SERVER=localhost:8888 python ./src/manage.py functional_tests --failfast```


Run functional tests against staging server:

```TEST_SERVER=staging.matthewjamesquinn.com python ./src/manage.py test functional_tests```
