--SQLite
INSERT INTO cleanup_settings VALUES
("Kitchen",	0, FALSE, 4, 8),
("Bathroom 2", 2, FALSE, 1, 3),
("Bathroom 3", 3, FALSE, 1, 3),
("Deckbrush 0+2", 2, TRUE, 0, 2),
("Deckbrush 1+3", 3, TRUE, 0, 2),
("Brojo/Brolo", 0, TRUE, 0, 1),
("Study/Laundry", 0, TRUE, 0, 1),
("0 Deck", 0, FALSE, 2, 4),
("1 Deck", 0, FALSE, 2, 4),
("Stairs and Halls", 0, FALSE, 2, 4);

DELETE FROM users;