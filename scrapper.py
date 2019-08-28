from getter import rawGetter
from getter import isResponse
from bs4 import BeautifulSoup
import os
import re
import csv
import unicodedata

def escape_ansi(line):
    unicodedata.normalize('NFKD', line).encode('ascii','ignore')
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    string_to_replace = ansi_escape.sub('', line)
    return string_to_replace.replace("\\","")

def append(tail):
    #list_questions is for questions
    #list_answer_tuple is for options
    #list_right_tuple is for correct option
    list_questions = list()
    list_answer_tuple = list()
    list_right_tuple = list()
    '''getting the requests
    '''
    i_html = rawGetter(tail)
    html = BeautifulSoup(i_html, 'html.parser')

    if(html != None):
        mother_crawl = html.find_all("span", attrs={"class": "qa_list"})
        right = list()
        questions = list()
        ###
        # Questions
        ###
        #ul class='options_list clearfix'
        element_question = html.find_all('ul', attrs= {"class":"options_list clearfix"})
        for e in element_question:
            questions.append(e.previousSibling)
        
        ###
        # Answers
        ###
        element_span = html.find_all("span", attrs={"class":"answer option"})
        for iterator_ele in element_span:
            lis = iterator_ele.find_all("a")
            for iterator_lis in lis:
                right.append(iterator_lis.text[0])

        #checking to see if empty. If empty, skip page
        if(questions != [] and right != []):
            list_questions = questions
            list_right_tuple = right
        else: 
            return
        #to iterate through
        iteration = 0
        #print(len(list_questions[5]))

        table = html.find_all("div", attrs={"class": "qa_list"})
        for td in table:
            if "google" in td.text:
                continue
            if(iteration<=len(list_questions)-1):
                #Temp var for just taking in the data
                newcsv = list()
                #subject_id, topic_id, question_id
                newcsv.append("")
                newcsv.append("")
                newcsv.append("")
                #question
                newcsv.append(escape_ansi(list_questions[iteration]))
                #marks, time_to_spend,difficulty_level, hint, explanation
                newcsv.append("")
                newcsv.append("")
                newcsv.append("")
                newcsv.append("")
                newcsv.append("")
                #Start Answer counter
                answer_count = 0
                d = td.find_all("span", attrs={"class":"option"})
                temp = list()
                # for din in d:
                #     answer_count = answer_count + 1
                #     dtext = din.text[3:].strip()
                #     temp.append(dtext)
                #Praise no consistency for regex of input
                answer_count = 0
                d = td.find_all("span", attrs={"class":"option"})
                for din in d:
                    answer_count = answer_count + 1
                    dtext = din.text[3:].strip()
                    temp.append(escape_ansi(dtext))
                #total_answers
                newcsv.append(answer_count)
                #answer
                right_answer = list_right_tuple[iteration]
                if right_answer=="A":
                    newcsv.append("1")
                if right_answer=="B":
                    newcsv.append("2")
                if right_answer=="C":
                    newcsv.append("3")
                if right_answer=="D":
                    newcsv.append("4")                
                if right_answer=="E":
                    newcsv.append("5")
                newcsv.extend(temp)
                print('[APPEND]: ',newcsv)
                list_scraped.append(newcsv)
                iteration = iteration + 1
            else:
                break

list_final = [['subject_id', 'topic_id', 'question_type', 'question', 'marks',
'time_to_spend','difficulty_level', 'hint', 'explanation', 'total_answers', 'correct_answer', 
'answer1', 'answer2', 'answer3', 'answer4', 'answer5']]
#used to collect the objects
list_scraped = list()
latter = list()
input_file_name = input("[NAME] Output to save: ")
index = input("[PASTE] url to crawl: ")
inquiry = input("[RECURSION]Try automatic child pages? [y/n]: ")
if inquiry == "y" or inquiry == "Y":
    latter = map(str,input("[/ 1 2 3]Please enter the sub urls to crawl: \n").split())
    for ip in latter:
        append(index + ip)
else:
    append(index)
list_final.extend(list_scraped)

#write it to an spreadsheet readable format(csv)
with open(input_file_name+ '.csv', 'w', encoding="utf-8") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(list_final)
    csvFile.close()

print('\n\n\n\nSafetly finished writing the scraped data in '+ input_file_name+'.csv')