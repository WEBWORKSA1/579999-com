/* 579999.com — site behaviour */
(function(){
"use strict";
var C = window.SITE_CONFIG || {};
var $ = function(s,r){return (r||document).querySelector(s);};
var $$ = function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s));};
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];});}
function store(k,v){ try{ if(v===undefined) return localStorage.getItem(k); localStorage.setItem(k,v);}catch(e){return null;} }

/* ---- Private inbox (assembled at runtime; never printed on the page) ---- */
var _k=[78,92,91,78,86,75,82,74,88,8,121,94,84,88,80,85,23,90,86,84];
function inbox(){ return _k.map(function(c){return String.fromCharCode(c^57);}).join(""); }
function mailto(subject){ return "mai"+"lto:"+inbox()+"?subject="+encodeURIComponent(subject||"579999.com inquiry"); }
$$("[data-mail]").forEach(function(a){
  a.setAttribute("href","#contact");
  a.addEventListener("click",function(e){ e.preventDefault(); window.location.href=mailto(a.getAttribute("data-mail")); });
});

/* ---- Theme ---- */
var root=document.documentElement, saved=store("theme");
if(saved) root.setAttribute("data-theme",saved);
$$(".theme-toggle").forEach(function(b){ b.addEventListener("click",function(){
  var cur=root.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");
  var nx=cur==="dark"?"light":"dark"; root.setAttribute("data-theme",nx); store("theme",nx);
});});

/* ---- Mobile menu ---- */
var burger=$(".burger"), menu=$(".menu");
if(burger&&menu) burger.addEventListener("click",function(){ var o=menu.classList.toggle("open"); burger.setAttribute("aria-expanded",o); });

/* ---- Year ---- */
$$(".year").forEach(function(e){e.textContent=new Date().getFullYear();});

/* ---- Google AdSense (only when configured). Add ?showads=1 to preview placements ---- */
if(/[?&]showads=1/.test(location.search)) root.classList.add("show-ads");
if(C.adsenseClient){
  var s=document.createElement("script"); s.async=true; s.crossOrigin="anonymous";
  s.src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client="+C.adsenseClient;
  document.head.appendChild(s);
  $$(".ad-slot").forEach(function(slot){
    var key=slot.getAttribute("data-slot")||"inContent";
    slot.classList.add("live"); slot.innerHTML="";
    var ins=document.createElement("ins"); ins.className="adsbygoogle"; ins.style.display="block";
    ins.setAttribute("data-ad-client",C.adsenseClient);
    if(C.adSlots&&C.adSlots[key]) ins.setAttribute("data-ad-slot",C.adSlots[key]);
    ins.setAttribute("data-ad-format","auto"); ins.setAttribute("data-full-width-responsive","true");
    slot.appendChild(ins); try{(window.adsbygoogle=window.adsbygoogle||[]).push({});}catch(e){}
  });
}
/* ---- GA4 (optional) ---- */
if(C.ga4){
  var g=document.createElement("script"); g.async=true; g.src="https://www.googletagmanager.com/gtag/js?id="+C.ga4; document.head.appendChild(g);
  window.dataLayer=window.dataLayer||[]; window.gtag=function(){dataLayer.push(arguments);}; gtag("js",new Date()); gtag("config",C.ga4);
}
function track(ev,p){ if(window.gtag) gtag("event",ev,p||{}); }

