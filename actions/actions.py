# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import numpy as np

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from .helpers.db_adapter import DatabaseAdapter


class ActionQueryResponse(Action):

    def name(self) -> Text:
        return "action_query_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots = ['metric', 'number', 'time_dimension']

        number = int(tracker.get_slot('number'))
        time_dim = tracker.get_slot('time_dimension')

        db = DatabaseAdapter(time_num=number, time_dim=time_dim)
        results = db.query_db()

        msg_params = {'metric': results,
                      'number': number,
                      'time_dimension': time_dim,
                      }

        dispatcher.utter_message(template='utter_query_response', **msg_params)

        return [SlotSet(slot, None) for slot in slots]
