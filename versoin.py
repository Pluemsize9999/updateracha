from fastapi import FastAPI

app = FastAPI()

@app.get("/update")
async def root():
    return {
        "version": "1.0.0",
        "urlbanner": "https://media.discordapp.net/attachments/968059364567035904/1484192472421896383/backUi.png?ex=69bd5574&is=69bc03f4&hm=d6dcdcc62e8d2f97052666fe0742bed47787dd3afe6152d8fc5cc18328526553&=&format=webp&quality=lossless&width=413&height=232",
        "urlupdate": "https://media.discordapp.net/attachments/968059364567035904/1484192472421896383/backUi.png?ex=69bd5574&is=69bc03f4&hm=d6dcdcc62e8d2f97052666fe0742bed47787dd3afe6152d8fc5cc18328526553&=&format=webp&quality=lossless&width=413&height=232",
        "content": "ควยม่อน"
    }
