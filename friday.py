import pyttsx3
import random
from datetime import date
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pandas as pd

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

dataset = pd.read_csv('shortjokes.csv')

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
	)


engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.elho()
	server.starttls()
	server.login('your_gmail.com','your_password')
	server.sendmail('your_mail',to, content)
	server.close()

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1 # it will give us one sec. rest during commnad
		audio = r.listen(source)

		try:
			print("Recognizing...")
			query = r.recognize_google(audio, language='en-in')
			print(f"User Said: {query}\n")
		except Exception as e:
			speak("Please Say Something Clearly")
			return takeCommand()
	return query

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak("Good Morning Sir")
	elif hour >= 12 and hour < 18:
		speak("Good AfterNoon Sir")
	else:
		speak("Good Evening Sir")

	speak("What can I do for you.")

if __name__ == '__main__':
	wishMe()
	while True:
		query = takeCommand().lower()
		if query is not "None":
			if 'wikipedia' in query:
				speak("Searching Wikipedia...")
				query = query.replace("wikipedia","")
				results = wikipedia.summary(query, sentences=2)
				speak("According to Wikipedia")
				print(results)
				speak(results)

			# elif 'movie' in query:
			# 	moviedir = "F:\\Hollywood Collection II\\Marvel Cinematic Universe\\"
			# 	movies = os.listdir(moviedir)
			# 	# print(songs)
			# 	index_of_movie = random.randint(0,len(movies))
			# 	os.startfile(os.path.join(moviedir,movies[index_of_movie]))

			elif 'time' in query:
				cur_time = datetime.datetime.now().strftime("%H:%M:%S")
				speak(f"Sir, The Time is {cur_time}")

			elif 'date' in query:
				today = date.today().strftime("%B %d %y%y")
				speak(f"Sir, Today is {today}")

			elif 'joke' in query or 'sad' in query:
				speak('Here is a Good joke for you')
				index = random.randint(0, len(dataset))
				speak(dataset['Joke'][index])
				speak("HaHaHa")

			elif 'email' in query:
				try:
					speak('What Should I Say!')
					content = takeCommand()
					to = 'badalkumawat213@gmail.com'
					sendEmail(to, content)
					speak('Email Sent Successfully')
				except Exception as e:
					speak('Sorry Sir, Email does not Sent')

			elif 'who are you' in query:
				speak("I am Friday. Your Personal Assistant")

			elif 'youtube' in query:
				speak("What You want to Watch on youtube")
				commnad = takeCommand()
				speak('Ok Sir. wait')
				webbrowser.get('chrome').open('https://youtube.com/results?search_query=' + commnad)

			elif 'search' in query:
				try: 
					from googlesearch import search 
				except ImportError: 
					print("No module named 'google' found") 
				speak("What You Want to Search")
				# to search 
				query = takeCommand()
				speak('I am Searching')
				x = []
				for j in search(query, tld="co.in", num=5, stop=5, pause=1): 
					x.append(j)
				webbrowser.get('chrome').open(x[0])

			elif 'drive' in query:
					url_path = 'https://drive.google.com/drive/u/0/my-drive'
					speak('Opening Google Drive')
					webbrowser.get('chrome').open(url_path)

			elif 'gmail' in query:
					url_path = 'gmail.com'
					speak('Opening Gmail')
					webbrowser.get('chrome').open(url_path)

			elif 'open google' in query:
				webbrowser.get('chrome').open('www.google.com')

			elif 'thank' in query:
				speak('anytime Sir.')

			elif 'help me' in query or 'you can do' in query:
				speak('I can Give You answers o your queries')

			elif 'bye' in query or 'shutdown' in query:
				speak('See You Sir. Have a good Day')
				break

			else:
				results = wikipedia.summary(query, sentences=2)
				speak("According to me ")
				print(results)
				speak(results)			
		else:
			pass