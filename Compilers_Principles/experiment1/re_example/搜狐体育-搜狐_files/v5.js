document.pv = new Array();
function sendPv(url){
    var _a=new Image();
    _a.src=url;
    document.pv.push(_a);
}
function getA(name){
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r!=null) return unescape(r[2]); return '11962';
}
function show(ads){
	if(Object.prototype.toString.apply(ads) === '[object Array]'){
		var l =  ads.length;
		var index = parseInt(Math.random()*l);
		var ad = ads[index];
	}else{
		var ad = ads;
	}
    if(typeof(ad.file)=="undefined")return; 
    if(typeof(ad.click)=="undefined" || ad.click =='' ) return; 
    if( ad.file.indexOf('.swf')>0 ){
        var sohuFlash2 = new sohuFlash(ad.file,"_default",width,height,"7");
        sohuFlash2.addParam("quality", "high");
        sohuFlash2.addParam("wmode", "opaque");
        sohuFlash2.write('contain');
    }else{
        
        document.getElementById("contain").innerHTML ='<img  width="'+width+'" height="'+height+'" border=0 src="'+ad.file+'"/>';
    }

    var adiv = document.getElementById("click");
    var d =  document.getElementById("click-img");
    var d1 =  document.getElementById("contain");
    d.style.width = width+'px';d1.style.width = width+'px';
    d.style.height= height+'px'; d1.style.height= height+'px';
    adiv.href = ad.click;
    var pid = getA('pid');
    var key = ad.key || '30q1d000r0000000q2R000q79';key = key==''?'30q1d000r0000000q2R000q79':key;
    var url = 'http://i.go.sohu.com/count/c?aid='+key+'&apid=beans_'+pid+'&impid=null&at=0&mkey='+key+'&latcy=0&rsln=null&ref=null&ax=null&ay=null&cx=null&cy=null&ctlk=null&ctrlt=null&ctrln=null&freq=-1&ipos=0&sf=1&c=&e=&ext=default_click&r='+new Date().getTime();

    adiv.onclick= function(){
        sendPv(url);
    };
    if("imp" in ad){
        sendPv(ad.imp);
    }
    url_p =  'http://i.go.sohu.com/count/v?aid='+key+'&apid=beans_'+pid+'&impid=null&at=0&mkey='+key+'&latcy=0&rsln=null&ref=null&ax=null&ay=null&cx=null&cy=null&ctlk=null&ctrlt=null&ctrln=null&freq=-1&ipos=0&sf=1&c=&e=&ext=default_click&r='+new Date().getTime();
    sendPv(url_p);
};