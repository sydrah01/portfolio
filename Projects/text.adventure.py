start = '''
You are travelling to London for a (lonely) vacation. You arrive at the airport 
and smell the tangy smell of jet fuel sniff sniff...
You need to get to your gate and not miss your flight.
'''
print(start)

print("You have to pee... but you also need to check your bags. Will you go to the bathroom first or check your bags? Type 'bathroom' or 'bags'")
user_input = input()
if user_input == "bags":
	print("You successfully check your bags and go pee.")
	print("After that, you see that you have some time before the flight. Will you go to the giftshop or get some food? Type 'food' or 'giftshop'")
	user_input = input()
	if user_input == "food":
		print('''You order a burger... Its the best burger you've ever had in your life...You hear a voice on the intercom saying your name... 
		you look at your watch and realize that you have two minuets to be on the plane...
		you lost track of time enjoying that darn burger. You know that you'll never make it in time so you take one last bite of your burger symoblizing your defeat.''')
	if user_input == "giftshop":
		print('''You are fufilling all your shopping needs and desires when your eyes skim the wall. You've been shopping for 2 hours. Your heart skips a beat as you realize that
		your flight is long gone. 'CURSE YOU AIRPORT GIFTSHOP!!!' you think to yourself... you leave the airport in defeat with 5 shopping bags hanging from you.''')
if user_input == "bathroom":
	print('''You go to the bathroom but someone took your bags when you turned your back. You rush out of the bathroom without washing your hands. People scold you for doing so as
	you try to get a glimpse of the culprit. Your two options are to chase after him or start screaming for security. Type 'chase' or 'scream''') 
	if user_input == "chase":
		print('''You chase after him. You pat yourself on the back for going running every morning for the past two weeks. Your footsteps echo in the thiefs ears, making him go faster...
 		you let out a quite 'zoomzoom' as you gain on him and snag your bags back from him with a confident smirk. He sprints away. You look around and realize you have no idea where you are 
 		in this huge airport but get a glimps of gate 1111. You squeel with delight as you run over to your gate just in time!!! You give the checker guy your ticket and says
 		'scuse me sir, this ain't ur flight m8. This is gate 1111 not 111'...''')


print('''Two days after your defeat, you sulk on the couch watching Netflix...alone...and decide to switch to the news channel. 
'Flight 111 to London never arrived at the airport yesterday. However, the aircraft was found in the Australian desert due to the captains desire to see some kangaroos.' THE END''')