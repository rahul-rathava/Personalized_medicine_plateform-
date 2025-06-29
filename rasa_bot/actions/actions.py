import os
import requests
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from typing import Any, Dict, List, Text

class ActionAnalyzeGenome(Action):
    def name(self) -> Text:
        return "action_analyze_genome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Absolute path to sample genome file
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../app/sample_genome.vcf'))

            # Optional clinical data (can also come from slot in future)
            clinical_notes = {
                "diabetes": True,
                "age": 45,
                "smoker": False
            }

            with open(file_path, 'rb') as f:
                files = {'file': f}
                data = {'clinical_notes': str(clinical_notes)}
                response = requests.post("http://localhost:5006/analyze", files=files, data=data, headers={"Accept": "application/json"})

            if response.status_code != 200:
                dispatcher.utter_message(text=f"❌ Genome analysis failed: {response.text}")
                return []

            data = response.json()
            result = data.get("result", {})

            counts = result.get("counts", {})
            total = result.get("total", 0)
            variants = result.get("variants", [])
            risks = result.get("disease_risks", [])
            drugs = result.get("drug_predictions", [])
            treatments = result.get("treatments", [])
            biomarkers = result.get("biomarkers", [])
            clinical = result.get("clinical_notes", {})

            # Start message
            message = f"✅ Genome Analysis Complete:\n"
            message += f"A: {counts.get('A', 0)}, T: {counts.get('T', 0)}, G: {counts.get('G', 0)}, C: {counts.get('C', 0)}, Total: {total}"

            if variants:
                message += f"\nVariants Detected: {len(variants)}"
            if risks:
                message += "\n🧠 Disease Risk Insights:\n" + "\n".join(risks)
            if drugs:
                message += "\n💊 Drug Response Predictions:\n" + "\n".join(drugs)
            if treatments:
                message += "\n🧩 Personalized Treatment Recommendations:\n" + "\n".join(treatments)
            if biomarkers:
                message += "\n🔬 Biomarker Insights:\n" + "\n".join(biomarkers)
            if clinical:
                message += f"\n🧾 Clinical Notes: {clinical}"

            dispatcher.utter_message(text=message)

        except Exception as e:
            dispatcher.utter_message(text=f"❌ Unexpected error: {str(e)}")

        return []
