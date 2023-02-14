from sqlmodel.ext.asyncio.session import AsyncSession


class CrudBase:
    def __init__(self, session: AsyncSession):
        self.session = session
