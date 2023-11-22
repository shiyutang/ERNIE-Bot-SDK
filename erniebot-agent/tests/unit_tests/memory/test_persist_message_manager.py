import asyncio
import unittest

from erniebot_agent.memory import PersistentMessageManager, SlidingWindowMemory
from erniebot_agent.messages import HumanMessage

from tests.unit_tests.testing_utils import MockErnieBot


class TestSlidingWindowMemory(unittest.TestCase):
    def setUp(self):
        self.llm = MockErnieBot(None, None, None)

    # @pytest.mark.parametrize("k", [1, 2, 4, 5, 10])
    # @pytest.mark.asyncio
    def test_sliding_window_memory(self, k=3):  # asyn pytest
        async def test_sliding_window_memory(k=3):  # asyn pytest
            # The memory

            memory = SlidingWindowMemory(
                100, message_manager=PersistentMessageManager(AK="AK-123", url="not used", session_id=None)
            )

            for _ in range(k):
                # 2 times of human message
                memory.add_message(HumanMessage(content="What is the purpose of model regularization?"))

                # AI message
                message = await self.llm.async_chat(memory.get_messages())
                memory.add_message(message)
            print(
                "!!! test_sliding_window_memory_wo_sessionid, conversation output",
                memory.msg_manager.client.memory.messages,
            )

            # self.assertTrue(len(memory.get_messages()) <= k)

        asyncio.run(test_sliding_window_memory())

    def test_sliding_window_memory_with_sessionid(self, k=3):  # asyn pytest
        async def test_sliding_window_memory(k=3):  # asyn pytest
            # The memory

            memory = SlidingWindowMemory(
                100,
                message_manager=PersistentMessageManager(
                    AK="AK-124", url="not used", session_id="session-124"
                ),
            )

            for _ in range(k):
                # 2 times of human message
                memory.add_message(HumanMessage(content="What is the purpose of model regularization?"))

                # AI message
                message = await self.llm.async_chat(memory.get_messages())
                memory.add_message(message)
            print(
                "!!! test_sliding_window_memory_with_sessionid, conversation output",
                memory.msg_manager.client.memory.messages,
            )

            # self.assertTrue(len(memory.get_messages()) <= k)

        asyncio.run(test_sliding_window_memory())


if __name__ == "__main__":
    unittest.main()
