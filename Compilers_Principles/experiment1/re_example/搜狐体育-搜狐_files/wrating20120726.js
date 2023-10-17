function _getAcc()
{
	var defaultId = "860010-0626010000";
	var wratingDomains={		
		'sports.sohu.com':'860010-0601010000',
		'lottery.sports.sohu.com':'860010-0601020000',
		'2012.sohu.com':'860010-0601070000',
		'info.2012.sohu.com':'860010-0601070000',
		'london.sohu.com':'860010-0601070000',
		'nba.s.sohu.com':'860010-0601080000',
		'product.sports.sohu.com':'860010-0601080000',
		'data.sports.sohu.com':'860010-0601080000',
		'2008.sohu.com':'860010-0601090000',
		'jingcai.2008.sohu.com':'860010-0601090000',
		'stock.sohu.com':'860010-0608020000',
		'guba.stock.sohu.com':'860010-0608020000',
		'stock.business.sohu.com':'860010-0608020000',
		'hkstock.business.sohu.com':'860010-0608020000',
		'q.stock.sohu.com':'860010-0608020000',
		'business.sohu.com':'860010-0608010000',
		'money.sohu.com':'860010-0608030000',
		'fund.sohu.com':'860010-0608040000',
		'q.fund.sohu.com':'860010-0608040000',
		'news.sohu.com':'860010-0603010000',
		'comment.news.sohu.com':'860010-0603010000',
		'comment2.news.sohu.com':'860010-0603010000',
		'mil.news.sohu.com':'860010-0603020000',
		'star.news.sohu.com':'860010-0603030000',
		'weather.news.sohu.com':'860010-0603040000',
		'cul.sohu.com':'860010-0604020000',
		'astro.women.sohu.com':'860010-0604010000',
		'act1.astro.women.sohu.com':'860010-0604010000',
		'book.sohu.com':'860010-0604050000',
		'lz.book.sohu.com':'860010-0604050000',
		'yc.book.sohu.com':'860010-0604060000',
		'gd.sohu.com':'860010-0604070000',
		'green.sohu.com':'860010-0604080000',
		'dm.sohu.com':'860010-0604090000',
		'flash.dm.sohu.com':'860010-0604090000',
		'sh.sohu.com':'860010-0604100000',
		'travel.sohu.com':'860010-0604110000',
		'diy.travel.sohu.com':'860010-0604110000',
		'health.sohu.com':'860010-0604120000',
		'haodf.health.sohu.com':'860010-0604120000',
		'act1.health.sohu.com':'860010-0604120000',
		'dise.health.sohu.com':'860010-0604120000',		
		'women.sohu.com':'860010-0604010000',
		'baodian.women.sohu.com':'860010-0604010000',
		'baobao.sohu.com':'860010-0604030000',
		'chihe.sohu.com':'860010-0604130000',
		'learning.sohu.com':'860010-0604140000',
		'daxue.learning.sohu.com':'860010-0604140000',
		'englishtown.sohu.com':'860010-0604150000',
		'goabroad.sohu.com':'860010-0604160000',
		'men.sohu.com':'860010-0604170000',
		'db.auto.sohu.com':'860010-0610020000',
		'auto.sohu.com':'860010-0610010000',
		'picture.auto.sohu.com':'860010-0610010000',
		'jsp.auto.sohu.com':'860010-0610010000',
		'ucar.auto.sohu.com':'860010-0610010000',
		'price.auto.sohu.com':'860010-0610010000',
		'yule.sohu.com':'860010-0606010000',
		'music.yule.sohu.com':'860010-0606020000',
		'music.sohu.com':'860010-0606020000',
		'data.tv.sohu.com':'860010-0606050000',
		'data.yule.sohu.com':'860010-0606050000',
		'korea.sohu.com':'860010-0606060000',
		'www.helloziyi.com':'860010-0606070000',
		'digi.it.sohu.com':'860010-0611010000',
		'it.sohu.com':'860010-0611010000',
		'act.it.sohu.com':'860010-0611010000',
		'zone.it.sohu.com':'860010-0611010000',		
		'house.sohu.com':'860010-0628010000',
		'gongyi.sohu.com':'860010-0603010000',
	  'rss.news.sohu.com':'860010-0603010000',
	  'v.business.sohu.com':'860010-0608010000',
	  'money.business.sohu.com':'860010-0608010000',
	  's.sohu.com':'860010-0601010000',
	  'stats.sports.sohu.com':'860010-0601010000',
	  'csldata.sports.sohu.com':'860010-0601010000',
	  'yaoming.sports.sohu.com':'860010-0601010000',
	  'weiqi.sports.sohu.com':'860010-0601010000',
	  'xba.sports.sohu.com':'860010-0601010000',
		'cbachina.sports.sohu.com':'860010-0601010000',
		'xbam1.sports.sohu.com':'860010-0601010000',
		'2006.sohu.com':'860010-0601010000',
		'www.snookerding.com':'860010-0601010000',
		'golf.sports.sohu.com':'860010-0601010000',
		'doha2006.sohu.com':'860010-0601010000',
		'dachao.sports.sohu.com':'860010-0601010000',
		'csl.sports.sohu.com':'860010-0601010000',
		'asiancup2007.sohu.com':'860010-0601010000',
		'2004.sports.sohu.com':'860010-0601010000',
		'v.korea.sohu.com':'860010-0606010000',
		'comic.chinaren.com':'860010-0606010000',
		'changxiangaoyun.sohu.com':'860010-0606010000',
		'myway.astro.women.sohu.com':'860010-0604010000',
		'huodong.women.sohu.com':'860010-0604010000',
		'zhengxing.women.sohu.com':'860010-0604010000',
		'life.sohu.com':'860010-0604010000',
		'life.women.sohu.com':'860010-0604010000',
		'hunjia.women.sohu.com':'860010-0604010000',
		'astro.sohu.com':'860010-0604010000'
	};
	var wratingId = null;
	try{	
		var urlArray = document.location.toString().split("/");
		var domain = urlArray[2].toLowerCase();
		if(typeof(wratingDomains[domain]) != 'undefined')
		{			
			wratingId = wratingDomains[domain];
		}
		else
		{
			wratingId = vjGetOtherAcc(document.location.toString());
			if(wratingId != "")
			{
				wratingId = wratingId;
			}
			else
			{
				wratingId = defaultId;
			}
		}
	}catch(e){}
	return wratingId;
}

