import csv
import definishions
import json
import logging
import os

file_for_testing = definishions.TEMP_FOLDER / 'random-michaels.csv'
file_for_testing_1 = definishions.TEMP_FOLDER / 'rmc.csv'
output_file = definishions.TEMP_FOLDER / 'result_Mysiakovska.csv'

data = set()
unique_rows = []

for file_path in [file_for_testing, file_for_testing_1]:
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_tuple = tuple(row)
            if row_tuple not in data:
                data.add(row_tuple)
                unique_rows.append(row)

with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_rows)

#Task 2

LOG_FILE_NAME = definishions.TEMP_FOLDER / "json__Mysiakovska.log"

logger = logging.getLogger("JSON_Validator")
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler(LOG_FILE_NAME, mode="w")
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)


for file_name in sorted(os.listdir(definishions.TEMP_FOLDER)):
    if file_name.endswith('.json'):
        file_path = definishions.TEMP_FOLDER / file_name

        try:
            with open(file_path) as f:
                json.load(f)
            print(f"{file_name} — valid JSON")
        except json.JSONDecodeError as error:
            logger.error(f"Invalid JSON in '{file_name}': {error.msg}")
            print(f"[ERROR] {file_name} — invalid JSON")
        except Exception as error:
            logger.error(f"Error reading '{file_name}': {error}")
            print(f"[ERROR] {file_name} — could not read file")


# Task 3

logger = logging.getLogger("XML_Finder")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

if not logger.handlers:
    logger.addHandler(console_handler)


def get_incoming_by_group_number(xml_file_path, group_number):
    with open(xml_file_path) as f:
        content = f.read()

    target_tag = f"<number>{group_number}</number>"
    groups = content.split("<group>")

    for group in groups:
        if target_tag in group:
            if "<incoming>" in group and "</incoming>" in group:
                incoming_value = group.split("<incoming>")[1].split("</incoming>")[0]

                logger.info(f"Group {group_number}: incoming = {incoming_value}")
                return incoming_value
            else:
                logger.info(f"Group {group_number}")
                return None

    logger.info(f"Group {group_number} not found")
    return None


file_path = definishions.TEMP_FOLDER / 'groups.xml'

# Тестуємо пошук:
print("RESULTS")
get_incoming_by_group_number(file_path, 0)
get_incoming_by_group_number(file_path, 2)
get_incoming_by_group_number(file_path, 3)
get_incoming_by_group_number(file_path, 4)
get_incoming_by_group_number(file_path, 5)

