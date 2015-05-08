class NewsStory(object):


    #initialize a NewsStory by setting its traits to the values given by the parser
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    #provide functions to access the information we just saved
    def getGuid(self):
        return self.guid
    
    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link

