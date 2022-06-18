#  person_selector_table_maintainer_app

# Link to app
On Azure : [ ]()
<br/>
In Dev : []()

# Learning Links
[Create an app that connects to Azure SQL](https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql)
[Create a Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli)

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

# Set up for development
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
2. Generate project : ./venv/bin/django-admin startproject maintain_db .  
3. Generate application : python3 manage.py startapp person_selector

# To migrate after changing models
1. python manage.py makemigrations
2. python manage.py migrate

# Run server
python3 manage.py runserver  

# To make ready for Azure
1. Add requirements.txt
2. Add 'klingon-transcriber.azurewebsites.net' to ALLOWED_HOSTS
3. Static_root to settings.py
4. Add to urlsettings in url.py + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
