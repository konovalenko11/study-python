import exvar as exvar

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


# remove punctuation
def strip_punctuation(text):
    for char in punctuation_chars:
        text = text.replace(char, '')

    return text


# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

positive_words_dict = {word: 0 for word in positive_words}


def get_pos(text):
    pwords = 0
    for word in text.split():
        if strip_punctuation(word) in positive_words_dict:
            pwords += 1
    return pwords


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

negative_words_dict = {word: 0 for word in negative_words}


def get_neg(text):
    nwords = 0
    for word in text.split():
        if strip_punctuation(word) in negative_words_dict:
            nwords += 1
    return nwords


def func1(text: exvar):
    return text


tw_data = open("project_twitter_data.csv", "r")
result_data = open("resulting_data.csv", "w")

line_num = 0
for line in tw_data:
    line_num += 1

    if line_num == 1:
        result_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
        continue

    line_str = line.strip()
    tw_text, tw_retweets, tw_replies = line_str.split(',')
    tw_pscore = get_pos(tw_text)
    tw_nscore = get_neg(tw_text)
    tw_net_score = tw_pscore - tw_nscore
    print("=====\n" + line_str)
    print("Tweet: [{}];\nRetweets: [{}];\nReplies: [{}]".format(
        tw_text, tw_retweets, tw_replies))
    print("P Score: [{}];\nN Score: [{}];\nNet Score: [{}]".format(
        tw_pscore, tw_nscore, tw_net_score))

    result_data_line = "{},{},{},{},{}\n".format(
        tw_retweets, tw_replies, tw_pscore, tw_nscore, tw_net_score)

    result_data.write(result_data_line)

tw_data.close
result_data.close
