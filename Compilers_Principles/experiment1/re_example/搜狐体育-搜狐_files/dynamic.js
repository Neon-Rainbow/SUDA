(function($){
	/*
	* @des ��̬Ч���� ʹ��ȫ�ֱ���SOHU_MDC_PU ������Ӧ����
	* @author xuluxi
	*/
	window.SOHU_MDC_PU = {
		'autoScroll':autoScroll,
		'changeTab':changeTab,
		'drag':drag,
		'pictureScroll':pictureScroll,
		'pictureScroll2':pictureScroll2,
		'pictureSlide':pictureSlide,
		'backToTop':backToTop,
		'alertOldIE':alertOldIE
		};
	/*
		�õ�Ƭ�ֻ��ӿ�  start
		����˵��:{
			'slideOuter' : '�����õ�Ƭ�����������',
			'picList' : '��ʾ�������б�',
			'interval' : 'һ�ι���ʱ��',
			'showCount' : '��ʾ����',
			'scrollDirec' : '�������� true : ���¹��� �� false : ���ҹ���',
			'auto' : '�Զ����� true || false',
			'stayTime' : '����Զ�����Ϊtrue,��Ҫ�趨�Զ�����ʱÿ���õ�Ƭ��ͣ��ʱ�䣨���룩',
			'scrollRound' : 'ͼƬѭ���޼�϶�ֲ� true || false'
		
		}
	*/
	function autoScroll(arg){
		var outer = arg.slideOuter,
			sli = outer.find('.scroll-auto li'),
			conr = outer.find('.scroll-con'),
			lisr = arg.picList,
			btns = {'up':outer.find('.scroll-btns .up'),'down':outer.find('.scroll-btns .down')},
			ts = arg.interval || 500,
			unit = arg.showCount,
			ft = arg.scrollDirec || false,
			auto = arg.auto || false,
			stayTime = arg.stayTime,
			scrollRound = arg.scrollRound,
			autoTimeId = 0,
			ableClick = true,
			picListLength = lisr.length,
			btnPr = btns.up,
			btnNr = btns.down,
			cls = "now";
		var ff = ft||false;
		var st = stayTime||5000;
		if (lisr.length <= 1) return;

		if(scrollRound){
			conr.append(conr.html());
			var pnumr = unit, numr = lisr.length*2;
		}else{
			var pnumr = unit, numr = lisr.length;
		}
		
		
		if(numr <= pnumr) {
			btnPr.hide();
			btnNr.hide();
			if(sli){sli.hide();}
			return;
		}
		
		var owr = lisr[1].offsetLeft - lisr[0].offsetLeft, 
			idxArear = [0, numr - pnumr],
			idxr = 0;

		if(ff){
			owr = lisr[1].offsetTop - lisr[0].offsetTop;
			}
		
		function updateNum(n){
			if(!scrollRound){if (n > idxArear[1] || n < idxArear[0]) {ableClick = true;return;}}
			clearInterval(autoTimeId);
			btnPr[((n == 0)?'add':'remove') + 'Class']('uN');
			btnNr[((n == idxArear[1])?'add':'remove') + 'Class']('dN');
			
			idxr = n;
			if(ff){
				conr.stop().animate({top: -n * owr},ts,function(){
					ableClick = true;
					if(auto==true){
						autoTimeId = window.setInterval(function(){
						ableClick = false;
						scoll()
						},st);
					}
				});
			}else{
				if(n == -1){
					n = picListLength-1;
					idxr = n;
					conr.css('left',-picListLength * owr);
				}
			

				conr.stop().animate({left: -n * owr},ts,function(){
					if(n == picListLength){
						conr.css('left','0px');
						idxr = 0;
					};
					ableClick = true;
					if(auto==true){
						autoTimeId = window.setInterval(function(){
							ableClick = false;
							scoll()
						},st);
					}
				});
			}
			if(sli){sli.removeClass(cls).eq(n).addClass(cls);}
		}
		
		var scoll = function(){
			if(idxr == picListLength){
				conr.css('left','0px');
				idxr = 0;
			}
			if (idxr < idxArear[1]){
				btnPr[((idxr == -1)?'add':'remove') + 'Class']('uN');
				btnNr[((idxr == (idxArear[1]-1))?'add':'remove') + 'Class']('dN');
				if(ff){
					conr.stop().animate({top: owr * -(++idxr)},ts,function(){ableClick = true});
				}else{
					conr.stop().animate({left: owr * -(++idxr)},ts,function(){ableClick = true});
				}
				if(sli){sli.removeClass(cls).eq(idxr).addClass(cls)};
			}
			idxr = idxr>=idxArear[1] ? idxr=-1 : idxr;
		}
		
		if(sli){
			if($.browser.msie && $.browser.version == '6.0'){
				sli.each(function(ii){
					$(this).click(function(ev){
						updateNum(ii);
						return false;
					});
				});
			}else{
				sli.each(function(ii){
					$(this).hover(function(ev){
						updateNum(ii);
						return false;
					});
				});
	
			}
		}
		
		btnPr.click(function(ev){
			if(!ableClick){return;}
			ableClick = false;
			updateNum(idxr - 1);
			return false;
		});
		btnNr.click(function(ev){
			if(!ableClick){return;}
			ableClick = false;
			updateNum(idxr + 1);
			return false;
		});

		if(auto==true){
			autoTimeId = window.setInterval(function(){
				ableClick = false;
				scoll()
			},st);
		}
	};
	/*
		�õ�Ƭ�ֻ��ӿ�  end
	*/

	/*
		��ǩ��������л�Ч���ӿ�
		����˵����{
			tabList : ��������������������л���list���������class now �Ƴ�ɾ��class now ��jQueryѡ����ѡ��
			conList : ���������list��tabList������ͬ�� ��jQueryѡ����ѡ��
			startPosition : ��ʼչ��λ��
			tabOuter : tabList�ĸ���Ԫ�أ�ÿ���л�tab���ı�tabOuter��class
			tabClass : ÿ���л�tab���ı�tabOuter��class��classֵΪtabClass����������֣����ּ�Ϊ���㿪ʼ�����tabλ��
		}
	*/
  function changeTab(arg){
		var tabList = arg.tabList,conList = arg.conList,startPosition = arg.startPosition,tabOuter = arg.tabOuter,tabClass = arg.tabClass;
		if(tabClass){
			var nowClass = tabClass+startPosition;
		}
		tabList.each(function(i){
			var $this = $(this);
			$this.mouseenter(function(){
				tabList.removeClass('now');
				$this.addClass('now');
				conList.hide();
				conList.eq(i).show();
				if(tabOuter){
					tabOuter.removeClass(nowClass);
					tabOuter.addClass(tabClass+i);
					nowClass = tabClass+i;
				}
			})
		});
	
		tabList.eq(startPosition).mouseenter();
		if(tabOuter){tabOuter.addClass(nowClass);}
  };
  /*
   �����ק��� 
    ����˵����{dragbar:����ק����,
			   content:������ק������ contentӦ����dragbar�ĸ���Ԫ��
			   }
  */
  function drag(arg){
		var myDrag = arg.dragbar,
		    content = arg.content;
		var startPos = false,
			startX = 0,
			startY = 0,
			divLeft = 0,
			divTop = 0,
			mouseDown = false;

		myDrag.mousedown(function(){
			mouseDown = true;
		})
		$('body').mouseup(function(){
			mouseDown = false;
			startPos = false;
		})

		$('body').mousemove(function(e){
		if(!mouseDown){return};
			if(!startPos){
				startX = e.clientX;
				startY = e.clientY;
				divLeft = parseInt(content.position().left);
				divTop = parseInt(content.position().top);
				startPos = true;
			}else{
				content.css('left',(divLeft+(e.clientX-startX))+'px');
				content.css('top',(divTop+(e.clientY-startY))+'px');
			}
		})
	}
	/*
		ͼƬ��ά�ֻ��ӿ� ��ʾ3��ͼƬ
		����˵����
		{
			'outerId' : 'p1_picRockPlayer', // �����������ⲿid
			'className' : 'box', // ÿ����ʾ��������class
			'width' : 140, // ��ʾ���ݵĿ�ȣ�px��
			'outerWidth' : 195, // �ⲿ��ʾ����Ŀ�� (px)
			'height' : 180 // ��ʾ���ݵĸ߶�(px)
		}
	*/

	function pictureScroll(obj){
		new picScroll(obj).init();
	};
	function picScroll(obj){
		obj.scrollList = $('#'+obj.outerId+' .'+obj.className);
		obj.leftBtn = $('#'+obj.outerId+' .turn-btns .btn-l');
		obj.rightBtn = $('#'+obj.outerId+' .turn-btns .btn-r');
		$.extend(this,obj);
		this.length = this.scrollList.length;
		this.left = (this.outerWidth - this.width)/2;
		this.ltop = this.height/8;
		this.lleft = (this.outerWidth-(this.width*0.75));
		this.pos = 0;
	}

	picScroll.prototype = {
		init : function(){
			var that = this;
			that.positionPic();
			that.addEvent();
		},
		positionPic : function(){
			var that = this;
			that.scrollList.eq(0).css({'left':that.left+'px','z-index':'102','width':that.width,'height':that.height});
			that.scrollList.eq(1).css({'left':that.lleft+'px','top':that.ltop+'px','width':(that.width*0.75)+'px','height':(that.height*0.75)+'px','z-index':'100','opacity':'0.6'}).attr('pos','right').bind('click',function(e){that._picClick(e,that)});
			that.scrollList.eq(that.length-1).css({'left':0,'top':that.ltop+'px','width':(that.width*0.75)+'px','height':(that.height*0.75)+'px','z-index':'100','opacity':'0.6'}).attr('pos','left').bind('click',function(e){that._picClick(e,that)});

			that.scrollList.each(function(i){
				if(i==0 || i==1 || i == (that.length-1)){
					return;
				}else{
					this.style.display = 'none';
				}
			});

			that.scrollList.eq(0).find('h5').show();
		},
		addEvent : function(){
			var that = this;
			that.leftBtn.click(function(){
				var nowpos = 0,
					nextPic = null,  // Ŀǰ��ʾ�ұ�
					prePic = null,  // Ŀǰ��ʾ���
					nowPic = null,  // Ŀǰ��ʾ
					preparePic = null; // ׼��

				if(that.pos == 0){
					nextPic = that.scrollList.eq(1);
					prePic = that.scrollList.eq(that.length - 1);
					nowPic = that.scrollList.eq(0);
					preparePic = that.scrollList.eq(2);
					that.pos += 1;
				}else if(that.pos == that.length - 2){
					nextPic = that.scrollList.eq(that.length - 1);
					prePic = that.scrollList.eq(that.length - 3);
					nowPic = that.scrollList.eq(that.length - 2);
					preparePic = that.scrollList.eq(0);
					that.pos += 1;
				}else if(that.pos == that.length - 1){
					nextPic = that.scrollList.eq(0);
					prePic = that.scrollList.eq(that.length - 2);
					nowPic = that.scrollList.eq(that.length - 1);
					preparePic = that.scrollList.eq(1);
					that.pos = 0;
				}else{
					nextPic = that.scrollList.eq(that.pos+1);
					prePic = that.scrollList.eq(that.pos-1);
					nowPic = that.scrollList.eq(that.pos);
					preparePic = that.scrollList.eq(that.pos+2);
					that.pos += 1;
				}

				that._picFadein(nextPic);
				that._picFadeout(nowPic,'left');
				that._picHide(prePic);
				that._picShow(preparePic,'right');
				
			});
			that.rightBtn.click(function(){
				var nowpos = 0,
					nextPic = null,  // Ŀǰ��ʾ�ұ�
					prePic = null,  // Ŀǰ��ʾ���
					nowPic = null,  // Ŀǰ��ʾ
					preparePic = null; // ׼��

				if(that.pos == 0){
					nextPic = that.scrollList.eq(1);
					prePic = that.scrollList.eq(that.length - 1);
					nowPic = that.scrollList.eq(0);
					preparePic = that.scrollList.eq(that.length - 2);
					that.pos = that.length - 1;
				}else if(that.pos == 1){
					nextPic = that.scrollList.eq(2);
					prePic = that.scrollList.eq(0);
					nowPic = that.scrollList.eq(1);
					preparePic = that.scrollList.eq(that.length - 1);
					that.pos -= 1;
				}else if(that.pos == that.length - 1){
					nextPic = that.scrollList.eq(0);
					prePic = that.scrollList.eq(that.length - 2);
					nowPic = that.scrollList.eq(that.length - 1);
					preparePic = that.scrollList.eq(that.length - 3);
					that.pos -= 1;
				}else{
					nextPic = that.scrollList.eq(that.pos+1);
					prePic = that.scrollList.eq(that.pos-1);
					nowPic = that.scrollList.eq(that.pos);
					preparePic = that.scrollList.eq(that.pos-2);
					that.pos -= 1;
				}

				that._picFadein(prePic);
				that._picFadeout(nowPic,'right');
				that._picHide(nextPic);
				that._picShow(preparePic,'left');
			});
		
		},
		_picFadein : function(ele){
			var that = this;
			ele.animate({
				top:'0',
				left:that.left+'px',
				width : that.width+'px',
				height : that.height+'px'
			});
			ele.css({'z-index':'102','opacity':'1'}).find('h5').show();
			ele.unbind('click').attr('pos','');
		},
		_picFadeout : function(ele,position){
			var that = this;
				ele.animate({
					left:position == 'left'?'0':that.lleft+'px',
					top : that.ltop+'px',
					width:(that.width*0.75)+'px',
					height : (that.height*0.75)+'px'
				})
			ele.attr('pos',position)
			ele.css({'z-index':'100','opacity':'0.6'}).find('h5').hide();
			ele.bind('click',function(e){that._picClick(e,that)});
		},
		_picHide : function(ele){
				ele.hide();
		},
		_picShow : function(ele,position){
			var that = this;
				var left = position == 'left' ? 0 : that.lleft;
				ele.css({'width':(that.width*0.75)+'px','height':(that.height*0.75)+'px','top':that.ltop+'px','left':left+'px','z-index':'100','opacity':'0.6'});
				ele.show().attr('pos',position).click('click',function(e){that._picClick(e,that)});;
		},
		_picClick : function(e,that){
			var $target = $(e.target).closest('.box');
			if($target.attr('pos') == 'left'){
				that.rightBtn.trigger('click');
			}else if($target.attr('pos') == 'right'){
				that.leftBtn.trigger('click');
			}
			e.preventDefault();
		}
	};
	/*
		ͼƬ��ά�ֻ��ӿ� ��ʾ5��ͼƬ
		����˵����
		{
			'outerId' : 'p1_picRockPlayer', // �����������ⲿid
			'className' : 'box', // ÿ����ʾ��������class
			'width' : 140, // ��ʾ���ݵĿ�ȣ�px��
			'outerWidth' : 195, // �ⲿ��ʾ����Ŀ�� (px)
			'height' : 180 // ��ʾ���ݵĸ߶�(px)
		}
	*/
	function pictureScroll2(obj){
		new picScroll2(obj).init();
	}
	function picScroll2(obj){
		this.scrollList = $('#'+obj.outerId+' .'+obj.className),
		this.leftBtn = $('#'+obj.outerId+' .turn-btns .btn-l'),
		this.rightBtn = $('#'+obj.outerId+' .turn-btns .btn-r'),
		this.n = this.scrollList.length,
		this.ableClick = true; // ���ҷ�ҳ��ť�Ƿ�ɵ����־λ

		this.scrollList.hide();  // ����������������

		this.littleWidth = obj.width*0.75;
		this.littleHeight = obj.height*0.75;
		this.littlerWidth = obj.width*0.5;
		this.littlerHeight = obj.height*0.5;
		$.extend(this,obj);

		this.a = null;
		this.b = null;
		this.c = null;
		this.d = null;
		this.e = null;  // �ֱ��ʾ��ʾ����������

	};

	picScroll2.prototype = {	
		init : function(){
			var n = this.n,
				scrollList = this.scrollList;

			this.a = scrollList.eq(n-2);
			this.b = scrollList.eq(n-1);
			this.c = scrollList.eq(0);
			this.d = scrollList.eq(1);
			this.e = scrollList.eq(2);
			this.a.num = n-2;
			this.e.num = 2;
			
			this.a.css({'width':this.littlerWidth,'height':this.littlerHeight,'left':0,'top':this.height*0.25,'display':'','z-index':100}); this.a.find('img').animate({'opacity':0.4},500);
			this.b.css({'width':this.littleWidth,'height':this.littleHeight,'left':this.width*0.25,'top':this.height*0.125,'display':'','z-index':101}); this.b.find('img').animate({'opacity':0.6},500);
			this.c.css({'width':this.width,'height':this.height,'left':(this.outerWidth-this.width)*0.5,'top':0,'display':'','z-index':102}).find('h5').show();
			this.d.css({'width':this.littleWidth,'height':this.littleHeight,'left':(this.outerWidth -this.littleWidth - this.width*0.25),'top':this.height*0.125,'display':'','z-index':101});  this.d.find('img').animate({'opacity':0.6},500);
			this.e.css({'width':this.littlerWidth,'height':this.littlerHeight,'left':this.outerWidth - this.littlerWidth,'top':this.height*0.25,'display':'','z-index':100});   this.e.find('img').animate({'opacity':0.4},500);

			this.event();
		},
		event : function (){
			var that = this;
			that.rightBtn.click(function(){
				if(!that.ableClick){return;}
				that.ableClick = false;
				that.e.fadeOut(500);
				that.d.animate({
					'left':that.outerWidth - that.littlerWidth,
					'top':that.height*0.25,
					'width':that.littlerWidth,
					'height':that.littlerHeight
				},500,function(){this.style.zIndex = 100});
				that.d.find('img').animate({'opacity':0.4},500)
				that.c.animate({
					'left':(that.outerWidth -that.littleWidth - that.width*0.25),
					'top':that.height*0.125,
					'width':that.littleWidth,
					'height':that.littleHeight
				},500,function(){$(this).find('h5').hide();this.style.zIndex = 101});
				that.c.find('img').animate({'opacity':0.6},500)
				that.b.animate({
					'left':(that.outerWidth-that.width)*0.5,
					'top':0,
					'width':that.width,
					'height':that.height
				},500,function(){$(this).find('h5').show();this.style.zIndex = 102});
				that.b.find('img').animate({'opacity':1},500)
				that.a.animate({
					'left':that.width*0.25,
					'top':that.height*0.125,
					'width':that.littleWidth,
					'height':that.littleHeight
				},500,function(){that.ableClick = true;this.style.zIndex = 101});
				that.a.find('img').animate({'opacity':0.6},500)
				var eNum = that.e.num;
				that.e = that.d;
				that.d = that.c;
				that.c = that.b;
				that.b = that.a;
				that.e.num = eNum == 0 ? that.n-1 : (eNum - 1)
				if(that.a.num == 0){
					that.a = that.scrollList.eq(that.n - 1);
					that.a.num = that.n-1;
				}else{
					var num = that.a.num;
					that.a = that.scrollList.eq(num - 1);
					that.a.num = num - 1;
				}
				if(that.n == 5){
					setTimeout(function(){
						that.a.show();
						that.a.css({'width':that.littlerWidth,'height':that.littlerHeight,'left':0,'top':that.height*0.25,'z-index':100});
						that.a.find('img').css('opacity','0.4');
					},550);
				}else{
					that.a.css({'width':that.littlerWidth,'height':that.littlerHeight,'left':0,'top':that.height*0.25,'z-index':100});
					that.a.find('img').css('opacity','0.4');
					that.a.fadeIn(500);
				}

			});
			that.leftBtn.click(function(){
				if(!that.ableClick){return;}
				that.ableClick = false;
				that.a.fadeOut(500);
				that.b.animate({
					'left':0,
					'top':that.height*0.25,
					'width':that.littlerWidth,
					'height':that.littlerHeight
				},500,function(){this.style.zIndex = 100});
				that.b.find('img').animate({'opacity':0.4},500);
				that.c.animate({
					'left':that.width*0.25,
					'top':that.height*0.125,
					'width':that.littleWidth,
					'height':that.littleHeight
				},500,function(){$(this).find('h5').hide();this.style.zIndex = 101});
				that.c.find('img').animate({'opacity':0.6},500);
				that.d.animate({
					'left':(that.outerWidth-that.width)*0.5,
					'top':0,
					'width':that.width,
					'height':that.height
				},500,function(){$(this).find('h5').show();this.style.zIndex = 102});
				that.d.find('img').animate({'opacity':1},500);
				that.e.animate({
					'left':(that.outerWidth -that.littleWidth - that.width*0.25),
					'top':that.height*0.125,
					'width':that.littleWidth,
					'height':that.littleHeight
				},500,function(){that.ableClick = true;this.style.zIndex = 101});
				that.e.find('img').animate({'opacity':0.6},500);
				
				var aNum = that.a.num;
				that.a = that.b;
				that.b = that.c;
				that.c = that.d;
				that.d = that.e;

				that.a.num = aNum == that.n-1 ? 0 : (aNum + 1)
				if(that.e.num == that.n-1){
					that.e = that.scrollList.eq(0);
					that.e.num = 0;
				}else{
					var num = that.e.num;
					that.e = that.scrollList.eq(num + 1);
					that.e.num = num + 1;
				};
				if(that.n == 5){
					setTimeout(function(){
						that.e.show();
						that.e.css({'width':that.littlerWidth,'height':that.littlerHeight,'left':that.outerWidth - that.littlerWidth,'top':that.height*0.25,'z-index':100});that.e.find('img').css('opacity',0.4);
					},550);
				}else{	
					that.e.css({'width':that.littlerWidth,'height':that.littlerHeight,'left':that.outerWidth - that.littlerWidth,'top':that.height*0.25,'z-index':100});that.e.find('img').css('opacity',0.4);
					that.e.fadeIn(500);
				}
			});
		  }
		};

	/*
		��������ʽͼƬչʾ
		����˵����
		{
			outerId : 'slider', // ���������id
			className : 'slide', // ÿ��չʾ���class 
			width : 300,  // ͼƬ��
			height : 450, // ͼƬ��
			showTitle : true   // չʾ��չ�����Ƿ���ʾ���� ��Ĭ��Ϊtrue��
		}
	*/

	function pictureSlide(obj){
			var id = obj.outerId;
			var className = obj.className;
			var showTitle = obj.showTitle == undefined ? true : obj.showTitle;
		
			var $slider = $("#"+id);
			var sbody = $slider.width();
			var n = $("#"+id+" ."+className), 
				nn = sbody / n.size();
			n.hover(function(){
				if(showTitle){
					$(this).find("div:last > a > span").removeClass("space");
					$(this).siblings().find("div:last > a > span").addClass("space");
				}else{
					$(this).find("div:last > a > span").hide();
					$(this).siblings().find("div:last > a > span").show();
				}
				$(this).find("div:last > a > em").show();
				$(this).siblings().find("div:last > a > em").hide();
			});

			n.each(function(i){
				var $this = $(this);
				$this.css({
					"left": (nn * i) + "px",
					"cursor": "pointer"
				}).bind("mouseover", {
					ni: (i + 1)
				}, function(s){
					var ss = 0;
					n.stop();
					
					n.each(function(j){
						var $this = $(this);
						if (j > 0 && j == s.data.ni) {
							ss = $this.width() - (Math.floor((sbody - $this.width()) / (n.size() - 1)));
						}

						$this.animate({
							left: (Math.floor((sbody - $this.width()) / (n.size() - 1))) * j + ss + "px"
						}, "normal");
						
					});
					return false;
				});
				
				$this.find("img").css({
					display: "block",
					width:obj.width+'px',
					height:obj.height+'px',
					border:"1px solid #fff",
					borderRight:"0px"
				})
				var textHeight = $this.find(".backgroundText").height();
				$this.find(".text").css({
					top: (obj.height - textHeight + 15)+"px"
				})
				$this.find(".backgroundText").css({
					top: (obj.height - textHeight)+"px"
				});
			}).eq(0).trigger("mouseover");
			
		};

	/*
	 * �ص�����
	*/
	function backToTop(id){ 
		var htop=document.getElementById(id);
		htop.style.display="none";
		htop.onclick = function(){
			rollTo(0)
		}
		function eventhandler(type,func,bol){
			if(window.addEventListener){
				window.addEventListener(type,func,bol);
			}
			else{
				window.attachEvent('on'+type,func);
			}
		}
		eventhandler('scroll',st,false);
		function st(){		
			var sh=window.pageYOffset||document.documentElement.scrollTop||document.body.scrollTop;
			if(sh>10){
				htop.style.display="block";
			}
			else{
				htop.style.display="none";
			}
		}

		window.rollInterval=null;
		window.rollTo=function(y){
		var max_scroll=Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)-document.body.clientHeight;
		var target_y=y<max_scroll?y:max_scroll;
		target_y=target_y>0?target_y:0;
		   if(rollInterval)
		   {
				clearInterval(rollInterval);
		   }
		rollInterval=setInterval(function(){
		 var current_y=document.documentElement.scrollTop + document.body.scrollTop;
		 
		if(Math.abs(current_y-target_y)>10)
		{
			window.scrollTo(0,current_y+(target_y-current_y)/10);
		}else
		{
		   window.scrollTo(0,target_y);
		  clearInterval(rollInterval);
		}
		},2);
		};
	};

	 /* 
	    �ж��Ƿ���IE 6,7 ���������ʾ�汾����

	 */

	function alertOldIE(){
		//util.removeCookie('alertIE');
		if(!$.browser.msie){
			return;
		}
		if($.browser.version != '6.0' && $.browser.version != '7.0'){
			return;
		}

		var ieCookie = util.getCookie('alertIE');
		if(ieCookie && ieCookie == 'alert'){
			return;
		}

		var htmlStr = '<div id="alertoldie">'+
		'<div class="close"></div>'+
		'<h3>����������汾���ͣ�Ϊ��֤���Ч��</h3>'+
		'<p>��������<a href="http://windows.microsoft.com/zh-cn/internet-explorer/ie-10-worldwide-languages" target="_blank">IE</a>�߰汾��<a href="http://www.google.cn/intl/zh-CN/chrome/browser/" target="_blank">Chrome</a>��<a href="http://www.firefox.com.cn/download/" target="_blank">FireFox</a>��������²鿴ҳ��</p>'+
		'<div class="continue"></div>'+
		'</div><div id="graybackground"></div>';

		$('body').append(htmlStr);

		var clientWidth = document.documentElement.clientWidth || document.body.clientWidth;
		var clientHeight = document.documentElement.clientHeight || document.body.clientHeight;
		var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;

		$('html').css('overflow','hidden');

		var $popUp = $('#alertoldie'),
			$graybackground = $('#graybackground'),
			closeBtn = $popUp.find('.close'),
			continueBtn = $popUp.find('.continue');

		$popUp.css({
			'left':(clientWidth*0.5-232)+'px',
			'top':(clientHeight*0.5-103)+'px'
		});

		closeBtn.click(close);
		continueBtn.click(close);
		function close(){
			$popUp.remove();
			$('#graybackground').remove();
			$('html').css('overflow','auto');
			util.setCookie('alertIE','alert',99999);
		};
	
	}
	
		
	/*
	*   ����������	
	*/
	var util = {
		getCookie : function(name){
			var cookieStr = document.cookie;
			var cookieArr = cookieStr.split(';');
			for(var i=0,l=cookieArr.length;i<l;i++){
				var arr = cookieArr[i].split('=');
				arrName = this.removeBlank(arr[0]);
				if(arrName == name){
					return arr[1];
				}
			}
		},
		setCookie : function(name,val,expireHours){
			var date = new Date();
			if(expireHours){
				var expTime = expireHours*3600*1000;
				date.setTime(date.getTime()+expTime);
				document.cookie = name+'='+escape(val)+';expires='+date.toGMTString();
			}else{
				document.cookie = name+'='+escape(val);
			}
	
		},
		removeCookie : function(name){
			document.cookie = name+'=;expires='+new Date(0).toGMTString();
		},
		removeBlank : function(str){ // ȥ���ַ����еĿհ׷�
			var newStr = str.replace(/\s/g,'');
			return newStr;
		}
	};
})(jQuery)