#  person_selector_table_maintainer_app

# Link to app
On Azure : [Person Selector DB Maintenance](https://maintainpersonselectordb.azurewebsites.net/person_selector/)
<br/>
In Dev : [Person Selector DB Maintenance](http://127.0.0.1:8000/person_selector/)

# Learning Links
[Create an app that connects to Azure SQL](https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql) <br>
[Create a Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli) <br>
[Connect Django to Azure SQL](https://docs.microsoft.com/en-us/samples/azure-samples/azure-sql-db-django/azure-sql-db-django/) <br>
[Example code from Microsoft with SQL and REST API](https://github.com/Azure-Samples/azure-sql-db-django/tree/main/customerapi) <br>
[Generating models.py for existing databases](https://docs.djangoproject.com/en/4.0/howto/legacy-databases/)

# Command to fix pyodbc install problems on MacOS Monterey
<br> NOTE : Check path for unixodbc by running `ls /opt/homebrew/Cellar/unixodbc/` <br>
CPPFLAGS='-I/opt/homebrew/Cellar/unixodbc/2.3.11/include' LDFLAGS='-L/opt/homebrew/Cellar/unixodbc/2.3.11/lib' pip install pyodbc
## Links to help
[Microsoft Intsructions](https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql)
[Stackexchange](https://stackoverflow.com/questions/71138425/installing-pyodbc-fails-on-osx-12-2-monterey#new-answer)

# packages to be installed in venv
- django
- pyodbc
- azure-identity
- azure-keyvault-secrets
- mssql-django

# Set up for development
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
2. Generate project : ./venv/bin/django-admin startproject maintain_db .  
3. Generate application : python3 manage.py startapp person_selector

# To migrate after changing models
1. python manage.py makemigrations
2. python manage.py migrate

# To generate models.py for existing table
python manage.py inspectdb > models.py

# Run server
python3 manage.py runserver  

# To make ready for Azure
1. Add requirements.txt
2. Add 'maintainpersonselectordb.azurewebsites.net' to ALLOWED_HOSTS
3. Static_root to settings.py (not necessary for this project)
4. Add to urlsettings in url.py + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) (not necessary for this project)
5. Add CSRF_TRUSTED_ORIGINS = ['127.0.0.1', 'maintainpersonselectordb.azurewebsites.net']
in settings.py
6. Give Keyvalut access to App Service
- Create managed identity for app service : Azure web app ->  Identity -> System Assigned ‘ON’ -> Save -> Getobject ID 
- Key Vault -> Access Policies -> Use template  "Secret management" -> Select Principal -> Search by Object ID & select -> Add -> Select Principal -> Search by Object ID & select -> Add
- [How to Use Azure Key Vault With an Azure Web App](https://www.loginradius.com/blog/engineering/guest-post/using-azure-key-vault-with-an-azure-web-app-in-c-sharp/)
- [Assign a Key Vault access policy](https://docs.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal)
