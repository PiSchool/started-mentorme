import pickle
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tqdm.auto import tqdm
tqdm.pandas()
import pandas as pd
from feature_extractor import extractFeature
from text_functions import *
from feature_union_transformer import *

# List of URL + CLASS + HTML_CODE
df_pkl_path = 'toy_started_dataset_df.pkl'
df = pd.read_pickle(df_pkl_path)
print(df.kind.value_counts())

documents = []
print('Extracting features from HTML')
with tqdm(total=df.count()[0]) as pbar:
    for i, row in df.iterrows():
        pbar.update(1)
        _, ic, im, text = extractFeature(row['html'])
        documents.append((ic, im, text))

cdf = pd.DataFrame(documents, columns=['input_count', 'img_count', 'text'])
cdf.reset_index(drop=True, inplace=True)
df.reset_index(drop=True, inplace=True)
df = pd.concat([df,cdf], axis=1)

print('\n Processing extracted text')
df['polarity']      = df['text'].progress_map(polarity_txt)
df['subjectivity']  = df['text'].progress_map(subj_txt)
df['len']           = df['text'].progress_map(len_text)

# Dataset split
seed = 42
X = df[['text', 'img_count', 'input_count', 'polarity', 'subjectivity','len']]
y =df['kind']
encoder = LabelEncoder()
y = encoder.fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

pipeline = Pipeline([
    ('union', FeatureUnion(
        transformer_list=[
            # Pipeline for pulling features from the text
            ('text', Pipeline([
                ('selector', ItemSelector(key='text')),
                ('tfidf', TfidfVectorizer( min_df =3, max_df=0.2, max_features=None,
                    strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
                    ngram_range=(1, 10), use_idf=1,smooth_idf=1,sublinear_tf=1,
                    stop_words = None, preprocessor=clean_txt)),
            ])),
            # Pipeline for pulling metadata features
            ('stats', Pipeline([
                ('selector', ItemSelector(key=['img_count','input_count', 'polarity', 'subjectivity', 'len'])),
                ('stats', PageStats()),  # returns a list of dicts
                ('vect', DictVectorizer()),  # list of dicts -> feature matrix
            ])),
        ],
        # weight components in FeatureUnion
        transformer_weights={
            'text': 1.2,
            'stats': 0.9
        },
    ))
])

pipeline.fit(x_train)
train_vec = pipeline.transform(x_train)
test_vec = pipeline.transform(x_test)

clf_lr = LogisticRegression(solver = 'lbfgs', max_iter=10000, random_state = 42)
clf_lr.fit(train_vec, y_train)
y_pred = clf_lr.predict(test_vec)
acc = accuracy_score(y_test, y_pred)
print(f'LR \t : {acc}')

with open('pipeline.pkl', 'wb+') as output: pickle.dump(pipeline, output)
with open('clf.pkl', 'wb+') as output: pickle.dump(clf_lr, output)
