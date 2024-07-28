from aiohttp import web
from models import Device, Location, User
from config import logger

async def index(request):
    return web.Response(text='Server is started')

async def get_all_devices(request):
    logger.info('Get all devices')

    try:
        devices = Device.select()
        devices_list = [
            {
                'id': device.id,
                'name': device.name,
                'type': device.type,
                'login': device.login,
                'password': device.password,
                'location_id': device.location.id,
                'api_user_id': device.api_user.id
            } for device in devices
        ]

        logger.info(f'Get {len(devices_list)} devices')
        return web.json_response(devices_list)

    except Exception as exc:
        logger.error(f'Failed to get devices: {exc}')
        return web.json_response({'error': 'Failed to get devices!'}, status=500)

async def get_device_by_id(request):
    device_id = request.match_info.get('id')
    logger.info(f'Get device by id: {device_id}')

    try:
        device = Device.get(Device.id == device_id)
        logger.info(f'Get device: {device.id}')
        return web.json_response(Device.current_device_info(device))

    except Device.DoesNotExist:
        logger.warning(f'Device {device_id} not found')
        return web.json_response({'error': 'Device not found!'}, status=404)

async def post_device(request):
    data = await request.json()
    logger.info(f'Get data for creating device: {data}')

    try:
        if not all(key in data for key in ['name', 'type', 'login', 'password', 'location_id', 'api_user_id']):
            raise ValueError('Missing required fields!')

        if not Location.select().where(Location.id == data['location_id']).exists():
            raise ValueError('Invalid location_id!')

        if not User.select().where(User.id == data['api_user_id']).exists():
            raise ValueError('Invalid api_user_id')

        device = Device.create(
            name=data['name'],
            type=data['type'],
            login=data['login'],
            password=data['password'],
            location=data['location_id'],
            api_user=data['api_user_id']
        )
        logger.info(f'Device {device.id} is created')
        return web.json_response(Device.current_device_info(device))

    except ValueError as err:
        logger.error(f'Error value: {err}')
        return web.json_response({'error': str(err)}, status=400)

    except Exception as err:
        logger.error(f'Error creating device: {err}')
        return web.json_response({'error': f'Error creating device: {err}'}, status=500)

async def update_device(request):
    device_id = request.match_info.get('id')
    data = await request.json()
    logger.info(f'Update device {device_id} to data {data}')

    try:
        if not all(key in data for key in ['name', 'type', 'login', 'password', 'location_id', 'api_user_id']):
            raise ValueError('Missing required fields!')

        if not Location.select().where(Location.id == data['location_id']).exists():
            raise ValueError('Invalid location_id!')

        if not User.select().where(User.id == data['api_user_id']).exists():
            raise ValueError('Invalid api_user_id!')

        device_query = Device.update(
            name=data['name'],
            type=data['type'],
            login=data['login'],
            password=data['password'],
            location=data['location_id'],
            api_user=data['api_user_id']
        ).where(Device.id == device_id)
        updated = device_query.execute()

        if updated:
            updated_device = Device.get(Device.id == device_id)
            logger.info(f'Update device {device_id} is success')

            return web.json_response(Device.current_device_info(updated_device))
        else:
            logger.warning(f'Device not found for update: {device_id}')
            return web.json_response({'error': 'Device not found'}, status=404)

    except ValueError as err:
        logger.error(f'Error update device: {err}')
        return web.json_response({'error': str(err)}, status=400)

    except Exception as err:
        logger.error(f'Exception  update device: {err}')
        return web.json_response({'error': 'Exception  update device'}, status=500)

async def patch_device_by_id(request):
    device_id = request.match_info.get('id')
    data = await request.json()
    logger.info(f'Patching device {device_id} via data: {data}')

    try:
        updates = {}
        if 'name' in data:
            updates['name'] = data['name']
        if 'type' in data:
            updates['type'] = data['type']
        if 'login' in data:
            updates['login'] = data['login']
        if 'password' in data:
            updates['password'] = data['password']
        if 'location_id' in data:
            if not Location.select().where(Location.id == data['location_id']).exists():
                raise ValueError('Invalid location_id!')
            updates['location'] = data['location_id']
        if 'api_user_id' in data:
            if not User.select().where(User.id == data['api_user_id']).exists():
                raise ValueError('Invalid api_user_id')
            updates['api_user'] = data['api_user_id']

        if not updates:
            logger.warning(f'Invalid fields for patching device {device_id}')
            return web.json_response({'error': 'Invalid fields for patching device'}, status=400)

        query = Device.update(**updates).where(Device.id == device_id)
        updated = query.execute()

        if updated:
            updated_device = Device.get(Device.id == device_id)
            logger.info(f'Patched device {device_id} success')
            return web.json_response(Device.current_device_info(updated_device))
        else:
            logger.warning(f'Device {device_id} not found for patching')
            return web.json_response({'error': 'Device not found'}, status=404)

    except ValueError as err:
        logger.error(f'ValueError patching device {device_id}: {err}')
        return web.json_response({'error': str(err)}, status=400)

    except Exception as err:
        logger.error(f'Error patching device {device_id}: {err}')
        return web.json_response({'error': 'Exception while patching device'}, status=500)

async def delete_device(request):
    device_id = request.match_info.get('id')
    logger.info(f'Delete device {device_id}')

    try:
        query = Device.delete().where(Device.id == device_id)
        deleted = query.execute()

        if deleted:
            logger.info(f'Device {device_id} is deleted')
            return web.json_response({'message': 'Device deleted successfully'})
        else:
            logger.warning(f'Device {device_id} not found for delete')
            return web.json_response({'error': 'Device not found'}, status=404)

    except Exception as err:
        logger.error(f'Error delete device {device_id}: {err}')
        return web.json_response({'error': 'Exception while deleting device'}, status=500)

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/devices/', get_all_devices)
    app.router.add_get('/devices/{id}/', get_device_by_id)
    app.router.add_post('/devices/', post_device)
    app.router.add_put('/devices/{id}/', update_device)
    app.router.add_patch('/devices/{id}/', patch_device_by_id)
    app.router.add_delete('/devices/{id}/', delete_device)
