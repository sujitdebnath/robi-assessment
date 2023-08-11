import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

FILE_PATH = r'Assessment - Data Scientist.xlsx'

def read_excel_sheet(file_path, sheet_name):

    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

def merge_dataframes(df1, df2, join_col, join_type, suffixes=None):
    df = None

    if suffixes == None:
        df = pd.merge(df1, df2, on=join_col, how=join_type)
    else:
        df = pd.merge(df1, df2, on=join_col, how=join_type, suffixes=suffixes)
    
    return df

if __name__ == "__main__":
    df_student = read_excel_sheet(FILE_PATH, 'Dataset-student')
    df_student_math = read_excel_sheet(FILE_PATH, 'Dataset-student-math')
    df_student_english = read_excel_sheet(FILE_PATH, 'Dataset-student-english')

    df_stud_and_math = merge_dataframes(df_student, df_student_math, 'Student Id', 'outer')
    df_stud_math_eng = merge_dataframes(df_stud_and_math, df_student_english, 'Student Id', 'outer', ('_Math', '_Eng'))
    print(df_stud_math_eng.head())

    # Task 01
    print("01. What is the difference in final grade in Math for male vs female students?\n"
          "Ans: Mean Difference is {:.3f}"
          .format(abs(df_stud_math_eng[df_stud_math_eng['sex']=='M']['G3_Math'].mean() - df_stud_math_eng[df_stud_math_eng['sex']=='F']['G3_Math'].mean())))  

    # Task 02
    print("02. How many students have higher score in Math in G2, than in G3?\n"
          "Ans: {} Students\n"
            .format(df_stud_math_eng[df_stud_math_eng['G2_Math']>df_stud_math_eng['G3_Math']]['Student Id'].count()))
    
    # Task 03
    print("03. What is the correlation between absence and Math final grade?\n"
          "Ans: Correlation {:.3f}\n"
            .format(df_stud_math_eng['absences'].corr(df_stud_math_eng['G3_Math'])))
    
    # Task 04


    # Task 05
    top_score_3rd = df_stud_math_eng['G3_Math'].sort_values(ascending=False).unique()[2]
    print("05. What is the student id of third top scorer in Math final grade?\n"
          "Ans: 3rd Top Score is {}, Number of 3rd Scorer is {}, and Students IDs are {}\n"
            .format(top_score_3rd,
                    len(df_stud_math_eng[df_stud_math_eng['G3_Math']==top_score_3rd]['Student Id'].to_list()),
                    df_stud_math_eng[df_stud_math_eng['G3_Math']==top_score_3rd]['Student Id'].to_list()))
    
    # Task 06
    df_stud_math_eng['Combine_Final_Grade'] = df_stud_math_eng['G3_Math']+df_stud_math_eng['G3_Eng']
    top_score_5th = df_stud_math_eng['Combine_Final_Grade'].sort_values(ascending=False).unique()[4]
    print("06. What is the student id of fifth top scorer combining both Math and English final grade?\n"
          "Ans: 5th Top Score is {}, Number of 5th Scorer is {}, and Students IDs are {}\n"
            .format(top_score_5th,
                    len(df_stud_math_eng[df_stud_math_eng['Combine_Final_Grade']==top_score_5th]['Student Id'].to_list()),
                    df_stud_math_eng[df_stud_math_eng['Combine_Final_Grade']==top_score_5th]['Student Id'].to_list()))
    
    # Task 07
    quartile_3rd = df_stud_math_eng['G3_Math'].quantile(0.75)
    print("07. What is the minimum final grade in Math for students in 3rd quartile?\n"
          "Ans: 3rd quartile value is {}, and min final grade in math for students in 3rd quartile is {}\n"
            .format(quartile_3rd,
                    df_stud_math_eng[df_stud_math_eng['G3_Math']>=quartile_3rd]['G3_Math'].min()))
    
    # Task 08
    sns.boxplot(
        x=df_stud_math_eng["age"],
        y=df_stud_math_eng["G3_Eng"],
        palette="Blues"
    ).set(
        title='Box and Whisker plot of Age vs Final Eng Grade',
        xlabel='Age',
        ylabel='Final Grade in English'
    )

    plt.savefig('boxplot age vs final grade in eng.png')


    # Task 09
    sns.displot(
        df_stud_math_eng,
        x="age",
        binwidth=1,
        kde=True
    ).set(
        title = 'Age distribution of students',
        xlabel='Age',
        ylabel='Count of Students'
    )
    plt.savefig('barplot of age.png', bbox_inches='tight')

    # Task 10
    print("10. What is the standard deviation in English final grade?\n"
          "Ans: {:.3f}\n"
            .format(df_stud_math_eng["G3_Eng"].std(skipna = True)))
    
    # Task 11
    sns.boxplot(df_stud_math_eng["G3_Math"]).set(title='Box and Whisker plot of Final Math Grade')
    plt.savefig('boxplot of math grade.png')

    z_score = np.abs(stats.zscore(df_stud_math_eng["G3_Math"]))
    print(np.where(z_score > 3))

    # Task 12
    print("12. If G2 value was missing for Student Id 10, what value would you put there?\n"
          "Ans: Mean value {:.3f} would be put there\n"
          .format(df_stud_math_eng[df_stud_math_eng['Student Id']!=10]['G2_Math'].mean()))

    # Task 13
    print("13. How many records have missing values?\n"
          "And: {} records have missing values"
          .format(df_stud_math_eng.isnull().any(axis=1).sum()))
    
    # Task 14
    # print(df_stud_math_eng[['school', 'address', 'G3_Math']])
    # df = df_stud_math_eng[['school', 'address', 'G3_Math']]
    # sns.boxplot(x='school', y='address', data=df)
    # plt.savefig('sample.png')

    # Task 15


    # Task 16
    df = df_stud_math_eng[['Student Id', 'G3_Math', 'G3_Eng']]
    math_mean = df_stud_math_eng['G2_Math'].mean()
    eng_mean = df_stud_math_eng['G3_Eng'].mean()
    print("Mean Math score is {:.3f}, and Mean English Score is {:.3f}".format(math_mean, eng_mean))

    good_in_math = df[df['G3_Math']>math_mean]['Student Id'].to_list()
    good_in_eng = df[df['G3_Eng']>eng_mean]['Student Id'].to_list()
    good_in_both = [id for id in df['Student Id'].tolist() if id in good_in_math and id in good_in_eng]
    print("{:.3f} students did avobe then average score, which ratio is almost {:.3f}%\n"
            .format(len(good_in_both), len(good_in_both)*100/df_stud_math_eng['Student Id'].count()))
    