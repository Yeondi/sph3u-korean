/* Chapters 4–10. Loaded after content.js; existing question IDs remain unchanged. */
(() => {
  const lab = window.ENGLISH_LAB;
  lab.chapters.push(
    {
      id:4, title:'부정문과 의문문', subtitle:'무엇을 부정하고 무엇을 묻는지 먼저 정하기',
      goal:'be·조동사·일반동사를 구별하고, 직접 질문과 문장 안의 질문을 다른 어순으로 만듭니다.',
      concepts:[
        ['왜 동사부터 확인하나요?', '한국어는 문장 끝과 억양으로 질문을 만들기 쉽지만 영어는 주어 앞에 나오는 동사·조동사가 중요합니다. Is it ready? / Can you help? / Do you need help?처럼 먼저 본동사와 조동사가 무엇인지 확인하세요. 회화의 You’re coming? 같은 확인 질문도 있지만 기본 의문문부터 안정적으로 만듭니다.'],
        ['부정문을 만드는 세 갈래', 'be는 is not, 조동사는 cannot·will not, 일반동사의 단순현재·과거는 do/does/did not + 원형입니다. She does not drive.에서는 시제와 주어 일치를 does가 담당합니다. She does not drives.처럼 중복 표시하지 않습니다.'],
        ['무엇을 묻는가에 따라', 'What did you buy?에서는 목적어를 묻기 때문에 did를 씁니다. Who called you?는 주어 자체를 물으므로 보통 do를 추가하지 않습니다. 주어 의문문의 who도 단수·복수 상황에 따라 달라질 수 있지만, 단독 who에는 보통 단수 동사를 씁니다.'],
        ['간접의문문은 평서문 어순', 'Where is the office?를 Do you know where the office is?로 넣으면 내부는 주어 + 동사 순서입니다. 예/아니요 질문은 if 또는 whether로 연결합니다. I wonder whether it is open.은 의문 내용을 담은 평서문이라 문장 끝에 반드시 물음표를 쓰지는 않습니다.'],
        ['부정의 범위와 응답', 'I don’t think it will work.는 내 판단을 완곡하게 부정합니다. Not everyone agrees.는 모두가 동의하는 것은 아니라는 뜻이며 Nobody agrees.와 다릅니다. Don’t you need it?에 Yes, I do.는 필요하다는 뜻입니다. 한국어 ‘네/아니요’를 그대로 대응시키지 말고 긍정·부정 내용을 덧붙이세요.']
      ],
      comparisons:[['Does she drives?','Does she drive?','does 뒤에는 동사원형입니다.'],['Do you know where is it?','Do you know where it is?','문장 안의 의문절은 주어 + 동사 순서입니다.'],['Who did called you?','Who called you?','주어를 묻는 보통 질문에는 did를 넣지 않습니다.']],
      analyses:[
        [['Did','조동사','과거 질문 표시'],['you','주어','질문받는 사람'],['receive','본동사','원형'],['my message','목적어','받았는지 묻는 대상']],
        [['Could','조동사','정중한 질문'],['you','주어','듣는 사람'],['tell','본동사','알려주다'],['me','목적어','정보를 받는 사람'],['when the store closes','의문절','when + 주어 + 동사']],
        [['Not everyone','주어','모든 사람이 그런 것은 아님'],['agrees','동사','단수 everyone과 일치'],['with the plan','전치사구','동의 대상']]
      ],
      checklist:['일반동사 질문·부정에서 do 뒤를 원형으로 바꿨는가?','문장 안의 질문은 주어 + 동사 어순인가?','무엇을 부정하는지와 대답의 긍정·부정이 명확한가?']
    },
    {
      id:5, title:'조동사와 태도 표현', subtitle:'능력·가능성·의무·정중함을 구별하기',
      goal:'같은 행동이라도 확신의 정도와 상대에게 요구하는 강도에 맞게 표현합니다.',
      concepts:[
        ['조동사는 말하는 사람의 태도', 'He can drive.는 능력, He might drive.는 가능성입니다. 한국어의 ‘~할 수 있다’가 능력인지 가능성인지 먼저 구별하세요. can/could/may/might/must/should/will/would 뒤에는 보통 to 없이 동사원형이 옵니다. have to는 형태가 달라 does he have to, had to처럼 변합니다.'],
        ['could와 would는 과거만이 아닙니다', 'Could you help me?는 지금의 정중한 부탁입니다. Would you like some tea?는 제안입니다. would를 무조건 과거의 will로 해석하면 현재 대화의 의도를 놓칩니다. 친한 사이의 Can you…?도 자연스럽고 정중함은 억양·관계·요청 부담에도 달려 있습니다.'],
        ['의무와 금지를 구별하기', 'must/have to는 강한 필요나 의무에 쓰입니다. mustn’t는 금지, don’t have to는 필요 없음입니다. You don’t have to come.은 와도 되지만 의무는 아니라는 뜻입니다. must는 내적 의무, have to는 외적 의무라는 구분은 경향일 뿐 항상 적용되는 법칙은 아닙니다.'],
        ['가능성과 추론', 'may/might/could는 가능성을 나타내지만 고정된 확률 숫자로 대응시키지 않습니다. He must be busy.는 강한 추론, He can’t be at home.은 그럴 리 없다는 추론입니다. must not은 맥락에 따라 부정적 추론일 수도 있으므로 무조건 금지로만 읽지 않습니다.'],
        ['조언·지난 일에 대한 판단', 'should는 조언이나 기대입니다. should have + 과거분사는 하지 못한 일을 돌아보는 후회·비판에 자주 쓰고, might have + 과거분사는 지난 일의 가능성을 말합니다. I should have checked.와 I had to check.는 각각 돌아보는 판단과 과거의 의무입니다.']
      ],
      comparisons:[['You mustn’t attend. (참석은 선택이라는 의도)','You don’t have to attend.','mustn’t는 참석 금지처럼 들립니다.'],['Could you to wait?','Could you wait?','조동사 뒤에는 동사원형입니다.'],['I should checked it.','I should have checked it.','과거의 하지 못한 일을 돌아보려면 have + 과거분사를 씁니다.']],
      analyses:[
        [['You','주어','조언을 받는 사람'],['should check','조동사 + 본동사','확인을 권함'],['the deadline','목적어','확인할 대상']],
        [['We','주어','의무가 없는 사람들'],['do not have to pay','동사구','지불할 필요 없음'],['today','시간 정보','현재 의무의 범위']],
        [['I','주어','추측하는 사람의 문장 주어'],['might have left','조동사 완료형','과거 행동의 가능성'],['my keys','목적어','두고 온 물건'],['at home','장소','추정하는 위치']]
      ],
      checklist:['능력·가능성·의무 중 어떤 의미인지 정했는가?','금지와 필요 없음을 혼동하지 않았는가?','조동사 뒤의 원형 또는 have + 과거분사가 맞는가?']
    },
    {
      id:6, title:'to부정사와 동명사', subtitle:'동사 두 개를 연결할 때 형태와 의미 고르기',
      goal:'앞 동사의 패턴을 확인하고, 기억·중단·시도처럼 형태에 따라 달라지는 의미를 구분합니다.',
      concepts:[
        ['한국어 ‘~하는 것’ 하나로 고르지 않기', 'I decided to leave. / I avoided driving.처럼 앞 동사가 뒤의 형태를 제한합니다. to는 미래, -ing는 과거라는 식으로 모든 용법을 단순화할 수 없습니다. 학습 사전에서 동사 + 뒤따르는 구조와 예문을 함께 확인하세요.'],
        ['자주 쓰는 결합', 'decide/hope/offer + to do, avoid/finish/consider + doing이 유용합니다. want someone to do처럼 사람 자리가 있는 구조도 구별합니다. 전치사 뒤에는 명사나 -ing가 올 수 있습니다: before leaving, interested in learning.'],
        ['to가 모두 부정사 표시는 아닙니다', 'look forward to meeting you와 be used to living alone에서 to는 전치사라 -ing를 받습니다. used to live는 예전에는 살았지만 지금은 보통 그렇지 않다는 과거 습관이고, be used to living은 익숙한 상태입니다.'],
        ['기억·중단의 의미 차이', 'Remember to lock the door.는 앞으로 해야 할 일을 잊지 말라는 뜻입니다. I remember locking it.는 잠갔던 기억입니다. stop talking은 말하기를 그만두는 것, stop to talk는 다른 행동을 멈추고 대화하는 것입니다.'],
        ['시도와 목적', 'try to restart는 재시동하려고 노력하는 것, try restarting은 해결 방법으로 재시동을 해 보는 것입니다. 실제 문맥에서 겹칠 때도 있습니다. I went outside to call her.의 to부정사는 목적이고 동사의 목적어가 아닙니다. 이름만 분류하기보다 무엇을 연결하는지 보세요.']
      ],
      comparisons:[['I look forward to meet you.','I look forward to meeting you.','이 결합의 to는 전치사입니다.'],['I finished to write the report.','I finished writing the report.','finish 뒤에 행동을 넣으면 -ing를 씁니다.'],['I stopped to smoke. (금연했다는 의도)','I stopped smoking.','stop to smoke는 다른 일을 멈추고 담배를 피우는 뜻입니다.']],
      analyses:[
        [['She','주어','제안한 사람'],['offered','동사','도움을 제안했다'],['to carry my bag','to부정사절','제안한 행동; bag은 carry의 목적어']],
        [['I','주어','기대하는 사람'],['look forward to','동사 + 전치사 결합','기대하다'],['working with you','-ing절','기대하는 활동']],
        [['We','주어','멈춘 사람들'],['stopped','동사','하던 일을 멈췄다'],['to get some coffee','목적의 to부정사절','왜 멈췄는지']]
      ],
      checklist:['앞 동사가 to do와 doing 중 어떤 형태를 받는가?','to가 전치사인지 부정사 표시인지 확인했는가?','형태를 바꿨을 때 기억·중단·시도의 의미가 달라지는가?']
    },
    {
      id:7, title:'전치사와 자연스러운 동사 결합', subtitle:'한국어 조사를 옮기지 않고 관계를 표현하기',
      goal:'의존 전치사·구동사·자주 쓰는 단어 조합을 문장 안에서 재사용합니다.',
      concepts:[
        ['전치사는 관계를 나타냅니다', 'at three는 시점, for three hours는 기간, by Friday는 늦어도 금요일까지 완료, until Friday는 그때까지 지속입니다. 한국어의 ‘~까지’만 보고 같은 단어를 고르면 의미가 달라집니다.'],
        ['의존 전치사는 함께 기억하기', 'depend on, apologize for, belong to, interested in처럼 앞말과 관습적으로 결합합니다. apologize to someone for something처럼 사람과 이유에 다른 전치사를 씁니다. 사전의 전체 예문을 살피세요.'],
        ['전치사가 없는 동사도 있습니다', 'reach the station, enter the room, discuss the issue는 대상을 바로 받습니다. arrive at the station, go into the room, talk about the issue와 구조가 다릅니다. 한국어 뜻이 비슷해도 결합 방식은 그대로 옮길 수 없습니다.'],
        ['구동사의 목적어 위치', 'turn off the light / turn the light off가 모두 가능하지만 대명사는 turn it off입니다. 모든 구동사가 분리되는 것은 아닙니다. look after the cat / look after it에서는 after 뒤에 목적어를 둡니다.'],
        ['관용적 결합과 문법', 'make a decision, take a break, do homework는 자연스러운 단어 조합입니다. 선택을 결정하는 보편 문법 공식이 따로 있는 것은 아닙니다. a homework처럼 관사를 잘못 붙이는 문제는 명사의 가산성에 관한 별도 문법 문제입니다.']
      ],
      comparisons:[['I arrived to the station.','I arrived at the station.','역 같은 지점에는 보통 arrive at을 씁니다. 도시·국가는 arrive in입니다.'],['Please turn off it.','Please turn it off.','분리 가능한 구동사의 대명사 목적어는 중간에 둡니다.'],['I am interested about robotics.','I am interested in robotics.','interested의 일반적인 결합은 in입니다.']],
      analyses:[
        [['I','주어','사과하는 사람'],['apologized','동사','과거의 사과'],['to my teammate','상대 전치사구','누구에게'],['for missing the meeting','이유 전치사구','무엇 때문에']],
        [['Please hand','명령문 동사','제출해 달라는 요청'],['it','목적어','앞서 언급한 과제'],['in','불변화사','hand in의 일부'],['by Friday','기한','늦어도 금요일까지']],
        [['We','주어','의견을 나누는 사람들'],['agree','동사','동의하다'],['with you','상대','누구의 의견에'],['on this point','주제','어떤 점에']]
      ],
      checklist:['동사에 필요한 전치사를 넣고 불필요한 전치사는 뺐는가?','기한 by와 지속 until을 구분했는가?','구동사 대명사 위치와 관용적인 단어 조합이 자연스러운가?']
    },
    {
      id:8, title:'접속사와 관계절', subtitle:'생각의 관계를 드러내며 문장 늘리기',
      goal:'이유·대조·조건·대상을 분명히 하면서 짧은 문장을 연결합니다.',
      concepts:[
        ['길이보다 관계가 먼저', 'because는 이유, so는 결과, although는 양보·대조입니다. 한국어 연결어를 하나씩 번역하지 말고 두 사실이 어떤 관계인지 정하세요. 한 문장이 너무 길어지면 둘로 나누어도 유창하고 자연스럽습니다.'],
        ['절과 구를 구별하기', 'because the bus was late는 주어와 동사가 있는 절입니다. because of the delay는 명사구를 받습니다. although it was raining과 despite the rain도 같은 방식으로 구별합니다. despite 뒤에는 -ing도 가능합니다.'],
        ['관계절로 대상을 특정하기', 'The student who sits next to me…에서 who절은 어떤 학생인지 알려 줍니다. the book that I borrowed에서는 that이 borrowed의 목적어이므로 목적어 it을 또 넣지 않습니다. 제한적 관계절의 목적격 관계사는 생략할 수 있습니다.'],
        ['필수 정보와 덧붙이는 정보', 'My friend who lives nearby…는 여러 친구 중 누구인지 특정할 수 있습니다. My friend Alex, who lives nearby, …는 이미 특정된 Alex에 정보를 덧붙입니다. 이런 비제한적 관계절은 쉼표를 쓰고 보통 that이나 관계사 생략을 쓰지 않습니다.'],
        ['상대가 따라올 수 있게', 'one point → reason → example 순으로 설명하면 도움이 됩니다. however는 접속부사이므로 정식 글에서 독립절 둘을 쉼표 하나로만 연결하지 않습니다. 말하기에서는 잠시 멈추고 새 문장으로 이어 가면 됩니다.'],
        ['시간절의 미래', 'I’ll call you when I arrive.에서 미래의 도착이지만 when절에는 단순현재를 씁니다. 이때 when은 ‘도착하면’이라는 시간절입니다. I don’t know when he will arrive.처럼 ‘언제 도착할지’라는 의문절과 구분하세요.']
      ],
      comparisons:[['Although it was late, but we continued.','Although it was late, we continued.','같은 대조를 although와 but으로 중복 연결하지 않습니다.'],['The book that I bought it is useful.','The book that I bought is useful.','관계사가 이미 목적어 역할을 하므로 it을 중복하지 않습니다.'],['Because of I was tired, I left.','Because I was tired, I left.','주어·동사가 있는 절은 because로 연결합니다.']],
      analyses:[
        [['Although the room is small','양보절','불리한 사실 인정'],['it','주절 주어','방을 가리킴'],['gets','동사','받다'],['plenty of natural light','목적어','장점을 나타내는 대상']],
        [['The charger','주어의 핵심 명사','충전기'],['that I borrowed','관계절','어떤 충전기인지 특정; borrowed의 목적어 자리'],['works','주절 동사','작동하다'],['well','부사','작동 상태']],
        [['I','주절 주어','연락할 사람'],['will text','주절 동사구','미래 행동'],['you','목적어','받는 사람'],['when I get home','시간절','집에 도착하면']]
      ],
      checklist:['이유·결과·대조에 맞는 연결어인가?','관계절 내부에서 주어·목적어를 중복하지 않았는가?','긴 문장 안에서도 주절의 주어와 동사가 명확한가?']
    },
    {
      id:9, title:'고급 문장 확장', subtitle:'가정·초점·전달 시점을 조절하기',
      goal:'조건문·수동태·간접화법을 의도에 맞게 사용하고 필요한 정보에 자연스럽게 초점을 줍니다.',
      concepts:[
        ['조건의 현실성과 시간', 'If it rains, we’ll stay inside.는 앞으로 일어날 수 있는 조건입니다. If I had more time, I would join you.는 지금의 상황과 거리를 둔 가정입니다. 과거형이 항상 과거 시간만 뜻하지 않습니다. 미래 가능성이 낮다고 느끼는 가정에도 씁니다.'],
        ['바꿀 수 없는 과거를 가정하기', 'If I had left earlier, I would have caught the bus.는 실제와 다른 과거를 상상합니다. 조건과 결과의 시간이 다르면 If I had slept better, I would feel better now.처럼 혼합할 수 있습니다. 모양만 외우지 말고 각각의 시간이 언제인지 먼저 정하세요.'],
        ['수동태는 정보의 초점', 'Someone repaired the heater.보다 The heater was repaired.가 난방 장치의 상태에 집중합니다. be + 과거분사로 만들고 행위자가 필요하면 by로 덧붙입니다. 자동사 arrive에는 이 방식의 수동태를 만들 수 없습니다. 수동태가 언제나 더 격식 있거나 더 좋은 문장은 아닙니다.'],
        ['간접화법은 지금 누구의 관점인가요?', 'She said, “I’m busy.”를 She said she was busy.처럼 옮길 수 있습니다. 시제·대명사·시간 표현은 전달하는 시점과 상황에 맞게 조정합니다. 지금도 참인 정보는 현재형을 유지하기도 하므로 모든 동사를 무조건 한 단계 과거로 바꾸지 않습니다. tell은 보통 말한 상대를 받지만 say는 상대 앞에 to를 씁니다.'],
        ['명확한 강조', 'I do understand.는 이해한다는 사실을 강조합니다. What I need is more practice.는 필요한 내용에 초점을 둡니다. 모든 문장을 강조 구문으로 만들면 오히려 부자연스럽습니다. 평범한 문장을 먼저 만들고 대조·정정할 부분만 강조하세요.'],
        ['가정법 표현의 선택', 'If I were you는 조언에서 흔한 표현입니다. 가정의 I/he/she에 were가 격식체에서 선호되지만 회화에서는 was도 쓰입니다. wish + 과거형은 현재의 아쉬움, wish + had + 과거분사는 과거의 아쉬움을 표현할 수 있습니다.']
      ],
      comparisons:[['If I will finish early, I’ll call you.','If I finish early, I’ll call you.','보통의 미래 조건절에는 단순현재를 씁니다. 의지 등을 나타내는 별도 will 용법과 구별합니다.'],['The heater repaired yesterday. (수리되었다는 의도)','The heater was repaired yesterday.','수동태에 be가 필요합니다.'],['She said me she was busy.','She told me she was busy.','tell + 사람 또는 say to + 사람입니다.']],
      analyses:[
        [['If I had a car','가정 조건절','현재와 거리를 둔 조건'],['I','주절 주어','결과 행동의 주인공'],['would visit','동사구','가정의 결과'],['more places','목적어','방문할 대상']],
        [['The schedule','주어','변경 대상'],['was updated','수동태 동사구','변경되었다'],['by the office','행위자','누가 변경했는지'],['this morning','시간 정보','끝난 사건의 시점']],
        [['What I need','주어 역할의 절','내가 필요로 하는 것'],['is','연결동사','두 부분을 연결'],['a clear explanation','주격 보어','강조하는 내용']]
      ],
      checklist:['조건과 결과가 각각 어느 시점인지 확인했는가?','수동태가 필요한 초점을 만들며 be + 과거분사 형태가 맞는가?','간접화법의 대명사·시제가 전달 상황과 맞는가?']
    },
    {
      id:10, title:'실전 응용과 자유 회화', subtitle:'한 문장에서 대화의 다음 턴으로',
      goal:'상황 설명 → 이유·입장 → 구체적 요청·후속 질문을 자신의 말로 연결합니다.',
      concepts:[
        ['자유 회화는 문장 암기에서 끝나지 않습니다', '먼저 전달할 핵심을 정하고 이유나 예를 한 가지 덧붙이세요. 상대가 무엇을 해 주면 좋은지도 분명히 하면 대화가 이어집니다. 이 장의 모범 답안은 가능한 대화 예시이며 그대로 외우거나 길이를 똑같이 맞출 필요는 없습니다.'],
        ['대화가 막혔을 때 복구하기', 'Could you put that another way?로 재설명을 요청하고, Do you mean…?으로 이해를 확인합니다. 이미 틀리게 말했으면 Sorry, I meant…로 바로잡으세요. 잠깐 멈추거나 쉬운 단어로 바꾸는 것도 실전 능력입니다.'],
        ['의견에는 근거와 여지를', 'I think… because…에 사례를 덧붙입니다. I see your point, but…은 인정 후 반론, I agree that…, although…는 일부 동의 후 제한입니다. 완곡어를 많이 넣기보다 실제로 동의하는 부분과 걱정하는 점을 구체적으로 말하세요.'],
        ['문제 설명과 해결 요청', 'The heater stopped working last night.로 사실을 말하고 Could someone take a look?로 요청합니다. 상대를 비난하는 단정 대신 관찰·영향·필요한 조치를 구별하세요. 모든 상황에서 간접 표현이 좋은 것은 아니며 급한 문제는 명확하고 짧게 말합니다.'],
        ['자연스러움의 판단 기준', '문법·의미·말투 외에 상대 말에 실제로 답했는지, 충분한 정보를 줬는지, 다음 질문이 가능한지 확인하세요. 자연스러운 회화는 반드시 복잡한 문장이나 어려운 단어를 많이 쓰는 것이 아닙니다. 이 도구는 자동 회화 상대나 음성 평가를 제공하지 않습니다.'],
        ['열린 답변과 후속 턴', '이 장의 말하기 문제는 2~3문장으로 답한 뒤, 답안 영역의 후속 질문에도 자기 경험으로 답해 보세요. 정해진 예시와 다른 사실을 골라도 됩니다. 5초는 짧은 첫 문장을 시작하는 훈련에만 쓰고, 여러 문장을 완성할 때는 제한 없음을 권합니다.']
      ],
      comparisons:[['Explain again. (처음 만난 교수에게 정중히 부탁하려는 의도)','Could you explain that part again?','첫 문장은 문법적으로 가능하지만 맥락에 따라 명령처럼 들릴 수 있습니다.'],['I am agree with you.','I agree with you.','agree는 일반동사라 be를 붙이지 않습니다.'],['I don’t understand anything. (특정 단계만 모르는 상황)','I understand the first step, but I’m not sure why we divide by two.','첫 문장도 문법적으로 맞지만 이해한 부분과 질문을 구체화하면 답을 받기 쉽습니다.']],
      analyses:[
        [['I understand the formula','첫 번째 절','이해한 범위 밝히기'],['but','접속사','대조'],['I’m not sure','두 번째 절의 중심','불확실함 표현'],['when to use it','의문사 + to부정사','모르는 내용 특정']],
        [['I’d prefer a smaller place','입장','선호 먼저 말하기'],['because','접속사','이유 연결'],['it would be easier to maintain','근거절','예상 장점 설명']],
        [['The tap has been leaking','문제 설명','지속되는 상태'],['since yesterday','시간 정보','시작점'],['Could you arrange a repair?','별도 요청 문장','구체적인 조치 요청']]
      ],
      checklist:['상대 질문이나 상황에 직접 답했는가?','이유·예시·요청을 필요한 만큼 구체적으로 덧붙였는가?','막혔을 때 다시 설명하거나 이해를 확인했는가?']
    }
  );
  lab.roadmap = [];
  function add(chapter, rows) {
    rows.forEach((row,index)=>{
      const [prompt,answer,pattern,explanation,error,alternative,transfer,transferAnswer]=row;
      lab.exercises.push({id:`c${chapter}-${index+1}`,chapter,mode:index<4?'build':index<8?'transform':'speak',prompt,answer,pattern,explanation,error,alternative,transfer,transferAnswer});
    });
  }
  add(4,[
    ['강의실이 아직 열리지 않았다고 말하세요.','The classroom is not open yet.','be + not + 보어','open은 여기서 열린 상태를 나타내는 형용사입니다.','The classroom does not open yet. → 이 상황의 상태를 말할 때는 is not open이 자연스럽습니다.','The classroom isn’t open yet.','프린터가 아직 준비되지 않았다고 말하세요.','The printer isn’t ready yet.'],
    ['어제 친구의 메시지를 받지 못했다고 말하세요.','I did not receive your message yesterday.','did not + 동사원형','과거 표시는 did가 담당합니다.','I didn’t received your message. → received가 아니라 receive입니다.','I didn’t get your message yesterday.','지난밤에 TV를 보지 않았다고 말하세요.','I didn’t watch TV last night.'],
    ['어떤 버스가 캠퍼스로 가는지 물으세요.','Which bus goes to campus?','주어 의문사구 + 동사','which bus가 주어이므로 일반적인 질문에 do를 추가하지 않습니다.','Which bus does goes to campus? → 주어 질문에 불필요한 does가 있습니다.','Which bus should I take to get to campus?','누가 이 문을 잠갔는지 직접 질문하세요.','Who locked this door?'],
    ['직원에게 신청서 제출처를 아는지 물으세요.','Do you know where I should submit this form?','Do you know + 의문사 + 주어 + 동사구','내부 질문은 I should submit 순서입니다.','Do you know where should I submit this form? → 내부에서 도치하지 않습니다.','Could you tell me where to submit this form?','친구에게 다음 수업이 언제 시작하는지 아는지 물으세요.','Do you know when the next class starts?'],
    ['She works on Fridays.를 예/아니요 질문으로 바꾸세요.','Does she work on Fridays?','Does + 주어 + 동사원형','3인칭 단수 표시가 works에서 does로 옮겨갑니다.','Does she works on Fridays? → work를 씁니다.','Does she usually work on Fridays? (평소 습관을 더 명시)','He needs a parking pass.를 질문으로 바꾸세요.','Does he need a parking pass?'],
    ['Where is the nearest bank?를 Could you tell me로 시작하는 질문으로 바꾸세요.','Could you tell me where the nearest bank is?','요청 의문문 + 의문절','전체 문장은 질문이지만 내부 where절은 평서문 어순입니다.','Could you tell me where is the nearest bank? → bank is 순서입니다.','Do you know where the nearest bank is?','What time does the library close?를 Do you know로 시작하세요.','Do you know what time the library closes?'],
    ['Is internet included?를 I’d like to know로 시작하는 문장으로 바꾸세요.','I’d like to know whether internet is included.','know + whether/if + 주어 + 동사','예/아니요 질문을 whether 또는 if로 연결합니다.','I’d like to know is internet included. → 연결어와 내부 어순을 바꿔야 합니다.','I’d like to know if internet is included.','Can I pay by card?를 I’d like to know로 시작하세요.','I’d like to know if I can pay by card.'],
    ['Everyone likes group work.를 ‘모두가 좋아하는 것은 아니다’로 바꾸세요.','Not everyone likes group work.','Not everyone + 단수 동사','일부는 좋아하지 않는다는 뜻이며 전원이 싫어한다는 뜻은 아닙니다.','Nobody likes group work. → 아무도 좋아하지 않는다는 더 강한 뜻입니다.','Some people don’t like group work.','모든 상점이 일요일에 여는 것은 아니라고 말하세요.','Not every store opens on Sundays.'],
    ['친구가 “Don’t you need your notes?”라고 묻습니다. 필요하다고 분명히 답하세요.','Yes, I do. I need them for class.','긍정 응답 + do + 내용 확인','부정형 질문이라도 필요하면 Yes, I do입니다.','No, I do. → 응답과 긍정 내용이 충돌합니다.','I do need them, thanks.','“Haven’t you submitted it?”에 아직 제출하지 않았다고 답하세요.','No, I haven’t. I’m still working on it.'],
    ['교수에게 과제에서 계산 과정을 보여 줘야 하는지 물으세요.','Do we need to show our calculations?','Do + 주어 + need to do','과제 요구사항을 확인하는 직접적인 질문입니다.','Are we need to show our calculations? → 일반동사 need에 do를 씁니다.','Should we show our calculations?','집주인에게 방문 전 약속을 잡아야 하는지 물으세요.','Do I need to make an appointment before visiting?'],
    ['식당 직원에게 견과류가 들어가는지 정중하게 물으세요.','Could you tell me whether this contains nuts?','Could you tell me + whether절','구체적인 재료를 확인하는 정보 질문입니다.','Could you tell me whether does this contain nuts? → whether 뒤에서 도치하지 않습니다.','Does this contain any nuts?','은행 직원에게 이 계좌에 월 수수료가 있는지 물으세요.','Could you tell me whether this account has a monthly fee?'],
    ['친구에게 방학 동안 무엇을 할 계획인지 물으세요.','What are you planning to do during the break?','What + be + 주어 + -ing','현재 계획하고 있는 내용을 질문합니다.','What you are planning to do? → 직접 의문문에서는 are you입니다.','What are your plans for the break?','친구가 왜 이 과정을 골랐는지 물으세요.','Why did you choose this program?']
  ]);
  add(5,[
    ['이번 주말에는 시간이 될 수도 있지만 아직 확실하지 않다고 말하세요.','I might be free this weekend, but I’m not sure yet.','might + 원형 + 불확실성','가능성을 열어 두되 약속으로 단정하지 않습니다.','I might am free. → be의 원형을 씁니다.','I may be available this weekend, but I haven’t decided yet.','내일 눈이 올 수도 있다고 말하세요.','It might snow tomorrow.'],
    ['내일은 교재를 가져올 필요가 없다고 말하세요.','You don’t have to bring the textbook tomorrow.','do not have to + 원형','필요 없다는 뜻이며 가져오는 것을 금지하지 않습니다.','You mustn’t bring the textbook. → 가져오지 말라는 금지에 가깝습니다.','You don’t need to bring the textbook tomorrow.','친구에게 지금 바로 대답할 필요는 없다고 말하세요.','You don’t have to answer right now.'],
    ['과제를 제출하기 전에 단위를 확인하는 게 좋겠다고 조언하세요.','You should check the units before submitting the assignment.','should + 원형','해야 할 행동에 대한 조언입니다. before 뒤는 -ing로 연결했습니다.','You should to check the units. → to 없이 원형입니다.','It’s a good idea to check the units before you submit it.','친구에게 버스 시간표를 미리 확인하라고 조언하세요.','You should check the bus schedule in advance.'],
    ['열쇠를 실습실에 두고 왔을지도 모른다고 말하세요.','I might have left my keys in the lab.','might have + 과거분사','과거에 일어났을 가능성을 추측합니다.','I might left my keys. → 과거 가능성에는 have left입니다.','Maybe I left my keys in the lab.','영수증을 버렸을지도 모른다고 말하세요.','I might have thrown away the receipt.'],
    ['Send me the slides.를 정중한 요청으로 바꾸세요.','Could you send me the slides, please?','Could you + 원형','could는 현재 부탁을 부드럽게 합니다.','Could you sent me the slides? → sent가 아닌 send입니다.','Would you mind sending me the slides?','창문을 닫아 달라는 문장을 정중한 요청으로 바꾸세요.','Could you close the window, please?'],
    ['I have to attend the orientation.을 어제의 의무로 바꾸세요.','I had to attend the orientation yesterday.','had to + 원형','과거의 의무를 had to로 나타냅니다.','I musted attend. → musted라는 과거형은 쓰지 않습니다.','I was required to attend the orientation yesterday. (더 격식 있음)','어제 일찍 일어나야 했다고 말하세요.','I had to get up early yesterday.'],
    ['I didn’t save a copy.에 ‘저장했어야 했는데’라는 후회를 담으세요.','I should have saved a copy.','should have + 과거분사','실제로 하지 않은 행동을 돌아봅니다.','I should save a copy. → 보통 지금이나 앞으로의 조언이지 과거 후회가 아닙니다.','I wish I had saved a copy.','예약 전에 후기를 확인했어야 했다고 말하세요.','I should have checked the reviews before booking.'],
    ['You can use your phone here.를 이 장소에서 휴대전화 사용 금지라는 뜻으로 바꾸세요.','You must not use your phone here.','must not + 원형','규칙상 금지를 분명히 전달합니다.','You don’t have to use your phone here. → 사용할 필요 없음이지 금지가 아닙니다.','You’re not allowed to use your phone here.','여기에 주차하면 안 된다고 말하세요.','You must not park here.'],
    ['교수에게 질문 하나 해도 되는지 묻고 시작하세요.','Could I ask a quick question?','Could I + 원형','내 행동에 대한 허락을 구합니다.','Could I asking a question? → ask 원형입니다.','May I ask a question?','친구에게 충전기를 잠깐 빌려도 되는지 물으세요.','Could I borrow your charger for a minute?'],
    ['친구의 전화가 계속 통화 중입니다. 다른 사람과 통화 중인 것 같다고 추측하세요.','She must be talking to someone else.','must + be + -ing','근거를 바탕으로 현재 진행 중인 일을 강하게 추측합니다.','She must talking. → 진행형에는 be가 필요합니다.','She’s probably on another call.','수업이 끝났는데 교실이 텅 비었습니다. 모두 이미 떠난 것 같다고 말하세요.','Everyone must have left already.'],
    ['친구에게 주말에 같이 커피 마시고 싶은지 제안하세요.','Would you like to get coffee this weekend?','Would you like to + 원형','제안에 상대가 선택할 여지를 줍니다.','Would you like get coffee? → 행동 앞에 to가 필요합니다.','Do you want to grab coffee this weekend? (더 편한 말투)','친구에게 함께 점심 먹을지 제안하세요.','Would you like to have lunch together?'],
    ['팀원에게 금요일까지 초안을 완성할 수 있다고 말하되 보장하기는 어렵다고 덧붙이세요.','I should be able to finish the draft by Friday, but I can’t promise.','should be able to + 원형','가능할 것이라는 기대이며 확정 약속보다 약합니다.','I should can finish. → 일반적으로 조동사 should와 can을 이렇게 겹치지 않습니다.','I think I can finish the draft by Friday, but I can’t guarantee it.','내일 모임에 올 수 있을 것 같지만 확실하지 않다고 말하세요.','I should be able to come tomorrow, but I’m not sure yet.']
  ]);
  add(6,[
    ['수업 전에 강의 자료를 읽기로 결정했다고 말하세요.','I decided to read the material before class.','decide + to do','결정한 행동을 to부정사로 연결합니다.','I decided reading the material. → decide의 일반적 행동 보충은 to read입니다.','I made a decision to read the material before class.','이번 주에는 집에서 요리하기로 결정했다고 말하세요.','I decided to cook at home this week.'],
    ['출퇴근 시간에 운전하는 것을 피한다고 말하세요.','I avoid driving during rush hour.','avoid + doing','피하는 활동을 -ing로 표현합니다.','I avoid to drive. → avoid 뒤에는 보통 driving입니다.','I try not to drive during rush hour. (피하려 노력한다는 뜻)','잠들기 전에 커피 마시는 것을 피한다고 말하세요.','I avoid drinking coffee before bed.'],
    ['새 반 친구들을 만나는 것이 기대된다고 말하세요.','I’m looking forward to meeting my new classmates.','look forward to + doing','to는 이 결합에서 전치사입니다.','I’m looking forward to meet them. → meeting을 씁니다.','I’m excited about meeting my new classmates.','팀 프로젝트에서 함께 일하는 것이 기대된다고 말하세요.','I’m looking forward to working with you on the project.'],
    ['기차를 타기 위해 일찍 집을 나섰다고 말하세요.','I left home early to catch the train.','동작 + 목적의 to do','왜 일찍 출발했는지 목적을 덧붙입니다.','I left home early for catch the train. → for 뒤에 동사원형을 이렇게 붙이지 않습니다.','I left home early so I could catch the train.','공부하려고 도서관에 갔다고 말하세요.','I went to the library to study.'],
    ['I used to live alone.을 과거 습관이 아니라 ‘혼자 사는 데 익숙하다’로 바꾸세요.','I am used to living alone.','be used to + doing','익숙함은 be used to, 과거 습관은 used to do입니다.','I am used to live alone. → 익숙한 활동은 living입니다.','Living alone feels normal to me now.','일찍 일어나는 데 익숙하다고 말하세요.','I’m used to getting up early.'],
    ['I stopped studying.를 공부를 멈추고 저녁을 먹었다는 뜻으로 확장하세요.','I stopped studying to have dinner.','stop doing + 목적의 to do','공부는 멈춘 활동이고 저녁은 멈춘 목적입니다.','I stopped to study. → 다른 일을 멈추고 공부하려 했다는 뜻이 됩니다.','I took a break from studying to have dinner.','운전을 멈추고 지도를 확인했다고 말하세요.','I stopped driving to check the map.'],
    ['I remembered to lock the door.를 ‘문을 잠갔던 기억이 있다’로 바꾸세요.','I remember locking the door.','remember + doing','과거 행동을 기억한다는 현재 상태입니다.','I remember to lock the door. → 할 일을 기억한다는 의미여서 회상의 뜻과 다릅니다.','I remember that I locked the door.','신청서를 제출했던 기억이 있다고 말하세요.','I remember submitting the application.'],
    ['Try to restart the app.을 해결 방법으로 재시작을 한 번 해 보라는 뜻으로 바꾸세요.','Try restarting the app.','try + doing: 방법 시험','가능한 해결책으로 행동을 해 보라는 제안입니다.','Try restart the app. → try 뒤에 동사를 바로 붙이지 않습니다.','See if restarting the app helps.','다른 케이블을 해결 방법으로 써 보라고 말하세요.','Try using a different cable.'],
    ['친구의 이사를 도와주겠다고 제안했던 일을 말하세요. offer를 사용하세요.','I offered to help my friend move.','offer + to do','offer 뒤에서 제안한 행동을 to do로 연결합니다. help 뒤의 move는 동사원형이며 to move도 가능합니다.','I offered helping my friend move. → offer의 행동 패턴은 to help입니다.','I told my friend I’d be happy to help with the move.','팀원에게 발표 자료를 검토해 주겠다고 제안했다고 말하세요.','I offered to review my teammate’s slides.'],
    ['집주인에게 계약서 사본을 보내 달라고 mind를 써서 요청하세요.','Would you mind sending me a copy of the lease?','mind + doing','상대가 해 주길 바라는 일을 -ing로 표현합니다.','Would you mind to send me a copy? → sending을 씁니다.','Could you send me a copy of the lease?','동료에게 조금 천천히 말해 달라고 mind를 써서 요청하세요.','Would you mind speaking a little more slowly?'],
    ['친구에게 알림을 확인하다가 시간을 너무 많이 보낸다고 말하세요.','I spend too much time checking notifications.','spend + 시간 + doing','어떤 활동에 시간을 쓰는지 -ing로 덧붙입니다.','I spend too much time to check notifications. → 이 활동 결합은 checking이 자연스럽습니다.','Checking notifications takes up too much of my time.','통학하는 데 하루 두 시간을 쓴다고 말하세요.','I spend two hours a day commuting.'],
    ['이미 한 일임을 전제로, 팀원에게 도와줘서 고맙다고 말하세요.','Thank you for helping me with the project.','전치사 for + doing','감사의 이유를 전치사 뒤의 -ing로 표현합니다.','Thank you for help me. → for 뒤에 helping이 필요합니다.','I appreciate your help with the project.','집주인에게 누수를 고쳐 줘서 고맙다고 말하세요.','Thank you for fixing the leak.']
  ]);
  add(7,[
    ['친구에게 약속을 놓쳐서 사과하세요.','I’m sorry for missing our appointment.','sorry for + doing','사과하는 이유를 for 뒤에 넣습니다.','I’m sorry to missing our appointment. → to missing으로 연결하지 않습니다.','I apologize for missing our appointment.','팀원에게 늦은 것에 대해 사과하세요.','I’m sorry for being late.'],
    ['친구에게 로봇공학에 관심이 있다고 말하세요.','I’m interested in robotics.','interested in + 명사','관심 분야를 in으로 연결합니다.','I’m interested on robotics. → 보통 interested in입니다.','I’d like to learn more about robotics. (학습 의도 추가)','재생에너지에 관심이 있다고 말하세요.','I’m interested in renewable energy.'],
    ['늦어도 목요일까지 서류를 제출해야 한다고 말하세요.','I have to submit the documents by Thursday.','by + 완료 기한','그 시점까지 완료해야 한다는 뜻입니다.','I have to submit the documents until Thursday. → 계속 제출하는 기간처럼 들릴 수 있습니다.','The documents are due on Thursday.','금요일까지 결정하겠다고 말하세요.','I’ll make a decision by Friday.'],
    ['어제 캘거리에 도착했다고 말하세요.','I arrived in Calgary yesterday.','arrive in + 도시','도시·국가에는 보통 in, 특정 지점에는 at을 씁니다.','I arrived to Calgary yesterday. → arrive to로 옮기지 않습니다.','I got to Calgary yesterday.','오후 3시에 역에 도착했다고 말하세요.','I arrived at the station at three.'],
    ['Turn off the lights.에서 the lights를 대명사로 바꾸세요.','Turn them off.','분리 구동사: 동사 + 대명사 + 불변화사','복수 lights는 them으로 받고 중간에 놓습니다.','Turn off them. → 이 구동사의 대명사는 중간에 옵니다.','Could you turn them off? (정중한 질문으로도 가능)','Pick up the package.의 목적어를 대명사로 바꾸세요.','Pick it up.'],
    ['I talked about the problem.을 discuss를 써서 바꾸세요.','I discussed the problem.','discuss + 직접목적어','동사를 바꾸면 전치사 결합도 바뀝니다.','I discussed about the problem. → about을 빼야 합니다.','I had a discussion about the problem.','I got to the station.을 reach로 바꾸세요.','I reached the station.'],
    ['I agree.에 ‘네 의견에, 이 점에 관해서’라는 정보를 덧붙이세요.','I agree with you on this point.','agree with + 사람 / on + 주제','상대와 논의 주제의 역할을 구분합니다.','I am agree with you. → agree는 일반동사입니다.','We agree on this point.','팀이 마감일에 합의했다고 말하세요.','The team agreed on a deadline.'],
    ['I need to decide.를 decision이라는 명사를 사용해 바꾸세요.','I need to make a decision.','make a decision','동사 decide에 대응하는 관용적 명사 결합입니다.','I need to do a decision. → decision에는 보통 make를 씁니다.','I have a decision to make.','잠깐 쉬어야 한다고 take를 써서 말하세요.','I need to take a break.'],
    ['친구에게 금요일까지 이곳에 머문다고 말하세요. (체류가 지속됨)','I’m staying here until Friday.','until + 지속의 끝','머무는 상태가 그때까지 이어집니다.','I’m staying here by Friday. → by는 보통 완료 기한입니다.','I’ll be here until Friday.','은행이 오후 5시까지 문을 연 상태라고 말하세요.','The bank is open until five.'],
    ['도서관 직원에게 빌린 책을 찾고 있다고 말하세요.','I’m looking for a book I borrowed.','look for + 찾는 대상','look at은 바라보는 것, look for는 찾는 것입니다.','I’m looking a book. → 찾는 뜻에는 for가 필요합니다.','I’m trying to find a book I borrowed.','잃어버린 학생증을 찾고 있다고 말하세요.','I’m looking for my student ID.'],
    ['친구에게 금요일 저녁에 공항에서 데려오겠다고 말하세요.','I’ll pick you up at the airport on Friday evening.','pick + 사람 + up / at 장소 / on 날짜','대명사 you를 중간에 둡니다. 특정 요일의 저녁에는 on을 씁니다.','I’ll pick up you. → 대명사 위치를 바꿉니다.','I’ll come and get you at the airport on Friday evening.','친구를 내일 역에서 데려오겠다고 말하세요.','I’ll pick you up at the station tomorrow.'],
    ['교수에게 과제에 대한 피드백을 부탁하세요.','Could you give me some feedback on my assignment?','give feedback on + 대상','feedback은 보통 불가산명사이고 평가 대상을 on으로 연결할 수 있습니다.','Could you give me a feedback? → 이 의미에서는 some feedback이 자연스럽습니다.','Could you comment on my assignment?','친구에게 발표에 대한 조언을 부탁하세요.','Could you give me some advice on my presentation?']
  ]);
  add(8,[
    ['방은 작지만 캠퍼스에서 가까워 마음에 든다고 한 문장으로 말하세요.','Although the room is small, I like it because it’s close to campus.','although 양보절 + 주절 + because 이유절','작다는 단점을 인정하고 좋아하는 이유를 따로 연결합니다.','Although the room is small, but I like it. → although와 but을 중복하지 않습니다.','The room is small, but I like how close it is to campus.','수업은 어렵지만 많이 배워서 좋다고 말하세요.','Although the course is challenging, I like it because I’m learning a lot.'],
    ['어제 빌린 충전기가 작동하지 않는다고 말하세요.','The charger that I borrowed yesterday doesn’t work.','명사 + 목적격 관계절 + 주절 동사','charger가 주절 주어이자 borrowed의 목적어입니다.','The charger that I borrowed it doesn’t work. → it을 중복하지 않습니다.','The charger I borrowed yesterday isn’t working.','네가 추천한 식당이 좋았다고 말하세요.','The restaurant you recommended was great.'],
    ['스터디 그룹에서 만난 사람이 같은 아파트에 산다고 말하세요.','Someone I met in my study group lives in the same building.','사람 명사 + 관계절 + 주절','I met이 어떤 사람인지 좁히고 lives가 주절 동사입니다.','Someone I met in my study group live nearby. → someone을 받는 동사는 lives입니다.','A person from my study group lives in my building.','옆자리에 앉는 학생이 나를 도와줬다고 말하세요.','The student who sits next to me helped me.'],
    ['집에 도착하면 메시지하겠다고 말하세요.','I’ll text you when I get home.','미래 주절 + when + 단순현재','시간절에서는 앞으로의 일도 보통 현재형을 씁니다.','I’ll text you when I will get home. → 이 일반적인 시간절에는 get입니다.','I’ll send you a message once I’m home.','과제를 끝내면 전화하겠다고 말하세요.','I’ll call you when I finish the assignment.'],
    ['The bus was late. I missed the first part of class.를 so로 연결하세요.','The bus was late, so I missed the first part of class.','원인절 + so + 결과절','원인과 결과를 한 방향으로 연결합니다.','Because the bus was late, so I missed class. → 보통 because와 so를 한 쌍으로 중복하지 않습니다.','I missed the first part of class because the bus was late.','배터리가 방전되어 전화를 못 했다는 내용을 so로 연결하세요.','My battery was dead, so I couldn’t call you.'],
    ['We stayed inside because it was raining.을 because of로 바꾸세요.','We stayed inside because of the rain.','because of + 명사구','절 it was raining을 명사구 the rain으로 바꿉니다.','because of it was raining → because of 뒤에 이 형태의 절을 붙이지 않습니다.','We stayed inside due to the rain.','I was late because traffic was heavy.를 because of로 바꾸세요.','I was late because of the heavy traffic.'],
    ['My friend Alex helped me. Alex lives nearby.를 추가 정보를 넣는 관계절로 합치세요.','My friend Alex, who lives nearby, helped me.','고유명사 + 쉼표 who절 + 주절','이미 특정된 Alex에 부가 정보를 넣습니다.','Alex, that lives nearby, helped me. → 이 비제한적 관계절에는 that을 쓰지 않습니다.','My friend Alex lives nearby and helped me.','My laptop is three years old. It still works well.을 추가 정보 관계절로 합치세요.','My laptop, which is three years old, still works well.'],
    ['The room is expensive. However, it is close to campus.를 although로 시작하는 한 문장으로 바꾸세요.','Although the room is expensive, it is close to campus.','although + 절, 주절','대조 관계를 종속절로 연결합니다.','Although the room is expensive, however it is close. → 대조 표시를 불필요하게 중복하지 않습니다.','The room is expensive, but it’s close to campus.','비가 오지만 산책하겠다는 문장을 although로 시작하세요.','Although it’s raining, I’m going for a walk.'],
    ['친구에게 조용히 공부할 수 있는 장소를 찾는다고 말하세요.','I’m looking for a place where I can study quietly.','장소 명사 + where절','where는 그 장소에서 한다는 관계를 표현합니다.','a place where I can study there → where와 there가 장소 역할을 중복합니다.','I’m looking for somewhere quiet to study.','자전거를 안전하게 보관할 곳이 필요하다고 말하세요.','I need a place where I can keep my bike safely.'],
    ['팀원에게 일정에는 동의하지만 시간이 더 필요하다고 말하세요.','I agree with the plan, but I need more time.','동의절 + but + 제한','상대의 계획을 인정한 뒤 현실적인 제약을 말합니다.','I agree the plan, but… → 이 의미에서는 agree with를 씁니다.','The plan sounds good, although I’ll need more time.','아이디어는 좋지만 비용이 걱정된다고 말하세요.','I like the idea, but I’m worried about the cost.'],
    ['교수에게 공식을 이해하지만 언제 쓰는지는 모르겠다고 말하세요.','I understand the formula, but I’m not sure when to use it.','대조 + 의문사 to부정사','이해한 점과 모르는 점을 구체적으로 나눕니다.','I’m not sure when use it. → when to use 또는 when I should use입니다.','I understand the formula, but I don’t know when I should use it.','프로그램 실행은 알지만 파일 저장법은 모르겠다고 말하세요.','I know how to run the program, but I’m not sure how to save a file.'],
    ['친구에게 아르바이트로 바쁘긴 해도 주말에는 만날 수 있다고 말하세요.','Although I’m busy with my part-time job, I can meet you this weekend.','양보절 + 가능성 주절','상대가 예상할 제약을 인정하면서 가능한 시간을 제시합니다.','Despite I’m busy, I can meet you. → 절에는 although, 명사구에는 despite입니다.','I’m busy with work, but I’m free to meet this weekend.','시험 준비로 바쁘지만 오늘 저녁 잠깐 통화할 수 있다고 말하세요.','Although I’m studying for exams, I can talk for a few minutes tonight.']
  ]);
  add(9,[
    ['내일 눈이 오면 버스를 타겠다고 말하세요.','If it snows tomorrow, I’ll take the bus.','if + 현재, will + 원형','일어날 수 있는 미래 조건입니다.','If it will snow tomorrow… → 보통의 미래 조건에는 snows입니다.','I’ll take the bus tomorrow if it snows.','수업이 일찍 끝나면 도서관에 가겠다고 말하세요.','If class finishes early, I’ll go to the library.'],
    ['지금 시간이 더 있다면 스터디 그룹에 참여할 텐데라고 말하세요.','If I had more time, I would join the study group.','if + 과거형, would + 원형','현재의 시간 부족과 거리를 둔 가정입니다.','If I would have more time… → 이 기본 조건 구조에는 had를 씁니다.','I’d join the study group if I had more time.','학교 근처에 살면 매일 걸어갈 텐데라고 말하세요.','If I lived near campus, I would walk to class every day.'],
    ['더 일찍 출발했더라면 버스를 놓치지 않았을 텐데라고 말하세요.','If I had left earlier, I wouldn’t have missed the bus.','if + had p.p., would have p.p.','이미 지난 사실과 다른 과거를 상상합니다.','If I left earlier, I wouldn’t miss the bus. → 보통 현재·미래 가정으로 읽혀 지난 후회가 분명하지 않습니다.','I would have caught the bus if I’d left earlier.','파일을 저장했더라면 작업을 잃지 않았을 텐데라고 말하세요.','If I had saved the file, I wouldn’t have lost my work.'],
    ['지금 필요한 것은 더 많은 시간이 아니라 더 명확한 설명이라고 말하세요.','What I need is a clearer explanation, not more time.','What절 + be + 초점','필요한 것이 무엇인지 대조하며 강조합니다.','What I need a clearer explanation. → 두 부분을 잇는 is가 필요합니다.','I need a clearer explanation rather than more time.','가장 마음에 드는 점은 작은 학급 규모라고 말하세요.','What I like most is the small class size.'],
    ['Someone repaired the heater yesterday.를 난방 장치를 주어로 바꾸세요.','The heater was repaired yesterday.','대상 + be + 과거분사','행위자를 모르면 생략할 수 있습니다.','The heater was repair yesterday. → 과거분사 repaired입니다.','Someone fixed the heater yesterday. (능동 대안)','The office changed the schedule.을 시간표 중심으로 바꾸세요.','The schedule was changed by the office.'],
    ['교수가 어제 “The test is on Friday.”라고 했습니다. 과거 전달 시점을 기준으로 간접화법으로 옮기세요.','The instructor said the test was on Friday.','said + 내용절, 시제 후퇴','과거 발언을 전달하는 흔한 방식입니다. 일정이 지금도 유효하면 is를 유지할 수도 있습니다.','The instructor said me the test was on Friday. → 사람을 넣으려면 told me 또는 said to me입니다.','The instructor said the test is on Friday. (여전히 유효한 일정으로 전달)','친구가 “I’m tired.”라고 했던 말을 전달하세요.','My friend said she was tired.'],
    ['I understand the rule.에 ‘이해는 정말 한다’는 강조를 넣으세요.','I do understand the rule.','강조 do + 원형','반대 주장이나 오해에 대비해 이해한다는 사실을 강조합니다.','I do understands the rule. → do 뒤에는 원형입니다.','I really do understand the rule.','She likes the course.를 강조하세요.','She does like the course.'],
    ['I don’t have a car.를 지금 차가 있으면 좋겠다는 아쉬움으로 바꾸세요.','I wish I had a car.','wish + 과거형','현재 현실과 다른 소망입니다.','I wish I have a car. → 현재의 비현실적 소망에는 보통 had입니다.','If only I had a car. (아쉬움이 더 강함)','어젯밤 더 잘 잤으면 좋았을 텐데라고 말하세요.','I wish I had slept better last night.'],
    ['친구가 두 집 사이에서 고민합니다. 나라면 학교에 가까운 집을 고르겠다고 말하세요.','If I were you, I’d choose the place closer to campus.','If I were you + would','상대 입장을 가정한 조언입니다.','If I were you, I will choose… → 가정의 결과에는 여기서 would가 맞습니다.','I’d go for the place closer to campus.','나라면 결정 전에 비용을 비교하겠다고 조언하세요.','If I were you, I’d compare the costs before deciding.'],
    ['집주인에게 난방 장치가 언제 수리될지 아는지 물으세요.','Do you know when the heater will be repaired?','의문절 + 미래 수동태','when은 시간 부사절이 아니라 언제인지 묻는 의문절이므로 will을 쓸 수 있습니다.','Do you know when will the heater be repaired? → 내부는 heater will be 순서입니다.','Do you know when someone will repair the heater?','직원에게 결과가 언제 발표될지 물으세요.','Do you know when the results will be announced?'],
    ['팀원에게 교수님이 초안 제출을 요청했다고 전달하세요.','The instructor asked us to submit a draft.','ask + 사람 + to do','원래 요청 내용을 행동 구조로 전달합니다.','The instructor asked us submit a draft. → to submit이 필요합니다.','The instructor requested a draft from us. (더 격식 있음)','집주인이 내일 다시 전화해 달라고 했다고 전달하세요.','The landlord asked me to call back tomorrow.'],
    ['어젯밤 잠을 더 잘 잤더라면 지금 덜 피곤할 텐데라고 말하세요.','If I had slept better last night, I would feel less tired now.','과거 조건 + 현재 결과','조건은 지난밤, 결과는 현재인 혼합 조건문입니다.','I would have felt less tired now. → 현재 상태를 강조하려면 would feel이 분명합니다.','I’d feel better now if I’d slept well last night.','그 일자리를 수락했더라면 지금 다른 도시에 살고 있을 거라고 말하세요.','If I had accepted that job, I would be living in another city now.']
  ]);
  add(10,[
    ['친구에게 왜 이 전공을 골랐는지 관심 분야와 배우고 싶은 내용을 연결해 2문장으로 말하세요.','I chose this program because I enjoy solving practical problems. I’d like to learn how electrical systems work.','선택의 이유 + 배우고 싶은 내용','본인의 실제 이유로 바꿔도 좋습니다. 추상적 장점보다 구체적 관심을 말해 보세요.','I chose this program because of I enjoy… → 절 앞에는 because를 씁니다.','I’m interested in electrical systems, so this program seemed like a good fit.','친구에게 새로운 취미를 시작한 이유와 앞으로 배우고 싶은 것을 말하세요.','I started cooking because I wanted to eat better. I’d like to learn how to make a few Korean dishes.'],
    ['교수에게 첫 단계는 이해하지만 왜 저항값을 더하는지 모르겠다고 말하고 재설명을 부탁하세요.','I understand the first step, but I’m not sure why we add the resistances. Could you explain that part again?','이해 범위 + 간접의문절 + 요청','모르는 지점을 좁히면 상대가 어떤 설명을 해야 할지 알 수 있습니다. 회로 조건은 문제에 따라 다르므로 여기서는 질문 구조를 연습합니다.','I’m not sure why do we add… → 내부 의문절은 we add입니다.','Could you go over why we add these values? I’m following the first step.','은행 직원에게 계좌 개설법은 이해하지만 수수료가 언제 부과되는지 모르겠다고 질문하세요.','I understand how to open the account, but I’m not sure when the fee is charged. Could you explain that?'],
    ['집주인에게 어젯밤부터 수도꼭지가 새며 수리를 예약해 달라고 요청하세요.','The tap has been leaking since last night. Could you arrange a repair?','지속되는 문제 + 구체적인 요청','발생 시점과 필요한 행동을 따로 말합니다. tap 대신 faucet도 자연스럽습니다.','The tap is leaking since last night. → 지금까지의 지속을 has been leaking으로 나타냅니다.','The faucet started leaking last night. Could someone come and fix it?','상점에 어제 산 이어폰 한쪽이 작동하지 않으며 교환하고 싶다고 말하세요.','One side of the headphones I bought yesterday doesn’t work. Could I exchange them?'],
    ['친구에게 도심 집의 편리함에는 동의하지만 월세가 걱정된다고 말하세요.','I agree that living downtown would be convenient, but I’m worried about the rent.','동의 that절 + 대조 + 걱정','동의와 반론을 모두 구체적으로 표현합니다.','I am agree that… → agree 앞에 am을 붙이지 않습니다.','Downtown would be convenient, although the rent is a concern for me.','팀원에게 새 장비가 유용하겠지만 예산이 걱정된다고 말하세요.','I agree that the new equipment would be useful, but I’m worried about the cost.'],
    ['I don’t like this plan.을 상대의 장점은 인정하고 일정에 대한 구체적 우려를 말하는 표현으로 바꾸세요.','I see why you like the plan, but I’m concerned that we won’t have enough time.','상대 관점 인정 + 우려절','단순 부정보다 대화 가능한 이유를 제시합니다.','I’m concerned we not have enough time. → we won’t have로 문장 구조를 완성합니다.','The idea makes sense, but the timeline seems tight.','이 집은 싫다는 말을 위치는 좋지만 소음이 걱정된다는 말로 바꾸세요.','I like the location, but I’m worried about the noise.'],
    ['Explain it again.을 무엇이 불분명한지 밝히고 정중히 재설명을 요청하는 두 문장으로 바꾸세요.','I’m not sure what you mean by “load.” Could you put that another way?','불명확한 용어 특정 + 재표현 요청','같은 말을 반복해 달라는 요청과 다른 말로 설명해 달라는 요청을 구별합니다.','Could you explain me “load”? → explain the term to me처럼 씁니다.','Could you explain what “load” means in this context?','대화 중 “deposit”이라는 말이 불분명하다고 밝히고 설명을 부탁하세요.','I’m not sure what you mean by “deposit.” Could you explain that term?'],
    ['I missed class.를 사유를 짧게 밝히고 놓친 자료를 요청하는 메시지로 확장하세요.','I missed class because I wasn’t feeling well. Could you send me the notes?','과거 사건 + 이유 + 요청','필요한 만큼 사유를 밝히고 원하는 도움을 구체화합니다.','Could you send me to the notes? → 내용은 직접목적어로 send me the notes 또는 send the notes to me입니다.','I was unwell and couldn’t make it to class. Would you mind sharing your notes?','모임에 늦었다고 말하고 이미 결정된 내용을 알려 달라고 요청하세요.','Sorry I’m late. Could you tell me what you’ve decided so far?'],
    ['친구에게 “I’ve been here for three years.”라고 잘못 말했습니다. 실제로는 3주라는 뜻이었다고 자연스럽게 정정하세요.','Sorry, I meant three weeks, not three years.','I meant + 정정 내용','대화 전체를 다시 시작할 필요 없이 잘못된 정보만 고칩니다.','I meaned three weeks. → mean의 과거형은 meant입니다.','Sorry, let me correct that. I’ve been here for three weeks.','약속을 화요일이라고 잘못 말했고 실제로는 목요일이라고 정정하세요.','Sorry, I meant Thursday, not Tuesday.'],
    ['친구가 “How has your first week been?”이라고 묻습니다. 좋았던 점·어려웠던 점을 말하고 친구에게도 질문하세요. 2~3문장으로 말해 보세요.','It’s been interesting, but I’m still getting used to the schedule. I’ve enjoyed meeting my classmates. How has your week been?','지금까지 경험 + 적응 중인 점 + 되묻기','실제 경험으로 답해도 됩니다. 문법뿐 아니라 상대에게도 말할 차례를 주었는지 확인하세요.','I’m getting used to follow the schedule. → be used to 뒤는 following입니다.','I’ve had a good week overall, although it’s been busy. What about you?','친구가 새 직장에서의 첫 달을 묻는다고 가정하고 장단점과 되묻기를 연결하세요.','It’s been a good month, but there’s a lot to learn. I like the team. How are things going for you?'],
    ['룸메이트가 밤늦게 음악을 틉니다. 영향과 구체적인 부탁을 말하고 타협안을 제시하세요. 2~3문장으로 말하세요.','I’m finding it hard to sleep with the music on. Could you use headphones after ten? That way, you could still listen while I sleep.','영향 설명 + 요청 + 타협의 이유','관찰 가능한 문제와 실행 가능한 조치를 말합니다. 상황에 맞는 시간으로 바꿔도 됩니다.','You make me can’t sleep. → 이 구조 대신 I can’t sleep with the music on처럼 표현합니다.','The music is keeping me awake. Would you mind switching to headphones at night?','팀원의 늦은 파일 공유가 검토를 어렵게 한다고 설명하고 하루 일찍 공유해 달라고 부탁하세요.','It’s hard to review everything at the last minute. Could you share the files a day earlier so I have time to check them?'],
    ['친구가 온라인 수업이 항상 더 좋다고 합니다. 장점을 인정하고 반대 이유와 자신의 선호를 말하세요. 2~3문장으로 말하세요.','Online classes are convenient, but I find it easier to ask questions in person. For hands-on subjects, I’d prefer to attend on campus.','장점 인정 + 비교 + 조건부 선호','항상 그렇다는 주장에 예외나 조건을 들어 답합니다. 본인의 입장으로 바꿔도 됩니다.','I prefer attend on campus. → prefer to attend 또는 prefer attending입니다.','I like the flexibility, although I learn practical skills better in person.','친구가 혼자 공부하는 것이 항상 낫다고 합니다. 장점을 인정하고 함께 공부할 때의 이점도 말하세요.','Studying alone helps me focus, but discussing problems with others can show me different approaches. I’d use both methods.'],
    ['식당에서 주문과 다른 음식이 나왔습니다. 상황을 설명하고 주문 확인을 부탁하며 시간이 걸릴 경우 대안을 물으세요. 2~3문장으로 말하세요.','I ordered the vegetable pasta, but this seems to have chicken in it. Could you check the order? If it takes a while to replace it, is there a quicker option?','사실 + 완곡한 확인 + 조건부 후속 질문','상황과 주문 내용을 분명히 합니다. 알레르기 등 별도 요구가 있다면 직접 명시해야 합니다.','Could you check what did I order? → 내부는 what I ordered입니다.','I think there may have been a mix-up with my order. Could you check it for me?','은행에서 예상하지 못한 수수료를 발견했습니다. 이유를 묻고 앞으로 피하는 방법을 질문하세요.','I noticed a fee I wasn’t expecting. Could you explain what it’s for and how I can avoid it in the future?']
  ]);
  const followups = [
    ['What has been the biggest adjustment?','The biggest adjustment has been planning my time. I’m trying to prepare for each class the night before.'],
    ['Would it be okay if I used speakers until nine?','That would work for me. Thanks for being flexible.'],
    ['What would make online classes work better for you?','More opportunities to ask questions would help. I’d also like practical sessions on campus.'],
    ['We can replace it, but it will take twenty minutes. Is that okay?','I’m afraid I don’t have that much time. Is there something quicker you could offer?']
  ];
  lab.exercises.filter(q=>q.chapter===10&&q.mode==='speak').forEach((q,i)=>{q.followup=followups[i][0];q.followupAnswer=followups[i][1];});
})();
