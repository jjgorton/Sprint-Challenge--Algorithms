'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # the simplest and most performant solution:
    # return len(word.split('th'))-1

    word_array = list(word)
    count = 0

    def inner_th(arr, count):
        new_arr = arr
        new_count = count
        if len(new_arr) < 2:
            return new_count
        else:
            if arr[-2] == 't' and arr[-1] == 'h':
                new_count += 1

            new_arr.pop()
            return inner_th(new_arr, new_count)

    return inner_th(word_array, count)


print(count_th('hellowthakdjfkdjfthkdsjfkdj'))