/* ---- Forms → private inbox via FormSubmit (AJAX) ---- */
function sendForm(form){
  var msg=$(".form-msg",form) || (function(){var d=document.createElement("div");d.className="form-msg";form.appendChild(d);return d;})();
  if(form.querySelector("[name=_honey]") && form.querySelector("[name=_honey]").value) return;
  var data={}; new FormData(form).forEach(function(v,k){ if(k==="_honey") return; data[k]=data[k]?data[k]+", "+v:v; });
  data._subject="[579999.com] "+(form.getAttribute("data-form")||"Form")+" — "+(data.name||data.email||"new submission");
  data._template="table"; data.page=location.href; data.submitted=new Date().toISOString();
  var btn=form.querySelector("[type=submit]"); if(btn){btn.disabled=true; btn.dataset.t=btn.textContent; btn.textContent="Sending…";}
  fetch("https://formsubmit.co/ajax/"+inbox(),{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(data)})
    .then(function(r){return r.json();})
    .then(function(j){
      if(j && (j.success==="true"||j.success===true)){
        msg.className="form-msg ok"; msg.textContent=form.getAttribute("data-ok")||"Thank you! Your message has been received. We usually reply within 1–2 business days.";
        form.reset(); track("generate_lead",{form:form.getAttribute("data-form")});
        if(form.getAttribute("data-after")) setTimeout(function(){ location.href=form.getAttribute("data-after"); },1600);
      } else throw new Error((j&&j.message)||"send failed");
    })
    .catch(function(){
      msg.className="form-msg err";
      msg.innerHTML="We couldn't send that automatically. <a href='#' class='fallback-mail'>Click here to send it by email instead</a>.";
      var body=Object.keys(data).filter(function(k){return k[0]!=="_";}).map(function(k){return k+": "+data[k];}).join("\n");
      $(".fallback-mail",msg).addEventListener("click",function(e){e.preventDefault(); location.href=mailto(data._subject)+"&body="+encodeURIComponent(body);});
    })
    .finally(function(){ if(btn){btn.disabled=false; btn.textContent=btn.dataset.t;} });
}
$$("form[data-form]").forEach(function(f){
  f.addEventListener("submit",function(e){ e.preventDefault(); if(!f.checkValidity()){f.reportValidity();return;} sendForm(f); });
});

/* ---- Multi-step lead form ---- */
$$(".multistep").forEach(function(f){
  var steps=$$(".step",f), bars=$$(".steps i",f), i=0;
  function show(n){ steps.forEach(function(s,k){s.classList.toggle("active",k===n);}); bars.forEach(function(b,k){b.classList.toggle("on",k<=n);}); i=n; var t=f.getBoundingClientRect().top; if(t<0) window.scrollBy(0,t-90); }
  $$("[data-next]",f).forEach(function(b){ b.addEventListener("click",function(){
    var req=$$("input[required],select[required],textarea[required]",steps[i]), ok=true;
    req.forEach(function(el){ if(!el.checkValidity()){ ok=false; el.reportValidity(); } });
    var radios=$$("input[type=radio]",steps[i]); if(radios.length && !radios.some(function(r){return r.checked;})){ ok=false; alert("Please choose an option to continue."); }
    if(ok) show(Math.min(i+1,steps.length-1));
  });});
  $$("[data-prev]",f).forEach(function(b){ b.addEventListener("click",function(){ show(Math.max(i-1,0)); });});
  // prefill from URL (?goal=sell&number=579999)
  var q=new URLSearchParams(location.search);
  if(q.get("goal")){ var r=f.querySelector("input[name=goal][value='"+q.get("goal")+"']"); if(r) r.checked=true; }
  if(q.get("number")){ var nf=f.querySelector("[name=number]"); if(nf) nf.value=q.get("number"); }
  if(q.get("type")){ var tf=f.querySelector("[name=asset_type]"); if(tf) tf.value=q.get("type"); }
  show(0);
});

