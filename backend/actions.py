from rasa_sdk import Tracker, FormValidationAction

class ValidateAuthenticateForm(FormValidationAction):
    """Example of a custom form action"""

    def name(self):
        return "validate_authenticate_form"
 
    def validate_slot_name(self, slot_value, dispatcher, tracker, domain):
        return {"name": slot_value}

    def validate_slot_contract_no(self, slot_value, dispatcher, tracker, domain):
        return {"contract_no": slot_value}

    def validate_slot_birthday(self, slot_value, dispatcher, tracker, domain):
        return {"birthday": slot_value}
