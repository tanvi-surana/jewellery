var highlightColor="#30aadc";
highlightColor="#08ECFF";

(function(){
	var expand=false;
	var interval;
	var navToggle=function(event){
		if(event.type==='click')
		{
			if(!expand)
			{
				expand=true;
				$("div.navBar div.wrapper div.sm-navPannel").css({"display":"block"});
				$(".navBar").css({"height":"400px"});
				$(".mainContent").css({"margin-top":"400px"});
				clearInterval(interval);
			}
			else
			{
				expand=false;
				$(".navBar").css({"height":"84px"});
				$(".mainContent").css({"margin-top":"84px"});
				interval=setInterval(function(){
					if(!expand)
					{
						$("div.navBar div.wrapper div.sm-navPannel").css({"display":"none"});
					}
				},1000);
			}
		}

		else if(event.type==='resize')
		{
			if(expand && window.innerWidth>935)
			{
				expand=false;
				$(".navBar").css({"height":"84px"});
				$(".mainContent").css({"margin-top":"84px"});
				$("div.navBar div.wrapper div.sm-navPannel").css({"display":"none"});
			}
		}
	}

	$(document).ready(function(){
		$("div.navBar div.wrapper div.dock ul li.more").click(function(e){
			navToggle(e);
		});

		$(window).on("orientationChange resize",function(e){
			navToggle(e);
		});
	});
})();

(function(){
	var hover=function(){
		if(window.innerWidth<935)
		{
			var pannelList=$("div.navBar .sm-navPannel .sidePannel ul .listOuter");
			for(i=0;i<pannelList.length;i++)
			{
				pannelList.eq(i).mouseenter(function(){
					var pageClass=$(pannelList[0]).parent()[0].className.split(" ")[1];
					$(this).css({"background-color":highlightColor});
					$(this).css({"border-bottom-left-radius":"4px","border-top-left-radius":"4px"});

					var hoverClass=$(this)[0].className.split(" ")[1];
					for(j=0;j<pannelList.length;j++)
					{
						var x=pannelList.eq(j)[0].className.split(" ")[1];
						if(x!==hoverClass)
						{
							pannelList.eq(j).css({"background-color":""});
						}
						if(x===pageClass)
						{
							pannelList.eq(j).css({"border-left":"4px solid "+highlightColor});
							pannelList.eq(j).css({"border-bottom-left-radius":"4px","border-top-left-radius":"4px"});
						}
						pannelList.eq(j).children("div.data").css({"display":"none"});
					}
					$(this).children("div.data").css({"display":"block"});
				});
			}
		}
	}

	var highlightSideNav=function(){
		var pannelList=$("div.navBar .sm-navPannel .sidePannel ul .listOuter");
		var pageClass=$(pannelList[0]).parent()[0].className.split(" ")[1];
		for(i=0;i<pannelList.length;i++)
		{
			var listclass=pannelList.eq(i)[0].className.split(" ")[1];
			if(pageClass===listclass)
			{
				pannelList.eq(i).css({"border-left":"4px solid "+highlightColor});
				pannelList.eq(i).css({"border-bottom-left-radius":"4px","border-top-left-radius":"4px"});
				pannelList.eq(i).children("div.data").css({"display":"block"});
			}
			else
			{
				pannelList.eq(i).css({"border-left":"4px solid transparent"});
			}
		}
	}
	$(document).ready(function(){
		highlightSideNav();
		hover();
		$(window).on("resize orientationChange",function(){
			hover();
		});
	});
})();

(function(){
	var hover=function(){
		var pannelList=$("div.navBar .nav ul div.list");
		var pageClass=$(pannelList[0]).parent()[0].className.split(" ")[1];
		for(i=0;i<pannelList.length;i++)
		{
			pannelList.eq(i).mouseenter(function(){
				for(j=0;j<pannelList.length;j++)
				{
					pannelList.eq(j).css({"border-top":"4px solid transparent"});
				}
				$(this).css({"border-top":"4px solid "+highlightColor});
				$(this).css({"box-shadow":"-2px 3px 6px rgba(0,0,0, 0.3)"});
				$(this).children("div.data").css({"display":"block"});
			});

			pannelList.eq(i).mouseleave(function(e){
				var hoverClass=$(this)[0].className.split(" ")[1];
				$(this).css({"box-shadow":""});
				$(this).children("div.data").css({"display":"none"});
				if(pageClass!==hoverClass)
				{
					$(this).css({"border-top":"4px solid transparent"});
				}
				pannelList.eq(0).parent().mouseleave(function(){
					highlightTopNav();
				});
			});
		}
	}
	var highlightTopNav=function(){
		var pannelList=$("div.navBar .nav ul div.list");
		var pageClass=$(pannelList[0]).parent()[0].className.split(" ")[1];
		for(i=0;i<pannelList.length;i++)
		{
			var listclass=pannelList.eq(i)[0].className.split(" ")[1];
			if(pageClass===listclass)
			{
				pannelList.eq(i).css({"border-top":"4px solid "+highlightColor});
				pannelList.eq(i).css({"border-top-right-radius":"4px","border-top-left-radius":"4px"});
			}
			else
			{
				pannelList.eq(i).css({"border-top":"4px solid transparent"});
				pannelList.eq(i).css({"border-top-right-radius":"4px","border-top-left-radius":"4px"});
			}
		}
	}
	$(document).ready(function(){
		highlightTopNav();
		hover();
	});
})();
