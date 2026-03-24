#!/usr/bin/env python3
"""Translate SPH3U course HTML files from English to Korean.
Preserves HTML structure, MathML, CSS, JS. Only replaces visible text content."""

import re
import sys

# Ordered list of (English, Korean) replacements.
# Order matters - longer/more specific phrases first to avoid partial matches.
REPLACEMENTS = [
    # Title and headers
    ("Learning activity 1.1: Characteristics of Waves", "학습 활동 1.1: 파동의 특성"),

    # Learning goals section
    ("Learning goals", "학습 목표"),
    ("We are learning to:", "우리가 배울 내용:"),
    ("identify the variables that result in a change to a wave (fixed/floating end, dampening, vertical shake\n                conditions, and rope tension)",
     "파동의 변화를 일으키는 변수를 파악한다 (고정/자유 끝, 감쇠, 수직 흔들림 조건, 줄의 장력)"),
    ("identify the variables that result in a change to a wave (fixed/floating end, dampening, vertical shake conditions, and rope tension)",
     "파동의 변화를 일으키는 변수를 파악한다 (고정/자유 끝, 감쇠, 수직 흔들림 조건, 줄의 장력)"),
    ("identify the medium in which the wave is created and travels", "파동이 생성되고 전달되는 매질을 파악한다"),
    ("classify waves into mechanical (longitudinal, transverse), and electromagnetic", "파동을 역학적 파동(종파, 횡파)과 전자기파로 분류한다"),
    ("describe waves using the terms amplitude, period/wavelength, trough, crest, equilibrium", "진폭, 주기/파장, 골, 마루, 평형 등의 용어를 사용하여 파동을 설명한다"),
    ("quantify periodic motion using scientific notation", "과학적 표기법을 사용하여 주기적 운동을 정량화한다"),
    ("use significant digits in calculations", "계산에서 유효 숫자를 사용한다"),
    ("describe periodic motion using a pendulum", "진자를 사용하여 주기적 운동을 설명한다"),
    ("introduce and use the Universal Wave equation", "파동의 기본 방정식을 도입하고 활용한다"),

    # Success criteria
    ("Success criteria", "성취 기준"),
    ("I am able to:", "나는 다음을 할 수 있다:"),
    ("record sentences and paragraphs describing waves using appropriate vocabulary", "적절한 용어를 사용하여 파동을 설명하는 문장과 문단을 작성한다"),
    ("explain the concept of medium and how waves are affected by different medium or no medium at all for\n                electromagnetic waves",
     "매질의 개념과 파동이 서로 다른 매질 또는 매질이 없는 경우(전자기파)에 어떻게 영향을 받는지 설명한다"),
    ("explain the concept of medium and how waves are affected by different medium or no medium at all for electromagnetic waves",
     "매질의 개념과 파동이 서로 다른 매질 또는 매질이 없는 경우(전자기파)에 어떻게 영향을 받는지 설명한다"),
    ("distinguish between longitudinal and transverse waves in different media, and provide examples of both\n                types",
     "다양한 매질에서 종파와 횡파를 구별하고, 두 유형의 예를 제시한다"),
    ("distinguish between longitudinal and transverse waves in different media, and provide examples of both types",
     "다양한 매질에서 종파와 횡파를 구별하고, 두 유형의 예를 제시한다"),
    ("calculate both the period and frequency for periodic motion", "주기적 운동의 주기와 진동수를 모두 계산한다"),
    ("explain the relationship between the speed of sound in various media", "다양한 매질에서의 음속 관계를 설명한다"),
    ("explain the idea of scientific notation and significant digits", "과학적 표기법과 유효 숫자의 개념을 설명한다"),
    ("solve problems involving wavelength, frequency, and wave speed", "파장, 진동수, 파동의 속력과 관련된 문제를 풀 수 있다"),
    ("describe the reflection of waves for both fixed and free ends", "고정단과 자유단에서의 파동 반사를 설명한다"),

    # Noscript warning
    ("<strong>Warning!</strong> To ensure the greatest educational experience, this learning activity\n                contians\n                aspects that require Javascript to be enabled.",
     "<strong>경고!</strong> 최상의 학습 경험을 위해 이 학습 활동에는 Javascript가 활성화되어야 하는 요소가 포함되어 있습니다."),
    ("<strong>Warning!</strong> To ensure the greatest educational experience, this learning activity contians aspects that require Javascript to be enabled.",
     "<strong>경고!</strong> 최상의 학습 경험을 위해 이 학습 활동에는 Javascript가 활성화되어야 하는 요소가 포함되어 있습니다."),

    # Welcome section
    ("<h2>Welcome to our course</h2>", "<h2>코스에 오신 것을 환영합니다</h2>"),
    ("Welcome to the study of physics! What is physics? We will revisit that question throughout the\n                        course, including coming to an understanding of why it's important in everyday life. In this\n                        course you will analyze energy and matter, solve problems and communicate results, and in a\n                        culminating assignment apply what you've learned to demonstrate your laboratory and research\n                        skills. This course is divided into four units: Waves and Sound, Motion and Forces, Energy and\n                        Society, and Electricity and Magnetism. Each unit will investigate a way that matter and energy\n                        affect our lives.",
     "물리학 공부에 오신 것을 환영합니다! 물리학이란 무엇일까요? 이 질문은 코스 전반에 걸쳐 다시 다루게 될 것이며, 일상생활에서 물리학이 왜 중요한지 이해하게 될 것입니다. 이 코스에서 여러분은 에너지와 물질을 분석하고, 문제를 풀고 결과를 전달하며, 종합 과제에서 배운 것을 적용하여 실험 및 연구 능력을 보여줄 것입니다. 이 코스는 파동과 소리, 운동과 힘, 에너지와 사회, 전기와 자기의 네 단원으로 구성되어 있습니다. 각 단원에서는 물질과 에너지가 우리 삶에 미치는 영향을 탐구합니다."),

    ("<h2>Waves and sound</h2>", "<h2>파동과 소리</h2>"),
    ("In this first unit, you will investigate the properties of waves (and sound as a particular\n                        example), solve problems involving them, and research how they affect society and the\n                        environment. At the end of this unit, you will complete a set of problems related to waves and\n                        sound, and communicate your work to your Teacher Marker.",
     "이 첫 번째 단원에서 여러분은 파동의 성질(특히 소리를 예로 들어)을 탐구하고, 관련 문제를 풀며, 파동이 사회와 환경에 미치는 영향을 조사할 것입니다. 이 단원의 마지막에는 파동과 소리와 관련된 문제를 풀고 그 결과를 교사에게 제출합니다."),

    ("<h2>Scientific communication</h2>", "<h2>과학적 의사소통</h2>"),
    ('In this course, you will use a word processor to prepare and submit your assignments. Part of\n                        that work requires you to use an equation editor to produce professionally-formatted\n                        mathematical expressions. Refer to the "Start Here - Welcome to SPH3U" section of the course for\n                        more information.',
     '이 코스에서 여러분은 워드 프로세서를 사용하여 과제를 준비하고 제출하게 됩니다. 이 작업의 일부로 수식 편집기를 사용하여 전문적으로 서식이 지정된 수학 표현식을 작성해야 합니다. 자세한 내용은 코스의 "시작하기 - SPH3U에 오신 것을 환영합니다" 섹션을 참조하세요.'),

    ("You may need to search online for support in creating your desired expressions using the editor\n                        of your choice.",
     "원하는 수식을 작성하기 위해 선택한 편집기의 사용법을 온라인에서 검색해야 할 수 있습니다."),

    # Notebook vocabulary section
    ("<h2 class=\"h3\">Notebook</h2>", "<h2 class=\"h3\">노트</h2>"),
    ("<h3>Notebook</h3>", "<h3>노트</h3>"),
    ("Vocabulary: This is a list of terms related to characteristics of waves. Record the terms\n                                in your notebook under a title: Characteristics of waves. As you complete this learning\n                                activity, fill in the definition and any thoughts you have related to the vocabulary\n                                list.",
     "어휘: 다음은 파동의 특성과 관련된 용어 목록입니다. 노트에 '파동의 특성'이라는 제목 아래 이 용어들을 기록하세요. 이 학습 활동을 완료하면서 각 용어의 정의와 관련된 생각을 채워 넣으세요."),

    # Vocabulary terms
    ("<li>wave</li>", "<li>파동(wave)</li>"),
    ("<li>oscillate</li>", "<li>진동하다(oscillate)</li>"),
    ("<li>vibrate</li>", "<li>떨다(vibrate)</li>"),
    ("<li>medium</li>", "<li>매질(medium)</li>"),
    ("<li>pulse</li>", "<li>펄스(pulse)</li>"),
    ("<li>mechanical wave</li>", "<li>역학적 파동(mechanical wave)</li>"),
    ("<li>electromagnetic wave</li>", "<li>전자기파(electromagnetic wave)</li>"),
    ("<li>transverse wave</li>", "<li>횡파(transverse wave)</li>"),
    ("<li>wavelength</li>", "<li>파장(wavelength)</li>"),
    ("<li>longitudinal wave</li>", "<li>종파(longitudinal wave)</li>"),
    ("<li>crest</li>", "<li>마루(crest)</li>"),
    ("<li>trough</li>", "<li>골(trough)</li>"),
    ("<li>cycle</li>", "<li>주기(cycle)</li>"),
    ("<li>periodic</li>", "<li>주기적(periodic)</li>"),
    ("<li>compressions</li>", "<li>밀(compression)</li>"),
    ("<li>rarefactions</li>", "<li>소(rarefaction)</li>"),

    # Types of waves
    ("<h2>Types of waves</h2>", "<h2>파동의 종류</h2>"),
    ("<p>Explore the following pictures:</p>", "<p>다음 사진들을 살펴보세요:</p>"),

    # Carousel captions
    ("<div class=\"carousel-caption\">Sea waves</div>", "<div class=\"carousel-caption\">바다 파도</div>"),
    ("<div class=\"carousel-caption\">An old oscilloscope screen displaying sine waves</div>", "<div class=\"carousel-caption\">사인파를 표시하는 오래된 오실로스코프 화면</div>"),
    ("<div class=\"carousel-caption\">When strummed, the strings of a guitar form waves.</div>", "<div class=\"carousel-caption\">기타 줄을 튕기면 파동이 형성됩니다.</div>"),
    ("Abstract background of glowing particles flowing in a\n                                    wave\n                                    pattern", "파동 패턴으로 흐르는 빛나는 입자들의 추상적 배경"),
    ("<div class=\"carousel-caption\">Splashing ocean waves</div>", "<div class=\"carousel-caption\">부서지는 바다 파도</div>"),

    # Wave descriptions
    ("As you can notice in the previous pictures, there are many different types of waves.\n                        Sometimes waves\n                        are\n                        useful, like water waves when we want to surf, but sometimes they can be destructive, like\n                        tsunami waves. Sound waves can help you learn about the environment around you, or give you\n                        enjoyment through music, but they can also be destructive when they cause noise pollution or\n                        when the sound is so intense that it injures your ear drum.",
     "앞의 사진에서 볼 수 있듯이 파동에는 다양한 종류가 있습니다. 서핑을 할 때의 물결처럼 유용한 경우도 있지만, 쓰나미처럼 파괴적인 경우도 있습니다. 음파는 주변 환경에 대해 알려주거나 음악을 통해 즐거움을 줄 수 있지만, 소음 공해를 일으키거나 소리가 너무 강해서 고막을 다치게 할 때는 파괴적일 수 있습니다."),

    # Think section
    ("<h3>Think</h3>", "<h3>생각해 보기</h3>"),
    ("Think of some examples of different waves. When you are ready, press the Show Suggested Answer button to read about some of the more common examples.",
     "다양한 파동의 예를 생각해 보세요. 준비가 되면 '예시 답안 보기' 버튼을 눌러 일반적인 예시들을 확인하세요."),
    ("Water waves, waves on a rope, sound waves, light waves, radio waves, X-rays, microwaves,\n                            and\n                            many\n                            more.",
     "수면파, 줄의 파동, 음파, 빛(가시광선), 전파, X선, 마이크로파 등 다양한 파동이 있습니다."),

    # Suggested Answer buttons
    (">Suggested\n                        Answer<", ">예시 답안<"),
    (">Suggested\n                        answer<", ">예시 답안<"),
    (">Suggested Answer<", ">예시 답안<"),
    (">Suggested answer<", ">예시 답안<"),

    # Investigate section
    ("<h2>Investigate: Wave on a string</h2>", "<h2>탐구: 줄 위의 파동</h2>"),
    ("<h3>Activity</h3>", "<h3>활동</h3>"),
    ("Now that you have considered various types of waves, let's try to understand how a wave is\n                        made. In other words, we will try to answer the question: What is a wave?",
     "다양한 종류의 파동을 살펴보았으니, 이제 파동이 어떻게 만들어지는지 이해해 봅시다. 즉, '파동이란 무엇인가?'라는 질문에 답해 보겠습니다."),
    ("Try the following simulation. You will explore how to make a wave. With the initial settings,\n                        try\n                        moving the wrench up and down (press and drag) to create waves.",
     "다음 시뮬레이션을 해 보세요. 파동을 만드는 방법을 탐구하게 됩니다. 초기 설정에서 렌치를 위아래로 움직여(누르고 끌어서) 파동을 만들어 보세요."),
    ("Press here\n                            for an accessible version of Wave On a String.", "여기를 눌러 '줄 위의 파동' 접근성 버전을 확인하세요."),
    ('Press here\n                            for an accessible version of "Properties of waves."', '여기를 눌러 "파동의 성질" 접근성 버전을 확인하세요.'),
    ("Press here\n                            for an accessible version of Wave Creation.", "여기를 눌러 '파동 생성' 접근성 버전을 확인하세요."),

    # Start button
    ("\n                        Start ", "\n                        시작 "),

    # Notebook prompts
    ("In your notebook, respond to the following prompts. Once you are done, compare your ideas\n                                to the suggested answers.",
     "노트에 다음 질문에 대한 답을 작성하세요. 완료하면 예시 답안과 비교해 보세요."),
    ("<li>Describe the simulation.</li>", "<li>시뮬레이션을 설명하세요.</li>"),
    ("<li>What caused the wave?</li>", "<li>파동의 원인은 무엇인가요?</li>"),
    ("<li>Explore the settings available in the simulation. What effect do they have?</li>", "<li>시뮬레이션에서 사용할 수 있는 설정을 탐색하세요. 어떤 효과가 있나요?</li>"),

    # Suggested answers for simulation
    ("A set of waves is created in the string. The waves stop eventually. They reflect\n                                        back to their source from the other end as well.",
     "줄에 일련의 파동이 생성됩니다. 파동은 결국 멈추며, 다른 쪽 끝에서 반사되어 원래 위치로 돌아옵니다."),
    ("I moved the wrench, which dragged the end of the string and caused the wave.",
     "렌치를 움직여 줄의 끝을 잡아당기면서 파동이 발생했습니다."),
    ("When I set damping to None, the wave kept going back and forth for a long time.\n                                        When I set it to Lots, it very quickly stopped moving. When I changed the\n                                        Tension, the speed of the wave changed.",
     "감쇠를 '없음'으로 설정하면 파동이 오랫동안 왕복했습니다. '최대'로 설정하면 매우 빠르게 멈췄습니다. 장력을 변경하면 파동의 속력이 변했습니다."),

    # About suggested answers
    ("Press the following button to learn more about the suggested answers in this course.",
     "이 코스의 예시 답안에 대해 더 알아보려면 다음 버튼을 누르세요."),
    ("Throughout this course you'll encounter Suggested Answer buttons like these. A\n                            suggested answer is just that &mdash; a suggestion. If you came up with a different\n                            answer, compare it carefully and thoughtfully to the suggested answer. How\n                            different is it? Does it still show all of the expected knowledge? If so, you're\n                            succeeding and can proceed. If it's still different, take a moment to think\n                            about the problem again. What other information can you gather?",
     "이 코스 전반에 걸쳐 이러한 예시 답안 버튼을 만나게 될 것입니다. 예시 답안은 말 그대로 하나의 예시일 뿐입니다. 다른 답을 생각해냈다면 예시 답안과 신중하게 비교해 보세요. 얼마나 다른가요? 기대되는 지식을 모두 포함하고 있나요? 그렇다면 잘 하고 있는 것이므로 계속 진행하세요. 여전히 다르다면 잠시 문제를 다시 생각해 보세요. 어떤 추가 정보를 얻을 수 있을까요?"),

    # What is a wave
    ("<h2>What is a wave?</h2>", "<h2>파동이란 무엇인가?</h2>"),
    ('In the simulation, the wave travelled through the string, and made the individual dots move up\n                        and down. In general, all waves have similar behaviour: They move through a medium (like our\n                        string) and make particles move back and forth. Another way of saying this is that the particles\n                        "oscillate" or "vibrate."',
     '시뮬레이션에서 파동은 줄을 통해 이동하면서 개별 점들을 위아래로 움직이게 했습니다. 일반적으로 모든 파동은 유사한 행동을 보입니다: 매질(예: 줄)을 통해 이동하면서 입자들을 앞뒤로 움직이게 합니다. 다른 말로, 입자들이 "진동"한다고 합니다.'),
    ("A wave, then, is a disturbance that transfers energy from particle to particle along a\n                        medium.",
     "따라서 파동이란 매질을 따라 입자에서 입자로 에너지를 전달하는 교란입니다."),
    ("A wave is created by a vibration or oscillation of the medium. Recall the simulation: in\n                        order to create the wave or pulse (single wave) one end of the string had to be moved up and\n                        down. Explore the following examples of waves. Think about what the medium is, and how the\n                        individual particles in the wave move.",
     "파동은 매질의 진동에 의해 생성됩니다. 시뮬레이션을 떠올려 보세요: 파동이나 펄스(단일 파동)를 만들기 위해 줄의 한쪽 끝을 위아래로 움직여야 했습니다. 다음 파동의 예를 살펴보세요. 매질이 무엇인지, 파동 속 개별 입자들이 어떻게 움직이는지 생각해 보세요."),

    ("<h3>Examples of waves</h3>", "<h3>파동의 예</h3>"),
    ("Water wave: Disturbance that transfers through water particles. The medium of the wave is\n                            water\n                            particles. The water particles oscillate or vibrate as the wave passes through them as\n                            shown in the previous image of water waves.",
     "수면파: 물 입자를 통해 전달되는 교란입니다. 이 파동의 매질은 물 입자입니다. 수면파의 이전 이미지에서 보듯이, 파동이 지나갈 때 물 입자는 진동합니다."),
    ("Sound wave: Disturbance that transfers sound energy through air particles. The medium of\n                            the\n                            sound wave is air particles. The air particles oscillate or vibrate as the sound wave\n                            passes\n                            through them. As represented in the image of the sound waves.",
     "음파: 공기 입자를 통해 소리 에너지를 전달하는 교란입니다. 음파의 매질은 공기 입자입니다. 음파의 이미지에서 보듯이, 음파가 지나갈 때 공기 입자는 진동합니다."),

    # Explore this
    ("<h3>Explore this!</h3>", "<h3>탐구해 보기!</h3>"),
    ("Explore the following video of an individual shaking battle ropes in a gym.",
     "체육관에서 배틀 로프를 흔드는 사람의 다음 동영상을 살펴보세요."),
    ("Can you identify the medium in the video?", "동영상에서 매질을 찾을 수 있나요?"),
    ("<p>Rope.</p>", "<p>줄(로프)입니다.</p>"),

    # Mechanical waves
    ("In these examples, there was always a medium through which the wave transferred energy. This\n                        behaviour makes them all a type of wave known as mechanical waves. In this learning activity, we\n                        will analyze some of the characteristics that mechanical waves share.",
     "이 예시들에서 파동이 에너지를 전달하는 매질이 항상 존재했습니다. 이러한 특성 때문에 이 파동들은 모두 역학적 파동이라고 합니다. 이 학습 활동에서는 역학적 파동이 공유하는 특성 중 일부를 분석하겠습니다."),
    ("Acknowledgements", "출처"),

    # Action section - Classifying waves
    ("<h2>Classifying waves</h2>", "<h2>파동의 분류</h2>"),
    ("Mechanical waves require a medium. There is another type of wave, in addition to mechanical\n                        waves: electromagnetic waves. Electromagnetic waves do not\n                        require a\n                        medium to travel, and can even travel in a vacuum like in outer space. In your physics\n                        studies,\n                        you will find that concepts are simplified at first, and then expanded upon.",
     "역학적 파동은 매질이 필요합니다. 역학적 파동 외에 또 다른 유형의 파동인 전자기파가 있습니다. 전자기파는 전달을 위해 매질이 필요하지 않으며, 우주 공간의 진공에서도 전파될 수 있습니다. 물리학 공부에서 개념은 처음에 단순화되었다가 점차 확장됩니다."),
    ("In this learning activity, you will study two types of mechanical waves, longitudinal and\n                        transverse, and\n                        you will learn how to recognize them. Note that in this course, you will only be learning about\n                        mechanical\n                        waves. If you want to learn all about electromagnetic waves, you'll have to take Grade 12 Physics!",
     "이 학습 활동에서는 두 가지 유형의 역학적 파동인 종파와 횡파를 공부하고 이를 구별하는 방법을 배웁니다. 이 코스에서는 역학적 파동만 학습한다는 점에 유의하세요. 전자기파에 대해 모두 배우려면 12학년 물리학을 수강해야 합니다!"),

    # Press here for long description
    ("Press here for a long\n                                    description.", "여기를 눌러 상세 설명을 확인하세요."),
    ("Press here for a long description.", "여기를 눌러 상세 설명을 확인하세요."),

    # Transverse waves
    ("<h3>Transverse waves</h3>", "<h3>횡파</h3>"),
    ("In a transverse wave, the motion of the particles and the direction of travel of the energy\n                        are\n                        at right angles (perpendicular) to each other. Only the energy moves across; the particles\n                        remain at their location as they transfer energy from one to the next.",
     "횡파에서 입자의 운동 방향과 에너지의 전달 방향은 서로 직각(수직)입니다. 에너지만 이동하며, 입자들은 에너지를 하나에서 다음으로 전달하면서 자신의 위치에 남아 있습니다."),
    ("Explore the following video to understand the behaviour of a transverse wave:",
     "다음 동영상을 통해 횡파의 거동을 이해해 보세요:"),
    ("As you observed, the particles move up and down, but the wave is travelling from left to right,\n                        so\n                        the energy is moving perpendicular to the motion of the particles.",
     "관찰한 바와 같이, 입자는 위아래로 움직이지만 파동은 왼쪽에서 오른쪽으로 이동하므로 에너지는 입자의 운동 방향에 수직으로 이동합니다."),
    ("This figure shows the creation of a transverse wave as the end of a rope is moved\n                        through one complete up-and-down cycle, or vibration. Notice that, after completing one\n                        cycle,\n                        the energy has reached only point E on the rope. The distance the wave has travelled after\n                        the\n                        source has made one vibration is called a wavelength. This is given the symbol λ (the Greek\n                        letter lambda).",
     "이 그림은 줄의 끝이 한 번의 완전한 위아래 주기(진동)를 거치면서 횡파가 생성되는 과정을 보여줍니다. 한 주기를 완료한 후 에너지는 줄의 E 지점까지만 도달했습니다. 파원이 한 번 진동한 후 파동이 이동한 거리를 파장이라고 하며, 기호 λ(그리스 문자 람다)로 나타냅니다."),
    ("<p class=\"caption\" style=\"text-align: center;\">Creation of transverse waves</p>", "<p class=\"caption\" style=\"text-align: center;\">횡파의 생성</p>"),
    ("As illustrated in the following figure, the high section of the wave is called a crest and\n                        the low\n                        section is called a trough. The crest is also called a positive pulse because the amplitude,\n                        A,\n                        (one half of the vertical distance between crests and troughs) is above the rest position.\n                        Troughs are also called negative pulses because their amplitude is below the rest position.",
     "다음 그림에서 보듯이, 파동의 높은 부분을 마루라 하고 낮은 부분을 골이라 합니다. 마루는 진폭 A(마루와 골 사이 수직 거리의 절반)가 평형 위치 위에 있으므로 양의 펄스라고도 합니다. 골은 진폭이 평형 위치 아래에 있으므로 음의 펄스라고도 합니다."),
    ("<p class=\"caption\" style=\"text-align: center;\">Transverse wave with crest and trough labelled.</p>",
     "<p class=\"caption\" style=\"text-align: center;\">마루와 골이 표시된 횡파</p>"),
    ("If a periodic vibration is used to produce a transverse wave in a rope, then a series of\n                        crests\n                        and troughs will be visible in the rope at one time. To produce this type of wave motion,\n                        your\n                        hand would have to move with a constant frequency up and down, as shown in the following\n                        figure.\n                        All the crests and troughs would have equal amplitudes and lengths. Notice that the pattern\n                        of\n                        the waves is repetitive.",
     "주기적인 진동을 이용하여 줄에 횡파를 만들면, 줄에 일련의 마루와 골이 동시에 보이게 됩니다. 이런 파동을 만들려면 다음 그림처럼 손을 일정한 진동수로 위아래로 움직여야 합니다. 모든 마루와 골은 동일한 진폭과 길이를 가집니다. 파동의 패턴이 반복적인 것에 주목하세요."),
    ("The wavelength (the distance across one crest and one trough) remains constant if the period\n                        remains constant. It is usually measured in metres, but there are situations where another\n                        length measurement is used. Since the wave has a repeating pattern of crests and troughs, there\n                        are multiple ways to measure the wavelength. In this diagram, four different spaces, each\n                        identical in length, are indicated with the Greek letter lambda (&lambda;).",
     "주기가 일정하면 파장(마루 하나와 골 하나에 걸친 거리)도 일정합니다. 파장은 보통 미터 단위로 측정하지만, 다른 길이 단위가 사용되는 경우도 있습니다. 파동은 마루와 골의 반복 패턴을 가지므로 파장을 측정하는 방법이 여러 가지 있습니다. 이 그림에서 동일한 길이의 네 구간이 그리스 문자 람다(λ)로 표시되어 있습니다."),
    ("<p style=\"text-align: center;\" class=\"caption \">Transverse waves with wavelength indicated.</p>",
     "<p style=\"text-align: center;\" class=\"caption \">파장이 표시된 횡파</p>"),

    # Longitudinal waves
    ("<h3>Longitudinal waves</h3>", "<h3>종파</h3>"),
    ("When the particles in the medium vibrate parallel to the direction of wave motion, the wave\n                        is\n                        called a longitudinal wave.",
     "매질 속 입자가 파동의 진행 방향과 평행하게 진동할 때, 이 파동을 종파라고 합니다."),
    ("Explore the following video to understand the behaviour of a longitudinal wave:",
     "다음 동영상을 통해 종파의 거동을 이해해 보세요:"),
    ("The most common longitudinal waves are sound waves. You will learn more about sound waves\n                        later\n                        in this unit.",
     "가장 흔한 종파는 음파입니다. 이 단원의 뒷부분에서 음파에 대해 더 배우게 됩니다."),
    ('One way to visualize longitudinal sound waves is to use a "slinky" spring, as shown in the\n                        following animation.',
     '종파인 음파를 시각화하는 한 가지 방법은 다음 애니메이션에서 보듯이 "슬링키" 용수철을 사용하는 것입니다.'),
    ("To produce a longitudinal wave in a slinky, arrange it in a straight line on the floor or\n                        some\n                        other horizontal surface. Tie one end to a fixed position and hold the other end in your\n                        hand.\n                        With the slinky stretched out to a reasonable length, you can move the end you are holding\n                        towards the slinky and then back again, parallel to the length of the slinky. Let's explore\n                        more\n                        about longitudinal waves.",
     "슬링키에서 종파를 만들려면 바닥이나 다른 수평면 위에 일직선으로 놓으세요. 한쪽 끝을 고정된 위치에 묶고 다른 쪽 끝을 손으로 잡으세요. 슬링키를 적당한 길이로 늘린 상태에서 잡고 있는 쪽 끝을 슬링키 방향으로 밀었다가 다시 당기세요(슬링키의 길이 방향과 평행하게). 종파에 대해 더 알아봅시다."),
    ("This periodic motion will produce compressions in the slinky when you are pushing towards it.\n                        In\n                        this case, the slinky's coils will get bunched closer together. You will produce\n                        rarefactions\n                        when your hand moves away from the slinky. In this case, the coils of the slinky will spread\n                        farther apart as shown in the following diagram.",
     "이 주기적 운동은 슬링키를 향해 밀 때 밀(압축)을 만듭니다. 이 경우 슬링키의 코일이 더 가까이 모입니다. 손이 슬링키에서 멀어질 때는 소(희박)가 만들어집니다. 이 경우 다음 그림처럼 슬링키의 코일이 더 멀리 퍼집니다."),
    ("These compressions and rarefactions will move along the length of the slinky, parallel to the\n                        direction of wave motion. In general, a compression occurs when the particles of the medium\n                        in a\n                        longitudinal wave are closer together than normal, and a rarefaction is when the particles\n                        are\n                        farther apart than normal.",
     "이러한 밀과 소는 파동의 진행 방향과 평행하게 슬링키의 길이를 따라 이동합니다. 일반적으로 밀은 종파에서 매질의 입자가 정상보다 가까이 모일 때 발생하고, 소는 입자가 정상보다 멀리 퍼질 때 발생합니다."),
    ("If you tie a ribbon to the slinky, you will observe the ribbon moves back and forth, parallel to\n                        the wave\n                        motion, as shown. For a longitudinal wave, a wavelength is measured from the centres of two\n                        successive\n                        compressions or rarefactions, as shown in the following diagram. As with transverse waves, the\n                        maximum\n                        displacement of the particles from the rest position is the amplitude. In one cycle, these\n                        particles will\n                        move a distance of four times the amplitude.",
     "슬링키에 리본을 묶으면 그림처럼 리본이 파동의 진행 방향과 평행하게 앞뒤로 움직이는 것을 관찰할 수 있습니다. 종파의 파장은 다음 그림처럼 연속된 두 밀 또는 두 소의 중심 사이 거리로 측정합니다. 횡파와 마찬가지로 평형 위치로부터 입자의 최대 변위가 진폭입니다. 한 주기 동안 이 입자들은 진폭의 네 배 거리를 이동합니다."),

    # Ideal vs real waves
    ("<h2>Ideal versus real waves</h2>", "<h2>이상적인 파동과 실제 파동</h2>"),
    ("The previous discussion of waves represents the ideal case. In physics, we often have to consider\n                        the ideal case of behaviour, since the real world is very complicated. We call these ideal\n                        waves. However, real waves, such as those in ropes, must pass\n                        through\n                        the air or rub against a surface, as they move. In such cases, friction often reduces the\n                        amplitude of the wave as it moves through the medium. You will also observe that the\n                        amplitude of\n                        the wave gradually decreases as it moves through the medium, but the wavelength does not\n                        change.",
     "앞의 파동에 대한 논의는 이상적인 경우를 나타냅니다. 물리학에서는 실제 세계가 매우 복잡하기 때문에 이상적인 경우를 먼저 고려해야 하는 경우가 많습니다. 이를 이상적인 파동이라고 합니다. 그러나 줄의 파동과 같은 실제 파동은 이동하면서 공기를 통과하거나 표면에 마찰합니다. 이러한 경우 마찰이 파동의 진폭을 감소시킵니다. 파동이 매질을 통과할 때 진폭은 점차 감소하지만 파장은 변하지 않는 것을 관찰할 수 있습니다."),

    # Try it
    ("<h3>Try it!</h3>", "<h3>해 보기!</h3>"),
    ("<h4>Activity 1</h4>", "<h4>활동 1</h4>"),
    ("<h4>Activity 2</h4>", "<h4>활동 2</h4>"),
    ('Let\'s use the wave simulation again. To compare a real wave to an ideal wave, set the\n                                damping (on\n                                the bottom of the screen) to "None" to mimic an ideal wave. Then, increase the\n                                damping to mimic\n                                a real wave. Notice what happens when you change the damping.',
     '파동 시뮬레이션을 다시 사용해 봅시다. 실제 파동과 이상적인 파동을 비교하려면 화면 하단의 감쇠를 "없음"으로 설정하여 이상적인 파동을 모방하세요. 그런 다음 감쇠를 높여 실제 파동을 모방하세요. 감쇠를 변경하면 어떤 일이 일어나는지 관찰하세요.'),
    ('Use the following "properties of waves" simulation to observe the difference between\n                        transverse and\n                        longitudinal waves made by a spring. Then, answer the questions that follow.',
     '다음 "파동의 성질" 시뮬레이션을 사용하여 용수철로 만든 횡파와 종파의 차이를 관찰하세요. 그런 다음 이어지는 질문에 답하세요.'),

    # Questions about wave types
    ("How is a longitudinal wave different from a transverse wave?",
     "종파는 횡파와 어떻게 다른가요?"),
    ("In a longitudinal wave, the particles move parallel to the direction of the wave. In\n                                    a transverse wave, the particles move perpendicular to the direction of the wave.",
     "종파에서 입자는 파동의 진행 방향과 평행하게 움직입니다. 횡파에서 입자는 파동의 진행 방향에 수직으로 움직입니다."),
    ("How would you describe a compression in a longitudinal wave?",
     "종파에서 밀(압축)을 어떻게 설명하겠습니까?"),
    ("It is the part of the wave where the particles are close together.",
     "입자들이 서로 가까이 모여 있는 파동의 부분입니다."),
    ("What is the highest point of a transverse wave called?",
     "횡파의 가장 높은 점을 무엇이라고 하나요?"),
    ("<p>The crest.</p>", "<p>마루입니다.</p>"),
    ("Use the following diagram and then answer the question that follows.",
     "다음 그림을 보고 이어지는 질문에 답하세요."),
    ("In the diagram, what is the distance from E to G in terms of wavelengths?",
     "그림에서 E에서 G까지의 거리는 파장으로 얼마인가요?"),
    ("<p>Half a wavelength.</p>", "<p>반 파장입니다.</p>"),

    # Take a break
    ("<h3>Take a break!</h3>", "<h3>잠시 쉬어가기!</h3>"),
    ("Excellent work! You have just completed the section on transverse and longitudinal\n                                waves. Now is a great time to take a break before you move on to periodic motion.",
     "훌륭합니다! 횡파와 종파에 대한 섹션을 완료했습니다. 주기적 운동으로 넘어가기 전에 잠시 쉬기 좋은 시간입니다."),

    # Periodic motion
    ("<h2>Periodic motion</h2>", "<h2>주기적 운동</h2>"),
    ("Explore the following video to learn about periodic motion.",
     "다음 동영상을 통해 주기적 운동에 대해 알아보세요."),
    ("A student moving back and forth on a swing can be described in many of the same ways as wave\n                        motion. A playground swing is like a pendulum, which is just a mass tied to a string that is\n                        swinging back and forth. Waves are often produced by this type of periodic motion, which is\n                        motion that repeats itself over and over again in equally spaced time intervals.",
     "그네에서 앞뒤로 움직이는 학생은 파동 운동과 여러 면에서 같은 방식으로 설명할 수 있습니다. 놀이터의 그네는 줄에 매달린 질량이 앞뒤로 흔들리는 진자와 같습니다. 파동은 이러한 유형의 주기적 운동, 즉 동일한 시간 간격으로 반복되는 운동에 의해 자주 생성됩니다."),
    ("Follow the instructions in the following simulation to make your own wave.",
     "다음 시뮬레이션의 지시에 따라 직접 파동을 만들어 보세요."),

    # Quantifying wave motion
    ("<h2>Quantifying wave motion</h2>", "<h2>파동 운동의 정량화</h2>"),
    ("It is now time to start quantifying wave motion. In other words, you will analyze periodic\n                        motion\n                        quantitatively (using numbers) rather than just qualitatively (using words) as you have been\n                        doing so far in this learning activity.",
     "이제 파동 운동을 정량화할 시간입니다. 즉, 이 학습 활동에서 지금까지 해온 정성적(말을 사용한) 분석이 아니라 정량적(숫자를 사용한) 분석을 하게 됩니다."),
    ("Before you begin, you will need to review two (2) important concepts in the study of physics:\n                        scientific notation and significant figures.",
     "시작하기 전에 물리학 학습에서 두 가지 중요한 개념을 복습해야 합니다: 과학적 표기법과 유효 숫자입니다."),

    # Scientific notation
    ("<h3>Scientific notation</h3>", "<h3>과학적 표기법</h3>"),
    ("Scientific notation is used regularly in physics to help us communicate very large numbers\n                        (for example,\n                        the mass of the Earth is approximately",
     "과학적 표기법은 물리학에서 매우 큰 수(예: 지구의 질량은 약"),
    ("kg), and very small numbers (for example, the mass of an\n                        electron is approximately", "kg)와 매우 작은 수(예: 전자의 질량은 약"),
    ("kg).", "kg)를 전달하는 데 정기적으로 사용됩니다."),

    ("A number in <strong>standard notation</strong> is written using only\n                        numbers, the usual kind of numbers we would\n                        imagine.",
     "<strong>일반 표기법</strong>의 수는 우리가 보통 생각하는 숫자만 사용하여 작성됩니다."),
    ("Scientists frequently deal with numbers that are both very large and very small. For example, the\n                        diameter of a living cell is microscopic, while distances between planets in space are immense.\n                        Using standard notation would involve too many zeros and could lead to confusion or calculation\n                        error. Thus, representing these numbers in a more compact way is often the best practice.",
     "과학자들은 매우 크거나 매우 작은 수를 자주 다룹니다. 예를 들어 살아 있는 세포의 지름은 극히 작고, 우주에서 행성 간의 거리는 매우 큽니다. 일반 표기법을 사용하면 0이 너무 많아서 혼란이나 계산 오류를 초래할 수 있습니다. 따라서 이러한 수를 더 간결하게 나타내는 것이 가장 좋은 방법입니다."),
    ("A number in <strong>scientific notation</strong> takes the form:", "<strong>과학적 표기법</strong>의 수는 다음과 같은 형태를 취합니다:"),
    ("where <em>M</em> is a number that is 1 or larger, but smaller than 10, and <em>n</em> is\n                        the number of decimal places to be moved.",
     "여기서 <em>M</em>은 1 이상 10 미만의 수이고, <em>n</em>은 소수점을 이동할 자릿수입니다."),
    ("The exponent, <em>n</em>, is equal to the number of decimal point moves or \"jumps\" because each\n                        move or jump represents a factor of ten.",
     "지수 <em>n</em>은 소수점 이동 횟수와 같습니다. 각 이동은 10배를 나타내기 때문입니다."),
    ("Importantly, a positive <em>n</em> indicates that the standard form is a large number, and a\n                        negative <em>n</em> indicates that the standard form is a small number.",
     "중요한 점은, 양의 <em>n</em>은 일반 표기법에서 큰 수를 나타내고, 음의 <em>n</em>은 작은 수를 나타낸다는 것입니다."),
    ("<h4>Examples</h4>", "<h4>예시</h4>"),
    ("The speed of light in a vacuum can be written in standard form as 299,792,458 metres per second.\n                        In scientific notation and rounded a bit, this is approximately",
     "진공에서의 빛의 속력은 일반 표기법으로 초속 299,792,458미터로 쓸 수 있습니다. 과학적 표기법으로 약간 반올림하면 약"),
    (". The decimal place has moved from beside the final 8, to between the first 2 and the 99\n                        that follows. This is a move 8 spaces left, so the exponent in scientific notation is",
     "입니다. 소수점이 마지막 8 옆에서 첫 번째 2와 그 다음의 99 사이로 이동했습니다. 이것은 왼쪽으로 8칸 이동한 것이므로 과학적 표기법의 지수는"),
    (". The value 3 is between one and ten, so it is acceptable as the <em>M</em> part of\n                        scientific notation.",
     "입니다. 값 3은 1과 10 사이이므로 과학적 표기법의 <em>M</em> 부분으로 적합합니다."),
    ("Small white blood cells are approximately 0.000007 metres in diameter. This standard notation\n                        number has a lot of zeros, and if you were copying it while calculating a related value, it\n                        would be easy to accidentally write too many or too few zeros. We can write it in scientific\n                        notation by moving the decimal place to the right until it comes after the 7. This is 6 jumps to\n                        the right, so the exponent in scientific notation will be",
     "작은 백혈구의 지름은 약 0.000007미터입니다. 이 일반 표기법의 수는 0이 많아서 관련 값을 계산하면서 복사할 때 실수로 0을 너무 많거나 적게 쓰기 쉽습니다. 소수점을 7 뒤에 올 때까지 오른쪽으로 이동하면 과학적 표기법으로 쓸 수 있습니다. 이것은 오른쪽으로 6칸 이동이므로 과학적 표기법의 지수는"),
    (". The remaining value 7 is between one and ten, so it is acceptable as <em>M</em>.",
     "이 됩니다. 남은 값 7은 1과 10 사이이므로 <em>M</em>으로 적합합니다."),
    ("Try converting the following numbers between scientific notation and standard notation.",
     "다음 수를 과학적 표기법과 일반 표기법 사이에서 변환해 보세요."),

    # Significant figures
    ("<h3>Significant figures</h3>", "<h3>유효 숫자</h3>"),
    ("Whenever you communicate scientific calculations, you need to ensure that you use proper\n                        significant\n                        figures (which are sometimes called significant digits).",
     "과학적 계산 결과를 전달할 때는 항상 적절한 유효 숫자(유효 자릿수라고도 함)를 사용해야 합니다."),
    ("A significant digit (also called a significant figure) is one that is actually measured. The\n                        number of significant digits in a measurement depends on the measuring device and the\n                        magnitude\n                        of its smallest graduation (for example, on most rulers, the smallest graduation is a\n                        millimetre).",
     "유효 숫자(유효 자릿수)란 실제로 측정된 숫자입니다. 측정값의 유효 숫자 수는 측정 장치와 최소 눈금의 크기에 따라 달라집니다(예: 대부분의 자에서 최소 눈금은 밀리미터입니다)."),
    ("Determining the number of significant figures in a measured quantity requires a few\n                        rules. The difficulty occurs primarily when there are zeros. Explore the following chart to\n                        know\n                        the rules.",
     "측정된 양의 유효 숫자 수를 결정하려면 몇 가지 규칙이 필요합니다. 어려움은 주로 0이 있을 때 발생합니다. 다음 표를 살펴보며 규칙을 알아보세요."),

    # Significant figures table
    ("<th scope=\"col\" style=\"width: 60%;\">Rule applied</th>", "<th scope=\"col\" style=\"width: 60%;\">적용 규칙</th>"),
    ("<th scope=\"col\" style=\"width: 40%;\">Examples</th>", "<th scope=\"col\" style=\"width: 40%;\">예시</th>"),
    ("All digits 1-9 (non-zeros) are significant.", "1-9의 모든 숫자(0이 아닌 수)는 유효합니다."),
    ("193 has 3 significant figures.", "193은 유효 숫자가 3개입니다."),
    ("Zeros between significant digits are significant.", "유효 숫자 사이의 0은 유효합니다."),
    ("6003 has 4 significant figures.", "6003은 유효 숫자가 4개입니다."),
    ("Leading zeros (those with no significant digits to the left) are not significant.", "앞의 0(왼쪽에 유효 숫자가 없는 0)은 유효하지 않습니다."),
    ("0.00345 has only 3 significant figures.", "0.00345는 유효 숫자가 3개뿐입니다."),
    ("Trailing zeros (those to the right of all other significant digits) are significant\n                                    only if a decimal point is present.",
     "뒤의 0(다른 모든 유효 숫자의 오른쪽에 있는 0)은 소수점이 있는 경우에만 유효합니다."),
    ("0.000000980 has 3 significant figures.", "0.000000980은 유효 숫자가 3개입니다."),
    ("0.14000 has 5 significant figures.", "0.14000은 유효 숫자가 5개입니다."),

    ("It is important to be accurate in both the taking and reporting of your measurements. The\n                        accuracy of a measurement/numerical value/number can be determined by the number of\n                        significant\n                        figures it comprises.",
     "측정값의 취득과 보고 모두에서 정확성이 중요합니다. 측정값/수치/수의 정확도는 그것이 포함하는 유효 숫자의 수에 의해 결정됩니다."),
    ("When performing calculations, after calculating a final answer, you must use significant figures\n                        to report your conclusion. In general for this course, your final answer should have the same\n                        number of significant figures as the smallest number of significant figures used in the\n                        calculation. This limitation only affects the communication of your value. If you use that same\n                        number for future calculations, you should use the full un-rounded value, then round again when\n                        reporting the next answer.",
     "계산을 수행할 때, 최종 답을 계산한 후에는 유효 숫자를 사용하여 결론을 보고해야 합니다. 이 코스에서 일반적으로 최종 답은 계산에 사용된 유효 숫자 중 가장 적은 유효 숫자 수와 같아야 합니다. 이 제한은 값의 전달에만 영향을 미칩니다. 같은 수를 향후 계산에 사용할 경우 반올림하지 않은 전체 값을 사용한 다음, 다음 답을 보고할 때 다시 반올림해야 합니다."),
    ("<h4>Exception: Exact values</h4>", "<h4>예외: 정확한 값</h4>"),
    ("Some values are exact, in which case they can be considered to have an infinite number of\n                        significant figures. For example, there are exactly 60 seconds in a minute. If you use 60 as a\n                        conversion from minutes to seconds, this conversion would not limit your significant figures.",
     "일부 값은 정확한 값이며, 이 경우 무한한 유효 숫자를 가진 것으로 간주할 수 있습니다. 예를 들어 1분은 정확히 60초입니다. 분을 초로 변환하기 위해 60을 사용할 경우, 이 변환은 유효 숫자를 제한하지 않습니다."),
    ("Refer to the Start Here section of the course for more supplementary information on mathematical\n                        and scientific communication.",
     "수학적 및 과학적 의사소통에 대한 보충 정보는 코스의 '시작하기' 섹션을 참조하세요."),

    # Simple pendulum
    ("<h2>Simple pendulum: Example of periodic motion</h2>", "<h2>단진자: 주기적 운동의 예</h2>"),
    ("For the student on the swing, one complete vibration, or cycle, would require them to swing\n                        from\n                        the top of one side, down to the bottom, then to the top on the other side, back to the\n                        bottom,\n                        and then back to where they started. The distance in either direction from the equilibrium,\n                        or\n                        rest position (when the mass is at rest, hanging vertically), to the maximum displacement\n                        (when\n                        the mass is at maximum deflection) is called the amplitude.",
     "그네를 타는 학생의 경우, 한 번의 완전한 진동(주기)은 한쪽 꼭대기에서 아래로, 다른 쪽 꼭대기로, 다시 아래로, 그리고 원래 위치로 돌아오는 것입니다. 평형 위치(질량이 정지 상태로 수직으로 매달려 있을 때)에서 최대 변위(질량이 최대 편향일 때)까지의 양쪽 거리를 진폭이라고 합니다."),
    ("There are a few words used to describe periodic motion that all mean the same thing.",
     "주기적 운동을 설명하는 데 사용되는 몇 가지 용어가 있으며 모두 같은 의미입니다."),
    ("<p>1 cycle = 1 vibration = 1 oscillation</p>", "<p>1 주기 = 1 진동 = 1 왕복</p>"),
    ("In the pendulum, when it moves from a to b to c, it has only swung through half a cycle. In\n                        order\n                        to complete one full cycle, it needs to swing from a over to c then back to a, as shown in\n                        the following diagram.",
     "진자에서 a에서 b를 거쳐 c로 이동하면 반 주기만 진행한 것입니다. 한 번의 완전한 주기를 완성하려면 다음 그림처럼 a에서 c로 갔다가 다시 a로 돌아와야 합니다."),

    # Period
    ("<h2>Period</h2>", "<h2>주기</h2>"),
    ("The time it takes for an object to go through one complete cycle is called the period. The\n                        symbol\n                        <em>T</em> is used to represent period, and the units of the period (<em>T</em>) are seconds.\n                        Period is often measured in seconds, but other time units can be used, like minutes, days,\n                        years, and so on. When measured in seconds, the symbol",
     "물체가 한 번의 완전한 주기를 완료하는 데 걸리는 시간을 주기라고 합니다. 기호 <em>T</em>를 사용하여 주기를 나타내며, 주기(<em>T</em>)의 단위는 초입니다. 주기는 보통 초 단위로 측정하지만 분, 일, 년 등 다른 시간 단위도 사용할 수 있습니다. 초 단위로 측정할 때 기호"),
    ("represents seconds, indicating that the measurement of period is in seconds.",
     "는 초를 나타내며, 주기의 측정이 초 단위임을 의미합니다."),
    ("<p>Example: 12 seconds is written as 12 s.</p>", "<p>예: 12초는 12 s로 씁니다.</p>"),
    ("Period can be calculated using the following equation:", "주기는 다음 공식으로 계산할 수 있습니다:"),

    # Formula section
    ("<h3>Formula</h3>", "<h3>공식</h3>"),
    ("<p>Where the time is measured in seconds.</p>", "<p>여기서 시간은 초 단위로 측정합니다.</p>"),

    # Period example
    ("<h3>Example: Period of a pendulum</h3>", "<h3>예제: 진자의 주기</h3>"),
    ("The pendulum makes 20 cycles in 5.0 seconds. What is the time needed to complete one cycle?",
     "진자가 5.0초 동안 20주기를 완성합니다. 한 주기를 완성하는 데 필요한 시간은 얼마인가요?"),

    # Table headers
    ("<th scope=\"col\" style=\"width: 20%;\">Step</th>", "<th scope=\"col\" style=\"width: 20%;\">단계</th>"),
    ("<th scope=\"col\" style=\"width: 80%;\">Example</th>", "<th scope=\"col\" style=\"width: 80%;\">예시</th>"),
    ("<th scope=\"col\">Step</th>", "<th scope=\"col\">단계</th>"),
    ("<th scope=\"col\">Example</th>", "<th scope=\"col\">예시</th>"),
    ("<th scope=\"col\" class=\"column_1 blueBorderLeft\">Step</th>", "<th scope=\"col\" class=\"column_1 blueBorderLeft\">단계</th>"),
    ("<th scope=\"col\" class=\"column_2\">Example</th>", "<th scope=\"col\" class=\"column_2\">예시</th>"),

    # Step names
    ("<td> Given </td>", "<td> 주어진 값 </td>"),
    ("<td> Unknown </td>", "<td> 구하는 값 </td>"),
    ("<td> Equation </td>", "<td> 공식 </td>"),
    ("<td> Solve </td>", "<td> 풀이 </td>"),
    ("<td> Statement </td>", "<td> 결론 </td>"),

    # Statement answers
    ("The time to complete one cycle is <b>0.25 s.</b>", "한 주기를 완성하는 데 걸리는 시간은 <b>0.25 s</b>입니다."),
    ("The total time had 2 significant digits, and the number of cycles can be considered exact.\n                        Therefore, our final statement had 2 significant digits.",
     "총 시간은 유효 숫자가 2개이고, 주기 수는 정확한 값으로 간주할 수 있습니다. 따라서 최종 결론은 유효 숫자 2개로 나타냈습니다."),

    # Note
    ("<h4>Note</h4>", "<h4>참고</h4>"),
    ("The period is usually measured in seconds, but larger units of time can be used for\n                        convenience\n                        if the period is very long. For example, the period of the moon orbiting the Earth is 27.3\n                        days.",
     "주기는 보통 초 단위로 측정하지만, 주기가 매우 길 경우 편의상 더 큰 시간 단위를 사용할 수 있습니다. 예를 들어, 달이 지구를 공전하는 주기는 27.3일입니다."),
    ("Try the following question to check your understanding of period.",
     "주기에 대한 이해를 확인하기 위해 다음 문제를 풀어보세요."),

    # Frequency
    ("<h2>Frequency</h2>", "<h2>진동수</h2>"),
    ("The number of cycles per second is called frequency (f). The unit of frequency is the hertz\n                        (Hz).\n                        Note: 1 Hz = 1/s.",
     "초당 주기 수를 진동수(f)라고 합니다. 진동수의 단위는 헤르츠(Hz)입니다. 참고: 1 Hz = 1/s."),
    ("Frequency can be calculated using the following equation:", "진동수는 다음 공식으로 계산할 수 있습니다:"),

    # Frequency example
    ("<h3>Example: Frequency of a pendulum</h3>", "<h3>예제: 진자의 진동수</h3>"),
    ("A pendulum swings through 12 cycles in 24 seconds. What is the frequency of the pendulum?",
     "진자가 24초 동안 12주기를 진행합니다. 진자의 진동수는 얼마인가요?"),
    ("The frequency of the pendulum is <b>0.50 Hz.</b> (The pendulum completes 0.5 of a\n                                        cycle in 1 s.)",
     "진자의 진동수는 <b>0.50 Hz</b>입니다. (진자는 1초에 0.5주기를 완성합니다.)"),
    ("Time had 2 significant digits, and number of cycles is exact, so our final answer was recorded\n                        with 2 significant digits.",
     "시간의 유효 숫자가 2개이고 주기 수는 정확한 값이므로, 최종 답은 유효 숫자 2개로 기록했습니다."),

    # Period and frequency relationship
    ("<h4 style=\"margin-left: 20px\">Relationship between period and frequency</h4>",
     "<h4 style=\"margin-left: 20px\">주기와 진동수의 관계</h4>"),
    ("Go back and review the period formula. Compare it to the frequency formula. Pause and\n                                think –\n                                what do you notice?",
     "주기 공식을 다시 살펴보세요. 진동수 공식과 비교해 보세요. 잠시 멈추고 생각해 보세요 – 무엇을 알 수 있나요?"),
    ("They are inverses of each other! The formulas are just flipped upside down as shown\n                                    in the following equations.",
     "서로 역수 관계입니다! 다음 공식에서 보듯이 분자와 분모가 뒤집어져 있습니다."),
    ("Therefore, if you know the frequency, you can find the period, and if you know\n                                    the period you can\n                                    find the frequency quite easily.",
     "따라서 진동수를 알면 주기를 구할 수 있고, 주기를 알면 진동수를 쉽게 구할 수 있습니다."),

    # Period and frequency example
    ("<h3>Example: Period and frequency in a pendulum</h3>", "<h3>예제: 진자의 주기와 진동수</h3>"),
    ("A pendulum vibrates 22 times in 11 s. Find the period and the frequency.",
     "진자가 11초 동안 22번 진동합니다. 주기와 진동수를 구하세요."),
    ("The period of the pendulum is <b>0.50 s</b> and the frequency of the\n                                        pendulum\n                                        is <b>2.0 Hz</b>. That means it takes 0.50 s for the pendulum to complete\n                                        one\n                                        cycle, and it will complete 2.0 cycles in one second.",
     "진자의 주기는 <b>0.50 s</b>이고 진동수는 <b>2.0 Hz</b>입니다. 이는 진자가 한 주기를 완성하는 데 0.50 s가 걸리며, 1초에 2.0주기를 완성한다는 의미입니다."),

    # Amplitude
    ("<h2>Amplitude</h2>", "<h2>진폭</h2>"),
    ("<p>Amplitude is the distance a particle moves from its rest position.</p>",
     "<p>진폭은 입자가 평형 위치에서 이동하는 거리입니다.</p>"),
    ("When the pendulum moves from the rest position to the top of its swing, this is considered\n                        the\n                        amplitude, as indicated in the diagram. In one full cycle, the pendulum will travel four\n                        amplitudes.",
     "진자가 평형 위치에서 흔들림의 꼭대기까지 이동할 때, 이것이 그림에 표시된 것처럼 진폭입니다. 한 번의 완전한 주기 동안 진자는 진폭의 네 배 거리를 이동합니다."),
    ("<h3>Example: A swing</h3>", "<h3>예제: 그네</h3>"),
    ("A student is sitting on a swing, going back and forth with a constant amplitude of 1.4 m.\n                        Find the\n                        total horizontal distance that the student moves through in five cycles.",
     "학생이 그네에 앉아 1.4 m의 일정한 진폭으로 앞뒤로 움직이고 있습니다. 5주기 동안 학생이 이동한 총 수평 거리를 구하세요."),
    ("<h3>Solution</h3>", "<h3>풀이</h3>"),
    ("In one cycle, the student moves through four amplitudes. There is a total of five cycles;\n                        therefore, the total number of amplitudes = 4 × 5 = 20 amplitudes. Each amplitude is 1.4 m,\n                        so\n                        the total horizontal distance = 20 x 1.4 m.",
     "한 주기 동안 학생은 진폭의 네 배를 이동합니다. 총 5주기이므로 총 진폭 수 = 4 × 5 = 20 진폭입니다. 각 진폭은 1.4 m이므로 총 수평 거리 = 20 × 1.4 m입니다."),
    ("The student moves a total horizontal distance of 28 m.", "학생은 총 28 m의 수평 거리를 이동합니다."),
    ("Try the following question to check your understanding of frequency.",
     "진동수에 대한 이해를 확인하기 위해 다음 문제를 풀어보세요."),

    # Universal wave equation
    ("<h2>Universal wave equation</h2>", "<h2>파동의 기본 방정식</h2>"),
    ("In this section, you will consider the motion of a wave through a rope and derive an equation\n                        for\n                        the speed of a wave. Imagine that the rope is tied to a secure position at one end, while\n                        you\n                        hold the other end in your hand. To make a crest, you would first move your hand rapidly up\n                        and\n                        then back down to the rest position, followed by moving your hand down and then back up to\n                        the\n                        rest position to make a trough. As you make this periodic motion, the wave will move through\n                        the\n                        rope (medium), as shown in the following figure. Recall that each time the source makes one\n                        cycle, the wave advances one wavelength.",
     "이 섹션에서는 줄을 통한 파동의 운동을 고려하고 파동의 속력에 대한 방정식을 유도합니다. 줄의 한쪽 끝이 고정되어 있고 다른 쪽 끝을 손으로 잡고 있다고 상상하세요. 마루를 만들려면 먼저 손을 빠르게 위로 올렸다가 평형 위치로 내리고, 다시 손을 아래로 내렸다가 평형 위치로 올려 골을 만듭니다. 이 주기적 운동을 하면 다음 그림처럼 파동이 줄(매질)을 통해 이동합니다. 파원이 한 주기를 만들 때마다 파동이 한 파장만큼 전진한다는 것을 기억하세요."),
    ("All types of waves keep a constant speed as they move through a medium. For example, if you\n                        drop\n                        a stone in a bowl of water, the waves created by the stone will travel at the same speed\n                        until\n                        they reach the edge of the bowl. Since there is no change in speed, the constant speed\n                        equation\n                        can be used.",
     "모든 유형의 파동은 매질을 통해 이동할 때 일정한 속력을 유지합니다. 예를 들어, 물그릇에 돌을 떨어뜨리면 돌이 만든 파동은 그릇의 가장자리에 도달할 때까지 같은 속력으로 이동합니다. 속력이 변하지 않으므로 등속 공식을 사용할 수 있습니다."),

    ("<h2>Speed of a wave</h2>", "<h2>파동의 속력</h2>"),
    ("To analyze the speed of the wave, we must first understand how to calculate the speed.",
     "파동의 속력을 분석하려면 먼저 속력을 계산하는 방법을 이해해야 합니다."),
    ("The speed of a wave can be calculated using the following equation:",
     "파동의 속력은 다음 공식으로 계산할 수 있습니다:"),
    ("<li><em>v</em> represents the speed of the wave, in metres per second (m/s)</li>",
     "<li><em>v</em>는 파동의 속력을 나타내며, 단위는 미터 매 초(m/s)입니다</li>"),
    ("<li><em>d</em> represents the distance the wave travels, in metres (m)</li>",
     "<li><em>d</em>는 파동이 이동한 거리를 나타내며, 단위는 미터(m)입니다</li>"),
    ("<li><em>t</em> represents the time it takes for the wave to travel, in seconds (s)</li>",
     "<li><em>t</em>는 파동이 이동하는 데 걸리는 시간을 나타내며, 단위는 초(s)입니다</li>"),
    ("The length of the wave has a special name, the wavelength (<em>λ</em>). So instead of using\n                        <em>d</em>, use <em>λ</em>.\n                        The\n                        time for a wave to complete one cycle also has a special name, the period (<em>T</em>). So\n                        instead of\n                        using <em>t</em>, use <em>T</em>.",
     "파동의 길이에는 특별한 이름이 있는데, 바로 파장(<em>λ</em>)입니다. 따라서 <em>d</em> 대신 <em>λ</em>를 사용합니다. 파동이 한 주기를 완성하는 시간에도 특별한 이름이 있는데, 바로 주기(<em>T</em>)입니다. 따라서 <em>t</em> 대신 <em>T</em>를 사용합니다."),
    ("This gives us a new formula for speed of a wave:", "이것은 파동의 속력에 대한 새로운 공식을 제공합니다:"),
    ("<li><em>λ</em> represents the length of one cycle of the wave, in metres (m)</li>",
     "<li><em>λ</em>는 파동 한 주기의 길이를 나타내며, 단위는 미터(m)입니다</li>"),
    ("<li><em>T</em> represents the time for one cycle of the wave to pass by, in seconds (s)\n                                </li>",
     "<li><em>T</em>는 파동 한 주기가 지나가는 시간을 나타내며, 단위는 초(s)입니다\n                                </li>"),
    ("Since there is an inverse relationship between frequency and period, we can multiply by frequency\n                        (<em>f</em>) instead of dividing by period (<em>T</em>) and\n                        come\n                        up with the universal wave equation.",
     "진동수와 주기 사이에는 역수 관계가 있으므로, 주기(<em>T</em>)로 나누는 대신 진동수(<em>f</em>)를 곱하여 파동의 기본 방정식을 도출할 수 있습니다."),
    ("Thus, the universal wave equation is:", "따라서 파동의 기본 방정식은 다음과 같습니다:"),
    ("<li><em>f</em> represents the frequency of the wave, in Hertz (Hz)</li>",
     "<li><em>f</em>는 파동의 진동수를 나타내며, 단위는 헤르츠(Hz)입니다</li>"),
    ("This is a very important equation. It is the universal wave equation, which means it works\n                        for\n                        all types of waves. You can use it to find out about the speed, wavelength, and frequency of\n                        water waves, sound waves, light waves, waves in a rope, and so on.",
     "이것은 매우 중요한 방정식입니다. 이것은 파동의 기본 방정식으로, 모든 유형의 파동에 적용됩니다. 수면파, 음파, 빛, 줄의 파동 등의 속력, 파장, 진동수를 구하는 데 사용할 수 있습니다."),

    # Examples
    ("<h3>Example 1: Universal wave equation</h3>", "<h3>예제 1: 파동의 기본 방정식</h3>"),
    ("A sound wave has a frequency of 256 Hz and is travelling at 335 m/s. What is the wavelength\n                        of\n                        the sound wave?",
     "음파의 진동수가 256 Hz이고 335 m/s로 이동하고 있습니다. 이 음파의 파장은 얼마인가요?"),
    ("The wavelength of the sound wave is <strong> 1.31 m</strong>.",
     "음파의 파장은 <strong>1.31 m</strong>입니다."),

    ("<h3>Example 2: Water wave</h3>", "<h3>예제 2: 수면파</h3>"),
    ("The wavelength of a water wave in a swimming pool is 4.0 m. The wave travels 6.0 m in 2.7 s.\n                        Find\n                        the frequency of the wave.",
     "수영장에서 수면파의 파장이 4.0 m입니다. 파동이 2.7초에 6.0 m를 이동합니다. 파동의 진동수를 구하세요."),
    ("Tip: v is not given, so use v=d/t first", "팁: v가 주어지지 않았으므로 먼저 v=d/t를 사용하세요"),
    ("Now you know the speed of the waves is 2.22 m/s, use the universal wave\n                                        equation\n                                        to find the frequency.",
     "이제 파동의 속력이 2.22 m/s임을 알았으므로, 파동의 기본 방정식을 사용하여 진동수를 구하세요."),
    ("(answer given to 2 significant digits).", "(유효 숫자 2개로 답을 표기)."),
    ("The frequency of the water waves is <b>0.56 Hz.</b>", "수면파의 진동수는 <b>0.56 Hz</b>입니다."),

    # Speed of sound section
    ("<h2>Speed of sound</h2>", "<h2>음속</h2>"),
    ("<h3>Example 3: Speed of sound</h3>", "<h3>예제 3: 음속</h3>"),

    # Consolidation section headers
    ("<h2>Summary</h2>", "<h2>요약</h2>"),
    ("<h3>Summary</h3>", "<h3>요약</h3>"),
    ("<h2>Consolidation</h2>", "<h2>정리</h2>"),

    # Generic UI elements
    ("(Opens in new\n                                window)", "(새 창에서 열림)"),
    ("(Opens in new window)", "(새 창에서 열림)"),
    ("(Opens in a new window)", "(새 창에서 열림)"),

    # Speed of sound table and related content
    ("Speed of sound in various media", "다양한 매질에서의 음속"),
    ("Medium", "매질"),
    ("Speed (m/s)", "속력 (m/s)"),
    ("Air (0°C)", "공기 (0°C)"),
    ("Air (20°C)", "공기 (20°C)"),
    ("Water (20°C)", "물 (20°C)"),
    ("Steel", "강철"),
    ("Aluminum", "알루미늄"),
    ("Glass", "유리"),

    # Misc
    ("lang=\"en\"", "lang=\"ko\""),
    ("Previous page", "이전 페이지"),
    ("Next page", "다음 페이지"),
]

def translate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for eng, kor in REPLACEMENTS:
        content = content.replace(eng, kor)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Translated: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for fp in sys.argv[1:]:
            translate_file(fp)
    else:
        print("Usage: python translate.py <file1.html> [file2.html ...]")
