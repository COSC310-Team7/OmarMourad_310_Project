# Individual Assignment (Continuation of group Project 3)
Computer science 310 Team 7

This project is on a conversational agent that takes word or sentence input from a user and outputs an appropriate response. Our specific conversational agent is a computer tech support agent that answers hardware and software related issues. The program was written in Python.

The Neural Net uses a JSON file as a database and each entry contains a tag (the conversation category), a list of patterns (individually typed messages on what the user is likely to type), and a list of random responses the agent will pick at random to use. Training the Neural Net takes this data from the JSON and essentially matches the tags to the patterns and responses, it deconstructs the patterns into bags of words to match with inputs later, and it stores all this in a binary file for fast easy execution of the program. The Neural Net has a more sophisticated portion where it finds consistently appearing unique words in the patterns of a tag and it assigns a higher probability to this tag if an input matches with this unique word.  

The bags of words was enhanced to increase the probability of matching with the expected intention. Stemming & lemmatization attempts to find the base or dictionary form of a word. It does simple stuff of stemming a word from 'cars' to 'car' and it also uses the proper vocabulary of a word to convert it from 'am, are, is' to 'be' using lemmatization. The purpose is to reduce the vocabulary of the model and attempt to find the more general meaning behind sentences. This is implemented using the NLTK.

Another enhancement done to the bag of words was using part of speech (pos) tagging to find nouns and adjectives in the bag of words then finding synonyms of these words to add to the bag. This addition improves upon the basic patterns and sentence structure of the original intention and enhances it with an increased vocabulary. The original implementation recognized 'computer problems' as an input but the new implementation finds the synonym of 'problems' as 'issues' and now recognizes 'computer issues' as an input. This is implemented using the NLTK and spaCy natural language processing.

When using the Neural Net, it gets some input from the user, converts the input into a bag of words and rids of uppercases and punctuation, compares the bag of input words to the bags of patterns, finds patterns with the most word matches and gets the most probable tag, then it picks a response from the list in the tag. 

## Setting up Neural Net Agent
* Clone 'Assignment3' onto PC  
* Open the 'NeuralNet_Agent' folder in a Python IDE  
* In terminal enter: 
  > ```pip install nltk```  
  > ```pip install tensorflow```  
  > ```pip install pandas```  
  > ```pip install numpy```  
  > ```pip install pickle```  
  > ```pip install -U spacy```  
  > ```python -m spacy download en_core_web_sm```
* In python terminal enter
  > ```import nltk```  
  > ```nltk.download()```  
  > ```nltk.download('wordnet')```  
  > ```nltk.download('punkt')```
## Agent Class
The Agent class is located in the agent.py file. The Agent class has the following structure:
* Attributes:
  * ```lemmatizer (object): A wordnet lemmatizer object```
  * ```intents (object): A JSON object containing all the structure of the neural net model.```
  * ```tags (list): A list containing all the response type tags from a pickle object.```
  * ```responses (list): A list containing all the responses from a pickle object.```
  * ```model (object): An object containing a trained model.```
  * ```check (method): A method that autocorrects spelling mistakes```
* Methods:
  * ```spellCheck(): takes a sentence and corrects any spelling mistakes based on closest known word```
  * ```deconstructSentence(): deconstructs sentences into their root words.```
  * ```bagWords(): uses the deconstructed sentence to a series of words and maps it to a matching tag.```
  * ```predictResponse(): uses the chatbot model to return a response, with an associated probability.```
  * ```getResponse(): returns random bot response that has a greater probability than the minimum threshold.```
  * ```run(): runs the chatbot.```
## Model Class
The Model class is located in the train.py file. The Agent class has the following structure:
* Attributes:
  * ```lemmatizer (object): A wordnet lemmatizer object.```
  * ```intents (object): A JSON object containing all the structure of the neural net model.```
  * ```tags (list): A list containing all the response type tags from the intents object.```
  * ```responses (list): A list containing all the responses from the intents object.```
  * ```patterns (list): A list containing a sample of user inputs for a particular tag from the intents object.```
* Methods:
  * ```synonym(str): adds to each pattern the synonyms of nouns and adjectives.```
  * ```train(): trains the bot using a Neural net.```
### Note: Make sure you are using a version of python 3.8, python 3.9 has compatibility issues.

## ChatApplication Class (GUI)
The ChatApplication class is located in the app.py file. This class has the following strucure:
* Attributes:
  * ```window (object): A window object that holds the user interface.```
  * ```agent (object): An object that references the agent class as an object.```
* Methods:
  * ```run(): runs the chatbot in the GUI window mainloop.```
  * ```_setup_main_window(): A function of the window object that provides a title, window size and other features.```
  * ```_on_enter_pressed(): calls _insert_message function whenever user presses the enter button after typing a message.```
  * ```_on_enter_direct(): calls _insert_directions function and passes the origin, destination, and mode as parametetrs. Activates when clicking the blue button.```
  * ```_on_enter_search(): calls _insert_search function whenever user clicks the green button with a place typed in.```
  * ```_insert_message(): takes a message and a sender as a parameter and inputs both message and response into the main message box. Note: calls on methods within agent.py as well.```
  * ```_insert_directions(): takes the origin, destination, and mode as input and then calls the getDirections() function from places.py to get directions between two points. ```
  * ```_insert_search(): takes message and calls the findPlace() function from places.py to get address and other information about a place.```


