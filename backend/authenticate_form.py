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
       dispatcher.utter_template('utter_submit', tracker)
       return []