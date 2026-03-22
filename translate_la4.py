#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate sph3u_u1la4.html from English to Korean."""

REPLACEMENTS = [
    # Title
    ("Learning activity 1.4: Interference of Waves", "학습 활동 1.4: 파동의 간섭"),

    # HTML lang
    ('<html lang="en">', '<html lang="ko">'),

    # Noscript
    ("<strong>Warning!</strong> To ensure the greatest educational experience, this learning activity\n                contians aspects that require Javascript to be enabled.", "<strong>주의!</strong> 최상의 학습 경험을 위해, 이 학습 활동은 Javascript가 활성화되어 있어야 합니다."),

    # Learning goals
    ("<h2>Learning goals</h2>", "<h2>학습 목표</h2>"),
    ("<p>We are learning to:</p>", "<p>학습 내용:</p>"),
    ("<li>understand how waves interact with each other through constructive and destructive interference, and\n                superposition</li>", "<li>보강 간섭과 상쇄 간섭, 그리고 중첩을 통해 파동이 서로 어떻게 상호작용하는지 이해한다</li>"),
    ("<li>demonstrate how beats are produced from two frequencies that interfere</li>", "<li>간섭하는 두 진동수로부터 맥놀이가 어떻게 생성되는지 보여준다</li>"),
    ("<li>use the beat frequency equation</li>", "<li>맥놀이 진동수 방정식을 사용한다</li>"),
    ("<li>create standing waves</li>", "<li>정상파를 만든다</li>"),
    ("<li>use equations including the variables time, wavelength, wave speed, node spacing and frequency to analyze\n                standing waves</li>", "<li>시간, 파장, 파동 속력, 마디 간격, 진동수 변수를 포함한 방정식을 사용하여 정상파를 분석한다</li>"),

    # Success criteria
    ("<h2>Success criteria</h2>", "<h2>성취 기준</h2>"),
    ("<p>I am able to:</p>", "<p>나는 다음을 할 수 있다:</p>"),
    ("<li>describe and depict the properties of waves as they interfere with each other\n            </li>", "<li>파동이 서로 간섭할 때의 성질을 설명하고 묘사할 수 있다\n            </li>"),
    ("<li>explain why standing waves occur</li>", "<li>정상파가 발생하는 이유를 설명할 수 있다</li>"),
    ("<li>calculate beat frequency</li>", "<li>맥놀이 진동수를 계산할 수 있다</li>"),
    ("<li>describe how sound may impact my life negatively</li>", "<li>소리가 일상에 부정적인 영향을 미칠 수 있는 방법을 설명할 수 있다</li>"),

    # Notebook - Vocabulary
    ("<h2 class=\"h3\">Notebook</h2>", "<h2 class=\"h3\">노트</h2>"),
    ("Vocabulary: Record the following vocabulary in your notebook. As you complete the\n                                learning\n                                activity fill in the definition and key\n                                terminology pertaining to the vocabulary.", "어휘: 다음 어휘를 노트에 기록하세요. 학습 활동을 완료하면서 어휘에 관련된 정의와 핵심 용어를 채워 넣으세요."),
    ("<li>constructive interference</li>", "<li>보강 간섭</li>"),
    ("<li>destructive interference</li>", "<li>상쇄 간섭</li>"),
    ("<li>superposition</li>", "<li>중첩</li>"),
    ("<li>nodes</li>", "<li>마디</li>"),
    ("<li>antinodes</li>", "<li>배</li>"),
    ("<li>loops</li>", "<li>루프</li>"),

    # Introduction
    ("<h2>Introduction</h2>", "<h2>도입</h2>"),
    ("Now that we know some of the characteristics of waves, let's consider what happens when two waves in the\n                        same medium interact. To do so, we'll start by simplifying the situation and considering just a single\n                        wavelength of each wave. We call these single wavelengths \"pulses.\"", "파동의 특성을 알았으니, 같은 매질에서 두 파동이 상호작용할 때 어떤 일이 일어나는지 살펴봅시다. 이를 위해 상황을 단순화하여 각 파동의 단일 파장만 고려해 보겠습니다. 이 단일 파장을 \"펄스\"라고 합니다."),
    (" Have you ever watched waves ripple out after dropping something in the water? What happens\n                        if you drop two objects close to each other? Do the waves from each object interact with\n                        each other? This is the question we will be investigating further in this learning activity.\n                    ", " 물에 무언가를 떨어뜨린 후 파동이 퍼져 나가는 것을 본 적이 있나요? 두 물체를 서로 가까이 떨어뜨리면 어떻게 될까요? 각 물체에서 나온 파동이 서로 상호작용할까요? 이것이 이 학습 활동에서 더 자세히 조사할 질문입니다.\n                    "),

    # Wave interference
    ("<h2>Wave interference</h2>", "<h2>파동의 간섭</h2>"),
    ("As you may have guessed, for the short period of time that the pulses spend passing through one another,\n                        they do interact, and this interaction is called interference.", "짐작했겠지만, 펄스가 서로를 통과하는 짧은 시간 동안 서로 상호작용하며, 이 상호작용을 간섭이라고 합니다."),

    # Explore this
    ("<h3>Explore this!</h3>", "<h3>탐구해 보세요!</h3>"),
    ("<p>The following video is a demonstration of two waves interfering.</p>", "<p>다음 영상은 두 파동이 간섭하는 모습을 보여줍니다.</p>"),
    ("Wave interference occurs when two or more waves interact at the same time in the same medium.\n                    ", "파동의 간섭은 두 개 이상의 파동이 같은 매질에서 동시에 상호작용할 때 발생합니다.\n                    "),

    # Definition callout
    ("<h3>Definition</h3>", "<h3>정의</h3>"),
    ("<b>Amplitude</b> is an important concept used in interference. Amplitude is the\n                                distance from the equilibrium line. When the wave is above the equilibrium line, it\n                                has a\n                                positive amplitude. When it is below the equilibrium line, it has a negative\n                                amplitude. ", "<b>진폭</b>은 간섭에서 사용되는 중요한 개념입니다. 진폭은 평형선으로부터의 거리입니다. 파동이 평형선 위에 있으면 양의 진폭을 가지고, 평형선 아래에 있으면 음의 진폭을 가집니다. "),

    # Constructive interference
    ("Now, let's study the two types of interference: constructive interference and destructive\n                        interference.", "이제 간섭의 두 가지 유형인 보강 간섭과 상쇄 간섭을 공부해 봅시다."),
    ("<h3 style=\"padding-top: 2%;\">Constructive interference</h3>", "<h3 style=\"padding-top: 2%;\">보강 간섭</h3>"),
    ("Constructive interference occurs when a crest interferes with a crest, or a trough interferes\n                        with a trough. In these cases, the two pulses will add together to form extra-large crests\n                        (called supercrests) or extra-large troughs (called supertroughs). The following two\n                        diagrams\n                        illustrate examples of constructive interference: the first with crests, and the second with\n                        troughs. ", "보강 간섭은 마루와 마루가 만나거나 골과 골이 만날 때 발생합니다. 이 경우, 두 펄스가 합쳐져서 매우 큰 마루(초마루)나 매우 큰 골(초골)을 형성합니다. 다음 두 그림은 보강 간섭의 예시를 보여줍니다: 첫 번째는 마루, 두 번째는 골의 경우입니다. "),
    ("Press here for a long description.", "상세 설명을 보려면 여기를 누르세요."),
    ("Both diagrams illustrate the two pulses before they meet, and then again during the time they\n                        interfere. At this point, the two pulses are superimposed on each other, just for an\n                        instant. Note that the amplitude of the supercrest/supertrough is the sum of the two\n                        amplitudes of the two smaller pulses. You can determine the superimposed amplitude by just\n                        adding the two amplitudes of the original pulses. Also notice that the two crests\n                        illustrated in the previous diagram just pass\n                        through each other and are unchanged afterwards and this is also the same case for the two\n                        troughs, as shown in the following diagram.", "두 그림 모두 펄스가 만나기 전과 간섭하는 동안의 모습을 보여줍니다. 이 시점에서 두 펄스는 순간적으로 서로 중첩됩니다. 초마루/초골의 진폭은 두 개의 작은 펄스의 진폭의 합이라는 점에 주목하세요. 원래 펄스의 두 진폭을 더하면 중첩된 진폭을 구할 수 있습니다. 또한 앞의 그림에서 두 마루는 서로를 통과한 후 변하지 않으며, 다음 그림에서 보듯이 두 골의 경우도 마찬가지입니다."),

    # Destructive interference
    ("<h3>Destructive interference</h3>", "<h3>상쇄 간섭</h3>"),
    ("<p>For destructive interference, things are very different.</p>", "<p>상쇄 간섭의 경우, 상황이 매우 다릅니다.</p>"),
    ("<p>The following video is a demonstration for destructive interference.</p>", "<p>다음 영상은 상쇄 간섭의 시연입니다.</p>"),
    ("In this case, a crest is superimposed on a trough. When the two meet during interference, the\n                        crest attempts to pull the particles in the medium up, while the trough attempts to pull\n                        them down. The two actions cancel each other out and the resultant wave has a lower\n                        amplitude than either pulse. The following diagram illustrates a crest and a trough with\n                        equal amplitudes\n                        interfering.", "이 경우 마루가 골 위에 중첩됩니다. 간섭 중에 두 개가 만나면, 마루는 매질의 입자를 위로 끌어당기려 하고 골은 아래로 끌어당기려 합니다. 두 작용이 서로 상쇄되어 결과 파동의 진폭은 어느 한쪽 펄스보다 작아집니다. 다음 그림은 같은 진폭을 가진 마루와 골이 간섭하는 모습을 보여줍니다."),
    ("Note that, in this case, you can observe two things that were not completely obvious in the\n                        constructive interference examples. This case clearly illustrates that the pulses do pass\n                        through\n                        each other and don't bounce off. During the interference, the amplitude is zero because the\n                        positive and negative amplitudes add up to zero, as shown in the following illustration.\n                    ", "이 경우 보강 간섭 예시에서 완전히 명확하지 않았던 두 가지를 관찰할 수 있습니다. 이 경우는 펄스가 서로를 통과하며 반사되지 않는다는 것을 분명히 보여줍니다. 간섭 중에 양의 진폭과 음의 진폭이 합쳐져 0이 되므로, 진폭은 0이 됩니다. 다음 그림에서 이를 확인할 수 있습니다.\n                    "),

    # Principle of superposition
    ("<h2>Principle of superposition</h2>", "<h2>중첩의 원리</h2>"),
    ("At any point in a medium, the resulting amplitude of two interfering waves is the algebraic\n                        sum of the individual displacements of each wave. ", "매질의 어느 지점에서든, 간섭하는 두 파동의 결과 진폭은 각 파동의 개별 변위의 대수적 합입니다. "),
    ("Examine the following diagram to help you understand the process better. To find the\n                        displacement of any particle in the medium, add the algebraic amplitudes for each individual\n                        wave. Keep in mind that displacements above the equilibrium (from crests) are positive and\n                        displacements below the equilibrium (from troughs) are negative.", "다음 그림을 살펴보면서 과정을 더 잘 이해해 보세요. 매질의 임의의 입자의 변위를 구하려면, 각 개별 파동의 대수적 진폭을 더하세요. 평형 위의 변위(마루에서)는 양수이고 평형 아래의 변위(골에서)는 음수라는 점을 기억하세요."),
    ("If you examine the rough work step, you can observe that on the left side of the\n                        superimposed waves, the displacement of the rectangular crest is positive, but the\n                        triangular trough has no displacement. This means that the resultant displacement will be\n                        positive and equal to the displacement of the rectangular crest. On the right end of\n                        the superimposed waves, the two displacements are equal in magnitude, but opposite in\n                        direction.", "과정을 살펴보면, 중첩된 파동의 왼쪽에서는 직사각형 마루의 변위가 양수이지만 삼각형 골의 변위는 없습니다. 이는 결과 변위가 양수이며 직사각형 마루의 변위와 같다는 것을 의미합니다. 중첩된 파동의 오른쪽 끝에서는 두 변위가 크기는 같지만 방향이 반대입니다."),
    ("At this point, they cancel each other and there is no displacement. In between\n                        the two ends, the positive displacement of the rectangular crest is always greater in\n                        magnitude than the negative displacement of the triangular trough. This results in a smaller\n                        positive displacement for each point in between the two ends. Afterwards, the pulses just\n                        pass through each other, unchanged.", "이 지점에서 서로 상쇄되어 변위가 없습니다. 두 끝 사이에서 직사각형 마루의 양의 변위는 항상 삼각형 골의 음의 변위보다 크기가 큽니다. 이로 인해 두 끝 사이의 각 점에서 더 작은 양의 변위가 생깁니다. 이후 펄스는 변하지 않고 서로를 통과합니다."),

    # Example: superposition
    ("<h3 style=\"padding-top: 2%;\">Example: Principle of superposition</h3>", "<h3 style=\"padding-top: 2%;\">예제: 중첩의 원리</h3>"),
    ("Using the superposition principle, determine the resultant displacement of the particles in\n                        the medium at the instant shown in following diagram. Compare your work with the suggested answer to check your understanding.", "중첩의 원리를 사용하여, 다음 그림에 표시된 순간의 매질 입자의 결과 변위를 구하세요. 풀이 예시와 비교하여 이해도를 확인하세요."),

    # Suggested Answer buttons
    (">Suggested\n                        Answer<", ">풀이 보기<"),
    (">Suggested\n                                Answer<", ">풀이 보기<"),
    (">Suggested\n                                                Answer<", ">풀이 보기<"),
    (">Suggested Answer<", ">풀이 보기<"),

    # Superposition answer
    ("You only need to be concerned about where the two pulses overlap or superimpose.\n                            When there is only one pulse in part of the medium, the pulse will be unchanged.\n                            For this example, they just superimpose in the middle, so adding the amplitudes\n                            gives the\n                            following result. Note that all you would observe is the solid line. The dotted\n                            lines\n                            would not be visible.", "두 펄스가 겹치거나 중첩되는 부분만 고려하면 됩니다. 매질의 일부에 하나의 펄스만 있을 때, 그 펄스는 변하지 않습니다. 이 예제에서는 가운데에서만 중첩되므로, 진폭을 더하면 다음과 같은 결과가 됩니다. 관찰할 수 있는 것은 실선뿐이며, 점선은 보이지 않습니다."),

    # Notebook callouts
    ("<h3>Notebook</h3>", "<h3>노트</h3>"),
    ("Use your notebook to complete the following question. Compare your work with\n                                the suggested answer to check your\n                                understanding.", "노트를 사용하여 다음 문제를 풀어 보세요. 풀이 예시와 비교하여 이해도를 확인하세요."),
    ("Using the superposition principle, determine the resultant displacement of the\n                                    particles in the medium when the\n                                    horizontal midpoints of the two pulses overlap, as shown in the following\n                                    diagram.", "중첩의 원리를 사용하여, 다음 그림에 표시된 것처럼 두 펄스의 수평 중간점이 겹칠 때 매질 입자의 결과 변위를 구하세요."),
    ("The resulting midpoint of the two pulses overlapping using the superposition\n                            principle would appear to be as shown in\n                            the following diagram.", "중첩의 원리를 사용하여 두 펄스가 겹치는 중간점의 결과는 다음 그림과 같습니다."),

    # Beats section
    ("<h2>Beats</h2>", "<h2>맥놀이</h2>"),
    ("When two nearly identical frequencies are sounded together, a strange thing happens. To\n                        examine what happens, you can take two identical tuning forks and place an elastic band\n                        around the tines of one of them. The elastic band will lower the frequency of the tuning\n                        fork slightly. When one tuning fork is sounded on its own, a person can hear a single\n                        frequency\n                        of constant sound. When the two are sounded together, a person can hear dramatic changes in\n                        the\n                        loudness of the sound at regular time intervals. Typically, the sound will be heard as a\n                        loud-soft-loud pattern. This pulsating pattern represents the constructive and destructive\n                        interference of the two tuning forks with the slightly different frequencies. ", "거의 동일한 두 진동수를 함께 울리면 이상한 일이 일어납니다. 무슨 일이 일어나는지 알아보기 위해, 동일한 두 소리굽쇠를 가져와 하나의 갈래에 고무줄을 감아 보세요. 고무줄은 소리굽쇠의 진동수를 약간 낮춥니다. 하나의 소리굽쇠만 울리면 일정한 소리의 단일 진동수를 들을 수 있습니다. 두 개를 함께 울리면, 규칙적인 시간 간격으로 소리의 세기가 극적으로 변하는 것을 들을 수 있습니다. 일반적으로 소리는 크게-작게-크게 패턴으로 들립니다. 이 맥동 패턴은 약간 다른 진동수를 가진 두 소리굽쇠의 보강 간섭과 상쇄 간섭을 나타냅니다. "),

    # Try it - beats
    ("<h3>Try it!</h3>", "<h3>직접 해 보세요!</h3>"),
    ("Let's simulate these phenomenons of constructive and destructive interference in the\n                                following interactive simulation.", "다음 대화형 시뮬레이션에서 보강 간섭과 상쇄 간섭의 현상을 시뮬레이션해 봅시다."),
    ("When playing a combination such as 440 Hz and 441 Hz in the simulation, you will hear something like,\n                                \"woo\u2014woo\u2014woo\u2014woo.\" The \"woos\"\n                                you hear\n                                are\n                                called beats. The three different frequency in the simulation are 440 Hz, 440.5 Hz\n                                and 441 Hz.", "시뮬레이션에서 440 Hz와 441 Hz의 조합을 재생하면 \"우\u2014우\u2014우\u2014우\"와 같은 소리를 듣게 됩니다. 들리는 \"우\" 소리를 맥놀이라고 합니다. 시뮬레이션의 세 가지 진동수는 440 Hz, 440.5 Hz, 441 Hz입니다."),
    ("Press here\n                            for an accessible version of Acoustic\n                            Beats.", "음향 맥놀이의 접근 가능한\n                            버전을 보려면 여기를 누르세요."),

    # Why beats
    ("<h4>Why do you hear beats?</h4>", "<h4>왜 맥놀이가 들리나요?</h4>"),
    ("These beats occur because the sound waves from the two sources are shifting in and out of\n                        phase (the waves are no longer in sync with each other). When they are in phase, the sounds\n                        get louder because they are interfering constructively and a person could hear the \"woo\"\n                        sound.\n                        When they are out of phase, the sound is very faint because they are interfering\n                        destructively.", "이 맥놀이는 두 음원의 음파가 위상이 맞았다가 어긋났다가 하기 때문에 발생합니다(파동이 더 이상 서로 동기화되지 않음). 위상이 맞을 때는 보강 간섭으로 소리가 커지며 \"우\" 소리를 들을 수 있습니다. 위상이 어긋나면 상쇄 간섭으로 소리가 매우 희미해집니다."),
    ("<h4>What is beat frequency?</h4>", "<h4>맥놀이 진동수란 무엇인가요?</h4>"),
    ("The number of beats heard per second (beat frequency) is equal to the difference in the\n                        frequency of the two sounds.", "초당 들리는 맥놀이의 수(맥놀이 진동수)는 두 소리의 진동수 차이와 같습니다."),
    ("<h4>Why are there beats?</h4>", "<h4>왜 맥놀이가 생기나요?</h4>"),
    ("The \"woos\" are called beats and the number of beats produced in a given amount of time is\n                        called the beat frequency. These beats occur because the sound waves from the two tuning\n                        forks are shifting in and out of phase. When they are in phase, the sounds get louder\n                        because they are interfering to form two beats over a short amount of time, as shown in the\n                        following diagram. To keep things\n                        simple, assume that the time is a little over one second.", "\"우\" 소리를 맥놀이라고 하며, 주어진 시간 동안 발생하는 맥놀이의 수를 맥놀이 진동수라고 합니다. 이 맥놀이는 두 소리굽쇠의 음파가 위상이 맞았다가 어긋났다가 하기 때문에 발생합니다. 위상이 맞으면 간섭으로 소리가 커지며, 다음 그림에서 보듯이 짧은 시간 동안 두 개의 맥놀이가 형성됩니다. 간단하게 하기 위해, 시간이 1초보다 약간 넘는다고 가정합니다."),
    ("<b>Note:</b> The frequencies used would not be high enough for a person to hear, but the\n                        diagram is\n                        provided just to help describe the concept of beat frequencies.", "<b>참고:</b> 사용된 진동수는 사람이 들을 수 있을 만큼 높지 않지만, 이 그림은 맥놀이 진동수의 개념을 설명하기 위해 제공됩니다."),
    ("<b>Note:</b> The diagram that the top sound source sends out eight compressions (C) and\n                        rarefactions (R) in one\n                        second. Its frequency is 8.0 Hz. The bottom sound source has a frequency of 5.5 Hz. The\n                        difference in frequencies is 2.5 Hz.", "<b>참고:</b> 그림에서 위쪽 음원은 1초 동안 8개의 밀(C)과 소(R)를 보냅니다. 그 진동수는 8.0 Hz입니다. 아래쪽 음원의 진동수는 5.5 Hz입니다. 진동수의 차이는 2.5 Hz입니다."),
    ("As the two sound waves move out, sometimes they interfere constructively to create a loud\n                        sound, sometimes destructively to create a soft sound, as shown in the diagram. In the one\n                        second interval used, the\n                        two waves create 2.5 beats.", "두 음파가 퍼져 나가면서, 그림에서 보듯이 때로는 보강 간섭으로 큰 소리를, 때로는 상쇄 간섭으로 작은 소리를 만듭니다. 사용된 1초 간격에서 두 파동은 2.5개의 맥놀이를 만듭니다."),

    # Beat frequency equation
    ("<h2>Beat frequency equation</h2>", "<h2>맥놀이 진동수 방정식</h2>"),
    ("<p>The following beat frequency equation is:</p>", "<p>맥놀이 진동수 방정식은 다음과 같습니다:</p>"),
    ("<h3>Formula</h3>", "<h3>공식</h3>"),
    ("<p>Where:</p>", "<p>여기서:</p>"),
    (" is the beat frequency", "는 맥놀이 진동수"),
    (" are the frequencies of the two tuning forks (or any\n                                other sources of sound).\n                            ", "는 두 소리굽쇠(또는 기타 음원)의 진동수입니다.\n                            "),
    ("The two vertical lines mean absolute value. They indicate that the beat frequency must be\n                        positive. If the difference between the two frequencies as illustrated were negative, you\n                        would\n                        just drop the minus sign and make it positive. To avoid this problem, you can always just\n                        subtract the lower frequency from the higher one.", "두 개의 수직선은 절댓값을 의미합니다. 맥놀이 진동수가 양수여야 함을 나타냅니다. 그림에서 보듯이 두 진동수의 차이가 음수이면, 음수 부호를 없애고 양수로 만들면 됩니다. 이 문제를 피하려면 항상 높은 진동수에서 낮은 진동수를 빼면 됩니다."),

    # Example: Frequency of tuning forks
    ("<h3>Example: Frequency of tuning forks</h3>", "<h3>예제: 소리굽쇠의 진동수</h3>"),
    ("Two tuning forks with slightly different frequencies are sounded together. One has a\n                        frequency of 256 Hz and the other has a frequency of 253 Hz. They are sounded together.", "약간 다른 진동수를 가진 두 소리굽쇠를 함께 울립니다. 하나는 256 Hz이고 다른 하나는 253 Hz입니다. 두 개를 함께 울립니다."),
    ("What is the beat frequency? When you are ready, press the <strong>Show Suggested Answer</strong> button to\n                            compare\n                            your thinking.", "맥놀이 진동수는 얼마인가요? 준비가 되면 <strong>풀이 보기</strong> 버튼을 눌러 자신의 생각과 비교하세요."),
    ("<strong>Show Suggested Answer</strong> button to compare your thinking.", "<strong>풀이 보기</strong> 버튼을 눌러 자신의 생각과 비교하세요."),

    # Example b
    ("The 256 Hz fork is removed and replaced with a new fork. Now when the two tuning forks are\n                            sounded together, you hear 10 beats in 5.0 s. What is the new frequency of the weighted\n                            fork? When you are ready, press the ", "256 Hz 소리굽쇠를 제거하고 새 소리굽쇠로 교체합니다. 이제 두 소리굽쇠를 함께 울리면, 5.0초 동안 10개의 맥놀이가 들립니다. 가중된 소리굽쇠의 새 진동수는 얼마인가요? 준비가 되면 "),
    ("10 beats in 5.0 s = 2 beats per second. Therefore, <em>f<sub>b</sub>\n                            </em> = 2 Hz. Therefore, the second tuning fork has to be 2 Hz different\n                            from the 253 Hz tuning fork. There are two possibilities, 255 Hz or 251 Hz.\n                            Both answers are valid and there is no way to eliminate one of them.\n                        ", "5.0초 동안 10개의 맥놀이 = 초당 2개의 맥놀이. 따라서 <em>f<sub>b</sub>\n                            </em> = 2 Hz. 따라서 두 번째 소리굽쇠는 253 Hz 소리굽쇠와 2 Hz 차이가 나야 합니다. 255 Hz 또는 251 Hz의 두 가지 가능성이 있습니다.\n                            두 답 모두 유효하며 하나를 제거할 방법은 없습니다.\n                        "),

    # Notebook - beat problems
    ("Try the following questions on your own in your notebook.", "노트에서 다음 문제를 스스로 풀어 보세요."),
    ("Tuning fork 1 (420.0 Hz) is sounded along with tuning fork 2 and exactly 20 beats are counted in\n                                    10.00 s. Tuning fork 2 is sounded along with tuning fork 3 (426.0 Hz) and exactly 12 beats are\n                                    detected in 3.00 s. What is the frequency of tuning fork 2? Explain your reasoning.", "소리굽쇠 1(420.0 Hz)을 소리굽쇠 2와 함께 울리면 10.00초 동안 정확히 20개의 맥놀이가 셉니다. 소리굽쇠 2를 소리굽쇠 3(426.0 Hz)과 함께 울리면 3.00초 동안 정확히 12개의 맥놀이가 감지됩니다. 소리굽쇠 2의 진동수는 얼마인가요? 이유를 설명하세요."),

    # Solution labels (common patterns)
    ("<p>Given:</p>", "<p>주어진 값:</p>"),
    ("<p style=\"padding-top: 1%;\">Unknown:</p>", "<p style=\"padding-top: 1%;\">구하는 값:</p>"),
    ("<p style=\"padding-top: 2%;\">Unknown:</p>", "<p style=\"padding-top: 2%;\">구하는 값:</p>"),
    ("<p style=\"padding-top: 1%;\">Equation:</p>", "<p style=\"padding-top: 1%;\">공식:</p>"),
    ("<p style=\"padding-top: 2%;\">Equation:</p>", "<p style=\"padding-top: 2%;\">공식:</p>"),
    ("<p style=\"padding-top: 1%;\">Solve:</p>", "<p style=\"padding-top: 1%;\">풀이:</p>"),
    ("<p style=\"padding-top: 2%;\">Solve:</p>", "<p style=\"padding-top: 2%;\">풀이:</p>"),
    ("<p style=\"padding-top: 1%;\">Statement:</p>", "<p style=\"padding-top: 1%;\">결론:</p>"),
    ("<p style=\"padding-top: 2%;\">Statement:</p>", "<p style=\"padding-top: 2%;\">결론:</p>"),

    # Solution - beat problem 1
    ("The beat frequency between forks 1 and 2 is 2.000 Hz, since ", "소리굽쇠 1과 2 사이의 맥놀이 진동수는 2.000 Hz입니다. "),
    ("The beat frequency between forks 2 and 3 is 4.00 Hz, since ", "소리굽쇠 2와 3 사이의 맥놀이 진동수는 4.00 Hz입니다. "),
    ("<p>The only option in common is 422 Hz, so ", "<p>공통된 유일한 선택지는 422 Hz이므로 "),
    ("<p>The frequency of tuning fork 2 is 422 Hz.</p>", "<p>소리굽쇠 2의 진동수는 422 Hz입니다.</p>"),

    # Beat problem 2
    ("Tuning fork 1 (256 Hz) is sounded along with tuning fork 2 (255 Hz). What is the\n                                    beat frequency?", "소리굽쇠 1(256 Hz)을 소리굽쇠 2(255 Hz)와 함께 울립니다. 맥놀이 진동수는 얼마인가요?"),
    ("(*Note that the absolute value symbol means we drop the negative if it is present.)", "(*참고: 절댓값 기호는 음수가 있으면 음수 부호를 제거한다는 의미입니다.)"),
    ("<p>The beat frequency is 1.00 Hz.</p>", "<p>맥놀이 진동수는 1.00 Hz입니다.</p>"),

    # Beat problem 3
    ("Elastic bands are attached to tuning fork 1 (which was 256 Hz) to reduce its\n                                    frequency. It is sounded again with tuning fork 2 (255 Hz), making exactly 12 beats in 6.00 s. What\n                                    is\n                                    the\n                                    new frequency of tuning fork 1? Explain your reasoning.", "소리굽쇠 1(원래 256 Hz)에 고무줄을 달아 진동수를 낮춥니다. 소리굽쇠 2(255 Hz)와 다시 울리면 6.00초 동안 정확히 12개의 맥놀이가 생깁니다. 소리굽쇠 1의 새 진동수는 얼마인가요? 이유를 설명하세요."),
    ("<p>The beat frequency given is in relation to the adjusted tuning fork.</p>", "<p>주어진 맥놀이 진동수는 조정된 소리굽쇠에 대한 것입니다.</p>"),
    ("We know that the new frequency was obtained by attaching elastic bands to fork 1. From earlier in\n                                    the\n                                    learning activity, we know \"The elastic band will lower the frequency of the tuning fork slightly.\"\n                                ", "소리굽쇠 1에 고무줄을 달아 새 진동수를 얻었다는 것을 알고 있습니다. 이전 학습 활동에서 \"고무줄은 소리굽쇠의 진동수를 약간 낮춥니다\"라는 것을 알았습니다.\n                                "),
    ("<p>Therefore, the new frequency must be lower than the original.</p>", "<p>따라서 새 진동수는 원래보다 낮아야 합니다.</p>"),
    ("The new frequency of tuning fork 1 is 253 Hz, since the new frequency must be lower than the old\n                                    frequency and the beat frequency tells us fork 1 and 2 are 2 Hz apart.\n                                ", "소리굽쇠 1의 새 진동수는 253 Hz입니다. 새 진동수는 원래 진동수보다 낮아야 하고, 맥놀이 진동수에 따르면 소리굽쇠 1과 2는 2 Hz 차이가 나기 때문입니다.\n                                "),

    # Wave on a string simulation
    ("Read the following instructions before trying the wave on a string stimulation:", "줄 위의 파동 시뮬레이션을 시도하기 전에 다음 지침을 읽으세요:"),
    ("In the top left corner choose oscillate, and in the top right corner, choose\n                                    fixed\n                                    end.", "왼쪽 상단에서 oscillate(진동)를 선택하고, 오른쪽 상단에서 fixed end(고정단)를 선택하세요."),
    ("Along the bottom, set frequency to 2.00 Hz.", "하단에서 진동수를 2.00 Hz로 설정하세요."),
    ("Set damping to none.", "감쇠를 없음으로 설정하세요."),
    ("Set tension to halfway between high and low.", "장력을 높음과 낮음의 중간으로 설정하세요."),
    ("It is easier to observe what is happening if you select slow motion. Start the\n                                following simulation and\n                                observe. Is the wave swinging up and down\n                                rather than\n                                travelling through the string?", "슬로우 모션을 선택하면 무슨 일이 일어나는지 관찰하기 더 쉽습니다. 다음 시뮬레이션을 시작하고 관찰하세요. 파동이 줄을 따라 이동하지 않고 위아래로 흔들리고 있나요?"),
    ("Press here\n                            for an accessible version of Wave On\n                            a\n                            String.", "줄 위의 파동의 접근 가능한\n                            버전을 보려면\n                            여기를\n                            누르세요."),

    # Standing Waves
    ("<h4>Standing Waves</h4>", "<h4>정상파</h4>"),
    ("Waves – especially sound and light waves – often travel very quickly, making them difficult\n                        to study. In this section, you will learn about a way to study waves so that the properties\n                        of a wave are much easier to observe. This method involves using two identical sources that\n                        send out waves in opposite directions. It is crucial that both waves have an identical\n                        wavelength and amplitude in order for this interference pattern to work. The wave pattern\n                        that is produced using this method is called a standing wave because it appears to have no\n                        wave motion, only particle motion.", "파동, 특히 음파와 빛의 파동은 매우 빠르게 이동하여 연구하기 어렵습니다. 이 절에서는 파동의 성질을 훨씬 쉽게 관찰할 수 있는 방법을 배우게 됩니다. 이 방법은 반대 방향으로 파동을 보내는 두 개의 동일한 파원을 사용합니다. 이 간섭 패턴이 작동하려면 두 파동의 파장과 진폭이 동일해야 합니다. 이 방법으로 만들어진 파동 패턴은 파동의 움직임이 없고 입자의 움직임만 있는 것처럼 보이기 때문에 정상파라고 합니다."),

    # Standing waves accessible version
    ("Press here for the accessible version of Standing Waves.", "정상파의 접근 가능한 버전을 보려면 여기를 누르세요."),

    # Standing wave description
    ("In the first graph of lines, two waves (shown in red and blue) move in opposite directions through\n                        the\n                        same medium. The subsequent graphs of lines show what happens as the red and blue\n                        waves move\n                        from point A to I (and vice versa).", "첫 번째 그래프에서 두 파동(빨간색과 파란색)이 같은 매질에서 반대 방향으로 이동합니다. 이어지는 그래프들은 빨간색과 파란색 파동이 A점에서 I점(또는 그 반대)으로 이동할 때 일어나는 일을 보여줍니다."),
    ("When two identical waves moving in opposite directions in a medium interfere, there are\n                        points in the medium that do not move at all. These points are called nodes. The points\n                        occur at positions in the medium where crests meet troughs.", "매질에서 반대 방향으로 이동하는 두 개의 동일한 파동이 간섭할 때, 매질에서 전혀 움직이지 않는 점들이 있습니다. 이 점들을 마디라고 합니다. 마디는 매질에서 마루와 골이 만나는 위치에 발생합니다."),
    ("As you learned earlier, the\n                        destructive interference for identical waves produces no displacement at all and the\n                        particle remains at rest. Midway between the nodal points, there are points called\n                        antinodes. These points occur at positions where troughs meet troughs, forming supertroughs,\n                        and where crests meet crests, forming supercrests. The resulting constructive interference\n                        produces displacements twice as large as the displacements of the source.", "앞에서 배웠듯이, 동일한 파동의 상쇄 간섭은 변위를 전혀 만들지 않으며 입자는 정지 상태를 유지합니다. 마디점들 사이의 중간에는 배라고 불리는 점들이 있습니다. 이 점들은 골과 골이 만나 초골을 형성하고, 마루와 마루가 만나 초마루를 형성하는 위치에 발생합니다. 결과적인 보강 간섭은 파원의 변위보다 두 배 큰 변위를 만듭니다."),
    ("If you observed a standing wave, you would notice that the nodes stay at rest, never moving,\n                        while all of the other points move back and forth, perpendicular to the wave motion. The\n                        antinodes would be located where the particles have the largest displacement.", "정상파를 관찰하면, 마디는 정지 상태를 유지하고 절대 움직이지 않으며, 다른 모든 점들은 파동의 운동에 수직으로 앞뒤로 움직이는 것을 알 수 있습니다. 배는 입자의 변위가 가장 큰 곳에 위치합니다."),

    # Standing wave simulation text
    ("<h3 class=\"margin-top-lg\">Standing wave simulation </h3>", "<h3 class=\"margin-top-lg\">정상파 시뮬레이션 </h3>"),
    ("When two identical waves moving in opposite directions in a medium interfere, there are points in the\n                        medium that do not move at all. These points are called nodes (N), as shown in the following diagram.\n                        Midway\n                        between the nodal points, there are points called antinodes, in the illustration. The following diagram of\n                        the standing wave has four nodes, six antinodes, and three loops.", "매질에서 반대 방향으로 이동하는 두 개의 동일한 파동이 간섭할 때, 매질에서 전혀 움직이지 않는 점들이 있습니다. 다음 그림에서 보듯이 이 점들을 마디(N)라고 합니다. 마디점들 사이의 중간에는 그림에서 보듯이 배라고 불리는 점들이 있습니다. 다음 정상파 그림에는 4개의 마디, 6개의 배, 3개의 루프가 있습니다."),
    ("One of the more useful properties of standing waves is the fact that the distance from one node to the\n                        next\n                        (one loop) is half a wavelength. Since these points don't move, it's very easy to measure the wavelength.\n                    ", "정상파의 더 유용한 성질 중 하나는 한 마디에서 다음 마디까지의 거리(하나의 루프)가 반파장이라는 사실입니다. 이 점들이 움직이지 않기 때문에 파장을 측정하기가 매우 쉽습니다.\n                    "),
    ("The width of one loop is half a wavelength, so the width of two loops will\n                        be one wavelength:", "하나의 루프 폭은 반파장이므로, 두 루프의 폭은 한 파장이 됩니다:"),

    # Example 1
    ("<h3>Example 1</h3>", "<h3>예제 1</h3>"),
    ("The distance between two successive (one right after the other) nodes in a standing wave is\n                        20.0 cm. The frequency of the source is 15 Hz. Find the speed of the waves. When you are ready, press the\n                        <strong>Show Suggested Answer</strong> button to compare your thinking.\n                    ", "정상파에서 연속된 두 마디 사이의 거리는 20.0 cm입니다. 파원의 진동수는 15 Hz입니다. 파동의 속력을 구하세요. 준비가 되면 <strong>풀이 보기</strong> 버튼을 눌러 자신의 생각과 비교하세요.\n                    "),
    ("The distance between two successive nodes is one loop. One loop is half a\n                            wavelength (", "연속된 두 마디 사이의 거리는 하나의 루프입니다. 하나의 루프는 반파장("),
    (". Now use the universal wave equation to find the speed:", "입니다. 이제 파동의 기본 방정식을 사용하여 속력을 구합니다:"),
    ("The speed of waves is ", "파동의 속력은 "),

    # Example 2
    ("<h3>Example 2</h3>", "<h3>예제 2</h3>"),
    ("A vibrating source makes a standing wave in a string as shown in the following diagram. The\n                        source moves up and down,\n                        completing 22 cycles in 5.5 s. The distance from the first node to the sixth node is 6.0 m.\n                        Find the speed of the waves. When you are ready, press the <strong>Show Suggested Answer</strong> button to compare\n                        your thinking.", "진동하는 파원이 다음 그림에 표시된 것처럼 줄에 정상파를 만듭니다. 파원은 위아래로 움직이며 5.5초 동안 22번의 진동을 완료합니다. 첫 번째 마디에서 여섯 번째 마디까지의 거리는 6.0 m입니다. 파동의 속력을 구하세요. 준비가 되면 <strong>풀이 보기</strong> 버튼을 눌러 자신의 생각과 비교하세요."),
    ("You can observe 5 loops between the first and sixth nodes. 5 loops = 2.5 λ =\n                            6.0 m", "첫 번째와 여섯 번째 마디 사이에 5개의 루프가 있습니다. 5 루프 = 2.5 λ = 6.0 m"),
    ("To find frequency, the equation is", "진동수를 구하기 위한 공식은"),
    ("where <em>N</em> = number of cycles and <em>t</em> = time.", "여기서 <em>N</em> = 진동 횟수이고 <em>t</em> = 시간입니다."),
    ("Now use the universal wave equation to find the speed of the waves.", "이제 파동의 기본 방정식을 사용하여 파동의 속력을 구합니다."),
    ("The wave speed is 9.6 m/s.", "파동의 속력은 9.6 m/s입니다."),

    # Notebook - standing wave problems
    ("Try these on your own in your notebook.", "노트에서 직접 풀어 보세요."),

    # Problem 1
    ("A source with a frequency of 30.0 Hz is used to make waves in a rope 12 m long. It\n                                    takes\n                                    0.20 s for the waves to travel from one fixed end of the rope to the other. What is\n                                    the speed\n                                    of the wave? What is the wavelength? How many loops are there in the standing wave\n                                    in the\n                                    rope?", "진동수 30.0 Hz의 파원으로 길이 12 m인 줄에 파동을 만듭니다. 파동이 줄의 한 고정단에서 다른 고정단까지 이동하는 데 0.20초가 걸립니다. 파동의 속력은 얼마인가요? 파장은 얼마인가요? 줄의 정상파에 루프가 몇 개 있나요?"),
    ("<p>There are three separate questions.</p>", "<p>세 가지 별도의 질문이 있습니다.</p>"),
    ("<p>First, find the speed of the wave using the length and time.</p>", "<p>먼저, 길이와 시간을 사용하여 파동의 속력을 구합니다.</p>"),
    ("<p>Then, find the wavelength using the universal wave equation.</p>", "<p>그런 다음, 파동의 기본 방정식을 사용하여 파장을 구합니다.</p>"),
    ("<p>Then note that one loop is half a wavelength in length.</p>", "<p>그런 다음 하나의 루프의 길이가 반파장이라는 점에 주목합니다.</p>"),
    ("The length of the rope is 12 m, and each loop is ", "줄의 길이는 12 m이고, 각 루프의 길이는 "),
    ("in length.", "입니다."),
    ("<p>So there are 12 loops.</p>", "<p>따라서 12개의 루프가 있습니다.</p>"),
    ("The speed of the wave is ", "파동의 속력은 "),
    (", the wavelength is 2.0 m, and there are 12 loops in the rope.\n                                ", "이고, 파장은 2.0 m이며, 줄에 12개의 루프가 있습니다.\n                                "),
    ("(Answers are given to 2 significant digits, since <em>d</em> has 2 significant digits. The speed\n                                    must\n                                    be expressed in scientific notation because \"60\" has only one significant digit, so it must be\n                                    written\n                                    as ", "(답은 유효 숫자 2자리로 나타냅니다. <em>d</em>가 유효 숫자 2자리이기 때문입니다. 속력은 \"60\"이 유효 숫자 1자리뿐이므로 과학적 표기법으로 나타내야 하며, "),
    ("to indicate that it has two significant digits.)", "로 써서 유효 숫자 2자리임을 나타냅니다.)"),

    # Problem 2
    ("Two waves travelling in opposite directions at 6.0 m/s produce nodes that are 0.40\n                                    m apart. What is the wavelength? Find the frequency of the waves.", "반대 방향으로 6.0 m/s로 이동하는 두 파동이 0.40 m 간격의 마디를 만듭니다. 파장은 얼마인가요? 파동의 진동수를 구하세요."),
    ("<p>First, find the wavelength.</p>", "<p>먼저, 파장을 구합니다.</p>"),
    ("The distance between nodes is the length of a single loop, and we know the length of a loop is half\n                                    a\n                                    wavelength.", "마디 사이의 거리는 하나의 루프 길이이며, 루프의 길이가 반파장이라는 것을 알고 있습니다."),
    ("Use the universal wave equation to find frequency.", "파동의 기본 방정식을 사용하여 진동수를 구합니다."),
    ("The wavelength is 0.80 m and the frequency is 7.5 Hz.\n                                ", "파장은 0.80 m이고 진동수는 7.5 Hz입니다.\n                                "),

    # Problem 3 (procedure)
    ("You tie the two opposite ends of a long rope to fixed positions. You have a source\n                                    that\n                                    can set up standing waves in the rope, a metre stick, and a stopwatch. Describe a\n                                    procedure\n                                    you could use to find the speed of the waves in the rope using the principles of\n                                    standing\n                                    waves.", "긴 줄의 양쪽 끝을 고정된 위치에 묶습니다. 줄에 정상파를 만들 수 있는 파원, 미터자, 스톱워치가 있습니다. 정상파의 원리를 사용하여 줄에서 파동의 속력을 구하는 절차를 설명하세요."),
    ("Since this is not a calculation question, it does not need to be expressed in the GUESS structure.\n                                ", "이것은 계산 문제가 아니므로 GUESS 구조로 표현할 필요가 없습니다.\n                                "),
    ("<p>First, activate the source to set up a standing wave.</p>", "<p>첫째, 파원을 작동시켜 정상파를 만듭니다.</p>"),
    ("<p>Second, measure the length between two adjacent nodes.</p>", "<p>둘째, 인접한 두 마디 사이의 길이를 측정합니다.</p>"),
    ("<p>Third, multiply that length by two to get the wavelength.</p>", "<p>셋째, 그 길이에 2를 곱하여 파장을 구합니다.</p>"),
    ("Fourth, use the stopwatch to measure how long it takes for the wave to complete five full cycles.\n                                ", "넷째, 스톱워치를 사용하여 파동이 5번의 완전한 진동을 완료하는 데 걸리는 시간을 측정합니다.\n                                "),
    ("<p>Fifth, Divide 5 (the number of cycles) by the time to get the frequency.</p>", "<p>다섯째, 5(진동 횟수)를 시간으로 나누어 진동수를 구합니다.</p>"),
    ("<p>Sixth, multiply the frequency by the wavelength. The result is the wave's speed.</p>", "<p>여섯째, 진동수에 파장을 곱합니다. 결과가 파동의 속력입니다.</p>"),

    # Sonic booms
    ("<h2>Sonic booms</h2>", "<h2>소닉 붐</h2>"),
    ("If an object is travelling at a speed that is less than the speed of sound, it is\n                            said to\n                            have subsonic speed. If it travels at a speed that is greater than the speed of\n                            sound, it\n                            has supersonic speed. To accomplish this feat, the object must first break through\n                            the sound\n                            barrier, which is a large increase in aerodynamic drag and vibration as a vehicle surpasses the speed of\n                            sound. Typically, jets are used to break the sound barrier, although some\n                            experimental\n                            cars have also accomplished this task. ", "물체가 음속보다 느린 속도로 이동하면 아음속이라고 합니다. 음속보다 빠른 속도로 이동하면 초음속입니다. 이를 달성하려면 물체가 먼저 음속 장벽을 돌파해야 하는데, 이는 차량이 음속을 초과할 때 공기 저항과 진동이 크게 증가하는 것입니다. 일반적으로 음속 장벽을 돌파하는 데 제트기가 사용되지만, 일부 실험용 자동차도 이 과업을 달성했습니다. "),

    # Sonic boom accordion
    (">How is a sonic boom\n                                        created?<", ">소닉 붐은 어떻게\n                                        만들어지나요?<"),
    ("As planes travel, they send out sound waves in all directions. When a plane\n                                        is travelling at the speed of sound, the sound waves in front of the jet are\n                                        travelling at the same speed as the plane itself. This causes the waves to\n                                        pile up in front of the jet and superimpose on each other. The waves add up\n                                        constructively to produce a sound wave of incredible amplitude and energy.\n                                        The air becomes very dense in front of the jet because the compression of\n                                        the air particles is so severe. The jet must exert extra thrust to break\n                                        through this dense air.", "비행기가 이동하면서 모든 방향으로 음파를 보냅니다. 비행기가 음속으로 이동하면, 제트기 앞의 음파는 비행기 자체와 같은 속도로 이동합니다. 이로 인해 파동이 제트기 앞에 쌓이고 서로 중첩됩니다. 파동이 보강적으로 합쳐져 엄청난 진폭과 에너지의 음파를 만듭니다. 공기 입자의 압축이 매우 심하기 때문에 제트기 앞의 공기가 매우 밀집됩니다. 제트기는 이 밀집된 공기를 돌파하기 위해 추가 추력을 가해야 합니다."),
    (" If the jet is not designed properly, these\n                                        tremendous forces and vibrations could rip it apart. At supersonic speeds, a\n                                        plane actually travels faster than its spherical wavefronts and leaves them\n                                        behind. These waves also interfere with each other constructively. The noise\n                                        from this constructive interference is called a sonic boom. At ground level,\n                                        a person can hear the sound as two large cracks that sound like thunder.\n                                    ", " 제트기가 제대로 설계되지 않으면, 이 엄청난 힘과 진동이 비행기를 찢어버릴 수 있습니다. 초음속에서 비행기는 실제로 구형 파면보다 빠르게 이동하여 파면을 뒤에 남깁니다. 이 파동들도 서로 보강적으로 간섭합니다. 이 보강 간섭에서 나오는 소음을 소닉 붐이라고 합니다. 지상에서 사람은 이 소리를 천둥과 같은 두 번의 큰 폭음으로 들을 수 있습니다.\n                                    "),

    (">What are the effects of sonic\n                                        booms?<", ">소닉 붐의 영향은\n                                        무엇인가요?<"),
    (" The noise is loud enough to startle people and scare away animals. If the\n                                        flight path were much nearer the ground, a sonic boom would be truly\n                                        terrifying, as it is so loud, as shown in the following diagrams. It would\n                                        actually shake sturdy rigid\n                                        structures, cause objects to tip over, and could even break windows. Some\n                                        scientists believe that the occasional random sonic boom won't have any\n                                        adverse effects on an ecosystem. But sonic booms that take place on a\n                                        regular basis\n                                        could permanently scare away wildlife and upset the balance of their\n                                        ecosystems. For this reason, there are severe restrictions on supersonic air\n                                        travel across the world.", " 소음은 사람들을 놀라게 하고 동물들을 겁주어 쫓아버릴 만큼 큽니다. 비행 경로가 지면에 훨씬 더 가까웠다면, 다음 그림에서 보듯이 소닉 붐은 매우 큰 소리로 정말 무서울 것입니다. 실제로 견고한 구조물을 흔들고, 물건을 넘어뜨리고, 심지어 창문을 깨뜨릴 수도 있습니다. 일부 과학자들은 가끔 발생하는 소닉 붐이 생태계에 부정적인 영향을 미치지 않을 것이라고 믿습니다. 그러나 정기적으로 발생하는 소닉 붐은 야생 동물을 영구적으로 겁주어 쫓아내고 생태계의 균형을 깨뜨릴 수 있습니다. 이러한 이유로 전 세계적으로 초음속 항공 여행에 대한 엄격한 제한이 있습니다."),

    # Consolidation
    ("<h2 class=\"h3\">Explore this!</h2>", "<h2 class=\"h3\">탐구해 보세요!</h2>"),
    ("Try answering the following questions based on the following animation:", "다음 애니메이션을 보고 다음 질문에 답해 보세요:"),
    ("Do waves bounce off each other when they meet or do they pass through each other?", "파동이 만날 때 서로 반사되나요, 아니면 서로를 통과하나요?"),
    ("The waves pass through each other. The second animation demonstrates this best as the top\n                            wave continues to the right after the waves interfere with each other.", "파동은 서로를 통과합니다. 두 번째 애니메이션이 이를 가장 잘 보여주는데, 파동이 서로 간섭한 후 위쪽 파동이 계속 오른쪽으로 이동합니다."),
    ("What happens to the shape of the wave when they are in the same space?", "파동이 같은 공간에 있을 때 파동의 모양은 어떻게 되나요?"),
    ("The shape of the wave changes but once they pass through each other the waves return to\n                            their original shape.", "파동의 모양이 변하지만, 서로를 통과하면 파동은 원래 모양으로 돌아갑니다."),

    # Review
    ("<h3>Review</h3>", "<h3>복습</h3>"),
    ("Refer back to the vocabulary list at the beginning of this learning activity. Verify your\n                                understanding of each word. Have a\n                                definition and related use of the word in a sentence for your learning activity.", "이 학습 활동의 처음에 있는 어휘 목록을 다시 참조하세요. 각 단어에 대한 이해를 확인하세요. 학습 활동을 위해 각 단어의 정의와 관련된 문장 사용법을 준비하세요."),

    # Self-check quiz
    ("<h3>Self-check quiz</h3>", "<h3>자기 점검 퀴즈</h3>"),
    ("<h4>Check your understanding!</h4>", "<h4>이해도를 확인하세요!</h4>"),
    ("Complete the following self-check quiz to determine where you are in your learning and\n                                what areas you need to focus on.", "다음 자기 점검 퀴즈를 풀어 현재 학습 위치와 집중해야 할 영역을 파악하세요."),
    ("This quiz is for feedback only, not part of your grade. You have unlimited attempts on\n                                this quiz. Take your time, do your best work, and reflect on any feedback provided.", "이 퀴즈는 피드백 전용이며 성적에 포함되지 않습니다. 이 퀴즈에 대한 시도 횟수는 무제한입니다. 충분한 시간을 가지고 최선을 다하며, 제공된 피드백을 되돌아보세요."),
    ("Press <strong>Quiz</strong> to access this tool.", "<strong>퀴즈</strong> 버튼을 눌러 도구에 접근하세요."),

    # So/or patterns
    ("<p>So ", "<p>따라서 "),
]


def translate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for eng, kor in REPLACEMENTS:
        content = content.replace(eng, kor)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    translate_file('course_content/lessons/sph3u_u1la4.html')
