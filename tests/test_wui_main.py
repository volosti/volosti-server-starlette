import pytest
from httpx import AsyncClient

from volosti_server_starlette.app import app


@pytest.mark.anyio
async def test_main_page() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.text == 'volosti-server-starlette'
