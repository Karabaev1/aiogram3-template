from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config

class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        # PostgreSQL ma'lumotlar bazasiga ulanish
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        # SQL so‘rovlarini bajarish uchun umumiy funksiya
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def initialize_tables(self):
        # Barcha jadvallarni yaratish
        await self.create_table_users()
        await self.create_table_user_access()


    async def create_table_users(self):
        # Users jadvali
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL,
            username VARCHAR(255),
            telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)


    async def create_table_user_access(self):
        # User Access jadvali
        sql = """
        CREATE TABLE IF NOT EXISTS user_access (
            id SERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE NOT NULL,
            is_active BOOLEAN DEFAULT TRUE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        # So'rovga kiritiladigan argumentlarni formatlash
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    # CRUD funksiyalari
    async def add_user(self, full_name, username, telegram_id):
        # Foydalanuvchini qo'shish
        sql = """
        INSERT INTO users (full_name, username, telegram_id) 
        VALUES ($1, $2, $3) 
        RETURNING *;
        """
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        # Barcha foydalanuvchilarni olish
        sql = "SELECT * FROM users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        # Foydalanuvchi ma'lumotlarini olish
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        # Foydalanuvchilar sonini hisoblash
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        # Foydalanuvchi username'ini yangilash
        sql = "UPDATE users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        # Barcha foydalanuvchilarni o'chirish
        await self.execute("DELETE FROM users WHERE TRUE", execute=True)

    async def drop_users(self):
        # Users jadvalini o'chirish
        await self.execute("DROP TABLE IF EXISTS users", execute=True)



