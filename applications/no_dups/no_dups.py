def no_dups(s):
    # Your code here

    cache = {}

    # Split the words into a list
    word = s.split()

    for i in word:
        # Add index to the cache
        if i not in cache:
            cache[i] = 1

    # Adding space

    new_word = ' '

    # Joining the items in cache together to form a string

    new_word = new_word.join(cache)

    return new_word


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
