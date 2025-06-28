import os
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text

class ActionAnalyzeGenome(Action):
    def name(self) -> Text:
        return "action_analyze_genome"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../../app/sample_genome.txt')
        )

        try:
            with open(file_path, 'rb') as f:
                files = {'file': ('sample_genome.txt', f)}
                response = requests.post("http://localhost:5006/analyze", files=files)

                print("Status Code:", response.status_code)
                print("Raw Response:", response.text)

                data = response.json()
                dispatcher.utter_message(text=data.get("message", "Genome analysis failed."))
        except Exception as e:
            dispatcher.utter_message(text=f"Error: {str(e)}")

        return []
