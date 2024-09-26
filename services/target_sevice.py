from config.base import session_factory


def convert_target_to_json(target_model):
    with session_factory() as session:
        target = session.merge(target_model)
        return {
            "id": target.id,
            "target_id": target.target_id,
            "city_name": target.city.name if target.city else None,
            "type_name": target.target_type.name if target.target_type else None,
            "industry_name": target.industry.name if target.industry else None,
            "location_latitude": target.location.latitude if target.location else None,
            "location_longitude": target.location.longitude if target.location else None,
            "priority": target.priority,
        }