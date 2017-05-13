import csv
import re
from questionnaire.settings import BASE_DIR


def get_data_from_csv(input_file):
    with open(input_file, 'rb') as csvfile:
        questionnaire_reader = csv.reader(csvfile)
        return [row for row in questionnaire_reader]


def get_all_questions_answer():
    data_source = 'CSV'
    if data_source == 'CSV':
        input_file = BASE_DIR + '/app/' + 'sample messages.csv'
        return get_data_from_csv(input_file)


def pre_process_data(data, query=None):
    lst_mandatory_words = ['title', 'cancel', 'cancel order',
                           'measure', 'address', 'phone number',
                           'distance', 'return', 'feedback']
    query_word = None
    if query:
        words = query.split()
        for word in words:
            word = "".join(re.findall("[a-zA-Z0-9]+", word))
            if word in lst_mandatory_words:
                query_word = word
                break
    if query_word:
        data = [k for k in data if query_word in [i.lower()
                                                  for i in k[0].split()]]
    lst_questions = [row[0] for row in data]

    dic_questionnaire = dict(data)
    return lst_questions, dic_questionnaire


def pridict_answer(query, limit=3, min_confidence=60):
    lst_questions, dic_questionnaire = pre_process_data(
        get_all_questions_answer(), query)
    from fuzzywuzzy import process
    predicted_questions = process.extract(query,
                                          lst_questions, limit=limit)
    pridicted = []
    for item in predicted_questions:
        if min_confidence <= item[1]:
            pridicted.append(dic_questionnaire[item[0]])
            # pridicted.append((item[0], item[1], dic_questionnaire[item[0]]))
    return pridicted


def add_new_questionnaire(question, answer, input_file=None):
    data_source = 'CSV'
    if data_source == 'CSV':
        input_file = BASE_DIR + '/app/' + 'sample messages.csv'
        rows = check_question_exists(question, answer, input_file)
        if rows:
            writer = csv.writer(open(input_file, 'w'))
            writer.writerows(rows)
            return
        with open(input_file, 'a') as f:
            fields = [question, answer]
            writer = csv.writer(f)
            writer.writerow(fields)


def check_question_exists(question, answer, input_file):
    rows = get_data_from_csv(input_file)
    found = False
    for row in rows:
        if row[0] == question:
            row[1] = answer
            found = True
    if found:
        return rows
    return None
