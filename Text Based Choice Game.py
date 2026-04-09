def invalid_choice():
    print("Not a valid option. You lose.")

play_again = "yes"

while play_again == "yes":
    name = input("Type your name: ").strip().title()
    print("Welcome", name, "to this epic adventure!")

    school_choice = input(
        "Your time in primary school has come to an end.\n"
        "You can go to either\n"
        "1. Crawford Sandton\n"
        "2. Hyde Park High School.\n"
        "Your choice: "
    ).strip().lower()

    if school_choice in ["1", "crawford sandton"]:
        second_school_choice = input(
            "The school fees are too expensive after 1 year.\n"
            "St. Davids show interest after one of their soccer coaches scouts you.\n"
            "You can go to either\n"
            "1. St. Davids\n"
            "2. Hyde Park High School\n"
            "Your choice: "
        ).strip().lower()

        if second_school_choice in ["1", "st. davids"]:
            print(
                "You go to St. Davids the following year but decide to leave\n"
                "after the first term because you don't like\n"
                "that it's an all-boys school."
            )
        elif second_school_choice in ["2", "hyde park high school"]:
            print("You finish your high school years at Hyde Park and face lots of trials and tribulations.")
        else:
            invalid_choice()

    elif school_choice in ["2", "hyde park high school"]:
        subject_choice = input(
            "When grade 10 comes, the last 2 subjects you can pick between are\n"
            "1. History\n"
            "2. Physics\n"
            "Your choice: "
        ).strip().lower()

        if subject_choice in ["2", "physics"]:
            print("You choose Physics and struggle in the subject.")
        elif subject_choice in ["1", "history"]:
            ap_english_offer = input(
                "You choose History and get offered to take AP English\n"
                "due to your good essay writing skills.\n"
                "Do you accept the offer? (yes/no)\n"
                "Your choice: "
            ).strip().lower()

            if ap_english_offer == "yes":
                print("You accept the AP English offer and pass with 60%. Congratulations!")
            elif ap_english_offer == "no":
                print("You decline the offer but still pass all your subjects with Cs.")
            else:
                invalid_choice()
        else:
            invalid_choice()
    else:
        invalid_choice()

    print("Thank you", name, "for playing!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

print("Goodbye!")