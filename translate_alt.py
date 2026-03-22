#!/usr/bin/env python3
"""
Translate 8 SPH3U alt-text HTML files from English to Korean.
Uses str.replace() for each (English, Korean) pair.
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))
ALT_DIR = os.path.join(BASE, "course_content", "assets", "alt")

files = [
    "sph3u_01.01.070.html",
    "sph3u_01.01.120.html",
    "sph3u_01.02.13b.html",
    "sph3u_01.03.12a.html",
    "sph3u_01.04.04.html",
    "sph3u_01.04.05.html",
    "sph3u_01.05.09.html",
    "sph3u_a1.05.01.html",
]

# ── Per-file replacements (description body text) ──────────────────────

per_file = {
    # --- sph3u_01.01.070 ---
    "sph3u_01.01.070.html": [
        (
            "Waves can be divided into two types: mechanical waves (which need a medium) and electromagnetic waves (which can travel without a medium). Mechanical waves can be further subdivided into longitudinal waves (for example, sound waves) and transverse waves (for example, water waves).",
            "파동은 두 가지 유형으로 나눌 수 있습니다: 역학적 파동(매질이 필요한 파동)과 전자기파(매질 없이 전파될 수 있는 파동). 역학적 파동은 다시 종파(예: 음파)와 횡파(예: 수면파)로 세분할 수 있습니다.",
        ),
    ],

    # --- sph3u_01.01.120 ---
    "sph3u_01.01.120.html": [
        (
            "Diagram of a slinky spring, which has the labels for wave direction, rarefactions, and compressions, as well as arrows for particle and source (hand) motion.",
            "슬링키 스프링의 도해로, 파동의 진행 방향, 소(疏), 밀(密)이 표시되어 있으며, 입자의 운동 방향과 파원(손)의 운동 방향을 나타내는 화살표가 있습니다.",
        ),
    ],

    # --- sph3u_01.02.13b ---
    "sph3u_01.02.13b.html": [
        (
            "Diagram of the particle motion R (spread apart) and C (clustered together) when sound wave is generated in the air.",
            "공기 중에서 음파가 발생할 때 입자 운동을 나타낸 도해로, R(소: 입자가 퍼져 있는 부분)과 C(밀: 입자가 모여 있는 부분)가 표시되어 있습니다.",
        ),
    ],

    # --- sph3u_01.03.12a ---
    "sph3u_01.03.12a.html": [
        (
            'Three cycles of a wave. Label "a" marks a distance between two matching points on consecutive cycles. The wave starts on the centre line, then goes up to a high point labelled "b." It then goes down to a low point, with label "c" marking the distance between the middle line and the low point. Label "d" is on the next low point. Label "e" marks a distance from the first high point to the third high point.',
            '파동의 3주기를 나타낸 그림입니다. 레이블 "a"는 연속된 두 주기에서 대응하는 두 점 사이의 거리를 표시합니다. 파동은 중심선(평형 위치)에서 시작하여 위로 올라가 "b"로 표시된 마루(높은 점)에 도달합니다. 그런 다음 아래로 내려가 골(낮은 점)에 이르며, 레이블 "c"는 중심선과 골 사이의 거리를 나타냅니다. 레이블 "d"는 다음 골 위에 있습니다. 레이블 "e"는 첫 번째 마루에서 세 번째 마루까지의 거리를 표시합니다.',
        ),
    ],

    # --- sph3u_01.04.04 ---
    "sph3u_01.04.04.html": [
        (
            "Diagram of before, during and after constructive interference with crests\n                    that increase in size when they meet and returning back to normal afterwards.",
            "보강 간섭의 전, 중, 후를 나타낸 도해로, 두 마루가 만날 때 크기가 증가하고 이후 원래 상태로 돌아가는 모습을 보여줍니다.",
        ),
    ],

    # --- sph3u_01.04.05 ---
    "sph3u_01.04.05.html": [
        (
            "Diagram of before, during and after constructive interference with troughs\n                    that increase in size when they meet and returning back to normal afterwards.",
            "보강 간섭의 전, 중, 후를 나타낸 도해로, 두 골이 만날 때 크기가 증가하고 이후 원래 상태로 돌아가는 모습을 보여줍니다.",
        ),
    ],

    # --- sph3u_01.05.09 ---
    "sph3u_01.05.09.html": [
        (
            "Diagram showing four pendulums moving at the same time. Pendulum one is the\n                    longest. Pendulums 2 and 4 are the same length. Pendulum 3 is the shortest, at about half the length of 2 and 4.",
            "네 개의 진자가 동시에 운동하는 모습을 보여주는 도해입니다. 진자 1이 가장 길고, 진자 2와 4는 같은 길이이며, 진자 3은 가장 짧아 진자 2와 4 길이의 약 절반입니다.",
        ),
    ],

    # --- sph3u_a1.05.01 ---
    "sph3u_a1.05.01.html": [
        (
            "<p>Two waves moving toward each other. Each wave is six units long. </p>\n                    <p>Wave one: </p>\n                    <p>From the starting point, a vertical line up 2 units then right 2 units. Vertically down 4 units, then right 2 units. Followed by a diagonal line that is 2 units right and 4 units up, ending with a vertical line down 2 units to the starting displacement. </p>\n                    <p>Wave two: </p>\n                    <p>From the starting point, a diagonal line right 1 unit and up 2 units, followed by a vertical line up 2 units. Then a horizontal line right 2 units, followed by a diagonal line right 3 units and down 6 units, ending with a vertical line up 2 units to the starting displacement. </p>",
            "<p>서로를 향해 이동하는 두 개의 파동이 있습니다. 각 파동의 길이는 6단위입니다. </p>\n                    <p>파동 1: </p>\n                    <p>시작점에서 위로 2단위 수직선을 그린 다음 오른쪽으로 2단위 수평선을 긋습니다. 아래로 4단위 수직선, 그 다음 오른쪽으로 2단위 수평선을 긋습니다. 이어서 오른쪽 2단위, 위로 4단위의 대각선을 그리고, 아래로 2단위 수직선을 그어 시작 변위로 돌아갑니다. </p>\n                    <p>파동 2: </p>\n                    <p>시작점에서 오른쪽 1단위, 위로 2단위의 대각선을 그린 다음 위로 2단위 수직선을 긋습니다. 그 다음 오른쪽으로 2단위 수평선을 그리고, 오른쪽 3단위, 아래로 6단위의 대각선을 긋습니다. 마지막으로 위로 2단위 수직선을 그어 시작 변위로 돌아갑니다. </p>",
        ),
    ],
}

# ── Common replacements (shared across all files) ──────────────────────

common_replacements = [
    ('lang="en"', 'lang="ko"'),
    ("<title>Description</title>", "<title>설명</title>"),
    ("<h1>Description</h1>", "<h1>설명</h1>"),
    (
        "<p><strong>Warning!</strong> To ensure the greatest educational experience, this learning activity contains\n                aspects that require Javascript to be enabled.</p>",
        "<p><strong>경고!</strong> 최상의 학습 경험을 위해, 이 학습 활동에는 자바스크립트를 활성화해야 하는 요소가 포함되어 있습니다.</p>",
    ),
    (
        "<p><strong>Warning!</strong> To ensure the greatest educational experience, this learning activity contains\n        aspects that require Javascript to be enabled.</p>",
        "<p><strong>경고!</strong> 최상의 학습 경험을 위해, 이 학습 활동에는 자바스크립트를 활성화해야 하는 요소가 포함되어 있습니다.</p>",
    ),
]

# ── Process each file ──────────────────────────────────────────────────

for fname in files:
    fpath = os.path.join(ALT_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply common replacements
    for eng, kor in common_replacements:
        content = content.replace(eng, kor)

    # Apply per-file replacements
    for eng, kor in per_file[fname]:
        content = content.replace(eng, kor)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Translated: {fname}")

print("\nDone. All 8 files translated.")
