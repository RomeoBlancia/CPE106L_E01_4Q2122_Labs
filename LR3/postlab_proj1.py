class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __init__(self,name):
        self.name=name
    def __eq__(self,s2):
        if self.name==s2.name:
            return True
        else:
            return False
    def __lt__(self,s2):
        if len(self.name)<len(s2.name):
            return True
        else:
            return False
    def __ge__(self,s2):
        if len(self.name)>=len(s2.name):
            return True
        else:
            return False
def main():
    """A simple test."""
    student = Student("Ken", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

def main():
    s1=Student("Ken")
    s2=Student("Kang")
    print(s1==s2)
    print(s1<s2)
    print(s1>=s2)
if __name__=='__main__':
    main()
    