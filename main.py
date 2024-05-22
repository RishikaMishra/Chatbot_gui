from feedback import feed
import tkinter as tk
from tkinter import scrolledtext
import random

class SimpleChatBot:
    def __init__(self):
        self.responses = {
            'hello': ['Hi!', 'Hello!', 'Hey!'],
            'how are you?': ['I am good, thank you!', 'I am just a bot, but I am fine. How about you?'],
            'bye': ['Goodbye!', 'See you later!', 'Bye!'],
            'who are you?': ['I am a simple bot.'],
            "who designed you?": ['I was designed by Rishika Mishra'],
            'i am good': ['Good to know'],
            "how old are you?": ["I was made in 2023, if that's what you are asking!"],
            'thanks': ['Happy to help','anytime','my pleasure'],
            "how you could help me?": ["I am a general purpose chatbot. I can chat with you."],
            "you are dumb": ["Well that hurts :("],
            'what are you doing?': ['Talking to you, ofcourse.'],
            "awesome": ['yeah!'],
            "you are awesome": ['Thankyou!', 'Good to hear.'],
            'it was nice talking to you': ["It was nice talking to you as well! Come back soon."],
            "google": ["Redirecting to Google..."],
            'where is great wall of china?':[" in China"],
            'where is india gate?': ["New Delhi"],
            'name seven wonders':['There are seven wonders listed below: \n 1. Taj mahal(India) \n 2. Christ the redeemer(Brazil) \n 3. great wall of china(China) \n 4. Machu picchu(Peru) \n 5. Petra(Jordan) \n 6. Chichen itza(Maxico) \n 7. Colosseum(Italy) '],
            'who drafted indian constitution?': ['Dr. B.R Ambedkar is drafted the constitution of india.'],
            'who is the national father of our nation?': ['Mahatma gandhi is the father of our nation.'],
            'who takes a decision in court?':['Magistrate takes the decision in court.'],
            'which animal is known as the Ship of the Desert?': ['Camel'],
            'who was the first President of India?':['Dr. Rajendra Prasad'],
            'name five organs of the body': ['Eyes, Ears, Nose, Tounge, Skin'],
            'who invents the computer?': ['Charles Babbage'],
            'how many continents in thw world?': ['There are seven continents in the world.'],
            'name seven continents': ['All the continents listed below: \n 1. Europe \n 2. Antarctica \n 3. Australia \n 4. Africa \n 5. Asia \n 6. North america \n 7. America'],
            'union territories':['there are 9 union territories listed below: \n 1.Delhi \n 2.Andaman and Nicobar \n 3.Lakshdweep \n 4.puducherry \n 5. Dadar and Haveli \n 6. Chandigarh \n 7. Daman and Diu \n 8. Jammu & kashmir \n 9. ladakh'],
            'statue of liberty is situated in which place': ['Statue of liberty is situated in New york(United States) & The height of the sculpture is 305 feet.'],
            'statue of unity is situated in which place': ['Statue of unity is situated in Gujarat(India) & The height of the sculpture is 597 feet.'],
            'how many planets in the solar system?': ['There are 8 planets in the solar system: \n Mercury, Venus, Earth, Mars, Jupiter, saturn, Uranus, Neptune'],
            'tallest building in the world.':['Burj khalifa is the tallest building in the world situated in Dubai'],
            'when do we celebrate our independence day?': ['15th August'],
            'india independence in which year': ['In 1947'],
            'when do we celebrate our republic day?': ['26th January'],
            'from which animal we get silk?': ['Silkworm'],
            'how many states in india?': [' There are 29 states in india.'],
            'who is the president of India?': ['Mrs. Draupadi Murmu'],
            'who is the prime minister of India?': [' Shri Narendra Damodar Das Modi'],
            'who is the health minister of India?': ['Shri Mansukh L. Mandaviya'],
            'who is the education minister of India?': ['Shri Dharmendra Pradhan'],
            'who is the finance minister of India?': ['Shrimati Nirmala Sitharaman'],
            'default':["I'm not sure I understand.", "Can you please elaborate?", "I'm just a simple bot."],

        }
    def get_response(self, message):
        message = message.lower()
        return random.choice(self.responses.get(message, self.responses['default']))

class ChatBotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Chat Bot")
        self.master.geometry('280x420+1000+200')
        self.master.configure(bg='Grey')
        self.master.resizable('false','false')
        self.chatbot = SimpleChatBot()
        self.create_widgets()

    def create_widgets(self):
        self.label=tk.Label(self.master,text="LET'S CHAT!",bg='grey', font=("Georgia","18", "bold"))
        self.label.place(x='15', y='10')

        self.chat_history = scrolledtext.ScrolledText(self.master, width=32, height=20, bg='pink', wrap=tk.WORD)
        self.chat_history.place(x='1',y='50')

        self.user_input = tk.Entry(self.master, width=30)
        self.user_input.place(x='10',y='390')

        self.send_button = tk.Button(self.master, text='SEND', width=8, height=1, command=self.send_message)
        self.send_button.place(x='200',y='385')

        self.feedback_button = tk.Button(self.master, text='Feedback', width=8, height=1, command=feed)
        self.feedback_button.place(x='200', y='15')
    def send_message(self):
        user_message = self.user_input.get()
        self.user_input.delete(0, tk.END)

        # Get the chat bot's response
        bot_response = self.chatbot.get_response(user_message)

        # Display the user's message and the bot's response in the chat history
        self.chat_history.insert(tk.END, f"You: {user_message}\n")
        self.chat_history.insert(tk.END, f"Bot: {bot_response}\n")
        self.chat_history.yview(tk.END)  # Auto-scroll to the bottom

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
