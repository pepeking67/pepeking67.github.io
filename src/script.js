'use strict';
const notesList=document.querySelector('#notes-list');
const dialog=document.querySelector('#note-dialog');
let notes=[];
let activeFilter='All';
const el=(tag,text,cls)=>{const n=document.createElement(tag);n.textContent=text;if(cls)n.className=cls;return n;};
function renderNotes(){
 notesList.replaceChildren();const filtered=notes.filter(n=>activeFilter==='All'||n.category===activeFilter);
 if(!filtered.length){const wrap=el('div','','empty-notes');wrap.append(el('span','✳','empty-symbol'));const copy=el('div','');copy.append(el('h3',activeFilter==='All'?'Notes are on their way.':`No ${activeFilter.toLowerCase()} yet.`),el('p','Study notes and paper reviews will appear here.'));wrap.append(copy);notesList.append(wrap);return;}
 filtered.forEach(note=>{const row=el('article','','note-row');const button=el('button',note.title);button.type='button';button.addEventListener('click',()=>openNote(note));row.append(el('div',noteMeta(note),'note-meta'),button);if(note.summary)row.append(el('p',note.summary));notesList.append(row);});
}
function noteMeta(note){return [note.category,note.topic,note.paperYear].filter(Boolean).join(' · ');}
let readerRequest=0;
async function openNote(note){
 const request=++readerRequest;
 const content=document.querySelector('#note-content');
 const title=el('h1',note.title);title.id='note-reader-title';
 content.replaceChildren(title,el('p',noteMeta(note),'note-meta'));
 if(note.authors)content.append(el('p',note.authors,'review-authors'));
 if(note.paperUrl){const links=el('div','','review-links');const paper=el('a','Paper ↗');paper.href=note.paperUrl;paper.target='_blank';paper.rel='noopener noreferrer';links.append(paper);content.append(links);}
 const body=el('div','Loading review…','reader-status');content.append(body);
 if(!dialog.open)dialog.showModal();dialog.scrollTop=0;
 history.replaceState(null,'',`?note=${encodeURIComponent(note.slug)}#notes`);
 try{const response=await fetch(note.contentUrl,{cache:'no-cache'});if(!response.ok)throw Error('Unable to load review');const rendered=await response.text();if(request!==readerRequest)return;body.className='review-body';body.innerHTML=rendered;}
 catch(error){if(request===readerRequest){body.replaceChildren(el('p','The review could not be loaded. Please try again.'));const retry=el('button','Try again');retry.type='button';retry.addEventListener('click',()=>openNote(note));body.append(retry);}}
}
document.querySelector('#close-note').addEventListener('click',()=>dialog.close());
dialog.addEventListener('close',()=>{readerRequest++;history.replaceState(null,'',location.pathname+'#notes');});
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{activeFilter=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>{const selected=b===button;b.classList.toggle('active',selected);b.setAttribute('aria-pressed',String(selected));});renderNotes();}));
fetch('notes.json',{cache:'no-cache'}).then(r=>{if(!r.ok)throw Error('Unable to load notes');return r.json();}).then(data=>{notes=data;renderNotes();const slug=new URLSearchParams(location.search).get('note');const note=notes.find(n=>n.slug===slug);if(note)openNote(note);}).catch(()=>{notesList.replaceChildren(el('p','Notes could not be loaded. Please refresh the page.'));});
if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){document.querySelectorAll('nav a').forEach(a=>{const selected=a.hash==='#'+entry.target.id;a.classList.toggle('current',selected);if(selected)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}});},{rootMargin:'-10% 0px -65% 0px',threshold:0});document.querySelectorAll('main section').forEach(section=>observer.observe(section));}

const contactDialog=document.querySelector('#contact-dialog');
document.querySelector('#open-contact').addEventListener('click',()=>contactDialog.showModal());
document.querySelector('#close-contact').addEventListener('click',()=>contactDialog.close());
contactDialog.addEventListener('click',e=>{if(e.target===contactDialog){const r=contactDialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)contactDialog.close();}});
