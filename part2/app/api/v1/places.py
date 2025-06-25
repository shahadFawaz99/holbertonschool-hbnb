def to_dict(self, include_owner=False, include_amenities=False):
    data = {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'price': self.price,
        'latitude': self.latitude,
        'longitude': self.longitude,
        'owner_id': self.owner.id if self.owner else None,
    }

    if include_owner and self.owner:
        data['owner'] = {
            'id': self.owner.id,
            'first_name': self.owner.first_name,
            'last_name': self.owner.last_name,
            'email': self.owner.email
        }

    if include_amenities:
        data['amenities'] = [
            {
                'id': amenity.id,
                'name': amenity.name
            } for amenity in self.amenities
        ]

    return data

