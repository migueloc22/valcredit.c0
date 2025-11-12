-- Insertar tipos de documento
INSERT INTO tipo_documento (nombre, alias) VALUES 
('Cédula de Ciudadanía', 'CC'),
('Cédula de Extranjería', 'CE'),
('Tarjeta de Identidad', 'TI'),
('Pasaporte', 'PA'),
('NIT', 'NIT'),
('Registro Civil', 'RC');

-- Insertar tipos de usuario
INSERT INTO tipo_usuario (id, nombre, created_at, updated_at) VALUES
(1, 'cliente', '2025-11-11 20:40:52', NULL),
(2, 'admin', '2025-11-11 20:40:52', NULL);


--  -- Insertar estados
INSERT INTO "estado" ("id", "nombre", "created_at", "updated_at") VALUES
(1,	'pendiente',	'2025-11-12 11:16:09.376992-05',	NULL),
(2,	'aprobada',	'2025-11-12 11:16:23.072936-05',	NULL),
(3,	'rechazada',	'2025-11-12 11:16:45.838758-05',	NULL);