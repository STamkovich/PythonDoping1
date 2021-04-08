# завести список который будет состоять из слов
# words = ["apple", "banana", "grape", " some other word", "stop", "hello", "goodbye"]
# цыкл должен остановитсья посл етого как увидит слово "stop" и остальные слова после него
words = ["apple", "banana", "grape", "some other word", "stop", "hello", "goodbye"]
i = 0
while words[i] != "stop":
    print(words[i])
    i += 1

for i in range(len(words)):
    if words[i] == "stop":
        break
    print(words[i])

# apple
# banana
# grape
# some other word
# apple
# banana
# grape
# some other word
