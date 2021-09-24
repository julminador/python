def run():
    palindrome = lambda word: word == word[::-1]
    print(palindrome('ana'))


if __name__ == '__main__':
    run()