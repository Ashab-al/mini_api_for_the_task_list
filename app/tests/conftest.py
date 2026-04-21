import sys
from pathlib import Path
import asyncio
import os

from fastapi import FastAPI

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from unittest.mock import AsyncMock
from motor.motor_asyncio import AsyncIOMotorClient


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

async def remove_response_model_in_router(router):
    """Убираем response_model из роутеров"""
    for route in router.routes:
        route.response_model = None
    return router

@pytest_asyncio.fixture
async def app(session_mock: AsyncMock) -> FastAPI:  # noqa: W0621
    """Создаем тестовый FastAPI app"""
    new_app = FastAPI()

    return new_app

@pytest_asyncio.fixture()
async def async_client(app: FastAPI):
    """Общий httpx AsyncClient для всех тестов."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
