#!/usr/bin/env python3
"""Translate sph3u_u1la5.html from English to Korean."""

REPLACEMENTS = [
    # Title and metadata
    ("Learning activity 1.5: Resonance", "학습 활동 1.5: 공명"),
    ('<html lang="en">', '<html lang="ko">'),

    # Noscript warning
    ("<strong>Warning!</strong> To ensure the greatest educational experience, this learning activity contains aspects that require Javascript to be enabled.", "<strong>주의!</strong> 최상의 학습 경험을 위해, 이 학습 활동은 Javascript가 활성화되어 있어야 합니다."),

    # Learning goals
    ("Learning goals", "학습 목표"),
    ("In this learning activity you will:", "학습 내용:"),
    ("understand constructive and destructive interference and superposition and how waves interact with each other", "보강 간섭과 상쇄 간섭, 그리고 중첩을 통해 파동이 서로 어떻게 상호작용하는지 이해한다"),
    ("demonstrate how beats are produced from two interfering frequencies", "간섭하는 두 진동수로부터 맥놀이가 어떻게 생성되는지 보여준다"),
    ("use the beat frequency equation", "맥놀이 진동수 방정식을 사용한다"),
    ("create standing waves", "정상파를 만든다"),
    ("analyze standing waves using equations involving time, wavelength, wave speed, node spacing, and frequency variables", "시간, 파장, 파동 속력, 마디 간격, 진동수 변수를 포함한 방정식을 사용하여 정상파를 분석한다"),
    ("Success criteria", "성취 기준"),
    ("I can:", "나는 다음을 할 수 있다:"),
    ("describe and illustrate properties of waves when they interact with each other", "파동이 서로 간섭할 때의 성질을 설명하고 묘사할 수 있다"),
    ("explain why standing waves occur", "정상파가 발생하는 이유를 설명할 수 있다"),
    ("calculate beat frequency", "맥놀이 진동수를 계산할 수 있다"),
    ("describe ways in which sound can have a negative impact on everyday life", "소리가 일상에 부정적인 영향을 미칠 수 있는 방법을 설명할 수 있다"),

    # Notebook vocabulary section
    ("Notebook", "노트"),
    ("Vocabulary: Record the following vocabulary in your notebook. As you complete the learning activity, fill in the related definitions and key terms for the vocabulary.", "어휘: 다음 어휘를 노트에 기록하세요. 학습 활동을 완료하면서 어휘에 관련된 정의와 핵심 용어를 채워 넣으세요."),
    ("constructive interference", "보강 간섭"),
    ("destructive interference", "상쇄 간섭"),
    ("superposition", "중첩"),
    ("nodes", "마디"),
    ("antinodes", "배"),
    ("loops", "루프"),

    # Introduction
    ("Introduction", "도입"),
    # Long paragraph about musical instruments - handle carefully
    ("When a musician plays a trumpet, they force air into the instrument. The trumpet amplifies the sound. Why does the trumpet amplify the sound?", "음악가가 트럼펫을 연주할 때, 악기 안으로 공기를 불어넣습니다. 트럼펫은 소리를 증폭시킵니다. 왜 트럼펫은 소리를 증폭시킬까요?"),
    ("All objects have what is known as a natural frequency, the frequency at which the object tends to vibrate. This natural frequency is also called the resonant frequency. If one pushes an object repeatedly at its natural frequency, the result is resonance.", "모든 물체는 고유 진동수라고 알려진, 그 물체가 진동하려는 경향이 있는 진동수를 가지고 있습니다. 이 고유 진동수를 공명 진동수라고도 합니다. 물체를 그 고유 진동수로 반복적으로 밀면, 공명이 발생합니다."),
    ("This is a very relevant concept, as building resonance during an earthquake can also make a building shake and topple over, depending on the characteristics of the earthquake and the building.", "이것은 매우 중요한 개념인데, 지진 중 건물의 공명은 지진과 건물의 특성에 따라 건물을 흔들어 무너뜨릴 수도 있기 때문입니다."),
    ("Why do different instruments sound different, even when they are playing the same note? What determines what frequencies a string will vibrate at? These are the questions that we will investigate in this lesson.", "왜 같은 음을 연주해도 악기마다 소리가 다를까요? 현이 어떤 진동수로 진동할지를 결정하는 것은 무엇일까요? 이것이 이 수업에서 탐구할 질문들입니다."),

    # Explore this sections
    ("Explore this!", "탐구해 보세요!"),
    ("Access the following video to explore how a toy whistle generates its sound.", "다음 영상을 통해 장난감 호루라기가 소리를 만드는 원리를 탐구해 보세요."),
    ("Resonance in air columns is the key to how most wind instruments make their distinctive sounds.", "공기 기둥에서의 공명은 대부분의 관악기가 독특한 소리를 내는 핵심 원리입니다."),

    # Mechanical Resonance section
    ("Mechanical resonance", "역학적 공명"),
    ("Mechanical resonance is a form of resonance that occurs in mechanical systems, such as pendulums, springs, and so on.", "역학적 공명은 진자, 용수철 등의 역학적 시스템에서 발생하는 공명의 한 형태입니다."),
    ("When a person pushes another person on a swing, mechanical resonance can occur.", "사람이 다른 사람을 그네에서 밀 때, 역학적 공명이 발생할 수 있습니다."),
    ("If the person on the swing is pushed at the natural frequency of the swing, the amplitude of the swing will increase with each push.", "그네를 타는 사람을 그네의 고유 진동수로 밀면, 밀 때마다 그네의 진폭이 증가합니다."),
    ("However, if the person on the swing is pushed at a different frequency, the amplitude of the swing will not increase.", "그러나 다른 진동수로 밀면, 그네의 진폭은 증가하지 않습니다."),
    ("This also applies to a parent pushing a child on a playground swing.", "이것은 놀이터에서 부모가 아이를 그네에서 미는 것에도 적용됩니다."),
    ("If the parent pushes at the natural frequency, the child will swing higher and higher.", "부모가 고유 진동수로 밀면, 아이는 점점 더 높이 올라갑니다."),
    ("If not, the swing will not go very high at all.", "그렇지 않으면, 그네는 높이 올라가지 않습니다."),

    # Sympathetic vibrations
    ("A tuning fork that vibrates at a specific frequency can cause a nearby tuning fork with the same natural frequency to also vibrate. This is called a sympathetic vibration.", "특정 진동수로 진동하는 소리굽쇠는 같은 고유 진동수를 가진 근처의 소리굽쇠도 진동하게 할 수 있습니다. 이것을 공감 진동이라고 합니다."),

    # Examples of resonance
    ("Examples of resonance", "공명의 예"),
    ("A tuning fork that vibrates at a specific frequency can cause a nearby wine glass to vibrate if the wine glass has the same natural frequency. If the amplitude of the vibration is large enough, the wine glass can shatter.", "특정 진동수로 진동하는 소리굽쇠는 같은 고유 진동수를 가진 근처의 와인 잔을 진동시킬 수 있습니다. 진동의 진폭이 충분히 크면, 와인 잔이 깨질 수 있습니다."),

    # Tacoma Narrows
    ("The Tacoma Narrows Bridge in Washington State collapsed in 1940 due to resonance caused by wind.", "1940년에 워싱턴 주의 타코마 내로스 다리는 바람에 의한 공명 때문에 무너졌습니다."),
    ("The wind caused the bridge to vibrate at its natural frequency, which caused the amplitude of the vibration to increase until the bridge collapsed.", "바람이 다리를 고유 진동수로 진동하게 하여, 다리가 무너질 때까지 진동의 진폭이 증가했습니다."),

    # Applications
    ("A car stuck in snow can be freed by rocking it back and forth at its natural frequency.", "눈에 빠진 자동차는 고유 진동수로 앞뒤로 흔들어 빼낼 수 있습니다."),
    ("Soldiers are told to break step when crossing a footbridge, because if they all marched in step at the natural frequency of the bridge, the bridge could collapse.", "병사들은 보행교를 건널 때 보조를 흐트러뜨리라는 지시를 받는데, 모두 다리의 고유 진동수에 맞춰 행진하면 다리가 무너질 수 있기 때문입니다."),

    # Resonance in strings
    ("Resonance in strings", "현에서의 공명"),
    ("Standing waves in strings", "현에서의 정상파"),

    # Common labels
    ("Given:", "주어진 값:"),
    ("Unknown:", "구하는 값:"),
    ("Equation:", "공식:"),
    ("Solve:", "풀이:"),
    ("Statement:", "결론:"),
    ("Show Suggested Answer", "풀이 보기"),
    ("Suggested Answer", "풀이 예시"),
    ("Hints", "힌트"),
    ("Hint", "힌트"),
    ("Another Hint", "추가 힌트"),
    ("Try it!", "풀어 보세요!"),
    ("Example", "예제"),
    ("Summary", "요약"),
    ("Review", "복습"),

    # String resonance content
    ("When a string is fixed at both ends, standing waves can be produced.", "현이 양쪽 끝에 고정되어 있을 때, 정상파가 만들어질 수 있습니다."),
    ("The simplest standing wave that can be produced in a string fixed at both ends is one with a single loop.", "양쪽 끝이 고정된 현에서 만들 수 있는 가장 단순한 정상파는 하나의 루프를 가진 것입니다."),
    ("This is called the fundamental frequency.", "이것을 기본 진동수라고 합니다."),
    ("The frequency of the fundamental is the lowest frequency that can produce a standing wave in the string.", "기본 진동수는 현에서 정상파를 만들 수 있는 가장 낮은 진동수입니다."),

    # Universal wave equation references
    ("the universal wave equation", "파동의 기본 방정식"),
    ("The universal wave equation", "파동의 기본 방정식"),
    ("universal wave equation", "파동의 기본 방정식"),

    # Problem solving text
    ("Now try the following questions about standing waves in strings. Compare your answers to the suggested answers.", "다음 현의 정상파에 관한 문제를 풀어 보세요. 풀이 예시와 답을 비교해 보세요."),
    ("Now try the following questions about waves in open air columns. Compare your answers to the suggested answers.", "다음 열린 공기 기둥의 파동에 관한 문제를 풀어 보세요. 풀이 예시와 답을 비교해 보세요."),
    ("You can use your notebook to complete each of the following questions. Compare your work with the suggested answer to check your understanding. If you need a hint for the questions, press on the hint button.", "노트를 사용하여 다음 각 문제를 풀어 보세요. 풀이 예시와 비교하여 이해도를 확인하세요. 문제에 대한 힌트가 필요하면 힌트 버튼을 누르세요."),

    # Speed of sound formula reference
    ("the speed of sound formula", "음속 공식"),

    # Standing wave problems - strings section
    ("The speed of the wave is", "파동의 속력은"),
    ("Write a sentence that responds to the question, including a consideration of significant digits.", "유효 숫자를 고려하여 질문에 답하는 문장을 작성하세요."),

    # Question 2
    ("2. What is the wavelength of the fundamental frequency?", "2. 기본 진동수의 파장은 얼마인가요?"),
    ("The wavelength of the fundamental frequency is 8.0 m.", "기본 진동수의 파장은 8.0 m입니다."),

    # Question 3
    ("3. What is the fundamental frequency of the string?", "3. 현의 기본 진동수는 얼마인가요?"),
    (", from question (1) above. Note that when you use a previously-calculated value for another question, you use all available digits, not just the final statement that was rounded due to significant digits.", ", 위의 문제 (1)에서 구한 값입니다. 이전에 계산한 값을 다른 문제에 사용할 때는, 유효 숫자로 반올림한 최종 결론이 아닌, 모든 자릿수를 사용한다는 점에 유의하세요."),
    (", from question (2).", ", 문제 (2)에서 구한 값입니다."),
    (". Either equation would be appropriate, but if you used the one with L you should include L in the list of given values. This problem can be solved multiple ways. This suggested answer provides just one way. If you used another way, compare your final answer and ensure that the work is reasonable. Either way is acceptable.", ". 두 공식 모두 적절하지만, L이 포함된 공식을 사용했다면 주어진 값 목록에 L을 포함해야 합니다. 이 문제는 여러 방법으로 풀 수 있습니다. 이 풀이 예시는 한 가지 방법만 제시합니다. 다른 방법을 사용했다면, 최종 답을 비교하고 풀이가 합리적인지 확인하세요. 어느 방법이든 허용됩니다."),
    ("by rearranging the universal wave equation.", "파동의 기본 방정식을 변형하여."),
    ("The fundamental frequency is 5.0 Hz.", "기본 진동수는 5.0 Hz입니다."),

    # Question 4
    ("4. Find the frequency that will produce a standing wave with 3 loops.", "4. 3개의 루프를 가진 정상파를 만드는 진동수를 구하세요."),
    ("The frequency that creates a standing wave with three loops is 15 Hz. (2 significant digits, since 5.0 Hz, 4.0 m, and 0.10 s all had 2.)", "3개의 루프를 가진 정상파를 만드는 진동수는 15 Hz입니다. (5.0 Hz, 4.0 m, 0.10 s 모두 유효 숫자 2자리이므로 2자리로 나타냅니다.)"),

    # Question 5
    ("5. Identify another frequency that will produce a standing wave in the string. How many loops will it have?", "5. 현에서 정상파를 만드는 다른 진동수를 구하세요. 몇 개의 루프를 가지나요?"),
    (', we also want to know "how many loops will it have?" which is the subscript, which we named n. There are two unknowns in this question, so we put them both here.)', ", 또한 \"몇 개의 루프를 가지나요?\"도 알아야 하는데, 이는 아래 첨자 n에 해당합니다. 이 문제에는 미지수가 두 개이므로 둘 다 여기에 적습니다.)"),
    ("(from the table before this section)", "(이 단원 앞의 표 참조)"),
    ("First, pick any number", "먼저, 1이나 3이 아닌 아무 수"),
    ("that isn't 1 or 3 (since we covered those cases already). Any number could be chosen. 2 is a good choice, but this could just as easily have been 4, or 5, and so on.", "를 선택하세요 (이미 다룬 경우이므로). 아무 수나 선택할 수 있습니다. 2가 좋은 선택이지만, 4, 5 등도 마찬가지로 가능합니다."),
    ("Let", ""),
    (", which will have 2 loops. (Note that 10 Hz must be reported in scientific notation since it has 2 significant digits and", ", 2개의 루프를 가집니다. (10 Hz는 유효 숫자가 2자리이고"),
    ("only has 1.)", "은 1자리뿐이므로, 과학적 표기법으로 나타내야 합니다.)"),

    # Question 6
    ("6. Will a frequency of 23 Hz produce a standing wave in the string? Explain.", "6. 23 Hz의 진동수가 현에서 정상파를 만들 수 있나요? 설명하세요."),
    ("Since this question isn't just a calculation problem, it doesn't necessarily need the usual GUESS problem-solving structure. You certainly could use it, but it can be answered in words instead.", "이 문제는 단순한 계산 문제가 아니므로, 반드시 일반적인 GUESS 문제 풀이 구조를 따를 필요는 없습니다. 물론 사용할 수 있지만, 말로 답할 수도 있습니다."),
    ("No, 23 Hz will not produce a standing wave. All standing waves have frequencies that are integer multiples of the fundamental frequency, 5.0 Hz. Since 23 is not a multiple of 5, 23 Hz cannot create a standing wave in this string.", "아니요, 23 Hz는 정상파를 만들지 못합니다. 모든 정상파는 기본 진동수 5.0 Hz의 정수 배인 진동수를 가집니다. 23은 5의 배수가 아니므로, 23 Hz는 이 현에서 정상파를 만들 수 없습니다."),
    ("In some other strings, other fundamental frequencies are possible. But in this string, the only frequencies that create standing waves are multiples of 5.0 Hz.", "다른 현에서는 다른 기본 진동수가 가능합니다. 하지만 이 현에서는 5.0 Hz의 배수인 진동수만 정상파를 만들 수 있습니다."),

    # Air columns section
    ("Air columns", "공기 기둥"),
    ("Plucking a tight string does not produce a very loud noise. A guitar uses a tight string that is mounted over what is essentially a wooden box", "팽팽한 현을 뜯으면 그다지 큰 소리가 나지 않습니다. 기타는 본질적으로 나무 상자인 것 위에 팽팽한 현을 장착하여 사용합니다"),
    ("a box of air. The result is a loud sound. As you will learn, a box of air can use resonance to increase the volume of a quiet string into something that can be heard throughout a room.", "— 공기 상자입니다. 그 결과 큰 소리가 납니다. 배우게 되겠지만, 공기 상자는 공명을 이용하여 조용한 현의 소리를 방 전체에 들릴 수 있을 만큼 증폭시킬 수 있습니다."),
    ("Most tuning forks are not very loud when struck. Sometimes, to help increase the volume, they are mounted on top of wooden boxes that are open at one end, as shown in the following diagram.", "대부분의 소리굽쇠는 쳤을 때 그다지 크지 않습니다. 때때로 소리를 키우기 위해, 다음 그림과 같이 한쪽 끝이 열린 나무 상자 위에 장착합니다."),
    ("You have encountered this apparatus before. This apparatus is the same as the one demonstrated in the video about sympathetic vibrations occurring in tuning forks.", "이 장치는 이전에 접한 적이 있습니다. 이 장치는 소리굽쇠에서 발생하는 공감 진동에 대한 영상에서 시연된 것과 동일합니다."),

    # Closed air column
    ("The following video exhibits equipment that can be used to investigate resonance in a closed air column.", "다음 영상은 닫힌 공기 기둥에서 공명을 조사하는 데 사용할 수 있는 장비를 보여줍니다."),
    ("A closed air column is just a long container with air in it, but the container is open at one end and closed at the other.", "닫힌 공기 기둥은 공기가 들어 있는 긴 용기로, 한쪽 끝은 열려 있고 다른 쪽 끝은 닫혀 있습니다."),
    ("In the following setup, water is used to close the bottom end of the cylinder.", "다음 실험 장치에서는 물을 사용하여 원통의 바닥 끝을 닫습니다."),
    ("Placing a tuning fork at the top of the closed air column will send sound down into the column.", "닫힌 공기 기둥 위에 소리굽쇠를 놓으면 소리가 기둥 아래로 전달됩니다."),
    ("The sound can reflect off the water and move back up through the closed air column, producing a standing wave of sound.", "소리는 물에서 반사되어 닫힌 공기 기둥을 통해 다시 위로 올라가며, 소리의 정상파를 만들 수 있습니다."),
    ("The water will act like a fixed end, meaning that there will always be a node at the bottom of the closed air column.", "물은 고정 끝처럼 작용하여, 닫힌 공기 기둥의 바닥에는 항상 마디가 있습니다."),
    ("If an antinode (wide part of the wave) is located at the top of the closed air column, a person will hear a much louder sound coming from the tuning fork than would normally be heard, due to resonance.", "배(파동의 넓은 부분)가 닫힌 공기 기둥의 꼭대기에 위치하면, 공명으로 인해 소리굽쇠에서 평소보다 훨씬 큰 소리가 들립니다."),
    ("This is very similar to the standing waves produced in strings. In strings, both ends were nodes. In this type of air column, one end will be a node and one end will be an antinode.", "이것은 현에서 만들어지는 정상파와 매우 유사합니다. 현에서는 양쪽 끝이 마디였습니다. 이 유형의 공기 기둥에서는 한쪽 끝이 마디이고 다른 쪽 끝이 배입니다."),
    ("The shortest air column that will produce resonance with the tuning fork is demonstrated in the following simplified diagram.", "소리굽쇠와 공명을 만드는 가장 짧은 공기 기둥이 다음 간략화된 그림에 나타나 있습니다."),
    ("In this case, since only half of a loop is present, the length of air column is:", "이 경우, 루프의 절반만 있으므로 공기 기둥의 길이는:"),
    ("If the air column is raised, there will no longer be a loud sound. Eventually, another antinode will be positioned at the top of the air column and resonance will take place again, producing another loud sound. In this case, one complete loop and half of a loop will fit inside the air column.", "공기 기둥을 올리면 더 이상 큰 소리가 나지 않습니다. 결국 다른 배가 공기 기둥의 꼭대기에 위치하게 되고 다시 공명이 일어나 큰 소리가 납니다. 이 경우, 완전한 루프 하나와 루프의 절반이 공기 기둥 안에 들어갑니다."),
    ("As previously mentioned, one loop has a length equal to half the wavelength of the wave. In this case, the second resonant length of the air column is:", "앞서 언급했듯이, 하나의 루프는 파동 파장의 절반과 같은 길이를 가집니다. 이 경우, 공기 기둥의 두 번째 공명 길이는:"),
    ("Notice that this resonant length is one loop longer, or", "이 공명 길이는 첫 번째보다 루프 하나, 즉"),
    ("longer than the first.", "만큼 더 깁니다."),
    ("To find the third resonant length, add another loop, or", "세 번째 공명 길이를 구하려면 루프 하나, 즉"),
    ("This means that the third resonant length is:", "이것은 세 번째 공명 길이가 다음과 같다는 것을 의미합니다:"),

    # Summary for closed air columns
    ("If we know the frequency of the sound wave, we can calculate the length of the closed air column that is needed to create a resonant length. The resonant length is important because that is what creates the loud sound. If the air column was not the correct length, the sound would not get amplified because there would be no resonance.", "음파의 진동수를 알면, 공명 길이를 만드는 데 필요한 닫힌 공기 기둥의 길이를 계산할 수 있습니다. 공명 길이는 큰 소리를 만드는 것이기 때문에 중요합니다. 공기 기둥이 올바른 길이가 아니면, 공명이 없기 때문에 소리가 증폭되지 않습니다."),
    ("and so on.", "등등."),
    ("Length", "길이"),
    ("Number of loops in standing wave", "정상파의 루프 수"),
    ("Diagram of standing wave", "정상파 그림"),

    # Closed air column problems
    ("1. The first resonant length of a closed air column is 20 cm. Find the second and third resonant lengths.", "1. 닫힌 공기 기둥의 첫 번째 공명 길이는 20 cm입니다. 두 번째와 세 번째 공명 길이를 구하세요."),
    ("Referring to the table above, is there a mathematical relationship between the resonant lengths that you could use here? Perhaps try writing out the given and unknown values, and finding an equation that incorporates both of those values.", "위의 표를 참고하여, 여기서 사용할 수 있는 공명 길이들 사이의 수학적 관계가 있나요? 주어진 값과 구하는 값을 적어 보고, 두 값을 모두 포함하는 공식을 찾아보세요."),
    ("There are at least two different ways to solve this problem. One way is to use the given length to find the wavelength of the sound waves, then use that to calculate the other resonant lengths. The other is this suggested answer. Either would be accepted.", "이 문제를 풀 수 있는 방법은 최소 두 가지입니다. 한 가지는 주어진 길이를 사용하여 음파의 파장을 구한 다음 다른 공명 길이를 계산하는 것입니다. 다른 방법은 이 풀이 예시입니다. 어느 방법이든 허용됩니다."),
    ("Checking the table above, some of the equations we have are:", "위의 표를 확인하면, 사용할 수 있는 공식들은 다음과 같습니다:"),
    ("The second resonant length is 60 cm and the third resonant length is 100 cm. (Since the given first resonant length had one significant digit, these are reported with one significant digit.)", "두 번째 공명 길이는 60 cm이고 세 번째 공명 길이는 100 cm입니다. (주어진 첫 번째 공명 길이가 유효 숫자 1자리이므로, 1자리로 나타냅니다.)"),

    # Problem 2 - shortest air column
    ("2. What is the shortest air column that will resonate with a tuning fork with a frequency of 460 Hz, when the speed of sound in air is 344 m/s?", "2. 공기 중 음속이 344 m/s일 때, 진동수 460 Hz의 소리굽쇠와 공명하는 가장 짧은 공기 기둥의 길이는 얼마인가요?"),
    ("can be used to find the wavelength, at which point the usual resonant length formula can be used.", "을 사용하여 파장을 구한 다음, 일반적인 공명 길이 공식을 사용할 수 있습니다."),
    ("(We know it's", "(가장 \"짧은\" 공기 기둥을 원하므로"),
    ("since we want the \"shortest\" air column", "임을 알 수 있습니다"),
    ("all other lengths are longer than this.)", "— 다른 모든 길이는 이보다 깁니다.)"),
    ("First, find the wavelength.", "먼저 파장을 구합니다."),
    ("(Keep a few extra decimal places in your written solutions, and do your best to keep the full value in your calculator as you work.)", "(풀이에서 소수점 아래 몇 자리를 더 유지하고, 계산기에서 전체 값을 유지하도록 하세요.)"),
    ("The shortest air column that will resonate with the given frequency is one measuring 0.19 m. (2 significant digits, since", "주어진 진동수와 공명하는 가장 짧은 공기 기둥의 길이는 0.19 m입니다. (유효 숫자 2자리,"),
    ("has 2.)", "가 2자리이므로.)"),

    # Problem 3 - tuning fork closed pipe
    ("3. A tuning fork causes resonance in a pipe with one closed end. The difference between the first resonant length and the second resonant length is 0.390 m. The air temperature is 26.0", "3. 소리굽쇠가 한쪽 끝이 닫힌 관에서 공명을 일으킵니다. 첫 번째 공명 길이와 두 번째 공명 길이의 차이는 0.390 m입니다. 공기 온도는 26.0"),
    ("C. Find the frequency of the turning fork and the third resonant length of the pipe.", "°C입니다. 소리굽쇠의 진동수와 관의 세 번째 공명 길이를 구하세요."),
    ("Setting out the given and unknown values helps in identifying the appropriate formula(s). If there is more than one equation, they could be combined. In addition, you will need to refer back to the speed of sound formula from earlier in the unit. This solution will be longer than the others we", "주어진 값과 구하는 값을 정리하면 적절한 공식을 찾는 데 도움이 됩니다. 공식이 여러 개이면 결합할 수 있습니다. 또한, 이 단원 앞부분의 음속 공식을 참고해야 합니다. 이 풀이는 지금까지의 것보다 길 것입니다"),
    ("ve encountered so far, since it combines multiple areas of knowledge.", ", 여러 지식 영역을 결합하기 때문입니다."),
    ("Use the temperature to find speed, then the difference in resonant lengths to find wavelength. Use those to find frequency. Afterwards, use the wavelength to find the third resonant length.", "온도를 사용하여 속력을 구하고, 공명 길이의 차이를 사용하여 파장을 구하세요. 이를 사용하여 진동수를 구하세요. 그 후, 파장을 사용하여 세 번째 공명 길이를 구하세요."),
    ("This is a complicated problem, with multiple steps. Take your time, perform rough work in your notebook, and check your answers. A suggested answer is presented here for you to follow along. If you get stuck, read just the next step and think about whether you can continue from there.", "이것은 여러 단계를 가진 복잡한 문제입니다. 시간을 가지고, 노트에 계산을 하고, 답을 확인하세요. 여기에 풀이 예시가 제시되어 있으니 따라가 보세요. 막히면 다음 단계만 읽고 거기서 계속할 수 있는지 생각해 보세요."),
    ("(There are many equations that can be combined in this situation. You can start by writing out as many as possible, then remove the ones you don't end up using. The GUESS problem-solving structure is a way to communicate your thinking, but it doesn't mean you can't edit it afterwards to ensure a clean, polished, professional presentation.)", "(이 상황에서는 결합할 수 있는 공식이 많습니다. 가능한 한 많은 공식을 적어 시작한 다음, 사용하지 않는 것을 제거할 수 있습니다. GUESS 문제 풀이 구조는 사고를 전달하는 방법이지만, 깔끔하고 체계적인 발표를 위해 나중에 편집할 수 없다는 의미는 아닙니다.)"),
    ("First, find the frequency. (The question asks for frequency first, then the third resonant length, which implies frequency can be found first. If I try this and get stuck, I can always try the other order and edit this statement.)", "먼저 진동수를 구합니다. (문제가 진동수를 먼저, 그 다음 세 번째 공명 길이를 묻고 있으므로, 진동수를 먼저 구할 수 있음을 암시합니다. 이 방법으로 시도해 보고 막히면, 순서를 바꿔 시도할 수 있습니다.)"),
    ("Start with the speed of sound.", "먼저 음속을 구합니다."),
    ("The only one of my formulas that involves frequency is the universal wave equation. I have speed, so to find frequency I also need to find wavelength.", "제 공식 중 진동수가 포함된 유일한 것은 파동의 기본 방정식입니다. 속력을 알고 있으므로, 진동수를 구하려면 파장도 구해야 합니다."),
    ("and substitute.", "그리고 대입합니다."),
    ("Substituting the wavelength terms,", "파장 항을 대입하면,"),
    ("Use decimals or collect like terms:", "소수로 바꾸거나 동류항을 정리합니다:"),
    ("(either would be appropriate, pick the one you're most comfortable with)", "(둘 다 적절합니다, 편한 것을 선택하세요)"),
    ("Use your algebra skills to get the wavelength alone.", "대수학 기술을 사용하여 파장만 남기세요."),
    ("Now that we have both speed and wavelength, we can find frequency.", "이제 속력과 파장을 모두 구했으므로, 진동수를 구할 수 있습니다."),
    ('Double-checking the "Unknown" section of GUESS, we have the solution to one part but not the other. We still need the other resonant length.', 'GUESS의 "구하는 값" 부분을 다시 확인하면, 한 부분의 답은 구했지만 다른 부분은 아직입니다. 다른 공명 길이를 아직 구해야 합니다.'),
    ("The frequency is 445 Hz and the third resonant length is 0.975 m.", "진동수는 445 Hz이고 세 번째 공명 길이는 0.975 m입니다."),

    # Problem 4 - ship's whistle
    ("So far we have analyzed changing the length of a closed air column. If the speed of sound is constant and a closed air column's length is also constant, we can also consider the column as having resonant frequencies by adjusting the wavelength. Apply your knowledge of closed air columns to this new situation by answering the following question.", "지금까지 닫힌 공기 기둥의 길이를 변화시키는 것을 분석했습니다. 음속이 일정하고 닫힌 공기 기둥의 길이도 일정하다면, 파장을 조절하여 기둥이 공명 진동수를 가지는 것으로 생각할 수 있습니다. 닫힌 공기 기둥에 대한 지식을 다음 문제에 적용해 보세요."),
    ("4. A ship's whistle is 0.50 m long and is closed at one end. If the speed of sound is 350 m/s, calculate the first and second resonant frequencies for the ship's whistle.", "4. 배의 기적은 길이가 0.50 m이고 한쪽 끝이 닫혀 있습니다. 음속이 350 m/s일 때, 배 기적의 첫 번째와 두 번째 공명 진동수를 계산하세요."),
    ('Consider the universal wave equation, and what you know about wavelengths in closed air columns. This is new, but the "first fundamental frequency" of a closed air column would be the frequency corresponding to a quarter-wavelength in the column', "파동의 기본 방정식과 닫힌 공기 기둥의 파장에 대해 알고 있는 것을 생각해 보세요. 이것은 새로운 것이지만, 닫힌 공기 기둥의 \"첫 번째 기본 진동수\"는 기둥에서 파장의 4분의 1에 해당하는 진동수입니다"),
    ("This is a new situation, so try to transfer your understanding to this new arrangement of waves.", "이것은 새로운 상황이므로, 이해한 내용을 이 새로운 파동 배열에 적용해 보세요."),
    ("The first resonant frequency would be the frequency corresponding to", "첫 번째 공명 진동수는"),
    ("에 해당하는 진동수입니다.", "에 해당하는 진동수입니다."),
    ("By applying my prior knowledge to this new situation, the first resonant frequency is 180 Hz and the second resonant frequency is 530 Hz. (two significant digits are used in the statement since the given length and speed each have two significant digits.)", "이전 지식을 새로운 상황에 적용하면, 첫 번째 공명 진동수는 180 Hz이고 두 번째 공명 진동수는 530 Hz입니다. (주어진 길이와 속력이 각각 유효 숫자 2자리이므로 2자리로 나타냅니다.)"),

    # Lab reports section
    ("Lab reports", "실험 보고서"),
    ("A lab report is a piece of scientific writing. Lab reports follow a standard structure so that the interesting information contained can be reliably interpreted by other scientists. A lab report is a scientist's evidence that they performed the stated experiment, found the given results, and made the stated conclusions in a transparent way. They are written in a way that can be repeated by other scientists wishing to verify the results.", "실험 보고서는 과학적 글쓰기의 한 형태입니다. 실험 보고서는 표준 구조를 따르므로, 포함된 흥미로운 정보를 다른 과학자들이 신뢰성 있게 해석할 수 있습니다. 실험 보고서는 과학자가 명시된 실험을 수행하고, 주어진 결과를 찾고, 명시된 결론을 투명한 방식으로 내렸다는 증거입니다. 결과를 검증하려는 다른 과학자들이 반복할 수 있는 방식으로 작성됩니다."),
    ("One of the expectations of this course is for you to understand and create lab reports.", "이 과정의 기대 사항 중 하나는 실험 보고서를 이해하고 작성하는 것입니다."),
    ("If you would like to refer to a sample lab report, you can access the example below. This is an example report for a slightly different experiment. You may use it to better format your lab report. You do not need to perform this experiment.", "샘플 실험 보고서를 참고하려면 아래 예시에 접근할 수 있습니다. 이것은 약간 다른 실험에 대한 예시 보고서입니다. 실험 보고서 형식을 개선하는 데 사용할 수 있습니다. 이 실험을 수행할 필요는 없습니다."),
    ("Press here for a sample lab report.", "샘플 실험 보고서를 보려면 여기를 누르세요."),
    ("Explore the following lab activity.", "다음 실험 활동을 탐구하세요."),
    ("Lab activity", "실험 활동"),
    ("Speed of sound in air using a closed air column lab", "닫힌 공기 기둥을 이용한 공기 중 음속 측정 실험"),
    ("Your task is now to review the lab and then explore the video. Then, complete the analysis and conclusion question. You will refer back to this activity in the Unit 1 Assignment.", "이제 실험을 검토한 다음 영상을 탐구하세요. 그런 다음 분석과 결론 질문을 완성하세요. 단원 1 과제에서 이 활동을 다시 참고하게 됩니다."),
    ("Purpose", "목적"),
    ("Materials", "재료"),
    ("Apparatus", "실험 장치"),
    ("Method", "방법"),
    ("Analysis", "분석"),
    ("Conclusion", "결론"),
    ("To calculate the speed of sound in air using the resonant lengths of a closed air column.", "닫힌 공기 기둥의 공명 길이를 이용하여 공기 중 음속을 계산한다."),
    ("tube, water, graduated cylinder, tuning fork, mallet, ruler", "관, 물, 눈금 실린더, 소리굽쇠, 망치, 자"),
    ("Fill a graduated cylinder with water.", "눈금 실린더에 물을 채웁니다."),
    ("Place a tube inside (making the end in the water a closed end).", "관을 안에 넣습니다 (물 속의 끝을 닫힌 끝으로 만듭니다)."),
    ("Sound the tuning fork (f = 1024 Hz).", "소리굽쇠를 칩니다 (f = 1024 Hz)."),
    ("Place it close to the open end of the closed air column.", "닫힌 공기 기둥의 열린 끝 가까이에 놓습니다."),
    ("Raise it from the water until a loud sound (resonance) is observed.", "큰 소리(공명)가 관찰될 때까지 물에서 올립니다."),
    ("Measure the length of the air column. This is the resonant length", "공기 기둥의 길이를 측정합니다. 이것이 공명 길이"),
    ("Repeat the procedure until the second resonant length", "두 번째 공명 길이"),
    (") is observed.", ")가 관찰될 때까지 절차를 반복합니다."),
    ("Complete the following questions.", "다음 질문을 완성하세요."),
    ("Using the equations for the resonant lengths, calculate the wavelength (in metres). Do this for both", "공명 길이 공식을 사용하여 파장(미터 단위)을 계산하세요."),
    ("Using the universal wave equation", "파동의 기본 방정식을 사용하여"),
    (", calculate the speed of sound in air using the frequency of the tuning fork (f = 1024 Hz) and the wavelength calculated in Question 1.", ", 소리굽쇠의 진동수 (f = 1024 Hz)와 문제 1에서 계산한 파장을 사용하여 공기 중 음속을 계산하세요."),
    ("Find the theoretical speed in air at 23.0", "23.0"),
    ("C using the equation:", "°C에서의 이론적 음속을 다음 공식을 사용하여 구하세요:"),
    ("Find the percent error for the experimental speed of sound calculations compared to the theoretical speed of sound in air. Use the formula:", "실험적 음속 계산값과 이론적 공기 중 음속을 비교한 백분율 오차를 구하세요. 다음 공식을 사용하세요:"),
    ("Percent Error", "백분율 오차"),
    ("experimental value", "실험값"),
    ("theoretical value", "이론값"),
    ("Write your own conclusion for the experiment based on the purpose of the lab, your results, and your analysis.", "실험 목적, 결과, 분석을 바탕으로 실험에 대한 자신만의 결론을 작성하세요."),
    ("Access the following video, which freezes a few times (so you can read the on-screen descriptions), to experience the apparatus and the results of the experiment.", "다음 영상을 시청하세요. 영상이 몇 번 멈추므로 (화면의 설명을 읽을 수 있도록) 실험 장치와 결과를 확인할 수 있습니다."),

    # Open air columns
    ("Open air columns", "열린 공기 기둥"),
    ("So far you have investigated standing waves with two fixed ends (nodes at each end), and standing waves with one fixed and one free end (one end is a node and one is an antinode). Another type of air column exists, where a long cylinder is open at both ends. This is called an open air column. This new type is formed when both ends of the wave are antinodes.", "지금까지 양쪽 끝이 고정된 정상파(양쪽 끝에 마디)와 한쪽이 고정되고 한쪽이 자유인 정상파(한쪽 끝이 마디이고 한쪽이 배)를 조사했습니다. 긴 원통의 양쪽 끝이 모두 열린 다른 유형의 공기 기둥이 있습니다. 이것을 열린 공기 기둥이라고 합니다. 이 새로운 유형은 파동의 양쪽 끝이 모두 배일 때 형성됩니다."),
    ("The following diagrams display the standing waves formed in an air column that is open both ends.", "다음 그림들은 양쪽 끝이 모두 열린 공기 기둥에서 형성되는 정상파를 보여줍니다."),
    ("First resonant length", "첫 번째 공명 길이"),
    ("Second resonant length", "두 번째 공명 길이"),
    ("Third resonant length", "세 번째 공명 길이"),
    ("The following diagram is of first length of air that will cause a loud sound from the tuning fork. The length is equal to", "다음 그림은 소리굽쇠에서 큰 소리를 만드는 첫 번째 공기 길이입니다. 길이는"),
    ("Given speed of sound and the frequency of the tuning fork, the universal wave equation can be used to find the wavelength if needed.", "음속과 소리굽쇠의 진동수가 주어지면, 필요시 파동의 기본 방정식을 사용하여 파장을 구할 수 있습니다."),
    ("The following diagram is of the second length of air that will cause a loud sound from the tuning fork. The length is equal to", "다음 그림은 소리굽쇠에서 큰 소리를 만드는 두 번째 공기 길이입니다. 길이는"),
    ("The following diagram is of third length of air that will cause a loud sound from the tuning fork. The length is equal to", "다음 그림은 소리굽쇠에서 큰 소리를 만드는 세 번째 공기 길이입니다. 길이는"),

    # Open air column example
    ("An organ pipe, which is 1.2 m long and open at both ends, produces a note with the fundamental frequency. If the speed of sound in air is 345 m/s, what is the fundamental frequency?", "양쪽 끝이 열린 길이 1.2 m의 오르간 파이프가 기본 진동수의 음을 냅니다. 공기 중 음속이 345 m/s일 때, 기본 진동수는 얼마인가요?"),
    ("Then, use the universal wave equation to find the frequency.", "그런 다음, 파동의 기본 방정식을 사용하여 진동수를 구합니다."),
    ("Therefore, the fundamental frequency of the pipe is 144 Hz.", "따라서, 파이프의 기본 진동수는 144 Hz입니다."),

    # Open air column summary
    ("If we know the frequency of the sound wave, we can predict the length of the open air column that is needed to create a resonant length. The resonant length is important because that is what creates the loud sound. If the air column was not the correct length, the sound would not get amplified because there would be no resonance.", "음파의 진동수를 알면, 공명 길이를 만드는 데 필요한 열린 공기 기둥의 길이를 예측할 수 있습니다. 공명 길이는 큰 소리를 만드는 것이기 때문에 중요합니다. 공기 기둥이 올바른 길이가 아니면, 공명이 없기 때문에 소리가 증폭되지 않습니다."),

    # Open air column problems
    ("1. A tuning fork with a frequency of 380 Hz is sounded near the top of an open air column when the speed of sound is 344 m/s. What is the wavelength of the sound? What are the first three resonant lengths?", "1. 음속이 344 m/s일 때, 진동수 380 Hz의 소리굽쇠를 열린 공기 기둥 위에서 칩니다. 소리의 파장은 얼마인가요? 처음 세 공명 길이는 얼마인가요?"),
    ("(With two significant digits, this will probably be the value that limits the significant digits of our reported answer.)", "(유효 숫자 2자리이므로, 이것이 최종 답의 유효 숫자를 제한할 것입니다.)"),
    ("The wavelength is 0.91 m and the first three resonant lengths are 0.45 m, 0.91 m, and 1.4 m.", "파장은 0.91 m이고 처음 세 공명 길이는 0.45 m, 0.91 m, 1.4 m입니다."),
    (", so", ", 따라서"),

    # Problem 2 open air
    ("2. A 450 Hz tuning fork is held at the top of an open air column when the temperature of the air is 18", "2. 공기 온도가 18"),
    ("C. How much longer is the third resonant length than the second resonant length?", "°C일 때, 450 Hz 소리굽쇠를 열린 공기 기둥 위에서 칩니다. 세 번째 공명 길이는 두 번째 공명 길이보다 얼마나 더 긴가요?"),
    ("First, find the speed of sound.", "먼저 음속을 구합니다."),
    ("The third resonant length is 0.38 m longer than the second resonant length.", "세 번째 공명 길이는 두 번째 공명 길이보다 0.38 m 더 깁니다."),
    ("(An interesting observation: since each resonant length is one", "(흥미로운 관찰: 각 공명 길이는 이전 것보다"),
    ("longer than the previous one, all pairs of consecutive resonant lengths will also have this difference.)", "만큼 더 기므로, 연속된 모든 공명 길이 쌍도 이 차이를 가집니다.)"),

    # Problem 3 open air
    ("3. An open air column is set up inside a home so that it will resonate with a tuning fork, using its first resonant length. Both the air column and tuning fork are taken outside in the wintertime, but now, resonance is not observed. Explain why this happens.", "3. 열린 공기 기둥을 집 안에 설치하여 첫 번째 공명 길이로 소리굽쇠와 공명하도록 합니다. 공기 기둥과 소리굽쇠를 모두 겨울에 밖으로 가져갔지만, 이제 공명이 관찰되지 않습니다. 이유를 설명하세요."),
    ("Resonance in an air column is related to the frequency, and the speed of sound, combining to make just the right wavelength.", "공기 기둥에서의 공명은 진동수와 음속이 결합하여 정확한 파장을 만드는 것과 관련됩니다."),
    ("Outside in the wintertime, the temperature of the air is lower and so the speed of sound is lower.", "겨울에 밖에서는 공기 온도가 낮으므로 음속도 낮습니다."),
    ("Since the speed of sound is now lower, the wavelength associated with the tuning fork's frequency is lower and no longer matches the resonant length of the open air column. As a result, the constructive interference required for resonance does not occur, and resonance is not observed.", "음속이 낮아졌으므로, 소리굽쇠의 진동수에 해당하는 파장도 짧아져 열린 공기 기둥의 공명 길이와 더 이상 일치하지 않습니다. 그 결과, 공명에 필요한 보강 간섭이 발생하지 않아 공명이 관찰되지 않습니다."),

    # Problem 4 open air
    ("4. Explain whether a tuning fork with a lower or a higher frequency will be required to cause resonance outside.", "4. 밖에서 공명을 일으키려면 더 낮은 진동수의 소리굽쇠가 필요한지 더 높은 진동수의 소리굽쇠가 필요한지 설명하세요."),
    ("The speed of sound outside is slower. Since", "밖에서의 음속은 더 느립니다."),
    (", to keep wavelength the same with the smaller speed, frequency would also need to be made smaller. We would need a tuning fork with a lower frequency to cause resonance outside. This is one of the reasons it's important to tune an instrument in the same environment it will be played.", ", 더 느린 속력에서 파장을 같게 유지하려면, 진동수도 작아져야 합니다. 밖에서 공명을 일으키려면 더 낮은 진동수의 소리굽쇠가 필요합니다. 이것이 악기를 연주할 환경과 같은 환경에서 조율하는 것이 중요한 이유 중 하나입니다."),

    # Application: Instruments
    ("Application: Instruments", "응용: 악기"),
    ("Wind instruments", "관악기"),
    ("String instruments", "현악기"),
    ("Human voice", "사람의 목소리"),
    ("Percussion", "타악기"),
    ("All wind instruments contain air columns that cause resonance to produce sound. The frequency of the sound produced depends on the length of the air column. In general, larger instruments have longer air columns and lower frequency sound. Smaller wind instruments will have shorter air columns and will produce higher frequency sounds. In some wind instruments the length of the air column is fixed, while in others, the length can be changed. In addition, many wind instruments have air columns that are bent into loops to decrease the overall length of the instrument. A trombone, for example, uses a variable column length and is bent into a loop to reduce its overall length.", "모든 관악기는 소리를 내기 위해 공명을 일으키는 공기 기둥을 포함합니다. 발생하는 소리의 진동수는 공기 기둥의 길이에 따라 달라집니다. 일반적으로, 더 큰 악기는 더 긴 공기 기둥과 더 낮은 진동수의 소리를 가집니다. 더 작은 관악기는 더 짧은 공기 기둥을 가지며 더 높은 진동수의 소리를 냅니다. 일부 관악기에서는 공기 기둥의 길이가 고정되어 있고, 다른 것에서는 길이를 바꿀 수 있습니다. 또한, 많은 관악기는 악기의 전체 길이를 줄이기 위해 공기 기둥이 루프 형태로 구부러져 있습니다. 예를 들어, 트롬본은 가변 기둥 길이를 사용하며 전체 길이를 줄이기 위해 루프로 구부러져 있습니다."),
    ("To produce sound in the air columns in wind instruments, students need something that will vibrate back and forth. One way to make sound is to blow air into the tube and past a membrane called a reed. The turbulence from the wind will cause the reed to vibrate and produce sound.", "관악기의 공기 기둥에서 소리를 내려면, 앞뒤로 진동하는 것이 필요합니다. 소리를 내는 한 가지 방법은 관에 공기를 불어 리드라고 하는 막을 지나가게 하는 것입니다. 바람의 난류가 리드를 진동시켜 소리를 만듭니다."),
    ("Instruments that use this method include the saxophone and the clarinet. Another way to produce sound in a wind instrument is to use the player's lips as the source of vibration. In this case, the player's lips act like a double reed. Typically, this method is used with brass instruments like the trombone, trumpet, and tuba.", "이 방법을 사용하는 악기에는 색소폰과 클라리넷이 있습니다. 관악기에서 소리를 내는 다른 방법은 연주자의 입술을 진동원으로 사용하는 것입니다. 이 경우, 연주자의 입술이 이중 리드처럼 작용합니다. 일반적으로 이 방법은 트롬본, 트럼펫, 튜바 같은 금관악기에 사용됩니다."),
    ("String instruments, such as a piano, guitar, and violin, use a vibrator (the string), as well as a resonator, to produce sound. The resonator is similar to the box closed at one end that is used to magnify the sound of tuning forks. Normally, a string by itself will not produce a very loud sound or even a very pleasant one.", "피아노, 기타, 바이올린 같은 현악기는 진동체(현)와 공명체를 사용하여 소리를 냅니다. 공명체는 소리굽쇠의 소리를 증폭시키는 데 사용되는 한쪽 끝이 닫힌 상자와 유사합니다. 보통, 현 자체만으로는 매우 큰 소리나 쾌적한 소리를 내지 못합니다."),
    ("Focusing the sound of a string into a resonator increases not only the volume of the sound through resonance, but also the quality of the sound. Some string instruments are played by plucking or striking the strings. Plucking a string in the centre will cause it to vibrate in its fundamental mode, with only one loop in the string. Plucking the string one-quarter of its entire length from one fixed end will cause it to vibrate with more than one frequency, simultaneously. The standing wave pattern produced in the string could be the superposition of a single loop interfering with another standing wave pattern with two loops. This interference pattern resulting from more than one frequency vibrating at a time will change the quality of the sound produced.", "현의 소리를 공명체에 집중시키면 공명을 통해 소리의 크기뿐만 아니라 음질도 향상됩니다. 일부 현악기는 현을 뜯거나 쳐서 연주합니다. 현의 중앙을 뜯으면 현이 하나의 루프만 있는 기본 모드로 진동합니다. 고정된 한쪽 끝에서 전체 길이의 4분의 1 지점을 뜯으면, 동시에 둘 이상의 진동수로 진동하게 됩니다. 현에서 만들어지는 정상파 패턴은 단일 루프와 두 개의 루프를 가진 다른 정상파 패턴의 중첩일 수 있습니다. 동시에 둘 이상의 진동수가 진동하여 만들어지는 이 간섭 패턴은 발생하는 소리의 음질을 변화시킵니다."),
    ("The human voice is the oldest form of a musical instrument. It consists of three main parts: the lungs, which provide the source of air; the vocal cords, which act as a double-reed vibrator; and the lower throat, which acts as a resonator.", "사람의 목소리는 가장 오래된 형태의 악기입니다. 세 가지 주요 부분으로 구성됩니다: 공기원을 제공하는 폐, 이중 리드 진동체 역할을 하는 성대, 그리고 공명체 역할을 하는 하부 인후입니다."),
    ("Typically, air from the lungs is forced past the vocal cords, causing them to vibrate. The frequency of the vibration is controlled by the tension in the cords, as well as their size. Loudness will increase if the amount of air forced from the lungs is increased. The quality of the sound is determined by resonance in the lower throat. Quality can be improved with training.", "일반적으로, 폐에서 나온 공기가 성대를 지나면서 성대를 진동시킵니다. 진동의 진동수는 성대의 장력과 크기에 의해 조절됩니다. 폐에서 밀어내는 공기량이 증가하면 음량이 커집니다. 소리의 음질은 하부 인후의 공명에 의해 결정됩니다. 훈련으로 음질을 개선할 수 있습니다."),
    ("Percussion instruments are played by striking a hard object, such as a hammer, bar, or stick, against another object. The most commonly used percussion instrument today is the drum. A typical drum set also includes one or more cymbal. Any percussion instrument vibrates when struck. It is the vibration of the object that produces the sound. Often, these instruments are used to keep the time for a band or orchestra. A drum consists of a membrane stretched over a cylinder.", "타악기는 망치, 막대, 스틱 같은 단단한 물체로 다른 물체를 쳐서 연주합니다. 오늘날 가장 일반적으로 사용되는 타악기는 드럼입니다. 일반적인 드럼 세트에는 하나 이상의 심벌즈도 포함됩니다. 모든 타악기는 쳤을 때 진동합니다. 소리를 내는 것은 물체의 진동입니다. 이 악기들은 종종 밴드나 오케스트라의 박자를 맞추는 데 사용됩니다. 드럼은 원통 위에 막을 팽팽하게 늘인 것으로 구성됩니다."),
    ("When the membrane is struck it vibrates back and forth, producing a two-dimensional standing wave that helps to amplify the sound. In addition, the sound echoes throughout the cylindrical frame, which causes resonance and improves the quality of the sound. The tighter the membrane is stretched across the hollow cylindrical frame, and the smaller the drum is, the higher the frequency of sound will be.", "막을 치면 앞뒤로 진동하여 소리를 증폭시키는 2차원 정상파를 만듭니다. 또한, 소리가 원통형 프레임 전체에 반향되어 공명을 일으키고 음질을 향상시킵니다. 막이 빈 원통형 프레임에 더 팽팽하게 당겨질수록, 그리고 드럼이 작을수록, 소리의 진동수가 높아집니다."),

    # Consolidation section
    ("Putting it all together", "종합하기"),
    ("Sea shells: Magic or science?", "조개껍데기: 마법인가 과학인가?"),
    ("If a person holds up a sea shell to their ear, it is said they will hear the sea. Record questions that you might have about this situation.", "조개껍데기를 귀에 대면 바다 소리가 들린다고 합니다. 이 상황에 대해 가질 수 있는 질문을 기록하세요."),
    ("Access the following video for an explanation of what causes the sound heard in a sea shell.", "조개껍데기에서 들리는 소리의 원인에 대한 설명을 다음 영상에서 확인하세요."),

    # Indigenous content
    ("Connecting our globe", "세계와의 연결"),
    ("In Indigenous communities across Canada, drums are an integral part of many First Nations,", "캐나다 전역의 원주민 공동체에서, 드럼은 많은 퍼스트 네이션,"),
    ("tis, and Inuit cultures. Some Indigenous peoples use large drums at gatherings such as powwows or socials as well as small hand drums that a person can hold and play. Drums are constructed based on the distinct geography and traditions of a particular community.", "메티, 이누이트 문화의 필수적인 부분입니다. 일부 원주민은 파우와우나 사교 모임 같은 행사에서 큰 드럼을 사용하며, 한 사람이 들고 연주할 수 있는 작은 핸드 드럼도 사용합니다. 드럼은 특정 공동체의 고유한 지리와 전통에 따라 제작됩니다."),
    ("For example, an Inuit hand drum, also known as a qilaut, is made out of caribou and seal skin, while a Haudenosaunee water drum is made from a local tree such as cedar or maple with deer hide stretched over top.", "예를 들어, 킬라우트라고도 알려진 이누이트 핸드 드럼은 순록과 물범 가죽으로 만들어지며, 하우데노소니 워터 드럼은 삼나무나 단풍나무 같은 지역 나무에 사슴 가죽을 위에 팽팽하게 늘여 만듭니다."),
    ("Qilaut from Eskimo Point, an Inuit settlement in the north of Canada.", "캐나다 북부의 이누이트 정착지인 에스키모 포인트의 킬라우트."),
    ("In First Nations,", "퍼스트 네이션,"),
    ("tis, and Inuit communities, drumming is usually combined with dancing and singing. The role of the drum extends beyond the production of sounds or music for Indigenous communities. It also provides spiritual and social connections as well as healing. Drums differ based on the community in which they are from and they are made from the materials that are local to those communities.", "메티, 이누이트 공동체에서 드럼 연주는 보통 춤과 노래와 결합됩니다. 원주민 공동체에서 드럼의 역할은 소리나 음악의 생산을 넘어섭니다. 드럼은 영적, 사회적 연결과 치유도 제공합니다. 드럼은 출신 공동체에 따라 다르며, 해당 공동체 지역의 재료로 만들어집니다."),
    ('For example, the Inuit of Inuvialuit (meaning "the real people") are from the Western Arctic area, in the modern-day Northwest Territories, and are from one of the four Inuit regions in Canada.', '예를 들어, 이누비알루이트의 이누이트("진정한 사람들"이라는 뜻)는 현대의 노스웨스트 준주에 해당하는 서부 북극 지역 출신이며, 캐나다의 네 이누이트 지역 중 하나에 속합니다.'),
    ("In the following video, observe how members of the The Ulukhaktok Western Drummers and Dancers from Inuvialuit use drums made of caribou skin. The teachings and traditions around the drum also vary from community to community.", "다음 영상에서, 이누비알루이트의 울루크학톡 서부 드러머와 댄서 단원들이 순록 가죽으로 만든 드럼을 어떻게 사용하는지 관찰하세요. 드럼에 관한 가르침과 전통도 공동체마다 다릅니다."),
    ("The following video about drumming explains the significance of the drum to Ojibwe people and how it is made.", "다음 드럼 연주에 관한 영상은 오지브웨 사람들에게 드럼의 의미와 드럼이 어떻게 만들어지는지 설명합니다."),
    ("While exploring these videos, it is important to understand that Indigenous ways of knowing, being and doing are equally important to scientific ways. These two ways are not contradictory, rather they often overlap as Indigenous knowledge includes scientific knowledge and vice versa. It is important that Indigenous knowledge and scientific knowledge are both ways of understanding the world around us.", "이 영상들을 탐구할 때, 원주민의 앎, 존재, 행동의 방식이 과학적 방식만큼 중요하다는 것을 이해하는 것이 중요합니다. 이 두 방식은 모순되지 않으며, 원주민 지식이 과학적 지식을 포함하고 그 반대도 마찬가지이므로 종종 겹칩니다. 원주민 지식과 과학적 지식 모두 우리 주변 세계를 이해하는 방법이라는 것이 중요합니다."),
    ("Read", "읽기"),
    ("The following article Meet the Scientists Embracing Traditional Indigenous Knowledge by Jimmy Thomson in The Narwhal discusses the overlap between", "The Narwhal의 Jimmy Thomson이 작성한 다음 기사 Meet the Scientists Embracing Traditional Indigenous Knowledge는"),
    ('"Indigenous" and "western" science.', '"원주민" 과학과 "서양" 과학 사이의 겹침을 논의합니다.'),
    ("Now you have completed all of of the learning activities in this unit, use the following prompts to complete some independent research. Record your findings in your notebook.", "이 단원의 모든 학습 활동을 완료했으므로, 다음 지시를 사용하여 독립적인 연구를 완성하세요. 연구 결과를 노트에 기록하세요."),
    ("Choose a career you are interested in and that is related to the topics presented in this unit. Research the education and training necessary to pursue this career.", "이 단원에서 다룬 주제와 관련된 관심 있는 직업을 선택하세요. 이 직업을 추구하는 데 필요한 교육과 훈련을 조사하세요."),
    ("Choose a famous Canadian physicist in a field of physics related to the content of this unit. Prepare a short biography including the name of the physicist, when they made their contribution to physics knowledge, what they contributed, and how it benefited society.", "이 단원의 내용과 관련된 물리학 분야의 유명한 캐나다 물리학자를 선택하세요. 물리학자의 이름, 물리학 지식에 기여한 시기, 기여 내용, 그리고 사회에 어떤 이점을 주었는지를 포함하는 짧은 전기를 준비하세요."),
    ("Review the vocabulary related to resonance. Ensure that you have a good understanding of how to use these words to describe the physics involved.", "공명과 관련된 어휘를 복습하세요. 이 단어들을 사용하여 관련 물리학을 설명하는 방법을 잘 이해하고 있는지 확인하세요."),
    ("Learning Activity 1.5 Assignment", "학습 활동 1.5 과제"),
    ("When you are ready, go to the following page to learn more about 1.5 Assignment.", "준비가 되면, 다음 페이지로 이동하여 1.5 과제에 대해 자세히 알아보세요."),
    ("Transferable skills survey", "전이 가능한 기술 설문"),
    ("Having completed the unit, take the opportunity to review your demonstration of Ontario's Transferable Skills, introduced in 1.1. Complete the Unit 1 Transferable Skills Survey to share your assessment and specific evidence for that rating.", "단원을 완료했으므로, 1.1에서 소개된 온타리오 전이 가능한 기술의 시연을 검토할 기회를 가지세요. 단원 1 전이 가능한 기술 설문을 완성하여 평가와 그 평가에 대한 구체적인 근거를 공유하세요."),
    ("Press the Transferable Skills Survey button to access it.", "전이 가능한 기술 설문 버튼을 눌러 접근하세요."),

    # Self-check quiz
    ("Self-check quiz", "자기 점검 퀴즈"),
    ("Check your understanding!", "이해도를 확인하세요!"),
    ("Complete the following self-check quiz to determine where you are in your learning and what areas you need to focus on.", "다음 자기 점검 퀴즈를 풀어 현재 학습 위치와 집중해야 할 영역을 파악하세요."),
    ("This quiz is for feedback only, not part of your grade. You have unlimited attempts on this quiz. Take your time, do your best work, and reflect on any feedback provided.", "이 퀴즈는 피드백 전용이며 성적에 포함되지 않습니다. 이 퀴즈에 대한 시도 횟수는 무제한입니다. 충분한 시간을 가지고 최선을 다하며, 제공된 피드백을 되돌아보세요."),
    ("Press Quiz to access this tool.", "퀴즈 버튼을 눌러 도구에 접근하세요."),

    # Misc
    ("(recall that a unit of", "("),
    ("is equivalent to Hz.)", "의 단위가 Hz와 같다는 것을 기억하세요.)"),
    ("(We're asked for another frequency)", "(다른 진동수를 구해야 합니다)"),
    ("Then", "그러면"),
]

def translate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for eng, kor in REPLACEMENTS:
        content = content.replace(eng, kor)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Translated {filepath}")

if __name__ == '__main__':
    translate_file('course_content/lessons/sph3u_u1la5.html')
