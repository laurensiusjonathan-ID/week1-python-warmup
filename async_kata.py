import asyncio, time
 
async def fetch_result(source: str) -> str:      # pass 1
    await asyncio.sleep(1)
    return f"data from {source}"
 
async def main() -> None:                        # pass 2: 5 concurrent
    t = time.perf_counter()
    out = await asyncio.gather(*[fetch_result(f"s{i}") for i in range(5)])
    print(len(out), "results in", round(time.perf_counter()-t, 2), "s")
 
asyncio.run(main())

#=============================================================================

SEM = asyncio.Semaphore(5)  # limit concurrent fetches to 5
 
async def fetch_limited(source: str) -> str:
    async with SEM:
        print(f"{time.perf_counter():.1f}s start {source}")
        return await fetch_result(source)

# in main(): gather fetch_limited for range(10)  → ~4s total, waves of 3
async def main() -> None:                        # pass 2: 5 concurrent
    t = time.perf_counter()
    out = await asyncio.gather(*[fetch_limited(f"s{i}") for i in range(10)])
    print(len(out), "results in", round(time.perf_counter()-t, 2), "s")

asyncio.run(main())

