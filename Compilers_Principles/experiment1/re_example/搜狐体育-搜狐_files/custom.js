/*
* 体育的定制功能
*  @author xlx
*/
$(function(){ // 定制
	var dingzhiL = ['nba','yingchao','cba','yijia','xijia','zonghe','yaguan','f1','zhongchao','zonghe'],
		nameList = {'cba':'CBA','dejia':'德甲','f1':'F1','nba':'NBA','xijia':'西甲','yaguan':'亚冠','yijia':'意甲','yingchao':'英超','zhongchao':'中超','zonghe':'综合'},
		$custom = $('#contentG .title-cut .custom-col'),
		$sportsList = $custom.find('li.normal'),
		locked = false, // 其它选项是否锁定
		$OKBtn = $custom.find('.end input');

	
	
	function initEvent(){
		var $checkboxs = $sportsList.find('input[type=checkbox]');
		$OKBtn.click(function(){
			var cookieValue = '';
			$sportsList.each(function(i){
				var $this = $(this),
					$input = {};
				if(!$this.hasClass('end')){
					$input = $this.find('input');
					if($input[0].checked){
						cookieValue += $input.attr('inc')+',';
					}
				}
			});
			Cookie.add('usersports',cookieValue.slice(0,-1));
			alert('定制成功');
			$OKBtn.unbind('click');
			init();
		});
		
		$checkboxs.change(function(){
			var num = checkSelectNum();
			if(num >= 6 && !locked){
				$checkboxs.each(function(i){
					if(!this.checked){
						this.disabled = 'disabled';
					}
				});
				locked = true;
			}else if(locked){
				$checkboxs.each(function(){
					this.removeAttribute('disabled');
				});
				locked = false;
			}
		});
		function checkSelectNum(){ // 查看被选中的个数
			var num = 0;
			$checkboxs.each(function(i){
				if(this.checked || this.checked == 'checked'){
					num += 1;
				}
			});
			return num;
		}
	}

	var Cookie = {
		add:function(name,value){
			var v = value,
				cookiestr = '',
				time = new Date(Date.now()+365*24*3600*1000);

			cookiestr = name+'='+v+';expire='+time.toGMTString();
			document.cookie = cookiestr;
		},
		remove:function(name,value){
			var cookiestr = '';
			if(value){
				
			}else{
				cookiestr = name+'=whatever;expire='+(new Date(0)).toGMTString();
				document.cookie = cookiestr;
			}
		},
		read:function(name){
			var value = '',
				cookie = document.cookie,
				index = cookie.indexOf(name);
			if(index == -1){
				return;
			}
			var indexStart = cookie.indexOf('=',index),
				indexEnd = cookie.indexOf(';',index);
			if(indexEnd != -1){
				value = cookie.substring(indexStart+1,indexEnd);
			}else{
				value = cookie.substring(indexStart+1);
			}
			return value;
		}
	}

	function showInc(arr){ // 显示inc文件
		var $list14 = $('#contentG .list14'),
			url = 'http://sports.sohu.com/_newslist/';
			
		for(var i=0;i<6;i++){
			(function(p){
				var title = nameList[arr[p]];
				$.ajax(url+arr[p]+'.inc').done(function(inc){
					addOne(inc,p,title);
				}).fail(function(){
				
				});
			})(i)
		}

		function addOne(inc,pos,title){
			var html = "<li class='inc_title'>"+title+"</li>"+inc;
			$list14.eq(pos).find('ul').html(html);
		}
	}

	function showChecked(arr){ // 在已选的内容前打钩
		if(!arr.length){return;}
		$sportsList.each(function(i){
			var $this = $(this).find('input'),
				inc = $this.attr('inc');
			if(arr.indexOf(inc) != -1){
				$this.attr('checked',true);
				$this[0].removeAttribute('disabled');
			}else{
				$this.attr('checked',false);
				if(arr.length == 6){
					$this.attr('disabled','disabled');
					locked = true;
				}
			}
		});
	}

	function init(){
		var custom = Cookie.read('usersports'),
			custom = custom ? custom.split(',') : [],
			dingL = dingzhiL.concat([]), // dingzhiL 的一份拷贝
			finalArr = [],
			l = custom.length;

		if(!Array.prototype.indexOf){
			Array.prototype.indexOf = function(item){
				for(var i=0,l=this.length;i<l;i++){
					if(item == this[i]){
						return i;
						break;
					}
				}
				return -1; 
			}
		}

		if(l < 6){
			for(var i=0;i<l;i++){
				var ind = dingL.indexOf(custom[i]);
				dingL.splice(ind,1);
			}
		}
		finalArr = custom.concat(dingL.slice(0,(6-l)));
		showInc(finalArr);
		showChecked(custom);
		initEvent();
	}

	init();
});