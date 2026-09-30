/* 579999.com — Number intelligence engine (client-side, no server needed) */
(function(){
"use strict";

var DIGITS = {
  "0":{han:"零",py:"líng",m:0.5,c:0.5,tone:"mix",short:"wholeness",mean:"Sounds like 灵 (líng, 'spirit / efficacious'). Also 'nothing', so it reads as neutral-to-positive, a sense of completeness."},
  "1":{han:"一",py:"yī / yāo",m:0.5,c:0.5,tone:"mix",short:"unity · 'want'",mean:"Stands for being first, unique and whole. In phone numbers it is read yāo, which sounds like 要 (yào, 'want / will'). That is why 18 reads 'will prosper'."},
  "2":{han:"二",py:"èr",m:1,c:1.5,tone:"good",short:"pairs · easy",mean:"'Good things come in pairs' (好事成双). In Cantonese, 二 (yi6) sounds like 易 ('easy')."},
  "3":{han:"三",py:"sān",m:0,c:1.5,tone:"mix",short:"life (Canto.)",mean:"In Mandarin, 三 can sound like 散 (sǎn, 'to scatter'). In Cantonese, saam1 sounds like 生 (saang1, 'life / birth'), which makes it lucky in Hong Kong and Guangdong."},
  "4":{han:"四",py:"sì",m:-3,c:-3,tone:"bad",short:"death",mean:"Sounds like 死 (sǐ, 'death') in both Mandarin and Cantonese. It is the most avoided digit: some buildings skip 4th, 14th and 24th floors, and numbers without a 4 sell at a premium."},
  "5":{han:"五",py:"wǔ",m:0,c:-0.5,tone:"mix",short:"me · five elements",mean:"Sounds like 吾/我 ('I, me') and appears in many internet codes (520 = I love you). It links to the Five Elements (五行). In Cantonese, ng5 sounds like 唔 ('not'), which can reverse the meaning of the digits that follow."},
  "6":{han:"六",py:"liù",m:2,c:1.5,tone:"good",short:"smooth flow",mean:"Sounds like 流 (liú, 'flow') and 禄 (lù, 'fortune / salary'). 六六大顺 means 'everything goes smoothly'. Online, 666 means 'awesome'."},
  "7":{han:"七",py:"qī",m:0.5,c:-1,tone:"mix",short:"rise · togetherness",mean:"Sounds like 起 ('to rise'), 气 ('vital energy') and 妻 ('wife'). The 7th lunar month is Ghost Month, and in Cantonese the digit has a vulgar slang sense. Whether it reads as lucky depends on context."},
  "8":{han:"八",py:"bā",m:3,c:3,tone:"good",short:"prosperity",mean:"Sounds like 发 (fā, 'to prosper / get rich'). It is the luckiest digit. The Beijing Olympics opened on 08/08/08 at 8:08 pm."},
  "9":{han:"九",py:"jiǔ",m:2.5,c:1.5,tone:"good",short:"forever",mean:"Sounds like 久 (jiǔ, 'long-lasting / forever'). It is the highest single digit and was historically tied to the Emperor. It is a favourite for weddings and for long-lived businesses."}
};

/* code, chinese, pinyin/reading, meaning, polarity (good|bad|mix), category */
var COMBOS = [
 ["579999","我妻久久久久","wǒ qī jiǔ jiǔ jiǔ jiǔ","'My wife, forever and ever', or read as 吾起久久久久 'I rise, lasting forever'. The brand number of this site.","good","love"],
 ["5201314","我爱你一生一世","wǒ ài nǐ yīshēng yīshì","I love you for a lifetime","good","love"],
 ["1314920","一生一世就爱你","yīshēng yīshì jiù ài nǐ","A lifetime, I'll only love you","good","love"],
 ["131420","一生一世爱你","yīshēng yīshì ài nǐ","Love you for a lifetime","good","love"],
 ["3344","生生世世","shēngshēng shìshì","Forever and ever, across lifetimes","good","love"],
 ["3399","长长久久","chángcháng jiǔjiǔ","Long and lasting, a classic wedding red-envelope amount","good","love"],
 ["1314","一生一世","yīshēng yīshì","For a whole lifetime","good","love"],
 ["9999","久久久久","jiǔ jiǔ jiǔ jiǔ","Forever and ever: the strongest 'lasting' pattern. 9999 is also the mark for 99.99% pure gold.","good","luck"],
 ["8888","发发发发","fā fā fā fā","Prosperity ×4, a top-tier wealth pattern","good","wealth"],
 ["6666","六六大顺","liù liù dà shùn","Everything goes perfectly smoothly","good","luck"],
 ["8013","伴你一生","bàn nǐ yīshēng","By your side for life","good","love"],
 ["7758","亲亲我吧","qīn qīn wǒ ba","Kiss me","good","love"],
 ["1711","一心一意","yīxīn yīyì","Wholehearted devotion","good","love"],
 ["1688","一路发发","yī lù fā fā","Prosper all the way, again and again","good","wealth"],
 ["5188","我要发发","wǒ yào fā fā","I will prosper big","good","wealth"],
 ["6688","顺顺发发","shùn shùn fā fā","Smooth and prosperous","good","wealth"],
 ["1818","要发要发","yào fā yào fā","Going to prosper, going to prosper","good","wealth"],
 ["7456","气死我了","qì sǐ wǒ le","I'm furious","bad","slang"],
 ["9494","就是就是","jiù shì jiù shì","Exactly! Totally agree","mix","slang"],
 ["999","久久久","jiǔ jiǔ jiǔ","Very long-lasting","good","luck"],
 ["888","发发发","fā fā fā","Triple prosperity","good","wealth"],
 ["666","溜溜溜 / 六六六","liù liù liù","Awesome, skilful, smooth (internet slang)","good","slang"],
 ["168","一路发","yī lù fā","Prosper all the way, a favourite for business numbers","good","wealth"],
 ["518","我要发","wǒ yào fā","I will prosper","good","wealth"],
 ["520","我爱你","wǒ ài nǐ","I love you. 20 May is China's online Valentine's Day.","good","love"],
 ["521","我愿意 / 我爱你","wǒ yuànyì","I'm willing / I love you","good","love"],
 ["530","我想你","wǒ xiǎng nǐ","I miss you","good","love"],
 ["596","我走了","wǒ zǒu le","I'm leaving (chat)","mix","slang"],
 ["687","对不起","duìbuqǐ","Sorry","mix","slang"],
 ["886","拜拜了","bàibài le","Bye then (chat)","mix","slang"],
 ["748","去死吧","qù sǐ ba","Go die (insult)","bad","slang"],
 ["514","我要死","wǒ yào sǐ","I want to die / I'm dying (exaggeration)","bad","slang"],
 ["484","是不是","shì bu shì","Is it or not?","mix","slang"],
 ["250","二百五","èr bǎi wǔ","Idiot, a half-wit (insult)","bad","slang"],
 ["233","哈哈哈","—","LOL (from an old forum laughing emoticon #233)","mix","slang"],
 ["555","呜呜呜","wū wū wū","Crying sounds","mix","slang"],
 ["99","久久","jiǔ jiǔ","Long-lasting","good","luck"],
 ["88","发发 / 拜拜","fā fā / bàibài","Double prosperity, or 'bye-bye' in chat","good","wealth"],
 ["66","顺顺","shùn shùn","Smooth and easy","good","luck"],
 ["58","我发","wǒ fā","I prosper","good","wealth"],
 ["57","我妻 / 吾起","wǒ qī / wú qǐ","'My wife' in informal internet readings, or 'I rise'","good","love"],
 ["28","易发","yì fā (Cantonese)","Easy to prosper. Hong Kong plate '28' sold for HK$18.1M.","good","wealth"],
 ["18","要发","yāo bā → yào fā","Will prosper","good","wealth"],
 ["54","我死 / 唔死","wǒ sǐ / m4 sei2","Mandarin 'I die', Cantonese 'won't die'. Reading depends on dialect.","mix","luck"],
 ["38","三八","sān bā","A derogatory word for a gossipy woman (avoid)","bad","slang"],
 ["14","要死","yào sǐ","Want to die, one reason floor 14 is skipped","bad","luck"],
 ["13","十三点","shísān diǎn","Silly / daft (Shanghainese slang)","bad","slang"]
];

var ANIMALS = [
 {n:"Rat",h:"鼠",e:"🐀",lucky:[2,3],colors:"blue, gold, green"},
 {n:"Ox",h:"牛",e:"🐂",lucky:[1,4],colors:"white, yellow, green"},
 {n:"Tiger",h:"虎",e:"🐅",lucky:[1,3,4],colors:"blue, grey, orange"},
 {n:"Rabbit",h:"兔",e:"🐇",lucky:[3,4,6],colors:"red, pink, purple, blue"},
 {n:"Dragon",h:"龙",e:"🐉",lucky:[1,6,7],colors:"gold, silver, greyish white"},
 {n:"Snake",h:"蛇",e:"🐍",lucky:[2,8,9],colors:"black, red, yellow"},
 {n:"Horse",h:"马",e:"🐎",lucky:[2,3,7],colors:"yellow, green"},
 {n:"Goat",h:"羊",e:"🐐",lucky:[3,4,9],colors:"brown, red, purple"},
 {n:"Monkey",h:"猴",e:"🐒",lucky:[4,9],colors:"white, blue, gold"},
 {n:"Rooster",h:"鸡",e:"🐓",lucky:[5,7,8],colors:"gold, brown, yellow"},
 {n:"Dog",h:"狗",e:"🐕",lucky:[3,4,9],colors:"red, green, purple"},
 {n:"Pig",h:"猪",e:"🐖",lucky:[2,5,8],colors:"yellow, grey, brown, gold"}
];
/* Chinese New Year (Gregorian) dates, month-day, for boundary births */
var CNY = {1960:"01-28",1961:"02-15",1962:"02-05",1963:"01-25",1964:"02-13",1965:"02-02",1966:"01-21",1967:"02-09",1968:"01-30",1969:"02-17",
1970:"02-06",1971:"01-27",1972:"02-15",1973:"02-03",1974:"01-23",1975:"02-11",1976:"01-31",1977:"02-18",1978:"02-07",1979:"01-28",
1980:"02-16",1981:"02-05",1982:"01-25",1983:"02-13",1984:"02-02",1985:"02-20",1986:"02-09",1987:"01-29",1988:"02-17",1989:"02-06",
1990:"01-27",1991:"02-15",1992:"02-04",1993:"01-23",1994:"02-10",1995:"01-31",1996:"02-19",1997:"02-07",1998:"01-28",1999:"02-16",
2000:"02-05",2001:"01-24",2002:"02-12",2003:"02-01",2004:"01-22",2005:"02-09",2006:"01-29",2007:"02-18",2008:"02-07",2009:"01-26",
2010:"02-14",2011:"02-03",2012:"01-23",2013:"02-10",2014:"01-31",2015:"02-19",2016:"02-08",2017:"01-28",2018:"02-16",2019:"02-05",
2020:"01-25",2021:"02-12",2022:"02-01",2023:"01-22",2024:"02-10",2025:"01-29",2026:"02-17",2027:"02-06",2028:"01-26",2029:"02-13",2030:"02-03"};
var ELEMENTS = ["Metal","Metal","Water","Water","Wood","Wood","Fire","Fire","Earth","Earth"];

function clean(s){ return String(s||"").replace(/[^0-9]/g,""); }

function findCombos(d){
  var out=[], used={};
  COMBOS.forEach(function(c){
    var i=d.indexOf(c[0]);
    if(i>-1 && !used[c[0]]){
      // skip sub-combos fully covered by an already-found longer combo at same place
      var covered = out.some(function(o){ return o.code.length>c[0].length && o.code.indexOf(c[0])>-1 && d.indexOf(o.code)>-1; });
      if(!covered){ out.push({code:c[0],han:c[1],py:c[2],mean:c[3],tone:c[4],cat:c[5]}); used[c[0]]=1; }
    }
  });
  return out;
}

function patterns(d){
  var p=[], pts=0, n=d.length;
  if(!n) return {list:p,pts:0};
  // longest run of identical digits
  var best=1,cur=1,bestDigit=d[0];
  for(var i=1;i<n;i++){ if(d[i]===d[i-1]){cur++; if(cur>best){best=cur;bestDigit=d[i];}} else cur=1; }
  // trailing run
  var tail=1; for(var j=n-1;j>0 && d[j]===d[j-1];j--) tail++;
  if(bestDigit==="4" && best>=2){ p.push("Repeated 4s ("+best+"×): amplifies the 'death' sound, so most Chinese buyers avoid it"); pts-=20*best; }
  else if(n>1 && best===n){ p.push("Solid "+n+"-digit repeat ("+d+"): the rarest pattern class"); pts+=100; }
  else {
    if(best>=5){ p.push(best+"× repeat of "+bestDigit); pts+=80; }
    else if(best===4){ p.push("Quad repeat "+bestDigit+bestDigit+bestDigit+bestDigit); pts+=60; }
    else if(best===3){ p.push("Triple repeat "+bestDigit+bestDigit+bestDigit); pts+=35; }
    if(tail>=3 && d[n-1]!=="4"){ p.push("Strong ending: last "+tail+" digits identical (the ending carries the most weight)"); pts+=10; }
  }
  if(n>=4){
    var t=d.slice(-4);
    if(t[0]===t[1]&&t[2]===t[3]&&t[1]!==t[2]){ p.push("AABB ending ("+t+")"); pts+=25; }
    if(t[0]===t[2]&&t[1]===t[3]&&t[0]!==t[1]){ p.push("ABAB ending ("+t+")"); pts+=25; }
  }
  if(n>=4 && d===d.split("").reverse().join("")){ p.push("Palindrome: reads the same both ways"); pts+=25; }
  var asc=1,desc=1,ma=1,md=1;
  for(var k=1;k<n;k++){
    if(+d[k]===+d[k-1]+1){asc++;ma=Math.max(ma,asc);}else asc=1;
    if(+d[k]===+d[k-1]-1){desc++;md=Math.max(md,desc);}else desc=1;
  }
  if(ma>=4){ p.push("Ascending run of "+ma+" (步步高, 'rising step by step')"); pts+=25; }
  if(md>=4){ p.push("Descending run of "+md); pts+=10; }
  if(d.indexOf("4")===-1 && n>=4){ p.push("No digit 4: preferred by Chinese buyers"); pts+=8; }
  if(d.indexOf("4")===-1 && d.indexOf("0")===-1 && n===6){ p.push("No 0 and no 4: part of the 262,144-combo 'premium 6N' set that numeric-domain investors track"); pts+=5; }
  var last=d[n-1];
  if(last==="8"||last==="9"||last==="6"){ p.push("Ends in "+last+" ("+DIGITS[last].short+")"); pts+=6; }
  if(last==="4"){ p.push("Ends in 4: the weakest possible ending"); pts-=15; }
  return {list:p,pts:pts};
}

function tierOf(pts){
  if(pts>=100) return {name:"Legendary",cls:"good",note:"Collector grade. Numbers like this reach auction headlines."};
  if(pts>=58) return {name:"Elite",cls:"good",note:"High-demand pattern. Get an expert appraisal before you sell."};
  if(pts>=30) return {name:"Premium",cls:"good",note:"Clearly above-average pattern with real resale appeal."};
  if(pts>=15) return {name:"Notable",cls:"mix",note:"Some attractive features. Value depends heavily on context."};
  return {name:"Standard",cls:"mix",note:"Everyday number. Its value is mostly personal meaning."};
}

function analyze(input, type){
  var d=clean(input);
  if(!d) return null;
  var combos=findCombos(d);
  // digits inside a well-known auspicious code (e.g. the 4 in 1314) are read as part of the phrase, not alone
  var mask=[]; combos.forEach(function(c){ if(c.tone==="good"&&c.code.length>=3){ var i=d.indexOf(c.code); for(var q=i;q<i+c.code.length;q++) mask[q]=1; } });
  function val(x,i,k){ var v=DIGITS[x][k]; return mask[i]?Math.max(v,1):v; }
  var ms=0,cs=0,tw=0,tc=0,L=d.length,T=Math.min(4,L);
  d.split("").forEach(function(x,i){ ms+=val(x,i,"m"); cs+=val(x,i,"c"); if(i>=L-T){ tw+=val(x,i,"m"); tc+=val(x,i,"c"); } });
  // weight the last 4 digits more heavily (as buyers do)
  var mAvg=(ms/L)*0.6+(tw/T)*0.4;
  var cAvg=(cs/L)*0.6+(tc/T)*0.4;
  var cb=0; combos.forEach(function(c){ cb += c.tone==="good"? Math.min(6,c.code.length*1.5) : c.tone==="bad"? -8 : 0; });
  var pat=patterns(d);
  function toScore(avg){ return Math.round(Math.max(3,Math.min(99, ((avg+3)/6)*85 + cb + Math.min(18,pat.pts/5) ))); }
  var mScore=toScore(mAvg), cScore=toScore(cAvg);
  var overall=Math.round(mScore*0.65+cScore*0.35);
  var tier=tierOf(pat.pts + (combos.filter(function(c){return c.tone==="good"&&c.code.length>=3&&!/^(\d)\1+$/.test(c.code)&&c.code!=="579999";}).length*8));
  var fours=(d.match(/4/g)||[]).length;
  var verdict = overall>=85?"Exceptionally auspicious": overall>=72?"Very lucky": overall>=60?"Lucky": overall>=45?"Balanced / neutral":"Unfavourable in Chinese numerology";
  return {digits:d,type:type||"any",mandarin:mScore,cantonese:cScore,score:overall,verdict:verdict,combos:combos,patterns:pat.list,tier:tier,fours:fours,typeNotes:typeNotes(d,type)};
}

function typeNotes(d,type){
  var n=[];
  switch(type){
    case "phone":
      n.push("Buyers weight the last 4 digits most, then the last 8. Premium carriers and auction platforms price 'AAAA' and 'AAAAA' endings far above the rest.");
      n.push("Reference: in 2003 the number +86 28 8888 8888 sold to Sichuan Airlines for CN¥2.33 million (about US$280,000).");
      break;
    case "plate":
      n.push("For plates, shorter usually means more valuable. In Hong Kong the short numeric plates '28', '18' and '9' are among the priciest ever auctioned.");
      n.push("Reference: Hong Kong plate '28' sold for HK$18.1 million (about US$2.3M) in 2016.");
      break;
    case "domain":
      n.push(d.length<=3?"Numeric .com names of 1–3 digits are ultra-rare and trade as premium assets.":d.length<=5?"4–5 digit numeric .com names (4N/5N) are liquid in the Chinese investor market.":"6-digit .com (6N) names are a large, tradeable class. Patterns, no 0/4 and repeated 8s and 9s drive price.");
      n.push("Numeric domains are memorable in China, where Pinyin brands are harder to recall (examples: 58.com, 360.cn, 163.com).");
      break;
    case "address":
      n.push("Feng shui house-number practice often uses the total too. Reduce the number to a single digit to see its core energy.");
      n.push("Remedy for a '4' address that many practitioners suggest: frame the number inside a circle or pair it with a strong-8 element.");
      break;
    case "price":
      n.push("Retail and real-estate prices in Chinese markets often end in 8 or 88 and avoid 4. Red-envelope gifts favour 168, 888, 1314 and 3399.");
      break;
    case "date":
      n.push("For event dates (weddings, launches), people favour dates containing 6, 8 and 9 and avoid 4. Also check the lunar calendar and the couple's zodiac.");
      break;
  }
  var sum=d.split("").reduce(function(a,b){return a+ +b;},0), root=sum; while(root>9) root=String(root).split("").reduce(function(a,b){return a+ +b;},0);
  n.push("Digit sum "+sum+" → root "+root+" ("+DIGITS[String(root)].short+").");
  return n;
}

/* ---------- Generator ---------- */
function rnd(a){ return a[Math.floor(Math.random()*a.length)]; }
function generate(opts){
  var len=Math.max(3,Math.min(12,+opts.length||8));
  var prefix=clean(opts.prefix||"").slice(0,len-2);
  var fav=(opts.fav&&opts.fav.length)?opts.fav:["6","8","9"];
  var pool=["0","1","2","3","5","6","7","8","9"]; // never 4
  var style=opts.style||"mixed", out={}, tries=0;
  var combos=["168","518","1314","520","5188","1688","6688","3399","888","999","9999","8888","58","28","18","66","99","88"];
  while(Object.keys(out).length<(opts.count||12) && tries<4000){
    tries++;
    var body="", need=len-prefix.length, s=style==="mixed"?rnd(["tail","aabb","abab","combo","asc","lucky","tail"]):style;
    if(s==="tail"){ var t=Math.min(need,rnd([3,4,4,5])); var dg=rnd(fav); while(body.length<need-t) body+=rnd(pool); body+=Array(t+1).join(dg); }
    else if(s==="aabb"){ var a=rnd(fav),b=rnd(fav.filter(function(x){return x!==a;}).concat(["6","8","9"].filter(function(x){return x!==a;}))); while(body.length<need-4) body+=rnd(pool); body+=a+a+b+b; }
    else if(s==="abab"){ var a2=rnd(fav),b2=rnd(pool.filter(function(x){return x!==a2;})); while(body.length<need-4) body+=rnd(pool); body+=a2+b2+a2+b2; }
    else if(s==="combo"){ var c=rnd(combos.filter(function(x){return x.length<=need;})); while(body.length<need-c.length) body+=rnd(pool); body+=c; }
    else if(s==="asc"){ var st=Math.floor(Math.random()*5)+1, run=""; for(var q=0;q<Math.min(need,5);q++){ var dd=(st+q)%10; if(dd===4) dd=5; run+=dd; } while(body.length<need-run.length) body+=rnd(pool); body+=run; }
    else { while(body.length<need) body+=rnd(fav.concat(["2","6","8","9"])); }
    var num=(prefix+body).slice(0,len);
    if(num.indexOf("4")>-1 && !prefix.match(/4/)) continue;
    if(!out[num]) out[num]=analyze(num,opts.type||"phone");
  }
  return Object.keys(out).map(function(k){return out[k];}).sort(function(x,y){return y.score-x.score;});
}

/* ---------- Zodiac ---------- */
function zodiac(dateStr, beforeCNY){
  var dt=new Date(dateStr+"T12:00:00"); if(isNaN(dt)) return null;
  var y=dt.getFullYear(), md=dateStr.slice(5), zy=y, uncertain=false;
  if(CNY[y]){ if(md<CNY[y]) zy=y-1; }
  else if(md<"02-21"){ if(md<"01-21") zy=y-1; else { uncertain=true; if(beforeCNY) zy=y-1; } }
  var a=ANIMALS[((zy-4)%12+12)%12];
  return {year:zy, animal:a, element:ELEMENTS[((zy%10)+10)%10], yin:(zy%2===0)?"Yang":"Yin", uncertain:uncertain, cny:CNY[y]?(y+"-"+CNY[y]):null};
}

window.NUM = {DIGITS:DIGITS,COMBOS:COMBOS,ANIMALS:ANIMALS,CNY:CNY,analyze:analyze,generate:generate,zodiac:zodiac,clean:clean,findCombos:findCombos};
})();
