import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

def testInput(userInput):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % userInput)
    results = cursor.fetchall()
    
    if results:
        return results
    else:
        return testSimilar(userInput)

def testSimilar(userInput):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '%s'" % (userInput[0] + "%"))
    results = cursor.fetchall()
    
    if len(get_close_matches(userInput, [item[0] for item in results], cutoff=0.8)) > 0:
        similarWord = get_close_matches(userInput, [item[0] for item in results], n=1, cutoff=0.8)[0]
        yn = input("Did you mean %s instead? y/n " % similarWord).lower()
        if yn == "y":
            return testInput(similarWord)
        elif yn == 'n':
            return "Word not found."
        else:
            return "Invalid response."  
    else:
        return "Word not found."

word = input("Please enter a word: ")
output = testInput(word)
    
if type(output) == list:
    for item in output:
        print(item[1])
else:
    print(output)
