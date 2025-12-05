# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License
import asyncio
import os
from functools import cache
from typing import Dict

import httpx


@cache
async def fetch_url(client: httpx.AsyncClient, url: str) -> str:
    response = await client.get(url)
    response.raise_for_status()
    return response.text


@cache
async def get_essays() -> Dict[str, str]:
    # Using the book from the `https://github.com/mungg/OneRuler` repo.
    # Learn more about OneRuler here: https://arxiv.org/abs/2503.01996
    url = "https://raw.githubusercontent.com/mungg/OneRuler/refs/heads/main/OneRuler/data/books/pt/the_book_of_disquietude_pt.txt"

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        text = await fetch_url(client, url)

    return {"text": text}


@cache
def get_all_essays() -> Dict[str, str]:
    """Synchronous wrapper for get_essays()"""
    return asyncio.run(get_essays())
