## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_bye
* bye
 - utter_bye

## story_thank
* thank
 - utter_thank
 
## story_name
* name{"name":"Sam"}
 - utter_greet
 
## story_happy
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* thank
 - utter_thank
* bye
 - utter_bye 