import pandas as pd

acm = pd.read_csv("acm.12.20-10.23.no.dups.with.all.csv")

print("\nACM number of missing abstarct: \n", len(acm['Abstract'][acm['Abstract'].isna()]))
print(acm['URL'][acm['Abstract'].isna()])

ieee = pd.read_csv("IEEE.21-23.no.dups.with.all.csv")

print("\nIEEE number of missing abstarct: \n", len(ieee['Abstract'][ieee['Abstract'].isna()]))
print(ieee['URL'][ieee['Abstract'].isna()])

philpapers = pd.read_csv("philpapers2123N.csv")

print("\nPhilpapers number of missing abstarct: \n",len(philpapers['Abstract'][philpapers['Abstract'].isna()]))
print(philpapers['URL'][philpapers['Abstract'].isna()])

springer = pd.read_csv("springer2123N.csv")

print("\nSpringer number of missing abstarct: \n",len(springer['Abstract'][springer['Abstract'].isna()]))
print(springer['URL'][springer['Abstract'].isna()])



import re

# function to remove special characters and clean the Abstracts
def remove_special_characters_lower(input_string):
    # Define a regular expression pattern to match non-alphanumeric characters excluding spaces
    pattern = re.compile('[^A-Za-z0-9 ]+')
    
    # Use the pattern to replace special characters with an empty string
    result_string = pattern.sub('', input_string).lower()
    
    return result_string

def get_eligibility_score(cleaned_string, keywords):
    
    count = 0
    total_count = 0
    word_list = cleaned_string.split(" ")

    for word in word_list:
        if word in keywords:
            count += keywords[word]
            total_count += 1
        else:
            total_count += 1

    eligibility_score = count/total_count
    return eligibility_score

keywords = {
    'ai': 1,
    'ethical': 3,
    'digital': 2,
    'ethics': 2,
    'data': 1, 
    'autonomy': 1,
    'discrimination': 1,
    'domination': 1,
    'exclusion': 1,
    'exploitation': 1,
    'inequality': 1,
    'justice': 1,
    'privacy': 1,
    'responsibility': 1,
    'trust': 1,
    'dignity': 1,
    'truth': 1,
}

# ACM
acm_eligibility = pd.DataFrame()

i = 0
for i in range(len(acm['Abstract'])):

    if isinstance(acm['Abstract'].loc[i], str):
        
        cleaned_string = remove_special_characters_lower(acm.loc[i, "Abstract"])
        eligibility_score = get_eligibility_score(cleaned_string, keywords)
        acm_eligibility.loc[i, "Title"] = acm["Title"].loc[i]
        acm_eligibility.loc[i, "Authors"] = acm["Authors"].loc[i]
        acm_eligibility.loc[i, "Publisher"] = "ACM"
        acm_eligibility.loc[i, "DOI"] = acm["DOI"].loc[i]
        acm_eligibility.loc[i, "URL"] = acm["URL"].loc[i]
        acm_eligibility.loc[i, "Abstract"] = acm["Abstract"].loc[i]
        acm_eligibility.loc[i, "Eligibility_Score"] = eligibility_score

acm_eligibility = acm_eligibility.sort_values(by='Eligibility_Score', ascending=False)
acm_eligibility = acm_eligibility.reset_index(drop=True)
acm_eligibility.to_csv("eligibilityStep/acm_eligibility2123.csv")

# IEEE
ieee_eligibility = pd.DataFrame()

i = 0
for i in range(len(ieee['Abstract'])):

    if isinstance(ieee['Abstract'].loc[i], str):
        
        cleaned_string = remove_special_characters_lower(ieee.loc[i, "Abstract"])
        eligibility_score = get_eligibility_score(cleaned_string, keywords)
        ieee_eligibility.loc[i, "Title"] = ieee["Title"].loc[i]
        ieee_eligibility.loc[i, "Authors"] = ieee["Authors"].loc[i]
        ieee_eligibility.loc[i, "Publisher"] = "ieee"
        ieee_eligibility.loc[i, "DOI"] = ieee["DOI"].loc[i]
        ieee_eligibility.loc[i, "URL"] = ieee["URL"].loc[i]
        ieee_eligibility.loc[i, "Abstract"] = ieee["Abstract"].loc[i]
        ieee_eligibility.loc[i, "Eligibility_Score"] = eligibility_score

ieee_eligibility = ieee_eligibility.sort_values(by='Eligibility_Score', ascending=False)
ieee_eligibility = ieee_eligibility.reset_index(drop=True)
ieee_eligibility.to_csv("eligibilityStep/ieee_eligibility2123.csv")

philpapers_eligibility = pd.DataFrame()

i = 0
for i in range(len(philpapers['Abstract'])):

    if isinstance(philpapers['Abstract'].loc[i], str):
        
        cleaned_string = remove_special_characters_lower(philpapers.loc[i, "Abstract"])
        eligibility_score = get_eligibility_score(cleaned_string, keywords)
        philpapers_eligibility.loc[i, "Title"] = philpapers["Title"].loc[i]
        philpapers_eligibility.loc[i, "Authors"] = philpapers["Authors"].loc[i]
        philpapers_eligibility.loc[i, "Publisher"] = "philpapers"
        philpapers_eligibility.loc[i, "DOI"] = philpapers["DOI"].loc[i]
        philpapers_eligibility.loc[i, "URL"] = philpapers["URL"].loc[i]
        philpapers_eligibility.loc[i, "Abstract"] = philpapers["Abstract"].loc[i]
        philpapers_eligibility.loc[i, "Eligibility_Score"] = eligibility_score

philpapers_eligibility = philpapers_eligibility.sort_values(by='Eligibility_Score', ascending=False)
philpapers_eligibility = philpapers_eligibility.reset_index(drop=True)
philpapers_eligibility.to_csv("eligibilityStep/philpapers_eligibility2123.csv")

springer_eligibility = pd.DataFrame()

i = 0
for i in range(len(springer['Abstract'])):

    if isinstance(springer['Abstract'].loc[i], str):
        
        cleaned_string = remove_special_characters_lower(springer.loc[i, "Abstract"])
        eligibility_score = get_eligibility_score(cleaned_string, keywords)
        springer_eligibility.loc[i, "Title"] = springer["Title"].loc[i]
        springer_eligibility.loc[i, "Authors"] = springer["Authors"].loc[i]
        springer_eligibility.loc[i, "Publisher"] = "springer"
        springer_eligibility.loc[i, "DOI"] = springer["DOI"].loc[i]
        springer_eligibility.loc[i, "URL"] = springer["URL"].loc[i]
        springer_eligibility.loc[i, "Abstract"] = springer["Abstract"].loc[i]
        springer_eligibility.loc[i, "Eligibility_Score"] = eligibility_score

springer_eligibility = springer_eligibility.sort_values(by='Eligibility_Score', ascending=False)
springer_eligibility = springer_eligibility.reset_index(drop=True)
springer_eligibility.to_csv("eligibilityStep/springer_eligibility2123.csv")