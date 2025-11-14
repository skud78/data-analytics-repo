from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.compute import ComputeManagementClient

subscription_id = 'your-subscription-id'
resource_group_name = 'your-resource-group'
location = 'eastus'

credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)
# Create Resource Group
resource_client.resource_groups.create_or_update(resource_group_name, {'location': location})   

vm_parameters = {
    'location': location,
    'storage_profile': {
        'image_reference': {
            'publisher': 'Canonical',
            'offer': 'UbuntuServer',
            'sku': '18.04-LTS',
            'version': 'latest'
        }
    },
    'hardware_profile': {
        'vm_size': 'Standard_DS1_v2'
    },
    'os_profile': {
        'computer_name': 'myVM',
        'admin_username': 'azureuser',
        'admin_password': 'YourPassword123'
    },
    'network_profile': {
        'network_interfaces': [{
            'id': '/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/networkInterfaces/myNic',
            'primary': True
        }]
    }
}   

vm = compute_client.virtual_machines.begin_create_or_update(resource_group_name, 'myVM', vm_parameters).result()
print("VM created:", vm.name)
