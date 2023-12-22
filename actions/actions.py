from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import UserUtteranceReverted
import json
from rasa_sdk.events import SlotSet

import httpx

import asyncio


from actions.ai_support import rasa_text_extract_company_name_project_name,rasa_text_extract_company_name,rasa_text_extract_all_three

from actions.azure_mysql_calls import fetch_all_customers,fetch_project_list

class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hi, How may I assist you?")
 
        return []    
    

class ActionGoodbye(Action):

    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Bye, Comeback when you are in need of further assistance")         
 
        return []
    
class ActionProjectList(Action):

    def name(self) -> Text:
        return "project_list_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        # getting user input
        user_input = tracker.latest_message.get('text')

        # getting customer name via rasa slot
        customer_name = tracker.get_slot('customer_name')

        # res = {
        #     'Title': "Project list",
        #     'Customer name': customer_name
        # }

        


        customer_list = fetch_all_customers()
        print(customer_list)

        # if customer_name is None or company_name_flag == 1:


        res = rasa_text_extract_company_name(user_input)
        print("inside palm",res)

        customer_name = res['company_name']


        if customer_name not in customer_list:
            print("company not present")
            bot_res =  "Customer is not part of our database"
            fetch_success = 0

        else:
            project_list = fetch_project_list(customer_name)
            bot_res =  f"The list of projects of the {customer_name} is ......"
            fetch_success = 1




        
        # else:
        #     res = rasa_text_extract_company_name(user_input)
        #     print("inside palm",res)

        #     customer_name = res['company_name']

        #     project_list = fetch_project_list(customer_name)



        # # checking the customer name is in sql or not
        # url = 'http://127.0.0.1:8000/meta/customer/all'
        # response = httpx.get(url)

        # response = asyncio.run(fetch_all_customers())

        # response = await fetch_all_customers()


        # print(response)

    
        # # flag for finding out the company name is on the DB or not
        # company_name_flag = 0

        # if response.status_code == 200:
        #     customer_data = response.json()
        #     print("Request was successful")
                        
        #     customer_list = []
                        
        #     for data in customer_data:
        #         customer_list.append(data["customer_name"])
                            
        #     if customer_name not in customer_list:
        #         print("company not present")
        #         company_name_flag = 1
                        
        #     else:
        #         print("company present")
        #         # geting all the projects under the customer name
        #         url = f'http://127.0.0.1:8000/meta/customer/{customer_name}'
        #         response = httpx.get(url)


        #     print(customer_list)

        # else:
        #     print(f"Request failed with status code {response.status_code}")
        #     print("Error message:", response.text) 

        # if customer_name is None or company_name_flag == 1:
        #     res = rasa_text_extract_company_name(user_input)
        #     print("inside palm",res)

        #     customer_name = res['company_name']

        


        

        # # geting all the projects under the customer name
        # url = f'http://127.0.0.1:8000/meta/customer/{customer_name}'
        # response = httpx.get(url)

        # if response.status_code == 200:
        #     customer_list = response.json()


        # else:
        #     print(f"Request failed with status code {response.status_code}")
        #     print("Error message:", response.text)


        # print(customer_name)

        # type(customer_name)

        # a = rasa_text_extract(user_input)
        # print("function call",a)

        if fetch_success:
            res = {
                'Title': "Project list",
                'Customer name': customer_name,
                'project list': project_list,
                'bot_text': bot_res
            }
        
        else:
            res = {
                'Title': "Project list",
                'Customer name': customer_name,
                'bot_text': bot_res
            }
            

        msg = json.dumps(res)
        # print(msg)
        dispatcher.utter_message(text=msg)

        return [SlotSet("customer_name", None)]
    
class ActionAlldocList(Action):

    def name(self) -> Text:
        return "all_doc_list_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        customer_name = tracker.get_slot('customer_name')
        project_name = tracker.get_slot('project_name')
        
        res = {
            'Title': "Project list",
            'Customer name': customer_name,
            'Project name': project_name
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return [SlotSet("customer_name", None),SlotSet("project_name", None)]
    
class ActionOnedocList(Action):

    def name(self) -> Text:
        return "single_doc_get_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        customer_name = tracker.get_slot('customer_name')
        project_name = tracker.get_slot('project_name')
        doc_type = tracker.get_slot('doc_type')
        
        res = {
            'Title': "Document type",
            'Customer name': customer_name,
            'Project name': project_name,
            'Doc type':doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return [SlotSet("customer_name", None),SlotSet("project_name", None),SlotSet("doc_type",None)]
    

class ActionTechCustProjectList(Action):

    def name(self) -> Text:
        return "tech_cust_project_list_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        customer_name = tracker.get_slot('customer_name')
        tech_stack = tracker.get_slot('tech_stack')
        
        res = {
            'Title': "Tech stack project list",
            'Customer name': customer_name,
            'Tech stack': tech_stack
        }

        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return [SlotSet("customer_name", None),SlotSet("tech_stack", None)]


class ActionTechAllProjectList(Action):

    def name(self) -> Text:
        return "customer_list_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        customer_name = tracker.get_slot('customer_name')
        
        res = {
            'Title': "Customer list",
            'Tech stack': customer_name
        }

        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return [SlotSet("customer_name", None)]

