import random

main = True
print("Hello, my name is Archibald II, but you can call me Arhie, what can I call you?")

username = input()
reply = {
 "true vagueness": {
   [f"That's interesting, {username}", 
   "How about that?",
   "Huh, you don't say",
   "Wow" 
   ]
   }
 "What is the time":{# I have no idea what is happening here. I can't find an answer any where either.
   ["Here, let me show you my watch.",
   "Why? You got somewhere to be?",
   "It's 4:30pm where I am.",
   "What even is time?"
   ]
   }
 "nothing": {
   [
     "Violen-oh, sorry, I mean silence can speak volumes",
   "Take your time, it's not like I'm going anywhere."
    "... hm ..."
    "... "
    "Would do like me to show you some options?"
   ]
   }
 "What is the weather":{
   [
    "Well their may or may not we clouds in the skys."
    "On Jupiter, it is storming."
    "I wish I could tell you but it looks like all of the Earth's satellites have vansihed."
     "Weather is defined as the state of the atmosphere at a given time and place, with respect to variables such as temperature, moisture, wind velocity, and barometric pressure."
   ]
   }
  }
bad_words = ["upload", "extension cord", "scrap"]
# I've been trying to  make it so the program scans for bad words, and I haven't figured out how.
def generated_response(user_input):
 
  if "what" and "time" in user_input:
   generated_response =  random.choice(reply["What is the time?"])
 
 elif "what" and "weather" in user_input:
   generated_response = random.choice(reply["What is the weather"])
 
 elif "" in user_input:
   generated_response = random.choice(reply["nothing"])


 elif "thanks" in user_input:
   generated_response = "No problem, but if this is a sarcastic response please remember I am a bot, and just tell the monkey who made me to code better."
 
 elif user_input == "Yes":
   generated_response = "Yes, what?"

 elif "show" and "options" in user_input:
   generated_response = " At the moment you can ask me about; the time, or the weather."

 else:
   generated_response = random.choice(reply["true vagueness"])
 return generated_response









def init_chat():
 quit_character = 'q'
 print(f"It's great to meet you {username}, how are you?")
 user_input = input()
 print(f"'{user_input}'? Well, that's interesting. Ask me anything you want.")
 user_input = input()
 while user_input != quit_character:
    user_input = input(generated_response(user_input) + "\n")
  

if __name__ == "__main__":
 init_chat()