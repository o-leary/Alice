# Alice
**A module for [Anjelica](https://github.com/o-leary/Anjelica) to integrate [A.L.I.C.E AIML bot](http://www.alicebot.org/downloads/sets.html)**

## Features
Anjelica will respond to any typed message, sending a response to the users channel prefixed with "@username:". By customising the AIML files for A.L.I.C.E you can create your own persona with remarkable intelligence.

## How to install
1. Install [Anjelica](https://github.com/o-leary/Anjelica).
2. Install PyAIML `sudo apt-get install python-aiml`.
3. Download this repo into Anjelicas modules directory in a folder called "alice".
4. Add 'alice' to Anjelicas modules.lua file.
5. Edit any settings in modules/alice/includes/alice.py such as name and botmaster.
6. Run `python alice.py` from within the modules/alice/includes folder, then start anjelica as usual.

## Thanks
Special thanks to [A.L.I.C.E. AI Foundation, Inc](http://www.alicebot.org/downloads/sets.html) for creating the A.L.I.C.E. bot and providing the AIML files under an LGPL license.

## License
```
GNU LESSER GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

See LICENCE file.
```