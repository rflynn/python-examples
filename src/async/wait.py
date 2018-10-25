import asyncio

async def slow_operation(n): 
    await asyncio.sleep(n) 
    print('{} Slow operation complete'.format(n))


async def main(): 
    print('main begin')
    await asyncio.wait([slow_operation(1),
                        slow_operation(2),
                        slow_operation(3)])
    print('main done')

if __name__ == '__main__':
    loop = asyncio.get_event_loop() 
    loop.run_until_complete(main())
