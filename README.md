# Reviews and Tweets Classifier
Some different simple ways (binary classifiers to neural nets) to classify bited-sized reviews and tweets as positive or negative

## What It Does
- **Goal**:  Given an input of a short string of text (under 200 characters), classify the sentiment as positive or negative
- **Results**:  Gives results with 80% accuracy from datasets such as Yelp reviews, tweets, and Amazon reviews

## Examples of data
                                            sentence  label source
0                           Wow... Loved this place.      1   yelp
1                                 Crust is not good.      0   yelp
2          Not tasty and the texture was just nasty.      0   yelp
3  Stopped by during the late May bank holiday of...      1   yelp
4  The selection on the menu was great and so wer...      1   yelp
211  If you hate earbugs, avoid this phone by all m...      0  amazon
212                                  Great price also!      1  amazon
213  The range is very decent, I've been able to ro...      1  amazon
214                                      fast service.      1  amazon
215                     I would highly recommend this.      1  amazon


### 1) Datasets and labelling + Baseline results
- **How it Works**: Started with three datasets from Yelp, Amazon, and IMDB, labelled with 1s and 0s are positive and negative
- **Summary of data / baseline model**:  2748 examples.  Baseline model uses Scikit for a binary classifier after doing a simple vector transform.  
Accuracy for yelp data:   0.7960
Accuracy for amazon data:   0.7960
Accuracy for imdb data:   0.7487

### 2) Neural net results
- **Simple Keras Model**:  2 layers, a simple 10 dimensional relu hidden layer, and an output sigmoid (loss is binary cross-entropy, adam optimizer, 40 epochs).
Training Accuracy:  1.0000
Testing Accuracy:  0.8080
- **Deeper Keras Model with Word Embeddings**:  Created new word embeddings with the size of the vocabular at 5000 words and 50 dimensions, with a max length of 100 and some padding.

## Running the different tools
`$ python gensim_summary.py`

`$ python textteaser_summary.py`

`cd nltk_summary | python nltk_summary.py airline.txt`

## Built With / Dependencies
Built in Python 3.6. See the Requirements.txt file.
Mostly Gensim, TextTeaser, Numpy, Scipy, NLTK.

## Versioning
Version 1.1.

## Dev Timeline - Next To Do
- Test on on other data
- Add Neural network

## License
This project is licensed under the MIT License.

Copyright 2019 - HermesFeet

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Appendix - Corpora to Check Out
- [awesome-text-summarization](https://github.com/icoxfog417/awesome-text-summarization)
- [Gensim Text Summarization](https://radimrehurek.com/gensim/summarization/summariser.html)
- [Summarizer from Scratch](https://towardsdatascience.com/write-a-simple-summarizer-in-python-e9ca6138a08e)
- [Unsupervised text summarization using embeddings](https://medium.com/jatana/unsupervised-text-summarization-using-sentence-embeddings-adb15ce83db1)
- [Sequence-to-Sequence with Attention Model for Text Summarization](https://github.com/tensorflow/models/tree/master/research/textsum)

