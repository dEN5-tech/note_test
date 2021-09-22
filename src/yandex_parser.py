import re
import time
from random import choice
import requests
import json
from bs4 import BeautifulSoup as bs

type_img_d= {
	"gif":"gifan",
	"png":"png",
	"jpg":"jpg"

}

type_img_size= {
	"Большие":"large",
	"Средние":"medium",
	"Маленькие":"small"

}

def get_req_img_whith_yandex(query_mn,start_=0,limit=1,type_="choice",add_page = True):
	img_size,type_img,recent = False,False,False
	headers = {
		'authority': 'yandex.ru',
		'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
		'device-memory': '4',
		'rtt': '250',
		'sec-ch-ua-mobile': '?0',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
		'viewport-width': '791',
		'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
		'x-requested-with': 'XMLHttpRequest',
		'dpr': '1',
		'downlink': '4.6',
		'ect': '4g',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-mode': 'cors',
		'sec-fetch-dest': 'empty',
		'referer': 'https://yandex.ru/images/search?from=tabbar&text=google%20search%20api',
		'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
		'cookie': 'yandexuid=1656658121627748886; is_gdpr=0; is_gdpr_b=CNuvQhCMPSgC; mda=0; yandex_gid=47; yuidss=1656658121627748886; ymex=1943281930.yrts.1627921930; gdpr=0; _ym_uid=1627921929389168988; font_loaded=YSv1; yabs-frequency=/5/00020000002bD0nX/xFboS9G0000eGY40/; my=YwA=; L=cgBqXEteYXkIUmFJaVV0fXZ/aXBXXlFYNzwvGUYbKAsV.1628413571.14691.359285.54149c8c4c01121b8b6e6d04fb2fb80b; yandex_login=twist.mas; i=lBKPw0MJ87nk53YzGgUCz+4kRB2Ea8Nroexu9+2ehmDVh1fiUS4cqRo3nD182MfeHmbbispw491bNV/CGOPRnBRTK2A=; Session_id=3:1628676515.5.0.1628413571717:hi1tWQ:2a.1|888287499.-1.2.1:189654856|3:239043.803375.rk3U96tP19VVQQMbau3BJvQYeNQ; sessionid2=3:1628676515.5.0.1628413571717:hi1tWQ:2a.1|888287499.-1.2.1:189654856|3:239043.803375.rk3U96tP19VVQQMbau3BJvQYeNQ; tuid=a:d8727723e3c055094b006a4226755b62a9ce317c946a8ef62467b5c6a851087b; Bismuth=1; computer=1; ys=udn.cDpNQVNURVIgVFdJU1Q%3D#vbch.2-35-0#wprid.1628846326454594-1673560982647130327-vla1-1886-vla-l7-balancer-prod-8080-BAL-65#c_chck.2975178627; lsq=google%20search%20api; _yasc=5ZmPesKO+l58urL8iml5IBOQWrpxYoRhWBWLXmGSDfwBCWHMJe4uP4O4; yp=1944917131.sp.aflt%3A1628693131#1628965240.zlgn_smrt.1#1629019508.gpauto.56_279039999999995%3A44_0139776%3A115341%3A3%3A1628846708#1660379523.p_cl.1628843522#1628965005.mcl.irflfd#1630513927.ygu.1#1943773571.udn.cDpNQVNURVIgVFdJU1Q%3D#1628960347.mct.null#1631438711.los.1#1660379380.p_sw.1628843379#1628960347.mcv.0#1628960347.szm.1%3A1366x768%3A791x625#1631438711.losc.0#1659705474.ln_tp.01#1629105260.clh.2063711#1631525140.csc.1#1628933379.nps.640319500%3Aclose',
	}
	list_links = []
	list_dict = []
	iter = 0
	iter+=start_
	start = time.monotonic()
	end = float()
	pager = []

	while add_page:
		params = [
			('format', 'json'),
			('request', '{"blocks":[{"block":"extra-content","params":{},"version":2},{"block":"serp-controller","params":{},"version":2},{"block":"serp-list_infinite_yes","params":{"initialPageNum":0},"version":2},{"block":"more_direction_next","params":{},"version":2},{"block":"gallery__items:ajax","params":{},"version":2}],"metadata":{"bundles":{"lb":"jCgK5?b*G$Xvb>:BUOR$"},"assets":{"las":"justifier-height=1;thumb-underlay=1;justifier-setheight=1;fitimages-height=1;justifier-fitincuts=1;react-with-dom=1;ca993f.0=1;d30d05.0=1;105ac6.0=1;bed1df.0=1"},"version":"0x0f74f9d0500","extraContent":{"names":["i-react-ajax-adapter"]}},"bmt":{"lb":"jCgK5?b*G$Xvb>:BUOR$"},"amt":{"las":"justifier-height=1;thumb-underlay=1;justifier-setheight=1;fitimages-height=1;justifier-fitincuts=1;react-with-dom=1;ca993f.0=1;d30d05.0=1;105ac6.0=1;bed1df.0=1"}}'),
			('yu', '1656658121627748886'),
			('p', iter),
			('from', 'tabbar'),
			('text', query_mn),
			('rpt', 'image'),
			('serpid', 'a7tbQ4lJOYyrChOZD000iQ'),
			('serpListType', 'horizontal'),
			('thumbSnippet', '0'),

		]
		if type_img:
			params.append(("itype",type_img_d[type_img]))
		if recent:
			params.append(("recent","7D"))
		if img_size:
			try:
				params.append(("isize",type_img_size[img_size]))
			except:
				size_offset = [("isize","eq"),("iw",img_size[0]),("ih",img_size[1])]
				for i in size_offset:
					params.append(i)


		response = requests.get('https://yandex.ru/images/search', headers=headers, params=params)
		json_data = json.dumps(response.text)
		json_without_slash = json.loads(json_data)
		try:
			data_json = json.loads(json_without_slash)["blocks"][2]['html']
		except json.decoder.JSONDecodeError:
			break
		soup = bs(data_json, 'html.parser')
		list_json = soup.find_all("div", class_=re.compile("serp-item serp-item_type_search serp-item_group_search serp-item_pos_.* serp-item_scale_yes justifier__item i-bem"))
		list_links_t = []
		for i in list_json:
			items = i.get("data-bem")
			item = json.loads(items)
			serp_item = item["serp-item"]
			list_links.append(serp_item["preview"][0]["url"])
			list_links_t.append(serp_item["preview"][0]["url"])
			list_dict.append(serp_item)
		if limit>1:
			iter+=1
		print(iter)
		pager.append({f"{iter}":list_links_t})

		if iter==limit+start_:
			print(iter)
			end =  time.monotonic()
			break
		print(len(list_links))
	print(len(list_links),end-start) 
	if type_=="all":
		return list_links
	if type_=="choice":
		return choice(list_links)
	if type_=="dic_ch":
		return choice(list_dict)
	if type_=="p_dict":
		return pager
	if type_=="choice_byte":
		return requests.get(choice(list_links),stream=True).raw