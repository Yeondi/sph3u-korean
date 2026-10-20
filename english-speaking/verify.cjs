/* Dependency-free logic tests. This DOM stub does NOT validate browser layout or audio. */
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const content = fs.readFileSync(path.join(__dirname,'content.js'),'utf8');
const expanded = fs.readFileSync(path.join(__dirname,'content-expanded.js'),'utf8');
const app = fs.readFileSync(path.join(__dirname,'app.js'),'utf8');
const KEY = 'english-speaking-lab-v1';
function element() {
  return {innerHTML:'',textContent:'',value:'',checked:false,hidden:true,disabled:false,dataset:{},
    setAttribute(k,v){this[k]=v;},focus(){this.focused=true;}};
}
function boot({data={},hash='#view=1',broken=false}={}) {
  const store = {...data}, events = {}, windowEvents = {}, intervals = new Map();
  let now=1800000000000, sequence=0;
  const nodes = Object.fromEntries(['#progress','#progress-label','#navigation','#main','#notice','#completion-status','#coverage','#storage-warning'].map(id=>[id,element()]));
  const context = {
    window:{addEventListener:(name,fn)=>windowEvents[name]=fn,scrollTo(){}},
    document:{querySelector:id=>nodes[id]||null,addEventListener:(name,fn)=>events[name]=fn,getElementById:()=>null},
    location:{hash},
    localStorage:{getItem:key=>{if(broken)throw Error('blocked');return store[key]||null;},setItem:(key,value)=>{if(broken)throw Error('blocked');store[key]=value;}},
    Date:class extends Date {constructor(...args){super(...(args.length?args:[now]));}static now(){return now;}},
    setTimeout:()=>++sequence,clearTimeout(){},setInterval:fn=>{intervals.set(++sequence,fn);return sequence;},clearInterval:id=>intervals.delete(id)
  };
  vm.createContext(context); vm.runInContext(content,context);vm.runInContext(expanded,context);vm.runInContext(app,context);
  const state=()=>JSON.parse(store[KEY]);
  function card(id,transfer=false) {
    const fields=Object.fromEntries(['textarea','.spoken','.feedback','[data-action="reveal"]','[data-action="bookmark"]','.rating-result','.review-meta','.time','.timer','[data-followup="true"]','.followup-spoken','.followup-answer'].map(key=>[key,element()]));
    fields.textarea.id='input-'+id+(transfer?'-transfer':'');
    fields['.time'].value='5';
    const ratings=[element(),element(),element()];
    const result={dataset:{q:id,transfer:String(transfer)},querySelector:key=>fields[key]||null,querySelectorAll:()=>ratings,fields,ratings};
    fields.textarea.matches=()=>true;fields.textarea.closest=()=>result;
    return result;
  }
  function click(card,dataset) {const b=element();b.dataset=dataset;b.closest=()=>card;events.click({target:{closest:()=>b}});return b;}
  function navigate(to){context.location.hash='#view='+to;windowEvents.hashchange();}
  return {context,nodes,state,card,click,navigate,events,store,intervals,advance(ms){now+=ms;for(const fn of intervals.values())fn();}};
}

const t=boot({data:{'eet-circuits-progress':'{"1":true}'}});
const data=t.context.window.ENGLISH_LAB;
assert.equal(data.chapters.length,10);assert.equal(data.roadmap.length,0);
assert.equal(data.exercises.length,120);
assert.equal(new Set(data.exercises.map(q=>q.id)).size,120);
for(const c of data.chapters){
  const qs=data.exercises.filter(q=>q.chapter===c.id);
  assert.equal(qs.length,12);
  for(const mode of ['build','transform','speak'])assert.equal(qs.filter(q=>q.mode===mode).length,4);
  assert.ok(c.concepts.length>=5);assert.ok(c.analyses.length>=3);
}
for(const q of data.exercises)for(const field of ['prompt','answer','pattern','explanation','error','alternative','transfer','transferAnswer'])assert.ok(q[field].trim(),q.id+': '+field);
assert.equal(new Set(data.exercises.map(q=>q.prompt)).size,120);
assert.equal(new Set(data.exercises.map(q=>q.transfer)).size,120);
assert.equal(t.nodes['#progress'].max,10);
assert.equal((t.nodes['#main'].innerHTML.match(/class="question"/g)||[]).length,12);
assert.equal((t.nodes['#main'].innerHTML.match(/class="feedback" hidden/g)||[]).length,12);
const c=t.card('c1-1');
t.click(c,{action:'reveal'});assert.equal(c.fields['.feedback'].hidden,true);
assert.ok(t.nodes['#notice'].textContent.includes('먼저'));
c.fields.textarea.value='   ';t.click(c,{action:'reveal'});assert.equal(c.fields['.feedback'].hidden,true);
c.fields.textarea.value='I am looking for a room close to school.';
t.events.input({target:c.fields.textarea});
t.click(c,{action:'reveal'});assert.equal(c.fields['.feedback'].hidden,false);
assert.ok(c.fields['.feedback'].innerHTML.includes(data.exercises[0].answer));
assert.ok(c.fields['.feedback'].innerHTML.includes('자동 채점 아님'));
t.click(c,{rating:'again'});
assert.equal(t.state().reviews['c1-1'].due,1800000600000);
assert.equal(t.state().attempts['c1-1'].rating,'again');
assert.equal(t.store['eet-circuits-progress'],'{"1":true}');
const persisted=boot({data:t.store});
assert.ok(persisted.nodes['#main'].innerHTML.includes('I am looking for a room close to school.'));
assert.equal((persisted.nodes['#main'].innerHTML.match(/class="feedback" hidden/g)||[]).length,12);
t.navigate('review');assert.ok(t.nodes['#main'].innerHTML.includes('현재 이 목록에 문제가 없습니다'));
t.click(null,{filter:'all'});assert.ok(t.nodes['#main'].innerHTML.includes(data.exercises[0].transfer));
const r=t.card('c1-1',true);r.fields['.spoken'].checked=true;
t.click(r,{action:'reveal'});assert.ok(r.fields['.feedback'].innerHTML.includes(data.exercises[0].transferAnswer));
t.click(r,{rating:'good'});assert.equal(t.state().reviews['c1-1'].due,1800000000000+86400000);
t.click(r,{rating:'good'});assert.equal(t.state().reviews['c1-1'].due,1800000000000+86400000,'same attempt must not advance review twice');
for(const days of [3,7,14,14]){
  const repeated=t.card('c1-1',true);t.click(repeated,{rating:'good'});
  assert.equal(t.state().reviews['c1-1'].due,1800000000000+days*86400000);
}
const hard=t.card('c1-1');t.click(hard,{rating:'hard'});assert.equal(t.state().reviews['c1-1'].level,0);
t.navigate('1');
const done={id:'complete',checked:true};t.events.change({target:done});assert.equal(done.checked,false);
for(const q of data.exercises.filter(q=>q.chapter===1)){const qc=t.card(q.id);t.click(qc,{rating:'good'});}
done.checked=true;t.events.change({target:done});assert.equal(t.state().done['1'],true);
assert.equal(t.nodes['#progress'].value,1);
const timer=t.card('c1-9');t.click(timer,{action:'timer'});assert.equal(t.intervals.size,1);
t.advance(5000);assert.equal(t.intervals.size,0);
assert.ok(timer.fields['.timer'].textContent.includes('시간 종료'));assert.equal(timer.fields['.feedback'].hidden,true);
t.click(timer,{action:'timer'});t.navigate('2');assert.equal(t.intervals.size,0);
const spoken=t.card('c2-9');spoken.fields['.spoken'].checked=true;t.click(spoken,{action:'reveal'});assert.equal(spoken.fields['.feedback'].hidden,false);
t.click(spoken,{action:'listen'});assert.ok(t.nodes['#notice'].textContent.includes('지원하지'));
t.click(spoken,{action:'mic'});assert.ok(t.nodes['#notice'].textContent.includes('지원하지'));
t.navigate('review');t.click(null,{remove:'c1-1'});assert.equal(t.state().reviews['c1-1'],undefined);
t.navigate('404');assert.ok(t.nodes['#main'].innerHTML.includes('아는 영어를'));
for(const chapter of data.chapters){
  t.navigate(String(chapter.id));
  assert.equal((t.nodes['#main'].innerHTML.match(/class="question"/g)||[]).length,12);
  assert.ok(t.nodes['#main'].innerHTML.includes(chapter.title));
  for(const q of data.exercises.filter(x=>x.chapter===chapter.id)){
    const qc=t.card(q.id);qc.fields.textarea.value='My independent answer.';t.click(qc,{action:'reveal'});
    assert.equal(qc.fields['.feedback'].hidden,false);
    assert.ok(qc.fields['.feedback'].innerHTML.includes('핵심 구조'));
    const tc=t.card(q.id,true);tc.fields['.spoken'].checked=true;t.click(tc,{action:'reveal'});
    assert.ok(tc.fields['.feedback'].innerHTML.includes(q.transferAnswer.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')));
  }
}
t.navigate('3');assert.ok(t.nodes['#main'].innerHTML.includes('data-view="4"'));
t.navigate('10');assert.ok(t.nodes['#main'].innerHTML.includes('복습으로'));
const follow=t.card('c10-9');follow.fields['.spoken'].checked=true;t.click(follow,{action:'reveal'});
assert.ok(follow.fields['.feedback'].innerHTML.includes('What has been the biggest adjustment?'));
t.click(follow,{action:'followup'});assert.equal(follow.fields['.followup-answer'].hidden,true);
follow.fields['[data-followup="true"]'].value='The weather has been the biggest adjustment.';
t.click(follow,{action:'followup'});assert.equal(follow.fields['.followup-answer'].hidden,false);
t.click(follow,{rating:'good'});t.click(follow,{action:'retry'});
assert.equal(follow.fields['.feedback'].hidden,true);assert.equal(follow.fields['.spoken'].checked,false);
assert.equal(follow.dataset.rated,undefined);assert.equal(follow.fields.textarea.value,'');
t.click(follow,{action:'reveal'});assert.equal(follow.fields['.feedback'].hidden,true);
const oldProgress=boot({data:{[KEY]:JSON.stringify({version:1,done:{1:true,2:true,3:true},drafts:{'c1-1':'My earlier answer.'},attempts:{'c1-1':{rating:'good'}}})}});
assert.equal(oldProgress.nodes['#progress'].value,3);assert.equal(oldProgress.nodes['#progress'].max,10);
assert.ok(oldProgress.nodes['#progress-label'].textContent.includes('30%'));
assert.ok(oldProgress.nodes['#main'].innerHTML.includes('My earlier answer.'));
const malicious=boot({data:{[KEY]:JSON.stringify({version:1,drafts:{'c1-1':'</textarea><img src=x onerror=alert(1)>'}})}});
assert.ok(!malicious.nodes['#main'].innerHTML.includes('<img src=x'));
assert.ok(malicious.nodes['#main'].innerHTML.includes('&lt;/textarea&gt;'));
assert.doesNotThrow(()=>boot({data:{[KEY]:'{broken'}}));
const denied=boot({broken:true});assert.ok(denied.nodes['#main'].innerHTML.includes('문장의 기본 구조'));
const deniedCard=denied.card('c1-1');denied.click(deniedCard,{action:'bookmark'});assert.doesNotThrow(()=>denied.navigate('review'));
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
for(const asset of ['content.js','content-expanded.js','app.js','styles.css']){assert.ok(html.includes('"'+asset+'"'));assert.ok(fs.existsSync(path.join(__dirname,asset)));}
assert.ok(html.indexOf('content.js')<html.indexOf('content-expanded.js'));
assert.ok(html.indexOf('content-expanded.js')<html.indexOf('app.js'));
const main=fs.readFileSync(path.join(__dirname,'../index.html'),'utf8');assert.ok(main.includes('href="english-speaking/"'));
console.log('PASS: 10 chapters / 120 unique exercises / 120 transfer tasks; all chapter rendering; input-before-reveal; spoken alternative; persistence and 3-to-10 chapter migration; isolated storage; spaced review 1/3/7/14 days; duplicate-rating guard; retry and follow-up gate; completion gate; timer expiry and cleanup; unsupported audio fallback; malformed/blocked storage; escaped drafts; relative assets and hub link.');
console.log('LIMIT: DOM stubs validate application logic, not real browser layout, microphone, TTS output or deployed HTTP routing.');
