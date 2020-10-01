def word_count(s):
    # Your code here
    cache = {}

    # word filter
    ignored_words = ['"', ":", ",", ";", ".", "-", "+", "=", "/",
                     "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\\"]

    # convert to lower case
    word = s.lower()

    for x in ignored_words:
        word = word.replace(str(x), '')

    # creating a list with each word separated
    word = word.split()

    for i in word:
        # if idx isn't in cache add it
        if i not in cache:
            cache[i] = 1
        # if it's there, add 1 to the counter
        else:
            cache[i] += 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
