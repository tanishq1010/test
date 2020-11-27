import requests
import pandas as pd
import json
from openpyxl import Workbook, load_workbook
from miscellaneous import *
import random


class Source(object):
    def __init__(self):
        super(Source, self).__init__()
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Content-Type': 'application/json; charset=UTF-8',
        }
        self.host = 'https://fiberdemoms.embibe.com'

    def callAPI(self, url, payload, method, token):
        self.headers['embibe-token'] = token
        response = requests.request(method, self.host + url, headers=self.headers, data=payload)
        if response.status_code != 200:
            print(url + ' - ' + str(response.content))
            return None
        return response

    def main(self, child_id, board, grade, exam, goal, embibe_token, subject, home_data, df_negative_results,
             df_positive_results):
        payload = {
            "board": goal,
            "child_id": child_id,
            "exam": exam,
            "exam_name": exam,
            "goal": goal,
            "grade": grade,
            "subject": subject,
            "fetch_all_content" : "true"
        }
        response1 = self.callAPI(
            f"/fiber_ms/home/test",
            json.dumps(payload),
            'POST', embibe_token)
        count=0
        chapter_count=0
        full_count=0
        
        for item in response1.json():
         
         chapter="Chapter"
         full="Full"
        
         
         if item['content_section_type']=="SUBJECTS":
            for data in item["content"]:
                count+=1
         if item['section_name'].find(full)>=0:
            full_count+=1
         if item['section_name'].find(chapter)>=0:
            chapter_count+=1
        for item in response1.json():
        
            # if item["content_section_type"] == "PRACTICEBANNER":
            #     hero_banner_checker(response1.json(), df_negative_results, df_positive_results,
            #                         "negative_practice_results.csv", "positive_practice_results.csv", home_data,
            #                         subject)

            if item["contentType"] =="Test":
                section_name = item["section_name"]
                for data in item["content"]:
                    title = data["title"]
                    description = data["description"]
                    length = data["duration"]
                    # currency = int(data["currency"])
                    id = data["bundle_id"]
                    questions=data["questions"]
                    Type = data["type"]
                    subject_tagged = data["subject"]
                    thumb = data["thumb"]
                    # thumbnail=True
                    if thumb == "":
                        thumbnail = False
                    else:
                        thumbnail = True
                    if title == "" or description == "" or length == "" or length == 0  or id == "" or Type == "" or questions ==0:
                        length = minutes_converter(length)
                        df_negative_results.loc[len(df_negative_results)] = home_data + [length, Type, id, title,
                                                                                         section_name, questions,
                                                                                         subject, subject_tagged, "",
                                                                                         "", "", "",thumbnail]

                        df_negative_results.to_csv("negative_test_results.csv", index=False)
                    else:
                        length = minutes_converter(length)
                        df_positive_results.loc[len(df_positive_results)] = home_data + [length, Type, id, title,
                                                                                         section_name, questions,
                                                                                         subject, subject_tagged, "",
                                                                                         "", "", "",thumbnail]

                        df_positive_results.to_csv("positive_test_results.csv", index=False)


        
        full = False
        if count==full_count:
            full=True
        part=False
        if count==chapter_count:
            part=True
        # for item in response1.json():
        #      str3=item["section_name"]
        #      if (str3.find(str1))>0:
        #          full=True
        #      if str3.find(str2)>0:
        #          part=True

        # df_positive_results = pd.read_csv("positive_learn_results.csv")
        if full == True and part == True:
            df_positive_results.loc[len(df_positive_results)] = home_data + ["", "", random.randint(0, 1000000), "",
                                                                             "All carousals present", "", "",
                                                                             subject, "", "", part,full,""]

            df_positive_results.to_csv("positive_test_results.csv", index=False)
        else:
            df_negative_results.loc[len(df_negative_results)] = home_data + ["", "", random.randint(0, 1000000), "",
                                                                             "All carousals present", "", "",
                                                                             subject, "", "",part,full,""]

            df_negative_results.to_csv("negative_test_results.csv", index=False)

        df11 = pd.read_csv("positive_test_results.csv")
        df2 = pd.read_csv("positive_test_results.csv")

        df1 = df11[df11['Exam'].str.contains(exam)]
        df2 = df1[df1['Exam'].str.contains(exam)]

        for ind in df2.index:
            df_new = df1.loc[df1['Id'] == df2["Id"][ind]]
            if len(df_new) > 0:
                df_new1 = df_new.loc[df_new["Section_name"] == df2["Section_name"][ind]]
                if len(df_new1) == 1:
                    df2["Duplicasy check"][ind] = str("yes")
                else:
                    df2["Duplicasy check"][ind] = str("no")

        df = pd.concat([df11, df2])

        df = df.dropna(axis=0, subset=['Duplicasy check'])
        # print(df)
        df.to_csv('positive_test_results.csv', index=False)


def subject_data_extractor(child_id, board, grade, exam, goal, embibe_token, subject, home_data, df_negative_results,
                           df_positive_results):
    src = Source()
    src.main(child_id, board, grade, exam, goal, embibe_token, subject, home_data, df_negative_results,
             df_positive_results)

# subject_data_extractor("", "", "", "", "",
#                        "yJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoic3R1ZGVudCIsInRpbWVfc3RhbXAiOiIyMDIwLTEwLTE1IDE3OjQyOjI2IFVUQyIsImlzX2d1ZXN0IjpmYWxzZSwiaWQiOjM2MTU1OTQsImVtYWlsIjoiYzEzNDEzOGUwNDc1QGppby1lbWJpYmUuY29tIn0.lG7sauHJW1Hwj3nQGzDBrBjyPbhaFJGGnZ05bbflJjkD-tmybjJ8V-Si7phyv6Wai28twrgH-J82P0iF7r_Sag",
#                        "Science")