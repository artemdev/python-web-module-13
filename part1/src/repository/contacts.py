from typing import List
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_, extract
from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, db: AsyncSession, user_id: int, name: str = None, surname: str = None, email: str = None) -> List[Contact]:
    stmt = select(Contact).where(Contact.user_id == user_id)
    if name:
        stmt = stmt.filter(Contact.first_name.contains(name))
    if surname:
        stmt = stmt.filter(Contact.last_name.contains(surname))
    if email:
        stmt = stmt.filter(Contact.email.contains(email))
    result = await db.execute(stmt.offset(skip).limit(limit))
    return result.scalars().all()


async def get_upcoming_birthdays(db: AsyncSession) -> List[Contact]:
    today = datetime.today().date()
    in_one_week = today + timedelta(days=7)
    stmt = select(Contact).filter(
        and_(
            extract('month', Contact.birthday) >= today.month,
            extract('day', Contact.birthday) >= today.day,
            extract('month', Contact.birthday) <= in_one_week.month,
            extract('day', Contact.birthday) <= in_one_week.day
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_contact(contact_id: int, user_id: int, db: AsyncSession) -> Contact:
    stmt = select(Contact).where(Contact.user_id ==
                                 user_id).filter(Contact.id == contact_id)
    result = await db.execute(stmt)
    return result.scalar_one()


async def create_contact(body: ContactModel, db: AsyncSession) -> Contact:
    contact = Contact(first_name=body.first_name,
                      last_name=body.last_name,
                      email=body.email,
                      phone=body.phone,
                      birthday=body.birthday,
                      additional_note=body.additional_note)
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def update_contact(contact_id: int, user_id: int, body: ContactModel, db: AsyncSession) -> Contact | None:
    stmt = select(Contact).where(Contact.user_id ==
                                 user_id).filter(Contact.id == contact_id)
    result = await db.execute(stmt)
    contact = result.scalar_one_or_none()
    if contact:
        contact.first_name = body.first_name,
        contact.last_name = body.last_name,
        contact.email = body.email,
        contact.phone = body.phone,
        contact.birthday = body.birthday,
        contact.additional_note = body.additional_note
        await db.commit()
    return contact


async def remove_contact(note_id: int, user_id, db: AsyncSession) -> Contact | None:
    stmt = select(Contact).where(Contact.user_id ==
                                 user_id).filter(Contact.id == note_id)
    result = await db.execute(stmt)
    contact = result.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
    return contact
