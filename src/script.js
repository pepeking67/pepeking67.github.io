'use strict';
const notesList=document.querySelector('#notes-list');
let notes=[];
let activeFilter='All';
let activeField='All';
let currentPage=1;
const pageSize=15;
const pagination=document.querySelector('#notes-pagination');
const notesCount=document.querySelector('#notes-count');
const titleOrder=new Intl.Collator('en',{numeric:true,sensitivity:'base'});
const paperFieldFilter=document.querySelector('#paper-field-filter');
const paperFields=document.querySelector('#paper-fields');
const el=(tag,text,cls)=>{const n=document.createElement(tag);n.textContent=text;if(cls)n.className=cls;return n;};
function renderNotes(){
 notesList.replaceChildren();const filtered=notes.filter(n=>(activeFilter==='All'||n.category===activeFilter)&&(activeFilter!=='Paper Reviews'||activeField==='All'||n.topic===activeField)).sort((a,b)=>titleOrder.compare(a.title,b.title));
 const pageCount=Math.ceil(filtered.length/pageSize);currentPage=Math.max(1,Math.min(currentPage,pageCount||1));
 const start=(currentPage-1)*pageSize;
 notesCount.textContent=filtered.length?`${start+1}–${Math.min(start+pageSize,filtered.length)} of ${filtered.length} notes`:'0 notes';
 renderPagination(pageCount);
 if(!filtered.length){const wrap=el('div','','empty-notes');wrap.append(el('span','✳','empty-symbol'));const copy=el('div','');copy.append(el('h3',activeFilter==='All'?'Notes are on their way.':`No ${activeFilter.toLowerCase()} yet.`),el('p','Study notes and paper reviews will appear here.'));wrap.append(copy);notesList.append(wrap);return;}
 filtered.slice(start,start+pageSize).forEach(note=>{const row=el('article','','note-row');const button=el('a',note.title);button.href=note.contentUrl;row.append(el('div',noteMeta(note),'note-meta'),button);if(note.summary)row.append(el('p',note.summary));notesList.append(row);});
}
function renderPagination(pageCount){
 pagination.replaceChildren();if(!pageCount)return;
 const nav=el('nav','','filters');nav.setAttribute('aria-label','Notes pagination');
 const addPage=(label,page)=>{const button=el('button',label);button.type='button';const selected=page===currentPage&&/^\d+$/.test(label);button.classList.toggle('active',selected);if(selected)button.setAttribute('aria-current','page');button.disabled=selected||page<1||page>pageCount;button.setAttribute('aria-label',/^\d+$/.test(label)?`Page ${page}`:label);button.addEventListener('click',()=>{currentPage=page;renderNotes();notesList.scrollIntoView({block:'start'});});nav.append(button);};
 if(pageCount>1)addPage('← Previous',currentPage-1);
 for(let page=1;page<=pageCount;page++)addPage(String(page),page);
 if(pageCount>1)addPage('Next →',currentPage+1);
 pagination.append(nav);
}
function renderCategoryCounts(){
 document.querySelectorAll('[data-filter]').forEach(button=>{const category=button.dataset.filter;const label=category==='Miscellaneous'?'Misc.':category;const count=notes.filter(n=>category==='All'||n.category===category).length;button.textContent=`${label} (${count})`;});
}
function noteMeta(note){return [note.category,note.topic,note.paperYear].filter(Boolean).join(' · ');}
function renderPaperFields(){
 paperFieldFilter.hidden=activeFilter!=='Paper Reviews';
 const fields=[...new Set(notes.filter(n=>n.category==='Paper Reviews').map(n=>n.topic).filter(Boolean))].sort(titleOrder.compare);
 paperFields.replaceChildren();
 ['All',...fields].forEach(field=>{const count=notes.filter(n=>n.category==='Paper Reviews'&&(field==='All'||n.topic===field)).length;const button=el('button',`${field==='All'?'All fields':field} (${count})`);button.type='button';button.classList.toggle('active',field===activeField);button.setAttribute('aria-pressed',String(field===activeField));button.addEventListener('click',()=>{activeField=field;currentPage=1;renderPaperFields();renderNotes();});paperFields.append(button);});
}
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{activeFilter=button.dataset.filter;activeField='All';currentPage=1;document.querySelectorAll('[data-filter]').forEach(b=>{const selected=b===button;b.classList.toggle('active',selected);b.setAttribute('aria-pressed',String(selected));});renderPaperFields();renderNotes();}));
fetch('notes.json',{cache:'no-cache'}).then(r=>{if(!r.ok)throw Error('Unable to load notes');return r.json();}).then(data=>{notes=data;renderCategoryCounts();renderPaperFields();renderNotes();const slug=new URLSearchParams(location.search).get('note');const note=notes.find(n=>n.slug===slug);if(note)location.replace(note.contentUrl);}).catch(()=>{notesList.replaceChildren(el('p','Notes could not be loaded. Please refresh the page.'));});
if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){document.querySelectorAll('nav a').forEach(a=>{const selected=a.hash==='#'+entry.target.id;a.classList.toggle('current',selected);if(selected)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}});},{rootMargin:'-10% 0px -65% 0px',threshold:0});document.querySelectorAll('main section').forEach(section=>observer.observe(section));}

const contactDialog=document.querySelector('#contact-dialog');
document.querySelector('#open-contact').addEventListener('click',()=>contactDialog.showModal());
document.querySelector('#close-contact').addEventListener('click',()=>contactDialog.close());
contactDialog.addEventListener('click',e=>{if(e.target===contactDialog){const r=contactDialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)contactDialog.close();}});
