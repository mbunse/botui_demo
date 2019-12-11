from rasa_sdk.forms import FormAction

class AuthenticateForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""
 
        return "authenticate_form"
 
    @staticmethod
    def required_slots(tracker):
        # type: () -> List[Text]
        """A list of required slots that the form has to fill"""
 
        return ["name", "product", "birthday",
                "contract_no"]
 
    def submit(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
           after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_bye', tracker)
        return []

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""

        return {
                "name": [self.from_entity(entity="name")],
                "product": [self.from_entity(entity="product")],
                "birthday": [self.from_entity(entity="birthday")],
                }
