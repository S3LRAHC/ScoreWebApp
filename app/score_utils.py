def calculate_phoenix_score(res):
    # Convert all judgement counts to int
    perfect = int(res['PERFECT'])
    great = int(res['GREAT'])
    good = int(res['GOOD'])
    bad = int(res['BAD'])
    miss = int(res['MISS'])
    max_combo = int(res['MAX COMBO'])

    # Calculate the note weights - MISS does not add to score at all
    note_weights = perfect + 0.6 * great + 0.2 * good + 0.1 * bad

    # Find the total notes
    total_notes = perfect + great + good + bad + miss

    # Calculate total score
    return int(round(
        (0.995 * note_weights + 0.005 * max_combo) / total_notes * 1000000, 0
    ))


def get_letter_grade_and_plate(score, result):
    # Convert string values to integers
    result = {key: int(value) for key, value in result.items()}

    # Determine letter grade
    if score > 995000:
        letter_grade = "SSS+"
    elif 990000 <= score <= 994999:
        letter_grade = "SSS"
    elif 985000 <= score <= 989999:
        letter_grade = "SS+"
    elif 980000 <= score <= 984999:
        letter_grade = "SS"
    elif 975000 <= score <= 979999:
        letter_grade = "S+"
    elif 970000 <= score <= 974999:
        letter_grade = "S"
    elif 960000 <= score <= 969999:
        letter_grade = "AAA+"
    elif 950000 <= score <= 959999:
        letter_grade = "AAA"
    elif 925000 <= score <= 949999:
        letter_grade = "AA+"
    elif 900000 <= score <= 924999:
        letter_grade = "AA"
    elif 825000 <= score <= 899999:
        letter_grade = "A+"
    elif 750000 <= score <= 824999:
        letter_grade = "A"
    elif 650000 <= score <= 749999:
        letter_grade = "B"
    elif 550000 <= score <= 649999:
        letter_grade = "C"
    elif 450000 <= score <= 549999:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Determine plate designation
    if result['PERFECT'] > 0 and all(result[key] == 0 for key in ['GREAT', 'GOOD', 'BAD', 'MISS']):
        plate = "Perfect Game"
    elif result['PERFECT'] > 0 and result['GREAT'] > 0 and all(result[key] == 0 for key in ['GOOD', 'BAD', 'MISS']):
        plate = "Ultimate Game"
    elif all(result[key] == 0 for key in ['BAD', 'MISS']) and all(result[key] > 0
                                                                  for key in ['PERFECT', 'GREAT', 'GOOD']):
        plate = "Extreme Game"
    elif result['MISS'] == 0:
        plate = "Superb Game"
    elif result['MISS'] <= 5:
        plate = "Marvelous Game"
    elif result['MISS'] <= 10:
        plate = "Talented Game"
    elif result['MISS'] <= 20:
        plate = "Fair Game"
    else:
        plate = "Rough Game"

    return letter_grade, plate
