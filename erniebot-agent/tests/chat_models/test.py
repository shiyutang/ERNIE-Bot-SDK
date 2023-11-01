import asyncio

from erniebot_agent.chat_models.erniebot import ERNIEBot
from erniebot_agent.message import HumanMessage, AIMessage

async def test_ernie_bot(model='ernie-bot-turbo', stream=False):
    api_type = 'aistudio'
    access_token = '1a76642806d7ccb26c8f6412c83450254ac9d680'
    eb = ERNIEBot(model=model, api_type=api_type, access_token=access_token)
    messages = [
        HumanMessage(content="我在深圳，周末可以去哪里玩？"),
    ]
    res = await eb.async_chat(messages, stream=stream)
    if not stream:
        print(res)
    else:
        async for chunk in res:
            print(chunk)

if __name__ == '__main__':
    asyncio.run(test_ernie_bot(stream=False))
    asyncio.run(test_ernie_bot(stream=True))