from returns.maybe import Maybe, Nothing
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from models import Target


def insert_target(target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_target_by_id(target_id: int) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Target, target_id))

def delete_target(target_id: int) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(target_id)
            if maybe_target is Nothing:
                return Failure(f"No target with the ID - {target_id}")
            target_to_delete = maybe_target.unwrap()
            session.delete(target_to_delete)
            session.commit()
            return Success(target_to_delete)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def update_target(target_id: int, updated_target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(target_id)
            if maybe_target is Nothing:
                return Failure(f"No target with the ID - {target_id}")
            target_to_update = maybe_target.unwrap()
            target_to_update.target_id = updated_target.target_id
            target_to_update.city_id = updated_target.city_id
            target_to_update.target_type_id = updated_target.target_type_id
            target_to_update.target_industry_id = updated_target.target_industry_id
            target_to_update.location_id = updated_target.location_id
            target_to_update.priority = updated_target.priority
            session.commit()
            session.refresh(target_to_update)
            return Success(target_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))
