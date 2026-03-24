#!/usr/bin/env python3
"""
Translate remaining SPH3U HTML files from English to Korean.
Uses str.replace() for each (English, Korean) pair.
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ─── File 1: sph3u_u1la5_assign1.html (assignment landing page) ───
f1 = os.path.join(BASE, "course_content", "assignments", "sph3u_u1la5_assign1.html")

with open(f1, "r", encoding="utf-8") as f:
    t = f.read()

t = t.replace('lang="en"', 'lang="ko"')
t = t.replace("<title>\n        1.5 Assignment: Waves and sound\n    </title>",
              "<title>\n        1.5 과제: 파동과 소리\n    </title>")
t = t.replace("1.5 Assignment: Waves and sound", "1.5 과제: 파동과 소리")  # h2
t = t.replace(
    "This is an Assessment of Learning, which is sued to evaluate your work based on established criteria and to assign a mark. Your Teacher Marker will provide you with feedback and a mark.",
    "이것은 학습 평가로, 정해진 기준에 따라 여러분의 과제를 평가하고 점수를 부여하는 데 사용됩니다. 담당 교사가 피드백과 점수를 제공합니다."
)
t = t.replace(
    "In this assignment, you will create full, thoughtful, well-formatted responses to a series of problems and questions involving light and waves. Where appropriate, you will apply significant digits and the GUESS (Given, unknown, equation, solve, statement) problem-solving structure presented in the course's learning activities.",
    "이 과제에서는 빛과 파동에 관한 일련의 문제와 질문에 대해 완전하고 사려 깊으며 체계적으로 서식을 갖춘 답변을 작성합니다. 적절한 경우 유효 숫자와 GUESS(주어진 것, 미지수, 공식, 풀이, 서술) 문제 풀이 구조를 적용합니다."
)
t = t.replace(
    "Your assignment will be typed, using a word processor and an equation editor for any mathematical work. Images can be created on a computer or drawn on blank paper with a ruler and pen or dark pencil, and carefully scanned. Images should be inserted into your assignment at the appropriate place – not attached separately.",
    "과제는 워드 프로세서와 수식 편집기를 사용하여 작성해야 합니다. 이미지는 컴퓨터로 만들거나 빈 종이에 자와 펜 또는 진한 연필로 그린 후 주의 깊게 스캔할 수 있습니다. 이미지는 과제의 적절한 위치에 삽입해야 하며, 별도로 첨부하지 마십시오."
)
t = t.replace(
    "You will use the feedback on this assignment to improve your mathematical and scientific expression in future work, and to ensure you have the knowledge needed for future units in this course.",
    "이 과제에 대한 피드백을 활용하여 향후 과제에서 수학적, 과학적 표현을 개선하고, 이 과정의 이후 단원에 필요한 지식을 갖추도록 합니다."
)
t = t.replace("This assignment is worth 10% of your course grade.", "이 과제는 전체 성적의 10%를 차지합니다.")
t = t.replace("Instructions", "지시 사항")
t = t.replace(
    '1. Access the following printable document: <a href="../assets/locker_docs/sph3u_01.05_Assignment_doc.html" target="_blank">Waves and sound assignment<span class="sr-only">Opens in a new window</span></a>.',
    '1. 다음 인쇄용 문서를 여십시오: <a href="../assets/locker_docs/sph3u_01.05_Assignment_doc.html" target="_blank">파동과 소리 과제<span class="sr-only">새 창에서 열림</span></a>.'
)
t = t.replace(
    "2. In an electronic file (.docx or .pdf), provide a full solution to each question that adheres to the formatting guidelines provided later on this page. You do not need to copy the question, but should ensure that all answers are numbered appropriately.",
    "2. 전자 파일(.docx 또는 .pdf)로 이 페이지 아래에 제공된 서식 지침에 따라 각 문제에 대한 완전한 풀이를 작성하십시오. 문제를 복사할 필요는 없지만, 모든 답안에 적절한 번호를 매기십시오."
)
t = t.replace(
    "3. Use the GUESS problem-solving format where appropriate, and show all work. Pay particular attention to significant digits.",
    "3. 적절한 경우 GUESS 문제 풀이 형식을 사용하고, 모든 풀이 과정을 보여 주십시오. 유효 숫자에 특히 주의하십시오."
)
t = t.replace(
    "4. Where diagrams are needed, draw them on paper using a dark pen or pencil and scan or photograph them carefully; or create them digitally and insert them in the appropriate place in your file.",
    "4. 도표가 필요한 경우, 진한 펜이나 연필로 종이에 그린 후 주의 깊게 스캔하거나 촬영하십시오. 또는 디지털로 작성하여 파일의 적절한 위치에 삽입하십시오."
)
t = t.replace("5. Add your name to your file.", "5. 파일에 이름을 기재하십시오.")
t = t.replace("6. Submit your solutions by following the directions below.", "6. 아래 지시에 따라 풀이를 제출하십시오.")
t = t.replace(
    "Your Teacher Marker will grade and provide feedback on your work using the following success criteria and rubric. Before submitting your assignment, review the success criteria and rubric. If you need guidance about how to format your assignments, citations, or what constitutes plagiarism, please review the following support pages:",
    "담당 교사가 다음 성공 기준과 평가 기준표를 사용하여 과제를 채점하고 피드백을 제공합니다. 과제를 제출하기 전에 성공 기준과 평가 기준표를 검토하십시오. 과제 서식, 인용, 또는 표절에 대한 안내가 필요하면 다음 지원 페이지를 참조하십시오:"
)
t = t.replace(
    'Referencing and Formatting Submission Guidelines<span class="sr-only"> (Opens in new window)</span>',
    '참고 문헌 및 서식 제출 지침<span class="sr-only"> (새 창에서 열림)</span>'
)
t = t.replace(
    'Avoiding Plagiarism Guide <span class="sr-only"> (Opens in new window)</span>',
    '표절 방지 안내서 <span class="sr-only"> (새 창에서 열림)</span>'
)
t = t.replace(
    'Science and Mathematics Submission Requirements<span class="sr-only"> (Opens in new window)</span>',
    '과학 및 수학 제출 요건<span class="sr-only"> (새 창에서 열림)</span>'
)
t = t.replace("Success criteria and rubric", "성공 기준 및 평가 기준표")
t = t.replace("I have provided a full solution to each question", "각 문제에 대한 완전한 풀이를 작성했습니다")
t = t.replace("My solutions are correct", "풀이가 정확합니다")
t = t.replace("Each question's solution is clearly labelled", "각 문제의 풀이에 명확한 번호가 매겨져 있습니다")
t = t.replace("My solutions follow the Science and Mathematics Submission Requirements", "풀이가 과학 및 수학 제출 요건을 따릅니다")
t = t.replace("My work is in a logical order and easy to follow", "과제가 논리적인 순서로 작성되어 있고 따라가기 쉽습니다")
t = t.replace("My work uses physics conventions, vocabulary, and terminology", "과제가 물리학의 규칙, 어휘 및 용어를 사용합니다")
t = t.replace("My work demonstrates knowledge and understanding of Unit 1", "과제가 1단원의 지식과 이해를 보여 줍니다")
t = t.replace("I have reflected on each answer to ensure that it is reasonable and fully responds to the problem", "각 답이 합리적이며 문제에 완전히 답하는지 검토했습니다")
t = t.replace("I use science vocabulary and notation in my solutions and explanations", "풀이와 설명에 과학 어휘와 표기법을 사용했습니다")
t = t.replace("I have applied my knowledge and skills to the best of my ability", "지식과 기술을 최선을 다해 적용했습니다")
t = t.replace(
    "Please note that you will not be able to access your assignment rubric until all previous assignments have been graded and returned to you.",
    "이전 과제가 모두 채점되어 반환될 때까지 과제 평가 기준표에 접근할 수 없습니다."
)
t = t.replace(
    'Press the <strong>Rubric</strong> button to access it.',
    '<strong>평가 기준표</strong> 버튼을 눌러 접근하십시오.'
)
t = t.replace("How to submit your assignment", "과제 제출 방법")
t = t.replace(
    "Please note that you will not be able to submit your assignment and the submission space will not appear until all previous assignments have been graded and returned to you.",
    "이전 과제가 모두 채점되어 반환될 때까지 과제를 제출할 수 없으며 제출 공간이 나타나지 않습니다."
)
t = t.replace(
    "Before you submit your assignment for grading, check your assignment for plagiarism using Turnitin. Please note that Turnitin is a tool to self-check your work, teacher feedback will not be provided. To learn more about how to use the Turnitin tool please review the following support page:",
    "과제를 채점을 위해 제출하기 전에 Turnitin을 사용하여 표절 여부를 확인하십시오. Turnitin은 자가 점검 도구이며 교사 피드백은 제공되지 않습니다. Turnitin 도구 사용 방법에 대해 자세히 알아보려면 다음 지원 페이지를 참조하십시오:"
)
t = t.replace(
    'Turnitin for Assignments Guide<span class="sr-only"> (Opens in new window)</span>',
    'Turnitin 과제 안내서<span class="sr-only"> (새 창에서 열림)</span>'
)
t = t.replace(
    'When you are ready, self-check your work by pressing the <strong>Turnitin</strong> button, then follow the submission directions.',
    '준비가 되면 <strong>Turnitin</strong> 버튼을 눌러 과제를 자가 점검한 후 제출 지시를 따르십시오.'
)
t = t.replace(
    'When you are ready, submit your assignment by pressing the <strong>Submit Your Work</strong> button and follow the submission directions.',
    '준비가 되면 <strong>과제 제출</strong> 버튼을 눌러 과제를 제출하고 제출 지시를 따르십시오.'
)
# noscript warning
t = t.replace(
    '<strong>Warning!</strong> To ensure the greatest educational experience, this learning activity contains aspects that require Javascript to be enabled.',
    '<strong>경고!</strong> 최상의 학습 경험을 위해 이 학습 활동에는 Javascript가 활성화되어야 하는 요소가 포함되어 있습니다.'
)
# sr-only texts
t = t.replace('<span class="sr-only">(opens in a new window)</span>', '<span class="sr-only">(새 창에서 열림)</span>')

with open(f1, "w", encoding="utf-8") as f:
    f.write(t)
print(f"[OK] {f1}")


# ─── File 2: sph3u_01.05_Assignment_doc.html (printable assignment questions) ───
f2 = os.path.join(BASE, "course_content", "assets", "locker_docs", "sph3u_01.05_Assignment_doc.html")

with open(f2, "r", encoding="utf-8") as f:
    t = f.read()

t = t.replace('lang="en"', 'lang="ko"')
t = t.replace("<title>1.5 Assignment: Waves and sound</title>",
              "<title>1.5 과제: 파동과 소리</title>")
t = t.replace("<h1>1.5 Assignment: Waves and sound</h1>",
              "<h1>1.5 과제: 파동과 소리</h1>")

# noscript warning
t = t.replace(
    '<strong>Warning!</strong> To ensure the greatest educational experience, this learning activity\n                contains\n                aspects\n                that require Javascript to be enabled.',
    '<strong>경고!</strong> 최상의 학습 경험을 위해 이 학습 활동에는 Javascript가 활성화되어야 하는 요소가 포함되어 있습니다.'
)

# Question preamble 1
t = t.replace(
    "A standing wave is formed in a string that is 98.0 cm long. Both ends of the string are fixed. Six\n                    loops are present in the standing wave. Answer the following questions about the wave.",
    "길이 98.0 cm인 줄에 정상파가 형성됩니다. 줄의 양 끝은 고정되어 있으며, 정상파에 6개의 배(loop)가 있습니다. 이 파동에 대한 다음 질문에 답하십시오."
)
t = t.replace(
    'Draw the standing wave. Label all nodes and antinodes, the amplitude, and one wavelength.\n                        <strong>(6 marks)</strong>',
    '정상파를 그리십시오. 모든 마디(node)와 배(antinode), 진폭, 그리고 파장 하나를 표시하십시오.\n                        <strong>(6점)</strong>'
)
t = t.replace(
    'Calculate the wavelength of the wave. (Recall that the GUESS problem-solving structure should\n                        always be used for calculation problems. <strong>(4 marks)</strong>',
    '파동의 파장을 계산하십시오. (계산 문제에는 항상 GUESS 문제 풀이 구조를 사용해야 합니다.) <strong>(4점)</strong>'
)
t = t.replace(
    'If it takes a wave 0.00242 s to travel the length of the string, find the speed of the wave.\n                        <strong>(3 marks)</strong>',
    '파동이 줄의 전체 길이를 이동하는 데 0.00242초가 걸린다면, 파동의 속력을 구하십시오.\n                        <strong>(3점)</strong>'
)
t = t.replace(
    'Find the frequency of the wave. <strong>(4 marks)</strong>',
    '파동의 진동수를 구하십시오. <strong>(4점)</strong>'
)

# Question preamble 2
t = t.replace(
    "A student completed a lab activity about the speed of sound in air. Using a tuning fork with a\n                    frequency of 415 Hz, they found the first and second resonant lengths of a closed air column to be\n                    21.30 cm and 63.90 cm.",
    "한 학생이 공기 중 음속에 관한 실험 활동을 수행했습니다. 진동수 415 Hz의 소리굽쇠를 사용하여, 폐관 공기 기둥의 첫 번째와 두 번째 공명 길이가 각각 21.30 cm와 63.90 cm임을 발견했습니다."
)
t = t.replace(
    'Find the third resonant length of the closed air column. <strong>(5 marks)</strong>',
    '폐관 공기 기둥의 세 번째 공명 길이를 구하십시오. <strong>(5점)</strong>'
)
t = t.replace(
    'Calculate the temperature of the room. <strong>(5 marks)</strong>',
    '방의 온도를 계산하십시오. <strong>(5점)</strong>'
)
t = t.replace(
    'If the experiment is repeated in a different room with the same tuning fork and a temperature of\n                        21 °C, what would the ninth resonant length be? <strong>(6 marks)</strong>',
    '같은 소리굽쇠를 사용하여 온도가 21°C인 다른 방에서 실험을 반복하면, 아홉 번째 공명 길이는 얼마입니까? <strong>(6점)</strong>'
)

# Questions about applications
t = t.replace(
    "Answer the following questions about the applications of waves. Each response should be about one\n                    paragraph.",
    "파동의 응용에 관한 다음 질문에 답하십시오. 각 답변은 약 한 문단 분량이어야 합니다."
)
t = t.replace(
    'Explain how an acoustic guitar produces loud music. Include the terms resonance, string, and\n                        <i>wavelength</i> in your response. <strong>(6 marks)</strong>',
    '어쿠스틱 기타가 어떻게 큰 소리의 음악을 만들어 내는지 설명하십시오. 답변에 공명, 줄, <i>파장</i>이라는 용어를 포함하십시오. <strong>(6점)</strong>'
)
t = t.replace(
    'With reference to your knowledge of waves, how can planting more trees in a neighbourhood reduce\n                        the effects of noise pollution? <strong>(5 marks)</strong>',
    '파동에 대한 지식을 바탕으로, 동네에 나무를 더 많이 심는 것이 소음 공해의 영향을 어떻게 줄일 수 있는지 설명하십시오. <strong>(5점)</strong>'
)

# GUESS problems
t = t.replace(
    "Use GUESS problem-solving to complete the following questions.",
    "다음 문제를 GUESS 문제 풀이 방법을 사용하여 풀어 보십시오."
)
t = t.replace(
    'A speaker attached to a movable cart is emitting a sound with a frequency of 698.5 Hz. If the\n                        speed of sound in the air is 348 m/s, how fast should the cart move (and in what direction) for\n                        an observer to hear the frequencies 659.3 Hz and 740.0 Hz? <strong>(7 marks)</strong>',
    '이동 가능한 수레에 부착된 스피커가 진동수 698.5 Hz의 소리를 방출하고 있습니다. 공기 중 음속이 348 m/s일 때, 관찰자가 659.3 Hz와 740.0 Hz의 진동수를 듣기 위해 수레는 어느 방향으로 얼마나 빠르게 움직여야 합니까? <strong>(7점)</strong>'
)
t = t.replace(
    'An open air column with a length of 1.00 m is placed in a room with a speed of sound of 332 m/s.\n                        What are the first and second resonant frequencies of the open air column? <strong>(5\n                            marks)</strong>',
    '길이 1.00 m의 개관 공기 기둥이 음속 332 m/s인 방에 놓여 있습니다.\n                        개관 공기 기둥의 첫 번째와 두 번째 공명 진동수는 얼마입니까? <strong>(5점)</strong>'
)

# Wave interference
t = t.replace(
    "Complete the following questions about wave interference.",
    "파동의 간섭에 관한 다음 질문을 풀어 보십시오."
)
t = t.replace(
    'When the two waves overlap completely, what will their superposition be? You may draw your\n                        answer and include a written explanation, or describe the wave in detail. In either form,\n                        explain your thinking. <strong>(6 marks)</strong>',
    '두 파동이 완전히 겹칠 때 중첩의 결과는 어떻게 됩니까? 답을 그림으로 그리고 서면 설명을 포함하거나 파동을 자세히 설명하십시오. 어느 형태든 자신의 사고 과정을 설명하십시오. <strong>(6점)</strong>'
)
t = t.replace(
    'Press here for a long description.',
    '자세한 설명을 보려면 여기를 누르십시오.'
)
t = t.replace(
    'An incoming wave has the form of a half-circle with a negative displacement and a radius of 8\n                        cm, what shape would cancel the incoming wave and result in no net displacement? Why? <strong>(3\n                            marks)</strong>',
    '들어오는 파동이 음의 변위를 가진 반지름 8 cm의 반원 형태일 때, 이 파동을 상쇄하여 순 변위가 0이 되게 하는 형태는 무엇입니까? 그 이유는? <strong>(3점)</strong>'
)

# Lab report section
t = t.replace(
    "Refer to the Lab activity: Speed of sound in air using a closed air column lab in Learning Activity\n                    1.5 to complete the following question.",
    "다음 질문을 완성하기 위해 학습 활동 1.5의 실험 활동: 폐관 공기 기둥을 사용한 공기 중 음속 측정 실험을 참조하십시오."
)
t = t.replace(
    'A lab report is a piece of scientific communication with a standard format. In this course, a\n                        lab report includes a descriptive title, and seven sections: Purpose, materials, apparatus,\n                        method, results, analysis, and conclusion. In the same document as the rest of your assignment,\n                        write a lab report for the Speed of sound in air using a closed air column lab. The purpose,\n                        materials, apparatus, and method are provided, so copy them. Format the results section to\n                        record the outcome of the lab. Answer the analysis questions in the analysis section of your\n                        report, and write your own conclusion that responds to the purpose of the lab. Be sure that your\n                        report is professionally formatted and spell-checked. <strong>(10 marks)</strong>',
    '실험 보고서는 표준 형식을 갖춘 과학적 의사소통의 한 형태입니다. 이 과정에서 실험 보고서에는 서술적 제목과 일곱 개의 섹션(목적, 재료, 실험 기구, 방법, 결과, 분석, 결론)이 포함됩니다. 과제의 나머지 부분과 같은 문서에 폐관 공기 기둥을 사용한 공기 중 음속 측정 실험에 대한 실험 보고서를 작성하십시오. 목적, 재료, 실험 기구, 방법은 제공되어 있으므로 복사하십시오. 결과 섹션은 실험의 결과를 기록하는 형식으로 작성하십시오. 보고서의 분석 섹션에서 분석 질문에 답하고, 실험의 목적에 부합하는 자신만의 결론을 작성하십시오. 보고서가 전문적인 형식을 갖추고 맞춤법이 점검되었는지 확인하십시오. <strong>(10점)</strong>'
)

# Print button area
t = t.replace("Print", "인쇄")
t = t.replace("Close this tab to return to the previous window.", "이 탭을 닫으면 이전 창으로 돌아갑니다.")

# sr-only
t = t.replace('<span class="sr-only">(Opens in new window)</span>', '<span class="sr-only">(새 창에서 열림)</span>')
t = t.replace('<span\n                                      class="sr-only">(Opens in new window)</span>', '<span\n                                      class="sr-only">(새 창에서 열림)</span>')

with open(f2, "w", encoding="utf-8") as f:
    f.write(t)
print(f"[OK] {f2}")


# ─── File 3: transferable_skills.html ───
f3 = os.path.join(BASE, "course_content", "assets", "locker_docs", "transferable_skills.html")

with open(f3, "r", encoding="utf-8") as f:
    t = f.read()

t = t.replace('lang="en"', 'lang="ko"')
t = t.replace("<title>Transferable skills</title>", "<title>전이 가능한 역량</title>")
t = t.replace("<h1>Transferable skills</h1>", "<h1>전이 가능한 역량</h1>")

# Critical thinking
t = t.replace("<h2>Critical thinking and problem solving</h2>", "<h2>비판적 사고와 문제 해결</h2>")
t = t.replace(
    "Critical thinking and problem solving involve looking at complex issues and problems from a variety of different points of view in order to make informed judgments and decisions. Learning is deeper when the experiences are meaningful, real world and authentic.",
    "비판적 사고와 문제 해결은 정보에 기반한 판단과 결정을 내리기 위해 복잡한 문제와 이슈를 다양한 관점에서 바라보는 것을 포함합니다. 학습 경험이 의미 있고 실제적이며 진정성이 있을 때 학습은 더 깊어집니다."
)
t = t.replace("<p>Students consistently:</p>", "<p>학생들은 일관되게:</p>", 1)
t = t.replace("<li>solve meaningful, real-life problems;</li>", "<li>의미 있는 실생활 문제를 해결합니다.</li>")
t = t.replace("<li>take steps to organize, design and manage projects using inquiry processes;</li>", "<li>탐구 과정을 활용하여 프로젝트를 조직, 설계, 관리합니다.</li>")
t = t.replace("<li>analyze information to make informed decisions;</li>", "<li>정보에 기반한 결정을 내리기 위해 정보를 분석합니다.</li>")
t = t.replace("<li>see patterns, make connections and transfer learning from one situation to another;</li>", "<li>패턴을 파악하고 연결 고리를 만들며, 한 상황에서 다른 상황으로 학습을 전이합니다.</li>")
t = t.replace("<li>see the connections between social, economic and ecological systems.</li>", "<li>사회적, 경제적, 생태적 체계 간의 연결성을 파악합니다.</li>")

# Innovation
t = t.replace("<h2>Innovation, creativity, and entrepreneurship</h2>", "<h2>혁신, 창의성, 기업가 정신</h2>")
t = t.replace(
    "Innovation, creativity, and entrepreneurship involve the ability to turn ideas into action to meet the needs of a community. The ability to contribute new-to-the-world thinking and solutions to solve complex problems involves\n                    leadership, risk taking and independent/ unconventional thinking. Experimenting with new strategies, techniques and perspectives through research is part of this skill set.",
    "혁신, 창의성, 기업가 정신은 아이디어를 실행에 옮겨 공동체의 필요를 충족시키는 능력을 포함합니다. 복잡한 문제를 해결하기 위해 세계적으로 새로운 사고와 해결책을 기여하는 능력에는 리더십, 위험 감수, 독립적이고 비관습적인 사고가 필요합니다. 연구를 통해 새로운 전략, 기법, 관점을 실험하는 것도 이 역량에 포함됩니다."
)
t = t.replace("<p>Students consistently:</p>", "<p>학생들은 일관되게:</p>", 1)
t = t.replace("<li>formulate insightful questions to generate opinions;</li>", "<li>의견을 도출하기 위한 통찰력 있는 질문을 만듭니다.</li>")
t = t.replace("<li>take risks in thinking;</li>", "<li>사고에서 위험을 감수합니다.</li>")
t = t.replace("<li>experiment to find new ways of doing things;</li>", "<li>새로운 방법을 찾기 위해 실험합니다.</li>")
t = t.replace("<li>demonstrate leadership in a range of creative projects;</li>", "<li>다양한 창의적 프로젝트에서 리더십을 발휘합니다.</li>")
t = t.replace("<li>motivate others in an ethical and entrepreneurial spirit.</li>", "<li>윤리적이고 기업가적인 정신으로 타인에게 동기를 부여합니다.</li>")

# Self-directed
t = t.replace("<h2>Self-directed learning</h2>", "<h2>자기 주도 학습</h2>")
t = t.replace(
    "Self-directed learning means: becoming aware and demonstrating ownership in your learning. Belief in your ability to learn (growth mindset), combined with strategies for planning, monitoring and reflecting on your past, present and\n                    future goals promote lifelong learning, well-being and adaptability in an ever- changing world.",
    "자기 주도 학습이란 자신의 학습에 대해 인식하고 주인 의식을 보여 주는 것을 의미합니다. 학습 능력에 대한 믿음(성장 마인드셋)과 과거, 현재, 미래 목표를 계획, 점검, 성찰하는 전략이 결합되면 끊임없이 변화하는 세상에서 평생 학습, 안녕, 적응력을 촉진합니다."
)
t = t.replace("<p>Students consistently:</p>", "<p>학생들은 일관되게:</p>", 1)
t = t.replace("<li>are aware of how they learn best;</li>", "<li>자신이 가장 잘 배우는 방법을 알고 있습니다.</li>")
t = t.replace("<li>ask for support when needed;</li>", "<li>필요할 때 도움을 요청합니다.</li>")
t = t.replace("<li>set goals and make a plan to achieve their goals;</li>", "<li>목표를 설정하고 그 목표를 달성하기 위한 계획을 세웁니다.</li>")
t = t.replace("<li>practice new skills they want to improve;</li>", "<li>향상시키고 싶은 새로운 기술을 연습합니다.</li>")
t = t.replace("<li>reflect on their own learning to determine strengths;</li>", "<li>강점을 파악하기 위해 자신의 학습을 성찰합니다.</li>")
t = t.replace("<li>learn to adapt to change and become resilient in the face of adversity;</li>", "<li>변화에 적응하고 역경에 직면하여 회복력을 기르는 법을 배웁니다.</li>")
t = t.replace("<li>become managers of different aspects of their lives to enhance their health and overall well being.</li>", "<li>건강과 전반적인 안녕을 향상시키기 위해 삶의 다양한 측면을 관리합니다.</li>")

# Collaboration
t = t.replace("<h2>Collaboration</h2>", "<h2>협력</h2>")
t = t.replace(
    "Collaboration involves participating ethically and effectively in teams. Being versatile across different situations, roles, groups and perspectives allows you to co-construct knowledge, meaning, content and learn from, and with\n                    others in physical and online spaces.",
    "협력은 팀에서 윤리적이고 효과적으로 참여하는 것을 포함합니다. 다양한 상황, 역할, 그룹, 관점에서 유연하게 대처하면 물리적 및 온라인 공간에서 타인과 함께 지식, 의미, 콘텐츠를 공동 구성하고 학습할 수 있습니다."
)
t = t.replace("<p>Students consistently:</p>", "<p>학생들은 일관되게:</p>", 1)
t = t.replace("<li>participate in teams in respectful and positive ways;</li>", "<li>존중하고 긍정적인 방식으로 팀에 참여합니다.</li>")
t = t.replace("<li>learn from others;</li>", "<li>타인으로부터 배웁니다.</li>")
t = t.replace("<li>contribute to the learning of others;</li>", "<li>타인의 학습에 기여합니다.</li>")
t = t.replace("<li>assume various roles on a team as needed being respectful of a diversity of perspectives including Indigenous ways of knowing;</li>", "<li>원주민의 앎의 방식을 포함한 다양한 관점을 존중하며, 필요에 따라 팀에서 여러 역할을 맡습니다.</li>")
t = t.replace("<li>address disagreements and manage conflict in sensitive and constructive ways;</li>", "<li>민감하고 건설적인 방식으로 의견 불일치를 다루고 갈등을 관리합니다.</li>")
t = t.replace("<li>network with a variety of people and groups on an ongoing basis.</li>", "<li>다양한 사람들 및 그룹과 지속적으로 네트워크를 형성합니다.</li>")

# Communication
t = t.replace("<h2>Communication</h2>", "<h2>의사소통</h2>")
t = t.replace(
    "Communication involves receiving and expressing meaning (e.g., reading and writing, viewing and creating, listening and speaking) in different contexts and with different audiences and purposes. Effective communication increasingly\n                    involves understanding both local and global perspectives, including using a variety of media appropriately, responsibly and safely with regard to your digital footprint.",
    "의사소통은 다양한 맥락에서 다양한 대상과 목적에 맞게 의미를 수용하고 표현하는 것(예: 읽기와 쓰기, 보기와 만들기, 듣기와 말하기)을 포함합니다. 효과적인 의사소통에는 디지털 발자국에 관하여 다양한 매체를 적절하고 책임감 있으며 안전하게 사용하는 것을 포함하여 지역적 및 세계적 관점을 모두 이해하는 것이 점점 더 중요해지고 있습니다."
)
t = t.replace("<p>Students consistently:</p>", "<p>학생들은 일관되게:</p>", 1)
t = t.replace("<li>communicate effectively in a variety of media;</li>", "<li>다양한 매체에서 효과적으로 의사소통합니다.</li>")
t = t.replace("<li>use digital tools appropriately to create a positive digital footprint;</li>", "<li>긍정적인 디지털 발자국을 만들기 위해 디지털 도구를 적절하게 사용합니다.</li>")
t = t.replace("<li>listen to understand;</li>", "<li>이해하기 위해 경청합니다.</li>")
t = t.replace("<li>ask effective questions;</li>", "<li>효과적인 질문을 합니다.</li>")
t = t.replace("<li>understand the cultural importance of language.</li>", "<li>언어의 문화적 중요성을 이해합니다.</li>")

# Global citizenship
t = t.replace("<h2>Global citizenship and sustainability</h2>", "<h2>세계 시민 의식과 지속 가능성</h2>")
t = t.replace(
    "Global citizenship and sustainability involve understanding diverse worldviews and perspectives in order to address political, ecological, social, and economic issues that are crucial to living in a in a sustainable world. Being\n                    aware of what it means to be an engaged citizen and how the appreciation for the diversity of people and perspectives contributes to a sustainable world are part of this skill set.",
    "세계 시민 의식과 지속 가능성은 지속 가능한 세상에서 살기 위해 중요한 정치적, 생태적, 사회적, 경제적 문제를 해결하기 위해 다양한 세계관과 관점을 이해하는 것을 포함합니다. 참여하는 시민이 된다는 것의 의미와 사람과 관점의 다양성에 대한 존중이 지속 가능한 세상에 어떻게 기여하는지 인식하는 것도 이 역량에 포함됩니다."
)
t = t.replace("<p>Students consistently:</p>", "<p>학생들은 일관되게:</p>", 1)
t = t.replace("<li>take actions and make responsible decisions to support the quality of life for all;</li>", "<li>모든 사람의 삶의 질을 지원하기 위해 행동하고 책임감 있는 결정을 내립니다.</li>")
t = t.replace("<li>understand the histories, knowledge, contributions and inherent rights of Indigenous people;</li>", "<li>원주민의 역사, 지식, 기여, 고유한 권리를 이해합니다.</li>")
t = t.replace("<li>recognize discrimination and work to promote the principles of equity;</li>", "<li>차별을 인식하고 형평성의 원칙을 증진하기 위해 노력합니다.</li>")
t = t.replace("<li>contribute to their local and global community;</li>", "<li>지역 사회와 세계 공동체에 기여합니다.</li>")
t = t.replace("<li>participate in an inclusive, accountable, sustainable and ethical manner, both in groups and in online networks.</li>", "<li>그룹과 온라인 네트워크 모두에서 포용적이고 책임감 있으며 지속 가능하고 윤리적인 방식으로 참여합니다.</li>")

# Digital literacy
t = t.replace("<h2>Digital literacy</h2>", "<h2>디지털 리터러시</h2>")
t = t.replace(
    "Digital literacy involves the ability to solve problems using technology in a safe, legal, and ethically responsible manner. Digitally literate students recognize the rights and responsibilities, as well as the opportunities, that\n                    come with living, learning, and working in an interconnected digital world.",
    "디지털 리터러시는 안전하고 합법적이며 윤리적으로 책임감 있는 방식으로 기술을 사용하여 문제를 해결하는 능력을 포함합니다. 디지털 리터러시를 갖춘 학생은 상호 연결된 디지털 세계에서 생활하고 학습하며 일하는 것에 따르는 권리와 책임, 그리고 기회를 인식합니다."
)
t = t.replace("<p>Students consistently:</p>", "<p>학생들은 일관되게:</p>", 1)
t = t.replace("<li>select and use appropriate digital tools to collaborate, communicate, create, innovate and solve problems;</li>", "<li>협력, 의사소통, 창작, 혁신, 문제 해결을 위해 적절한 디지털 도구를 선택하고 사용합니다.</li>")
t = t.replace("<li>use technology in a way that is consistent with supporting their mental health and well-being;</li>", "<li>정신 건강과 안녕을 지원하는 방식으로 기술을 사용합니다.</li>")
t = t.replace("<li>use digital tools effectively to solve problems and inform decisions;</li>", "<li>문제를 해결하고 결정에 도움이 되도록 디지털 도구를 효과적으로 사용합니다.</li>")
t = t.replace("<li>demonstrate a willingness and confidence to explore new or unfamiliar digital tools and emerging technologies;</li>", "<li>새롭거나 익숙하지 않은 디지털 도구와 신기술을 탐색하려는 의지와 자신감을 보여 줍니다.</li>")
t = t.replace("<li>manage their digital footprint by engaging in social media and online communities respectfully, inclusively, safely, legally and ethically.</li>", "<li>소셜 미디어와 온라인 커뮤니티에 존중, 포용, 안전, 합법, 윤리적으로 참여하여 디지털 발자국을 관리합니다.</li>")

# Definition / Look fors labels (replace all)
t = t.replace('<p class="h3">Definition</p>', '<p class="h3">정의</p>', )
t = t.replace('<p class="h3">Definition </p>', '<p class="h3">정의</p>')
t = t.replace('<p class="h3">Look fors</p>', '<p class="h3">관찰 지표</p>')

# Footer
t = t.replace(
    'Adapted from material provided by the Ministry of Education for Ontario: <a href="https://www.dcp.edu.gov.on.ca/en/transferable-skills" target="_blank">Transferable skills<span class="sr-only">(Opens in a new window)</span></a>',
    '온타리오 교육부에서 제공한 자료를 바탕으로 작성: <a href="https://www.dcp.edu.gov.on.ca/en/transferable-skills" target="_blank">전이 가능한 역량<span class="sr-only">(새 창에서 열림)</span></a>'
)

with open(f3, "w", encoding="utf-8") as f:
    f.write(t)
print(f"[OK] {f3}")


# ─── File 4: sph3u_acknowledgements.html ───
f4 = os.path.join(BASE, "course_content", "assets", "locker_docs", "sph3u_acknowledgements.html")

with open(f4, "r", encoding="utf-8") as f:
    t = f.read()

t = t.replace('lang="en"', 'lang="ko"')
t = t.replace("<title>\n            SPH3U Acknowledgements\n        </title>",
              "<title>\n            SPH3U 저작권 표시\n        </title>")
t = t.replace("<h1>\n                            SPH3U Acknowledgements\n                        </h1>",
              "<h1>\n                            SPH3U 저작권 표시\n                        </h1>")

# noscript
t = t.replace(
    '<strong>Warning!</strong>\n                    To ensure the greatest educational experience, this learning activity contains aspects that require\n                    Javascript to be enabled.',
    '<strong>경고!</strong>\n                    최상의 학습 경험을 위해 이 학습 활동에는 Javascript가 활성화되어야 하는 요소가 포함되어 있습니다.'
)

# Section headers
t = t.replace('<h2 id="unit1">Unit 1</h2>', '<h2 id="unit1">1단원</h2>')
t = t.replace('<h2 id="unit2">Unit 2</h2>', '<h2 id="unit2">2단원</h2>')
t = t.replace('<h2 id="unit3">Unit 3</h2>', '<h2 id="unit3">3단원</h2>')
t = t.replace('<h2 id="unit4">Unit 4</h2>', '<h2 id="unit4">4단원</h2>')

# Intro text
t = t.replace(
    "Some images supplied by Getty Images. Other images, graphs, diagrams, and illustrations in this course, unless otherwise specified, are TVO created.",
    "일부 이미지는 Getty Images에서 제공되었습니다. 이 과정의 기타 이미지, 그래프, 도표, 삽화는 별도의 명시가 없는 한 TVO에서 제작한 것입니다."
)
t = t.replace(
    "Graphs created by OECA with GeoGebra (www.geogebra.org).",
    "그래프는 OECA에서 GeoGebra(www.geogebra.org)를 사용하여 제작했습니다."
)

with open(f4, "w", encoding="utf-8") as f:
    f.write(t)
print(f"[OK] {f4}")

print("\nAll 4 files translated successfully.")
