#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install autoscraper')


# In[22]:


from autoscraper import AutoScraper


# In[25]:


amazon_url="https://www.amazon.in/s?k=mi+phones+under+15000&crid=14EX6CU4S4GYA&sprefix=mi+phones+%2Caps%2C459&ref=nb_sb_ss_ts-doa-p_6_10"
wanted_list=["₹8,990","Mi Xiaomi Max (Silver, 32GB)"]


# In[26]:


scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)
print(result)


# In[28]:


scraper.get_result_similar(amazon_url,grouped=True)


# In[30]:


scraper.set_rule_aliases({'rule_ndqe':'Title','rule_rfhr':'Price'})
scraper.keep_rules(['rule_ndqe','rule_rfhr'])
scraper.save('amazon-search')


# In[33]:


final_results=scraper.get_result_similar('https://www.amazon.in/s?k=iphones&ref=nb_sb_noss',group_by_alias=True)
final_results['Title']


# In[34]:


final_results['Price']


# In[ ]:




