from service import Service
from db_builder import DbBuilder

if __name__ == "__main__":
    builder = DbBuilder()
    builder.create_database()
    service = Service()
    service.run()
