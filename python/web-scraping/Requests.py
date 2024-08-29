import requests

url1 = "https://www.google.com/"
url2 = 'https://www.lightinthebox.com/he/p/adults-women-s-cosplay-retro-medieval-dress-cosplay-costume-for-party-halloween-festival-polyster-halloween-carnival-masquerade-dress_p7596584.html?edmdiscountkey=a0010862f59c05f6deab75beeea76391&litb_from=newsletter&user_email=9dc700ce8c89a8fb5604f0b7544129ce9b658929db68d025&crm_features=&mname=he_nl_L20230128_1_M_US128_&p_id=0&c_id=0&send_date=2023012814&utm_source=crm&utm_content=newsletter&utm_medium=newsletter&utm_campaign=LITB20230128US128&content=Product&country_code=US&currency=USD'
url3 = "https://www.amazon.com/PINECIL-%D7%9E%D7%9C%D7%97%D7%9D-%D7%9E%D7%99%D7%A0%D7%99-%D7%A0%D7%99%D7%99%D7%93-%D7%97%D7%9B%D7%9D/dp/B096X6SG13/ref=pd_rhf_d_ee_s_pd_crcd_sccl_1_2/147-7057278-1801918?pd_rd_w=nz0Rb&content-id=amzn1.sym.840d50bc-9f73-460b-8793-15925b0bb70e&pf_rd_p=840d50bc-9f73-460b-8793-15925b0bb70e&pf_rd_r=RHFR6185PRJTX2DHWJTZ&pd_rd_wg=BDbW2&pd_rd_r=0836b360-f62e-41fc-b564-9b03e83ee398&pd_rd_i=B096X6SG13&psc=1"
url4 = "https://elastic.co/downloads/elasticsearch"

#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

#response = requests.get(url3, headers=headers)
response = requests.get(url4)

webpage = response.content

print(webpage)

print(response.headers)

for key, value in response.headers.items():
    print(key, ':', value)
    
print(response.request.headers)

print(response.status_code)
