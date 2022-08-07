#objective
import string
import random
from graph import Graph, Vertex


def get_words_from_texts(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        text = ' '.join(text.split()) # turn whitespace into just space
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    #for each word in word
    #check if in it, if not, add it
    #if previous word, add edge
    #increment weigt by 1
    # set our word to the prvious word and iterate
    # probability mapping before composing

    for word in words:
        word_vertex = g.get_vertex(word)

        if prev_word:
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()

    return g


def compose(g, words, length=50):

    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition



def main():

#1: get words from text
    words = get_words_from_texts('finnegans_wake.txt')
#2: make a graph from those words
    g = make_graph(words)
#3: get the next word for n number of words (defined by user)

#4 display results
    composition = compose(g, words, 100)
    return ' '.join(composition)

if __name__ == '__main__':

    print(main())


