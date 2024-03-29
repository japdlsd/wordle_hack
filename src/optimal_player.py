import math
import random


def random_selection(viable_words):
    return random.choice(list(viable_words))


def most_reducing(viable_words):
    best_word = ""
    least_average_remaining = math.inf
    for gnum, guess in enumerate(viable_words):
        remaining_total = 0
        for truth in viable_words:
            pattern = eval_pattern(guess, truth)
            for word in viable_words:
                if pattern == eval_pattern(word, truth):
                    remaining_total += 1
        average_remaining = remaining_total / len(viable_words)
        if least_average_remaining > average_remaining:
            best_word = guess
            least_average_remaining = average_remaining
    return best_word


def most_reducing_subsample(viable_words,
                            subsample_truth_count=1,
                            subsample_word_count=100):
    best_word = ""
    least_average_remaining = math.inf
    for gnum, guess in enumerate(viable_words):
        if gnum % 100 == 0:
            print(f"Processing guess #{gnum} {guess}")
        remaining_total = 0
        for truth in random.choices(list(viable_words), k=subsample_truth_count):
            pattern = eval_pattern(guess, truth)
            for word in random.choices(list(viable_words), k=subsample_truth_count):
                if pattern == eval_pattern(word, truth):
                    remaining_total += 1
        average_remaining = remaining_total / (subsample_truth_count)
        if least_average_remaining > average_remaining:
            best_word = guess
            least_average_remaining = average_remaining
    return best_word


def time_optimised(viable_words):
    if len(viable_words) > 500:
        return random_selection(viable_words)
    else:
        return most_reducing(viable_words)


class Player:
    def __init__(self, words, selecting_strategy=random_selection):
        self.words = words
        self.viable_words = set(words)
        self.game_log = []
        self.selecting_strategy = selecting_strategy

    def next_guess(self):
        print(f"Number of viable words left: {len(self.viable_words)}")
        if len(self.viable_words) < 10:
            print(f"Those are viable: {list(self.viable_words)}")
        if len(self.viable_words) > 0:
            result = self.selecting_strategy(self.viable_words)
        else:
            print(f"There are no viable words left!")
            result = ""
        return result

    def add_result(self, guess, result):
        self.game_log.append((guess, result))

        if len(result) == 0:
            # the word is not in the dictionary, just remove it
            self.viable_words.remove(guess)
        else:
            # remove nonviable words
            new_viable_words = []
            for word in self.viable_words:
                if result == eval_pattern(guess, word):
                    new_viable_words.append(word)
            self.viable_words = set(new_viable_words)


def main():
    words_filename = "../data/words5.txt"
    with open(words_filename) as f:
        words = list(load_words(f))

    print(f"Total 5 letters word count: {len(words)}")

    game_log = []
    player = Player(words, selecting_strategy=time_optimised)
    round_num = 0
    while True:
        round_num += 1
        guess = player.next_guess()
        print(f"Player's guess on round #{round_num} is: {guess}")
        result = input("Type the result "
                       "('g' for green, 'y' for yellow, 'w' for grey; "
                       "empty for non-dictionary):")
        game_log.append({'guess': guess, 'result': result})
        player.add_result(guess, result)
        if len(result) == 0:
            print(f"Word not in the dictionary!")
            round_num -= 1
        if result == "ggggg":
            print(f"We have won!")
            break


def load_words(f):
    for line in f:
        word = line.strip()
        yield word


def letter_counts(word):
    result = {}
    for letter in word:
        result[letter] = 1 + result.get(letter, 0)
    return result


def eval_pattern(guess, truth):
    assert len(guess) == len(truth)
    result = ['w' for _ in range(len(guess))]
    guess_letter_count = letter_counts(guess)
    truth_letter_count = letter_counts(truth)

    for i, (g, t) in enumerate(zip(guess, truth)):
        if g == t:
            result[i] = 'g'
            guess_letter_count[g] -= 1
            truth_letter_count[g] -= 1

    for i in range(len(result)):
        if result[i] != 'g' and guess_letter_count[guess[i]] > 0 and truth_letter_count.get(guess[i], 0) > 0:
            result[i] = 'y'
            guess_letter_count[guess[i]] -= 1
            truth_letter_count[guess[i]] -= 1
        else:
            pass  # intentionally
    return "".join(result)


if __name__ == "__main__":
    main()
