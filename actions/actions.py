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

        # # getting customer name via rasa slot
        # customer_name = tracker.get_slot('customer_name')

        # res = {
        #     'Title': "Project list",
        #     'Customer name': customer_name
        # }

        customer_list = fetch_all_customers()
        print(customer_list)

        # if customer_name is None or company_name_flag == 1:

        res = rasa_text_extract_company_name(user_input)
        print("inside palm",res)

        customer_name = res['company_name'].lower()

        # print(customer_name)


        if customer_name not in customer_list:
            print("company not present")
            bot_res =  "Customer is not part of our database"
            fetch_success = 0

        else:
            project_list = fetch_project_list(customer_name)
            bot_res =  f"The list of projects of the {customer_name} is ......"
            fetch_success = 1


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

        # customer_name = tracker.get_slot('customer_name')
        # project_name = tracker.get_slot('project_name')


        # getting user input
        user_input = tracker.latest_message.get('text')

        # fetch customer_list
        customer_list = fetch_all_customers()
        print(customer_list)


        res = rasa_text_extract_company_name_project_name(user_input)
        print("inside palm",res)

        customer_name = res['company_name'].lower()
        project_name = res['project_name'].lower()


        print(customer_name,project_name)

        # project_name = res['']


        # if customer_name not in customer_list:
        #     print("company not present")
        #     bot_res =  "Customer is not part of our database"
        #     fetch_success = 0




        # else:
        #     project_list = fetch_project_list(customer_name)
        #     # bot_res =  f"The list of projects of the {customer_name} is ......"
        #     # fetch_success = 1

            

        
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

        
        res = {
            'Title': "Customer list",
        }

        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return [SlotSet("customer_name", None)]

