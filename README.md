# keylistener

Hacked together for one-time use fighting GPW2 Bowser but thought I might need something similar one day.

## Installation and Set up

Git clone, Install python3, and install pipenv.

Requires a google `service-account-credentials.json` file similar to `service-account-credentials.example.json` but with all fields filled. I think this is a file I copied from google cloud rather than something you want to fill in manually, but I forget. The key mapping and google sheets title are at the bottom of `listener.py` so that's where I'd start messing with things. Data is entered in a starting cell and then just keeps being entered down that column. It is hardcoded to start in column A of sheet 1 but could easily be modified.

Aggregations and graphs need to be built manually in your sheet. An example google sheet with aggregations and a progress chart can be copied [from here](https://docs.google.com/spreadsheets/d/1kVMXamBKYXcnh9wLZPw3JM059vVy0bT6Q-RW8XaJf1o/edit?usp=sharing).

You'll also need to give your service account Editor access to your google sheet by sharing it with them. I got an email for this that looked like `BLAH-service-account@BLAH-NUMBER.iam.gserviceaccount.com`. Sorry, I don't remember exactly how I set this up either.

Good luck! :/

## Running it

`sudo pipenv run python3 listener.py`

sudo is required for the `keyboard` library for some reason.

## Roadmap
### v1
- Use argsparse to ask for:
  - number of phases
  - keymapping file
  - google sheet name
  - initial attempt #
  - cell of the first attempt
  - maybe to input the keymapping itself
- Allow for the keymapping to be specified from a file
- Generate the Sheet from the CLI
- Link to or create better google cloud service account instructions

### Beyond
- Re-do the whole thing as a cool website instead of a janky google sheet
