PROBLEM 1

Parsing is the process of turning a data stream into a structured format that is more convenient to work with. We have provided you with code that will retrieve and parse the Google and Yahoo news feeds.

Parsing all of this information from the feeds that Google/Yahoo/the New York Times/etc. gives us is no small feat. So, let's tackle an easy part of the problem first: Pretend that someone has already done the specific parsing, and has left you with variables that contain the following information for a news story:

globally unique identifier (GUID) - a string that serves as a unique name for this entry

title - a string

subject - a string

summary - a string

link to more content - a string

We want to store this information in an object that we can then pass around in the rest of our program. Your task, in this problem, is to write a class, NewsStory, starting with a constructor that takes (guid, title, subject, summary, link) as arguments and stores them appropriately. NewsStory also needs to contain the following methods:

getGuid(self)
getTitle(self)
getSubject(self)
getSummary(self)
getLink(self)
Each method should return the apprpriate element of an instance. For example, if we have implemented the class and call