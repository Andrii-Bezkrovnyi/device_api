from models import User, Location, Device
from config import db, logger

def db_setup():
    user1 = None
    location1 = None
    device1 = None

    with db.connection_context():
        logger.info("Creating tables ...")

        if not User.table_exists():
            logger.info("Creating User table...")
            db.create_tables([User])
            user1, created = User.get_or_create(name='User_1',
                                                email='test_user_1@example.com',
                                                password='test_password_1')

        if not Location.table_exists():
            logger.info("Creating Location table...")
            db.create_tables([Location])
            location1, created = Location.get_or_create(name='Location_1')

        if not Device.table_exists():
            logger.info("Creating Device table...")
            db.create_tables([Device])
            device1, created = Device.get_or_create(
                name='Test Device_1',
                type='Test Type_1',
                login='test_login_1',
                password="test_password_1",
                location=location1,
                api_user=user1
            )

        logger.info("Tables checked/created successfully!")

        if user1:
            logger.info(f"User table is created: {user1.id}, {user1.name}")

        if location1:
            logger.info(f"Location table is created: {location1.id}, {location1.name}")

        if device1:
            logger.info(f"Device table is created: {device1.id}, {device1.name}, {device1.type}")
