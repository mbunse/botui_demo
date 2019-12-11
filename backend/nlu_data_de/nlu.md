<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 --> 

## intent:bye <!--- The label of the intent --> 
- Tschüss 			<!--- Training examples for intent 'bye'--> 
- Auf Wiedersehen
- Bis dann
- Ade
- Einen schönen Tag noch

## intent:greet
- Hallo
- Hi
- Guten Tag
- Guten Morgen
- Guten Abend
- Hallo easyBot
- Good morning

## intent:thank
- Danke
- Danke Dir
- Vielen Dank
- Danke easyBot
- Danke dafür
- Ok danke
- Perfekt, danke

## intent:affirm
- ja
- sicher
- genau
- richtig
- das ist richtig
- korrekt
- das ist korrekt
- ja, so ist es

## intent:contract_no_unknown
- ich finde meine Vertragsnummer nicht
- wo finde ich die Vertragsnummer
- ich weiß meine Vertragsnummer nicht
- ich kenne die Vertragsnummer nicht
- was soll das für eine Nummer sein
- Vertragsnummer habe ich noch nie gehört

## intent:clueless
- keine Ahnung
- weiß ich nicht
- kenne ich nicht
- kein Plan
- ?

## intent:contract_no
- [1234567890](contract_no)
- die Vetragsnummer lautet [0987654321](contract_no)
- meine Vetragsnummer ist [0987654321](contract_no)

## regex:contract_no <!--- Name of regex is just for debugging purposes -->
- [0-9]{10}
