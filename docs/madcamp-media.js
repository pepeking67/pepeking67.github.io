'use strict';
// Load the byte-identical original recording only when the reader requests it.
document.querySelectorAll('[data-load-video]').forEach(button=>{
 button.addEventListener('click',async()=>{
  const container=button.closest('.note-video');
  const video=container.querySelector('video');
  const status=container.querySelector('[role="status"]');
  button.disabled=true;button.textContent='Loading video…';status.hidden=true;
  try{
   const manifestUrl=new URL(video.dataset.videoManifest,location.href);
   const response=await fetch(manifestUrl);
   if(!response.ok)throw Error('Unable to load video');
   const manifest=await response.json();
   const pieces=new Array(manifest.chunks.length);let next=0;
   async function worker(){
    while(next<manifest.chunks.length){
     const index=next++;const chunk=await fetch(new URL(manifest.chunks[index],manifestUrl));
     if(!chunk.ok)throw Error('Unable to load recording');
     pieces[index]=await chunk.arrayBuffer();
    }
   }
   await Promise.all(Array.from({length:4},worker));
   const blob=new Blob(pieces,{type:manifest.type});
   if(blob.size!==manifest.bytes)throw Error('Incomplete recording');
   const url=URL.createObjectURL(blob);video.src=url;video.hidden=false;button.hidden=true;
   window.addEventListener('pagehide',()=>URL.revokeObjectURL(url),{once:true});
   video.play().catch(()=>{});
  }catch(error){
   button.disabled=false;button.textContent='Retry video';
   status.hidden=false;status.textContent='The video could not be loaded. Please try again.';
  }
 });
});
