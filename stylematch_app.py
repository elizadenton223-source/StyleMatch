import flet as ft


# COLOURS
PINK = "#B46F83"
DARK_PINK = "#7D4558"
LIGHT_PINK = "#FBEFF0"
WHITE = "#FFFFFF"
SOFT_GREY = "#8B737B"


def main(page: ft.Page):

    page.title = "StyleMatch"
    page.bgcolor = LIGHT_PINK
    page.padding = 25
    page.scroll = ft.ScrollMode.AUTO

    # SIX QUIZ QUESTIONS
    questions = [
        {
            "question": "What is your go-to everyday outfit?",
            "answers": [
                "Neutral top and jeans",
                "Something trendy",
                "Blazer and tailored pants",
                "Activewear and sneakers"
            ]
        },
        {
            "question": "Which shoes would you choose?",
            "answers": [
                "Simple white sneakers",
                "Statement boots",
                "Classic loafers",
                "Running sneakers"
            ]
        },
        {
            "question": "What's your favourite colour palette?",
            "answers": [
                "Neutral colours",
                "Bright and trending colours",
                "Black, white and navy",
                "Earthy and casual colours"
            ]
        },
        {
            "question": "What would you wear to dinner?",
            "answers": [
                "Simple dress and jewellery",
                "A statement outfit",
                "Tailored pants and a nice top",
                "Jeans and sneakers"
            ]
        },
        {
            "question": "What's most important when choosing clothes?",
            "answers": [
                "Simplicity",
                "Following trends",
                "Timelessness",
                "Comfort"
            ]
        },
        {
            "question": "Which item would you buy?",
            "answers": [
                "A basic white T-shirt",
                "A statement piece",
                "A tailored blazer",
                "A matching activewear set"
            ]
        }
    ]

    # STYLE CATEGORIES
    styles = [
        "Minimalist",
        "Trendy",
        "Classic",
        "Sporty"
    ]

    # STARTING SCORES
    scores = {
        "Minimalist": 0,
        "Trendy": 0,
        "Classic": 0,
        "Sporty": 0
    }

    current_question = 0

    # PERSONALISED STYLE DESCRIPTIONS
    descriptions = {

        "Minimalist": (
            "Your style is effortless, simple and timeless. "
            "You love neutral colours, clean silhouettes "
            "and versatile wardrobe essentials."
        ),

        "Trendy": (
            "You love experimenting with fashion! "
            "Statement pieces, current trends and bold "
            "outfits are your go-to."
        ),

        "Classic": (
            "Your style is polished and sophisticated. "
            "You gravitate towards tailored pieces, "
            "timeless outfits and elegant details."
        ),

        "Sporty": (
            "Your style is relaxed, comfortable and practical. "
            "You love sneakers, casual outfits and "
            "effortless everyday dressing."
        )
    }

    # PERSONALISED OUTFIT RECOMMENDATIONS
    outfits = {

        "Minimalist": {
            "top": "White fitted T-shirt",
            "bottom": "Straight-leg blue jeans",
            "shoes": "White leather sneakers",
            "accessory": "Simple gold jewellery"
        },

        "Trendy": {
            "top": "Statement top",
            "bottom": "Low-rise wide-leg jeans",
            "shoes": "Statement boots",
            "accessory": "Bold shoulder bag"
        },

        "Classic": {
            "top": "Tailored blazer",
            "bottom": "Black tailored trousers",
            "shoes": "Leather loafers",
            "accessory": "Structured handbag"
        },

        "Sporty": {
            "top": "Oversized T-shirt",
            "bottom": "Matching activewear shorts",
            "shoes": "Running sneakers",
            "accessory": "Baseball cap"
        }
    }

    # CREATE A PINK BUTTON
    def pink_button(text, action):

        return ft.Button(
            content=text,
            bgcolor=PINK,
            color=WHITE,
            height=55,
            width=290,
            on_click=action
        )

    # CREATE AN ANSWER BUTTON
    def answer_button(text, style):

        return ft.Button(
            content=text,
            bgcolor=WHITE,
            color=DARK_PINK,
            height=55,
            width=290,
            on_click=lambda e: choose_answer(style)
        )

    # SAVE ANSWER AND MOVE TO NEXT QUESTION
    def choose_answer(style):

        nonlocal current_question

        scores[style] += 1
        current_question += 1

        if current_question < len(questions):
            show_question()
        else:
            show_result()

    # DISPLAY THE CURRENT QUESTION
    def show_question():

        page.clean()

        question = questions[current_question]

        progress = current_question / len(questions)

        page.add(
            ft.Column(
                controls=[

                    ft.Text(
                        "stylematch ♡",
                        size=30,
                        color=DARK_PINK,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(
                        f"QUESTION {current_question + 1} OF 6",
                        size=13,
                        color=SOFT_GREY
                    ),

                    ft.ProgressBar(
                        value=progress,
                        color=PINK,
                        bgcolor="#EBD4DA",
                        width=290
                    ),

                    ft.Container(height=15),

                    ft.Text(
                        question["question"],
                        size=26,
                        color=DARK_PINK,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Container(height=15),

                    *[
                        answer_button(answer, styles[index])
                        for index, answer in enumerate(
                            question["answers"]
                        )
                    ],

                    ft.Container(height=15),

                    ft.Text(
                        "Choose the answer that feels most like you ♡",
                        size=12,
                        color=SOFT_GREY,
                        text_align=ft.TextAlign.CENTER
                    )

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        )

    # DISPLAY THE FINAL RESULT
    def show_result():

        page.clean()

        result = max(scores, key=scores.get)

        outfit = outfits[result]

        page.add(
            ft.Column(
                controls=[

                    ft.Text(
                        "stylematch ♡",
                        size=30,
                        color=DARK_PINK,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Container(height=20),

                    ft.Text(
                        "YOUR STYLE PROFILE",
                        size=14,
                        color=SOFT_GREY
                    ),

                    ft.Text(
                        result.upper(),
                        size=38,
                        weight=ft.FontWeight.BOLD,
                        color=DARK_PINK,
                        text_align=ft.TextAlign.CENTER
                    ),

                    # STYLE DESCRIPTION
                    ft.Container(
                        content=ft.Text(
                            descriptions[result],
                            size=17,
                            color=DARK_PINK,
                            text_align=ft.TextAlign.CENTER
                        ),

                        bgcolor=WHITE,
                        padding=25,
                        border_radius=20,
                        width=320
                    ),

                    ft.Container(height=15),

                    # STYLE SCORES
                    ft.Text(
                        "Your style scores",
                        size=18,
                        color=DARK_PINK,
                        weight=ft.FontWeight.BOLD
                    ),

                    *[
                        ft.Text(
                            f"{style}: {score}",
                            size=15,
                            color=DARK_PINK
                        )
                        for style, score in scores.items()
                    ],

                    ft.Container(height=20),

                    # OUTFIT RECOMMENDATION HEADING
                    ft.Text(
                        "YOUR OUTFIT EDIT ♡",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=DARK_PINK
                    ),

                    # OUTFIT RECOMMENDATION CARD
                    ft.Container(
                        content=ft.Column(
                            controls=[

                                ft.Text(
                                    "TOP: " + outfit["top"],
                                    size=15,
                                    color=DARK_PINK
                                ),

                                ft.Text(
                                    "BOTTOM: " + outfit["bottom"],
                                    size=15,
                                    color=DARK_PINK
                                ),

                                ft.Text(
                                    "SHOES: " + outfit["shoes"],
                                    size=15,
                                    color=DARK_PINK
                                ),

                                ft.Text(
                                    "ACCESSORY: " + outfit["accessory"],
                                    size=15,
                                    color=DARK_PINK
                                )

                            ],

                            spacing=12
                        ),

                        bgcolor=WHITE,
                        padding=25,
                        border_radius=20,
                        width=320
                    ),

                    ft.Container(height=20),

                    # RESTART BUTTON
                    pink_button(
                        "Try Again ♡",
                        restart_quiz
                    )

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12
            )
        )

    # RESTART QUIZ AND RESET SCORES
    def restart_quiz(e):

        nonlocal current_question

        current_question = 0

        for style in scores:
            scores[style] = 0

        show_question()

    # START QUIZ
    def start_quiz(e):
        show_question()

    # WELCOME SCREEN
    page.add(
        ft.Column(
            controls=[

                ft.Container(height=60),

                ft.Text(
                    "stylematch ♡",
                    size=42,
                    color=DARK_PINK,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Text(
                    "YOUR PERSONAL STYLE EDIT",
                    size=13,
                    color=SOFT_GREY
                ),

                ft.Container(height=30),

                ft.Container(
                    content=ft.Column(
                        controls=[

                            ft.Text(
                                "Your style starts here.",
                                size=28,
                                color=DARK_PINK,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER
                            ),

                            ft.Text(
                                "Answer six quick questions "
                                "and discover your personal "
                                "fashion identity.",
                                size=16,
                                color=SOFT_GREY,
                                text_align=ft.TextAlign.CENTER
                            )

                        ],

                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15
                    ),

                    bgcolor=WHITE,
                    padding=30,
                    border_radius=20,
                    width=320
                ),

                ft.Container(height=25),

                pink_button(
                    "Find my style ♡",
                    start_quiz
                ),

                ft.Container(height=20),

                ft.Text(
                    "A personalised fashion experience",
                    size=12,
                    color=SOFT_GREY
                )

            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )


ft.run(main)