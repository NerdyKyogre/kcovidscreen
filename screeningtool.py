# -*- coding: utf-8 -*-
"""
NerdyKyogre's COVID-19 Self Assessment tool
Use this tool to detect if a person has covid symptoms and determine the necessary action to take.
"""

import pyautogui
import random

def main():
    
    seed = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    random.shuffle(seed) 
    question = 0
    covid = False
    
    n = (["Do you have a fever?","Do you have a cough?","Are you experiencing shortness of breath?","Do you have a sore throat?","Do you have a runny nose?","Have you lost your sense of smell or taste?","Are you experiencing chills?","Is it painful to swallow?","Do you have aches in your joints or muscles?","Do you feel at all unwell or fatigued?","Do you have nausea, vomiting, or diarrhea?","Have you lost your apetite?","Do you have pink eye?","Have you recently been in contact with a confirmed COVID case?","Have you left the country in the last two weeks?"])
    p = (["Is your body temperature normal?","Has it been more than 24 hours since your last bout of coughing?","Are you able to breathe normally?","Is your throat painless?","Is your nose free of excess mucus?","Are you able to smell and taste as normal?","Was the last time you experienced recurring chills more than 24 hours ago?","Are you able to swallow without pain?","Are your joints and muscles free of aches?","Are your energy levels normal?","Is your digestive system functioning properly?","Were you able to eat your most recent meal normally?","Are your eyes their usual colour?","Have you recently been able to avoid contact with any confirmed COVID cases?","Have you stayed within your country for the last two weeks?"])
    
    pyautogui.alert(text="Welcome to NerdyKyogre's COVID-19 Self Assessment Tool.\nThe following tool will help you to determine whether you or a loved one may be infected with COVID-19.\nIt will also advise you of what action to take based on the results.\nPress OK when you are ready to begin.", title="Begin Assessment")
    
    while question < 15 and covid == False:
        q = seed[question]
        pos = random.choice([n,p])
        
        input = 'None'
        
        while str(input) == 'None':
            input = pyautogui.confirm(text=pos[q], title="COVID-19 Screening In Progress", buttons=['Yes','No'])
        
        if (input == 'Yes' and pos == n) or (input == 'No' and pos == p):
            pyautogui.alert(text="You may have COVID-19.\nPlease remain calm and get tested as soon as possible.\nThen, follow isolation requirements as outlined by your local government.\nFor Albertans, go to myhealth.alberta.ca.", title="Warning")
            covid = True
            
        question = question + 1
        
    if covid == False:
        pyautogui.alert(text="You most likely do not have COVID-19 or any similar illness.\nYou may go about your daily activities as normal.\n",title="Success")
        
    redo = pyautogui.confirm(text="Thank you for choosing NerdyKyogre's COVID-19 Self Assessment tool.\nWould you or someone else in the room like to take the test again?", title="Assessment Complete",buttons=["Close","Go again"])
    if redo == "Go again":
        main()
    
main()