import random
import time
import os

ROUNDS = 10

MODE = {
    "Easy": 5,
    "Med": 6,
    "Less hard": 7,
    "Hard": 8,
    "Extremely difficult": 9
}

# =====================================
# CLEAR SCREEN
# =====================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# =====================================
# INVERT BINARY
# =====================================

def invert_bits(binary):

    result = ""

    for bit in binary:

        if bit == "1":
            result += "0"

        else:
            result += "1"

    return result

# =====================================
# GRADE SYSTEM
# =====================================

def grade(percent, full_combo):

    if full_combo:
        return "A+ (Full Combo!)"

    elif percent >= 75:
        return "A"

    elif percent >= 65:
        return "B"

    elif percent >= 50:
        return "C"

    else:
        return "D"

# =====================================
# GAME
# =====================================

def play_game(diff_name):

    BIT_LENGTH = MODE[diff_name]
    MAX_SCORE = BIT_LENGTH * ROUNDS

    progress = "0000000000"
    round_scores = []

    for round_num in range(1, ROUNDS + 1):

        clear()

        binary = ""

        for _ in range(BIT_LENGTH):
            binary += random.choice("01")

        answer = invert_bits(binary)

        # current x position
        display_progress = (
            progress[:round_num - 1]
            + "x"
            + progress[round_num:]
        )

        # dashboard
        print("------------------------------------------------")
        print(f"ROUND({round_num}/{ROUNDS})   |  {display_progress}")
        print(f"DIFF: {diff_name}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

        print("----     " + binary + "     ---")
        print()

        user = input("+++      ")

        print()

        check_line = ""
        correct_count = 0

        for i in range(BIT_LENGTH):

            if i < len(user) and user[i] == answer[i]:

                check_line += "✓"
                correct_count += 1

            else:

                check_line += "×"

        print("#########" + check_line + "##########")

        round_scores.append(correct_count)

        # update progress
        if correct_count == BIT_LENGTH:

            progress = (
                progress[:round_num - 1]
                + "C"
                + progress[round_num:]
            )

        else:

            progress = (
                progress[:round_num - 1]
                + str(correct_count)
                + progress[round_num:]
            )

        print()
        print("CORRECT:", answer)
        print("BIT SCORE:", correct_count)

        time.sleep(2)

    # =====================================
    # FINAL RESULT
    # =====================================

    clear()

    score = sum(round_scores)

    if len(round_scores) > 0:

        formula_score = (
            ROUNDS
            * ((round_scores[0] + round_scores[-1]) / 2)
        )

    else:

        formula_score = 0

    percent = (score / MAX_SCORE) * 100

    full_combo = score == MAX_SCORE

    rank = grade(percent, full_combo)

    print("======================================")
    print("       RE√(E)Rt COMPLETE")
    print("======================================")
    print()

    print("PROGRESS :", progress + "x")
    print()

    print("TOTAL SCORE :", score, "/", MAX_SCORE)
    print(f"PERCENT     : {percent:.1f}%")
    print(f"FORMULA     : {formula_score:.1f}")

    print()
    print("RANK:", rank)
    print()

    if full_combo:

        print("STATUS: FULL CLEAR ☠️")

    elif percent >= 75:

        print("STATUS: CASIO GOD 😈")

    elif percent >= 50:

        print("STATUS: TERMINAL USER 😏")

    else:

        print("STATUS: HUMAN ERROR ☠️")

    print()

    input("Press Enter to return...")

# =====================================
# MAIN MENU
# =====================================

while True:

    clear()

    print("""=========================================================
                        RE√(E)Rt
             Convert the binary is never boring                          
 alpha0.0.1 ==============================================""")
    print()

    print("[1] PLAY GAME")
    print("[2] HTP")
    print("[3] EXIT")

    print()

    choice = input("SELECT > ")

    # =====================================
    # PLAY
    # =====================================

    if choice == "1":

        while True:

            clear()

            print("======================================")
            print("          SELECT DIFFICULTY")
            print("======================================")
            print()

            print("[1] EASY")
            print("[2] MED")
            print("[3] LESS HARD")
            print("[4] HARD")
            print("[5] EXTREMELY DIFFICULT")
            print("[6] BACK")

            print()

            diff = input("SELECT > ")

            if diff == "1":

                play_game("Easy")
                break

            elif diff == "2":

                play_game("Med")
                break

            elif diff == "3":

                play_game("Less hard")
                break

            elif diff == "4":

                play_game("Hard")
                break

            elif diff == "5":

                play_game("Extremely difficult")
                break

            elif diff == "6":

                break

            else:

                print()
                print("UNKNOWN OPTION ☠️")
                time.sleep(1)

    # =====================================
    # HOW TO PLAY
    # =====================================

    elif choice == "2":

        clear()

        print("======================================")
        print("             HOW TO PLAY")
        print("======================================")
        print()

        print("Convert all bits to opposite form.")
        print()

        print("0 -> 1")
        print("1 -> 0")

        print()

        print("EXAMPLE:")
        print()

        print("101001")
        print("010110")

        print()

        print("C = FULL CLEAR")
        print("x = CURRENT ROUND")

        print()

        print("RANK SYSTEM:")
        print("A+ = FULL COMBO")
        print("A  = 75%+")
        print("B  = 65%+")
        print("C  = 50%+")
        print("D  = BELOW 50%")

        print()

        input("Press Enter to return...")

    # =====================================
    # EXIT
    # =====================================

    elif choice == "3":

        clear()

        print("Shutting down RE√(E)Rt...")
        time.sleep(1)

        print("Saving memory...")
        time.sleep(1)

        print("Session terminated.")
        time.sleep(1)

        break

    # =====================================
    # INVALID
    # =====================================

    else:

        print()
        print("UH... Is look like your command doesn't exist")
        time.sleep(2.3)