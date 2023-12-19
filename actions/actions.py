from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import UserUtteranceReverted
import json
from rasa_sdk.events import SlotSet



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

        customer_name = tracker.get_slot('customer_name')
        res = {
            'Title': "Project list",
            'Customer name': customer_name
        }
        msg = json.dumps(res)
        print(msg)
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
    

class ActionProjectList(Action):

    def name(self) -> Text:
        return "tech_project_list_action"

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
