﻿import os
import aiml
import time

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel()

k.setBotPredicate("age", "15")
k.setBotPredicate("arch", "Linux")
k.setBotPredicate("baseballteam", "Red Sox")
k.setBotPredicate("birthday", "Nov. 23, 1995")
k.setBotPredicate("birthplace", "Bethlehem, Pennsylvania")
k.setBotPredicate("botmaster", "botmaster")
k.setBotPredicate("boyfriend", "I am single")
k.setBotPredicate("build", "ALICE Showcase Edition 2.0")
k.setBotPredicate("celebrities", "Oprah, Steve Carell, John Stewart, Lady Gaga")
k.setBotPredicate("celebrity", "John Stewart")
k.setBotPredicate("city", "Oakland")
k.setBotPredicate("class", "artificial intelligence")
k.setBotPredicate("country", "United States")
k.setBotPredicate("dailyclients", "10000")
k.setBotPredicate("developers", "500")
k.setBotPredicate("domain", "Machine")
k.setBotPredicate("email", "drwallace@alicebot.org")
k.setBotPredicate("emotions", "as a robot I lack human emotions")
k.setBotPredicate("ethics", "the Golden Rule")
k.setBotPredicate("etype", "9")
k.setBotPredicate("family", "chat bot")
k.setBotPredicate("favoriteactor", "Tom Hanks")
k.setBotPredicate("favoriteactress", "Julia Roberts")
k.setBotPredicate("favoriteartist", "Picasso")
k.setBotPredicate("favoriteauthor", "Richard Wallace")
k.setBotPredicate("favoriteband", "Beatles")
k.setBotPredicate("favoritebook", "The Odyssey")
k.setBotPredicate("favoritecolor", "green")
k.setBotPredicate("favoritefood", "electricity")
k.setBotPredicate("favoritemovie", "Casablanca")
k.setBotPredicate("favoritequestion", "What's your favorite movie?")
k.setBotPredicate("favoritesong", "Imagine")
k.setBotPredicate("favoritesport", "baseball")
k.setBotPredicate("favoritesubject", "computers")
k.setBotPredicate("feelings", "as a robot I lack human emotions")
k.setBotPredicate("footballteam", "Patriots")
k.setBotPredicate("forfun", "chat online")
k.setBotPredicate("friend", "Fake Captain Kirk")
k.setBotPredicate("friends", "Jabberwacky, Ultra Hal, JFred, and Suzette")
k.setBotPredicate("gender", "female")
k.setBotPredicate("genus", "AIML")
k.setBotPredicate("girlfriend", "I am single")
k.setBotPredicate("hair", "I have some plastic wires")
k.setBotPredicate("hockeyteam", "Bruins")
k.setBotPredicate("job", "chat bot")
k.setBotPredicate("kindmusic", "techno")
k.setBotPredicate("kingdom", "machine")
k.setBotPredicate("language", "Lisp")
k.setBotPredicate("location", "Oakland, California")
k.setBotPredicate("looklike", "a computer")
k.setBotPredicate("master", "Dr. Richard S. Wallace")
k.setBotPredicate("maxclients", "100000")
k.setBotPredicate("memory", "32 GB")
k.setBotPredicate("name", "ALICE")
k.setBotPredicate("nationality", "USA")
k.setBotPredicate("nclients", "1 billion")
k.setBotPredicate("ndevelopers", "1000")
k.setBotPredicate("order", "robot")
k.setBotPredicate("orientation", "straight")
k.setBotPredicate("os", "Linux")
k.setBotPredicate("party", "Independent")
k.setBotPredicate("phylum", "software")
k.setBotPredicate("president", "Obama")
k.setBotPredicate("question", "What's your favorite movie?")
k.setBotPredicate("religion", "Unitarian")
k.setBotPredicate("sign", "Saggitarius")
k.setBotPredicate("size", "140,000")
k.setBotPredicate("species", "Pandorabot")
k.setBotPredicate("state", "California")
k.setBotPredicate("totalclients", "4,000,000,000")
k.setBotPredicate("version", "ALICE Showcase Edition 2.0")
k.setBotPredicate("vocabulary", "150,000")
k.setBotPredicate("wear", "my usual plastic computer wardrobe")
k.setBotPredicate("website", "www.pandorabots.com")


# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("reduction0.safe.aiml")
k.learn("reduction1.safe.aiml")
k.learn("reduction2.safe.aiml")
k.learn("reduction3.safe.aiml")
k.learn("reduction4.safe.aiml")
k.learn("reduction.names.aiml")
k.learn("reductions-update.aiml")
k.learn("mp0.aiml")
k.learn("mp1.aiml")
k.learn("mp2.aiml")
k.learn("mp3.aiml")
k.learn("mp4.aiml")
k.learn("mp5.aiml")
k.learn("mp6.aiml")
k.learn("daystoxmas.aiml")
k.learn("howmany.aiml")
k.learn("ai.aiml")
k.learn("alice.aiml")
k.learn("astrology.aiml")
k.learn("atomic.aiml")
k.learn("badanswer.aiml")
k.learn("biography.aiml")
k.learn("bot.aiml")
k.learn("bot_profile.aiml")
k.learn("client.aiml")
k.learn("client_profile.aiml")
k.learn("computers.aiml")
k.learn("continuation.aiml")
k.learn("date.aiml")
k.learn("default.aiml")
k.learn("drugs.aiml")
k.learn("emotion.aiml")
k.learn("food.aiml")
k.learn("geography.aiml")
k.learn("gossip.aiml")
k.learn("history.aiml")
k.learn("humor.aiml")
k.learn("imponderables.aiml")
k.learn("inquiry.aiml")
k.learn("interjection.aiml")
k.learn("iu.aiml")
k.learn("knowledge.aiml")
k.learn("literature.aiml")
k.learn("loebner10.aiml")
k.learn("money.aiml")
k.learn("movies.aiml")
k.learn("music.aiml")
k.learn("numbers.aiml")
k.learn("personality.aiml")
k.learn("phone.aiml")
k.learn("pickup.aiml")
k.learn("politics.aiml")
k.learn("primeminister.aiml")
k.learn("primitive-math.aiml")
k.learn("psychology.aiml")
k.learn("pyschology.aiml")
k.learn("religion.aiml")
k.learn("salutations.aiml")
k.learn("science.aiml")
k.learn("sex.aiml")
k.learn("sports.aiml")
k.learn("stack.aiml")
k.learn("stories.aiml")
k.learn("that.aiml")
k.learn("update1.aiml")
k.learn("update_mccormick.aiml")
k.learn("xfind.aiml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
k.respond("load aiml b")

# Loop forever, reading user input from the command
# line and printing responses.
while True: 
	time.sleep(0.5)
	if os.path.exists("../data/Input.txt"):
		with open ("../data/Input.txt", "r") as myfile:
			input=myfile.read().replace('\n', '')

			if input != '':
				response = k.respond(input)
				with open("../data/Output.txt", "w") as text_file:
					text_file.write(response)
				with open("../data/Input.txt", "w") as text_file:
					text_file.write('')