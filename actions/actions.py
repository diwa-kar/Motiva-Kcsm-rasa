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

from actions.azure_mysql_calls import fetch_all_customers,fetch_project_list,check_customer_presence,fetch_document_list

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

        # getting user list from azure mysql
        customer_list = fetch_all_customers()
        print("inside projects list",customer_list)

        # checking company name is present or not using regex
        customer_name = check_customer_presence(customer_list,user_input)

        if customer_name != False:
            res = "customer found"
            project_list = fetch_project_list(customer_name)


            res = {
                "bot_text": f"The list of projects of customer {customer_name}  ..",
                "project_list":project_list

            }
        
        else:

             res = {
                "bot_text": f"The given customer is not a part of our DB",

            }
            

        msg = json.dumps(res)
        dispatcher.utter_message(text=msg)

        return [SlotSet("customer_name", None)]
    
class ActionAlldocList(Action):

    def name(self) -> Text:
        return "all_doc_list_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # customer_name = tracker.get_slot('customer_name')
        # project_name = tracker.get_slot('project_name')


        # getting user input
        user_input = tracker.latest_message.get('text')

        # fetch customer_list
        customer_list = fetch_all_customers()
        print(customer_list)


        # checking company name is present or not using regex
        customer_name = check_customer_presence(customer_list,user_input)

        if customer_name != False:
            project_list = fetch_project_list(customer_name)

            # checking project name is present or not
            project_name = check_customer_presence(project_list,user_input)

            if project_name != False:

                doc_data = fetch_document_list(customer_name,project_name)

                res = {
                    "bot_text": f"The documents present in {customer_name}-{project_name}  ..",
                    "doc_data": doc_data,
                }
            
            else:
                res = {
                    "bot_text": "project not present",
                }

        
        else:

             res = {
                "bot_text": f"The given customer is not a part of our DB",
            }




        # res = customer_list


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