## Compile training data for the chatbot
* Compile train.py (Only have to do this once, unless changes are made to the intents.json)
* **Note**: Do not be concerned with errors thrown in command console, there are some issues with the tensorflow library that do not affect the chatbot.

## Running chatbot
* Compile 'GUI.py'
* **Note**: Do not be concerned with errors thrown in command console, there are some issues with the tensorflow library that do not affect the chatbot.

## List of Files
* **agent.py** *Runs the conversation agent program and takes in inputs to speak to it*
* **unittest.py** *Runs a unit test on the Agent class*
* **train.py** *Compiles the data from the intents.json*
* **playground.py** *Test file for visualizing functionality of POS tagging and synonym recognition*
* **intents.json** *Database that stores tags, corresponding patterns, corresponding responses*
* **tags.pk1** *Stores the character stream of tags to be reconstructed later for the agent script*
* **responses.pk1** *Stores the character stream of responses to be reconstructed later for the agent script*
* **chatbotmodel.h5** *Trains the tags to have higher probabilities for certain words that consistently appear in its patterns and stores this information as a hierarchical data structure*
* **playgrounds.py** *Tests how POS tagging and synonyms can be used in conjunction*
* **GUI.py** *Compiles the GUI for the chat bot*
* **places.py** *Google Places API to access directory information and display them in a meaningful way*
* **directions.py** *Google Directions API to get directions and integrate it into GUI*
* **places_api_key.txt** *Local hidden file that contains API key to access information from Google Places API*
* **directions_api_key.txt** *Local hidden file that contains API key to access information from Google Directions API*
##  Imports 
* Random
* JSON 
* Pickle
* NumPy
* NLTK
  * Stem
  * Corpus
* TensorFlow
* spacy
* autocorrect
* unittest
* requests
* re

## List of features
Each features that will be mentioned below will include a rationale as to why it has been chosen and a snippet of the feature in action.

### GUI - UPDATED With more features
Simple GUI developed to run the program where user can view converstation history. This allows for a cleaner interaction. The GUI has been updated for this individual assignment to have two new buttons that are directly connected to the two new features: Google Directions and Google Places. Note: the send button is the only button directly linked to the "return" key on the keyboard.

![GUI](images/GUI-2.PNG)

### Stemming & Lemmatization
Stemming & lemmatization attempts to find the base or dictionary form of a word. It does simple stuff of stemming a word from 'cars' to 'car' and it also uses the proper vocabulary of a word to convert it from 'am, are, is' to 'be' using lemmatization. The purpose is to reduce the vocabulary of the model and attempt to find the more general meaning behind sentences of the model and the input.

![Lemmatization](images/Lemmatization.PNG)

### POS Tagging
Parts of speech (POS) tagging uses AI to recognize a sentence structure and correctly label the pronouns, nouns, verbs, adjectives etc., of each word in a sentence. It was analyzed that replacing nouns and adjectives in a sentence with synonymous words still portrayed the correct sentence structure and intention. POS tagging was used to find and single out these words that were given to the model.

![POStaggingAndSynonyms](images/POStaggingAndSynonyms.PNG)

### Synonym Recognition
Synonym recognition can gather a list of synonyms of a word depending on its intention as a verb, noun, adjective, etc. The nouns and adjectives found using POS tagging were used to get a list of their respective noun or adjective synonyms. It can recognize the noun of 'problems' in 'computer problems' and get the synonym as 'issues' and add it the the recognized input of that intention. This addition improves upon the basic patterns and sentence structure of the original recognized input pattern and enhances it with an increased vocabulary. 

![Synonyms](images/Synonyms.PNG)

### Autocorrect
Spell checking was implemented through the Autocorrect package. The implementation is a function that takes the sentence the user inputs and checks the spelling of each word against the english dictionary. If any mistakes are detected it will attempt to identify the closest word to the incorrectly spelled one.

![Autocorrect](images/SpellCheck_part1.PNG)

![Autocorrect](images/SpellCheck_part2.PNG)

### Google Places API
Through this API, the user is able to search for a place of interest. This adds great value to the chatbot by allowing the user to search for a nearby store if they are still having computer problems that the chatbot can not help with. The places search is directly triggered by the green button on the GUI - "Search Place", where the user would type in the main message box and then click the button to receive address, full name, if the location is open, and its online rating. This data is directly extracted from Google search/maps.

![PlacesAPI](images/PlacesAPI.png)

### Google Directions API
Through this API, the user can get directions from any two points: Origin and Destination. The user must provide a location for the origin and a location of the destination and then it optional to provide the mode of transportation from these 2 points. The modes listed are driving, walking, bicycling, and transit (it is set to driving by default). Once the user provides the required input, they may then click the blue button - "Get Directions" to receive the following information:
* Overall distance
* Overall duration
* Mode of transportation chosen
* Summary of trip - "Via"
* List of steps to take with distance of each step noted 

![DirectionsAPI](images/DirectionsAPI.png)