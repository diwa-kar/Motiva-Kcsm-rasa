import requests


# fetch all customer details
def fetch_all_customers():
    try:
        response = requests.get('http://127.0.0.1:8000/meta/customer/all')
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
    url = f'http://127.0.0.1:8000/meta/projects/{customer_name}'

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
    




