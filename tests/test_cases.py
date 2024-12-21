TEST_CASES = [
    (
        [
            "  @---A---+",
            "          |",
            "  x-B-+   C",
            "      |   |",
            "      +---+",
        ],
        ("@---A---+|C|+---+|+-B-x", "ACB"),
        "Basic example",
    ),
    (
        [
            "  @",
            "  | +-C--+",
            "  A |    |",
            "  +---B--+",
            "    |      x",
            "    |      |",
            "    +---D--+",
        ],
        ("@|A+---B--+|+--C-+|-||+---D--+|x", "ABCD"),
        "Passing though example",
    ),
    (
        [
            "  @---A---+",
            "          |",
            "  x-B-+   |",
            "      |   |",
            "      +---C",
        ],
        ("@---A---+|||C---+|+-B-x", "ACB"),
        "Turn on letters",
    ),
    (
        [
            "     +-O-N-+",
            "     |     |",
            "     |   +-I-+",
            " @-G-O-+ | | |",
            "     | | +-+ E",
            "     +-+     S",
            "             |",
            "             x",
        ],
        ("@-G-O-+|+-+|O||+-O-N-+|I|+-+|+-I-+|ES|x", "GOONIES"),
        "Don't collect letters twice",
    ),
    (
        [
            "     x",
            "     |",
            "@----A-+",
            "   +-+ |",
            "   |   |",
            "   +---+",
        ],
        ("@----A-+||+---+|+-+A|x", "A"),
        "Turn to a visited field after +",
    ),
    (
        [
            " +-L-+",
            " |  +A-+",
            "@B+ ++ H",
            " ++    x",
        ],
        ("@B+++B|+-L-+A+++A-+Hx", "BLAH"),
        "BLAH",
    ),
    (
        [
            "  @-A--+",
            "       |",
            "       +-B--x-C--D",
        ],
        ("@-A--+|+-B--x", "AB"),
        "Ignore letters after ending",
    ),
    (
        [
            "  x",
            "  C",
            " @--+",
            "+---A",
            "| B",
            "+-+",
        ],
        ("@--+A---+|+-+B--Cx", "ABC"),
        "Pass through double intersection",
    ),
    (
        [
            "     x",
            "     |",
            "@-A-+B",
            "    ||",
            "    ++",
        ],
        ("@-A-+|++|B|x", "AB"),
        "At + ignore the field in front",
    ),
    (
        [
            "   +--+",
            "@---+ |",
            " xCBA-+",
            "   ||",
            "   ++",
        ],
        ("@---+A|++|B-+--+|+-ABCx", "ABC"),
        "At + ignore the pathway in wrong direction",
    ),
]

TEST_CASES_WITH_ERRORS = [
    (
        [
            "   x",
            "   |",
            "@--|-+",
            "   +-+",
        ],
        "Pass through, wrong crossing order",
    ),
    (
        [
            "  +----+",
            "  |    |",
            "+------+",
            "| @--+",
            "+----+",
            "  |",
            "  x",
        ],
        "Cannot pass through the @",
    ),
    (
        [
            "     x",
            "     |",
            "@------+",
            "   +-+ |",
            "   |   |",
            "   +---+",
        ],
        "Cannot turn to the pathway in wrong direction",
    ),
    (
        [
            "      A---+",
            "          |",
            "  x-B-+   C",
            "      |   |",
            "      +---+",
        ],
        "No starting point",
    ),
    (
        [
            "   @--A---+",
            "          |",
            "    B-+   C",
            "      |   |",
            "      +---+",
        ],
        "No ending point",
    ),
    (
        [
            "   @--A-@-+",
            "          |",
            "  x-B-x+  C",
            "      |   |",
            "      +---+",
        ],
        "Two starting points",
    ),
    (
        [
            "        x-B",
            "          |",
            "   @--A---+",
            "          |",
            "     x+   C",
            "      |   |",
            "      +---+",
        ],
        "Fork at +",
    ),
    (
        [
            "   @--A-+",
            "        |",
            "         ",
            "      B-x",
        ],
        "No way to continue",
    ),
    (
        [
            "x-B-@-A-x",
        ],
        "Fork at @",
    ),
    (
        [
            "@-A-+-B-x",
        ],
        "Cannot go forward option after +",
    ),
]
