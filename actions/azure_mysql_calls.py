import requests
import re


# fetch all customer details
def fetch_all_customers():
    try:
        response = requests.get('http://43.204.46.203:8000/meta/customer/all')
        response.raise_for_status()  # Raise an exception for bad responses (non-2xx)

        customer_data = response.json()
        print("Request was successful")
        print(customer_data)

        customer_list = [data["customer_name"] for data in customer_data]
        return customer_list

    except requests.exceptions.RequestException as e:
        print(f"Request failed with exception: {e}")
        print("Cannot fetch the customer list")

        return f"Request failed with exception: {e}"
    



# fetch project list using customer name
def fetch_project_list(customer_name):
    url = f'http://43.204.46.203:8000/meta/projects/{customer_name}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (non-2xx)

        project_data = response.json()

        project_list = [projects["project_name"].split('/')[1] for projects in project_data]

        return project_list

    except requests.exceptions.RequestException as e:
        print(f"Request failed with exception: {e}")
        print("Error message:", response.text if 'response' in locals() else 'No response object')
        return []
    


def fetch_document_list(customer_name,project_name):
    url = f'http://43.204.46.203:8000/meta/documents/{customer_name}/{project_name}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (non-2xx)
        
        project_doc_list = response.json()

        return_data_list = []

        for i in project_doc_list:
            data_dict = {}
            
            data_dict["customer_id"]= i["customer_id"]
            data_dict["project_id"]= i["project_id"]
            data_dict["project_name"]= i["project_name"].split('/')[1]
            data_dict["document_id"]= i["document_id"]
            data_dict["document_name"]= i["document_name"].split('/')[2]
            
            data_dict["document_type"]= i["document_type"]
            data_dict["document_extension"]= i["document_extension"]
            data_dict["phase"]= i["phase"]
            data_dict["document_storage_link"]= i["document_storage_link"]
            
            return_data_list.append(data_dict)

        return return_data_list

    except requests.exceptions.RequestException as e:
        print(f"Request failed with exception: {e}")
        print("Error message:", response.text if 'response' in locals() else 'No response object')
        return []





## Regex calls to get company name
    

def check_customer_presence(customer_names, line):
    for customer_name in customer_names:
        pattern = re.compile(fr'\b{re.escape(customer_name)}\b', re.IGNORECASE)
        if re.search(pattern, line):
            return customer_name
    
    return False
