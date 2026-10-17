'use strict';
// Original image bytes are grouped into local files and fetched near the viewport.
const imagePacks=new Map();
async function loadNoteImage(image){
 const pack=image.dataset.imagePack,key=image.dataset.imageKey;
 try{
  if(!imagePacks.has(pack))imagePacks.set(pack,fetch(pack).then(response=>{if(!response.ok)throw Error('Unable to load images');return response.json();}));
  const images=await imagePacks.get(pack);if(!images[key])throw Error('Missing image');
  image.src=images[key];image.removeAttribute('data-image-pack');
 }catch(error){imagePacks.delete(pack);image.alt=image.alt||'Image could not be loaded. Reload this page to retry.';}
}
const packedImages=document.querySelectorAll('img[data-image-pack]');
if('IntersectionObserver' in window){
 const imageObserver=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){imageObserver.unobserve(entry.target);loadNoteImage(entry.target);}});},{rootMargin:'800px'});
 packedImages.forEach(image=>imageObserver.observe(image));
}else packedImages.forEach(loadNoteImage);
