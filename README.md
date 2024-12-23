__Testing__

Run unit tests (including functional tests using djangos test server). Needs to be run from src folder for django to 
find tests.

```python manage.py test```

Run functional tests against local server:

```TEST_SERVER=localhost:8888 python ./src/manage.py test functional_tests --failfast```


Run functional tests against staging server:

```TEST_SERVER=staging.matthewjamesquinn.com python ./src/manage.py test functional_tests```


__Deployment__

Push changes to staging server

```ansible-playbook -i infra/inventory_staging.yaml --vault-password-file infra/.vault-pwd infra/site.yaml```


Push changes to production server

```ansible-playbook -i infra/inventory_production.yaml --vault-password-file infra/.vault-pwd infra/site.yaml```


__Docker__

open a terminal inside a running container

```docker exec -it <container-id-or-name> bash```