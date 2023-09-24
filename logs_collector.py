import requests, json
import pandas as pd

# Constants
TENANT_ID = 'VALUE_FROM_PS_SCRIPT_OUTPUT'
APP_ID = 'VALUE_FROM_PS_SCRIPT_OUTPUT'
APP_SECRET = 'VALUE_FROM_PS_SCRIPT_OUTPUT'

# Prepare access token request
token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/token"
token_data = {
    "grant_type": "client_credentials",
    "client_id": APP_ID,
    "client_secret": APP_SECRET,
    "resource": "https://graph.microsoft.com"
}

# Get access token
token_response = requests.post(token_url, data=token_data).json()
access_token = token_response["access_token"]

# Make a request to retrieve sign-in logs
graph_api_sign_ins_url = "https://graph.microsoft.com/v1.0/auditLogs/signIns"
headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get(graph_api_sign_ins_url, headers=headers)
sign_ins_json = response.json()
sign_ins_df = pd.DataFrame(sign_ins_json['value'])
# Export sign_ins to csv
sign_ins_df.to_csv(f'aad_sign_ins.csv', index=False)

# TODO: Pagination

# Make a request to retrieve directory audit logs
graph_api_directory_audit_url = "https://graph.microsoft.com/v1.0/auditLogs/directoryAudits"

response = requests.get(graph_api_directory_audit_url, headers=headers)
directory_audit_logs = response.json()
directory_audit_df = pd.DataFrame(directory_audit_logs['value'])
# Export sign_ins to csv
sign_ins_df.to_csv(f'aad_audit_logs.csv', index=False)