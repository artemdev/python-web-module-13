from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models import Role, User
from src.database.db import get_db
from src.schemas import ContactModel, ContactResponse
from src.repository import contacts as repository_contacts
from src.services.roles import RoleAccess
from src.services.auth import auth_service
from fastapi_limiter.depends import RateLimiter

router = APIRouter(prefix='/contacts', tags=["contacts"])

NOT_FOUND_MESSAGE = "Contact not found"

access_to_route_all = RoleAccess([Role.admin])


@router.get("/", response_model=List[ContactResponse], dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def read_contacts(skip: int = 0, limit: int = 100, name: Optional[str] = None, surname: Optional[str] = None, email: Optional[str] = None, db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    return await repository_contacts.get_contacts(skip, limit, db, user.id, name, surname, email)


@router.get("/birthdays", response_model=List[ContactResponse], dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def birthdays(db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    return await repository_contacts.get_upcoming_birthdays(db)


@router.get("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.get_contact(contact_id, user.id, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MESSAGE)
    return contact


@router.post("/", response_model=ContactResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def create_contact(body: ContactModel, db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    return await repository_contacts.create_contact(body, db)


@router.put("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def update_contact(body: ContactModel, contact_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.update_contact(contact_id, user.id, body, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MESSAGE)
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def remove_contact(contact_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.remove_contact(contact_id, user.id,  db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MESSAGE)
    return contact
