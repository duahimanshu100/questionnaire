import csv
from questionnaire.settings import BASE_DIR


def get_all_questions_answer():
    data_source = 'CSV'
    if data_source == 'CSV':
        return get_data_from_csv(BASE_DIR + '/app/' + 'sample messages.csv')


def get_data_from_csv(input_file):
    with open(input_file, 'rb') as csvfile:
        questionnaire_reader = csv.reader(csvfile)
        return [row for row in questionnaire_reader]


def pre_process_data(data):
    lst_questions = [row[0] for row in data]
    dic_questionnaire = dict(data)
    return lst_questions, dic_questionnaire


def pridict_answer(query, limit=3, min_confidence=70):
    lst_questions, dic_questionnaire = pre_process_data(
        get_all_questions_answer())
    from fuzzywuzzy import process
    predicted_questions = process.extract(query,
                                          lst_questions, limit=limit)
    pridicted = []
    for item in predicted_questions:
        if min_confidence <= item[1]:
            pridicted.append(dic_questionnaire[item[0]])
            # pridicted.append((item[0], item[1], dic_questionnaire[item[0]]))
    return pridicted
