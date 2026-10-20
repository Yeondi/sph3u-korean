/* No network requests, accounts, AI grading or shared keys with other study pages. */
(() => {
  'use strict';
  const {chapters, roadmap, exercises} = window.ENGLISH_LAB;
  const KEY = 'english-speaking-lab-v1';
  const $ = s => document.querySelector(s);
  const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const validId = id => exercises.some(q => q.id === id);
  const fresh = () => ({version:1, done:{}, attempts:{}, reviews:{}, drafts:{}});
  let state = fresh(), storageProblem = false;
  try {
    const raw = JSON.parse(localStorage.getItem(KEY));
    if (raw && raw.version === 1) {
      for (const c of chapters) if (raw.done?.[c.id] === true) state.done[c.id] = true;
      for (const q of exercises) {
        const a = raw.attempts?.[q.id], r = raw.reviews?.[q.id];
        if (a && ['again','hard','good'].includes(a.rating)) state.attempts[q.id] = {rating:a.rating};
        if (r && Number.isFinite(r.due) && Number.isInteger(r.level) && r.level >= 0 && r.level <= 4) state.reviews[q.id] = {due:r.due, level:r.level};
        for (const suffix of ['', '-transfer']) {
          const key = q.id + suffix;
          if (typeof raw.drafts?.[key] === 'string') state.drafts[key] = raw.drafts[key].slice(0,4000);
        }
      }
    }
  } catch { storageProblem = true; }
  let view = 'home', filter = 'due', noticeTimer, recognition = null;
  const timers = new Map();
  function notify(message) { clearTimeout(noticeTimer); $('#notice').textContent = message; noticeTimer = setTimeout(() => $('#notice').textContent = '',7000); }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); }
    catch { storageProblem = true; notify('브라우저 저장을 사용할 수 없습니다. 현재 탭에서만 유지됩니다. 저장 공간·사이트 설정을 확인해 주세요.'); }
  }
  function nav() {
    const count = chapters.filter(c => state.done[c.id]).length;
    $('#progress').value = count;
    $('#progress-label').textContent = `${count} / ${chapters.length}장 완료 · ${Math.round(count/chapters.length*100)}% (공개분 기준)`;
    const due = Object.values(state.reviews).filter(r => r.due <= Date.now()).length;
    const links = [['home','학습 안내'], ...chapters.map(c => [String(c.id),`${state.done[c.id]?'✓ ':''}${c.id}. ${c.title}`]), ['review',`오답·복습 (${due})`]];
    $('#navigation').innerHTML = links.map(([id,label])=>`<button data-view="${id}" class="${view===id?'active':''}" ${view===id?'aria-current="page"':''}>${escape(label)}</button>`).join('');
  }
  function home() {
    return `<span class="eyebrow">BUILD FIRST. SPEAK NEXT.</span><h1>아는 영어를, 직접 만드는 영어로.</h1>
    <p class="muted">English Speaking Lab · 한국어 설명과 영어 문장 생성 훈련</p>
    <div class="callout"><b>정확하게 조립한 뒤, 조금씩 빠르게.</b><p>문법을 이해해도 말할 때 동사와 어순이 흔들릴 수 있습니다. 시험 점수로 말하기 수준을 단정하지 않고, 실제로 만든 문장을 보며 연습합니다. 처음부터 타이머를 켤 필요는 없습니다.</p></div>
    <div class="grid"><div class="card"><span class="badge">현재 제공</span><h3>3개 챕터 · 36개 연습</h3><p>각 장에 조립 4개, 변형 4개, 즉답 4개. 복습에서는 같은 구조를 다른 상황에 적용하는 추가 문제 36개를 제공합니다.</p></div><div class="card"><span class="badge">학습 방식</span><h3>자동 점수 대신 구조 비교</h3><p>내 답을 먼저 작성하고 예시와 비교합니다. 표현이 달라도 의미·구조·말투가 맞으면 가능합니다. AI 문법 채점과 발음 평가는 제공하지 않습니다.</p></div></div>
    <h2>한 번의 학습 순서</h2><ol><li>개념과 문장 성분을 읽고 <b>주어 → 동사 → 필요한 자리</b>를 고릅니다.</li><li>답을 직접 입력한 뒤 모범 답안, 흔한 오류, 대안 표현을 비교합니다.</li><li>‘다시 연습 / 헷갈림 / 스스로 가능’으로 자기평가합니다. 앞의 두 선택은 복습 목록에 자동 등록됩니다.</li><li>즉답 문제는 먼저 말하고 ‘직접 말했어요’를 체크합니다. 익숙해지면 15초 → 10초 → 5초로 줄입니다.</li><li>복습에서는 새 상황으로 다시 말해 봅니다. 필요하면 원문도 다시 풀 수 있습니다.</li></ol>
    <p class="small muted">시간 단축 기준은 자기 판단입니다. 여러 새 상황에서도 의미·동사 구조·시제를 안정적으로 만들 수 있을 때 줄이세요. 빨리 말했다고 정확한 것은 아닙니다.</p>
    <h2>학습 과정</h2><div class="grid">${chapters.map(c=>`<button class="card" data-view="${c.id}"><span class="badge">학습 가능 · 12문제 ${state.done[c.id]?'· 완료':''}</span><h3>${c.id}. ${escape(c.title)}</h3><p>${escape(c.subtitle)}</p><span class="small">학습 시작 →</span></button>`).join('')}${roadmap.map((title,i)=>`<div class="card unavailable"><span class="badge unavailable">준비 중 · 학습 및 완료 처리 불가</span><h3>${i+4}. ${escape(title)}</h3><p>독립 챕터의 설명·분석·연습을 검토한 뒤 공개합니다.</p></div>`).join('')}</div>
    <h2>저장과 음성 기능</h2><p>진도·입력·복습 일정은 이 기기의 현재 브라우저에 저장됩니다. 다른 기기와 동기화되지 않으며 브라우저 데이터 삭제 시 사라질 수 있습니다. 기존 물리·회로 학습 데이터와 별도로 저장합니다.</p>
    <p>예문 듣기는 브라우저 TTS를 사용합니다. 음성 입력은 브라우저 지원 및 마이크 권한에 따라 제공되며, 음성이 브라우저 제공업체의 서비스로 전송될 수 있습니다. 동의하는 경우에만 음성 입력 버튼을 누르세요. 받아쓰기 오류는 발음 점수가 아닙니다.</p>
    <h2>문법 참고 자료</h2><p class="small">설명·문제는 이 도구를 위해 작성했습니다. 아래 자료에서 기본 구조와 용법을 더 확인할 수 있습니다. 예문의 대안은 유일한 정답이 아닙니다.</p><ul class="source-links"><li><a href="https://learnenglish.britishcouncil.org/free-resources/grammar/english-grammar-reference/verb-be" target="_blank" rel="noopener">British Council · The verb be</a></li><li><a href="https://learnenglish.britishcouncil.org/free-resources/grammar/a1-a2/verbs-followed-ing-or-infinitive" target="_blank" rel="noopener">British Council · Verbs followed by -ing or infinitive</a></li><li><a href="https://learnenglish.britishcouncil.org/grammar/english-grammar-reference/present-perfect" target="_blank" rel="noopener">British Council · Present perfect</a></li></ul>`;
  }
  function question(q, transfer = false) {
    const key = q.id + (transfer ? '-transfer' : ''), speaking = q.mode === 'speak' || transfer;
    const review = state.reviews[q.id], attempt = state.attempts[q.id];
    return `<article class="question" data-q="${q.id}" data-transfer="${transfer}"><span class="badge">${q.id} · ${transfer?'새 상황 복습':{build:'문장 조립',transform:'문장 변형',speak:'즉답 훈련'}[q.mode]}</span>
    <h3>${escape(transfer?q.transfer:q.prompt)}</h3>
    ${speaking?`<div class="actions"><label for="time-${key}">준비 시간</label><select id="time-${key}" class="time"><option value="0">제한 없음</option><option value="15">15초</option><option value="10">10초</option><option value="5">5초</option></select><button data-action="timer">시작 / 다시 시작</button><span class="timer" role="status">준비되면 시작하세요</span></div><p class="small muted">상황을 읽고 시작하세요. 시간 종료 후에도 계속 답할 수 있고 정답은 자동으로 열리지 않습니다.</p>`:''}
    <label for="input-${key}">내가 만든 영어 문장</label><textarea id="input-${key}" maxlength="4000" lang="en" spellcheck="false" autocomplete="off" placeholder="먼저 영어 문장을 만들어 보세요.">${escape(state.drafts[key]||'')}</textarea>
    ${speaking?`<label class="check"><input type="checkbox" class="spoken">답안을 보지 않고 직접 말했어요 (입력 없이도 비교 가능)</label>`:''}
    <div class="actions"><button data-action="reveal" class="primary">모범 답안과 비교</button><button data-action="bookmark" aria-pressed="${!!review}">${review?'복습 저장됨':'어려운 문제 저장'}</button>${('SpeechRecognition' in window || 'webkitSpeechRecognition' in window)?'<button data-action="mic">음성 입력</button>':'<span class="small muted">음성 인식 미지원 · 텍스트로 입력해 주세요.</span>'}</div>
    <p class="review-meta">${attempt?'최근 자기평가: '+{again:'다시 연습',hard:'헷갈림',good:'스스로 가능'}[attempt.rating]:'아직 자기평가하지 않았습니다.'}${review?' · 다음 복습: '+escape(new Date(review.due).toLocaleString('ko-KR')):''}</p>
    <div class="feedback" hidden></div></article>`;
  }
  function chapter(c) {
    const qs = exercises.filter(q=>q.chapter===c.id);
    return `<span class="eyebrow">CHAPTER ${c.id} / 10 · 공개된 핵심 과정</span><h1>${c.id}. ${escape(c.title)}</h1><p class="muted">${escape(c.subtitle)}</p><div class="callout">${escape(c.goal)}</div>
    <div class="section-nav"><button data-section="concept">A 개념</button><button data-section="analysis">B 구조 분석</button><button data-section="build">C 조립</button><button data-section="transform">D 변형</button><button data-section="speak">E 즉답</button><button data-section="review-guide">F 복습</button></div>
    <section id="concept"><h2>A. 개념 이해</h2>${c.concepts.map(([title,body])=>`<div class="card"><h3>${escape(title)}</h3><p>${escape(body)}</p></div>`).join('')}<h3>의도한 의미에서의 오류와 자연스러운 문장</h3><div class="tablewrap"><table><thead><tr><th scope="col">오류 예문</th><th scope="col">수정 예문</th><th scope="col">이유</th></tr></thead><tbody>${c.comparisons.map(row=>`<tr>${row.map((s,i)=>`<td ${i<2?'lang="en"':''}>${escape(s)}</td>`).join('')}</tr>`).join('')}</tbody></table></div></section>
    <section id="analysis"><h2>B. 문장 구조 분석</h2><p class="muted">색뿐 아니라 역할 이름으로 구별합니다. 동사구·절 내부에도 자체 구조가 있습니다.</p>${c.analyses.map(parts=>`<div class="analysis"><div class="tokens">${parts.map(([word,role,why])=>`<div class="token"><span>${escape(role)}</span><b lang="en">${escape(word)}</b><small>${escape(why)}</small></div>`).join('')}</div></div>`).join('')}</section>
    ${[['build','C. 문장 조립 훈련','한국어 상황의 뜻을 먼저 파악하고 주어와 동사부터 고르세요.'],['transform','D. 문장 변형 훈련','기존 문장을 그대로 외우지 말고 달라지는 구조와 의미를 확인하세요.'],['speak','E. 상황별 즉답 훈련','먼저 소리 내어 말하세요. 음성 입력 없이 직접 말하고 체크해도 됩니다.']].map(([mode,title,desc])=>`<section id="${mode}"><h2>${title}</h2><p>${desc}</p>${mode==='speak'?'<p class="small muted">음성 입력은 받아쓰기이며 발음·문법 평가가 아닙니다. 브라우저 제공업체로 음성이 전송될 수 있으므로 동의하는 경우에만 사용하세요.</p>':''}${qs.filter(q=>q.mode===mode).map(q=>question(q)).join('')}</section>`).join('')}
    <section id="review-guide"><h2>F. 복습 및 오답 관리</h2><ul>${c.checklist.map(s=>`<li>${escape(s)}</li>`).join('')}</ul><p>답안과 다르다는 이유만으로 오답은 아닙니다. 뜻·구조·상황에 맞는 말투를 비교하세요. ‘다시 연습’은 10분 뒤, ‘헷갈림’은 1일 뒤 복습합니다. 저장한 문제를 스스로 만들면 1 → 3 → 7 → 14일로 간격을 늘립니다. 학습 효율을 보장하는 알고리즘이 아니라 간단한 복습 일정입니다.</p><button data-view="review">오답·복습 목록 열기 →</button>
    <div class="completion"><label class="check"><input type="checkbox" id="complete" ${state.done[c.id]?'checked':''}>이 장의 개념과 12문제를 연습했습니다</label><p class="small" id="completion-status">${qs.filter(q=>state.attempts[q.id]).length} / 12문제 자기평가 완료 · 모두 비교한 뒤 완료 표시할 수 있습니다.</p></div><div class="actions"><button data-view="${c.id===1?'home':c.id-1}">← 이전</button><button data-view="${c.id===3?'review':c.id+1}">${c.id===3?'복습으로':'다음 장으로'} →</button></div></section>`;
  }
  function reviews() {
    const saved = exercises.filter(q=>state.reviews[q.id]);
    const shown = saved.filter(q=>filter==='all'||state.reviews[q.id].due<=Date.now());
    return `<span class="eyebrow">RETRIEVE · TRANSFER · REPEAT</span><h1>오답·복습 노트</h1><p>같은 동사 구조를 새로운 상황에서 꺼내 보세요. 아래 문제는 원래 문제의 번역을 반복하지 않습니다.</p><p class="small muted">‘다시 연습 / 헷갈림’은 직접 판단한 기록입니다. 자동으로 문법 오류를 판정한 목록이 아닙니다. 음성 입력은 받아쓰기이며 브라우저 제공업체로 음성이 전송될 수 있습니다.</p><div class="actions"><button data-filter="due" aria-pressed="${filter==='due'}" class="${filter==='due'?'primary':''}">지금 복습할 문제</button><button data-filter="all" aria-pressed="${filter==='all'}" class="${filter==='all'?'primary':''}">저장한 문제 전체 (${saved.length})</button></div><p class="small">기한이 지난 문제는 다음 접속 시에도 남습니다. 이 목록을 열 때 현재 시각으로 갱신합니다.</p>${shown.length?shown.map(q=>`${question(q,true)}<div class="actions"><button data-view="${q.chapter}">원래 ${q.chapter}장 연습</button><button data-remove="${q.id}">이 문제를 복습 목록에서 제거</button></div>`).join(''):'<div class="empty">현재 이 목록에 문제가 없습니다. 학습 중 ‘어려운 문제 저장’을 누르거나 자기평가에서 ‘다시 연습 / 헷갈림’을 선택해 주세요.</div>'}`;
  }
  function stopActivities() {
    timers.forEach(t=>clearInterval(t)); timers.clear();
    if (recognition) { recognition.abort(); recognition=null; }
    if (window.speechSynthesis) window.speechSynthesis.cancel();
  }
  function render(next, focus = false) {
    stopActivities(); view = ['home','review',...chapters.map(c=>String(c.id))].includes(String(next)) ? String(next) : 'home';
    nav(); $('#main').innerHTML = view==='home'?home():view==='review'?reviews():chapter(chapters.find(c=>String(c.id)===view));
    if (focus) { $('#main').focus(); window.scrollTo({top:0,behavior:'instant'}); }
  }
  function reveal(card,q,transfer) {
    if (!card.querySelector('textarea').value.trim() && !card.querySelector('.spoken')?.checked) { notify('먼저 영어 문장을 입력하거나 직접 말한 뒤 체크해 주세요.'); card.querySelector('textarea').focus(); return; }
    const timerKey = card.querySelector('textarea').id;
    clearInterval(timers.get(timerKey)); timers.delete(timerKey);
    if (card.querySelector('.timer')) card.querySelector('.timer').textContent = '답안 비교 중';
    const feedback = card.querySelector('.feedback');
    feedback.hidden = false;
    feedback.innerHTML = `<span class="badge">자기 비교 · 자동 채점 아님</span><h4>가능한 모범 문장</h4><p class="model" lang="en">${escape(transfer?q.transferAnswer:q.answer)}</p><button data-action="listen">▶ 예문 듣기</button><h4>핵심 구조${transfer?' (원래 문제에서 연습한 구조)':''}</h4><p>${escape(q.pattern)}</p>${transfer?`<p>이 새 상황의 문장을 먼저 비교한 뒤, 원래 문제의 설명을 참고하세요. 주어·동사·시제·말투는 상황에 맞게 달라질 수 있습니다.</p><details><summary>원래 문제의 모범 답안과 설명</summary><p lang="en">${escape(q.answer)}</p><p>${escape(q.explanation)}</p><p class="error">${escape(q.error)}</p><p>${escape(q.alternative)}</p></details>`:`<p>${escape(q.explanation)}</p><h4>흔한 오류와 이유</h4><p class="error">${escape(q.error)}</p><h4>자연스러운 대안 표현</h4><p>${escape(q.alternative)}</p>`}<div class="rating"><h4>내 답은 어땠나요?</h4><p class="small">문자열이 달라도 맞을 수 있습니다. 의미를 전달했는지, 동사의 자리를 채웠는지, 상황에 맞는지 확인하세요.</p><div class="actions"><button data-rating="again">다시 연습 · 10분 뒤</button><button data-rating="hard">헷갈림 · 1일 뒤</button><button data-rating="good">스스로 가능</button></div><p class="rating-result" role="status"></p></div>`;
    card.querySelector('[data-action="reveal"]').textContent = '답안 다시 비교';
  }
  function rate(card,q,rating) {
    state.attempts[q.id] = {rating};
    const previous = state.reviews[q.id];
    let message = '자기평가를 저장했습니다.';
    if (rating !== 'good') {
      state.reviews[q.id] = {level:0,due:Date.now()+(rating==='again'?600000:86400000)};
      message = rating==='again'?'10분 뒤 복습하도록 저장했습니다.':'1일 뒤 복습하도록 저장했습니다.';
    } else if (previous) {
      const days = [1,3,7,14][Math.min(previous.level,3)];
      state.reviews[q.id] = {level:Math.min(previous.level+1,4),due:Date.now()+days*86400000};
      message = `${days}일 뒤 복습하도록 저장했습니다.`;
    }
    save(); nav(); card.querySelector('.rating-result').textContent = message;
    card.querySelectorAll('[data-rating]').forEach(b=>b.disabled=true);
    const bookmark = card.querySelector('[data-action="bookmark"]'); bookmark.textContent = state.reviews[q.id]?'복습 저장됨':'어려운 문제 저장'; bookmark.setAttribute('aria-pressed',String(!!state.reviews[q.id]));
    card.querySelector('.review-meta').textContent = `최근 자기평가: ${{again:'다시 연습',hard:'헷갈림',good:'스스로 가능'}[rating]}${state.reviews[q.id]?' · 다음 복습: '+new Date(state.reviews[q.id].due).toLocaleString('ko-KR'):''}`;
    if ($('#completion-status')) $('#completion-status').textContent = `${exercises.filter(x=>x.chapter===q.chapter&&state.attempts[x.id]).length} / 12문제 자기평가 완료 · 모두 비교한 뒤 완료 표시할 수 있습니다.`;
  }
  function startTimer(card) {
    const key = card.querySelector('textarea').id;
    clearInterval(timers.get(key)); timers.delete(key);
    const seconds = Number(card.querySelector('.time').value), label = card.querySelector('.timer');
    if (!seconds) {label.textContent='제한 없음 · 정확하게 말해 보세요';return;}
    const deadline = Date.now()+seconds*1000;
    label.textContent = `${seconds}초 남음`;
    const interval = setInterval(()=>{const remaining=Math.max(0,Math.ceil((deadline-Date.now())/1000)); if(!remaining){clearInterval(interval);timers.delete(key);label.textContent='시간 종료 · 끝까지 말한 뒤 비교하세요';}else label.textContent=`${remaining}초 남음`;},250);
    timers.set(key,interval);
  }
  function dictate(card,button) {
    if (recognition) {recognition.stop();return;}
    const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!Recognition) { notify('음성 인식을 지원하지 않습니다. 텍스트로 입력해 주세요.'); return; }
    const instance = new Recognition(); recognition=instance;
    instance.lang='en-CA';instance.interimResults=false;instance.continuous=false;
    const input=card.querySelector('textarea');
    instance.onresult=e=>{ if(!input.isConnected)return; const words=Array.from(e.results).map(r=>r[0].transcript).join(' '); input.value=(input.value.trim()+' '+words).trim().slice(0,4000);input.dispatchEvent(new Event('input',{bubbles:true}));notify('받아쓰기를 추가했습니다. 인식된 단어를 직접 확인해 주세요.'); };
    instance.onerror=e=>notify(({ 'not-allowed':'마이크 권한이 허용되지 않았습니다. 텍스트 입력을 이용해 주세요.', 'no-speech':'말소리를 인식하지 못했습니다. 다시 시도하거나 입력해 주세요.', 'network':'음성 인식 서비스에 연결하지 못했습니다. 텍스트 입력을 이용해 주세요.', 'audio-capture':'사용할 수 있는 마이크가 없습니다. 텍스트 입력을 이용해 주세요.', 'aborted':'음성 입력을 중단했습니다.' })[e.error]||'음성 입력을 사용할 수 없습니다. 텍스트로 입력해 주세요.');
    instance.onend=()=>{button.textContent='음성 입력';if(recognition===instance)recognition=null;};
    try {instance.start();button.textContent='■ 음성 입력 중지';notify('마이크로 영어 문장을 말해 주세요. 인식 결과는 채점하지 않습니다.');} catch {recognition=null;button.textContent='음성 입력';notify('음성 입력을 시작하지 못했습니다. 텍스트 입력을 이용해 주세요.');}
  }
  document.addEventListener('input',e=>{
    if(!e.target.matches('.question textarea'))return;
    const card=e.target.closest('.question'), key=card.dataset.q+(card.dataset.transfer==='true'?'-transfer':'');
    state.drafts[key]=e.target.value;save();
  });
  document.addEventListener('change',e=>{
    if(e.target.id==='complete'){
      const qs=exercises.filter(q=>String(q.chapter)===view);
      if(e.target.checked && !qs.every(q=>state.attempts[q.id])){e.target.checked=false;notify('12문제를 직접 풀고 답안 비교 후 자기평가를 마쳐 주세요.');return;}
      state.done[view]=e.target.checked;save();nav();
    }
  });
  document.addEventListener('click',e=>{
    const b=e.target.closest('button');if(!b)return;
    if(b.dataset.section){document.getElementById(b.dataset.section)?.scrollIntoView();return;}
    if(b.dataset.view){location.hash=`view=${b.dataset.view}`; if(view===b.dataset.view)render(view,true);return;}
    if(b.dataset.filter){filter=b.dataset.filter;render('review');return;}
    if(b.dataset.remove){if(validId(b.dataset.remove)){delete state.reviews[b.dataset.remove];save();render('review');}return;}
    const card=b.closest('.question');if(!card)return;
    const q=exercises.find(x=>x.id===card.dataset.q), transfer=card.dataset.transfer==='true';if(!q)return;
    if(b.dataset.rating){rate(card,q,b.dataset.rating);return;}
    switch(b.dataset.action){
      case 'reveal': reveal(card,q,transfer);break;
      case 'bookmark': if(!state.reviews[q.id])state.reviews[q.id]={level:0,due:Date.now()};save();nav();b.textContent='복습 저장됨';b.setAttribute('aria-pressed','true');notify('복습 목록에 저장했습니다. 새 상황으로 다시 연습할 수 있습니다.');break;
      case 'timer':startTimer(card);break;
      case 'mic':dictate(card,b);break;
      case 'listen':if(!('speechSynthesis' in window)||!('SpeechSynthesisUtterance' in window)){notify('예문 듣기를 지원하지 않는 브라우저입니다.');break;}window.speechSynthesis.cancel();const utterance=new SpeechSynthesisUtterance(transfer?q.transferAnswer:q.answer);utterance.lang='en-CA';utterance.rate=.9;const voices=window.speechSynthesis.getVoices();const voice=voices.find(v=>v.lang==='en-CA')||voices.find(v=>v.lang.startsWith('en'));if(voice)utterance.voice=voice;utterance.onerror=event=>{if(event.error!=='interrupted'&&event.error!=='canceled')notify('예문을 재생하지 못했습니다. 기기의 영어 음성·오디오 설정을 확인해 주세요.');};window.speechSynthesis.speak(utterance);break;
    }
  });
  window.addEventListener('hashchange',()=>{if(location.hash.startsWith('#view='))render(location.hash.slice(6),true);});
  window.addEventListener('pagehide',stopActivities);
  render(location.hash.startsWith('#view=')?location.hash.slice(6):'home');
  if(storageProblem)notify('저장된 학습 정보를 읽지 못했습니다. 이 탭에서는 새 상태로 시작합니다.');
})();
