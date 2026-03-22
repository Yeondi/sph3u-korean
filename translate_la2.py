#!/usr/bin/env python3
"""Translate sph3u_u1la2.html from English to Korean."""

import re

REPLACEMENTS = [
    # Title
    ("Learning activity 1.2: Transmission of Waves", "학습 활동 1.2: 파동의 전달"),

    # Learning goals
    ("Learning goals", "학습 목표"),
    ("We are learning to:", "우리는 다음을 학습합니다:"),
    ("understand how humans hear sound waves", "인간이 음파를 듣는 방법 이해하기"),
    ("identify the decibel scale of sound energy and logarithms", "소리 에너지의 데시벨 척도와 로그 이해하기"),
    ("calculate the speed, wavelength, frequency of sound in a medium such as air or water from given data", "주어진 데이터로부터 공기나 물과 같은 매질에서의 음속, 파장, 진동수 계산하기"),
    ("identify the Doppler effect of a moving sound source", "움직이는 음원의 도플러 효과 파악하기"),
    ("describe how sound waves are used and applied in nature and machinery", "음파가 자연과 기계에서 어떻게 사용되고 적용되는지 설명하기"),
    ("understand how exposure to loud sounds over time can lead to permanent hearing loss", "시간이 지남에 따라 큰 소리에 노출되면 영구적인 청력 손실을 초래할 수 있음을 이해하기"),

    # Success criteria
    ("Success criteria", "성취 기준"),
    ("I am able to:", "나는 다음을 할 수 있습니다:"),
    ("calculate the speed of sound in air and solve related problems", "공기 중 음속을 계산하고 관련 문제를 풀 수 있다"),
    ("explain why the speed of sound varies from one medium to another", "음속이 매질에 따라 달라지는 이유를 설명할 수 있다"),
    ("explain the Doppler effect and solve problems involving moving sources of sound", "도플러 효과를 설명하고 움직이는 음원과 관련된 문제를 풀 수 있다"),
    ("describe various applications involving /the transmission of sound", "음파의 전달과 관련된 다양한 응용을 설명할 수 있다"),

    # Notebook / Vocabulary
    ("Notebook", "노트"),
    ("Vocabulary: Record the following terms related to the physics of sound in your notebook. As you complete the learning activity fill in the definition and key\n                                terminology pertaining to the vocabulary.   ", "어휘: 음파의 물리학과 관련된 다음 용어들을 노트에 기록하세요. 학습 활동을 완료하면서 각 어휘의 정의와 핵심 용어를 채워 넣으세요.   "),
    ("<li>noise</li>", "<li>소음 (noise)</li>"),
    ("<li>frequency</li>", "<li>진동수 (frequency)</li>"),
    ("<li>hertz</li>", "<li>헤르츠 (hertz)</li>"),
    ("<li>decibel (dB)</li>", "<li>데시벨 (dB)</li>"),
    ("<li>logarithmic scale</li>", "<li>로그 척도 (logarithmic scale)</li>"),
    ("<li>Doppler effect</li>", "<li>도플러 효과 (Doppler effect)</li>"),
    ("<li>density</li>", "<li>밀도 (density)</li>"),
    ("<li>ultrasonic</li>", "<li>초음파 (ultrasonic)</li>"),

    # Sounds in our lives
    ("<h2>Sounds in our lives</h2>", "<h2>일상 속의 소리</h2>"),
    ("Many humans and other animals use sounds to communicate with each other, and obtain\n                        important information about the environment. Sounds may be combined in a purposeful way\n                        to produce music, which can enrich our lives. However, sound is also produced by machines,\n                        and these sounds become a nuisance to both people and animals. In many work environments,\n                        sound intensity levels may become too great, which could become a health concern.\n                        Noise-induced hearing loss may be caused by exposure to long durations of loud sounds.\n                        People who work in environments that produce loud sounds should take precautions to minimize\n                        their exposure. ",
     "많은 인간과 다른 동물들은 서로 의사소통하고 환경에 대한 중요한 정보를 얻기 위해 소리를 사용합니다. 소리는 의도적으로 조합되어 음악을 만들어 우리의 삶을 풍요롭게 할 수 있습니다. 그러나 기계에서도 소리가 발생하며, 이러한 소리는 사람과 동물 모두에게 불쾌감을 줍니다. 많은 작업 환경에서 소리의 세기가 너무 커져 건강 문제가 될 수 있습니다. 소음성 난청은 큰 소리에 장시간 노출되어 발생할 수 있습니다. 큰 소리가 발생하는 환경에서 일하는 사람들은 노출을 최소화하기 위한 예방 조치를 취해야 합니다. "),
    ("Portable music players (such as smartphones) that play music through earbuds should\n                        also be played at a sound level that is within safe ranges so that hearing loss does not\n                        occur. ",
     "이어폰을 통해 음악을 재생하는 휴대용 음악 재생 장치(스마트폰 등)도 청력 손실이 발생하지 않도록 안전한 범위 내의 음량으로 재생해야 합니다. "),
    ("Sound affects our lives in a lot of ways. But do you actually know how sound works? What\n                        determines how fast sound waves travel? Did you know that there are applications of sound in\n                        industry and manufacturing, and that doctors use it to treat injuries? In this learning\n                        activity, you will learn about the main principles of sound, and about some of its\n                        applications.",
     "소리는 많은 방식으로 우리의 삶에 영향을 미칩니다. 하지만 소리가 실제로 어떻게 작동하는지 알고 있나요? 음파의 속도를 결정하는 것은 무엇일까요? 산업과 제조에서 소리의 응용이 있으며, 의사들이 부상 치료에 소리를 사용한다는 것을 알고 있었나요? 이 학습 활동에서는 소리의 주요 원리와 몇 가지 응용에 대해 배울 것입니다."),

    # String telephone activity
    ("Try it!", "직접 해보기!"),
    ("Investigate: String telephone activity", "탐구: 실 전화기 활동"),
    ("You will be exploring how sound is transmitted through various mediums like gases,\n                                liquids, and solids. In fact, you may be surprised how well sound travels in liquids\n                                and solids. Study the following activity on string telephone and, if possible, give\n                                it a try.",
     "기체, 액체, 고체 등 다양한 매질을 통해 소리가 어떻게 전달되는지 탐구할 것입니다. 사실, 소리가 액체와 고체에서 얼마나 잘 전달되는지 놀랄 수 있습니다. 다음 실 전화기 활동을 살펴보고, 가능하다면 직접 해 보세요."),
    ("Before trying the activity, think about the following questions:", "활동을 시작하기 전에 다음 질문들에 대해 생각해 보세요:"),
    ("Do you think two people can hear each other from separate rooms?", "별도의 방에 있는 두 사람이 서로의 소리를 들을 수 있다고 생각하나요?"),
    ("What is vibrating to produce a sound?", "소리를 내기 위해 무엇이 진동하고 있나요?"),
    ("What mechanism allows people to hear sounds?", "어떤 메커니즘이 사람들에게 소리를 듣게 해 주나요?"),
    ("<h4>Materials</h4>", "<h4>준비물</h4>"),
    ("two large paper cups (disposable plastic cups will also work)", "큰 종이컵 2개 (일회용 플라스틱 컵도 가능)"),
    ("two paperclips or toothpicks", "클립 또는 이쑤시개 2개"),
    ("length of cotton string or fishing line approximately 3 to 10 metres long", "길이 약 3~10미터의 면실 또는 낚싯줄"),
    ("quiet area", "조용한 장소"),
    ("another person", "상대방 1명"),
    ("<h4>Procedure</h4>", "<h4>절차</h4>"),
    (" Punch a small hole in the center of the bottom of each cup (for plastic cups,\n                            you might need a nail or other sharp tool, so use caution when completing this\n                            step).",
     " 각 컵 바닥 중앙에 작은 구멍을 뚫으세요 (플라스틱 컵의 경우 못이나 다른 뾰족한 도구가 필요할 수 있으므로 이 단계를 수행할 때 주의하세요)."),
    (" Thread one end of string through the bottom of each cup.", " 실의 각 끝을 각 컵 바닥을 통해 꿰세요."),
    (" Place a paperclip or toothpick in the bottom of each cup and tie the loose end\n                            of the string around it (the clip or pick is just here to keep the string from\n                            slipping through the bottom of the cup).",
     " 각 컵 바닥에 클립이나 이쑤시개를 놓고 실의 느슨한 끝을 그 주위에 묶으세요 (클립이나 이쑤시개는 실이 컵 바닥을 통해 빠져나가는 것을 방지하기 위한 것입니다)."),
    (" Give one cup to your conversation partner and hold one yourself.", " 컵 하나를 대화 상대에게 주고 하나는 직접 잡으세요."),
    ("Walk slowly apart until the string connecting the cups is straight and tight.\n                        ",
     "컵을 연결하는 실이 곧고 팽팽해질 때까지 천천히 멀어지세요.\n                        "),
    ("Put your cup over your ear and have your partner talk or make sounds into their cup (keep the conversation/sound making devices relatively quiet if you are standing close to one another, but be sure to make louder sounds than a whisper).",
     "컵을 귀에 대고 상대방이 자신의 컵에 대고 말하거나 소리를 내게 하세요 (서로 가까이 서 있는 경우 비교적 조용하게 하되, 속삭임보다는 큰 소리를 내도록 하세요)."),

    # Sound as a wave
    ("<h2>Sound as a wave </h2>", "<h2>파동으로서의 소리 </h2>"),
    ("Do you recall the difference between transverse and longitudinal waves?", "횡파와 종파의 차이를 기억하나요?"),
    ("Sound is a longitudinal wave and is produced by rapidly vibrating objects.", "소리는 종파이며, 빠르게 진동하는 물체에 의해 만들어집니다."),

    # Explore this
    ("Explore this!", "탐구해 보기!"),

    # Tuning fork video
    (" The following video shows that a tuning fork vibrates when making a sound and that these vibrations\n                                are distorted/dampened in contact with water, which makes a buzzing sound.",
     " 다음 영상은 소리굽쇠가 소리를 낼 때 진동하며, 이 진동이 물과 접촉하면 왜곡/감쇠되어 윙윙거리는 소리를 내는 것을 보여줍니다."),

    # Sound is periodic motion
    ("<h3>Sound is an example of periodic motion</h3>", "<h3>소리는 주기적 운동의 한 예입니다</h3>"),
    ("A pendulum is not the only example of periodic motion. Others include a boat bobbing up and\n                        down as waves pass by, a mass on a spring moving back and forth, and the second hand on a\n                        clock, among numerous others. In this unit, you will concentrate on sound, and methods of\n                        producing sound, as the main type of periodic motion.",
     "진자만이 주기적 운동의 유일한 예는 아닙니다. 파동이 지나갈 때 위아래로 흔들리는 배, 스프링에 달린 물체가 앞뒤로 움직이는 것, 시계의 초침 등 수많은 예가 있습니다. 이 단원에서는 주요 주기적 운동 유형으로서 소리와 소리를 만드는 방법에 집중할 것입니다."),
    ("Rapidly vibrating objects produce waves in the air, which travel in all directions. When\n                        sounds are heard, it is because the wave has reached the person's ear, causing the person's\n                        eardrum to vibrate, stimulating the person's auditory nerve. ",
     "빠르게 진동하는 물체는 공기 중에 파동을 만들어내며, 이 파동은 모든 방향으로 이동합니다. 소리가 들리는 것은 파동이 사람의 귀에 도달하여 고막을 진동시키고 청각 신경을 자극하기 때문입니다. "),

    # Review
    ("<h3>Review</h3>", "<h3>복습</h3>"),
    ("To learn about how humans hear and measure sounds, access the following article <a href=\"../assets/locker_docs/sph3u_01_how_hearing_works.pdf\" target=\"_blank\">How Hearing Works<span class=\"sr-only\">(Opens in new window)</span></a> to\n                                review the\n                                anatomy of the ear.",
     "인간이 소리를 듣고 측정하는 방법에 대해 알아보려면 다음 자료 <a href=\"../assets/locker_docs/sph3u_01_how_hearing_works.pdf\" target=\"_blank\">청각의 원리<span class=\"sr-only\">(새 창에서 열림)</span></a>를 참조하여 귀의 해부학적 구조를 복습하세요."),
    ("The following video provides additional details on how human hearing works. ", "다음 영상은 인간의 청각이 어떻게 작동하는지에 대한 추가 정보를 제공합니다. "),

    # Sound frequencies
    ("Sometimes the sound is not loud enough and can go undetected, while at other times, the sound\n                        can be so intense that it can frighten, or even injure people. Sound intensity levels are\n                        measured in decibels (dB).",
     "때때로 소리가 충분히 크지 않아 감지되지 않을 수 있고, 다른 경우에는 소리가 너무 강해서 사람들을 놀라게 하거나 부상을 입힐 수도 있습니다. 소리의 세기는 데시벨(dB)로 측정됩니다."),
    ("In addition, people cannot hear all frequencies. Young people can usually hear a wider range\n                        of frequencies than older people as the inner ear hairs tend to degrade over time. A\n                        young person can hear a range of frequencies from 20 Hz to 20,000 Hz. Frequencies higher\n                        than 20,000 Hz are called ultrasonic frequencies and those lower than 20 Hz are called\n                        infrasonic frequencies.",
     "또한 사람들은 모든 진동수를 들을 수 없습니다. 내이의 유모 세포가 시간이 지남에 따라 퇴화하는 경향이 있으므로, 젊은 사람들은 보통 나이 든 사람들보다 더 넓은 범위의 진동수를 들을 수 있습니다. 젊은 사람은 20 Hz에서 20,000 Hz 범위의 진동수를 들을 수 있습니다. 20,000 Hz보다 높은 진동수를 초음파라 하고, 20 Hz보다 낮은 진동수를 초저주파라 합니다."),
    ("Hearing aids are one way to address ear damage. Hearing aids can be programmed to amplify specific\n                        frequencies that match a person's needs.",
     "보청기는 귀 손상을 해결하는 한 가지 방법입니다. 보청기는 개인의 필요에 맞는 특정 진동수를 증폭하도록 프로그래밍할 수 있습니다."),
    ("Sometimes, a person's inner ear can be unable to sense a broad range of frequencies. In this kind of\n                        hearing loss, a cochlear implant can bypass the ear itself, and send electronic signals directly to the\n                        auditory nerve.",
     "때때로 사람의 내이가 넓은 범위의 진동수를 감지하지 못할 수 있습니다. 이러한 종류의 청력 손실에서는 인공 와우가 귀 자체를 우회하여 전자 신호를 청각 신경에 직접 보낼 수 있습니다."),
    ("<h3>Investigate – Sound frequencies</h3>", "<h3>탐구 – 소리의 진동수</h3>"),
    ("<h4>Activity</h4>", "<h4>활동</h4>"),
    ("Hearing loss caused by exposure to loud, sustained sound energy such as music from\n                        earbuds has been linked to hearing loss. Adolescents should be able to perceive\n                        frequencies between 20 Hz and 18 kHz. Find out what frequencies you can perceive.\n",
     "이어폰 음악과 같은 지속적인 큰 소리 에너지에 노출되면 청력 손실이 발생할 수 있습니다. 청소년은 20 Hz에서 18 kHz 사이의 진동수를 인지할 수 있어야 합니다. 자신이 인지할 수 있는 진동수를 알아보세요.\n"),
    ("The following video demonstrates how different pitches are heard.", "다음 영상은 다른 높낮이의 소리가 어떻게 들리는지 보여줍니다."),

    # Intensity of sound table
    ("<h3>Intensity of sound</h3>", "<h3>소리의 세기</h3>"),
    ("Now let's study the intensity of sound levels and some sources that closely match these levels.", "이제 소리의 세기 수준과 이러한 수준에 가까운 음원들을 살펴보겠습니다."),
    ("<th scope=\"col\">Source</th>", "<th scope=\"col\">음원</th>"),
    ("<th scope=\"col\">Intensity level (dB)</th>", "<th scope=\"col\">세기 수준 (dB)</th>"),
    (" Threshold of human hearing", " 인간 청각의 문턱값"),
    (" Whisper ", " 속삭임 "),
    (" Average home", " 일반 가정"),
    (" Two-person conversation", " 두 사람의 대화"),
    (" Vacuum cleaner", " 진공청소기"),
    (" Loud music in home", " 집에서의 큰 음악"),
    (" Rock concert", " 록 콘서트"),
    (" Pain threshold", " 통증 문턱값"),

    # Noise and noise pollution
    ("<h4>Noise and noise pollution</h4>", "<h4>소음과 소음 공해</h4>"),
    ("You have already considered some of the impacts that noise can have on society\n                        and the environment. Now you will study what can be defined as noise. Some\n                        people hear loud music and say that it's just noise, while others might be hearing their\n                        favourite song. How, then, can a society define noise? It's all a matter of\n                        personal opinion.",
     "여러분은 소음이 사회와 환경에 미칠 수 있는 영향에 대해 이미 생각해 보았습니다. 이제 소음으로 정의할 수 있는 것이 무엇인지 알아볼 것입니다. 어떤 사람들은 큰 음악을 듣고 단지 소음이라고 말하지만, 다른 사람들은 자신이 좋아하는 노래를 듣고 있을 수 있습니다. 그렇다면 사회는 소음을 어떻게 정의할 수 있을까요? 이것은 전적으로 개인적 의견의 문제입니다."),
    ("Any form of unwelcome sound is considered noise. What, then, constitutes noise\n                        pollution? ",
     "모든 형태의 원치 않는 소리는 소음으로 간주됩니다. 그렇다면 소음 공해란 무엇일까요? "),
    ("Noise pollution is sound that disrupts human activity or the balance of nature.\n                        In humans, noise pollution can cause psychological problems, as well as real\n                        physical damage to the functioning of the ear. In many studies, people have\n                        reported higher levels of stress, frustration, and aggression, due to an\n                        increase in noise pollution. The inability to concentrate and a general lack of\n                        focus is well documented in these studies. Noise pollution can interfere with\n                        normal behaviour in animals as well, causing them to move to other areas, where\n                        possible.\n",
     "소음 공해는 인간의 활동이나 자연의 균형을 방해하는 소리입니다. 인간에게 소음 공해는 심리적 문제뿐만 아니라 귀의 기능에 실질적인 물리적 손상을 일으킬 수 있습니다. 많은 연구에서 소음 공해의 증가로 인해 더 높은 수준의 스트레스, 좌절감, 공격성이 보고되었습니다. 집중력 부족과 전반적인 주의력 결핍은 이러한 연구들에서 잘 기록되어 있습니다. 소음 공해는 동물들의 정상적인 행동도 방해할 수 있으며, 가능한 경우 다른 지역으로 이동하게 만들 수 있습니다.\n"),
    ("Problems with noise pollution are mostly due to the intensity of a sound, rather\n                        than just the occasional annoyance of a quiet periodic sound. The range of sound\n                        intensities that can be detected by the human ear is vast. You can hear a pin\n                        drop in a silent room, as well as a jet engine that is several kilometres away.\n",
     "소음 공해의 문제는 조용한 주기적 소리의 간헐적 불쾌감보다는 대부분 소리의 세기 때문입니다. 인간의 귀가 감지할 수 있는 소리 세기의 범위는 매우 넓습니다. 조용한 방에서 핀이 떨어지는 소리부터 수 킬로미터 떨어진 제트 엔진 소리까지 들을 수 있습니다.\n"),
    ("To help deal with this wide range of sound intensities, the decibel scale was\n                        invented. In this scale, the lowest audible intensity of sound that can be\n                        detected by the human ear, called the threshold of hearing, is assigned a value\n                        of 0 decibels (dB). Considering your metric prefixes, you may be able to tell that this is actually\n                        equivalent to one tenth (deci-) of a different unit (the bel). A sound that is 10 times as intense, like the\n                        rustling of\n                        leaves, is then assigned a decibel level of 10 dB. A whisper that is 1000\n                        (10<sup>3</sup>) times as intense as the threshold of hearing is assigned 30 dB.\n                        A normal conversation that is one million times as intense (10<sup>6</sup>) is\n                        assigned 60 dB. Basically, if the sound becomes 10 times more intense then the decibel level increases by\n                        10.",
     "이 넓은 범위의 소리 세기를 다루기 위해 데시벨 척도가 발명되었습니다. 이 척도에서 인간의 귀가 감지할 수 있는 가장 낮은 소리의 세기인 청각의 문턱값에는 0 데시벨(dB)의 값이 부여됩니다. 미터법 접두사를 고려하면, 이것이 실제로 다른 단위(벨)의 10분의 1(데시-)에 해당한다는 것을 알 수 있습니다. 나뭇잎이 바스락거리는 소리처럼 10배 더 강한 소리에는 10 dB의 데시벨 수준이 부여됩니다. 청각의 문턱값보다 1000(10<sup>3</sup>)배 강한 속삭임은 30 dB이 부여됩니다. 100만 배(10<sup>6</sup>) 강한 일반 대화는 60 dB이 부여됩니다. 기본적으로 소리가 10배 더 강해지면 데시벨 수준은 10 증가합니다."),
    ("<b>For example</b>: If sound 1 is 50 dB and sound 2 is 80 dB, then sound 2 is 30\n                        dB higher than sound 1, and is therefore 10<sup>3</sup> = 1000 times more\n                        intense. ",
     "<b>예시</b>: 소리 1이 50 dB이고 소리 2가 80 dB이면, 소리 2는 소리 1보다 30 dB 높으므로 10<sup>3</sup> = 1000배 더 강합니다. "),
    ("This property of sound measured with the decibel scale is called loudness. Humans\n                        will actually feel physical pain if exposed to 120 dB or more. Exposure to very\n                        loud sounds over a lengthy period of time, or extremely loud sounds for a short\n                        time, can cause temporary or permanent hearing loss.\n",
     "데시벨 척도로 측정되는 이 소리의 특성을 음량이라고 합니다. 인간은 120 dB 이상에 노출되면 실제로 물리적 고통을 느낍니다. 매우 큰 소리에 장시간 노출되거나, 극도로 큰 소리에 짧은 시간 노출되면 일시적 또는 영구적 청력 손실을 초래할 수 있습니다.\n"),
    ("One way to reduce noise pollution is to build structures using materials that\n                        absorb sound, rather than reflecting or transmitting it. In this way, sound\n                        levels inside buildings will decrease and the effects of noise pollution will be\n                        reduced. This solution won't help people outside, however. One solution for",
     "소음 공해를 줄이는 한 가지 방법은 소리를 반사하거나 전달하는 대신 흡수하는 재료를 사용하여 건물을 짓는 것입니다. 이렇게 하면 건물 내부의 소리 수준이 감소하고 소음 공해의 영향이 줄어듭니다. 그러나 이 해결책은 외부에 있는 사람들에게는 도움이 되지 않습니다."),
    ("outside noise involves wearing ear plugs, which simply block sound from entering\n                        the ear to reduce the loudness. Of course, the person is then less aware of\n                        other sounds around them, which could be a disadvantage or even a safety\n                        concern.",
     " 외부 소음에 대한 한 가지 해결책은 귀마개를 착용하는 것으로, 단순히 소리가 귀에 들어가는 것을 차단하여 음량을 줄입니다. 물론, 그 사람은 주변의 다른 소리에 대한 인식이 낮아지므로, 이는 단점이거나 안전 문제가 될 수 있습니다."),
    ("A high-tech solution involves using noise cancellation headphones. These\n                        headphones are placed over the ears and have a small microphone attached to\n                        them. When a sound is detected by the microphone, the headphones produce exactly\n                        the same sound but they shift it completely out of phase. In this way, the sound\n                        from the environment and the sound from the headphones interfere destructively.\n                        No sound is detected by the person wearing the headphones. This type of\n                        technology is typically used by passengers travelling first class on airplanes\n                        or workers who must endure very loud noises.\n",
     "첨단 기술 해결책으로는 소음 제거 헤드폰을 사용하는 것이 있습니다. 이 헤드폰은 귀 위에 놓이며 작은 마이크가 부착되어 있습니다. 마이크가 소리를 감지하면 헤드폰은 정확히 같은 소리를 생성하되 완전히 위상을 반대로 바꿉니다. 이렇게 하면 환경의 소리와 헤드폰의 소리가 상쇄 간섭합니다. 헤드폰을 착용한 사람은 아무 소리도 감지하지 못합니다. 이러한 유형의 기술은 일반적으로 비행기의 일등석 승객이나 매우 큰 소음을 견뎌야 하는 근로자들이 사용합니다.\n"),

    # Try it - check understanding
    ("Try the following questions to check your understanding.", "다음 문제를 풀어 이해도를 확인하세요."),
    (" Try the following questions to check your understanding.", " 다음 문제를 풀어 이해도를 확인하세요."),

    # Sound travels in air
    ("<h2>Sound travels in air</h2>", "<h2>공기 중에서의 소리 전달</h2>"),
    ("Sound is a mechanical wave, which means it needs a medium to travel through. That means sound\n                        cannot travel through a vacuum. ",
     "소리는 역학적 파동으로, 이동하기 위해 매질이 필요합니다. 이는 소리가 진공을 통해 이동할 수 없다는 것을 의미합니다. "),
    ("The following video demonstrates that sound requires a medium in which to propagate\n                                (travel). When the air is slowly removed from the apparatus, the sound is no longer\n                                heard.",
     "다음 영상은 소리가 전파(이동)하기 위해 매질이 필요하다는 것을 보여줍니다. 장치에서 공기가 천천히 제거되면 소리가 더 이상 들리지 않습니다."),
    ("To explain more clearly how sound travels through air, consider a typical tuning fork.",
     "소리가 공기를 통해 어떻게 이동하는지 더 명확하게 설명하기 위해, 일반적인 소리굽쇠를 생각해 봅시다."),
    ("A tuning fork has two tines (prongs) that move back and forth when they are struck. When the\n                        tines move, they push the particles in the air closer together, making what are called\n                        compressions; they also pull back from the particles in the air allowing them to spread out\n                        more, creating what are called rarefactions.",
     "소리굽쇠에는 두 개의 가지(갈래)가 있어 타격하면 앞뒤로 움직입니다. 가지가 움직이면 공기 중의 입자들을 더 가까이 밀어 밀(압축)이라 불리는 것을 만들고, 또한 공기 중 입자들로부터 뒤로 당겨져 입자들이 더 퍼지게 하여 소(희박)라 불리는 것을 만듭니다."),
    ("These air particles are displaced from their equilibrium positions and they then bump into\n                        neighbouring particles, causing them to move as well. This pattern of air particle movement\n                        occurs in all directions, which is what allows the sound wave to travel through the air, as\n                        represented in the following diagram.",
     "이 공기 입자들은 평형 위치에서 벗어나 이웃 입자들과 부딪혀 그들도 움직이게 합니다. 이러한 공기 입자 운동 패턴은 모든 방향에서 발생하며, 이것이 다음 그림에 나타난 것처럼 음파가 공기를 통해 이동할 수 있게 하는 것입니다."),

    # Press here for long description
    ("Press\n                                                here for a long description.", "상세 설명을 보려면\n                                                여기를 누르세요."),
    ("(Opens in new window)", "(새 창에서 열림)"),

    # Sound is a longitudinal wave
    ("<h3>Sound is a longitudinal wave</h3>", "<h3>소리는 종파입니다</h3>"),
    ("Since the air particles only move back and forth, parallel to the direction of the wave motion, this\n                        represents a longitudinal wave. In a compression, the particles are densely packed together and the pressure\n                        is high. In a rarefaction, the particles are spread out and the pressure is low.",
     "공기 입자들은 파동의 운동 방향과 평행하게 앞뒤로만 움직이므로, 이것은 종파를 나타냅니다. 밀(압축)에서는 입자들이 빽빽하게 모여 있고 압력이 높습니다. 소(희박)에서는 입자들이 퍼져 있고 압력이 낮습니다."),
    ("Rather than representing sound waves as a series of dots (which denote particles), you can use another\n                        method to indicate the areas of high pressure and low pressure – you may use a graph of pressure created by\n                        the movement of the wave through the medium. If you represent the sound pressure waves as a transverse wave,\n                        you can show the regions of high pressure (compressions in the diagram indicated as C) as crests and the\n                        regions of low pressure (rarefactions in the diagram indicated as R) as troughs. Thus, the diagram shows the\n                        simpler method of representing a sound wave.",
     "음파를 일련의 점(입자를 나타냄)으로 표현하는 대신, 고압 영역과 저압 영역을 나타내는 다른 방법을 사용할 수 있습니다 – 매질을 통한 파동의 운동에 의해 생성된 압력 그래프를 사용할 수 있습니다. 음압파를 횡파로 표현하면, 고압 영역(그림에서 C로 표시된 밀)을 마루로, 저압 영역(그림에서 R로 표시된 소)을 골로 나타낼 수 있습니다. 따라서 이 그림은 음파를 표현하는 더 간단한 방법을 보여줍니다."),

    # Perception of sound
    ("<h3>Perception of sound</h3>", "<h3>소리의 인지</h3>"),
    ("You may have noticed that since sound is a wave, all of the terminology and concepts associated with waves\n                        from Learning activity 1.1 also apply to sound. Louder sounds imply greater amplitude of vibration of the\n                        air\n                        particles. A higher pitch of sound refers to higher frequencies of vibration. Sound also travels at a",
     "소리가 파동이므로 학습 활동 1.1의 파동과 관련된 모든 용어와 개념이 소리에도 적용된다는 것을 알았을 것입니다. 더 큰 소리는 공기 입자의 더 큰 진폭의 진동을 의미합니다. 더 높은 음높이의 소리는 더 높은 진동수의 진동을 나타냅니다. 소리는 또한"),
    ("constant speed, unless the medium changes. ",
     "매질이 변하지 않는 한 일정한 속력으로 이동합니다. "),
    ("The frequency of the sound wave is related to the pitch of the sound. The pitch is what is perceived by the\n                        listener. For example, high frequency sounds are perceived as high-pitched sounds, while low frequency\n                        vibrations would cause low-pitched sounds. ",
     "음파의 진동수는 소리의 음높이와 관련이 있습니다. 음높이는 듣는 사람이 인지하는 것입니다. 예를 들어, 고주파 소리는 높은 음높이의 소리로 인지되고, 저주파 진동은 낮은 음높이의 소리를 만듭니다. "),
    ("Each tuning fork has a specific frequency. A 256 Hz tuning fork means the tines vibrate back and forth 256\n                        times per second. A 512 Hz tuning fork means the tines vibrate back and forth 512 times per second. The 512\n                        Hz tuning fork would have a higher pitch because it is going back and forth more times per second than the\n                        256 Hz tuning fork.",
     "각 소리굽쇠에는 특정 진동수가 있습니다. 256 Hz 소리굽쇠는 가지가 초당 256회 앞뒤로 진동한다는 의미입니다. 512 Hz 소리굽쇠는 가지가 초당 512회 앞뒤로 진동합니다. 512 Hz 소리굽쇠가 256 Hz 소리굽쇠보다 초당 더 많이 앞뒤로 움직이므로 더 높은 음높이를 가집니다."),

    # Speed of sound in air
    ("<h2>Speed of sound in air</h2>", "<h2>공기 중 음속</h2>"),
    ("Careful experiments have shown that sound travels at 332 m/s at normal pressure and 0°C. If the temperature\n                        of the air is higher, then the speed of sound increases. For every increase in temperature of 1°C, the speed\n                        of sound increases by 0.59 m/s. ",
     "정밀한 실험에 의하면 소리는 정상 압력과 0°C에서 332 m/s로 이동합니다. 공기의 온도가 높으면 음속이 증가합니다. 온도가 1°C 증가할 때마다 음속은 0.59 m/s 증가합니다. "),
    ("The speed of sound in air (<em>v</em>) at normal pressure can be calculated using the following equation:\n",
     "정상 압력에서의 공기 중 음속(<em>v</em>)은 다음 공식을 사용하여 계산할 수 있습니다:\n"),
    ("<h3>Formula</h3>", "<h3>공식</h3>"),
    ("Where <i>T</i> is the temperature in degrees Celsius.", "여기서 <i>T</i>는 섭씨 온도입니다."),
    ("<strong>Note:</strong> This equation can only be used when the sound is\n                                    travelling through\n                                    air. If it is\n                                    travelling in a different medium, for example water, you cannot use this\n                                    equation.&#9;",
     "<strong>참고:</strong> 이 공식은 소리가 공기를 통해 이동할 때만 사용할 수 있습니다. 예를 들어 물과 같은 다른 매질에서 이동하는 경우에는 이 공식을 사용할 수 없습니다.&#9;"),

    # Example: Calculate speed of sound
    ("<h3>Example: Calculate speed of sound</h3>", "<h3>예제: 음속 계산</h3>"),
    ("Calculate the speed of sound in air when the temperature is 18°C.", "온도가 18°C일 때 공기 중 음속을 계산하세요."),
    (">Step<", ">단계<"),
    (">Example<", ">풀이<"),
    ("> Given <", "> 주어진 값 <"),
    ("> Unknown <", "> 구하는 값 <"),
    ("> Equation <", "> 공식 <"),
    ("> Solve <", "> 풀이 <"),
    ("> Statement <", "> 결론 <"),
    ("Temperature ", "온도 "),
    ("Since we have recorded the given value(s) and the unknown value(s), we can find an equation from\n                                        our notes that references both items. Though there aren't many options yet, you will develop a\n                                        larger equation reference sheet throughout this course. The speed of sound formula includes both\n                                        speed and temperature, so we should use that equation.",
     "주어진 값과 구하는 값을 기록했으므로, 두 항목을 모두 참조하는 공식을 노트에서 찾을 수 있습니다. 아직 선택지가 많지 않지만, 이 과정을 통해 더 큰 공식 참조표를 만들게 될 것입니다. 음속 공식은 속력과 온도를 모두 포함하므로, 그 공식을 사용해야 합니다."),
    ("The speed of sound is <b>340 m/s.</b> (Rounded to 2 significant figures.)", "음속은 <b>340 m/s</b>입니다. (유효 숫자 2자리로 반올림.)"),

    # Example: Finding wavelength
    ("<h3>Example: Finding wavelength of sound</h3>", "<h3>예제: 소리의 파장 구하기</h3>"),
    ("A 350 Hz tuning fork is sounded outside where the temperature is –20.0°C. What is the\n                        wavelength of the sound?",
     "350 Hz 소리굽쇠가 온도가 –20.0°C인 실외에서 울렸습니다. 소리의 파장은 얼마인가요?"),
    ("The first step is to find the speed of sound.", "첫 번째 단계는 음속을 구하는 것입니다."),
    ("The speed of sound is <b>320.2 m/s.</b> (Since this is not the final statement in the problem, it\n                                    does not need to be rounded to three significant digits.)",
     "음속은 <b>320.2 m/s</b>입니다. (이것은 문제의 최종 결론이 아니므로 유효 숫자 3자리로 반올림할 필요가 없습니다.)"),
    ("The second step is to rearrange the universal wave equation to find the wavelength.", "두 번째 단계는 파동의 기본 방정식을 재배열하여 파장을 구하는 것입니다."),
    ("The wavelength of the sound wave is <b>0.91 m.</b>", "음파의 파장은 <b>0.91 m</b>입니다."),

    # Example: Finding air temperature
    ("<h3>Example: Finding air temperature</h3>", "<h3>예제: 기온 구하기</h3>"),
    ("What is the temperature if the speed of sound is 360 m/s?", "음속이 360 m/s일 때 온도는 얼마인가요?"),
    ("The air temperature is <b>47 °C.</b> (Answer is given to 2 significant figures.)", "기온은 <b>47 °C</b>입니다. (답은 유효 숫자 2자리로 주어집니다.)"),

    # Explore video pulse waves
    ("Explore the following video clip with two different wave pulse waves. ", "두 가지 다른 파동 펄스가 있는 다음 영상을 살펴보세요. "),
    ("Notice within the previous video that the time for the wave pulse to travel is always the\n                        same no matter the amplitude\n                        or frequency of the initial vibration.",
     "이전 영상에서 초기 진동의 진폭이나 진동수에 관계없이 파동 펄스가 이동하는 시간은 항상 같다는 것에 주목하세요."),
    ("For sound, a change in the medium can cause a drastic change in the speed of sound.", "소리의 경우, 매질의 변화는 음속에 급격한 변화를 일으킬 수 있습니다."),
    ("Recall that a wave travels at a constant speed, as long it stays in the same medium. ", "파동은 같은 매질에 머무는 한 일정한 속력으로 이동한다는 것을 기억하세요. "),

    # Sound travels in various materials
    ("<h2>Sound travels in various materials</h2>", "<h2>다양한 물질에서의 소리 전달</h2>"),

    # Tab labels
    (">Gas</a>", ">기체</a>"),
    (">Liquid</a>", ">액체</a>"),
    (">Solid</a>", ">고체</a>"),

    # Table headers for material tabs
    (">State</th>", ">상태</th>"),
    (">Material</th>", ">물질</th>"),
    (">Speed of sound (m/s)</th>", ">음속 (m/s)</th>"),

    # Materials in table
    ("\n                                                Gas\n", "\n                                                기체\n"),
    ("Carbon dioxide", "이산화탄소"),
    (" Oxygen ", " 산소 "),
    (" Nitrogen ", " 질소 "),
    (" Helium ", " 헬륨 "),
    (" Hydrogen ", " 수소 "),
    ("\n                                                Liquid\n", "\n                                                액체\n"),
    ("Alcohol", "알코올"),
    (" Sea water ", " 바닷물 "),
    (" Fresh water ", " 민물 "),
    (" Mercury ", " 수은 "),
    ("\n                                                Solid\n", "\n                                                고체\n"),
    ("Pine wood", "소나무"),
    (" Maple wood ", " 단풍나무 "),
    (" Steel ", " 강철 "),
    (" Glass ", " 유리 "),
    (" Aluminum ", " 알루미늄 "),

    # Sound waves in solids, liquids, gases
    ("<h3>Sound waves in solids, liquids and gases</h3>", "<h3>고체, 액체, 기체에서의 음파</h3>"),
    ("The particle theory of matter states that all matter is made up of tiny particles. ", "물질의 입자 이론에 따르면 모든 물질은 작은 입자로 이루어져 있습니다. "),
    ("In a solid, these particles are strongly attracted to one another and held close\n                            together in a fixed arrangement. ",
     "고체에서 이 입자들은 서로 강하게 끌어당기며 고정된 배열로 가까이 붙어 있습니다. "),
    ("In a liquid, they are not quite as strongly attracted together, and are a little further\n                            apart and able to move freely. ",
     "액체에서는 인력이 그다지 강하지 않고, 약간 더 떨어져 있으며 자유롭게 움직일 수 있습니다. "),
    ("In a gas, there is almost no attraction between particles. They are far apart and they\n                            can float around freely. ",
     "기체에서는 입자 사이에 거의 인력이 없습니다. 입자들은 멀리 떨어져 있고 자유롭게 떠다닐 수 있습니다. "),
    ("How does this explain why sound travels the fastest in a solid, more slowly in liquids, and\n                        the slowest in a gas? Study the following elements to learn more.",
     "이것이 왜 소리가 고체에서 가장 빠르고, 액체에서 더 느리며, 기체에서 가장 느린지를 어떻게 설명할까요? 더 자세히 알아보려면 다음 내용을 살펴보세요."),

    # Tab content: Solids, Liquid, Gas
    ("Solids</a>", "고체</a>"),
    ("A sound wave is a longitudinal wave and the particles in the medium just move\n                                        back and forth, parallel to the wave motion. The wave transfers when the\n                                        particles move from their equilibrium position and begin to bump into the\n                                        particles next to them. The strong force of attraction existing between\n                                        particles in a solid means that when a particle is disturbed, it pushes or\n                                        it pulls all of its neighbours immediately because they are so close. This\n                                        allows sound to travel very fast in solids.",
     "음파는 종파이며 매질의 입자들은 파동의 운동 방향과 평행하게 앞뒤로만 움직입니다. 입자들이 평형 위치에서 이동하여 옆의 입자들과 부딪히기 시작하면 파동이 전달됩니다. 고체에서 입자 사이에 존재하는 강한 인력은 입자가 교란되면 매우 가까이 있기 때문에 즉시 모든 이웃을 밀거나 당긴다는 것을 의미합니다. 이것이 소리가 고체에서 매우 빠르게 이동할 수 있게 합니다."),
    ("In a liquid, the particles are less attracted to each other and further\n                                        apart. This means that a particle needs to be moved quite a bit before it\n                                        begins to disturb its nearest neighbours. Therefore, sound travels more\n                                        slowly. ",
     "액체에서는 입자들이 서로 덜 끌어당기고 더 멀리 떨어져 있습니다. 이는 입자가 가장 가까운 이웃을 교란하기 시작하기 전에 상당히 많이 움직여야 한다는 것을 의미합니다. 따라서 소리가 더 느리게 이동합니다. "),
    ("In a gas, the particles are spread out and are hardly attracted to each\n                                        other. This means that gas particles have to move around until they actually\n                                        run into each other, in order to transmit sound. Sound moves the slowest\n                                        through a gas.",
     "기체에서는 입자들이 퍼져 있고 서로 거의 끌어당기지 않습니다. 이는 기체 입자들이 소리를 전달하기 위해 실제로 서로 부딪힐 때까지 돌아다녀야 한다는 것을 의미합니다. 소리는 기체를 통해 가장 느리게 이동합니다."),

    # Think
    ("<h3>Think</h3>", "<h3>생각해 보기</h3>"),
    ("1. In which state of matter does sound travel the fastest?", "1. 소리가 가장 빠르게 이동하는 물질의 상태는 무엇인가요?"),
    (">Suggested\n                                Answer<", ">풀이\n                                보기<"),
    (">Suggested\n                                Answer</button>", ">풀이\n                                보기</button>"),
    ("<p>Solids.</p>", "<p>고체입니다.</p>"),
    ("2. What happens to the speed of sound in air as the temperature\n                                increases? (Think about the formula for speed of sound.)",
     "2. 온도가 증가하면 공기 중 음속은 어떻게 되나요? (음속 공식을 생각해 보세요.)"),
    ("<p>The speed increases.</p>", "<p>속력이 증가합니다.</p>"),
    ("3. Mercury is a very dense liquid, while sea water is not very\n                                dense. How does the density relate to the speed of sound? ",
     "3. 수은은 매우 밀도가 높은 액체이고, 바닷물은 밀도가 그다지 높지 않습니다. 밀도는 음속과 어떤 관계가 있나요? "),
    ("As the density increases, the speed increases. As the density decreases, the\n                                    speed decreases.",
     "밀도가 증가하면 속력이 증가합니다. 밀도가 감소하면 속력이 감소합니다."),

    # Doppler effect
    ("<h2>The Doppler effect</h2>", "<h2>도플러 효과</h2>"),
    ("Have you ever heard the sound of a siren from an emergency vehicle as it is passing you? You\n                        might have noticed that the siren sounds more high-pitched as the vehicle approaches you and\n                        more low-pitched as it is moving away. From the listener's perspective, the apparent\n                        frequency of the siren changes when the source of sound is approaching, compared to when\n                        it's moving away. This change in frequency from your perspective due to the motion of the\n                        source is called the <b>Doppler effect.</b>",
     "지나가는 응급 차량의 사이렌 소리를 들어본 적이 있나요? 차량이 다가올 때 사이렌 소리가 더 높은 음으로 들리고, 멀어질 때 더 낮은 음으로 들린다는 것을 알았을 것입니다. 듣는 사람의 관점에서 음원이 다가올 때와 멀어질 때 사이렌의 겉보기 진동수가 변합니다. 음원의 운동으로 인한 이러한 진동수의 변화를 <b>도플러 효과</b>라고 합니다."),
    ("To understand the Doppler effect, you will examine the following diagram. The first\n                        illustration shows a source of sound waves that is stationary. The waves travel\n                        away from the source at a constant speed in all directions. These waves will be equally\n                        spaced, as shown in the following diagram.",
     "도플러 효과를 이해하기 위해 다음 그림을 살펴보겠습니다. 첫 번째 그림은 정지해 있는 음원을 보여줍니다. 파동은 음원에서 모든 방향으로 일정한 속력으로 이동합니다. 이 파동들은 다음 그림에 보이는 것처럼 균일한 간격을 가집니다."),
    ("The second illustration shows a sound source that is moving, away\n                        from point A and towards point B. The sound still travels at a constant speed in all\n                        directions, but the source is also moving. The waves at point A are moving\n                        away from the source at the speed of sound, minus the speed of v<sub>source</sub> (the speed of the source).\n                        By the time\n                        one wave peak is emitted and then the next is emitted, the source has already moved, so the\n                        waves are not concentric anymore. From the perspective of an observer at A, this causes the waves to stretch\n                        out, increasing the\n                        wavelength and decreasing the frequency (because the speed is constant). So, the wavefronts\n                        in front of the source will get closer together, while behind the source, they will be more\n                        spaced out.",
     "두 번째 그림은 점 A에서 멀어지고 점 B를 향해 이동하는 음원을 보여줍니다. 소리는 여전히 모든 방향으로 일정한 속력으로 이동하지만, 음원도 이동하고 있습니다. 점 A에서의 파동은 음속에서 v<sub>source</sub>(음원의 속력)를 뺀 속력으로 음원에서 멀어지고 있습니다. 하나의 파동 봉우리가 방출되고 다음 것이 방출될 때쯤이면 음원은 이미 이동한 상태이므로, 파동은 더 이상 동심원이 아닙니다. A에 있는 관측자의 관점에서 이는 파동이 늘어나 파장이 증가하고 진동수가 감소하게 합니다(속력이 일정하므로). 따라서 음원 앞의 파면은 서로 더 가까워지고, 음원 뒤의 파면은 더 멀어집니다."),
    ("The waves that are headed\n                        towards B will have a higher frequency. This is because while the sound travels away from\n                        the source, the source is headed in the direction of the sound. The waves in front of the\n                        source (at position B) are \"bunching up,\" so the wavelength is smaller. These waves will hit\n                        the eardrum of an observer at B more often than before so the frequency will be higher. At\n                        B, an observer will hear the siren at a higher pitch. The opposite effect happens at A, as\n                        presented in the illustration. As a result, an observer at A will hear a lower\n                        frequency when the source is moving away, which will result in a lower pitch. ",
     "B를 향해 가는 파동은 더 높은 진동수를 가집니다. 이는 소리가 음원에서 멀어지는 동안 음원이 소리의 방향으로 향하고 있기 때문입니다. 음원 앞의 파동(위치 B)은 \"밀집\"되어 파장이 더 작습니다. 이 파동은 이전보다 더 자주 B에 있는 관측자의 고막에 도달하므로 진동수가 더 높아집니다. B에서 관측자는 사이렌을 더 높은 음으로 듣게 됩니다. 그림에 나타난 것처럼 A에서는 반대 효과가 발생합니다. 결과적으로, A에 있는 관측자는 음원이 멀어질 때 더 낮은 진동수를 듣게 되어 더 낮은 음이 됩니다. "),
    ("The following equation to calculate the apparent frequency of a moving source is:", "움직이는 음원의 겉보기 진동수를 계산하는 공식은 다음과 같습니다:"),

    # Doppler equation explanation
    ("Where f<sub>source</sub> or f<sub>1</sub> is the stationary frequency of the source,\n                        f<sub>observed</sub> or f<sub>2</sub> is the apparent frequency detected by an observer at\n                        either A or B, v<sub>sound</sub> is the speed of sound in air, and v<sub>source</sub> is the\n                        speed of the source. The denominator v<sub>sound</sub> + v<sub>source</sub> is used when the\n                        source is moving away from the observer.",
     "여기서 f<sub>source</sub> 또는 f<sub>1</sub>은 음원의 정지 진동수이고, f<sub>observed</sub> 또는 f<sub>2</sub>는 A 또는 B에 있는 관측자가 감지한 겉보기 진동수이며, v<sub>sound</sub>는 공기 중 음속이고, v<sub>source</sub>는 음원의 속력입니다. 분모 v<sub>sound</sub> + v<sub>source</sub>는 음원이 관측자로부터 멀어질 때 사용됩니다."),
    ("In this case, the denominator is larger, which makes the apparent frequency lower than the\n                        stationary frequency. The denominator v<sub>sound</sub> – v<sub>source</sub> is used when\n                        the source is moving towards the observer. In this case, the denominator is smaller, which\n                        makes the apparent frequency higher than the stationary frequency. Note that the units for\n                        speed must be identical for you to use this equation.",
     "이 경우, 분모가 더 크므로 겉보기 진동수가 정지 진동수보다 낮아집니다. 분모 v<sub>sound</sub> – v<sub>source</sub>는 음원이 관측자를 향해 다가올 때 사용됩니다. 이 경우, 분모가 더 작으므로 겉보기 진동수가 정지 진동수보다 높아집니다. 이 공식을 사용하려면 속력의 단위가 동일해야 합니다."),
    ("The following table summarizes what would happen if a source that is creating a sound with a\n                        frequency of 600 Hz is moving in different ways.",
     "다음 표는 600 Hz의 진동수로 소리를 내는 음원이 다른 방식으로 움직일 때 어떤 일이 일어나는지 요약합니다."),

    # Doppler summary table
    (">Movement of sound source</th>", ">음원의 움직임</th>"),
    (">Frequency of sound created by source</th>", ">음원이 만든 소리의 진동수</th>"),
    (">Frequency heard by observer</th>", ">관측자가 듣는 진동수</th>"),
    ("Towards observer", "관측자를 향해 이동"),
    (" Higher than 600 Hz ", " 600 Hz보다 높음 "),
    (" Away from observer ", " 관측자로부터 멀어짐 "),
    (" Lower than 600 Hz ", " 600 Hz보다 낮음 "),
    (" Stationary ", " 정지 "),

    ("It is important to realize that the frequency of the source never changes. It is constant.\n                        The observer hears different frequencies, the apparent frequency, due to the Doppler effect.\n",
     "음원의 진동수는 절대 변하지 않는다는 것을 인식하는 것이 중요합니다. 그것은 일정합니다. 관측자는 도플러 효과로 인해 다른 진동수, 즉 겉보기 진동수를 듣게 됩니다.\n"),

    # Example: Calculating sound frequency
    ("<h3>Example: Calculating sound frequency</h3>", "<h3>예제: 소리의 진동수 계산</h3>"),
    ("A car is travelling down a highway at 27 m/s when the temperature of the air is 12°C. The\n                        driver sounds a 420 Hz horn when passing a stationary person at the side of the road. What\n                        frequency can the person hear when the car is approaching and when it is moving away?",
     "기온이 12°C일 때 자동차가 고속도로를 27 m/s로 달리고 있습니다. 운전자가 도로변에 서 있는 사람을 지나갈 때 420 Hz의 경적을 울립니다. 자동차가 다가올 때와 멀어질 때 그 사람이 들을 수 있는 진동수는 얼마인가요?"),
    ("Step 1", "단계 1"),
    ("First find the speed of sound in air.", "먼저 공기 중 음속을 구합니다."),
    ("Step 2", "단계 2"),
    (" <em>f<sub>1</sub></em> = 420 Hz\n                                    (frequency of source), <em>f<sub>2</sub></em> is the frequency heard by the observer. Use the minus\n                                    sign in the formula when the source is approaching, and the plus sign when it is moving away.",
     " <em>f<sub>1</sub></em> = 420 Hz\n                                    (음원의 진동수), <em>f<sub>2</sub></em>는 관측자가 듣는 진동수입니다. 음원이 다가올 때는 공식에서 빼기 부호를, 멀어질 때는 더하기 부호를 사용합니다."),
    ("Step 3", "단계 3"),
    ("<p>Approaching:</p>", "<p>다가올 때:</p>"),
    ("<p>Moving away:</p>", "<p>멀어질 때:</p>"),
    ("Step 4", "단계 4"),
    ("The person will hear a frequency of 460 Hz as the driver approaches, and 390 Hz as the driver moves\n                                    away. (Answers to 2 significant figures.)",
     "그 사람은 운전자가 다가올 때 460 Hz의 진동수를, 멀어질 때 390 Hz의 진동수를 듣게 됩니다. (유효 숫자 2자리로 답.)"),
    ("This makes sense because we know the frequency sounds higher when the source is\n                                    approaching the observer.",
     "음원이 관측자에게 다가올 때 진동수가 더 높게 들린다는 것을 알고 있으므로 이것은 타당합니다."),

    # Try it - Doppler questions
    ("Now try the following questions in your notebook.\n", "다음 문제를 노트에 풀어 보세요.\n"),
    ("1. In the following diagram, will a person at point \"A\" hear a higher or lower\n                                frequency than 350 Hz? Why?",
     "1. 다음 그림에서 점 \"A\"에 있는 사람은 350 Hz보다 높은 진동수를 들을까요, 낮은 진동수를 들을까요? 그 이유는?"),
    ("The ambulance is moving toward the observer, so they will hear a sound with a higher frequency.", "구급차가 관측자를 향해 이동하고 있으므로, 그들은 더 높은 진동수의 소리를 듣게 됩니다."),
    ("2. What would the ambulance have to be doing so the person will hear a frequency\n                                equal to 350 Hz?",
     "2. 그 사람이 350 Hz와 같은 진동수를 듣기 위해서는 구급차가 어떤 상태여야 하나요?"),
    ("The ambulance would have to be at rest (not moving). Alternatively, both the ambulance and the\n                                    observer could be moving in the same direction at the exact same speed, resulting in no difference in\n                                    their speeds.",
     "구급차가 정지해 있어야(움직이지 않아야) 합니다. 또는 구급차와 관측자가 정확히 같은 속력으로 같은 방향으로 이동하여 속력 차이가 없어야 합니다."),
    ("3. A car horn has a frequency of 480 Hz and the car is moving at 25 m/s. The speed of\n                                sound in air is 334 m/s. Find the apparent frequency detected by an observer when\n                                the car is moving away from them.",
     "3. 자동차 경적의 진동수는 480 Hz이고 자동차는 25 m/s로 이동하고 있습니다. 공기 중 음속은 334 m/s입니다. 자동차가 관측자로부터 멀어질 때 관측자가 감지하는 겉보기 진동수를 구하세요."),
    ("The observer will detect a frequency of 450 Hz.", "관측자는 450 Hz의 진동수를 감지하게 됩니다."),
    ("4. A racing car on a straight track sounds a 510 Hz horn during a promotion. The car\n                                is moving at 42 m/s and the temperature is 28°C. Find the apparent frequency of the\n                                horn for a stationary observer when the car is moving toward the observer.",
     "4. 직선 트랙의 레이싱 카가 홍보 행사 중 510 Hz 경적을 울립니다. 자동차는 42 m/s로 이동하고 온도는 28°C입니다. 자동차가 관측자를 향해 이동할 때 정지한 관측자에 대한 경적의 겉보기 진동수를 구하세요."),
    ("First, find the speed of sound.", "먼저, 음속을 구합니다."),
    ("Using that speed, apply the Doppler effect.\n", "그 속력을 사용하여 도플러 효과를 적용합니다.\n"),
    ("The observer will detect a frequency of 580 Hz.", "관측자는 580 Hz의 진동수를 감지하게 됩니다."),
    ("5. A truck sounds its 450 Hz horn while moving towards a stationary person. The\n                                person hears a frequency of 465 Hz. The speed of sound is 340 m/s. How fast is the\n                                truck moving?",
     "5. 트럭이 정지한 사람을 향해 이동하면서 450 Hz 경적을 울립니다. 그 사람은 465 Hz의 진동수를 듣습니다. 음속은 340 m/s입니다. 트럭은 얼마나 빠르게 이동하고 있나요?"),
    ("The truck is moving at 11 m/s.", "트럭은 11 m/s로 이동하고 있습니다."),

    # Applications of sound waves
    ("<h2>Applications of sound waves</h2>", "<h2>음파의 응용</h2>"),
    ("There are many applications of sound waves. Some that you will learn about are: ultrasound,\n                        acoustics, echolocation in animals, echoes, and sonar.",
     "음파에는 많은 응용이 있습니다. 여러분이 배울 것들 중 일부는: 초음파, 음향학, 동물의 반향 정위, 메아리, 그리고 소나입니다."),

    # Ultrasound
    ("<h3>Ultrasound</h3>", "<h3>초음파</h3>"),
    ("Recall that ultrasonic waves are sound waves with frequencies of over 20,000 Hz. This makes\n                        them inaudible to the human ear. These sound waves carry energy that can be absorbed by\n                        materials, as well as reflected. Ultrasound can be used to produce images of structures\n                        inside the human body. The procedure is fundamentally similar to sonar. A transducer emits\n                        the ultrasonic sound waves and a microphone detects the reflected waves. ",
     "초음파는 20,000 Hz 이상의 진동수를 가진 음파라는 것을 기억하세요. 이 때문에 인간의 귀에는 들리지 않습니다. 이 음파는 물질에 의해 흡수되거나 반사될 수 있는 에너지를 운반합니다. 초음파는 인체 내부 구조의 이미지를 생성하는 데 사용될 수 있습니다. 이 절차는 근본적으로 소나와 유사합니다. 변환기가 초음파를 방출하고 마이크가 반사된 파동을 감지합니다. "),
    ("Ultrasonic sound waves are more likely to pass through less dense material in the human body,\n                        like skin, with very little of the wave's energy being reflected. Denser materials, like\n                        bone, reflect ultrasonic waves more readily. A computer is used to calculate distances,\n                        using the reflected waves, and this process results in an image being formed. Ultrasonic\n                        waves have an added advantage over X-rays (a form of high-energy light) because they have no\n                        side effects when used to form an image.",
     "초음파는 피부와 같이 밀도가 낮은 인체 물질을 더 쉽게 통과하며, 파동의 에너지가 거의 반사되지 않습니다. 뼈와 같이 밀도가 높은 물질은 초음파를 더 쉽게 반사합니다. 컴퓨터를 사용하여 반사파를 이용해 거리를 계산하며, 이 과정으로 영상이 형성됩니다. 초음파는 영상을 형성할 때 부작용이 없기 때문에 X선(고에너지 빛의 한 형태)에 비해 추가적인 장점이 있습니다."),
    ("Ultrasounds can also be used in several forms to treat injury and illness. If high-energy\n                        ultrasound waves are used, then enough energy can be absorbed by human tissue to cause it to\n                        heat up. This increase in temperature of the muscle tissue can help relieve pain, promote\n                        healing for injured or overextended muscles, and even break down scar tissue. Care must be\n                        used with this form of treatment to make sure that overheating doesn't cause any damage.",
     "초음파는 부상과 질병을 치료하는 데에도 여러 형태로 사용될 수 있습니다. 고에너지 초음파를 사용하면 인체 조직이 가열될 만큼 충분한 에너지가 흡수될 수 있습니다. 근육 조직의 온도 증가는 통증을 완화하고, 부상을 입거나 과도하게 늘어난 근육의 치유를 촉진하며, 흉터 조직을 분해하는 데도 도움이 됩니다. 과열로 인한 손상이 발생하지 않도록 이 형태의 치료에는 주의가 필요합니다."),
    ("These high-energy ultrasound waves can destroy unwanted material in the body, when focused on\n                        a particular area. For example, painful gall and kidney stones can be shattered using this\n                        method of treatment.",
     "이 고에너지 초음파는 특정 부위에 집중하면 체내의 원치 않는 물질을 파괴할 수 있습니다. 예를 들어, 고통스러운 담석과 신장 결석을 이 치료 방법으로 분쇄할 수 있습니다."),

    # Acoustics
    ("<h3>Acoustics</h3>", "<h3>음향학</h3>"),
    ("When music is played in an auditorium or hall, some of the sound produced reflects off the\n                        walls and ceiling to form an echo. How the sound reflects off the walls partly determines\n                        the sound quality in the room. The properties of a room that affect sound quality are called\n                        acoustics. There are many things that can affect the acoustics in a room, such as the shape\n                        and size of the room, the furniture, the people, the floor covering, the materials on the\n                        walls, and so on. All of these things help to determine the acoustics in a room because they\n                        all affect the way that sound is reflected. In a large, empty room echoes are very\n                        noticeable. However, if a few rugs and curtains are added, the echoes are lessened and the\n                        acoustics improve.",
     "강당이나 홀에서 음악을 연주하면, 발생한 소리의 일부가 벽과 천장에서 반사되어 메아리를 형성합니다. 소리가 벽에서 어떻게 반사되는지가 방의 음질을 부분적으로 결정합니다. 음질에 영향을 미치는 방의 특성을 음향이라 합니다. 방의 모양과 크기, 가구, 사람, 바닥재, 벽의 재료 등 방의 음향에 영향을 미칠 수 있는 것들이 많습니다. 이 모든 것들이 소리가 반사되는 방식에 영향을 미치기 때문에 방의 음향을 결정하는 데 도움이 됩니다. 크고 빈 방에서는 메아리가 매우 두드러집니다. 그러나 몇 개의 깔개와 커튼을 추가하면 메아리가 줄어들고 음향이 개선됩니다."),
    ("However, when it comes to music, sound can seem flat and boring if there are no echoes at\n                        all. Ideally, you want the sound to come directly from the stage, with several early\n                        reflections directed at the audience. This will give the sound depth and character.\n                        Subsequent reflections should be minimized to improve sound quality.",
     "그러나 음악의 경우, 메아리가 전혀 없으면 소리가 평탄하고 지루하게 느껴질 수 있습니다. 이상적으로는 소리가 무대에서 직접 나오고, 몇 개의 초기 반사가 관객에게 향하기를 원합니다. 이것이 소리에 깊이와 특성을 부여합니다. 음질을 향상시키기 위해 이후의 반사는 최소화해야 합니다."),
    ("Acoustics in a hall are used to make sure that everyone can hear clearly and to improve sound\n                        quality. In a well-designed concert hall, the audience can only hear the music a second or\n                        two after it is played, due to the echoes. This is called the reverberation time.\n                        Reverberation time is the most important factor in determining sound quality in a concert\n                        hall.",
     "홀의 음향은 모든 사람이 명확하게 들을 수 있고 음질을 향상시키는 데 사용됩니다. 잘 설계된 콘서트 홀에서 관객은 메아리로 인해 음악이 연주된 후 1~2초 후에만 들을 수 있습니다. 이를 잔향 시간이라 합니다. 잔향 시간은 콘서트 홀에서 음질을 결정하는 가장 중요한 요소입니다."),

    # Echolocation
    ("<h3>Echolocation in animals</h3>", "<h3>동물의 반향 정위</h3>"),
    ("Dolphins, orca whales, and even bats often have to hunt in the dark, where they can't see\n                        their prey. To help them, they make sounds that echo off the prey in order to determine the\n                        prey's location.",
     "돌고래, 범고래, 심지어 박쥐도 종종 먹잇감을 볼 수 없는 어둠 속에서 사냥해야 합니다. 이를 돕기 위해 먹잇감에서 반사되는 소리를 내어 먹잇감의 위치를 파악합니다."),
    ("Dolphins use nasal sacs and an organ called a melon to help them locate their prey, as\n                        indicated in the following diagram. The nasal sacs are used to make high-frequency sounds\n                        that pass through the melon. The melon focuses the sound wave in a beam, in front of the\n                        dolphin. When these sound waves bounce off a fish that is swimming just ahead of the\n                        dolphin, the echo gives its location away. The dolphin detects the echo through its lower\n                        jaw. Orca whales and bats use similar methods for detecting prey.",
     "돌고래는 다음 그림에 나타난 것처럼 비강낭과 멜론이라 불리는 기관을 사용하여 먹잇감의 위치를 파악합니다. 비강낭은 멜론을 통과하는 고주파 소리를 만드는 데 사용됩니다. 멜론은 돌고래 앞쪽에서 음파를 빔으로 집중시킵니다. 이 음파가 돌고래 바로 앞에서 헤엄치는 물고기에 반사되면, 메아리가 그 위치를 알려줍니다. 돌고래는 아래턱을 통해 메아리를 감지합니다. 범고래와 박쥐도 먹잇감을 탐지하는 데 유사한 방법을 사용합니다."),

    # Echoes
    ("<h3>Echoes</h3>", "<h3>메아리</h3>"),
    ("You learned that waves can be reflected back into the medium through which they are\n                        travelling. Sound waves can do this as well. An easy way to detect this effect is to go into\n                        a large, open area with a large, hard, flat surface, like a cliff or big flat wall, nearby.\n                        If a person yells, the sound will travel away from you in all directions. The sound that\n                        hits the large flat surface will reflect back towards you and you will hear the person's\n                        yell again. The sound that is reflected back is called an echo.",
     "파동이 이동하고 있는 매질로 다시 반사될 수 있다는 것을 배웠습니다. 음파도 마찬가지입니다. 이 효과를 감지하는 쉬운 방법은 절벽이나 큰 평평한 벽과 같은 크고 딱딱한 평평한 표면이 근처에 있는 넓고 개방된 장소로 가는 것입니다. 사람이 소리를 지르면 소리가 모든 방향으로 멀어집니다. 큰 평평한 표면에 부딪힌 소리가 다시 반사되어 그 사람의 외침을 다시 듣게 됩니다. 반사되어 돌아온 소리를 메아리라고 합니다."),
    ("You can detect an echo clearly if it reflects back to your position in a time greater than\n                        0.10 s. Otherwise, the time interval is too small and you will just think that the sound is\n                        the original sound you made. This means that the distance between you and the hard\n                        reflecting surface must be greater than about 17 m. Echoes can be used to find the distance\n                        from the source to the reflecting surface. If you know the speed of sound and you measure\n                        the time between the original sound and the echo, you can calculate the distance travelled\n                        by the sound. Since the sound has to travel to the reflecting surface and then back, this\n                        distance represents twice the distance from the source to the reflecting surface. The following example\n                        illustrates how to solve one of these problems.",
     "메아리가 0.10초보다 긴 시간 내에 당신의 위치로 반사되면 명확하게 감지할 수 있습니다. 그렇지 않으면 시간 간격이 너무 작아서 원래 만든 소리라고 생각할 것입니다. 이는 당신과 딱딱한 반사면 사이의 거리가 약 17 m보다 커야 한다는 것을 의미합니다. 메아리는 음원에서 반사면까지의 거리를 구하는 데 사용할 수 있습니다. 음속을 알고 원래 소리와 메아리 사이의 시간을 측정하면 소리가 이동한 거리를 계산할 수 있습니다. 소리가 반사면까지 이동한 후 다시 돌아와야 하므로, 이 거리는 음원에서 반사면까지 거리의 두 배를 나타냅니다. 다음 예제는 이러한 문제를 푸는 방법을 보여줍니다."),

    # Example: Echoes
    ("<h3>Example: Echoes</h3>", "<h3>예제: 메아리</h3>"),
    ("A person yells and hears the echo off a cliff 2.5 s later. The speed of sound in air is 344\n                        m/s. Find the distance from the person to the cliff.",
     "한 사람이 소리를 지르고 2.5초 후에 절벽에서 반사된 메아리를 듣습니다. 공기 중 음속은 344 m/s입니다. 그 사람에서 절벽까지의 거리를 구하세요."),
    (">Show Suggested Answer<", ">풀이 보기<"),
    ("First find the total distance.", "먼저 총 거리를 구합니다."),
    ("Since the sound waves moved from the person, to the cliff, and back to their ears, this distance is\n                            double the distance from the person to the cliff.",
     "음파가 사람에서 절벽까지, 그리고 다시 귀로 돌아왔으므로, 이 거리는 사람에서 절벽까지 거리의 두 배입니다."),
    ("Therefore,", "따라서,"),
    ("The distance from the person to the cliff is 430 m.", "그 사람에서 절벽까지의 거리는 430 m입니다."),

    # Sonar
    ("<h3>Sonar</h3>", "<h3>소나</h3>"),
    ("Sonar stands for sound navigation and ranging. Typically, devices of this type are used by\n                        large ships. The ship has a transducer (a transmitter of sound) at the bottom that produces\n                        sound waves directed down towards the sea bed. ",
     "소나는 음파 탐지기(sound navigation and ranging)의 약자입니다. 일반적으로 이러한 유형의 장치는 대형 선박에 사용됩니다. 선박 하부에 변환기(소리 송신기)가 있어 해저를 향해 아래로 향하는 음파를 생성합니다. "),
    ("These sound waves reflect off objects below the surface (such as fish) and off the sea floor,\n                        and are detected by a microphone (a receiver of the sound). A computer then uses the speed\n                        of sound in water and the time for the echo to return to calculate the depth of the various\n                        objects below the water, using a solution similar to the echoes example. This information\n                        can then be converted into an image. These kinds of images can be used to locate schools of\n                        fish, sunken vessels, submarines, or just the depth of the water, as represented in the\n                        following diagrams.",
     "이 음파는 수면 아래의 물체(예: 물고기)와 해저에서 반사되어 마이크(소리 수신기)에 의해 감지됩니다. 그런 다음 컴퓨터가 물속의 음속과 메아리가 돌아오는 시간을 사용하여 메아리 예제와 유사한 방법으로 수면 아래 다양한 물체의 깊이를 계산합니다. 이 정보는 영상으로 변환될 수 있습니다. 이러한 종류의 영상은 다음 그림에 나타난 것처럼 물고기 떼, 침몰된 선박, 잠수함, 또는 단순히 수심을 파악하는 데 사용할 수 있습니다."),

    # Example: Sonar
    ("<h3>Example: Sonar</h3>", "<h3>예제: 소나</h3>"),
    ("A fishing vessel sends out a signal towards the bottom of the ocean. It receives one echo\n                        back after 0.30 s and another after 0.80 s. One echo is from a school of fish and the other\n                        is from the ocean floor. If the speed of sound in this sea water is 1470 m/s, how far above the ocean floor\n                        are the fish?",
     "어선이 해저를 향해 신호를 보냅니다. 0.30초 후에 하나의 메아리를, 0.80초 후에 또 다른 메아리를 수신합니다. 하나의 메아리는 물고기 떼에서, 다른 하나는 해저에서 온 것입니다. 이 바닷물에서의 음속이 1470 m/s라면, 물고기는 해저 위 얼마나 높은 곳에 있나요?"),
    (">Suggested\n                        Answer<", ">풀이\n                        보기<"),
    ("The distance between the fish and the floor is ", "물고기와 해저 사이의 거리는 "),
    ("Each given time is twice the time to the object, since the sound reflects back.\n                            Distance from boat to fish:", "각 주어진 시간은 소리가 반사되어 돌아오므로 물체까지의 시간의 두 배입니다.\n                            배에서 물고기까지의 거리:"),
    ("Distance from boat to ocean floor:", "배에서 해저까지의 거리:"),
    ("The difference between the two is", "둘의 차이는"),
    ("The fish are 370 m above the ocean floor.", "물고기는 해저 위 370 m에 있습니다."),

    # Consolidation
    ("<h2>Connect your understanding</h2>", "<h2>이해를 연결하기</h2>"),
    ("Let's revisit the first activity. You could hear your partner's voice because both the cups\n                        and the string vibrate to transmit the sounds that originated with the vocal cords. You have\n                        learned about the transmission and perception of sounds in this learning activity. ",
     "첫 번째 활동을 다시 살펴봅시다. 컵과 실 모두가 진동하여 성대에서 시작된 소리를 전달하기 때문에 상대방의 목소리를 들을 수 있었습니다. 이 학습 활동에서 소리의 전달과 인지에 대해 배웠습니다. "),
    ("You will now connect what you have learned about sounds and hearing, by learning how to\n                        minimize the risks of hearing loss in our lifetime.",
     "이제 청력 손실의 위험을 최소화하는 방법을 배움으로써 소리와 청각에 대해 배운 내용을 연결할 것입니다."),
    ("<h3>Read</h3>", "<h3>읽기</h3>"),
    ("Examine the following articles: ", "다음 자료를 살펴보세요: "),
    (">Government of\n                                    Canada - Noise-induced hearing loss<", ">캐나다 정부 - 소음성 난청<"),
    ("Opens in a new window", "새 창에서 열림"),
    (">Government of\n                                    Canada - Personal stereo systems and the risk of hearing loss<", ">캐나다 정부 - 개인 스테레오 시스템과 청력 손실의 위험<"),
    ("Part of having a positive digital footprint includes sharing information that you learn and\n                        think others should know. In this way you are contributing positively to your online\n                        community. You have now studied the issue of noise-induced hearing loss. ",
     "긍정적인 디지털 발자국을 갖는 것의 일부는 배운 정보를 공유하고 다른 사람들이 알아야 한다고 생각하는 것을 나누는 것입니다. 이렇게 하면 온라인 커뮤니티에 긍정적으로 기여하게 됩니다. 지금까지 소음성 난청 문제를 학습했습니다. "),
    ("Using a web-based tool or a word processor, practice having a positive footprint by\n                                creating a meme (an image and statement combination) that could be shared on social\n                                media to help educate others on the risks or measures that they could take to\n                                protect themselves.",
     "웹 기반 도구나 워드 프로세서를 사용하여, 소셜 미디어에서 공유할 수 있는 밈(이미지와 문구의 조합)을 만들어 다른 사람들에게 위험이나 자신을 보호할 수 있는 조치에 대해 교육하는 데 도움이 되도록 긍정적인 디지털 발자국을 실천하세요."),
    ("Compare your meme to some of the following that can be found on the web: ", "여러분의 밈을 웹에서 찾을 수 있는 다음의 것들과 비교해 보세요: "),

    # Final notebook section
    ("<h4>Ongoing task: Course formula sheet</h4>", "<h4>지속 과제: 과정 공식 목록</h4>"),
    ("Recall that after the first learning activity you were asked to identify and record\n                                the physics formulas used in the activity in your notebook.",
     "첫 번째 학습 활동 후 활동에 사용된 물리 공식을 노트에 식별하고 기록하라는 요청을 받았다는 것을 기억하세요."),
    ("You can add to the formulas under the heading:", "다음 제목 아래에 공식을 추가할 수 있습니다:"),
    ("<h4>Unit 1: Waves and sound</h4>", "<h4>단원 1: 파동과 소리</h4>"),
    ("Record the formulas presented in this learning activity.", "이 학습 활동에서 제시된 공식을 기록하세요."),
    ("Also, beside the formulas, record a short note stating in which situation you would\n                                use that equation. ",
     "또한 공식 옆에 그 공식을 어떤 상황에서 사용할 것인지 간단한 메모를 기록하세요. "),
    ("For example:", "예시:"),
    ("Use to find speed of wave. ", "파동의 속력을 구하는 데 사용. "),
    ("Speed = Wavelength &times; Frequency", "속력 = 파장 &times; 진동수"),
    ("Variables: speed, frequency, and wavelength.", "변수: 속력, 진동수, 파장."),
    ("You can add to your notes as well, to help you consider when to use it and how to use\n                                it.",
     "언제, 어떻게 사용할지 생각하는 데 도움이 되도록 노트에 추가할 수도 있습니다."),
    ("Additionally, verify that you have updated the vocabulary list you created at the\n                                start of this learning activity. Make sure you have a good understanding of the\n                                meaning and use of each word in the context of the physics of sound. ",
     "또한 이 학습 활동 시작 시 작성한 어휘 목록을 업데이트했는지 확인하세요. 음파의 물리학 맥락에서 각 단어의 의미와 용법을 잘 이해하고 있는지 확인하세요. "),

    # Self-check quiz
    ("<h3>Self-check quiz</h3>", "<h3>자기 점검 퀴즈</h3>"),
    ("<h4>Check your understanding!</h4>", "<h4>이해도를 확인하세요!</h4>"),
    ("Complete the following self-check quiz to determine where you are in your learning and what areas you\n                                need to focus on.",
     "다음 자기 점검 퀴즈를 완료하여 학습 현황과 집중해야 할 영역을 파악하세요."),
    ("This quiz is for feedback only, not part of your grade. You have unlimited attempts on this quiz. Take\n                                your time, do your best work, and reflect on any feedback provided.",
     "이 퀴즈는 피드백용이며, 성적에 포함되지 않습니다. 이 퀴즈에 대한 시도 횟수는 무제한입니다. 시간을 갖고 최선을 다하며, 제공된 피드백을 반영하세요."),
    ("Press <strong>Quiz</strong> to access this tool.", "<strong>퀴즈</strong> 버튼을 눌러 이 도구에 접속하세요."),
    ("(opens in a new window)", "(새 창에서 열림)"),

    # Warning noscript
    ("<strong>Warning!</strong> To ensure the greatest educational experience, this learning activity\n                contians aspects that require Javascript to be enabled.",
     "<strong>경고!</strong> 최상의 교육 경험을 보장하기 위해, 이 학습 활동에는 자바스크립트가 활성화되어야 하는 요소가 포함되어 있습니다."),

    # Misc standalone words/phrases in table cells and small texts
    ("<p><strong>Given:</strong></p>", "<p><strong>주어진 값:</strong></p>"),
    ("<p><strong>Given:</strong>", "<p><strong>주어진 값:</strong>"),
    ("<strong>Given:</strong>", "<strong>주어진 값:</strong>"),
    ("<p><strong>Unknown:</strong></p>", "<p><strong>구하는 값:</strong></p>"),
    ("<strong>Unknown:</strong>", "<strong>구하는 값:</strong>"),
    ("<p><strong>Equation:</strong></p>", "<p><strong>공식:</strong></p>"),
    ("<strong>Equation:</strong>", "<strong>공식:</strong>"),
    ("<p><strong>Solve:</strong></p>", "<p><strong>풀이:</strong></p>"),
    ("<strong>Solve:</strong>", "<strong>풀이:</strong>"),
    ("<p><strong>Statement:</strong></p>", "<p><strong>결론:</strong></p>"),
    ("<strong>Statement:</strong>", "<strong>결론:</strong>"),

    # Sound travels in various materials section
    ("Sound may also travel in solids and liquids. For example, if you are swimming underwater, you\n                        can still hear sounds.",
     "소리는 고체와 액체에서도 전달됩니다. 예를 들어, 수중에서 수영할 때도 여전히 소리를 들을 수 있습니다."),
    ("During a lightning storm, you first observe the flash of lightning in the distance, and then you hear it.\n                        The reason for this is that the light from the lightning bolt travels at the speed of light (300,000,000\n                        m/s), while the speed of sound is much slower. People don't normally think of sound as being slow. In fact,\n                        it is only slow when compared to the speed of light.",
     "번개 폭풍 동안 먼저 멀리서 번개의 섬광을 관찰한 후 소리를 듣게 됩니다. 이는 번개의 빛이 빛의 속력(300,000,000 m/s)으로 이동하는 반면, 음속은 훨씬 느리기 때문입니다. 사람들은 보통 소리가 느리다고 생각하지 않습니다. 사실, 빛의 속력과 비교할 때만 느린 것입니다."),

    # sr-only text
    ('<span class="sr-only">(Opens in new window)</span>', '<span class="sr-only">(새 창에서 열림)</span>'),
    ('<span class="sr-only">Opens in a new window</span>', '<span class="sr-only">새 창에서 열림</span>'),

    # Suggested Answer buttons - various patterns
    ("Suggested\n                                Answer", "풀이\n                                보기"),
    ("Suggested\n                        Answer", "풀이\n                        보기"),
    ("Show Suggested Answer", "풀이 보기"),
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
    translate_file('course_content/lessons/sph3u_u1la2.html')
