def print_upper_words(words):
    """Print each word from a given list on a separate line
        Each word should be uppercased
        
        >>> print_upper_words(["hello", "goodbye", "dog", "cat"])
        HELLO
        GOODBYE
        DOG
        CAT
    """
    for word in words:
        print(word.upper())
    
def print_upper_words_v2(words):
    """Print each word from a given list that starts with 'e' or 'E' on a separate line
        Each word should be uppercased
        
        >>> print_upper_words_v2(["earthling", "eagle", "excellent", "cat"])
        EARTHLING
        EAGLE
        EXCELLENT
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())
    

def print_upper_words_v3(words, starts_with):
    """Print each word from a given list on a separate line that starts with the letter given
        Each word should be uppercased
        
        >>> print_upper_words(["hello", "goodbye", "dog", "cat"], starts_with=["H", "C"])
        HELLO
        CAT
    """
    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())
                break