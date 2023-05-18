## Fetching Html from all the links

import asyncio
import aiohttp

# the following code is needed to run code in Jupyter else there will be "event loop error"
import nest_asyncio
nest_asyncio.apply()
#.......................................#

all_links = ['https://www.tes.com/jobs/vacancy/headteacher-suffolk-1754682']
htmls = []

try:
    async def main():
           async_count = 0
           try:
               async with aiohttp.ClientSession() as session:
                     for link in all_links:
                                   async_count += 1
                                   print(async_count)
                                
                                   async with session.get(link) as response:
                                                  html = await response.text()
                                                  htmls.append(html)
            except Exception as e:
                        print(e)

     loop = asyncio.get_event_loop()
     loop.run_until_complete(main())

except Exception as e:
        print(e)
print("\n\ntotal Scraped :", len(htmls))
