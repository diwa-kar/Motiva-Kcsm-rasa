from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import UserUtteranceReverted
import json


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
    
class ActionRetriveTP(Action):

    def name(self) -> Text:
        return "action_retrive_tp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        project_name = tracker.get_slot('project_name')
        customer_name = tracker.get_slot('customer_name')
        doc_type = tracker.get_slot('doc_type')
        res = {
            'Title': "Retrive TP Document",
            'Project name': project_name,
            'Customer name': customer_name,
            'Document type': doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []
    
class ActionRetriveCP(Action):

    def name(self) -> Text:
        return "action_retrive_cp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot('project_name')
        customer_name = tracker.get_slot('customer_name')
        doc_type = tracker.get_slot('doc_type')
        res = {
            'Title': "Retrive CP Document",
            'Project name': project_name,
            'Customer name': customer_name,
            'Document type': doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []
    
class ActionRetriveFRS(Action):

    def name(self) -> Text:
        return "action_retrive_frs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot('project_name')
        customer_name = tracker.get_slot('customer_name')
        doc_type = tracker.get_slot('doc_type')
        res = {
            'Title': "Retrive FRS Document",
            'Project name': project_name,
            'Customer name': customer_name,
            'Document type': doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []

class ActionRetriveRFP(Action):

    def name(self) -> Text:
        return "action_retrive_rfp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot("project_name")
        print(project_name)
        customer_name = tracker.get_slot('customer_name')
        doc_type = tracker.get_slot('doc_type')
        res = {
            'Title': "Retrive RFP Document",
            'Project name': project_name,
            'Customer name': customer_name,
            'Document type': doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []

class ActionRetriveSDD(Action):

    def name(self) -> Text:
        return "action_retrive_sdd"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot('project_name')
        customer_name = tracker.get_slot('customer_name')
        doc_type = tracker.get_slot('doc_type')
        res = {
            'Title': "Retrive SDD Document",
            'Project name': project_name,
            'Customer name': customer_name,
            'Document type': doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []
    
class ActionRetriveUAT(Action):

    def name(self) -> Text:
        return "action_retrive_uat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot('project_name')
        customer_name = tracker.get_slot('customer_name')
        doc_type = tracker.get_slot('doc_type')
        res = {
            'Title': "Retrive UAT Document",
            'Project name': project_name,
            'Customer name': customer_name,
            'Document type': doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []
    
class ActionRetriveCutover(Action):

    def name(self) -> Text:
        return "action_retrive_cutover"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot('project_name')
        customer_name = tracker.get_slot('customer_name')
        doc_type = tracker.get_slot('doc_type')
        res = {
            'Title': "Retrive cutover Document",
            'Project name': project_name,
            'Customer name': customer_name,
            'Document type': doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []
    
class ActionRetriveSignoff(Action):

    def name(self) -> Text:
        return "action_retrive_signoff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot('project_name')
        customer_name = tracker.get_slot('customer_name')
        doc_type = tracker.get_slot('doc_type')
        res = {
            'Title': "Retrive signoff Document",
            'Project name': project_name,
            'Customer name': customer_name,
            'Document type': doc_type
        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []
    
class ActionRetriveAlldocs(Action):

    def name(self) -> Text:
        return "action_retrive_alldocs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot('project_name')
        customer_name = tracker.get_slot('customer_name')

        res = {
            'Title': "Retrive All Documents",
            'Project name': project_name,
            'Customer name': customer_name,

        }
        msg = json.dumps(res)
        print(msg)
        dispatcher.utter_message(text=msg)

        return []
    
class ActionProjectList(Action):

    def name(self) -> Text:
        return "action_project_list"

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

        return []
    