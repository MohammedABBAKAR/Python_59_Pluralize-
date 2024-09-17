
#  todo Pluralize!

# ? Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
# * Examples

# *pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

# *pluralize(["table", "table", "table"]) ➞ { "tables" }

# *pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

#! Notes

#    ! This is an oversimplification of the English language so no edge cases will appear.
#    ! Only focus on whether or not to add an s to the ends of words.
#     ! All tests will be valid



def pluralize(lst):
    lst2 =set()
    for x in lst:
     
        y = lst.count(x)
        if y > 1:
          lst2.add(x+"s")
        else:
           lst2.add(x)
    return lst2
print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))







def pluralize(words):
    word_count = {}  # Dictionary to count occurrences of each word
    result = set()   # Set to store the final pluralized or singular words

    # Count occurrences of each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Add the pluralized or singular form to the result set
    for word, count in word_count.items():
        if count > 1:
            result.add(word + 's')  # Pluralize the word
        else:
            result.add(word)  # Keep the word in singular form

    return result

# Test cases
print(pluralize(["cow", "pig", "cow", "cow"]))  # ➞ {"cows", "pig"}
print(pluralize(["table", "table", "table"]))  # ➞ {"tables"}
print(pluralize(["chair", "pencil", "arm"]))  # ➞ {"chair", "pencil", "arm"}
