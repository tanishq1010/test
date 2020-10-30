import pandas as pd
# from check_grade_by_video_id import check_grade_by_video_id

# from check_grade_by_book_id import check_grade_by_book_id


def comparator(name1, name2):
    df1 = pd.read_csv(name1)
    # df1=df[df['Grades'].str.contains(grade)]
    df2 = pd.read_csv(name2)
    for ind in df1.index:
        df_new = df2.loc[df2["Section_name"] == df1["Section_name"][ind]]

        if len(df_new) > 0:
            df_new1 = df_new.loc[df_new["Id"] == df1["Id"][ind]]

            if len(df_new1) > 0:
                df_new2 = df_new1.loc[df_new1["Exam"] == df1["Exam"][ind]]

                if len(df_new2) > 0:
                    df_new3 = df_new2.loc[df_new2["Goal"] == df1["Goal"][ind]]
                    if len(df_new3) > 0:
                        df_new4 = df_new3.loc[df_new3["Subject_tagged"] == df1["Subject_tagged"][ind]]
                        if len(df_new4) > 0:
                            df1["present in subject"][ind] = str("yes")
        else:
            df1["present in subject"][ind] = str("no")
    df1.to_csv(name1, index=False)


def minutes_converter(length):
    seconds = length
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    days = int(seconds / seconds_in_day)
    hours = int((seconds - (days * seconds_in_day)) / seconds_in_hour)
    minutes = int((seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) / seconds_in_minute)
    seconds = int(seconds % 60)
    if hours == 0:
        return (str(int(minutes)) + " Min " + str(seconds) + " Sec")
    elif hours != 0:
        return (str(int(hours)) + "h " + str(minutes) + " Min")
    elif minutes != 0:
        return (str(int(minutes)) + " Min " + str(seconds) + " Sec")
    else:
        return (str(seconds) + " Sec")



# def video_book_validation(df, csv_name):
#     df["Correctly present in CG"] = [""] * len(df)

#     for ind in df.index:
#         if df["Section_name"][ind] == "INDIVIDUAL":
#             continue
#         elif df["Type"][ind] == "chapter" or df["Type"][ind] == "practice":
#             # answer =check_grade_by_video_id(df["Id"][ind],df["Grade"][ind])
#             df["Correctly present in CG"][ind] = "not_in_scope"
#         elif df["Type"][ind] == "Book":
#             answer = check_grade_by_book_id(df["Id"][ind], df["Exam"][ind])
#             df["Correctly present in CG"][ind] = answer
#         else:
#             df["Correctly present in CG"][ind] = "not_in_scope"
#     df.to_csv(csv_name, index=False)





def hero_banner_checker(payload, df_negative_results, df_positive_results, name1, name2, home_data, subject):
    for item in payload:
        flag = 0
        if item["content_section_type"] == "TESTBANNER":
            flag = 1
            section_id = item["section_id"]
            for data in item["content"]:
                for data in data["data"]:
                    for details in data["test_list"]:
                        description = details["description"]
                        title = details["title"]
                        duration = details["duration"]
                        Type = details["type"]
                        id = details["bundle_id"]
                        questions = details["questions"]
                        subject_tagged = details["subject"]

                        if title == "" or description == "" or duration == 0 or questions == 0 or id == "" or Type == "" or section_id != 100:
                            duration = minutes_converter(duration)
                            df_negative_results.loc[len(df_negative_results)] = home_data + [duration, Type, id, title,
                                                                                             "TESTBANNER", questions,
                                                                                             subject, subject_tagged,
                                                                                             "",
                                                                                             "", "", "", ""]
                            df_negative_results.to_csv(name1, index=False)
                        else:
                            duration = minutes_converter(duration)
                            df_positive_results.loc[len(df_positive_results)] = home_data + [duration, Type, id, title,
                                                                                             "TESTBANNER", questions,
                                                                                             subject, subject_tagged,
                                                                                             "",
                                                                                             "", "", "", ""]
                            df_positive_results.to_csv(name2, index=False)
        if flag == 1:
            break
