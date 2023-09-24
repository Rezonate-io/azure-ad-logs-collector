# azure-ad-logs-collector
A set of scripts used to collect logs from Azure Active Directory (Entra) Tenant

Step 1:
Execute register_aad_log_reader_app.ps1 as an Azure AD administrator. The script will:
1. Authenticate to Azure AD
2. Register a new Azure AD application with permissions to read Audit Logs
3. Create a new set of credentials that will be used in step 2
4. Open a web page to consent the newly created application

Step 2:
1. Edit logs_collector.py - copy the output from Step 1 to the script Constants section
2. Execute logs_collector.py
3. The output will be saved in the script's execution directory in the form of 2 CSV files 