function vjGetOtherAcc(urlString)
{
	if(!urlString)
	{
		return "";
	}
	var otherUrlList=
	{
		'.news.sohu.com':'860010-0603010000',
		'zj.svip.sohu.com/news':'860010-0603010000',
		'zj.svip.sohu.com/gongyi':'860010-0603010000',
		'zj.svip.sohu.com/stock':'860010-0608010000',
		'.sports.sohu.com':'860010-0601010000',
		'2008.sohu.com/qiantao453':'860010-0601010000',
		'zj.svip.sohu.com/sports':'860010-0601010000',
		'2008.sohu.com/fengxingguanzhu':'860010-0601010000',
		'.2008.sohu.com':'860010-0601010000',
		'2008.sohu.com/2008bizhi':'860010-0601010000',
		'korea.sohu.com/html/silverlight':'860010-0606010000',
		'korea.sohu.com/news':'860010-0606010000',
		'korea.sohu.com/istar':'860010-0606010000',
		'korea.sohu.com/md':'860010-0606010000',
		'korea.sohu.com/vod':'860010-0606010000',
		'korea.sohu.com/enjoy':'860010-0606010000',
		'korea.sohu.com/mv':'860010-0606010000',
		'korea.sohu.com/special':'860010-0606010000',
		'zj.svip.sohu.com/yule':'860010-0606010000',
		'.yule.sohu.com':'860010-0606010000',
		'tv.sohu.com/tvad/7k7k.shtml':'860010-0606010000',
		'auto.sohu.com/goche':'860010-0610010000',
		'.auto.sohu.com':'860010-0610010000',
		'.women.sohu.com':'860010-0604010000',
		'zj.svip.sohu.com/women':'860010-0604010000',
		'.baobao.sohu.com':'860010-0604030000',
		'zj.svip.sohu.com/astro':'860010-0604010000',
		'.yc.sohu.com':"860010-0604060000"
	};
	for(var obj in otherUrlList)
	{
		if(urlString.indexOf(obj) >= 0)
		{
			return  otherUrlList[obj];
		}
	}
	return "";
}