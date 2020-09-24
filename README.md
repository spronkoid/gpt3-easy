# GPT3 put simply
---
(edit: I didn't actually know they were monatizing it so I won't be able to update this if it changes, I'm from a very poor background and would never in my whole life be able to pay 100 dollars per month for this) <br>
Just a few lines of code that should help you with interacting with the GPT3 model (in python, javascript version soon maybe?) <br>
Examples of usage:

### 1. Sentiment Analysis
```python
import gpt3.complete as c
prompt = """
'I hate this' Negative
'Its cool' Positive
'I love it!'"""

auth('sk-yourkeygoeshere')
print(c(prompt, stop="'") # stop generating once it hits the '
```
Options for `gpt3.complete` are as follows:
```
prompt (required) - The prompt to generate completions from
max_tokens (optional) - How many tokens to complete to (how long should the text be)
temperature (optional) - What sampling temperature to use. Higher values will mean the model will take more "risks"
top_p (optional) - An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend using this or temperature but not both.
stop (optional) - Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.
presence_penalty (optional) - Number between 0 and 1 (default 0) that penalizes new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics.
frequency_penalty	(optional) - Number between 0 and 1 (default 0) that penalizes new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.
engine (optional) - the engine ID
```

### 2. Document Searching
returns the three best matches for your query
first put a file (name is irrelevant) containing your text within a folder entitled `data` located within the same directory of your code. <br>
(alternatively use the `relative_file_location` parameter to specify which folder to read, be careful! it reads every file within that folder.)
```python
import gpt3.search as search
import gpt3.auth as auth

query = "mitochondria"

auth('sk-yourkeygoeshere')
one, two, three = search(query)
print(one)
```
Options for `gpt3.search` are:
```
query (required) - A string to search for within the data
relative_file_location (optional) the folder in which all texts are stored to be searched through
extend (optional) - how many lines after the one stated should be required (default 3) usually helps with context if what you've searched for is the Title of a document
```
### Other Documentation:

`gpt3.auth ` is for authenticating your instance of GPT3, it's used here (where `sk-yourkeygoeshere` should be replaced with your key:
```python
gpt3.auth('sk-yourkeygoeshere')
``` 
---
(edit) I've also added `translate(text, language)` and `summarize(text, target_audience)` where strings are the values provided, for example the `target_audience` could be `"third grader"`

Follow me on Twitter [@spronkoid](https://twitter.com/spronkoid)
