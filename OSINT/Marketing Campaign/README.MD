# Marketing Campaign

### Description

Greetings analyst! As you know, our recent attempts to acquire a very lucrative contract failed when our customer decided to go with a Swedish competitor instead. Unfortunately, the SkyTractor-9000 and its munition the VFFR (Very Fast Flying Rock, accurate to within a 1m2 by 1m2 zone!) were very expensive to develop and build, and we only ended up building one SkyTractor-9000 and 3 VFFRs. Thankfully, we have a plan to ...convince our customer to reconsider the contract and get more money to build more. This is where you come in.  

We need you to find the location of the aircraft in the rightmost part of the photo (the one between 06 and 05). Don't give us latitude and longitude, we need a form of geolocation more precise and reliable than that for our needs. Try to get your location right on the yellow line in the middle. Our pilot will handle the rest from there. Good luck!

### Difficulty
5/10 (Medium)

### Flag
PCTF{headache.workshop.savings}

### Hints
The word workshop should appear in your answer (don't forget to wrap it in PCTF{}!)

### Author
Migyaksuil (Maxime Bonnaud)

### Tester
None

### Learning objective
The goal was to teach how to identify military aircraft by a rough profile and nation of origin and then use that knowledge to locate the airbases that operate them. If done correctly, there should be very little manual checking on Google Maps/Earth involved. The secondary goal was to teach about geolocation methods that are accurate to 1 meter and easy to transmit. Latitude and Longitude can be accurate to within 1m, but a simple error copying them down can through the whole location off (which is easy to do since it is a lot of numbers), it also takes a while to transmit over a radio. The same is true for MGRS. What3words is a system that allows for consistent enforcement of accuracy, while also being super easy to transmit (it is quite literally 3 words). In fact, what3words is used by multiple UK and French rescue teams as their preferred method of locating individuals.

### Writeup

Reverse image the image and find something about Eastern Europe airfields. Using the description and some google searching, we can find the plane to be the Gripen C. This plane is only operated in Sweden, Czech Republic, and Hungary. Checking Hungary, we can see that there is only one airfield that has Gripens: Kecskemét Air Base. Now we can use What3words to get a geolocation accurate to within a meter.
