-- ADMIN USER
INSERT INTO User (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$g9tE4jRAwNFKDdQrB/FCTOC57xxa8gHg4l0KEt8rFbE3hJhxYm1Ue',
    TRUE
);

-- AMENITIES
INSERT INTO Amenity (id, name)
VALUES 
    ('9ecf2db7-67ea-4f79-9914-1938c2a1a9ce', 'WiFi'),
    ('f2daabcf-b0d9-4f65-9df0-cde93cb92d8b', 'Swimming Pool'),
    ('1e81d5c4-5f9b-4f5a-92a9-efbaee290e6b', 'Air Conditioning');

