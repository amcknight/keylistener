# keylistener

Hacked together for one-time use fighting GPW2 Bowser but thought I might need something similar one day.

Requires a google `service-account-credentials.json` file similar to `service-account-credentials.example.json` but with all fields filled. I think this is a file I copied on google cloud rather than something you want to fill in manually, but I forget. The key mapping and google sheets title are at the bottom of `listener.py` so that's where I'd start messing with things. Data is entered in a starting cell and then just keeps being entered down that column. Aggregations and graphs need to be built manually in your sheet.
