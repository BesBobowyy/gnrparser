# GNR PARSER #
Library for parsing a .gnr files and operate with parsed data.

gnrparser.read(data: str) - Returns readed data from file content.
gnrparser.analyze(data: dict) - Recieves parsed data and returns normalized data with all fields and autocompletions.

GNR files have this structure (Version 1):
[Version: <INTEGER>] - Version of format.
[Game: <STRING>] - Name of the game.
[P<INT>: <STRING>] - Index and name of player. Format hasn't any limit for players count.
[Variation: <STRING>] - Name of the game variation.
[Termination: <STRING>] - How the game ended, write "null" if game in process.
[Date: <STRING>] - When game playing.
[Field Size: <LIST[INT, INT]>] - Size of the field.
[Time Limit: <STRING>] - Time limit in format: BASE+ADD, BASE or null if game hasn't time limit.
[Organization: <STRING>] - The game place.
[Start Position: <STRING>] - Unique formatting for the game start position.
1. <MOVES> 2. <MOVES> 3. ... - Unique formatting for the game moves.

# How to install #
1. Install the package.
```pip install gnrparser```

2. Import the package.
```import gnrparser```

3. Use library functions.
```gnrparser.read()
gnrparser.analyze()```

Author: BesBobowyy (2025)