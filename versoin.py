from fastapi import FastAPI

app = FastAPI()

@app.get("/update")
async def root():
    return {
        "version": "1.0.0",
        "urlbanner": "https://media.discordapp.net/attachments/968059364567035904/1484192472421896383/backUi.png?ex=69bd5574&is=69bc03f4&hm=d6dcdcc62e8d2f97052666fe0742bed47787dd3afe6152d8fc5cc18328526553&=&format=webp&quality=lossless&width=413&height=232",
        "urlupdate": "https://media.discordapp.net/attachments/1236760642741080124/1239929741805490177/sdsdsds.png?ex=69bd490f&is=69bbf78f&hm=78af2fb910cb79ba30666acf0b237a3141b6e9861922678da5d14ef683344edf&=&format=webp&quality=lossless&width=641&height=481",
        "content": "ควยม่อน"
    }