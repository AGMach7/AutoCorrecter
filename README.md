# Auto-Correction Program

This program suggests possible spelling corrections for input words based on a given text corpus.

## Getting Started
To get started with this program, you will need to clone this repository to your local machine:
```
git clone https://github.com/AGMach7/AutoCorrecter.git
```

## Prerequisites
This program requires Python 3 and the following libraries:
- tkinter
- re
- collections

These can be installed using pip:
```
pip install tkinter collections re
```

## Project Structure
The project contains the following files and folders:

- data/ This folder contains the unprocessed data used to train the model.
  - shakespeare.txt: This file contains the unprocessed data to generate the spelling suggestions.
- src/: This folder contains the source code for the project.
  - data_preprocessing.py: This module contains functions for processing and cleaning the input data.
  - string_manipulation.py: This module contains functions for manipulating strings.
  - edite_letters.py: This module contains functions for generating all possible words that are one or two edits away from a given word.
  - spelling_suggestions.py: This module contains functions for generating spelling suggestions.
  - app.py: This module contains the code for the user interface.
- README.md: This file provides information about the project.

## Running the Program
To run the program, navigate to the main directory and run the following command:
```
python app.py
```

You can specify the number of suggested corrections to display by entering a number in the "Number of suggestions" field. By default, the program will display 5 suggestions.

Enter a word in the "Enter a word" field and click the "Correct" button to see a list of suggested corrections.

## Acknowledgments
This program was inspired by the work of Younes Bensouda and his cours on NLP Specialization (the first assignment of Course 2): https://www.coursera.org/specializations/natural-language-processing.
