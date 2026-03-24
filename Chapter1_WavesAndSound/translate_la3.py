#!/usr/bin/env python3
"""Translate sph3u_u1la3.html from English to Korean."""

REPLACEMENTS = [
    # Title
    ("Learning activity 1.3: Reflecting on Waves", "학습 활동 1.3: 파동의 반사"),

    # Noscript warning
    ("<strong>Warning!</strong> To ensure the greatest educational experience, this learning activity\n                contians\n                aspects that require Javascript to be enabled.", "<strong>주의!</strong> 최상의 학습 경험을 위해, 이 학습 활동은 Javascript가 활성화되어 있어야 합니다."),

    # Learning goals
    ("<h2>Learning goals</h2>", "<h2>학습 목표</h2>"),
    ("<p>We are learning to:</p>", "<p>학습 내용:</p>"),
    ("<li>assess our knowledge on waves and sound</li>", "<li>파동과 소리에 대한 지식을 평가한다</li>"),
    ("<li>reflect on errors and missing key concepts</li>", "<li>오류와 누락된 핵심 개념을 되돌아본다</li>"),

    # Success criteria
    ("<h2>Success criteria</h2>", "<h2>성취 기준</h2>"),
    ("<p>I am able to:</p>", "<p>나는 다음을 할 수 있다:</p>"),
    ("<li>answer each question correctly on my own</li>", "<li>각 문제를 스스로 정확하게 답할 수 있다</li>"),
    ("successfully correct my answer to questions where immediate feedback identifies an error in my understanding\n                or calculations", "즉각적인 피드백이 나의 이해나 계산에서 오류를 지적한 문제에 대해 성공적으로 답을 수정할 수 있다"),
    ("<li>self-assess my readiness to move on to more material on waves</li>", "<li>파동에 관한 추가 학습으로 나아갈 준비가 되었는지 자기 평가할 수 있다</li>"),

    # Minds On - Reflecting
    ("<h2>Reflecting</h2>", "<h2>되돌아보기</h2>"),
    ("As we explore and learn about a new subject, it is important to pause and reflect on our learning. This\n                        gives\n                        us the opportunity to reinforce existing knowledge, correct any misunderstandings, and prepare for future\n                        study.", "새로운 주제를 탐구하고 배울 때, 잠시 멈추어 학습을 되돌아보는 것이 중요합니다. 이를 통해 기존 지식을 강화하고, 잘못된 이해를 바로잡고, 앞으로의 학습을 준비할 수 있습니다."),
    ("The purpose of this learning activity is to reflect on waves, and to prepare for the first assignment of\n                        this\n                        course, which is at the end of Unit 1. ", "이 학습 활동의 목적은 파동에 대해 되돌아보고, 단원 1의 마지막에 있는 이 과정의 첫 번째 과제를 준비하는 것입니다. "),

    # Notebook callout
    ("<h2 class=\"h3\">Notebook</h2>", "<h2 class=\"h3\">노트</h2>"),
    ("<p>This is a self-assessment, which will help you to: </p>", "<p>이것은 자기 평가로, 다음에 도움이 됩니다: </p>"),
    ("<li>assess and evaluate your learning</li>", "<li>학습을 평가한다</li>"),
    ("determine where you are in you learning, where you need to go, and how best to get\n                                    there", "현재 학습 위치를 파악하고, 어디로 나아가야 하며, 어떻게 도달할 수 있는지 결정한다"),
    ("You can use your notebook to complete each of the following questions. Compare your work\n                                with the suggested answers to check your understanding. ", "노트를 사용하여 다음 각 문제를 풀어 보세요. 풀이 예시와 비교하여 이해도를 확인하세요. "),

    # Task headings
    ("<h2>Task 1: Multiple choice – Terms you need to know</h2>", "<h2>과제 1: 객관식 – 알아야 할 용어</h2>"),
    ("Select the term that best matches the explanation.", "설명에 가장 잘 맞는 용어를 선택하세요."),
    ("<h2>Task 2: True/False – How much do you know about waves?</h2>", "<h2>과제 2: 참/거짓 – 파동에 대해 얼마나 알고 있나요?</h2>"),
    ("Identify whether the statement is true or false.", "문장이 참인지 거짓인지 판별하세요."),
    ("<h2>Task 3: What do you know? </h2>", "<h2>과제 3: 무엇을 알고 있나요? </h2>"),
    ("Attempt the following problems. If you get stuck, check the hint. Compare your solution to the suggested\n                        answer, and reflect on whether your solution is accurate, clear, and complete.", "다음 문제를 풀어 보세요. 막히면 힌트를 확인하세요. 풀이 예시와 비교하여, 자신의 풀이가 정확하고 명확하며 완전한지 되돌아보세요."),
    ("<h2>Task 4: Label the wave</h2>", "<h2>과제 4: 파동에 이름 붙이기</h2>"),
    ("For the different letters labelling the wave, select and match the appropriate name or\n                        numerical description. ", "파동에 표시된 각 문자에 대해, 적절한 이름이나 수치적 설명을 선택하여 연결하세요. "),
    ("Press here for a long description.", "상세 설명을 보려면 여기를 누르세요."),

    # Problem 1
    ("A 280.0 Hz buzzer produces sound waves that are 1.21 m long. What is the temperature of the air in which\n                            the sound is produced?", "280.0 Hz 부저가 파장이 1.21 m인 음파를 만들어 냅니다. 소리가 전달되는 공기의 온도는 얼마입니까?"),

    # Hints for Problem 1
    (" Use the universal wave equation ", " 파동의 기본 방정식 "),
    (" first to help you find the speed.", "을 먼저 사용하여 속력을 구하세요."),
    (" Use the equation for speed of sound in air<br>", " 공기 중 음속 공식을 사용하세요<br>"),
    ("where <em>T</em> is temperature and <em>v</em> is the speed of the sound wave.", "여기서 <em>T</em>는 온도이고 <em>v</em>는 음파의 속력입니다."),

    # Solution labels (common)
    ("<p>Given:</p>", "<p>주어진 값:</p>"),
    ("<p style=\"padding-top: 2%;\">Unknown:</p>", "<p style=\"padding-top: 2%;\">구하는 값:</p>"),
    ("<p style=\"padding-top: 2%;\">Equation:</p>", "<p style=\"padding-top: 2%;\">공식:</p>"),
    ("<p style=\"padding-top: 2%;\">Solve:</p>", "<p style=\"padding-top: 2%;\">풀이:</p>"),
    ("<p style=\"padding-top: 2%;\">Statement:</p>", "<p style=\"padding-top: 2%;\">결론:</p>"),
    ("<p style=\"padding-top: 1%;\">Unknown:</p>", "<p style=\"padding-top: 1%;\">구하는 값:</p>"),
    ("<p style=\"padding-top: 1%;\">Equation:</p>", "<p style=\"padding-top: 1%;\">공식:</p>"),
    ("<p style=\"padding-top: 1%;\">Solve:</p>", "<p style=\"padding-top: 1%;\">풀이:</p>"),
    ("<p style=\"padding-top: 1%;\">Statement:</p>", "<p style=\"padding-top: 1%;\">결론:</p>"),
    ("<p>Unknown:</p>", "<p>구하는 값:</p>"),
    ("<p>Equation:</p>", "<p>공식:</p>"),
    ("<p>Solve:</p>", "<p>풀이:</p>"),
    ("<p>Statement:</p>", "<p>결론:</p>"),

    # Solution text - Problem 1
    (" is the universal wave equation.", "은 파동의 기본 방정식입니다."),
    ("<p>We will also need the speed of sound formula</p>", "<p>음속 공식도 필요합니다</p>"),
    ("<p>First, find the speed of sound.</p>", "<p>먼저 음속을 구합니다.</p>"),
    ("<p>Then use the speed of sound vs. temperature formula to find the temperature.</p>", "<p>그런 다음 음속과 온도의 관계식을 사용하여 온도를 구합니다.</p>"),
    ("The temperature of the air is 11.5 °C. (Three significant digits, since the given values had 4 and\n                                        3.)", "공기의 온도는 11.5 °C입니다. (주어진 값이 유효 숫자 4자리와 3자리이므로, 유효 숫자 3자리로 나타냅니다.)"),

    # Problem 2
    ("A tuning fork with a frequency of 420 Hz emits sound with a wavelength of 0.82 m in air. If\n                            the temperature of the air increases, what will happen to the wavelength: increase, decrease, or\n                            stay the same?", "진동수가 420 Hz인 소리굽쇠가 공기 중에서 파장 0.82 m의 소리를 냅니다. 공기의 온도가 올라가면 파장은 어떻게 되나요: 증가, 감소, 또는 변화 없음?"),

    # Hint for Problem 2
    (" Think about the how the temperature will affect the speed.", " 온도가 속력에 어떤 영향을 미칠지 생각해 보세요."),
    (" Think about the universal wave equation <br>", " 파동의 기본 방정식을 생각해 보세요 <br>"),
    ("If <em>v</em> increases but <em>f</em> remains constant, what should happen\n                                            to the wavelength?", "<em>v</em>가 증가하지만 <em>f</em>가 일정하다면, 파장은 어떻게 되어야 할까요?"),

    # Solution - Problem 2
    ("<p>Using the speed of sound in air equation,", "<p>공기 중 음속 공식을 사용하면,"),
    ("<p>you can discern that as the temperature increases, the speed will increase. </p>", "<p>온도가 올라가면 속력이 증가한다는 것을 알 수 있습니다. </p>"),
    ("<p>So you know the speed of the wave is increasing.</p>", "<p>따라서 파동의 속력이 증가하고 있다는 것을 알 수 있습니다.</p>"),
    ("<p>Using the universal wave equation,", "<p>파동의 기본 방정식을 사용하면,"),
    ("you conclude that if <em>v</em> increases but <em>f</em> stays the same,\n                                        wavelength (<em>&#x03BB;</em>) must increase.", "<em>v</em>가 증가하지만 <em>f</em>가 일정하다면, 파장(<em>&#x03BB;</em>)은 증가해야 한다고 결론 내릴 수 있습니다."),

    # Problem 3
    ("Find the frequency and the period for each of the following:", "다음 각각의 진동수와 주기를 구하세요:"),
    ("A light bulb turns on and off 60 times in 1 s.", "전구가 1초 동안 60번 켜졌다 꺼집니다."),
    ("A hummingbird flap its wings 120 times in 6 s.", "벌새가 6초 동안 날개를 120번 칩니다."),

    # Hints for Problem 3
    ("<p>The formula for period is:</p>", "<p>주기 공식은:</p>"),
    ("<p>or</p>", "<p>또는</p>"),
    ("where <em>N</em> is number of cycles and <em>t</em> is time. In a) there\n                                                are 60 cycles, in b) there are 120 cycles.", "여기서 <em>N</em>은 진동 횟수이고 <em>t</em>는 시간입니다. a)에서는 60번, b)에서는 120번 진동합니다."),
    ("<p>Once you know the period you can use the formula </p>", "<p>주기를 알면 다음 공식을 사용할 수 있습니다 </p>"),
    ("<p>to find the frequencies.</p>", "<p>이를 사용하여 진동수를 구합니다.</p>"),

    # Solution - Problem 3a
    ("The period is 0.02 s and the frequency is 60 Hz. ", "주기는 0.02 s이고 진동수는 60 Hz입니다. "),
    (" Notice that since time was 1 s, you could have stated the frequency without\n                                        doing any calculations. The statement uses one significant digit, since \"1 s\" has just a single\n                                        significant digit.", " 시간이 1 s이므로, 계산 없이도 진동수를 바로 말할 수 있습니다. 결론은 유효 숫자 1자리로 나타냅니다. \"1 s\"가 유효 숫자 1자리이기 때문입니다."),

    # Solution - Problem 3b
    ("<p>The period is 0.05 s and the frequency is 20 Hz.</p>", "<p>주기는 0.05 s이고 진동수는 20 Hz입니다.</p>"),

    # Problem 4
    ("A train on a straight track sounds a 400.0 Hz horn as it passes a parked car on the road. The\n                            train is moving at 20.0 m/s and the temperature is 10.0°C. Find the apparent frequency of the\n                            horn for a person sitting inside the car when the train is approaching.", "직선 선로 위의 기차가 도로에 주차된 자동차 옆을 지나며 400.0 Hz의 경적을 울립니다. 기차는 20.0 m/s로 이동하고 있으며 온도는 10.0°C입니다. 기차가 다가올 때 자동차 안에 앉아 있는 사람이 듣는 겉보기 진동수를 구하세요."),

    # Hints for Problem 4
    (" First, use the temperature to find the speed of sound using the\n                                                equation.", " 먼저 다음 공식을 사용하여 온도로부터 음속을 구하세요."),
    ("<p>Decide if you should use the + or – sign in the Doppler effect formula.\n                                            </p>", "<p>도플러 효과 공식에서 + 또는 – 부호 중 어느 것을 사용해야 할지 결정하세요.\n                                            </p>"),

    # Solution - Problem 4
    ("<p>First, find the speed of sound based on temperature.</p>", "<p>먼저 온도에 따른 음속을 구합니다.</p>"),
    ("Then use the Doppler effect with minus since the train is approaching.", "기차가 다가오고 있으므로 도플러 효과 공식에서 빼기를 사용합니다."),
    ("<p>The person will observe a frequency of 425 Hz.</p>", "<p>그 사람은 425 Hz의 진동수를 관측하게 됩니다.</p>"),

    # Accordion labels
    (">Show Suggested Answer<", ">풀이 보기<"),
    (">Show Suggested Answer 1<", ">풀이 보기 1<"),
    (">Show Suggested Answer 2<", ">풀이 보기 2<"),
    (">Hints<", ">힌트<"),
    (">Hint<", ">힌트<"),

    # Consolidation
    ("<h2>Putting it all together</h2>", "<h2>종합하기</h2>"),
    ("<h3>Notebook</h3>", "<h3>노트</h3>"),
    ("<h4 style=\"margin-left: 20px\">Task 5: Reflection</h4>", "<h4 style=\"margin-left: 20px\">과제 5: 되돌아보기</h4>"),
    (" Complete the following questions in your notebook.", " 노트에 다음 질문에 답하세요."),
    ("After reviewing the suggested answers for the practice questions, what\n                                    concepts do you need to improve upon?", "연습 문제의 풀이 예시를 검토한 후, 어떤 개념을 더 보완해야 하나요?"),
    ("What are your next steps to ensure you understand all concepts?", "모든 개념을 이해하기 위한 다음 단계는 무엇인가요?"),
    ("What are your strengths as an independent learner? What have you done to\n                                    help you focus? What resources, if any, have you turned to for help?", "자기주도 학습자로서 당신의 강점은 무엇인가요? 집중하기 위해 어떤 노력을 했나요? 도움을 위해 어떤 자료를 참고했나요?"),
    ("What areas do you need to improve upon? What steps might you take to be a\n                                    better learner?", "어떤 부분을 개선해야 하나요? 더 나은 학습자가 되기 위해 어떤 조치를 취할 수 있나요?"),

    # Self-check quiz
    ("<h3>Self-check quiz</h3>", "<h3>자기 점검 퀴즈</h3>"),
    ("<h4>Check your understanding!</h4>", "<h4>이해도를 확인하세요!</h4>"),
    ("Complete the following self-check quiz to determine where you are in your learning and what areas\n                                you\n                                need to focus on.", "다음 자기 점검 퀴즈를 풀어 현재 학습 위치와 집중해야 할 영역을 파악하세요."),
    ("This quiz is for feedback only, not part of your grade. You have unlimited attempts on this quiz.\n                                Take\n                                your time, do your best work, and reflect on any feedback provided.", "이 퀴즈는 피드백 전용이며 성적에 포함되지 않습니다. 이 퀴즈에 대한 시도 횟수는 무제한입니다. 충분한 시간을 가지고 최선을 다하며, 제공된 피드백을 되돌아보세요."),
    ("Press <strong>Quiz</strong> to access this tool.", "<strong>퀴즈</strong> 버튼을 눌러 도구에 접근하세요."),

    # HTML lang
    ('<html lang="en">', '<html lang="ko">'),
]


def translate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for eng, kor in REPLACEMENTS:
        content = content.replace(eng, kor)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    translate_file('course_content/lessons/sph3u_u1la3.html')
