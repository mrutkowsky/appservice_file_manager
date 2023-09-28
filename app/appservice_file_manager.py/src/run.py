from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient

available_attributes = dir(WebSiteManagementClient)

methods_and_functions = [attr for attr in available_attributes if callable(getattr(WebSiteManagementClient, attr))]

# Print the list of methods and functions
print(methods_and_functions)