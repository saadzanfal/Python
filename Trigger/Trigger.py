# Enter your code for WordTrigger, TitleTrigger,

class WordTrigger(Trigger):
    #take in a word as our "trigger"
    def  __init__(self, word):
        self.word = word
    
    def is_word_in(self, text):
        #make list of words split at spaces and other punctuation
        textlist = text.split(' ')
        for punc in string.punctuation:
            for i in textlist:
                if punc in i:
                    textlist.extend(i.split(punc))
                    textlist.remove(i)
        #check if our trigger is in the list
        if self.word in textlist:
            return True
        else:
            return False

class TitleTrigger(WordTrigger):
    #make a WordTrigger
    def __init__(self, word):
        WordTrigger.__init__(self, word.lower())

    #use WordTrigger's is_word_in function on story's title
    def evaluate(self, story):
        title = story.title.lower()
        return WordTrigger.is_word_in(self, title)
    
class SubjectTrigger(WordTrigger):
    #make a WordTrigger
    def __init__(self, word):
        WordTrigger.__init__(self, word.lower())

    #use WordTrigger's is_word_in function on story's subject
    def evaluate(self, story):
        subject = story.subject.lower()
        return WordTrigger.is_word_in(self, subject)


class SummaryTrigger(WordTrigger):
    #make a WordTrigger
    def __init__(self, word):
        WordTrigger.__init__(self, word.lower())

    #use WordTrigger's is_word_in function on story's subject        
    def evaluate(self, story):
        summary = story.summary.lower()
        return WordTrigger.is_word_in(self, summary)

# SubjectTrigger, SummaryTrigger, and PhraseTrigger in this box
class PhraseTrigger(Trigger):
    #take in a string
    def __init__(self, phrase):
        self.phrase = phrase

    #is_phrase_in will check if that string is anywhere in the string 'text'
    def is_phrase_in(self, text):
        if self.phrase in text:
            return True
        else:
            return False

    #check title, subject, AND summary for our phrase
    def evaluate(self, story):
        return self.is_phrase_in(story.title) or self.is_phrase_in(story.subject) or self.is_phrase_in(story.summary)


