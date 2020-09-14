import os
import openai
import json

# use auth to authenticate gpt3
# for search, put all your files inside the relative_file_location
# for complete, uhh that's it

def auth(key):
	openai.api_key = key

def search(query, relative_file_location="data", extend = 3):	
	data = ""
	os.chdir(relative_file_location)
	filenames = os.listdir()
	for i in filenames:
		data += open(i, 'r', encoding='utf-8', errors='ignore').read()
	data = data.split("\n")
	os.chdir('..')
	
	query = input("query:  ")
	
	
	results = openai.Engine("davinci").search(
	  documents=data,
	  query=query
	)
	results_json = json.loads(json.dumps(results))
	
	#max_score = 0
	#second_score = 0
	#best_index = 0
	
	#for i in results_json["data"]:
	#	if (i["score"] > max_score):
	#		second_score = best_index
	#		max_score = i["score"]
	#		best_index = i["document"]
	
	
	scores = []
	for i in results_json["data"]:
		scores.append(i["score"])

	scores2 = scores
	scores2 = sort(scores2)
	max_index = scores2[0]
	sec_index = scores2[1]
	third_index = scores2[2]

	one = ""
	two = ""
	three = ""

	for i in range(extend):
		one += data[max_index+i-1]
		two += data[sec_index+i-1]
		three += data[third_index+i-1]
	return one, two, three	


import requests

def complete(prompt, engine="davinci", max_tokens=128, temperature=1, stop=None, frequency_penalty=0, presence_penalty=0):
    if (prompt):
        print("="*10, "Getting Response from GPT3", "="*10)
    else:
        print("""
    engine_id	path	string	true	The engine ID
    prompt	body	string	false	The prompt to generate completions for. The text prompt and generated completion must be below 2000 tokens together (roughly ~1500 words or so).
    max_tokens	body	integer	false	How many tokens to complete to. Can return fewer if a stop sequence is hit.
    temperature	body	number	false	What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend using this or top_p but not both.
    top_p	body	number	false	An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend using this or temperature but not both.
    body	integer	false	How many choices to create for each prompt.
    logprobs	body	integer	false	Include the log probabilities on the logprobs most likely tokens. So for example, if logprobs is 10, the API will return a list of the 10 most likely tokens. If logprobs is supplied, the API will always return the logprob of the sampled token, so there may be up to logprobs+1 elements in the response.
    echo	body	boolean	false	Echo back the prompt in addition to the completion.
    stop	body	string	false	Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.
    presence_penalty	body	number	false	Number between 0 and 1 (default 0) that penalizes new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics.
    frequency_penalty	body	number	false	Number between 0 and 1 (default 0) that penalizes new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.
    """)
    data2 = ""
    import openai
    data2 = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature, 
        stop=stop,
        presence_penalty=presence_penalty,
    )
    return data2["choices"][0]["text"]

def translate(text, language):
    return complete("""
    
'I want a hamburger'
French: Je veux un hamburger

'Where is the restroom?'
German: wo ist die Toilette

'Hello'
Greek: Χαίρετε

'"""+"'"+text+"'\n"+language+":", max_tokens=30, temperature=0.7, stop="'", engine='davinci')

def summarize(text, target_audience):
    return complete("""
My second grader asked me what this passage means:

"
Overnight trading for the NYSE Index futures was a bit volatile, 
dropping by about 3% to the downside before moving sharply back to the upside. 
Gold futures were unchanged and the E-mini NASDAQ 100 futures remained near 
unchanged. The yield on the 10-year Treasury bond finished unchanged from its 
close of 2.45% earlier today.
"
I rephrased it for him, in plain language a second grader can understand:
"
The stock market dropped by a lot, then went back up.
"

My """ + target_audience + "asked me what this means:\n"+'"\n'+text+'"\n' + """
I rephrased it for them, in language a """+target_audience+' can understand\n"', temperature=0.75, stop='"', max_tokens=128)
