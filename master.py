from goal_exam_extractor import goal_exam_grade_extractor
from home_data_extractor import home_data
import pandas as pd
import numpy as np

from login_sign_up import *

from miscellaneous import *
# from home_data_continue_learning import home_data



def for_all_exam_goal(goal_exam_grade):
    for ind in goal_exam_grade.index:
     # if goal_exam_grade["Exam_name"][ind]=="IBPS RRB Office Assistant Mains":
        print(goal_exam_grade["Goal"][ind], goal_exam_grade["Exam_name"][ind])
        # signup_data=Signup()
        # login_data=login(signup_data[0],"embibe1234")
        # # child_data=add_user(signup_data[1],login_data[0])
        # embibe_token=login_data[1]
        # child_id=signup_data[1]
        home_data(3721404, goal_exam_grade["Goal"][ind], goal_exam_grade["Grade"][ind],
                  goal_exam_grade["Exam_name"][ind],
                  goal_exam_grade["Goal"][ind],'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoic3R1ZGVudCIsInRpbWVfc3RhbXAiOiIyMDIwLTEwLTE1IDE3OjQyOjI2IFVUQyIsImlzX2d1ZXN0IjpmYWxzZSwiaWQiOjM3MjE0MDQsImVtYWlsIjoiMzYxNTU5NF8xNjAyNzgzNzQ2QGVtYmliZS11c2VyLmNvbSJ9.QYI2fB25BRp4c8KNkHIKSOSYLvxARKIDGxJXstk5OMqmlZiQ-E2kult1tDHHKP7eNtNnh4-upBdjmFQeM8CkVw')
        # break
     # else :
     #    continue


if __name__ == '__main__':

    df_negative_results_all_subjects = pd.DataFrame(columns=['Child_ID', 'Exam', 'Goal', "Grade",
                                                             'Duration/Concept count', 'Type', 'Id', "Title", 'Section_name',
                                                             'Questions', "Subject", "Subject_tagged",
                                                             "present in subject", "Correctly present in CG","Chapter test present","Full test present","Thumbnail present"])
    df_positive_results_all_subjects = pd.DataFrame(columns=['Child_ID', 'Exam', 'Goal', "Grade",
                                                             'Duration/Concept count', 'Type', 'Id', "Title", 'Section_name',
                                                             'Questions', "Subject", "Subject_tagged",
                                                             "present in subject", "Correctly present in CG","Chapter test present","Full test present","Thumbnail present"])
    df_negative_results_all_subjects.to_csv("negative_test_results_all_subjects.csv", index=False)
    df_positive_results_all_subjects.to_csv("positive_test_results_all_subjects.csv", index=False)
    df_negative_results = pd.DataFrame(columns=['Child_ID', 'Exam', 'Goal', "Grade",
                                                'Duration/Concept count', 'Type', 'Id', "Title", 'Section_name',
                                                'Questions', "Subject", "Subject_tagged", "Duplicasy check",
                                                "Correctly present in CG","Chapter test present","Full test present","Thumbnail present"])
    df_positive_results = pd.DataFrame(columns=['Child_ID', 'Exam', 'Goal', "Grade",
                                                'Duration/Concept count', 'Type', 'Id', "Title", 'Section_name',
                                                'Questions', "Subject", "Subject_tagged", "Duplicasy check",
                                                "Correctly present in CG","Chapter test present","Full test present","Thumbnail present"])
    df_negative_results.to_csv("negative_test_results.csv", index=False)
    df_positive_results.to_csv("positive_test_results.csv", index=False)

    goal_exam_grade = goal_exam_grade_extractor()
    for_all_exam_goal(goal_exam_grade)

    # print("\n\n COMPARING")
    comparator("positive_test_results_all_subjects.csv", "positive_test_results.csv")
    comparator2("positive_test_results_all_subjects.csv", "positive_test_results.csv")
    video_book_validation(pd.read_csv("positive_test_results.csv"),"positive_test_results.csv")
    video_book_validation(pd.read_csv("positive_test_results_all_subjects.csv"),"positive_test_results_all_subjects.csv")
    df1=pd.read_csv('positive_test_results_all_subjects.csv')
    df2=pd.read_csv('positive_test_results.csv')
    df3=pd.read_csv('negative_test_results_all_subjects.csv')
    df4=pd.read_csv('negative_test_results.csv')
    
    def recode_empty_cells(dataframe, list_of_columns):

        for column in list_of_columns:
         dataframe[column] = dataframe[column].replace(r'\s+', np.nan, regex=True)
         dataframe[column] = dataframe[column].fillna("NA")

        return dataframe
    df1=recode_empty_cells(df1,df1.columns.tolist())
    df2=recode_empty_cells(df2,df2.columns.tolist())
    df3=recode_empty_cells(df3,df3.columns.tolist())
    df4=recode_empty_cells(df4,df4.columns.tolist())
    df1.to_csv('positive_test_results_all_subjects.csv',index=False)
    df2.to_csv('positive_test_results.csv',index=False)
    df3.to_csv('negative_test_results_all_subjects.csv',index=False)
    df4.to_csv('negative_test_results.csv',index=False)




    # df = pd.DataFrame(columns=['Child_ID', 'Exam', 'Goal', "Grade",'Type', 'Id', "Title", "Subject", "Subject_tagged"])
    # df.to_csv("continue_learning.csv")

    # df1=pd.read_csv("actual_continue_learning.csv")
    # home_data()
    # df2=pd.read_csv("continue_learning.csv")

    # for ind in df1.index:
    #     list1 = [""] * len(df1)
    #     df1["present in api"] = list1
    #     df_new=df2.loc[df2["Id"]==df1["Id"][ind]]
    #     if len(df_new)==1:
    #         df1["present in api"][ind]="yes"
    #     else:
    #         df1["present in api"][ind] = "no"
    #     df1.to_csv("actual_continue_learning.csv",index=False)