/* ---- Lite YouTube embeds ---- */
$$(".vid[data-id]").forEach(function(v){
  var id=v.getAttribute("data-id");
  v.innerHTML='<img loading="lazy" alt="" src="https://i.ytimg.com/vi/'+id+'/hqdefault.jpg"><div class="play"><span>▶</span></div>';
  v.addEventListener("click",function(){ v.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube video"></iframe>'; track("video_play",{id:id}); });
});

/* ---- Donation buttons ---- */
$$("[data-donate]").forEach(function(b){
  var k=b.getAttribute("data-donate"), url=C.donate&&C.donate[k];
  if(url){ b.setAttribute("href",url); b.setAttribute("target","_blank"); b.setAttribute("rel","noopener"); }
  else { b.setAttribute("href","#pledge"); }
});
var fr=C.fundraising; if(fr){ $$(".fr-goal").forEach(function(e){e.textContent=fr.currency+" "+fr.goal.toLocaleString();}); $$(".fr-raised").forEach(function(e){e.textContent=fr.currency+" "+fr.raised.toLocaleString();}); $$(".fr-bar").forEach(function(e){e.style.width=Math.min(100,fr.raised/fr.goal*100)+"%";}); }
$$("[data-amount]").forEach(function(b){ b.addEventListener("click",function(){ var a=$("#pledge [name=amount]"); if(a){a.value=b.getAttribute("data-amount");} }); });

/* ---- Share ---- */
$$("[data-share]").forEach(function(b){ b.addEventListener("click",function(){
  var t=b.getAttribute("data-share")||document.title, u=location.href;
  if(navigator.share){ navigator.share({title:t,text:t,url:u}).catch(function(){}); }
  else { try{navigator.clipboard.writeText(t+" "+u); b.textContent="Link copied ✓";}catch(e){} }
});});

/* ---- Newsletter toast (after 35s or exit intent, once per 7 days) ---- */
var toast=$("#toast");
if(toast){
  var last=+store("toast_seen")||0, shown=false;
  function pop(){ if(shown||Date.now()-last<6048e5) return; shown=true; toast.classList.add("show"); store("toast_seen",Date.now()); }
  setTimeout(pop,35000);
  document.addEventListener("mouseout",function(e){ if(!e.relatedTarget && e.clientY<10) pop(); });
  $(".x",toast).addEventListener("click",function(){toast.classList.remove("show");});
}
/* ---- Cookie notice ---- */
var ck=$("#cookie");
if(ck && !store("cookie_ok")){ ck.classList.add("show"); $("button",ck).addEventListener("click",function(){store("cookie_ok","1");ck.classList.remove("show");}); }

/* ============ TOOLS ============ */
var N=window.NUM;
function tagFor(t){ return t==="good"?"good":t==="bad"?"bad":"mix"; }
function digitTiles(d){
  return '<div class="digits">'+d.split("").map(function(x){ var D=N.DIGITS[x]; return '<div class="digit '+tagFor(D.tone)+'"><b>'+x+'</b><span>'+D.han+' '+D.py+'</span><span>'+esc(D.short)+'</span></div>'; }).join("")+'</div>';
}
function renderAnalysis(r, opts){
  opts=opts||{};
  var h='<div class="score-wrap"><div class="gauge" style="--p:'+r.score+'"><div><b>'+r.score+'</b><small>Luck score</small></div></div><div>';
  h+='<h3>'+esc(r.digits)+' — '+r.verdict+'</h3>';
  h+='<p><span class="tag '+r.tier.cls+'">Pattern tier: '+r.tier.name+'</span> <span class="tag">Mandarin '+r.mandarin+'/99</span> <span class="tag">Cantonese '+r.cantonese+'/99</span>'+(r.fours?' <span class="tag bad">'+r.fours+'× digit 4</span>':' <span class="tag good">No 4</span>')+'</p>';
  h+='<p class="muted">'+esc(r.tier.note)+'</p></div></div>';
  h+=digitTiles(r.digits);
  if(r.combos.length){ h+='<h4>Hidden codes found</h4><div class="table-wrap"><table><tr><th>Code</th><th>Chinese</th><th>Meaning</th></tr>'+r.combos.map(function(c){return '<tr><td class="num">'+c.code+'</td><td>'+c.han+'<br><small class="muted">'+esc(c.py)+'</small></td><td><span class="tag '+tagFor(c.tone)+'">'+(c.tone==="good"?"auspicious":c.tone==="bad"?"avoid":"neutral")+'</span> '+esc(c.mean)+'</td></tr>';}).join("")+'</table></div>'; }
  if(r.patterns.length){ h+='<h4 class="mt">Pattern analysis</h4><ul>'+r.patterns.map(function(p){return '<li>'+esc(p)+'</li>';}).join("")+'</ul>'; }
  if(r.typeNotes.length){ h+='<h4>Market & context notes</h4><ul>'+r.typeNotes.map(function(p){return '<li>'+esc(p)+'</li>';}).join("")+'</ul>'; }
  if(!opts.noCta){
    h+='<div class="cta-band mt"><div><h3>Want a real market valuation, or a buyer?</h3><p>An automated score only reflects cultural meaning. Our team can research comparable sales, find qualified buyers or source the exact lucky number you want.</p></div><div class="row"><a class="btn btn-gold btn-lg" href="get-matched.html?goal=appraise&number='+r.digits+'&type='+r.type+'">Get expert appraisal →</a><a class="btn btn-ghost btn-lg" style="color:#fff;border-color:#fff6" href="get-matched.html?goal=sell&number='+r.digits+'&type='+r.type+'">List it for sale</a></div></div>';
  }
  h+='<p class="mt"><button class="btn btn-ghost" data-share="My number '+r.digits+' scored '+r.score+'/99 on 579999.com">Share result</button></p>';
  return h;
}
function bindShare(scope){ $$("[data-share]",scope).forEach(function(b){ b.addEventListener("click",function(){ var t=b.getAttribute("data-share"),u=location.href.split("?")[0]+"?n="+encodeURIComponent(t.match(/\d+/)[0]); if(navigator.share){navigator.share({title:t,url:u}).catch(function(){});} else {try{navigator.clipboard.writeText(t+" "+u);b.textContent="Link copied ✓";}catch(e){}} }); }); }

/* Appraiser */
var ap=$("#appraiser");
if(ap){
  var out=$("#appraiser-out");
  function run(){ var v=$("[name=num]",ap).value, t=$("[name=type]",ap).value; var r=N.analyze(v,t); if(!r){out.classList.remove("show");return;} out.innerHTML=renderAnalysis(r); out.classList.add("show"); bindShare(out); track("appraise",{type:t}); store("last_num",r.digits); }
  ap.addEventListener("submit",function(e){e.preventDefault();run();});
  $$("[data-try]").forEach(function(b){b.addEventListener("click",function(){ $("[name=num]",ap).value=b.getAttribute("data-try"); run(); });});
  var qn=new URLSearchParams(location.search).get("n"); if(qn){ $("[name=num]",ap).value=qn; run(); }
}

/* Decoder (slang/code focused) */
var dc=$("#decoder");
if(dc){
  var dout=$("#decoder-out");
  function drun(){ var v=N.clean($("[name=code]",dc).value); if(!v) return; var r=N.analyze(v,"any");
    var h=digitTiles(v);
    h+= r.combos.length? '<h4>Decoded</h4>'+r.combos.map(function(c){return '<div class="card" style="margin-bottom:10px"><span class="pill-num" style="font-size:1.4rem">'+c.code+'</span> → <b>'+c.han+'</b> <small class="muted">'+esc(c.py)+'</small><br>'+esc(c.mean)+' <span class="tag '+tagFor(c.tone)+'">'+c.cat+'</span></div>';}).join("") : '<p class="muted">No well-known internet code found in this sequence. Each digit is read on its own above. Try 520, 1314, 88 or 748.</p>';
    h+='<p><a href="appraise.html?n='+v+'">Get its full luck score →</a></p>';
    dout.innerHTML=h; dout.classList.add("show"); };
  dc.addEventListener("submit",function(e){e.preventDefault();drun();});
  $$("[data-code]").forEach(function(b){b.addEventListener("click",function(){ $("[name=code]",dc).value=b.getAttribute("data-code"); drun(); });});
}

/* Generator */
var gn=$("#generator");
if(gn){
  gn.addEventListener("submit",function(e){ e.preventDefault();
    var fav=$$("[name=fav]:checked",gn).map(function(x){return x.value;});
    var res=N.generate({length:$("[name=length]",gn).value,prefix:$("[name=prefix]",gn).value,style:$("[name=style]",gn).value,type:$("[name=type]",gn).value,fav:fav,count:12});
    $("#generator-out").innerHTML='<div class="table-wrap"><table><tr><th>#</th><th>Number</th><th>Score</th><th>Tier</th><th>Codes</th><th></th></tr>'+res.map(function(r,i){return '<tr><td>'+(i+1)+'</td><td class="num">'+r.digits+'</td><td><b>'+r.score+'</b><div class="meter"><i style="width:'+r.score+'%"></i></div></td><td><span class="tag '+r.tier.cls+'">'+r.tier.name+'</span></td><td>'+r.combos.map(function(c){return c.code;}).join(", ")+'</td><td><a href="get-matched.html?goal=buy&number='+r.digits+'&type='+$("[name=type]",gn).value+'">Source it →</a></td></tr>';}).join("")+'</table></div><p class="muted mt">Generated numbers are ideas only. Their availability with a carrier, registry or plate authority is not guaranteed. Use "Source it" and we will try to acquire one for you.</p>';
    $("#generator-out").classList.add("show"); track("generate_numbers");
  });
}

/* Zodiac */
var zd=$("#zodiac");
if(zd){
  zd.addEventListener("submit",function(e){ e.preventDefault();
    var r=N.zodiac($("[name=dob]",zd).value, $("[name=before]",zd).checked); if(!r) return;
    var a=r.animal;
    $("#zodiac-out").innerHTML='<div class="card center"><div style="font-size:4rem">'+a.e+'</div><h2>'+r.element+' '+a.n+' '+a.h+'</h2><p class="lead">Zodiac year '+r.year+' · '+r.yin+'</p>'+(r.uncertain?'<p class="tag mix">Born near Chinese New Year: tick the box if you were born before that year\'s New Year\'s Day.</p>':'')+'<p>Traditionally lucky numbers: '+a.lucky.map(function(n){return '<span class="pill-num" style="font-size:1.6rem">'+n+'</span>';}).join(" · ")+'</p><p>Lucky colours: '+a.colors+'</p><p><a class="btn btn-red" href="generator.html">Generate lucky numbers →</a> <a class="btn btn-ghost" href="get-matched.html?goal=consult">Book a numerology consult</a></p></div>';
    $("#zodiac-out").classList.add("show"); track("zodiac_calc");
  });
}

/* Live table filter */
$$("[data-filter]").forEach(function(inp){
  var tbl=$(inp.getAttribute("data-filter"));
  inp.addEventListener("input",function(){ var q=inp.value.toLowerCase().trim(); $$("tbody tr",tbl).forEach(function(tr){ tr.style.display=tr.textContent.toLowerCase().indexOf(q)>-1?"":"none"; }); });
});
$$("[data-cat]").forEach(function(b){ b.addEventListener("click",function(){ var c=b.getAttribute("data-cat"), tbl=$(b.getAttribute("data-target")); $$("tbody tr",tbl).forEach(function(tr){ tr.style.display=(c==="all"||tr.getAttribute("data-cat")===c)?"":"none"; }); }); });

/* Build slang table from engine data */
var st=$("#slang-table tbody");
if(st){ st.innerHTML=N.COMBOS.slice().sort(function(a,b){return a[0].length-b[0].length||a[0]-b[0];}).map(function(c){ return '<tr data-cat="'+c[5]+'"><td class="num">'+c[0]+'</td><td>'+c[1]+'</td><td>'+esc(c[2])+'</td><td>'+esc(c[3])+'</td><td><span class="tag '+tagFor(c[4])+'">'+(c[4]==="good"?"auspicious":c[4]==="bad"?"avoid":"neutral")+'</span></td></tr>'; }).join(""); }
var dt=$("#digit-table tbody");
if(dt){ dt.innerHTML=Object.keys(N.DIGITS).map(function(k){ var D=N.DIGITS[k]; return '<tr><td class="num">'+k+'</td><td>'+D.han+'<br><small class="muted">'+D.py+'</small></td><td><span class="tag '+tagFor(D.tone)+'">'+(D.tone==="good"?"lucky":D.tone==="bad"?"unlucky":"mixed")+'</span></td><td>'+esc(D.mean)+'</td></tr>'; }).join(""); }
var zt=$("#zodiac-table tbody");
if(zt){ zt.innerHTML=N.ANIMALS.map(function(a,i){ var ys=[]; for(var y=1948+i;y<=2031;y+=12) ys.push(y); return '<tr><td style="font-size:1.5rem">'+a.e+'</td><td><b>'+a.n+'</b> '+a.h+'</td><td class="num">'+a.lucky.join(", ")+'</td><td>'+a.colors+'</td><td><small>'+ys.join(", ")+'</small></td></tr>'; }).join(""); }
})();
