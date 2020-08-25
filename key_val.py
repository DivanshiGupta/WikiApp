import wptools
import json
import wikidata
from wikidata.client import Client

f = open('test.json')
names = json.load(f)
output_list = []

fela = wptools.page(names).get_parse()

infobox = fela.data['infobox']
id = fela.data['wikibase']
wikidata_client = Client()
entity = wikidata_client.get(id, load=True)
p = wikidata_client.get('P21')
gender = entity[p].label

dictionary = {
    "name": "",
    "gender": "",
    "nationality": "",
    "occupation": "",
    "birth_date": "",
    "birth_name": "",
    "birth_place": "",
    "title": "",
    "employer": "",
    "office": "",
    "term_start": "",
    "term_end": "",
    "predecessor": "",
    "successor": "",
    "office1": "",
    "term_start1": "",
    "term_end1": "",
    "predecessor1": "",
    "successor1": "",
    "office2": "",
    "term_start2": "",
    "term_end2": "",
    "predecessor2": "",
    "successor2": "",
    "office3": "",
    "term_start3": "",
    "term_end3": "",
    "predecessor3": "",
    "successor3": "",
    "office4": "",
    "term_start4": "",
    "term_end4": "",
    "predecessor4": "",
    "successor4": "",
    "office5": "",
    "term_start5": "",
    "term_end5": "",
    "predecessor5": "",
    "successor5": "",
    "office6": "",
    "term_start6": "",
    "term_end6": "",
    "predecessor6": "",
    "successor6": "",
    "office7": "",
    "term_start7": "",
    "term_end7": "",
    "predecessor7": "",
    "successor7": "",
    "fields": "",
    "term": "",
    "awards": "",
    "honors": "",
    "known_for": "",
    "political_party": "",
    "notable_works": "",
    "parents": "",
    "mother": "",
    "father": "",
    "relatives": "",
    "spouse": "",
    "partner": "",
    "children": "",
    "home_town": "",
    "alma_mater": "",
    "education": "",
    "citizenship": "",
    "residence": "",
    "death_date": "",
    "death_place": "",
    "years_active": "",
    "boards": "",
    "net_worth": "",
    "salary": "",
    "website": ""
}
words = ["unbulleted list", "Unbulleted list", "bulleted list", "Bulleted list", "small",
         "Small", "Nowrap", "nowrap", "Nobr", "nobr"]

date_words = [
    "birth date and age|",  "Birth date and age|", "birth date and age", "Birth date and age",
    "birth year and age|", "Birth year and age|", "birth year and age", "Birth year and age",
    "birth date|", "birth date", "Birth date|", "Birth date",
    "|df|=|yes|", "df|=|yes|", "|df|=|yes", "|df|=|y|", "df|=|y|", "|df|=|y",
    "|mf|=|yes|", "mf|=|yes|", "|mf|=|yes", "|mf|=|y|", "mf|=|y|", "|mf|=|y",
    "Birth year|", "birth year|", "Birth year", "birth year",
    "death date and age|",  "Death date and age|", "death date and age", "Death date and age",
    "death year and age|", "Death year and age|", "death year and age", "Death year and age",
    "death date|", "death date", "Death date|", "Death date",
    "|df|=|yes|", "df|=|yes|", "|df|=|yes", "|df|=|y|", "df|=|y|", "|df|=|y",
    "|mf|=|yes|", "mf|=|yes|", "|mf|=|yes", "|mf|=|y|", "mf|=|y|", "|mf|=|y",
    "Death year|", "death year|", "Death year", "death year", "dda|", "dda", "d-da|", "d-da"
]

for k in dictionary.keys():
    if k in infobox:
        dictionary[k] = infobox[k]

x = dictionary['birth_date']
temp = ""
i = 0
while(i != len(x)):
    s = 0
    for j in date_words:
        if len(j) + i <= len(x):
            r = 0
            for u in range(0, len(j)):
                if j[u] != x[i+u]:
                    r = 1
                    break
            if r == 0:
                i += len(j)
                s = 1
        if s == 1:
            break
    if s == 1:
        continue
    if x[i] != '{' and x[i] != '}':
        temp += x[i]
    i += 1
dictionary['birth_date'] = temp

x = dictionary['death_date']
temp = ""
i = 0
while(i != len(x)):
    for j in date_words:
        if len(j) + i <= len(x):
            r = 0
            for u in range(0, len(j)):
                if j[u] != x[i+u]:
                    r = 1
                    break
            if r == 0:
                i += len(j)
                break
    if x[i] != '{' and x[i] != '}':
        temp += x[i]
    i += 1
dictionary['death_date'] = temp

for k in dictionary.keys():
    if k == "gender":
        continue
    x = dictionary[k]
    temp = ""
    i = 0
    while(i != len(x)):
        for j in words:
            if len(j) + i <= len(x):
                r = 0
                for u in range(0, len(j)):
                    if j[u] != x[i+u]:
                        r = 1
                        break
                if r == 0:
                    i += len(j)
                    break
        if(x[i] == '|' and k != "birth_date" and k != "death_date"):
            temp += ','
        elif x[i] != '[' and x[i] != ']' and x[i] != '<' and x[i] != '{' and x[i] != '}' and x[i] != '\n' and x[i] != '\u00b7':
            temp += x[i]
        elif x[i] == '<':
            if (len(temp) == 0) or (len(temp) > 1 and temp[len(temp) - 1] == " " and temp[len(temp)-2] == ','):
                con = 1
            elif (len(temp) > 0 and temp[len(temp)-1] == ',') or (i > 3 and x[i-1] == 'd' and x[i-2] == 'n' and x[i-3] == 'a'):
                if(temp[len(temp)-1] != ' '):
                    temp += " "
            else:
                temp += ','
            f = 0
            for j in range(i, len(x)):
                if x[j] == '>':
                    f = j
                    break
            i = f
        elif x[i] == '\n':
            if (len(temp) > 0 and temp[len(temp)-1] == ',') or (i > 3 and x[i-1] == 'd' and x[i-2] == 'n' and x[i-3] == 'a'):
                if(temp[len(temp)-1] != ' '):
                    temp += " "
            else:
                temp += ','
        elif x[i] == "\u00b7":
            temp += ','

        i += 1
    dictionary[k] = temp

gender = str(gender)
if gender[0] == 'f' or gender[0] == 'F':
    dictionary['gender'] = "female"
else:
    dictionary['gender'] = "male"
output_list.append(dictionary)

json_object = json.dumps(output_list, indent=4)
with open("key_val.json", "w") as outfile:
    outfile.write(json_object)
