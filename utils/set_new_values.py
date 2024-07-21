import json
import asyncio


async def get_appointment_first(driver):
    await asyncio.sleep(15)
    for attempt in range(5):
        for request in driver.requests:
            if request.response:
                if request.response.status_code == 200 and 'appointments' in request.url and '25.json' in request.url:
                    response_body = request.response.body.decode('utf-8')
                    data = json.loads(response_body)
                    dates = [item['date'] for item in data]
                    if dates:
                        print(dates)
                        return dates
                    break
        await asyncio.sleep(1)
    return None


async def get_hour_first(driver):
    await asyncio.sleep(15)
    for attempt in range(5):
        for request in driver.requests:
            if request.response:
                if request.response.status_code == 200 and 'date' in request.url and '25.json' in request.url:
                    response_body = request.response.body.decode('utf-8')
                    data = json.loads(response_body)
                    if 'available_times' in data:
                        times = [time for time in data['available_times']]
                        print(times)
                        return times
                    break
        await asyncio.sleep(1)
    return None


async def get_appointment_second(driver, new_date, new_time):
    await asyncio.sleep(15)
    for attempt in range(5):
        for request in driver.requests:
            if request.response:
                if request.response.status_code == 200 and 'appointments' in request.url and '26.json' in request.url and new_date in request.url and new_time in request.url:
                    response_body = request.response.body.decode('utf-8')
                    data = json.loads(response_body)
                    dates = [item['date'] for item in data]
                    if dates:
                        print(dates)
                        return dates
                    break
        await asyncio.sleep(1)
    return None


async def get_hour_second(driver, new_date, new_time):
    await asyncio.sleep(15)
    for attempt in range(5):
        for request in driver.requests:
            if request.response:
                if request.response.status_code == 200 and 'date' in request.url and 'times' in request.url and '26.json' in request.url and new_date in request.url and new_time in request.url:
                    response_body = request.response.body.decode('utf-8')
                    data = json.loads(response_body)
                    if 'available_times' in data:
                        times = [time for time in data['available_times']]
                        print(times)
                        return times
                    break
        await asyncio.sleep(1)
    return None
