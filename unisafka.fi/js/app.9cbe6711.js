(function(t){function e(e){for(var n,r,o=e[0],c=e[1],u=e[2],l=0,d=[];l<o.length;l++)r=o[l],Object.prototype.hasOwnProperty.call(s,r)&&s[r]&&d.push(s[r][0]),s[r]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(t[n]=c[n]);p&&p(e);while(d.length)d.shift()();return i.push.apply(i,u||[]),a()}function a(){for(var t,e=0;e<i.length;e++){for(var a=i[e],n=!0,r=1;r<a.length;r++){var o=a[r];0!==s[o]&&(n=!1)}n&&(i.splice(e--,1),t=c(c.s=a[0]))}return t}var n={},r={app:0},s={app:0},i=[];function o(t){return c.p+"js/"+({Organizer:"Organizer",doorbell:"doorbell",footer:"footer",menu:"menu"}[t]||t)+"."+{Organizer:"3510d734",doorbell:"dbc2d99b",footer:"a6e753f0",menu:"c811a8b7"}[t]+".js"}function c(e){if(n[e])return n[e].exports;var a=n[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,c),a.l=!0,a.exports}c.e=function(t){var e=[],a={Organizer:1,footer:1,menu:1};r[t]?e.push(r[t]):0!==r[t]&&a[t]&&e.push(r[t]=new Promise((function(e,a){for(var n="css/"+({Organizer:"Organizer",doorbell:"doorbell",footer:"footer",menu:"menu"}[t]||t)+"."+{Organizer:"25b34bf0",doorbell:"31d6cfe0",footer:"e506eae9",menu:"018f8b80"}[t]+".css",s=c.p+n,i=document.getElementsByTagName("link"),o=0;o<i.length;o++){var u=i[o],l=u.getAttribute("data-href")||u.getAttribute("href");if("stylesheet"===u.rel&&(l===n||l===s))return e()}var d=document.getElementsByTagName("style");for(o=0;o<d.length;o++){u=d[o],l=u.getAttribute("data-href");if(l===n||l===s)return e()}var p=document.createElement("link");p.rel="stylesheet",p.type="text/css",p.onload=e,p.onerror=function(e){var n=e&&e.target&&e.target.src||s,i=new Error("Loading CSS chunk "+t+" failed.\n("+n+")");i.code="CSS_CHUNK_LOAD_FAILED",i.request=n,delete r[t],p.parentNode.removeChild(p),a(i)},p.href=s;var f=document.getElementsByTagName("head")[0];f.appendChild(p)})).then((function(){r[t]=0})));var n=s[t];if(0!==n)if(n)e.push(n[2]);else{var i=new Promise((function(e,a){n=s[t]=[e,a]}));e.push(n[2]=i);var u,l=document.createElement("script");l.charset="utf-8",l.timeout=120,c.nc&&l.setAttribute("nonce",c.nc),l.src=o(t);var d=new Error;u=function(e){l.onerror=l.onload=null,clearTimeout(p);var a=s[t];if(0!==a){if(a){var n=e&&("load"===e.type?"missing":e.type),r=e&&e.target&&e.target.src;d.message="Loading chunk "+t+" failed.\n("+n+": "+r+")",d.name="ChunkLoadError",d.type=n,d.request=r,a[1](d)}s[t]=void 0}};var p=setTimeout((function(){u({type:"timeout",target:l})}),12e4);l.onerror=l.onload=u,document.head.appendChild(l)}return Promise.all(e)},c.m=t,c.c=n,c.d=function(t,e,a){c.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},c.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},c.t=function(t,e){if(1&e&&(t=c(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(c.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)c.d(a,n,function(e){return t[e]}.bind(null,n));return a},c.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return c.d(e,"a",e),e},c.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},c.p="/",c.oe=function(t){throw console.error(t),t};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],l=u.push.bind(u);u.push=e,u=u.slice();for(var d=0;d<u.length;d++)e(u[d]);var p=l;i.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"009f":function(t,e,a){"use strict";var n=a("b44b"),r=a.n(n);r.a},"0146":function(t,e,a){},"025e":function(t,e,a){"use strict";a.d(e,"a",(function(){return n})),a.d(e,"b",(function(){return r}));a("e260"),a("2532"),a("1276"),a("ddb0");function n(){if("fonts"in document){var t=new FontFace("Signika","url(https://fonts.gstatic.com/s/signika/v8/vEFR2_JTCgwQ5ejvG1EmBg.woff2)",{style:"normal",weight:"400"});t.load(),t.loaded.then(()=>{console.log("signikaFace loaded")}),document.fonts.add(t),document.fonts.ready.then(()=>{console.log("document.fonts.ready"),document.body.classList+=" fonts-loaded"})}else console.log("document.fonts NOT supported")}function r(t){var e=window.document.body.className.split(" ");!t&&e.includes("dark")?window.document.body.className=e.filter(t=>"dark"!==t).join(" "):t&&!e.includes("dark")&&(window.document.body.className=[...e,"dark"].join(" "))}},"18be":function(t,e,a){},"1e2d":function(t,e,a){t.exports=a.p+"img/en-flag.ac002e83.png"},"204f":function(t,e,a){},"25cf":function(t,e,a){"use strict";var n=a("5f78"),r=a.n(n);r.a},"25ef":function(t,e,a){"use strict";var n=a("94af"),r=a.n(n);e["default"]=r.a},3574:function(t,e,a){"use strict";var n=a("0146"),r=a.n(n);r.a},4360:function(t,e,a){"use strict";var n={};a.r(n),a.d(n,"GET_CURRENT_DAY",(function(){return d})),a.d(n,"GET_ALL_DAYS",(function(){return p})),a.d(n,"GET_SINGLE_DAY",(function(){return m})),a.d(n,"CHOOSE_DAY",(function(){return h})),a.d(n,"FLUSH_CACHE",(function(){return g})),a.d(n,"CHECK_SUNDAY",(function(){return b}));var r={};a.r(r),a.d(r,"currentData",(function(){return w})),a.d(r,"currentOrder",(function(){return _})),a.d(r,"isResHidden",(function(){return A})),a.d(r,"currentHiddenKeys",(function(){return y})),a.d(r,"currentShowKeys",(function(){return k}));var s={};a.r(s),a.d(s,"CHOOSE_CAMPUS",(function(){return S})),a.d(s,"CHOOSE_DAY",(function(){return C})),a.d(s,"CHOOSE_DIET",(function(){return T})),a.d(s,"CHOOSE_DIET_FILTER_TYPE",(function(){return x})),a.d(s,"CHOOSE_DIET_FILTER_LOGICAL_AND",(function(){return D})),a.d(s,"CHOOSE_SETTING",(function(){return j})),a.d(s,"SET_NEW_ORDER",(function(){return L})),a.d(s,"SET_DAY_TO_ERR",(function(){return I})),a.d(s,"TOGGLE_RES_VISIBILITY",(function(){return M})),a.d(s,"SET_NEW_HIDDENS_FOR_CAMPUS",(function(){return H})),a.d(s,"BUST_CACHE_VERSION",(function(){return N})),a.d(s,"INVALIDATE_DATA",(function(){return R})),a.d(s,"SET_HIDE_WHOLE_RES",(function(){return B})),a.d(s,"HIDE_CUSTOM_CAMPUS_INFO_MSG",(function(){return Y})),a.d(s,"INCREASE_VISIT_COUNT",(function(){return P})),a.d(s,"HIDE_TOOLTIP",(function(){return U})),a.d(s,"SET_LANGUAGE",(function(){return F})),a.d(s,"REVERT_PREFS",(function(){return V}));var i=a("2b0e"),o=a("2f62"),c=a("0e44"),u=(a("c975"),a("e6cf"),a("f3f3")),l=a("4570"),d=t=>{var{state:e,commit:a}=t;m({state:e,commit:a},e.current.dayName)},p=(t,e)=>{var{dispatch:a}=t;["ma","ti","ke","to","pe","la","su"].forEach((t,n)=>{"su"===t&&e||setTimeout(()=>{a("GET_SINGLE_DAY",t)},100*n)})},f=t=>Object(u["a"])({},t["restaurants_tty"],{},t["restaurants_tay"],{},t["restaurants_tays"],{},t["restaurants_tamk"]),m=(t,e)=>{var{state:a,commit:n}=t,r=a.current.week,s=a.jsonData.version,o="/static/json/2021/".concat(r,"/").concat(s,"/").concat(e,".json"),c=a.jsonData[e];return c.week===r&&c.version===s?Promise.resolve():o in a.concurrent?void 0:(a.concurrent[o]=!0,fetch(o).then(t=>t.json()).then(t=>{Object.keys(t).forEach(e=>{0===e.indexOf("restaurants_")&&Object.keys(t[e]).forEach(a=>{t[e][a]["res"]=a})}),delete a.concurrent[o],s===a.jsonData.version&&(a.jsonData.week=a.current.week,a.jsonData.year=a.current.year,t.week=r,t.version=s,t["restaurants_oma"]=f(t),i["a"].set(a.jsonData,e,t))}).catch(t=>{n("SET_DAY_TO_ERR",e)}))},h=(t,e)=>{var{state:a,commit:n,dispatch:r}=t;n("CHOOSE_DAY",e),Object.keys(a.jsonData[e]).length<2&&r("GET_SINGLE_DAY",e)},v=(t,e)=>{var a="/static/json/".concat(e,"/").concat(t,"/v.json");return fetch(a,{headers:{"cache-control":"no-cache",pragma:"no-cache"}}).then(t=>t.json()).then(t=>parseInt(t["v"]))},g=t=>{var{state:e,dispatch:a,commit:n}=t,{year:r,week:s}=e.current;return v(s,r).then(t=>{var i=e.jsonData.version;console.log("".concat(s,": ").concat(i," => ").concat(t)),t&&parseInt(t)!==parseInt(i)&&(n("BUST_CACHE_VERSION",t),a("GET_ALL_DAYS"),Object(l["c"])("".concat(r,"-").concat(s,"-").concat(t)),Object(l["a"])("".concat(r,"-").concat(s),t))}).catch(t=>{console.log("fetchVersion::catch"),console.log(t)})},b=t=>{var{state:e,dispatch:a}=t,n=new Date,r=n.getWeek()+1;n.isSunday()&&v(r,n.getFullYear()).then(t=>{!t||e.jsonData.version===t&&e.current.week===r||(console.log("Bumb week..."),e.jsonData.version=t,e.current.week=n.getWeek()+1,e.days.forEach(t=>{"su"!==t&&i["a"].set(e.jsonData,t,{})}),a("GET_ALL_DAYS",!0),e.showSundayBanner=!0)}).catch(t=>{console.log("TMRS V NOT AVAILABLE",t)})},w=(a("2532"),t=>{var e="restaurants_".concat(t.prefs.campus),a=t.jsonData[t.current.dayName];return e in a?a[e]:"error"in a?a:{}}),_=(t,e)=>{var a=t.prefs.campus,n=Object.keys(e.currentData);if(a in t.prefs.orders){var r=t.prefs.orders[a];if(r.length>0){var s=n.filter(t=>-1===r.indexOf(t));return r.concat(s)}}return n},A=t=>e=>{var a=t.prefs.hiddens[t.prefs.campus];return!!a&&-1!==a.indexOf(e)},y=t=>t.prefs.hiddens[t.prefs.campus]||[],k=(t,e)=>{var a=e.currentHiddenKeys;return e.currentOrder.filter(t=>!a.includes(t))},O=(a("fb6a"),a("025e")),E=(t,e)=>(-1===t.indexOf(e)?t.push(e):t=t.filter(t=>t!==e),t),S=(t,e)=>{t.prefs.campus=e.toLowerCase(),Object(l["b"])("campus")},C=(t,e)=>{t.current.dayName=e,Object(l["b"])("day")},T=(t,e)=>{t.prefs.dietFilters=E(t.prefs.dietFilters.slice(),e),Object(l["b"])("diet")},x=(t,e)=>{t.prefs.dietFilterType=e,Object(l["b"])("dietFilterType")},D=(t,e)=>{t.prefs.dietFilterLogicalAnd=e,Object(l["b"])("dietLogicalAnd")},j=(t,e)=>{t.prefs[e]=!t.prefs[e];var a="dark"===e;a&&Object(O["b"])(t.prefs["dark"]),Object(l["b"])(a?"toggleDark":e)},L=(t,e)=>{i["a"].set(t.prefs.orders,t.prefs.campus,e)},I=(t,e)=>{t.jsonData[e].error=!0},M=(t,e)=>{var a=t.prefs.campus;t.prefs.hiddens[a]||i["a"].set(t.prefs.hiddens,a,[]),t.prefs.hiddens[a]=E(t.prefs.hiddens[a],e)},H=(t,e)=>{t.prefs.hiddens[t.prefs.campus]||i["a"].set(t.prefs.hiddens,t.prefs.campus,[]),t.prefs.hiddens[t.prefs.campus]=e},N=(t,e)=>{t.jsonData.version=parseInt(e)},R=(t,e)=>{var a=new Date;(!a.isSunday()||a.isSunday()&&t.current.week!=a.getWeek()+1)&&(t.current.year=a.getFullYear(),t.current.week=a.getWeek()),e&&(t.current.dayName=t.days[a.getDay()]),t.jsonData.week!==t.current.week&&(t.jsonData.version=1,t.days.forEach(e=>{i["a"].set(t.jsonData,e,{})}))},B=(t,e)=>{t.prefs.hideWholeRes=e},Y=t=>{t.prefs.hideCustomCampusMsg=!0},P=t=>{t.prefs.visitCount+=1},U=(t,e)=>{var a={settings:"hideSettingsMsg"};t.prefs[a[e]]=!0,Object(l["b"])("tooltip:".concat(e))},F=(t,e)=>{t.prefs.lang=e,window.setDoorbellLanguage(e),Object(l["b"])("toggleLang")},V=t=>{var{prefsReverted:e,visitCount:a}=t.prefs;0===a?t.prefs.prefsReverted=!0:0===a||e||(t.prefs.prefsReverted=!0,t.prefs.showDiets=!0,t.prefs.showPrices=!0,t.prefs.showGroups=!0)};a.d(e,"a",(function(){return X})),i["a"].use(o["a"]),Date.prototype.getWeek=function(){var t=this,e=new Date(t.valueOf()),a=(t.getDay()+6)%7;e.setDate(e.getDate()-a+3);var n=e.valueOf();return e.setMonth(0,1),4!==e.getDay()&&e.setMonth(0,1+(4-e.getDay()+7)%7),1+Math.ceil((n-e)/6048e5)},Date.prototype.isSunday=function(){return 0===(new Date).getDay()};var z=["su","ma","ti","ke","to","pe","la"],Q=window,q=document,W=q.documentElement,J=q.getElementsByTagName("body")[0],G=Q.innerWidth||W.clientWidth||J.clientWidth,X={HIGH:"high",ONLY:"only",HIDE:"hide"};e["b"]=new o["a"].Store({state:{mobile:G<990,showSundayBanner:!1,days:z,campuses:["TTY","TAY","TAYS","TAMK","OMA"],current:{dayName:null,week:null,year:null},diets:["G","L","M","KASV","VEG"],dietFilterTypes:[{name:X.HIGH,text:"highlight"},{name:X.ONLY,text:"showOnly"},{name:X.HIDE,text:"hide"}],prefs:{lang:"fi",campus:null,orders:{},hiddens:{},hideWholeRes:!1,dietFilters:[],dietFilterType:X.HIGH,dietFilterLogicalAnd:!0,showGroups:!0,showDiets:!0,showPrices:!0,hideCustomCampusMsg:!1,hideSettingsMsg:!1,visitCount:0,dark:!1,prefsReverted:!1},concurrent:{},jsonData:{version:1,week:1,year:2021,ma:{},ti:{},ke:{},to:{},pe:{},la:{},su:{}}},mutations:s,actions:n,getters:r,plugins:[Object(c["a"])({paths:["prefs","jsonData"]})]})},4570:function(t,e,a){"use strict";a.d(e,"e",(function(){return o})),a.d(e,"d",(function(){return c})),a.d(e,"b",(function(){return u})),a.d(e,"c",(function(){return l})),a.d(e,"a",(function(){return d}));var n=a("4360"),r=()=>window.ga&&ga.create,s=(t,e,a)=>{setTimeout(()=>{r()&&ga("send","event",{eventCategory:t,eventAction:e,eventLabel:a})},2e3)},i=()=>s("piirto","kampus",n["b"].state.prefs.campus);function o(t){i();var e=(new Date).getDate();window.__gaVueFireD!==e&&(window.__gaVueFireD=e,setTimeout(()=>{d(),p(),m(t)},2500))}function c(){s("piirto","ekakerta",n["b"].state.prefs.campus)}function u(t){s("piirto","toiminnot",t)}function l(t){s("stats","cacheBusted","cb-".concat(t))}function d(){s("stats","version","".concat(n["b"].state.current.week,"::").concat(n["b"].state.jsonData.version))}function p(){s("stats","bundle","MODERN")}var f=(t,e)=>{s("prefs",t,e)};function m(t){"en"===t.lang&&f("lang","en"),t.dark&&f("theme","dark"),t.showGroups||f("hideGroups",!0),t.showDiets||f("hideDiets",!0),t.showPrices||f("hidePrices",!0),0!==t.dietFilters.length&&f("dietFilters",!0)}},"56d7":function(t,e,a){"use strict";a.r(e);a("e6cf"),a("2532"),a("1276");var n=a("2b0e"),r=a("a925"),s=a("376c"),i=a("4360"),o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("transition",{attrs:{appear:"","appear-class":"root-appear","appear-to-class":"root-appear-to","appear-active-class":"root-appear-active"}},[a("div",{attrs:{id:"root_app"}},[t.showStartScreen?[a("StartScreen")]:[a("TopBar"),a("Menu"),a("div",{staticClass:"d-flex justify-content-center m-2 mt-4 p-0"},[t.corona?a("div",{staticClass:"alert alert-warning p-3",staticStyle:{"text-align":"center","max-width":"800px"}},[t._v(" "+t._s(t.$t("corona"))+" ")]):t._e()]),a("transition",{attrs:{name:"bounce"}},[t.showSundayBanner?a("div",{staticClass:"d-flex justify-content-center m-4",staticStyle:{"text-align":"center"}},[a("div",{staticClass:"alert alert-warning mb-0",attrs:{role:"alert"}},[t._v(" "+t._s(t.$t("next"))+" ")])]):t._e()]),a("div",{ref:"campus-slide-container",attrs:{id:"campus-slide-container"}},[a("transition",{attrs:{name:"campus-slide",mode:"out-in"}},[t.loading?[a("DotBouncer")]:t.dayErrorMsg?[a("div",{staticClass:"error-container"},[t._v(" Voi vitkale... "),a("br"),t._v(" Valitun päivän ruokalistojen lataamisessa tapahtui jonkinlainen virhe. Yritä ladata sivu uudelleen. ")])]:[a("Campus",{key:t.currentCampus+":"+t.currentDay})]],2)],1),a("Footer")]],2)])},c=[],u=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"d-flex start-screen-container justify-content-center"},[a("div",{staticClass:"p-2 actual-container"},[t._m(0),a("span",{staticClass:"note"},[t._v("(vanhat TTY, TAY, TAYS ja TAMK)")]),a("p",{staticClass:"mt-4"},[t._v("Aloita valitsemalla kampus!")]),a("div",{staticClass:"buttons"},t._l(["TTY","TAY","TAYS","TAMK","OMA"],(function(e){return a("button",{key:e,staticClass:"btn btn-sm btn-success",on:{click:function(a){return t.choose(e)}}},[t._v(" "+t._s(t.getCampusName(e))+" ")])})),0),t._m(1)])])},l=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("h3",[a("span",{staticClass:"tuni-t"},[t._v("(T)")]),t._v("Unisafka "),a("br"),a("span",{staticClass:"h3-tampere"},[t._v("Tampereen korkeakouluyhteisön ruokalistat ")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("p",{staticClass:"links"},[t._v(" Kampukset löytyvät myös suoraan osoitteista "),a("a",{attrs:{href:"/tty/"}},[t._v("unisafka.fi/tty")]),t._v(", "),a("a",{attrs:{href:"/tay/"}},[t._v("unisafka.fi/tay")]),t._v(", "),a("a",{attrs:{href:"/tays/"}},[t._v("unisafka.fi/tays")]),t._v(" ja "),a("a",{attrs:{href:"/tamk/"}},[t._v("unisafka.fi/tamk")])])}],d=a("4570"),p={name:"StartScreen",methods:{choose(t){this.$store.commit("CHOOSE_CAMPUS",t),Object(d["d"])()},getCampusName(t){return"TTY"===t?"Hervanta":"TAY"===t?"Keskusta":t}}},f=p,m=(a("009f"),a("2877")),h=Object(m["a"])(f,u,l,!1,null,"23fa5092",null),v=h.exports,g=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("transition",{attrs:{appear:"","appear-class":"campus-appear","appear-to-class":"campus-appear-to","appear-active-class":"campus-appear-active"}},[a("div",{},[a("div",{staticClass:"container mb-4 campus"},[a("div",{staticClass:"d-flex col-md-4",staticStyle:{"margin-bottom":"1.75rem"}},[a("div",{staticClass:"flex-grow-1"},[a("h2",[t._v(t._s(t.tuniKampus(t.campus)))])]),a("div",{staticClass:"d-flex align-items-center trigger",staticStyle:{cursor:"pointer"}},[a("i",{on:{click:t.toggleOrganizer}},[a("img",{staticClass:"organizer",attrs:{src:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAHeSURBVGhD7dm/S8NAHAXwuIggom7iKII/VgUXwcXFVVBB0L9BcBbEzUlEEQTBVRwVXAQXBxd3XQQRHFykij9A/PVebDBcr5c05r5JzD34QJNLaF7aa0LjubiUM51wArv+UkHDEufwBWdcETfcUVob6MKxoMQFdEHscCdpp6DmTyUY7vgJ9wIeQVckXOIaBqrrAh0QGe5c+XlpPaOgFmmHoIQJj3EVWkAbbvQA4TNgywTw/cJFmuEQggN+BfWTZIlg/AiaoCbBBpLUr1a4zB0MghquuwFuM8kVatT2EnhW1cQpswgcX/eXcpyoMrPAsS1/KedhmQPgAfNnOBxjkZ4MdIMpLLMJK/7Sb4xFOCBNd0GMk8giH3Al4BasFsnygthIylOE90C6SZm2abBaRJqVIrxhk7YDSWIsUqSUo8hQBvogScox2TnwDrpJmbZLsFrEXdkbjCtSTWSRJxgXsABWi0izUuQ4A2uQJMYiRUo5iugmpW3DkCTlmOwceIN9AXwKZbVIUS6Ic/AvimwD91/2l5TkpcgYTNUxAxvAu/QX6IWa5KHICHB9FD47mQdtuMEz6M5E2paA76cWaQX+16v7gaA94NOqfqibcGMpSeeIMbozYJv6L7uLi4uLKZ73DY6xi9sJ1zHpAAAAAElFTkSuQmCC"}})])])]),t.showCustomCampusInfo?a("div",{staticClass:"alert alert-primary alert-dismissible"},[a("span",{domProps:{innerHTML:t._s(t.$t("oma"))}}),a("button",{staticClass:"close",attrs:{type:"button","aria-label":"Close"},on:{click:t.hideMsg}},[a("span",{attrs:{"aria-hidden":"true"}},[t._v("×")])])]):t._e(),a("transition",{attrs:{name:"organizer"}},[t.showOrganizer?a("RestaurantOrganizer"):t._e()],1),a("div",{staticClass:"row m-0"},[t._l(t.orderedData,(function(t){return[a("Restaurant",{key:t.res,attrs:{restaurant:t}})]}))],2)],1)])])},b=[],w=a("b75f"),_=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-md-4 restaurant-outer-container"},[a("div",{staticClass:"d-flex name-hours-row"},[a("div",{staticClass:"restaurant-name"},[a("a",{class:{hidden:t.hidden},attrs:{href:t.restaurant.rurli,target:"_BLANK"}},[t._v(t._s(t.restaurant.restaurant))])]),t.hidden?t._e():a("div",{staticClass:"ml-auto hours-outer"},[t._v(" "+t._s(t.restaurant.eating_hours)+" "),t.restaurant.open_hours?[t._v(" ("+t._s(t.restaurant.open_hours)+")")]:t._e()],2)]),t.hidden?t._e():[t.restaurant.out_of_campus?a("div",{staticClass:"out-of-campus"},[t._v(" "+t._s(t.$t("outsideCampus"))+" ")]):t._e(),t.restaurant.open_today?[t.restaurant.lisainfo?[a("div",{staticClass:"lisainfoboksi_yla"},[t._v(" "+t._s(t.restaurant.lisainfo)+" ")])]:t._e(),a("div",{staticClass:"meal_box"},t._l(t.meals,(function(e,n){return a("Meal",{key:"meal-"+n,attrs:{meal:e,prefs:t.prefs}})})),1)]:[a("div",{staticClass:"mealit"},[a("div",{},[t.restaurant.lisainfo?[t._v(" "+t._s(t.restaurant.lisainfo)+" ")]:[t._v(t._s(t.$t("closed")))]],2)])]]],2)},A=[],y=(a("e260"),a("498a"),a("ddb0"),a("f3f3")),k=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"meal"},[a("div",{staticClass:"d-flex title-price"},[t.prefs.showGroups?a("div",{staticClass:"meal-group"},[t._v(" "+t._s(t.meal.kok)+" ")]):t._e(),t.prefs.showPrices?a("div",{staticClass:"ml-auto meal-price"},[t._v(" "+t._s(t.meal.price)+" ")]):t._e()]),a("div",{staticClass:"d-flex flex-column"},t._l(t.meal.mo,(function(e){return a("div",{class:{"highlight-meal":e.high}},[a("div",{key:e.mpn,staticClass:"meal-name"},[t._v(" "+t._s(e.mpn)+" ")]),t.prefs.showDiets?a("div",{key:e.mpn+"d",staticClass:"meal-diet"},[t._v(" "+t._s(e.mpd)+" ")]):t._e()])})),0)])},O=[],E={name:"Meal",props:["meal","prefs"],data(){return{iconDietOk:w["f"]}},computed:{dietFiltersInUse(){return!(0===this.prefs.dietFilters.length)&&this.prefs.dietFilterType===i["a"].HIGH}}},S=E,C=(a("82fc"),Object(m["a"])(S,k,O,!1,null,"432aaeca",null)),T=C.exports,x={name:"Restaurant",props:["restaurant"],components:{Meal:T},computed:{meals(){var t=this.prefs.dietFilters,e=this.prefs.dietFilterLogicalAnd,a="fi"===this.$root.$i18n.locale?this.restaurant.meals:this.restaurant.meals_en;return a.filter(t=>t.mo.length>0).map(t=>Object(y["a"])({},t,{mo:[...t.mo]})).map(a=>0===t.length?a:Object(y["a"])({},a,{mo:a.mo.map(t=>Object(y["a"])({},t)).filter(a=>{var n=t.filter(t=>!a.mpd.split(",").map(t=>t.trim()).includes(t)),r=e?0!==n.length:n.length===t.length;switch(this.prefs.dietFilterType){case i["a"].HIGH:return a.high=!r,!0;case i["a"].ONLY:return!r;case i["a"].HIDE:return r;default:return!0}})})).filter(t=>t.mo.length>0)},prefs(){return this.$store.state.prefs},hidden(){return this.$store.getters.isResHidden(this.restaurant.res)},showYr(){return 48===this.$store.state.current.week}}},D=x,j=(a("3574"),a("7b0f")),L=Object(m["a"])(D,_,A,!1,null,"208f16b8",null);"function"===typeof j["default"]&&Object(j["default"])(L);var I=L.exports,M={components:{Restaurant:I,RestaurantOrganizer:()=>a.e("Organizer").then(a.bind(null,"1f08"))},data(){return{showOrganizer:!1,jarjestinOffsetObject:{marginTop:"0px !important"},joffsetOriginal:-400,joffset:-400,icoJarjesta:w["c"],eiExternal:w["b"],transitionFromLeftToRight:!0}},mounted(){Object(d["e"])(this.$store.state.prefs)},computed:{campus(){return this.$store.state.prefs.campus.toUpperCase()},currentData(){return this.$store.getters.currentData},orderedData(){var t=this.$store.state.prefs.hideWholeRes;return this.$store.getters.currentOrder.filter(e=>!t||!this.$store.getters.isResHidden(e)).map(t=>this.currentData[t]).filter(t=>!!t)},showCustomCampusInfo(){return"OMA"===this.campus&&!this.$store.state.prefs.hideCustomCampusMsg}},methods:{tuniKampus:function(t){return{TTY:"Hervanta (TTY)",TAY:"Keskusta (TAY)",TAYS:"TAYS",OMA:"OMA",TAMK:"TAMK"}[t]},toggleOrganizer:function(){this.showOrganizer?(this.joffset=this.joffsetOriginal,setTimeout(function(t){return function(){t.showOrganizer=!1}}(this),300)):(this.showOrganizer=!0,Object(d["b"])("JARJ"))},hideMsg(){this.$store.commit("HIDE_CUSTOM_CAMPUS_INFO_MSG")}}},H=M,N=(a("9f0e"),a("637a")),R=Object(m["a"])(H,g,b,!1,null,"508b780a",null);"function"===typeof N["default"]&&Object(N["default"])(R);var B=R.exports,Y=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("transition",{attrs:{appear:"","appear-class":"top-appear","appear-to-class":"top-appear-to","appear-active-class":"top-appear-active"}},[a("div",{staticClass:"container first-container"},[a("div",{staticClass:"row d-flex title-row"},[a("div",{staticClass:"d-flex align-items-center",staticStyle:{"min-width":"45px"}},[a("img",{attrs:{src:"/static/logo.png"}})]),a("div",{staticClass:"col-auto"},[a("div",{staticClass:"title"},[t._v(" Unisafka ")]),a("div",{attrs:{id:"title-day"}},[t._v(t._s(t.$t(t.dayText.t))+" "+t._s(t.dayText.d))])]),t.mobile?a("Dark"):t._e(),a("div",{staticClass:"ml-auto",attrs:{id:"top-links"}},[a("a",{attrs:{href:"/tty/"}},[t._v("/tty")]),t._v(" "),a("a",{attrs:{href:"/tay/"}},[t._v("/tay")]),a("a",{attrs:{href:"/tays/"}},[t._v("/tays")]),t._v(" "),a("a",{attrs:{href:"/tamk/"}},[t._v("/tamk")]),a("br"),a("a",{attrs:{href:"https://nyssetutka.fi",target:"_BLANK"}},[t._v("Nyssetutka.fi")])])],1)])])},P=[],U=(a("fb6a"),a("e08d")),F={name:"TopBar",components:{Dark:U["a"]},computed:{dayText(){var t=this.$store.state.jsonData[this.$store.state.current.dayName].dteksti||"";return t?{t:t.slice(0,2),d:t.slice(3)}:{}},mobile(){return this.$store.state.mobile}}},V=F,z=(a("fe2a"),Object(m["a"])(V,Y,P,!1,null,"e94d1934",null)),Q=z.exports,q=a("7cce");function W(){var t=document.getElementById("dot-init");null!==t&&(t.style.display="none")}a("7588"),a("d9b5");var J={name:"App",components:{StartScreen:v,TopBar:Q,Campus:B,Menu:()=>a.e("menu").then(a.bind(null,"fd76")),Footer:()=>a.e("footer").then(a.bind(null,"5a3c")),DotBouncer:q["a"]},data(){return{showFooter:!1}},watch:{lang(t){this.$root.$i18n.locale=t}},computed:{showSundayBanner(){return this.$store.state.showSundayBanner},corona(){return[12,13,14,15].includes(this.$store.state.current.week)},lang(){return this.$store.state.prefs.lang},showStartScreen(){return!this.$store.state.prefs.campus},loading(){return 0===Object.keys(this.dataNyt).length},dayErrorMsg(){return this.dataNyt.error},currentCampus(){return this.$store.state.prefs.campus},dataNyt(){return this.$store.getters.currentData},currentDay(){return this.$store.state.current.dayName}},created(){W()},mounted(){setTimeout(()=>{this.showFooter=!0},500),s["a"].addMetadata("vue","ok")}},G=J,X=(a("65f9"),a("25ef")),K=Object(m["a"])(G,o,c,!1,null,"f084bfc0",null);"function"===typeof X["default"]&&Object(X["default"])(K);var $=K.exports,Z=a("025e");function tt(){"localhost"!==window.location.hostname&&setTimeout(()=>{"serviceWorker"in navigator?(console.log("SW:CLIENT: in progress"),navigator.serviceWorker.register("/service-worker.js").then((function(){console.log("SW:CLIENT: reg complete")}),(function(){console.log("SW:CLIENT: reg failure")}))):console.log("SW:CLIENT: not supported")},2e3)}n["a"].use(r["a"]),"localhost"!==window.location.hostname&&window.TrackJS&&s["a"].install({token:"04ec886748e4440fb23bbb6d6a014583",application:"unisafka-trackjs",console:{enabled:!1}}),Object(Z["b"])(i["b"].state.prefs.dark),console.log("MODERN"),Object(Z["a"])();var et=t=>{i["b"].commit("INVALIDATE_DATA",t),i["b"].dispatch("GET_CURRENT_DAY"),i["b"].dispatch("FLUSH_CACHE"),setTimeout(()=>i["b"].dispatch("GET_ALL_DAYS"),150),setTimeout(()=>i["b"].dispatch("CHECK_SUNDAY"),1e3)};document.addEventListener("visibilitychange",()=>{"visible"===document.visibilityState&&et()});var at=window.location.href.split("/");["tty","tay","tays","tamk"].forEach(t=>{at.includes(t)&&i["b"].commit("CHOOSE_CAMPUS",t)}),et(!0);var nt=new r["a"]({locale:i["b"].state.prefs.lang||"fi",messages:{fi:{ma:"ma",ti:"ti",ke:"ke",to:"to",pe:"pe",la:"la",su:"su"},en:{ma:"Mon",ti:"Tue",ke:"Wed",to:"Thu",pe:"Fri",la:"Sat",su:"Sun"}}});new n["a"]({el:"#APP",render:t=>t($),store:i["b"],i18n:nt}),a.e("doorbell").then(a.bind(null,"c1d9")).then(t=>{var e=t.default;e.initDoorbell(i["b"].state.mobile,i["b"].state.prefs.lang)}),tt(),i["b"].commit("REVERT_PREFS"),i["b"].commit("INCREASE_VISIT_COUNT")},"5f78":function(t,e,a){},"637a":function(t,e,a){"use strict";var n=a("f554"),r=a.n(n);e["default"]=r.a},"65f9":function(t,e,a){"use strict";var n=a("18be"),r=a.n(n);r.a},7588:function(t,e,a){},"7b0f":function(t,e,a){"use strict";var n=a("8562"),r=a.n(n);e["default"]=r.a},"7c2f":function(t,e){t.exports="data:image/png;base64,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"},"7cce":function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},r=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"dot-container"},[a("div",{staticClass:"dot-bouncer"}),a("div",{staticClass:"step",attrs:{id:"s1"}}),a("div",{staticClass:"step",attrs:{id:"s2"}}),a("div",{staticClass:"step",attrs:{id:"s3"}})])}],s={name:"DotBouncer"},i=s,o=a("2877"),c=Object(o["a"])(i,n,r,!1,null,null,null);e["a"]=c.exports},"82fc":function(t,e,a){"use strict";var n=a("b7ad"),r=a.n(n);r.a},8562:function(t,e){t.exports=function(t){t.options.__i18n=t.options.__i18n||[],t.options.__i18n.push('{"fi":{"closed":"Ravintola kiinni tänään","outsideCampus":"Ravintola sijaitsee kampuksen ulkopuolella"},"en":{"closed":"Restaurant closed today","outsideCampus":"Restaurant is not located in campus area"}}'),delete t.options._Ctor}},8731:function(t,e,a){},"94af":function(t,e){t.exports=function(t){t.options.__i18n=t.options.__i18n||[],t.options.__i18n.push('{"fi":{"next":"Jipii! Seuraavan viikon ruokalistat ovat jo saatavilla. Selaa niitä vaihtamalla päivää.","corona":"Koronaviruksen vuoksi ravintoloiden ruokalistat ja aukioloajat vaihtelevat päivittäin. Osa ravintoloista myy ruokaa mukaan. Tiedot kannattaa tarkistaa ravintolan nimeä klikkaamalla."},"en":{"next":"Juhuu! Next week\'s menus are already available. You may browse them by changing the day of week.","corona":"Due to the COVID-19 situation, menus and opening times change on daily basis. Some of the restaurants also sell food to-go. Check latest info by clicking the restaurant names."}}'),delete t.options._Ctor}},"9f0e":function(t,e,a){"use strict";var n=a("8731"),r=a.n(n);r.a},b44b:function(t,e,a){},b75f:function(t,e,a){"use strict";a.d(e,"b",(function(){return n})),a.d(e,"c",(function(){return r})),a.d(e,"d",(function(){return s})),a.d(e,"f",(function(){return i})),a.d(e,"h",(function(){return o})),a.d(e,"a",(function(){return c})),a.d(e,"g",(function(){return u})),a.d(e,"e",(function(){return l}));var n='\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50" width="20px" height="20px" style="fill: #337ab7;">\n<path d="M38.288 10.297l1.414 1.415-14.99 14.99-1.414-1.414z"/>\n<path d="M40 20h-2v-8h-8v-2h10z"/>\n<path d="M35 38H15c-1.7 0-3-1.3-3-3V15c0-1.7 1.3-3 3-3h11v2H15c-.6 0-1 .4-1 1v20c0 .6.4 1 1 1h20c.6 0 1-.4 1-1V24h2v11c0 1.7-1.3 3-3 3z"/>\n</svg>',r='\n<svg version="1.1" baseProfile="basic"\nxmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="15px" height="15px"\nviewBox="0 0 32 32" xml:space="preserve">\n<path transform="matrix(0.032,0,0,0.032,0,0)" stroke="none" style="fill:#000000" d="M 1000 360 L 1000 0 L 999 0 L 748 0 L 748 0 L 639 0 L 806 167 L 499 473 L 193 167 L 360 0 L 0 0 L 0 360 L 167 193 L 473 499 L 167 806 L 0 639 L 0 1000 L 360 1000 L 193 832 L 499 526 L 806 832 L 639 1000 L 999 1000 L 1000 806 L 1000 748 L 1000 748 L 1000 639 L 832 806 L 526 499 L 832 193 z"/>\n</svg>',s='<svg width="25px" height="25px" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="cogs" class="svg-inline--fa fa-cogs fa-w-20" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path fill="#fff" d="M512.1 191l-8.2 14.3c-3 5.3-9.4 7.5-15.1 5.4-11.8-4.4-22.6-10.7-32.1-18.6-4.6-3.8-5.8-10.5-2.8-15.7l8.2-14.3c-6.9-8-12.3-17.3-15.9-27.4h-16.5c-6 0-11.2-4.3-12.2-10.3-2-12-2.1-24.6 0-37.1 1-6 6.2-10.4 12.2-10.4h16.5c3.6-10.1 9-19.4 15.9-27.4l-8.2-14.3c-3-5.2-1.9-11.9 2.8-15.7 9.5-7.9 20.4-14.2 32.1-18.6 5.7-2.1 12.1.1 15.1 5.4l8.2 14.3c10.5-1.9 21.2-1.9 31.7 0L552 6.3c3-5.3 9.4-7.5 15.1-5.4 11.8 4.4 22.6 10.7 32.1 18.6 4.6 3.8 5.8 10.5 2.8 15.7l-8.2 14.3c6.9 8 12.3 17.3 15.9 27.4h16.5c6 0 11.2 4.3 12.2 10.3 2 12 2.1 24.6 0 37.1-1 6-6.2 10.4-12.2 10.4h-16.5c-3.6 10.1-9 19.4-15.9 27.4l8.2 14.3c3 5.2 1.9 11.9-2.8 15.7-9.5 7.9-20.4 14.2-32.1 18.6-5.7 2.1-12.1-.1-15.1-5.4l-8.2-14.3c-10.4 1.9-21.2 1.9-31.7 0zm-10.5-58.8c38.5 29.6 82.4-14.3 52.8-52.8-38.5-29.7-82.4 14.3-52.8 52.8zM386.3 286.1l33.7 16.8c10.1 5.8 14.5 18.1 10.5 29.1-8.9 24.2-26.4 46.4-42.6 65.8-7.4 8.9-20.2 11.1-30.3 5.3l-29.1-16.8c-16 13.7-34.6 24.6-54.9 31.7v33.6c0 11.6-8.3 21.6-19.7 23.6-24.6 4.2-50.4 4.4-75.9 0-11.5-2-20-11.9-20-23.6V418c-20.3-7.2-38.9-18-54.9-31.7L74 403c-10 5.8-22.9 3.6-30.3-5.3-16.2-19.4-33.3-41.6-42.2-65.7-4-10.9.4-23.2 10.5-29.1l33.3-16.8c-3.9-20.9-3.9-42.4 0-63.4L12 205.8c-10.1-5.8-14.6-18.1-10.5-29 8.9-24.2 26-46.4 42.2-65.8 7.4-8.9 20.2-11.1 30.3-5.3l29.1 16.8c16-13.7 34.6-24.6 54.9-31.7V57.1c0-11.5 8.2-21.5 19.6-23.5 24.6-4.2 50.5-4.4 76-.1 11.5 2 20 11.9 20 23.6v33.6c20.3 7.2 38.9 18 54.9 31.7l29.1-16.8c10-5.8 22.9-3.6 30.3 5.3 16.2 19.4 33.2 41.6 42.1 65.8 4 10.9.1 23.2-10 29.1l-33.7 16.8c3.9 21 3.9 42.5 0 63.5zm-117.6 21.1c59.2-77-28.7-164.9-105.7-105.7-59.2 77 28.7 164.9 105.7 105.7zm243.4 182.7l-8.2 14.3c-3 5.3-9.4 7.5-15.1 5.4-11.8-4.4-22.6-10.7-32.1-18.6-4.6-3.8-5.8-10.5-2.8-15.7l8.2-14.3c-6.9-8-12.3-17.3-15.9-27.4h-16.5c-6 0-11.2-4.3-12.2-10.3-2-12-2.1-24.6 0-37.1 1-6 6.2-10.4 12.2-10.4h16.5c3.6-10.1 9-19.4 15.9-27.4l-8.2-14.3c-3-5.2-1.9-11.9 2.8-15.7 9.5-7.9 20.4-14.2 32.1-18.6 5.7-2.1 12.1.1 15.1 5.4l8.2 14.3c10.5-1.9 21.2-1.9 31.7 0l8.2-14.3c3-5.3 9.4-7.5 15.1-5.4 11.8 4.4 22.6 10.7 32.1 18.6 4.6 3.8 5.8 10.5 2.8 15.7l-8.2 14.3c6.9 8 12.3 17.3 15.9 27.4h16.5c6 0 11.2 4.3 12.2 10.3 2 12 2.1 24.6 0 37.1-1 6-6.2 10.4-12.2 10.4h-16.5c-3.6 10.1-9 19.4-15.9 27.4l8.2 14.3c3 5.2 1.9 11.9-2.8 15.7-9.5 7.9-20.4 14.2-32.1 18.6-5.7 2.1-12.1-.1-15.1-5.4l-8.2-14.3c-10.4 1.9-21.2 1.9-31.7 0zM501.6 431c38.5 29.6 82.4-14.3 52.8-52.8-38.5-29.6-82.4 14.3-52.8 52.8z"></path></svg>',i='\n<svg version="1.1" baseProfile="basic"\n   xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="32px" height="32px"\n   viewBox="0 0 32 32" xml:space="preserve"\n   style="width:17px;">\n  <path transform="matrix(0.032,0,0,0.032,0,4)" stroke="none" style="fill:#008000" d="M 996 4 C 992 0 986 0 982 3 L 314 510 L 17 296 C 13 293 7 294 4 297 C 0 301 0 306 2 310 L 302 745 C 304 747 307 749 310 749 C 310 749 310 749 311 749 C 313 749 316 748 318 746 L 996 18 C 999 14 1000 8 996 4 z"/>\n</svg>',o='\n<svg version="1.1" baseProfile="basic"\n   xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="32px" height="32px"\n   viewBox="0 0 32 32" xml:space="preserve"\n    style="width:16px;">\n  <path transform="matrix(0.032,0,0,0.032,0,2)" stroke="none" style="fill:#008000" d="M 1000 827 L 0 827 L 499 0"/>\n</svg>',c='\n<svg version="1.1" baseProfile="basic"\n   xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="32px" height="32px"\n   viewBox="0 0 32 32" xml:space="preserve"\n    style="width:16px;">\n  <path transform="matrix(0.032,0,0,0.032,0,2)" stroke="none" style="fill:#008000" d="M 0 0 L 1000 0 L 500 827"/>\n</svg>',u='\n<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24">\n<path d="M18.1 5.1c0 .3-.1.6-.3.9l-1.4 1.4-.9-.8 2.2-2.2c.3.1.4.4.4.7zm-.5 5.3h3.2c0 .3-.1.6-.4.9s-.5.4-.8.4h-2v-1.3zm-6.2-5V2.2c.3 0 .6.1.9.4s.4.5.4.8v2h-1.3zm6.4 11.7c-.3 0-.6-.1-.8-.3l-1.4-1.4.8-.8 2.2 2.2c-.2.2-.5.3-.8.3zM6.2 4.9c.3 0 .6.1.8.3l1.4 1.4-.8.9-2.2-2.3c.2-.2.5-.3.8-.3zm5.2 11.7h1.2v3.2c-.3 0-.6-.1-.9-.4s-.4-.5-.4-.8l.1-2zm-7-6.2h2v1.2H3.2c0-.3.1-.6.4-.9s.5-.3.8-.3zM6.2 16l1.4-1.4.8.8-2.2 2.2c-.2-.2-.3-.5-.3-.8s.1-.6.3-.8z"/>\n<circle cx="12" cy="11" r="4"/>\n</svg>\n',l='\n<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20">\n  <path d="M17.39 15.14A7.33 7.33 0 0 1 11.75 1.6c.23-.11.56-.23.79-.34a8.19 8.19 0 0 0-5.41.45 9 9 0 1 0 7 16.58 8.42 8.42 0 0 0 4.29-3.84 5.3 5.3 0 0 1-1.03.69z"/>\n</svg>\n'},b7ad:function(t,e,a){},d53e:function(t,e,a){var n={"./en-flag.png":"1e2d","./fi-flag.png":"7c2f"};function r(t){var e=s(t);return a(e)}function s(t){if(!a.o(n,t)){var e=new Error("Cannot find module '"+t+"'");throw e.code="MODULE_NOT_FOUND",e}return n[t]}r.keys=function(){return Object.keys(n)},r.resolve=s,t.exports=r,r.id="d53e"},d9b5:function(t,e,a){},e08d:function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"dark-picker mt-3 mr-3",class:{"mobile-dark-picker":t.mobile}},[n("img",{staticClass:"mr-2",attrs:{width:"20",src:a("d53e")("./"+("fi"===t.lang?"en":"fi")+"-flag.png")},on:{click:t.toggleLang}}),t.dark?[n("span",{staticStyle:{fill:"white"},domProps:{innerHTML:t._s(t.sun)},on:{click:t.toggle}})]:[n("span",{staticStyle:{fill:"black"},domProps:{innerHTML:t._s(t.moon)},on:{click:t.toggle}})]],2)},r=[],s=a("b75f"),i={name:"Dark",data(){return{sun:s["g"],moon:s["e"]}},computed:{mobile(){return this.$store.state.mobile},dark(){return this.$store.state.prefs.dark},lang(){return this.$store.state.prefs.lang}},methods:{toggle(){this.$store.commit("CHOOSE_SETTING","dark")},toggleLang(){this.$store.commit("SET_LANGUAGE","fi"===this.$store.state.prefs.lang?"en":"fi")}}},o=i,c=(a("25cf"),a("2877")),u=Object(c["a"])(o,n,r,!1,null,null,null);e["a"]=u.exports},f554:function(t,e){t.exports=function(t){t.options.__i18n=t.options.__i18n||[],t.options.__i18n.push('{"fi":{"oma":"Jipii! Valitsit oman kampuksen<br>Oman kampuksen sivulle voit valita mitkä tahansa ravintolat mihin tahansa järjestykseen. Aloita painamalla järjestysnappulaa yllä."},"en":{"oma":"Jipii! You chose a custom campus<br>On this custom campus view you may choose whatever restaurants you want and even order them to your liking. Start by pressing the re-ordering icon above."}}'),delete t.options._Ctor}},fe2a:function(t,e,a){"use strict";var n=a("204f"),r=a.n(n);r.a}});
//# sourceMappingURL=app.9cbe6711.js.map