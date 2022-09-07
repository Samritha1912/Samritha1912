from bs4 import BeautifulSoup as Bs
import request
link="amazon.in/dp/B09ZBFD6TJ?pf_rd_r=T6MMBW2WBX6ZB1FMC1VJ&pf_rd_p=1d4bc0df-8144-4aea-8b04-eb09f1954bcd&pd_rd_r=77d2abae-8101-447a-b850-5ec8826be75a&pd_rd_w=vP3UZ&pd_rd_wg=COXfl&ref_=pd_gw_unk&th=1"
page=request.get(link)
page