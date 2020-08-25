import wptools
import json
import sys
f = open('key_val.json')
key_vals = json.load(f)
output_paras = []
for i in range(len(key_vals)):
    dict = key_vals[i]
    for key in dict:
        if dict[key] == '' or dict[key] == " ":
            dict[key] = "NULL"

    para1_keys = [

        ["name", "occupation"],
        ["name", "nationality"],
        ["name", "title"],
        ["name", "employer"],
        ["name", "office", "term_start", "term_end"],
        ["name", "office", "term_start"],
        ["name", "office", "term_end"],
        ["name", "office"],
        ["name", "predecessor"],
        ["name", "successor"],
        ["name", "office1", "term_start1", "term_end1"],
        ["name", "office1", "term_start1"],
        ["name", "office1", "term_end1"],
        ["name", "office1"],
        ["name", "predecessor1"],
        ["name", "successor1"],
        ["name", "office2", "term_start2", "term_end2"],
        ["name", "office2", "term_start2"],
        ["name", "office2", "term_end2"],
        ["name", "office2"],
        ["name", "predecessor2"],
        ["name", "successor2"],
        ["name", "office3", "term_start3", "term_end3"],
        ["name", "office3", "term_start3"],
        ["name", "office3", "term_end3"],
        ["name", "office3"],
        ["name", "predecessor3"],
        ["name", "successor3"],
        ["name", "office4", "term_start4", "term_end4"],
        ["name", "office4", "term_start4"],
        ["name", "office4", "term_end4"],
        ["name", "office4"],
        ["name", "predecessor4"],
        ["name", "successor4"],
        ["name", "office5", "term_start5", "term_end5"],
        ["name", "office5", "term_start5"],
        ["name", "office5", "term_end5"],
        ["name", "office5"],
        ["name", "predecessor5"],
        ["name", "successor5"],
        ["name", "office6", "term_start6", "term_end6"],
        ["name", "office6", "term_start6"],
        ["name", "office6", "term_end6"],
        ["name", "office6"],
        ["name", "predecessor6"],
        ["name", "successor6"],
        ["name", "office7", "term_start7", "term_end7"],
        ["name", "office7", "term_start7"],
        ["name", "office7", "term_end7"],
        ["name", "office7"],
        ["name", "predecessor7"],
        ["name", "successor7"],
        ["name", "fields"],
        ["name", "term"],
        ["name", "years_active"],
        ["name", "awards"],
        ["name", "honors"],
        ["name", "known_for"],
        ["name", "notable_works"],
        ["name", "political_party"],
        ["name", "birth_date", "birth_place"],
        ["name", "birth_date"],
        ["name", "birth_place"],
        ["name", "parents"],
        ["name", "mother", "father"],
        ["name", "father"],
        ["name", "mother"],
        ["name", "relatives"],
        ["name", "partner"],
        ["name", "children"],
        ["name", "home_town"],
        ["name", "alma_mater"],
        ["name", "education"],
        ["name", "citizenship"],
        ["name", "residence"],
        ["name", "death_date", "death_place"],
        ["name", "death_date"],
        ["name", "death_place"],
        ["name", "predecessor"],
        ["name", "successor"],
        ["name", "boards"],
        ["name", "net_worth"],
        ["name", "salary"],
        ["name", "website"]
    ]
    para1_sentences = [

        "1 is a 2. ",
        "1 has 2 nationality. ",
        "1 is the 2. ",
        "1 works at 2. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was his predecessor. ",
        "2 was his successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was his predecessor. ",
        "2 was his successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was his predecessor. ",
        "2 was his successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was his predecessor. ",
        "2 was his successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in office 2 from 3. ",
        "1 worked in office 2 till 3. ",
        "1 worked in 2. ",
        "2 was his predecessor. ",
        "2 was his successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was his predecessor. ",
        "2 was his successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was his predecessor. ",
        "2 was his successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was his predecessor. ",
        "2 was his successor. ",
        "1 worked in the fields of 2. ",
        "1 has worked for term 2. ",
        "1 has been active in years 2. ",
        "1 won the award for 2. ",
        "1 received the honor of 2. ",
        "1 is known for 2. ",
        "1 did notable works 2. ",
        "1 is assosciated with political party 2. ",
        "1 was born on 2 in 3. ",
        "1 was born on 2. ",
        "1 was born in 2. ",
        "1 was born to parents 2. ",
        "1 was born to mother 1 and father 2. ",
        "1 was born to father 2. ",
        "1 was born to mother 2. ",
        "1 has relaives 2. ",
        # "2 is his spouse. ",
        "2 is his partner. ",
        "1 has children - 2. ",
        "His hometown is 2. ",
        "His alma mater is 2. ",
        "1 is educated from 2. ",
        "1 is a citizen of 2. ",
        "1 resides in 2. ",
        "1 passed away on 2 in 3. ",
        "1 passed away on 2. ",
        "1 passed away in 2. ",
        "2 was his predecessor. ",
        "1 was succeeded by 2. ",
        "1 is a board member of 2. ",
        "1 has a net worth of 2. ",
        "1 has a salary of 2. ",
        "You can know more about him on 2. "
    ]

    paraf_sentences = [

        "1 is a 2. ",
        "1 has 2 nationality. ",
        "1 is the 2. ",
        "1 works at 2. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was her predecessor. ",
        "2 was her successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was her predecessor. ",
        "2 was her successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was her predecessor. ",
        "2 was her successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was her predecessor. ",
        "2 was her successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in office 2 from 3. ",
        "1 worked in office 2 till 3. ",
        "1 worked in 2. ",
        "2 was her predecessor. ",
        "2 was her successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was her predecessor. ",
        "2 was her successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was her predecessor. ",
        "2 was her successor. ",
        "1 worked at 2 from 3 till 4. ",
        "1 works in 2 from 3. ",
        "1 worked in 2 till 3. ",
        "1 worked in 2. ",
        "2 was her predecessor. ",
        "2 was her successor. ",
        "1 worked in the fields of 2. ",
        "1 has worked for term 2. ",
        "1 has been active in years 2. ",
        "1 won the award for 2. ",
        "1 received the honor of 2. ",
        "1 is known for 2. ",
        "1 did notable works 2. ",
        "1 is assosciated with political party 2. ",
        "1 was born on 2 in 3. ",
        "1 was born on 2. ",
        "1 was born in 2. ",
        "1 was born to parents 2. ",
        "1 was born to mother 1 and father 2. ",
        "1 was born to father 2. ",
        "1 was born to mother 2. ",
        "1 has relaives 2. ",
        "2 is her partner. ",
        "1 has children - 2. ",
        "Her hometown is 2. ",
        "Her alma mater is 2. ",
        "1 is educated from 2. ",
        "1 is a citizen of 2. ",
        "1 resides in 2. ",
        "1 passed away on 2 in 3. ",
        "1 passed away on 2. ",
        "1 passed away in 2. ",
        "2 was her predecessor. ",
        "1 was succeeded by 2. ",
        "1 is a board member of 2. ",
        "1 has a net worth of 2. ",
        "1 has a salary of 2. ",
        "You can know more about her on 2. "
    ]

    paragraph1 = ""
    for i in range(len(para1_keys)):
        f = 1
        for j in range(len(para1_keys[i])):
            x = para1_keys[i][j]
            if dict[x] == "NULL":
                f = 0
                break
        if f == 1:
            if dict["gender"] == "male":
                y = para1_sentences[i]
            else:
                y = paraf_sentences[i]
            sentence = ""
            for j in range(len(y)):
                if y[j].isdigit():
                    z = int(y[j])-1
                    w = para1_keys[i][z]
                    sentence += dict[w]
                    if w != "name":
                        dict[w] = "NULL"
                    if w == "name":
                        if dict["gender"] == "female":
                            dict["name"] = "She"
                        else:
                            dict["name"] = "He"

                else:
                    sentence += y[j]
            paragraph1 += sentence

    if dict["gender"] == "female":
        w = 5
    paragraph1 = str(paragraph1)
    # output_paras.append(paragraph1)
    json_object = json.dumps(paragraph1, indent=4)
    with open("generated_templates.json", "w") as outfile:
        outfile.write(json_object)
