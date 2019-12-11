## story_greet_happy_path <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - authenticate_form
 - form{"name": "authenticate_form"} <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 - slot{"name": "Sam Johns"}
 - slot{"product": "credit"}
 - slot{"birthday": "01.01.1979"}
 - slot{"contract_no": "123457890"}
 - form{"name": null}
 
## story_greet_no_contract
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - authenticate_form
 - form{"name": "authenticate_form"} <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 - slot{"name": "Sam Johns"}
 - slot{"product": "credit"}
 - slot{"birthday": "01.01.1979"}
* contract_no_unknown
 - utter_contract_no_help
 - utter_ask_contract_no
 - slot{"contract_no": "123457890"}
 - form{"name": null}

## story_bye
* bye
 - utter_bye

## story_thank
* thank
 - utter_thank