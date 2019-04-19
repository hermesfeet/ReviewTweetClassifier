'''This script defines a baseline model using logistic regression to compare other models to.
We vectorize the words into simple numbers using a bag of words model and run the logistic regression classifier.'''


from sklearn.model_selection import train_test_split
from examine_data import filepath_dict, df, df_list
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


#Split Yelp data into train and test sets
df_yelp = df[df['source'] == 'yelp']
sentences = df_yelp['sentence'].values
y = df_yelp['label'].values
sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)


#Vectorize all data - we stack vectors of word counts, and each vector was the same length
# (the size of the total corpus vocabulary).
vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test = vectorizer.transform(sentences_test)
X_train


#Run classifer on Yelp data and show accuracy on test vs train
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)

#print("Accuracy for Yelp only:  ", score)


#Score all 3 datasets

def show_scikit_score():
    for source in df['source'].unique():
        df_source = df[df['source'] == source]
        sentences = df_source['sentence'].values
        y = df_source['label'].values

        sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

        vectorizer = CountVectorizer()
        vectorizer.fit(sentences_train)
        X_train = vectorizer.transform(sentences_train)
        X_test = vectorizer.transform(sentences_test)
        X_train

        # Run classifer on all data and show accuracy on test vs train
        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)
        score = classifier.score(X_test, y_test)

        print("Accuracy for {} data:   {:.4f}".format(source, score))

#show_scikit_score()