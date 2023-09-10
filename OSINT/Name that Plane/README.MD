# Name that Plane

### Description

Time to identify some not so UFOs. I'd like you to identify the aircraft in the zoomed in picture and the airport it was photographed at. 

Flag Format: PCTF{NameOfPlane_IATAcodeForAirport}

The name of the plane should include its number ex:

If your plane is the Siebel Si 201:

Siebel_Si_201

An IATA code for an airport looks like this:
Name: Ronald Reagan Washington National Airport
IATA Code: DCA

### Difficulty
5/10 (Medium)

### Flag
PCTF{Cessna_208_Caravan_HEA}
PCTF{Cessna_208_HEA}
PCTF{AC_208_HEA}

### Hints
None

### Author
Migyaksuil (Maxime Bonnaud)

### Tester
Txnn3r (Tanner Leventry)

### Learning objective
Sometimes an image is just hard to locate. The airfield in this image is especially generic and could be anywhere in the Middle East. This is where learning to fingerprint: or gather general information about a vehicle, even if you can't stricly identify it, can come in handy. You can then use the fingerprint to lower the search radius down to Afghanistan and from there get a positive ID on the Cessna from the Afghan Air Force wiki page.

### Writeup

If you do some reverse image searching, you should find the airport to be somewhere in the Middle East. Using the shape of the plane provided (it looks American and military), you can eliminate several countries from the potential list and end up with Afghanistan. Searching for what aircraft they operate should yield a Cessna 208 as one of the results. It is then just a matter of looking at the major airports in Afghanistan to see if their profile matches the provided image.
