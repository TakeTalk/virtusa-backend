# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from fastapi import UploadFile
from service.similarWordsService import *
from service.TokenizeService import *
from model.knowledgebase import Knowledge

session = boto3.Session(profile_name='default')


def uploadPhoto(file: UploadFile, email: str, timeStamp: str):
    client = session.client('s3')
    client.upload_fileobj(file.file, "testimagetotext", email + timeStamp + file.filename)
    return file.filename


def detect_text(file: UploadFile, email: str, timeStamp: str):
    photo = email + timeStamp + file.filename
    uploadPhoto(file, email, timeStamp)
    client = session.client('rekognition')
    response = client.detect_text(Image={'S3Object': {'Bucket': "testimagetotext", 'Name': photo}})

    medicines = []

    textDetections = response['TextDetections']
    for text in textDetections:
        if text['Type'] == 'LINE':
            if checkMedicine(text['DetectedText']):
                medicines.append(medSuggestion(email, text['DetectedText']))
    allMedicines = {'medicineSuggestion': medicines}
    return allMedicines


def checkMedicine(sentence: str):
    if 'mg' in sentence: return True
    words = word_tokenize(sentence.lower())
    knowledge = Knowledge()
    for w in words:
        if knowledge.medicineSigns.get(w) is not None:
            return True


def medSuggestion(email: str, sentence: str):
    sentence = sentence.lower()
    words = word_tokenize(sentence)
    knowledge = Knowledge()
    allMedicines = []
    medTimes = {}
    flag = False
    for w in words:
        if knowledge.medicineTime.get(w) is not None:
            medTimes = {'name': sentence, 'time': knowledge.medicineTime.get(w), 'price': 102.50}
    updatePoint(email, 50)
    return medTimes
