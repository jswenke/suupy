# suupy
suupy by vid_

NOTE: if you're here from my linkedin profile this is what is referred to on my resume as "Automated Clothing Purchase Web Browser Utility" and was written in the summer of 2017 

some background information:
this was my first little project in python that I worked on for a bit after learning the very basics of python for a month or two after graduating highschool.
the code isn't anything special it's here more or less for nostalgia's sake and to have something to compare where I'm at and where I'll be in five or ten years I guess.
might come back to it, might not, we'll see

managed to make a very crude login screen and window after where you can fill out size, address, credit card information, and what item you want to buy
(only managed to do complete the code for a single item cart and checkout). this was followed by searching the website by xpath or name for the item 
and the whole process was pretty inefficient. the site navigation used selenium for chrome and I think I used a combination of pyautogui and selenium
sendkeys for entering the information. supreme was changing the checkout process a lot at the time to deal with bots and it started to confuse me 
why certain things would work and not work so the code for sending keys is especially ugly since I didn't have a solid foundation of knowledge to work 
off of at the time. I don't really care if someone stumbles across this and repurposes it but you're probably better off starting from scratch lol
