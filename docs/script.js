'use strict';
const notesList=document.querySelector('#notes-list');
const dialog=document.querySelector('#note-dialog');
let notes=[];
let activeFilter='All';
const el=(tag,text,cls)=>{const n=document.createElement(tag);n.textContent=text;if(cls)n.className=cls;return n;};
function renderNotes(){
 notesList.replaceChildren();const filtered=notes.filter(n=>activeFilter==='All'||n.category===activeFilter);
 if(!filtered.length){const wrap=el('div','','empty-notes');wrap.append(el('span','✳','empty-symbol'));const copy=el('div','');copy.append(el('h3',activeFilter==='All'?'Notes are on their way.':`No ${activeFilter.toLowerCase()} yet.`),el('p','Study notes and paper reviews will appear here.'));wrap.append(copy);notesList.append(wrap);return;}
 filtered.forEach(note=>{const row=el('article','','note-row');const button=el('button',note.title);button.type='button';button.addEventListener('click',()=>openNote(note));row.append(el('div',`${note.category} · ${note.date}`,'note-meta'),button,el('p',note.summary||''));notesList.append(row);});
}
function openNote(note){const content=document.querySelector('#note-content');content.replaceChildren(el('h1',note.title),el('p',`${note.category} · ${note.date}`,'note-meta'));const body=el('div','');body.innerHTML=note.html;content.append(body);dialog.showModal();dialog.scrollTop=0;history.replaceState(null,'',`?note=${encodeURIComponent(note.slug)}#notes`);}
document.querySelector('#close-note').addEventListener('click',()=>dialog.close());
dialog.addEventListener('close',()=>history.replaceState(null,'',location.pathname+'#notes'));
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{activeFilter=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>{const selected=b===button;b.classList.toggle('active',selected);b.setAttribute('aria-pressed',String(selected));});renderNotes();}));
fetch('notes.json').then(r=>{if(!r.ok)throw Error('Unable to load notes');return r.json();}).then(data=>{notes=data;renderNotes();const slug=new URLSearchParams(location.search).get('note');const note=notes.find(n=>n.slug===slug);if(note)openNote(note);}).catch(()=>{notesList.replaceChildren(el('p','Notes could not be loaded. Please refresh the page.'));});
if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){document.querySelectorAll('nav a').forEach(a=>{const selected=a.hash==='#'+entry.target.id;a.classList.toggle('current',selected);if(selected)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}});},{rootMargin:'-10% 0px -65% 0px',threshold:0});document.querySelectorAll('main section').forEach(section=>observer.observe(section));}

const contactDialog=document.querySelector('#contact-dialog');
document.querySelector('#open-contact').addEventListener('click',()=>contactDialog.showModal());
document.querySelector('#close-contact').addEventListener('click',()=>contactDialog.close());
contactDialog.addEventListener('click',e=>{if(e.target===contactDialog){const r=contactDialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)contactDialog.close();}});
