# Word Embeddings

**_Word embeddings_** is one of the most used techniques in natural language processing (NLP).
It's often said that the performance and ability of State-of-the-art (SOTA) models wouldn't have been possible without
word embeddings.
It's precisely because of word embeddings that language models like RNNs, LSTMs, ELMo, BERT, AlBERT, GPT-2 and GPT-3
have evolved at a staggering pace.

These algorithms are fast and can generate language sequences and other downstream tasks with high accuracy, including
**contextual understanding**, **semantic and syntactic properties**, as well as the **linear relationship** between words.

At the core, these models use embedding as a method to extract patterns from text or voice sequences.

## What are word embeddings?
Word embeddings are a way to represent words and whole sentences in a numerical manner. We know that computers understand
the language of numbers, so we try to encode words in a sentence to numbers such that the computer can read it and
process it.

But reading and processing are not the only things that we want computers to do. We also want computers to build a
relationship between each word in a sentence, or document with the other words in the same.

We want word embeddings to capture the context of the paragraph or previous sentences along with capturing the semantic 
and syntactic properties and similarities of the same.

For instance, if we take a sentence: \
"The cat is lying on the floor and the dog was eating", \
then we can take the two subjects (cat and dog) and switch them in the sentence making it: \
"The dog is lying on the floor and the cat was eating." \
In both sentences, the semantic or meaning-related relationship is preserved, i.e. cat and dog are animals. And the
sentence makes sense.

Similarly, the sentence also perserved syntactic relationship, i.e. rule-based relationship or grammar.

In order to achieve that kind of semantic and syntactic relationship we need to demand more than just mapping a word in
a sentence or document to mere numbers. We need a larger representation of those numbers that can represent that can
represent both **_semantic and syntactic_** properties.

We need vectors. Not only that, but **_learnable_** vectors.

A lot of people also define word embedding as a dense represenation of words in the form of vectors.

For instance, the word cat and dog can be represented as:
* W(cat) = (0.9, 0.1, 0.3, -0.23, ...)
* W(dog) = (0.76, 0.1, -0.38, 0.3, ...)

Now, hypothetically speaking, if the model is able to preserve the contextual similarity, then both words will be close 
in a vector space.

So far we've dealt with two words (cat and dog), but what if there are more words?
The job of word embedding model is to cluster similar information and establish a relationship between them.

There are a lot of shallow algorithms present that work well for clustering. Why do we need neural networks?

One of the biggest misconceptions is that word embeddings require deep neural networks. As we build different word
embedding models, we will see that for all the embeddings, the model is a shallow neural network, and some are linear
models as well.

The reasons we use neural networks to create word embeddings are:
1. It's useful in finding nearest neighbors in the embedding space.
2. It can be used as an input to supervised learning tasks.
3. It creates a mapping of discrete variables, such as words to a vector, of continuous variables.
4. It also tackles the curse of dimensionality.

### What is shallow algorithm?
Shallow learning, also known as shallow machine learning or traditional machine learning, refers to a class of machine
learning algorithms that typically involve a single layer of data transformation and learning. Unlike deep learning models,
which are composed of multiple layers of interconnceted nodes, shallow learning models have a simpler structure and are
easier to interpret and understand.

Shallow learning algorithms aim to find patterns and relationships in the input data to make predictions or decisions.
These algorithms often rely on handcrafted features extracted from the data and utilize simple mathematical models for
learning and inference.

## Neural Language Model
Word embeddings were proposed to tackle what's known as the curse of dimensionality, a common problem in statistical 
langauge modeling.

It turns out that the method could train a neural network such that each training sentence could inform the model about
a number of semantically available neighboring words, which was known as distributed **_representation of words_**. \
The neural network not established relationships between different words, but also it preserved relationships in terms
of both **_semantic and syntactic properties_**.

This introduces a neural network architecture approach that laid the foundation for many current approaches. \
This neural network has 3 components:
1. An **embedding layer** that generates word embedding, and the parameters are shared across words.
2. A **hidden layer** of one or more layers, which intoduced non-linearity to the embeddings.
3. A **softmax function** that produces probability distribution over all the words in the vocabulary.
