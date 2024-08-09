import pandas as pd

# 建立範例資料
students_data = {
    "student_id": [1, 2, 13, 6],
    "student_name": ["Alice", "Bob", "John", "Alex"]
}

subjects_data = {
    "subject_name": ["Math", "Physics", "Programming"]
}

examinations_data = {
    "student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
    "subject_name": ["Math", "Physics", "Programming", "Programming", "Physics", "Math", "Math", "Programming", "Physics", "Math", "Math"]
}

# 建立DataFrame
students_df = pd.DataFrame(students_data)
subjects_df = pd.DataFrame(subjects_data)
examinations_df = pd.DataFrame(examinations_data)

# 建立所有學生與所有課程的組合
student_subject_df = students_df.assign(key=1).merge(subjects_df.assign(key=1), on="key").drop("key", axis=1)

# 左連接來合併Examinations資料
result_df = student_subject_df.merge(examinations_df, how="left", on=["student_id", "subject_name"])

# 計算每個學生每門課的考試次數
result_df = result_df.groupby(["student_id", "student_name", "subject_name"]).size().reset_index(name="attended_exams")

# 按student_id和subject_name排序
result_df = result_df.sort_values(by=["student_id", "subject_name"])

# import ace_tools as tools; tools.display_dataframe_to_user(name="Students and Examinations Result", dataframe=result_df)
"""
   student_id student_name subject_name  attended_exams
0           1        Alice         Math               3
1           1        Alice      Physics               2
2           1        Alice  Programming               1
3           2          Bob         Math               1
4           2          Bob      Physics               1
"""
