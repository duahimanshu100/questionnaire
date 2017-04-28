import csv


def get_all_questions_answer():
    data_source = 'CSV'
    if data_source == 'CSV':
        return get_data_from_csv('sample messages.csv')


def get_data_from_csv(input_file):
    with open(input_file, 'rb') as csvfile:
        questionnaire_reader = csv.reader(csvfile)
        return [row for row in questionnaire_reader]

print(get_all_questions_answer())
