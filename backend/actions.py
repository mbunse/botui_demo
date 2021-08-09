import re

from rasa_sdk import Tracker, FormValidationAction

class ValidateAuthenticateForm(FormValidationAction):

    # pattern for uncode word characters except numbers    
    regex_name = r'[^\W\d]{2,}(\s[^\W\d]{2,}){0,2}'
    regex_contract_no = r'[0-9]{10}'
    regex_birthday = r'\d\d\d\d-\d\d-\d\d'
    max_allowed_vaid_fails = 1
    def name(self):
        return "validate_authenticate_form"

    def validate_name(self, slot_value, dispatcher, tracker, domain):
        return self._validate_slot("name", slot_value, dispatcher, tracker)

    def validate_contract_no(self, slot_value, dispatcher, tracker, domain):
        return self._validate_slot("contract_no", slot_value, dispatcher, tracker)

    def validate_birthday(self, slot_value, dispatcher, tracker, domain):
        return self._validate_slot("birthday", slot_value, dispatcher, tracker)

    def _validate_slot(self, slot_name, slot_value, dispatcher, tracker):
        if re.fullmatch(getattr(self, f"regex_{slot_name}"), slot_value):
            return {
                slot_name: slot_value,
                "validate_authenticate_form_fails": 0,
                }

        validate_authenticate_form_fails = 1
        if tracker.get_slot("validate_authenticate_form_fails") is not None:
            validate_authenticate_form_fails = tracker.get_slot("validate_authenticate_form_fails") + 1

        dispatcher.utter_message(response=f"utter_not_valid_{slot_name}", slot_value=slot_value)
        return {
            slot_name: None,
            "validate_authenticate_form_fails": validate_authenticate_form_fails,
            # to end the form action, set requested_slot to none if the max allowed fails are exceeded.
            "requested_slot": None if validate_authenticate_form_fails > self.max_allowed_vaid_fails else slot_name,
            }