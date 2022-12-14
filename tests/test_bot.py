import pytest
from deltachat_rpc_client import AttrDict, events

from faqbot import hooks
from faqbot.orm import init


@pytest.mark.asyncio
async def test_bot(tmp_path, acfactory):
    path = tmp_path / "sqlite.db"
    await init(f"sqlite+aiosqlite:///{path}", True)
    bot = await acfactory.get_unconfigured_bot()
    bot.add_hooks(hooks)
    snapshot1 = AttrDict(text="hello")
    await bot._on_event(snapshot1, events.NewMessage)
