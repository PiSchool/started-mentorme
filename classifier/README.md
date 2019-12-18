# STARTUP CLASSIFIER
This folder contains all the files to use the startup classifier and eventually retrain it .
## Requirements
**IMPORTANT:** You need first to download from the Google Drive folder the file `pipeline.pkl` and insert it into this folder. \
You need also python3 installed on your system.
Then you have to run the following command from the classifier directory:
```
pip3 install -r requirements.txt
```
## Use the classifier (Predict)
To use the startup classifier you just need to type the following command from the classifier directory:
```
python3 classifier.py website_url
```
Example:
```
python3 classifier.py https://www.filotrack.com/
```
The script will load the model, and then will output the results:
```
Checking website, please wait...
According to our classifier, your website is a startup!
```

## Train the classifier
**IMPORTANT:** Before training the classifier, move the files of your previous model (`pipeline.pkl`, `clf.pkl`) in a different folder. \
**If you don't do that, the pretrained classifier will be erased!** \
If you want to retrain the model, just type the following command:
```
python3 train_clf.py
```
then you can use the classifier following the instruction in the section `Use the classifier (Predict)` of this readme file.