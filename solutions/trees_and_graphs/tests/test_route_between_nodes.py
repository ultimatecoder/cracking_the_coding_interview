from .. import route_between_nodes


def test_is_route_exists():
    sample_inputs_and_expected_answers = (
        (
            {
                1: [3],
                3: [8, 4, 6],
                8: [1],
                4: [6],
                6: []
            },
            1,
            6,
            True
        ),
        (
            {}, 1, 12, False
        ),
        (
            {
                1: [1]
            },
            1,
            1,
            True
        ),
        (
            {
                1: [2],
                2: [3],
                3: [4],
                4: [5],
            },
            4,
            1,
            False
        ),
        (
            {
                1: [2],
                2: [3],
                3: [4],
                4: [5],
            },
            3,
            4,
            True
        )
    )
    for graph, start, end, expected_answer in (
        sample_inputs_and_expected_answers
    ):
        assert route_between_nodes.is_route_exists(
            graph, start, end
        ) == expected_answer
