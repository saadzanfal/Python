Implement a phrase trigger (PhraseTrigger) that fires when a given phrase is in any of the story's subject, title, or summary. The phrase should be an argument to the class's constructor. You may find the Python operator in helpful, as in:

>>> print "New York City" in "In the heart of New York City's famous cafe"
True
>>> print "New York City" in "I love new york city"
False
When this is done, the PhraseTrigger unit tests should pass.