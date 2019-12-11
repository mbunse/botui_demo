<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 --> 

## intent:bye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot

## intent:thank
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely

## intent:contract_no_unknown
- i can't find my contract no
- i can't find my contract number
- where do i find my contract no
- i don't know my contract number
- never heard of a contract number

## intent:clueless
- no plan
- no idea
- i don't know
- ?

## intent:contract_no
- [1234567890](contract_no)
- my contract no is [0987654321](contract_no)
- [0987654321](contract_no) is my contract number

## regex:contract_no <!--- Name of regex is just for debugging purposes -->
- [0-9]{10}