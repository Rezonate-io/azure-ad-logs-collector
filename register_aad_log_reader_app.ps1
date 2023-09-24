# Install and import the Azure PowerShell module (Az module) if not already installed
Install-Module -Name Az

# Connect to Azure
Connect-AzAccount

# Define your Azure AD details
$tenantId = (Get-AzContext).Tenant.Id

# Create a new Azure AD application
$newApp = New-AzADApplication -DisplayName "LogsExportApplication" 

# Define the required permissions for reading audit and sign-in logs
Add-AzADAppPermission -ObjectId $newApp.Id -ApiId 00000003-0000-0000-c000-000000000000 -PermissionId b0afded3-3588-46d8-8b3d-9842eff778da -Type "Role"

# Generate a new client secret for the application
$secret = New-AzADAppCredential -ObjectId $newApp.Id 

# Display the output
Write-Host "AAD Tenant ID: $tenantId"
Write-Host "App ID (Client ID): $($newApp.AppId)"
Write-Host "App Secret: $($secret.SecretText)"

# Wait for the application to be created before consent
Write-Output "Grant admin consent for Default Directory"
Start-Sleep -s 3

# Consent tha application's permission
$url = "https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/~/CallAnAPI/appId/$($newApp.AppId)/isMSAApp~/false"
Start-Process $url